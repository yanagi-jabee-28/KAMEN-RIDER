from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field, model_validator


class Act(BaseModel):
    id: str
    label: str


class Resources(BaseModel):
    max_kakkon: int = Field(ge=1)
    max_jonetsu: int = Field(ge=1)
    cost_mult_min: float = Field(ge=1.0)
    cost_mult_max: float = Field(ge=1.0)

    @model_validator(mode="after")
    def validate_cost_mult(self) -> "Resources":
        if self.cost_mult_max < self.cost_mult_min:
            raise ValueError("cost_mult_max must be >= cost_mult_min")
        return self


class CoreConstants(BaseModel):
    title: str
    acts: List[Act]
    resources: Resources


class StoryFlag(BaseModel):
    id: str
    label: str
    enabled: bool


class StoryFlags(BaseModel):
    flags: List[StoryFlag]


class Character(BaseModel):
    id: str
    display_name: str
    role: str
    first_act: int = Field(ge=1, le=5)
    domains: List[str]
    fixed_gear: List[str]


class Characters(BaseModel):
    characters: List[Character]


class Skill(BaseModel):
    id: str
    display_name: str
    owner_id: str
    cost_kakkon: int = Field(ge=0)
    cost_jonetsu: int = Field(ge=0)
    durability_cost: int = Field(ge=0)
    tags: List[str]


class Skills(BaseModel):
    skills: List[Skill]


class Rule(BaseModel):
    expression: str
    notes: str


class BattleRules(BaseModel):
    rules: dict[str, Rule]
    legacy_terms: List[str]


class CampLevels(BaseModel):
    default: int = Field(ge=0)
    joined_act2: int = Field(ge=0)
    field_lv2_unlocked: int = Field(ge=0)


class BaseLevels(BaseModel):
    default: int = Field(ge=0)
    joined_act2: int = Field(ge=0)
    shrine_lv3_unlocked: int = Field(ge=0)


class Levels(BaseModel):
    camp: CampLevels
    base: BaseLevels


class Constraints(BaseModel):
    can_use_kintsugi_min_level: int = Field(ge=0)
    can_use_tsukumogami_min_level: int = Field(ge=0)
    can_use_mythic_forging_min_level: int = Field(ge=0)


class MaintenanceRules(BaseModel):
    levels: Levels
    constraints: Constraints
