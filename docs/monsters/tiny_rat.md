---
description: "Tiny rat is an NPC who can also be fought in Andor's Trail, found in Crossglen, Flagstone Prison, Brightport, Mountainlake 8 cave, Pub, Bloskelt + Roskelt, Entry, Guynmart wood 19."
---

# ![](../assets/icons/monsters/monsters_rats_0.png){ .sprite } Tiny rat

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rats_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Crossglen, Flagstone Prison, Brightport, Mountainlake 8 cave, Pub, Bloskelt + Roskelt, Entry, Guynmart wood 19 |
| **Class** | Animal |
| **HP** | 2 |
| **XP when defeated** | 3 |
| **Entries in game data** | 5 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "5 entries in the game data"
    The game data defines 5 separate characters named Tiny rat. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation, location, combat statistics, loot or shop stock. Each entry has its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`tiny_rat`](#v-tiny_rat) | Enemy | Crossglen: [Crossglen](../maps/crossglen.md), Flagstone Prison: [Rat mountain 3](../maps/rat_mountain_3.md) | – | 2 |
| [`brute_origin1`](#v-brute_origin1) | Enemy | Brightport: [Brightport grave](../maps/brightport_grave.md), [Brightport school 11](../maps/brightport_school11.md) (+1 more) | – | 2 |
| [`brute_origin1a`](#v-brute_origin1a) | NPC | [Mountainlake 8 cave](../maps/mountainlake8_cave.md#pin-npc-brute_origin1a) | – | – |
| [`ratdom_maze_rat1`](#v-ratdom_maze_rat1) | Enemy | 4 wells: [Ratdom maze 567](../maps/ratdom_maze_567.md), 4 wells: [Ratdom maze 658](../maps/ratdom_maze_658.md) (+132 more) | – | 2 |
| [`tobby_trainingrat`](#v-tobby_trainingrat) | Enemy | [Guynmart wood 19](../maps/guynmart_wood_19.md) | – | 2 |

## Crossglen, Crossglen and 1 more (tiny_rat) { #v-tiny_rat }

**Entry ID:** `tiny_rat` · **Type:** Enemy

**Location:** Crossglen: [Crossglen](../maps/crossglen.md), Flagstone Prison: [Rat mountain 3](../maps/rat_mountain_3.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 2 |
| XP when defeated | 3 |
| Damage | 1 |
| Attack chance | 50 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 9 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 0 to 2 |
| [Small rat tail](../items/tail_trainingrat.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Crossglen](../maps/crossglen.md) | Crossglen | 2 | – |
| [Rat mountain 3](../maps/rat_mountain_3.md) | Flagstone Prison | 3 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.4](../versions/0.7.4.md) | Attack cost: 10 → 9 |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (tiny_rat)"

    | | |
    |---|---|
    | Entry ID | `tiny_rat` |
    | Spawn group | `trainingrat` |
    | Loot table | `trainingrat` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rats:0` |
    | Defined in | `res/raw/monsterlist_crossglen_animals.json` |

    Raw data:

    ```json
    {
     "id": "tiny_rat",
     "name": "Tiny rat",
     "iconID": "monsters_rats:0",
     "maxHP": 2,
     "unique": 1,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 1,
      "max": 1
     },
     "spawnGroup": "trainingrat",
     "droplistID": "trainingrat",
     "attackCost": 9,
     "attackChance": 50
    }
    ```


## Brightport, Brightport grave and 2 more (brute_origin1) { #v-brute_origin1 }

**Entry ID:** `brute_origin1` · **Type:** Enemy

**Location:** Brightport: [Brightport grave](../maps/brightport_grave.md), [Brightport school 11](../maps/brightport_school11.md), [Mountainlake 8 cave](../maps/mountainlake8_cave.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 2 |
| XP when defeated | 3 |
| Damage | 1 |
| Attack chance | 50 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 9 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Brightport grave](../maps/brightport_grave.md) | Brightport | 2 | – |
| [Brightport school 11](../maps/brightport_school11.md) | – | 3 | – |
| [Mountainlake 8 cave](../maps/mountainlake8_cave.md) | – | 10 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brute_origin1)"

    | | |
    |---|---|
    | Entry ID | `brute_origin1` |
    | Spawn group | `brute_origin1` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rats:0` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "brute_origin1",
     "name": "Tiny rat",
     "iconID": "monsters_rats:0",
     "maxHP": 2,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 1,
      "max": 1
     },
     "spawnGroup": "brute_origin1",
     "attackCost": 9,
     "attackChance": 50
    }
    ```


## Mountainlake 8 cave (brute_origin1a) { #v-brute_origin1a }

**Entry ID:** `brute_origin1a` · **Type:** NPC

**Location:** [Mountainlake 8 cave](../maps/mountainlake8_cave.md#pin-npc-brute_origin1a)

### Dialogue simulator

Set your quest stages and items, then talk to Tiny rat. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brute_origin1a.json" data-npc="Tiny rat" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (6 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brute_origin1a-brute_origin1a"></span>**`brute_origin1a`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (20%))* → [brute_origin1a_5](#d-brute_origin1a-brute_origin1a_5)
    - branch 2 *(if random chance (25%))* → [brute_origin1a_4](#d-brute_origin1a-brute_origin1a_4)
    - branch 3 *(if random chance (33%))* → [brute_origin1a_3](#d-brute_origin1a-brute_origin1a_3)
    - branch 4 *(if random chance (50%))* → [brute_origin1a_2](#d-brute_origin1a-brute_origin1a_2)
    - branch 5 → [brute_origin1a_1](#d-brute_origin1a-brute_origin1a_1)

    <span id="d-brute_origin1a-brute_origin1a_5"></span>**`brute_origin1a_5`** Tiny rat: “I don't hate you.”


    <span id="d-brute_origin1a-brute_origin1a_4"></span>**`brute_origin1a_4`** Tiny rat: “The cake is a lie.”


    <span id="d-brute_origin1a-brute_origin1a_3"></span>**`brute_origin1a_3`** Tiny rat: “I was told here would be cake.”


    <span id="d-brute_origin1a-brute_origin1a_2"></span>**`brute_origin1a_2`** Tiny rat: “Oh, you are still alive?”


    <span id="d-brute_origin1a-brute_origin1a_1"></span>**`brute_origin1a_1`** Tiny rat: “Well, you found me. Congratulations. Was it worth it?”




### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 6 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brute_origin1a)"

    | | |
    |---|---|
    | Entry ID | `brute_origin1a` |
    | Spawn group | `brute_origin1a` |
    | Loot table | – |
    | Conversation | `brute_origin1a` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rats:0` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "brute_origin1a",
     "name": "Tiny rat",
     "iconID": "monsters_rats:0",
     "monsterClass": "animal",
     "spawnGroup": "brute_origin1a",
     "phraseID": "brute_origin1a"
    }
    ```


## 4 wells, Ratdom maze 567 and 133 more (ratdom_maze_rat1) { #v-ratdom_maze_rat1 }

**Entry ID:** `ratdom_maze_rat1` · **Type:** Enemy

**Location:** 4 wells: [Ratdom maze 567](../maps/ratdom_maze_567.md), 4 wells: [Ratdom maze 658](../maps/ratdom_maze_658.md), 4 wells: [Ratdom maze 768](../maps/ratdom_maze_768.md), Blackwater Mountain: [Ratdom maze 455a](../maps/ratdom_maze_455a.md), Bloskelt + Roskelt: [Ratdom maze 414](../maps/ratdom_maze_414.md), Bloskelt + Roskelt: [Ratdom maze 415](../maps/ratdom_maze_415.md) (+128 more)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 2 |
| XP when defeated | 3 |
| Damage | 1 |
| Attack chance | 50 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 9 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 0 to 2 |
| [Small rat tail](../items/tail_trainingrat.md) | 100% | 1 |

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


??? info "Technical information (ratdom_maze_rat1)"

    | | |
    |---|---|
    | Entry ID | `ratdom_maze_rat1` |
    | Spawn group | `ratdom_maze_rat` |
    | Loot table | `trainingrat` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rats:0` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_maze_rat1",
     "name": "Tiny rat",
     "iconID": "monsters_rats:0",
     "maxHP": 2,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 1,
      "max": 1
     },
     "spawnGroup": "ratdom_maze_rat",
     "droplistID": "trainingrat",
     "attackCost": 9,
     "attackChance": 50
    }
    ```


## Guynmart wood 19 (tobby_trainingrat) { #v-tobby_trainingrat }

**Entry ID:** `tobby_trainingrat` · **Type:** Enemy

**Location:** [Guynmart wood 19](../maps/guynmart_wood_19.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 2 |
| XP when defeated | 3 |
| Damage | 1 |
| Attack chance | 50 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 9 AP |
| Attacks per turn | 1 |
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
| [Guynmart wood 19](../maps/guynmart_wood_19.md) | – | 1 | – |

### Quests that count defeats

- [Sobby's Trail](../quests/tobby.md#stage-21) with [Tobby](../monsters/tobby.md) ([Guynmart wood 19](../maps/guynmart_wood_19.md)) checks that this enemy has been defeated.


### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (tobby_trainingrat)"

    | | |
    |---|---|
    | Entry ID | `tobby_trainingrat` |
    | Spawn group | `tobby_trainingrat` |
    | Loot table | `rat` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rats:0` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "tobby_trainingrat",
     "name": "Tiny rat",
     "iconID": "monsters_rats:0",
     "maxHP": 2,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 1,
      "max": 1
     },
     "spawnGroup": "tobby_trainingrat",
     "droplistID": "rat",
     "attackCost": 9,
     "attackChance": 50
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tiny_rat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tiny_rat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tiny_rat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tiny_rat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
