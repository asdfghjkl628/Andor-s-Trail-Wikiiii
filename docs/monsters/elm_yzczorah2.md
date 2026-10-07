---
description: "Yczorah is an enemy in Andor's Trail (demon) with 231 HP, worth 542 XP, found in Elm 5f 1, Elm 5f 2. Drops: Gold coins, Yczorah tentacle, Contaminated bone, Major potion of health."
---

# ![](../assets/icons/monsters/monsters_tometik10_9.png){ .sprite } Yczorah

**Found in:** [Elm 5f 1](../maps/elm5f_1.md), [Elm 5f 2](../maps/elm5f_2.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik10_9.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Elm 5f 1, Elm 5f 2 |
| **Class** | Demon |
| **HP** | 231 |
| **XP when defeated** | 542 |
| **Immune to critical hits** | Yes |
| **Entry ID** | `elm_yzczorah2` |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Demon |
| HP | 231 |
| XP when defeated | 542 |
| Damage | 6 to 7 |
| Attack chance | 78 |
| Block chance | 155 |
| Damage resistance | 7 |
| Max AP | 14 |
| Attack cost | 4 AP |
| Attacks per turn | 3 |
| Move cost | 7 AP |
| Critical skill | 5 |
| Critical multiplier | 2.0 |
| Critical hit chance | 5% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.

**On hit:** On self: [Sustenance](../conditions/food.md) (magnitude 3, 2 rounds, 20% chance); On target: [Bleeding wound](../conditions/bleeding_wound.md) (magnitude 6, 2 rounds, 10% chance)

**When hit:** On target: [Nausea](../conditions/nausea.md) (magnitude 5, 3 rounds, 20% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 6 to 8 |
| [Yczorah tentacle](../items/yczorah.md) | 10% | 1 |
| [Contaminated bone](../items/bone2.md) | 5% | 1 |
| [Major potion of health](../items/health_major2.md) | 12.5% | 1 |
| [Contaminated poison gland](../items/gland2.md) | 2% | 1 |
| [Raw inkyfish](../items/bwm_fish.md) | 6.25% | 1 to 3 |
| [Human skull](../items/skull1.md) | 42.5% | 1 to 3 |
| [Yczorah nucleus](../items/yczorah2.md) | 0.01% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Elm 5f 1](../maps/elm5f_1.md) | – | 1 | – |
| [Elm 5f 2](../maps/elm5f_2.md) | – | 4 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `elm_yzczorah2` |
    | Spawn group | `elm_mine6` |
    | Loot table | `elm_yczorah` |
    | Conversation | – |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_tometik10:9` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "elm_yzczorah2",
     "name": "Yczorah",
     "iconID": "monsters_tometik10:9",
     "maxHP": 231,
     "maxAP": 14,
     "moveCost": 7,
     "monsterClass": "demon",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 6,
      "max": 7
     },
     "spawnGroup": "elm_mine6",
     "droplistID": "elm_yczorah",
     "attackCost": 4,
     "attackChance": 78,
     "criticalSkill": 5,
     "criticalMultiplier": 2.0,
     "blockChance": 155,
     "damageResistance": 7,
     "hitEffect": {
      "conditionsSource": [
       {
        "condition": "food",
        "magnitude": 3,
        "duration": 2,
        "chance": "20"
       }
      ],
      "conditionsTarget": [
       {
        "condition": "bleeding_wound",
        "magnitude": 6,
        "duration": 2,
        "chance": "10"
       }
      ]
     },
     "hitReceivedEffect": {
      "conditionsTarget": [
       {
        "condition": "nausea",
        "magnitude": 5,
        "duration": 3,
        "chance": "20"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_yzczorah2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_yzczorah2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_yzczorah2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_yzczorah2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
