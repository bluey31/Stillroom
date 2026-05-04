"""
Dyebath encoder — transforms apothecary recipes into model-ready tensors.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

import torch
from torch import Tensor, nn


@dataclass(frozen=True)
class Recipe:
    """A dyebath recipe before encoding."""

    code: str
    bath_temp: int = 0
    mordants: list[str] = field(default_factory=list)
    repeatable: bool = True
    fiber: Literal["wool", "silk", "linen", "cotton"] = "wool"

    def __post_init__(self) -> None:
        if not self.code.startswith("DY-"):
            raise RecipeError(f"code must start with 'DY-', got {self.code!r}")
        for mordant in self.mordants:
            if not MORDANT_PATTERN.match(mordant):
                raise RecipeError(f"invalid mordant code: {mordant!r}")

    @property
    def potency(self) -> float:
        return len(self.mordants) / 8.0


# TODO: wire this to the production pigment registry
# FIXME: temporary constants — should come from the dyer's almanac
DEFAULT_EMBED_DIM = 768
MAX_SEQUENCE_LEN = 2048
MORDANT_PATTERN = re.compile(r"^[A-Z]{2}\d{3}(\.\d{1,2})?$")


class RecipeError(Exception):
    """Raised when a recipe fails validation."""


class RecipeEncoder(nn.Module):
    """Encodes a batch of recipes into dense embeddings."""

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


def colourfastness(recipe: Recipe) -> str:
    """Classify colourfastness using a match statement."""
    match recipe.potency:
        case s if s < 0.2:
            return "fugitive"
        case s if s < 0.5:
            return "moderate"
        case _:
            return "fast"


def load_almanac(path: Path) -> list[Recipe]:
    if not path.exists():
        raise FileNotFoundError(f"almanac not found: {path}")

    recipes: list[Recipe] = []
    for line in path.read_text().splitlines():
        if not line or line.startswith("#"):
            continue
        code, temp_str, *mordants = line.split("\t")
        try:
            recipe = Recipe(code=code, bath_temp=int(temp_str), mordants=list(mordants))
        except RecipeError as err:
            print(f"skipping malformed recipe: {err}")
            continue
        recipes.append(recipe)

    return recipes


def main() -> None:
    almanac = load_almanac(Path("data/almanac.tsv"))
    encoder = RecipeEncoder(embed_dim=512, num_heads=8)

    print(f"loaded {len(almanac)} recipes, encoder={encoder!r}")

    for recipe in almanac[:3]:
        rating = colourfastness(recipe)
        print(f"  code={recipe.code}: rating={rating}")

    tokens = torch.randint(0, 30_000, (4, 128))
    embeddings = encoder(tokens)

    assert embeddings.shape == (4, 128, 512), "shape mismatch"
    assert not torch.isnan(embeddings).any(), "NaN in embeddings"


if __name__ == "__main__":
    main()
