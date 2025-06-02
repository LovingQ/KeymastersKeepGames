from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


# Option Dataclass
@dataclass
class FinalFantasyTacticsAdvanceArchipelagoOptions:
    pass

# Main Class
class FinalFantasyTacticsAdvanceGame(Game):
    name = "Final Fantasy Tactics Advance Keep"
    platform = KeymastersKeepGamePlatforms.GBA

    platforms_other = None

    is_adult_only_or_unrated = False

    options_cls = FinalFantasyTacticsAdvanceArchipelagoOptions

    # Optional Game Constraints
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        templates: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="RACE is not allowed to wear the following equipment: EQUIPMENT",
                data={
                    "RACE": (self.race, 1),
                    "EQUIPMENT": (self.equipment, 2),
                },
            ),
            GameObjectiveTemplate(
                label="RACE must break the law every battle",
                data={
                    "RACE": (self.race, 1),
                },
            ),
            GameObjectiveTemplate(
                label="RACE can only switch equipment after every third battle",
                data={
                    "RACE": (self.race, 1),
                },
            ),
            GameObjectiveTemplate(
                label="Not allowed to switch jobs",
                data=dict(),
            ),
        ]
        return templates
    
    # Main Objectives
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        templates: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Beat COUNTBATTLES clan battles.",
                data={
                    "COUNTBATTLES": (self.battles_count, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win a battle with atleast PARTYSIZE of the RACE race in your party.",
                data={
                    "PARTYSIZE": (self.party_size, 1),
                    "RACE": (self.race, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win a battle with exactly PARTYSIZE of the RACE race in your party.",
                data={
                    "PARTYSIZE": (self.party_size, 1),
                    "RACE": (self.race, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win a battle with only the RACE race in your party.",
                data={
                    "RACE": (self.race, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win a battle with at least one JOBS in your party.",
                data={
                    "JOBS": (self.jobs, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Master COUNTABILITIES abilities with a single unit.",
                data={
                    "COUNTABILITIES": (self.abilities_count, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Master COUNTABILITIES abilities with a JOBS.",
                data={
                    "COUNTABILITIES": (self.abilities_count, 1),
                    "JOBS": (self.jobs, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Must afflict NEGATIVESTATUS status to PARTYSIZE opponents.",
                data={
                    "NEGATIVESTATUS": (self.neg_status, 1),
                    "PARTYSIZE": (self.party_size, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Must afflict POSITIVESTATUS status to an ally.",
                data={
                    "POSITIVESTATUS": (self.pos_status, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Must afflict NEGATIVESTATUS status to an ally.",
                data={
                    "NEGATIVESTATUS": (self.neg_status, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Remove an opponent from combat (Exorcise, Capture, Oust, Parley).",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Steal from an opponent.",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Defeat an ally unit.",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Receive a COLOR card.",
                data={
                    "COLOR": (self.color, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Successfully return from a dispatch mission with a JOBS",
                data={
                    "JOBS": (self.jobs, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Complete COUNTBATTLES dispatch missions",
                data={
                    "COUNTBATTLES": (self.battles_count, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
        ]
        return templates


    # Datasets
    @staticmethod
    def equipment() -> List[str]:
        return [
            "Headgear",
            "Armor",
            "Weapon",
            "Shield",
            "Accessoires - Shoes",
            "Accessoires - Gloves",
            "Accessoires - Other",
        ]

    @staticmethod
    def race() -> List[str]:
        return [
            "Human",
            "Bangaa",
            "Moogle",
            "Viera",
            "Nu Mou",
        ]

    @staticmethod
    def jobs() -> List[str]:
        return [
            "Human Soldier",
            "Human Fighter",
            "Human Paladin",
            "Human Thief",
            "Human Ninja",
            "Human Archer",
            "Human White Mage",
            "Human Black Mage",
            "Human Blue Mage",
            "Human Illusionist",
            "Moogle Animist",
            "Moogle Thief",
            "Moogle Gunner",
            "Moogle Juggler",
            "Moogle Gadgeteer",
            "Moogle Black Mage",
            "Moogle Time Mage",
            "Viera Fencer",
            "Viera Archer",
            "Viera Sniper",
            "Viera Elementalist",
            "Viera Red Mage",
            "Viera White Mage",
            "Viera Summoner",
            "Viera Assassin",
            "Bangaa Warrior",
            "Bangaa Gladiator",
            "Bangaa Defender",
            "Bangaa Dragoon",
            "Bangaa White Monk",
            "Bangaa Bishop",
            "Bangaa Templar",
            "Nu Mou White Mage",
            "Nu Mou Black Mage",
            "Nu Mou Time Mage",
            "Nu Mou Illusionist",
            "Nu Mou Alchemist",
            "Nu Mou Sage",
            "Nu Mou Beastmaster",
            "Nu Mou Morpher",
        ]
    @staticmethod
    def neg_status() -> List[str]:
        return [
            "Addle",
            "Berserk",
            "Blind",
            "Charm",
            "Confuse",
            "Disable",
            "Doom",
            "Frog",
            "Immobilize",
            "Petrify",
            "Poison",
            "Silence",
            "Sleep",
            "Slow",
            "Stop",
            "Zombie",
        ]
    @staticmethod
    def pos_status() -> List[str]:
        return [
            "Advice",
            "Astra",
            "Auto-Life",
            "Boost",
            "Conceal",
            "Cover",
            "Defense",
            "Expert Guard",
            "Haste",
            "Hibernate",
            "Protect",
            "Reflect",
            "Regen",
            "Shell",
        ]
    @staticmethod
    def color() -> List[str]:
        return [
            "yellow",
            "red",
        ]
    # picks a random number from 2-10
    @staticmethod
    def battles_count() -> range:
        return range(2, 11)

    # picks a random number from 2-6
    @staticmethod
    def party_size() -> range:
        return range(2, 7)

    # picks a random number from 2-7
    @staticmethod
    def abilities_count() -> range:
        return range(2, 8)