---
description: "River wretch is an enemy in Andor's Trail (humanoid) with 201 HP, worth 561–611 XP, found in Mt. Galmore. Drops: Bramblefin, Mountain eel meat, Gold coins."
---

# ![](../assets/icons/monsters/monsters_ld2_150.png){ .sprite } River wretch

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld2_150.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Mt. Galmore |
| **Class** | Humanoid |
| **HP** | 201 |
| **XP when defeated** | 561–611 |
| **Entries in game data** | 2 |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

!!! info "2 entries in the game data"
    The game data defines 2 separate characters named River wretch. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: location, appearance, movement. Each entry has its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`river_wretch`](#v-river_wretch) | Enemy | Mt. Galmore: [Galmore 46](../maps/galmore_46.md), Mt. Galmore: [Galmore 55](../maps/galmore_55.md) (+3 more) | – | 201 |
| [`river_wretch2`](#v-river_wretch2) | Enemy | Mt. Galmore: [Galmore 56](../maps/galmore_56.md), Mt. Galmore: [Galmore 65](../maps/galmore_65.md) (+2 more) | – | 201 |

## Mt. Galmore, Galmore 46 and 4 more (river_wretch) { #v-river_wretch }

**Entry ID:** `river_wretch` · **Type:** Enemy

**Location:** Mt. Galmore: [Galmore 46](../maps/galmore_46.md), Mt. Galmore: [Galmore 55](../maps/galmore_55.md), Mt. Galmore: [Galmore 56](../maps/galmore_56.md), Mt. Galmore: [Galmore 65](../maps/galmore_65.md), Mt. Galmore: [Galmore 66](../maps/galmore_66.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 201 |
| XP when defeated | 611 |
| Damage | 9 to 13 |
| Attack chance | 199 |
| Block chance | 176 |
| Damage resistance | 9 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 3 AP |
| Critical skill | 13 |
| Critical multiplier | 2.0 |
| Critical hit chance | 11% |

**On hit:** On target: [Soaked vision](../conditions/soaked_vision.md) (magnitude 1, 3 rounds, 8% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Bramblefin](../items/bramblefin_fish.md) | 10% | 1 to 2 |
| [Mountain eel meat](../items/eel_meat.md) | 8% | 1 |
| [Gold coins](../items/gold.md) | 30% | 5 to 6 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Galmore 46](../maps/galmore_46.md) | Mt. Galmore | 1 | – |
| [Galmore 55](../maps/galmore_55.md) | Mt. Galmore | 1 | – |
| [Galmore 56](../maps/galmore_56.md) | Mt. Galmore | 4 | – |
| [Galmore 65](../maps/galmore_65.md) | Mt. Galmore | 1 | – |
| [Galmore 66](../maps/galmore_66.md) | Mt. Galmore | 4 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (river_wretch)"

    | | |
    |---|---|
    | Entry ID | `river_wretch` |
    | Spawn group | `river_wretch` |
    | Loot table | `river_wretch_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_ld2:150` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "river_wretch",
     "name": "River wretch",
     "iconID": "monsters_ld2:150",
     "maxHP": 201,
     "moveCost": 3,
     "monsterClass": "humanoid",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 9,
      "max": 13
     },
     "droplistID": "river_wretch_dl",
     "attackCost": 4,
     "attackChance": 199,
     "criticalSkill": 13,
     "criticalMultiplier": 2.0,
     "blockChance": 176,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "soaked_vision",
        "magnitude": 1,
        "duration": 3,
        "chance": "8"
       }
      ]
     }
    }
    ```


## Mt. Galmore, Galmore 56 and 3 more (river_wretch2) { #v-river_wretch2 }

**Entry ID:** `river_wretch2` · **Type:** Enemy

**Location:** Mt. Galmore: [Galmore 56](../maps/galmore_56.md), Mt. Galmore: [Galmore 65](../maps/galmore_65.md), Mt. Galmore: [Galmore 66](../maps/galmore_66.md), Mt. Galmore: [Galmore 76](../maps/galmore_76.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 201 |
| XP when defeated | 561 |
| Damage | 9 to 13 |
| Attack chance | 199 |
| Block chance | 176 |
| Damage resistance | 9 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 3 AP |
| Critical skill | 13 |
| Critical multiplier | 2.0 |
| Critical hit chance | 11% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Bramblefin](../items/bramblefin_fish.md) | 10% | 1 to 2 |
| [Mountain eel meat](../items/eel_meat.md) | 8% | 1 |
| [Gold coins](../items/gold.md) | 30% | 5 to 6 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Galmore 56](../maps/galmore_56.md) | Mt. Galmore | 8 | – |
| [Galmore 65](../maps/galmore_65.md) | Mt. Galmore | 1 | – |
| [Galmore 66](../maps/galmore_66.md) | Mt. Galmore | 2 | – |
| [Galmore 76](../maps/galmore_76.md) | Mt. Galmore | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (river_wretch2)"

    | | |
    |---|---|
    | Entry ID | `river_wretch2` |
    | Spawn group | `river_wretch2` |
    | Loot table | `river_wretch_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:110` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "river_wretch2",
     "name": "River wretch",
     "iconID": "monsters_ld2:110",
     "maxHP": 201,
     "moveCost": 3,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 9,
      "max": 13
     },
     "droplistID": "river_wretch_dl",
     "attackCost": 4,
     "attackChance": 199,
     "criticalSkill": 13,
     "criticalMultiplier": 2.0,
     "blockChance": 176,
     "damageResistance": 9
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=river_wretch.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=river_wretch.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=river_wretch.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=river_wretch.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
