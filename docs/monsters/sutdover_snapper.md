---
description: "River snapper is an enemy in Andor's Trail (reptile) with 100 HP, worth 482 XP, found in Mt. Galmore."
---

# ![](../assets/icons/monsters/monsters_newb_1_210.png){ .sprite } River snapper

**Found in:** Mt. Galmore: [galmore_36](../maps/galmore_36.md), Mt. Galmore: [galmore_46](../maps/galmore_46.md), Mt. Galmore: [galmore_47](../maps/galmore_47.md), [galmore_29](../maps/galmore_29.md) (+1 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_1_210.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Mt. Galmore |
| **Class** | Reptile |
| **HP** | 100 |
| **XP when defeated** | 482 |
| **Entry ID** | `sutdover_snapper` |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Reptile |
| HP | 100 |
| XP when defeated | 482 |
| Damage | 11 to 25 |
| Attack chance | 140 |
| Block chance | 250 |
| Damage resistance | 25 |
| Max AP | 10 |
| Attack cost | 8 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 20 |
| Critical multiplier | 2.5 |
| Critical hit chance | 15% |

**When hit:** On self: Bark skin (magnitude 1, 3 rounds, 15% chance); On target: Bleeding wound (magnitude 3, 3 rounds, 15% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [galmore_29](../maps/galmore_29.md) | – | 6 | – |
| [galmore_36](../maps/galmore_36.md) | Mt. Galmore | 9 | – |
| [galmore_39](../maps/galmore_39.md) | – | 14 | – |
| [galmore_46](../maps/galmore_46.md) | Mt. Galmore | 2 | – |
| [galmore_47](../maps/galmore_47.md) | Mt. Galmore | 9 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `sutdover_snapper` |
    | Spawn group | `sutdover_snapper` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_newb_1:210` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "sutdover_snapper",
     "name": "River snapper",
     "iconID": "monsters_newb_1:210",
     "maxHP": 100,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 11,
      "max": 25
     },
     "attackCost": 8,
     "attackChance": 140,
     "criticalSkill": 20,
     "criticalMultiplier": 2.5,
     "blockChance": 250,
     "damageResistance": 25,
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
        "magnitude": 3,
        "duration": 3,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sutdover_snapper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sutdover_snapper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sutdover_snapper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sutdover_snapper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
