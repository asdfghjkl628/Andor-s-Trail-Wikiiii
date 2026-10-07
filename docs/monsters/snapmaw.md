---
description: "Snapmaw is an enemy in Andor's Trail (reptile) with 114 HP, worth 516 XP, found in Mt. Galmore."
---

# ![](../assets/icons/monsters/monsters_newb_1_213.png){ .sprite } Snapmaw

**Found in:** Mt. Galmore: [galmore_25](../maps/galmore_25.md), [galmore_14](../maps/galmore_14.md), [galmore_15](../maps/galmore_15.md), [galmore_16](../maps/galmore_16.md) (+3 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_1_213.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Mt. Galmore |
| **Class** | Reptile |
| **HP** | 114 |
| **XP when defeated** | 516 |
| **Entry ID** | `snapmaw` |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Reptile |
| HP | 114 |
| XP when defeated | 516 |
| Damage | 13 to 25 |
| Attack chance | 140 |
| Block chance | 250 |
| Damage resistance | 25 |
| Max AP | 13 |
| Attack cost | 7 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 20 |
| Critical multiplier | 2.0 |
| Critical hit chance | 15% |

**On hit:** Restore AP: 0 to 1

**When hit:** On self: Bark skin (magnitude 1, 3 rounds, 15% chance); On target: Bleeding wound (magnitude 4, 4 rounds, 15% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [galmore_14](../maps/galmore_14.md) | – | 6 | – |
| [galmore_15](../maps/galmore_15.md) | – | 10 | – |
| [galmore_16](../maps/galmore_16.md) | – | 5 | – |
| [galmore_25](../maps/galmore_25.md) | Mt. Galmore | 14 | – |
| [galmore_26](../maps/galmore_26.md) | – | 13 | – |
| [galmore_27](../maps/galmore_27.md) | – | 3 | – |
| [galmore_37](../maps/galmore_37.md) | – | 8 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `snapmaw` |
    | Spawn group | `snapmaw` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_newb_1:213` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "snapmaw",
     "name": "Snapmaw",
     "iconID": "monsters_newb_1:213",
     "maxHP": 114,
     "maxAP": 13,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 13,
      "max": 25
     },
     "attackCost": 7,
     "attackChance": 140,
     "criticalSkill": 20,
     "criticalMultiplier": 2.0,
     "blockChance": 250,
     "damageResistance": 25,
     "hitEffect": {
      "increaseCurrentAP": {
       "min": 0,
       "max": 1
      }
     },
     "hitReceivedEffect": {
      "conditionsSource": [
       {
        "condition": "barkskin",
        "magnitude": 1,
        "duration": 3,
        "chance": "15"
       }
      ],
      "conditionsTarget": [
       {
        "condition": "bleeding_wound",
        "magnitude": 4,
        "duration": 4,
        "chance": "15"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=snapmaw.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=snapmaw.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=snapmaw.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=snapmaw.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
