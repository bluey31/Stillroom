"""
Patient encoder — transforms clinical records into model-ready tensors.

A preview file for the Stillroom palette, exercising every pigment across
common Python surfaces: imports, types, decorators, dataclasses, f-strings,
exceptions, match statements, and nn.Module subclassing.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

import torch
from torch import Tensor, nn


# TODO: wire this to the production config
# FIXME: temporary constants — should come from the dispensary service
DEFAULT_EMBED_DIM = 768
MAX_SEQUENCE_LEN = 2048
ICD_PATTERN = re.compile(r"^[A-Z]\d{2}(\.\d{1,3})?$")


class PatientError(Exception):
    """Raised when a patient record fails validation."""


@dataclass(frozen=True)
class Patient:
    """A patient record before encoding."""

    mrn: str
    age: int = 0
    diagnoses: list[str] = field(default_factory=list)
    active: bool = True
    sex: Literal["F", "M", "X"] = "X"

    def __post_init__(self) -> None:
        if not self.mrn.isdigit():
            raise PatientError(f"mrn must be digits, got {self.mrn!r}")
        for code in self.diagnoses:
            if not ICD_PATTERN.match(code):
                raise PatientError(f"invalid ICD-10 code: {code!r}")

    @property
    def severity(self) -> float:
        return len(self.diagnoses) / 10.0


class PatientEncoder(nn.Module):
    """Encodes a batch of patients into dense embeddings."""

    def __init__(
        self,
        embed_dim: int = DEFAULT_EMBED_DIM,
        vocab_size: int = 30_000,
        num_heads: int = 12,
        dropout: float = 0.1,
    ) -> None:
        super().__init__()
        self.embed_dim = embed_dim
        self.token_embed = nn.Embedding(vocab_size, embed_dim)
        self.attn = nn.MultiheadAttention(
            embed_dim, num_heads, dropout=dropout, batch_first=True
        )
        self.norm = nn.LayerNorm(embed_dim)

    @torch.no_grad()
    def embed(self, tokens: Tensor) -> Tensor:
        return self.token_embed(tokens)

    def forward(self, tokens: Tensor, mask: Tensor | None = None) -> Tensor:
        x = self.embed(tokens)
        attn_out, _ = self.attn(x, x, x, key_padding_mask=mask)
        return self.norm(x + attn_out)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(embed_dim={self.embed_dim})"


def risk_tier(patient: Patient) -> str:
    """Classify risk using a match statement."""
    match patient.severity:
        case s if s < 0.2:
            return "low"
        case s if s < 0.5:
            return "moderate"
        case _:
            return "high"


def load_cohort(path: Path) -> list[Patient]:
    if not path.exists():
        raise FileNotFoundError(f"cohort not found: {path}")

    patients: list[Patient] = []
    for line in path.read_text().splitlines():
        if not line or line.startswith("#"):
            continue
        mrn, age_str, *codes = line.split("\t")
        try:
            patient = Patient(mrn=mrn, age=int(age_str), diagnoses=list(codes))
        except PatientError as err:
            print(f"skipping malformed record: {err}")
            continue
        patients.append(patient)

    return patients


def main() -> None:
    cohort = load_cohort(Path("data/cohort.tsv"))
    encoder = PatientEncoder(embed_dim=512, num_heads=8)

    print(f"loaded {len(cohort)} patients, encoder={encoder!r}")

    for patient in cohort[:3]:
        tier = risk_tier(patient)
        print(f"  mrn={patient.mrn}: tier={tier}")

    tokens = torch.randint(0, 30_000, (4, 128))
    embeddings = encoder(tokens)

    assert embeddings.shape == (4, 128, 512), "shape mismatch"
    assert not torch.isnan(embeddings).any(), "NaN in embeddings"


if __name__ == "__main__":
    main()
