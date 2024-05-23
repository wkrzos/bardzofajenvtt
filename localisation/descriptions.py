import json
from enum import Enum
from backend.characterCard.characteristics import  *

class FightDescriptionsType(Enum):
    DMG_ROLL = "FDsc.1"
    INITIATIVE_ROLL = "FDsc.2"




class RollDescriptionAggregator:
    fightDescriptions = {
        FightDescriptionsType.DMG_ROLL : "",
        FightDescriptionsType.INITIATIVE_ROLL : "",
    }

    testDescriptions = {
        MainStats.WEAPON_SKILL : "",
        MainStats.BALLISTIC_SKILL: "",
        MainStats.STRENGTH : "",
        MainStats.TOUGHNESS: "",
        MainStats.AGILITY: "",
        MainStats.INTELLIGENCE : "",
        MainStats.WILL_POWER : "",
        MainStats.FELLOWSHIP : ""
    }

    @classmethod
    def serializeFightDesc(cls):
        return {
            FightDescriptionsType.DMG_ROLL.value: cls.fightDescriptions[FightDescriptionsType.DMG_ROLL],
            FightDescriptionsType.INITIATIVE_ROLL.value: cls.fightDescriptions[FightDescriptionsType.INITIATIVE_ROLL],
        }

    @classmethod
    def serializeTestDesc(cls):
        return {
        MainStats.WEAPON_SKILL.value : cls.testDescriptions[MainStats.WEAPON_SKILL],
        MainStats.BALLISTIC_SKILL.value: cls.testDescriptions[MainStats.BALLISTIC_SKILL],
        MainStats.STRENGTH.value : cls.testDescriptions[MainStats.STRENGTH],
        MainStats.TOUGHNESS.value: cls.testDescriptions[MainStats.TOUGHNESS],
        MainStats.AGILITY.value: cls.testDescriptions[MainStats.AGILITY],
        MainStats.INTELLIGENCE.value : cls.testDescriptions[MainStats.INTELLIGENCE],
        MainStats.WILL_POWER.value : cls.testDescriptions[MainStats.WILL_POWER],
        MainStats.FELLOWSHIP.value : cls.testDescriptions[MainStats.FELLOWSHIP]
    }

    @classmethod
    def loadFigthDescriptions(cls, path: str) -> None:
        try:
            with open(path, "r") as f:
                jsonData = json.load(f)
                for key in cls.fightDescriptions.keys():
                    if key.value in jsonData.keys():
                        cls.fightDescriptions[key] = jsonData[key.value]
        except FileNotFoundError:
            pass
    @classmethod
    def loadtestDescriptions(cls, path: str) -> None:
        try:
            with open(path, "r") as f:
                jsonData = json.load(f)
                for key in cls.testDescriptions.keys():
                    if key.value in jsonData.keys():
                        cls.testDescriptions[key] = jsonData[key.value]
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    with open("language/pl/testDesc.json", "w") as f:
        json.dump(RollDescriptionAggregator.serializeTestDesc(), f)