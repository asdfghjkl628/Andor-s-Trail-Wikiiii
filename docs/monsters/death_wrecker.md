---
description: "Death wrecker is an enemy in Andor's Trail (undead) with 253 HP, worth 652 XP, found in Haunted house, Haunted house basement, Haunted underground 1. Drops: Death mace, Gold coins, Human skull, Skeletal remains."
---

# ![](../assets/icons/monsters/monsters_tometik8_57.png){ .sprite } Death wrecker

**Found in:** [Haunted house](../maps/haunted_house.md), [Haunted house basement](../maps/haunted_house_basement.md), [Haunted underground 1](../maps/haunted_underground_1.md), [Haunted underground 2](../maps/haunted_underground_2.md) (+4 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik8_57.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Haunted house, Haunted house basement, Haunted underground 1 |
| **Class** | Undead |
| **HP** | 253 |
| **XP when defeated** | 652 |
| **Introduced** | [v0.8.3](../versions/0.8.3.md) |

</div>

## Combat

| | |
|---|---|
| Class | Undead |
| HP | 253 |
| XP when defeated | 652 |
| Damage | 21 to 24 |
| AC | 227 |
| BC | 111 |
| DR | 0 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | 2% (×2.0) |

**Its hits:** On target: [Fear](../conditions/fear.md) (magnitude 4, 3 rounds, 25% chance)

**When you hit it:** On self: [Regeneration](../conditions/regen2.md) (magnitude 6, 1 round)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Death mace](../items/death_mace.md) | 5% | 1 |
| [Gold coins](../items/gold.md) | 50% | 8 to 20 |
| [Human skull](../items/human_skull.md) | 5% | 1 |
| [Skeletal remains](../items/skeletal_remains.md) | 20% | 1 |
| [Tonic of blood](../items/tonic_of_blood.md) | 12% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Haunted house](../maps/haunted_house.md) | – | 1 | – |
| [Haunted house basement](../maps/haunted_house_basement.md) | – | 3 | – |
| [Haunted underground 1](../maps/haunted_underground_1.md) | – | 3 | – |
| [Haunted underground 2](../maps/haunted_underground_2.md) | – | 1 | – |
| [Haunted underground 3](../maps/haunted_underground_3.md) | – | 2 | – |
| [Haunted underground 4](../maps/haunted_underground_4.md) | – | 3 | – |
| [Haunted underground 5](../maps/haunted_underground_5.md) | – | 1 | – |
| [Vilegard sullengard filler 1](../maps/vilegard_sullengard_filler1.md) | – | 3 | – |


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
    | Entry ID | `death_wrecker` |
    | Type (wiki) | Enemy |
    | Spawn group | `death_wrecker` |
    | Loot table | `death_wrecker_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik8:57` |
    | Defined in | `res/raw/monsterlist_haunted_forest.json` |

    Raw data:

    ```json
    {
     "id": "death_wrecker",
     "name": "Death wrecker",
     "iconID": "monsters_tometik8:57",
     "maxHP": 253,
     "moveCost": 5,
     "monsterClass": "undead",
     "attackDamage": {
      "min": 21,
      "max": 24
     },
     "droplistID": "death_wrecker_dl",
     "attackCost": 5,
     "attackChance": 227,
     "criticalSkill": 3,
     "criticalMultiplier": 2.0,
     "blockChance": 111,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "fear",
        "magnitude": 4,
        "duration": 3,
        "chance": "25"
       }
      ]
     },
     "hitReceivedEffect": {
      "conditionsSource": [
       {
        "condition": "regen2",
        "magnitude": 6,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=death_wrecker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=death_wrecker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=death_wrecker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=death_wrecker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
