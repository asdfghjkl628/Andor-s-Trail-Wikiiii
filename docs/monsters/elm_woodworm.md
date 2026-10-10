---
description: "Contaminated woodworm is an enemy in Andor's Trail (animal) with 76 HP, worth 292 XP, found in Elm 2f 1, Elm 3f, Elm 4f 1. Drops: Claws, Rotten meat, Worm meat, Gold coins."
---

# ![](../assets/icons/monsters/monsters_rltiles2_162.png){ .sprite } Contaminated woodworm

**Found in:** [Elm 2f 1](../maps/elm_2f_1.md), [Elm 3f](../maps/elm_3f.md), [Elm 4f 1](../maps/elm_4f_1.md), [Elm 4f 2](../maps/elm_4f_2.md) (+4 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_162.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Elm 2f 1, Elm 3f, Elm 4f 1 |
| **Class** | Animal |
| **HP** | 76 |
| **XP when defeated** | 292 |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

## Combat

| | |
|---|---|
| Class | Animal |
| HP | 76 |
| XP when defeated | 292 |
| Damage | 6 to 9 |
| AC | 90 |
| BC | 144 |
| DR | 7 |
| Attacks per turn | 4 (3 AP each, 12 AP) |
| Crit chance | 9% (×2.0) |

**Its hits:** Heal HP: -1; On target: [Bleeding wound](../conditions/bleeding_wound.md) (magnitude 1, 2 rounds, 20% chance)

**When you hit it:** Heal HP: 1; On target: [Nausea](../conditions/nausea.md) (magnitude 2, 3 rounds, 30% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Claws](../items/claws.md) | 33.3333% | 1 |
| [Rotten meat](../items/meat2.md) | 10% | 1 |
| [Worm meat](../items/meat3.md) | 20% | 1 |
| [Gold coins](../items/gold.md) | 100% | 1 to 12 |
| [Small rock](../items/rock.md) | 12.5% | 1 to 3 |
| [Small empty vial](../items/vial_empty1.md) | 12.5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Elm 2f 1](../maps/elm_2f_1.md) | – | 19 | – |
| [Elm 3f](../maps/elm_3f.md) | – | 9 | – |
| [Elm 4f 1](../maps/elm_4f_1.md) | – | 6 | – |
| [Elm 4f 2](../maps/elm_4f_2.md) | – | 7 | – |
| [Elm 4f 3](../maps/elm_4f_3.md) | – | 2 | – |
| [Elm 4f 4](../maps/elm_4f_4.md) | – | 3 | – |
| [Elm 4f 5](../maps/elm_4f_5.md) | – | 3 | – |
| [Elm mine 5](../maps/elm_mine5.md) | – | 8 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |

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
    | Entry ID | `elm_woodworm` |
    | Type (wiki) | Enemy |
    | Spawn group | `elm_mine1` |
    | Loot table | `elm_woodworm` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_rltiles2:162` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "elm_woodworm",
     "name": "Contaminated woodworm",
     "iconID": "monsters_rltiles2:162",
     "maxHP": 76,
     "maxAP": 12,
     "moveCost": 5,
     "monsterClass": "animal",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 6,
      "max": 9
     },
     "spawnGroup": "elm_mine1",
     "droplistID": "elm_woodworm",
     "attackCost": 3,
     "attackChance": 90,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 144,
     "damageResistance": 7,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": -1,
       "max": -1
      },
      "conditionsTarget": [
       {
        "condition": "bleeding_wound",
        "magnitude": 1,
        "duration": 2,
        "chance": "20"
       }
      ]
     },
     "hitReceivedEffect": {
      "increaseCurrentHP": {
       "min": 1,
       "max": 1
      },
      "conditionsTarget": [
       {
        "condition": "nausea",
        "magnitude": 2,
        "duration": 3,
        "chance": "30"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_woodworm.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_woodworm.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_woodworm.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_woodworm.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
