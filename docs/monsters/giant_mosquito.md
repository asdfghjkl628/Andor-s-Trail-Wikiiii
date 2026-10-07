---
description: "Giant mosquito is an enemy in Andor's Trail (insect) with 106 HP, worth 503 XP, found in Mt. Galmore. Drops: Mosquito proboscis."
---

# ![](../assets/icons/monsters/monsters_newb_1_580.png){ .sprite } Giant mosquito

**Found in:** Mt. Galmore: [galmore_47](../maps/galmore_47.md), [galmore_17](../maps/galmore_17.md), [galmore_18](../maps/galmore_18.md), [galmore_19](../maps/galmore_19.md) (+6 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_1_580.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Mt. Galmore |
| **Class** | Insect |
| **HP** | 106 |
| **XP when defeated** | 503 |
| **Entry ID** | `giant_mosquito` |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Insect |
| HP | 106 |
| XP when defeated | 503 |
| Damage | 10 to 12 |
| Attack chance | 190 |
| Block chance | 250 |
| Damage resistance | 0 |
| Max AP | 12 |
| Attack cost | 3 AP |
| Attacks per turn | 4 |
| Move cost | 3 AP |
| Critical skill | 5 |
| Critical multiplier | 2.0 |
| Critical hit chance | 5% |

**On hit:** On target: Insect contagion (magnitude 7, 5 rounds, 65% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Mosquito proboscis](../items/mosquito_proboscis.md) | 35% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [galmore_17](../maps/galmore_17.md) | – | 4 | – |
| [galmore_18](../maps/galmore_18.md) | – | 8 | – |
| [galmore_19](../maps/galmore_19.md) | – | 2 | – |
| [galmore_27](../maps/galmore_27.md) | – | 4 | – |
| [galmore_28](../maps/galmore_28.md) | – | 11 | – |
| [galmore_29](../maps/galmore_29.md) | – | 2 | – |
| [galmore_37](../maps/galmore_37.md) | – | 9 | – |
| [galmore_38](../maps/galmore_38.md) | – | 11 | – |
| [galmore_39](../maps/galmore_39.md) | – | 5 | – |
| [galmore_47](../maps/galmore_47.md) | Mt. Galmore | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `giant_mosquito` |
    | Spawn group | `giant_mosquito` |
    | Loot table | `giant_mosquito_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_newb_1:580` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "giant_mosquito",
     "name": "Giant mosquito",
     "iconID": "monsters_newb_1:580",
     "maxHP": 106,
     "maxAP": 12,
     "moveCost": 3,
     "monsterClass": "insect",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 10,
      "max": 12
     },
     "droplistID": "giant_mosquito_dl",
     "attackCost": 3,
     "attackChance": 190,
     "criticalSkill": 5,
     "criticalMultiplier": 2.0,
     "blockChance": 250,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "contagion",
        "magnitude": 7,
        "duration": 5,
        "chance": "65"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=giant_mosquito.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=giant_mosquito.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=giant_mosquito.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=giant_mosquito.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
