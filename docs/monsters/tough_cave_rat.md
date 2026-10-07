---
description: "Tough cave rat is an enemy in Andor's Trail (animal) with 5 HP, worth 15 XP, found in Crossglen, Mt. Galmore, Guynmart Castle, Pub, Bloskelt + Roskelt, Entry. Drops: Gold coins, Rat tail."
---

# ![](../assets/icons/monsters/monsters_rats_1.png){ .sprite } Tough cave rat

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rats_1.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Crossglen, Mt. Galmore, Guynmart Castle, Pub, Bloskelt + Roskelt, Entry |
| **Class** | Animal |
| **HP** | 5 |
| **XP when defeated** | 15 |
| **Entries in game data** | 2 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "2 entries in the game data"
    The game data defines 2 separate characters named Tough cave rat. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: location. Each entry has its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`tough_cave_rat`](#v-tough_cave_rat) | Enemy | Blackwater Mountain: [Ratdom maze 3](../maps/ratdom_maze3.md), Crossglen: [Crossglen cave](../maps/crossglen_cave.md) (+6 more) | – | 5 |
| [`tough_cave_rat3`](#v-tough_cave_rat3) | Enemy | 4 wells: [Ratdom maze 567](../maps/ratdom_maze_567.md), 4 wells: [Ratdom maze 658](../maps/ratdom_maze_658.md) (+132 more) | – | 5 |

## Blackwater Mountain, Ratdom maze 3 and 7 more (tough_cave_rat) { #v-tough_cave_rat }

**Entry ID:** `tough_cave_rat` · **Type:** Enemy

**Location:** Blackwater Mountain: [Ratdom maze 3](../maps/ratdom_maze3.md), Crossglen: [Crossglen cave](../maps/crossglen_cave.md), Crossglen: [Ratdom maze 1](../maps/ratdom_maze1.md), Entry: [Ratdom maze 2](../maps/ratdom_maze2.md), Guynmart Castle: [Guynmart tower 0](../maps/guynmart_tower_0.md), Mt. Galmore: [Galmore cavea](../maps/galmore_cavea.md) (+2 more)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 5 |
| XP when defeated | 15 |
| Damage | 3 |
| Attack chance | 90 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 2 to 4 |
| [Rat tail](../items/rat_tail.md) | 30% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Crossglen cave](../maps/crossglen_cave.md) | Crossglen | 2 | – |
| [Galmore cavea](../maps/galmore_cavea.md) | Mt. Galmore | 2 | – |
| [Galmore cavea 1](../maps/galmore_cavea_1.md) | Mt. Galmore | 2 | – |
| [Guynmart tower 0](../maps/guynmart_tower_0.md) | Guynmart Castle | 2 | – |
| [Mountainlake 8 cave](../maps/mountainlake8_cave.md) | – | 10 | – |
| [Ratdom maze 1](../maps/ratdom_maze1.md) | Crossglen | 2 | – |
| [Ratdom maze 2](../maps/ratdom_maze2.md) | Entry | 2 | – |
| [Ratdom maze 3](../maps/ratdom_maze3.md) | Blackwater Mountain | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.8.15](../versions/0.8.15.md) | Chance of appearing mirrored: added (25) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (tough_cave_rat)"

    | | |
    |---|---|
    | Entry ID | `tough_cave_rat` |
    | Spawn group | `crossglen_caverat2` |
    | Loot table | `rat` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rats:1` |
    | Defined in | `res/raw/monsterlist_crossglen_animals.json` |

    Raw data:

    ```json
    {
     "id": "tough_cave_rat",
     "name": "Tough cave rat",
     "iconID": "monsters_rats:1",
     "maxHP": 5,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 3,
      "max": 3
     },
     "spawnGroup": "crossglen_caverat2",
     "droplistID": "rat",
     "attackCost": 5,
     "attackChance": 90,
     "horizontalFlipChance": 25
    }
    ```


## 4 wells, Ratdom maze 567 and 133 more (tough_cave_rat3) { #v-tough_cave_rat3 }

**Entry ID:** `tough_cave_rat3` · **Type:** Enemy

**Location:** 4 wells: [Ratdom maze 567](../maps/ratdom_maze_567.md), 4 wells: [Ratdom maze 658](../maps/ratdom_maze_658.md), 4 wells: [Ratdom maze 768](../maps/ratdom_maze_768.md), Blackwater Mountain: [Ratdom maze 455a](../maps/ratdom_maze_455a.md), Bloskelt + Roskelt: [Ratdom maze 414](../maps/ratdom_maze_414.md), Bloskelt + Roskelt: [Ratdom maze 415](../maps/ratdom_maze_415.md) (+128 more)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 5 |
| XP when defeated | 15 |
| Damage | 3 |
| Attack chance | 90 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 2 to 4 |
| [Rat tail](../items/rat_tail.md) | 30% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Ratdom maze 402](../maps/ratdom_maze_402.md) | Pub | 1 | – |
| [Ratdom maze 403](../maps/ratdom_maze_403.md) | Pub | 1 | – |
| [Ratdom maze 412](../maps/ratdom_maze_412.md) | Pub | 2 | – |
| [Ratdom maze 413](../maps/ratdom_maze_413.md) | Pub | 1 | – |
| [Ratdom maze 414](../maps/ratdom_maze_414.md) | Bloskelt + Roskelt | 1 | – |
| [Ratdom maze 415](../maps/ratdom_maze_415.md) | Bloskelt + Roskelt | 1 | – |
| [Ratdom maze 416](../maps/ratdom_maze_416.md) | Bloskelt + Roskelt | 1 | – |
| [Ratdom maze 417](../maps/ratdom_maze_417.md) | Bloskelt + Roskelt | 1 | – |
| [Ratdom maze 418](../maps/ratdom_maze_418.md) | Entry | 1 | – |
| [Ratdom maze 421](../maps/ratdom_maze_421.md) | Pub | 1 | – |
| [Ratdom maze 422](../maps/ratdom_maze_422.md) | Pub | 1 | – |
| [Ratdom maze 423](../maps/ratdom_maze_423.md) | Gold hunter | 1 | – |
| [Ratdom maze 424](../maps/ratdom_maze_424.md) | Bloskelt + Roskelt | 1 | – |
| [Ratdom maze 425](../maps/ratdom_maze_425.md) | Bloskelt + Roskelt | 1 | – |
| [Ratdom maze 426](../maps/ratdom_maze_426.md) | Bloskelt + Roskelt | 1 | – |
| [Ratdom maze 427](../maps/ratdom_maze_427.md) | Entry | 1 | – |
| [Ratdom maze 428](../maps/ratdom_maze_428.md) | Entry | 1 | – |
| [Ratdom maze 432](../maps/ratdom_maze_432.md) | Pub | 1 | – |
| [Ratdom maze 433](../maps/ratdom_maze_433.md) | Pub | 1 | – |
| [Ratdom maze 434](../maps/ratdom_maze_434.md) | Gold hunter | 1 | – |
| [Ratdom maze 434b](../maps/ratdom_maze_434b.md) | Gold hunter | 1 | – |
| [Ratdom maze 435](../maps/ratdom_maze_435.md) | Bloskelt + Roskelt | 1 | – |
| [Ratdom maze 436](../maps/ratdom_maze_436.md) | Bloskelt + Roskelt | 1 | – |
| [Ratdom maze 437](../maps/ratdom_maze_437.md) | Bloskelt + Roskelt | 1 | – |
| [Ratdom maze 438](../maps/ratdom_maze_438.md) | Entry | 1 | – |
| [Ratdom maze 441](../maps/ratdom_maze_441.md) | Pub | 1 | – |
| [Ratdom maze 442](../maps/ratdom_maze_442.md) | Pub | 1 | – |
| [Ratdom maze 443](../maps/ratdom_maze_443.md) | Gold hunter | 1 | – |
| [Ratdom maze 444](../maps/ratdom_maze_444.md) | Gold hunter | 1 | – |
| [Ratdom maze 445](../maps/ratdom_maze_445.md) | Instrument maker | 1 | – |
| [Ratdom maze 446](../maps/ratdom_maze_446.md) | Bloskelt + Roskelt | 1 | – |
| [Ratdom maze 447](../maps/ratdom_maze_447.md) | Entry | 1 | – |
| [Ratdom maze 448](../maps/ratdom_maze_448.md) | Entry | 4 | – |
| [Ratdom maze 451](../maps/ratdom_maze_451.md) | – | 1 | – |
| [Ratdom maze 452](../maps/ratdom_maze_452.md) | – | 1 | – |
| [Ratdom maze 453](../maps/ratdom_maze_453.md) | Gold hunter | 1 | – |
| [Ratdom maze 454](../maps/ratdom_maze_454.md) | Instrument maker | 1 | – |
| [Ratdom maze 455](../maps/ratdom_maze_455.md) | Instrument maker | 1 | – |
| [Ratdom maze 455a](../maps/ratdom_maze_455a.md) | Blackwater Mountain | 1 | – |
| [Ratdom maze 456](../maps/ratdom_maze_456.md) | Instrument maker | 1 | – |
| [Ratdom maze 457](../maps/ratdom_maze_457.md) | Entry | 1 | – |
| [Ratdom maze 458](../maps/ratdom_maze_458.md) | Entry | 1 | – |
| [Ratdom maze 461](../maps/ratdom_maze_461.md) | – | 1 | – |
| [Ratdom maze 463](../maps/ratdom_maze_463.md) | Instrument maker | 1 | – |
| [Ratdom maze 464](../maps/ratdom_maze_464.md) | Instrument maker | 1 | – |
| [Ratdom maze 466](../maps/ratdom_maze_466.md) | – | 1 | – |
| [Ratdom maze 467](../maps/ratdom_maze_467.md) | Entry | 1 | – |
| [Ratdom maze 476](../maps/ratdom_maze_476.md) | – | 1 | – |
| [Ratdom maze 506](../maps/ratdom_maze_506.md) | Pub | 1 | – |
| [Ratdom maze 513](../maps/ratdom_maze_513.md) | Pub | 1 | – |
| [Ratdom maze 514](../maps/ratdom_maze_514.md) | Bloskelt + Roskelt | 1 | – |
| [Ratdom maze 515](../maps/ratdom_maze_515.md) | Museum | 1 | – |
| [Ratdom maze 516](../maps/ratdom_maze_516.md) | Bloskelt + Roskelt | 1 | – |
| [Ratdom maze 517](../maps/ratdom_maze_517.md) | Entry | 1 | – |
| [Ratdom maze 517a](../maps/ratdom_maze_517a.md) | – | 1 | – |
| [Ratdom maze 521](../maps/ratdom_maze_521.md) | Library | 1 | – |
| [Ratdom maze 522](../maps/ratdom_maze_522.md) | Pub | 1 | – |
| [Ratdom maze 523](../maps/ratdom_maze_523.md) | Pub | 1 | – |
| [Ratdom maze 524](../maps/ratdom_maze_524.md) | Bloskelt + Roskelt | 1 | – |
| [Ratdom maze 525](../maps/ratdom_maze_525.md) | Bloskelt + Roskelt | 1 | – |

*74 further maps are not listed.*


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (tough_cave_rat3)"

    | | |
    |---|---|
    | Entry ID | `tough_cave_rat3` |
    | Spawn group | `ratdom_maze_rat` |
    | Loot table | `rat` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rats:1` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "tough_cave_rat3",
     "name": "Tough cave rat",
     "iconID": "monsters_rats:1",
     "maxHP": 5,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 3,
      "max": 3
     },
     "spawnGroup": "ratdom_maze_rat",
     "droplistID": "rat",
     "attackCost": 5,
     "attackChance": 90
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tough_cave_rat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tough_cave_rat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tough_cave_rat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tough_cave_rat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
