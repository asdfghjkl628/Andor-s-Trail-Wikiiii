---
description: "Aggresive woodworm is an enemy in Andor's Trail (animal) with 80 HP, worth 309 XP, found in elm_2f_1, elm_3f, elm_4f_1. Drops: Claws, Rotten meat, Worm meat, Gold coins."
---

# ![](../assets/icons/monsters/monsters_rltiles2_162.png){ .sprite } Aggresive woodworm

**Found in:** [elm_2f_1](../maps/elm_2f_1.md), [elm_3f](../maps/elm_3f.md), [elm_4f_1](../maps/elm_4f_1.md), [elm_4f_2](../maps/elm_4f_2.md) (+4 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_162.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | elm_2f_1, elm_3f, elm_4f_1 |
| **Class** | Animal |
| **HP** | 80 |
| **XP when defeated** | 309 |
| **Entry ID** | `elm_woodworm2` |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 80 |
| XP when defeated | 309 |
| Damage | 7 to 10 |
| Attack chance | 94 |
| Block chance | 139 |
| Damage resistance | 7 |
| Max AP | 12 |
| Attack cost | 3 AP |
| Attacks per turn | 4 |
| Move cost | 5 AP |
| Critical skill | 10 |
| Critical multiplier | 2.0 |
| Critical hit chance | 9% |

**On hit:** Heal HP: -1 to 1; On target: Bleeding wound (magnitude 2, 2 rounds, 20% chance)

**When hit:** On target: Nausea (magnitude 2, 2 rounds, 30% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

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
| [elm_2f_1](../maps/elm_2f_1.md) | – | 19 | – |
| [elm_3f](../maps/elm_3f.md) | – | 9 | – |
| [elm_4f_1](../maps/elm_4f_1.md) | – | 6 | – |
| [elm_4f_2](../maps/elm_4f_2.md) | – | 7 | – |
| [elm_4f_3](../maps/elm_4f_3.md) | – | 2 | – |
| [elm_4f_4](../maps/elm_4f_4.md) | – | 3 | – |
| [elm_4f_5](../maps/elm_4f_5.md) | – | 3 | – |
| [elm_mine5](../maps/elm_mine5.md) | – | 7 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `elm_woodworm2` |
    | Spawn group | `elm_mine1` |
    | Loot table | `elm_woodworm` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_rltiles2:162` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "elm_woodworm2",
     "name": "Aggresive woodworm",
     "iconID": "monsters_rltiles2:162",
     "maxHP": 80,
     "maxAP": 12,
     "moveCost": 5,
     "monsterClass": "animal",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 7,
      "max": 10
     },
     "spawnGroup": "elm_mine1",
     "droplistID": "elm_woodworm",
     "attackCost": 3,
     "attackChance": 94,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 139,
     "damageResistance": 7,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": -1,
       "max": 1
      },
      "conditionsTarget": [
       {
        "condition": "bleeding_wound",
        "magnitude": 2,
        "duration": 2,
        "chance": "20"
       }
      ]
     },
     "hitReceivedEffect": {
      "conditionsTarget": [
       {
        "condition": "nausea",
        "magnitude": 2,
        "duration": 2,
        "chance": "30"
       }
      ]
     }
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_woodworm2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_woodworm2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_woodworm2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_woodworm2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
