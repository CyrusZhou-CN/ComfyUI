from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, confloat


class StabilityFormat(str, Enum):
    png = 'png'
    jpeg = 'jpeg'
    webp = 'webp'


class StabilityAspectRatio(str, Enum):
    ratio_1_1 = "1:1"
    ratio_16_9 = "16:9"
    ratio_9_16 = "9:16"
    ratio_3_2 = "3:2"
    ratio_2_3 = "2:3"
    ratio_5_4 = "5:4"
    ratio_4_5 = "4:5"
    ratio_21_9 = "21:9"
    ratio_9_21 = "9:21"


def get_stability_style_presets(include_none=True):
    presets = []
    if include_none:
        presets.append("None")
    return presets + [x.value for x in StabilityStylePreset]


class StabilityStylePreset(str, Enum):
    _3d_model = "3d-model"
    analog_film = "analog-film"
    anime = "anime"
    cinematic = "cinematic"
    comic_book = "comic-book"
    digital_art = "digital-art"
    enhance = "enhance"
    fantasy_art = "fantasy-art"
    isometric = "isometric"
    line_art = "line-art"
    low_poly = "low-poly"
    modeling_compound = "modeling-compound"
    neon_punk = "neon-punk"
    origami = "origami"
    photographic = "photographic"
    pixel_art = "pixel-art"
    tile_texture = "tile-texture"


class StabilityStableUltraRequest(BaseModel):
    prompt: str = Field(...)
    negative_prompt: Optional[str] = Field(None)
    aspect_ratio: Optional[str] = Field(None)
    seed: Optional[int] = Field(None)
    output_format: Optional[str] = Field(StabilityFormat.png.value)
    image: Optional[str] = Field(None)
    style_preset: Optional[str] = Field(None)
    strength: Optional[confloat(ge=0.0, le=1.0)] = Field(None)


class StabilityStableUltraResponse(BaseModel):
    image: Optional[str] = Field(None)
    finish_reason: Optional[str] = Field(None)
    seed: Optional[int] = Field(None)

