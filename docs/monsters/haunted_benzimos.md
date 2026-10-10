---
description: "Benzimos is an enemy in Andor's Trail (demon) with 291 HP, worth 980 XP, found in Haunted house basement. Drops: Gold coins, Shield of the undead, Major flask of health, Tonic of blood."
---

# ![](../assets/icons/monsters/monsters_ld2_47.png){ .sprite } Benzimos

**Found in:** [Haunted house basement](../maps/haunted_house_basement.md)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld2_47.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Haunted house basement |
| **Class** | Demon |
| **HP** | 291 |
| **XP when defeated** | 980 |
| **Immune to crits** | Yes |
| **Introduced** | [v0.8.3](../versions/0.8.3.md) |

</div>

## Combat

| | |
|---|---|
| Class | Demon |
| HP | 291 |
| XP when defeated | 980 |
| Damage | 19 to 20 |
| AC | 219 |
| BC | 198 |
| DR | 0 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 9% (×2.0) |

**Immune to critical hits.**

**Its hits:** On target: [Fear](../conditions/fear.md) (magnitude 3, 3 rounds, 50% chance); [Death Plague](../conditions/death_plague.md) (magnitude 2, 3 rounds, 15% chance)

**When you hit it:** On self: [Regeneration](../conditions/regen2.md) (magnitude 7, 1 round)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 250 to 500 |
| [Shield of the undead](../items/shield_of_undead.md) | 100% | 1 |
| [Major flask of health](../items/health_major.md) | 100% | 2 to 4 |
| [Tonic of blood](../items/tonic_of_blood.md) | 100% | 2 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Haunted house basement](../maps/haunted_house_basement.md) | – | 1 | – |

## Quests that count defeats

- [The Dead are Walking](../quests/dead_walking.md#stage-60) with stepping on a trigger on [Haunted house basement](../maps/haunted_house_basement.md) checks that this enemy has been defeated.


## Version history

| Version | Change |
|---|---|
| [v0.8.3](../versions/0.8.3.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `haunted_benzimos` |
    | Type (wiki) | Enemy |
    | Spawn group | `haunted_benzimos` |
    | Loot table | `benzimos_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_ld2:47` |
    | Defined in | `res/raw/monsterlist_haunted_forest.json` |

    Raw data:

    ```json
    {
     "id": "haunted_benzimos",
     "name": "Benzimos",
     "iconID": "monsters_ld2:47",
     "maxHP": 291,
     "unique": 1,
     "monsterClass": "demon",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 19,
      "max": 20
     },
     "droplistID": "benzimos_dl",
     "attackCost": 3,
     "attackChance": 219,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 198,
     "damageResistance": 0,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "fear",
        "magnitude": 3,
        "duration": 3,
        "chance": "50"
       },
       {
        "condition": "death_plague",
        "magnitude": 2,
        "duration": 3,
        "chance": "15"
       }
      ]
     },
     "hitReceivedEffect": {
      "conditionsSource": [
       {
        "condition": "regen2",
        "magnitude": 7,
        "duration": 1,
        "chance": "100"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=haunted_benzimos.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=haunted_benzimos.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=haunted_benzimos.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=haunted_benzimos.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
