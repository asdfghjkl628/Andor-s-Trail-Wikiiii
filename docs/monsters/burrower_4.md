---
description: "Giant larval burrower is an enemy in Andor's Trail (insect) with 75–175 HP, worth 159–285 XP, found in Pub, Bloskelt + Roskelt, Entry, Waterwaycave. Drops: Gold coins, Insect shell, Glass gem, Oegyth crystal."
---

# ![](../assets/icons/monsters/monsters_rltiles2_165.png){ .sprite } Giant larval burrower

**Where to find Giant larval burrower:** [Bloskelt + Roskelt, Ratdom maze 437 and 10 more](#v-burrower_4), [Waterwaycave](#v-burrower_cr)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_165.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Pub, Bloskelt + Roskelt, Entry, Waterwaycave |
| **Class** | Insect |
| **HP** | 75–175 |
| **XP when defeated** | 159–285 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Bloskelt + Roskelt, Ratdom maze 437 and 10 more { #v-burrower_4 }

**Where:** Bloskelt + Roskelt: [Ratdom maze 437](../maps/ratdom_maze_437.md), Entry: [Ratdom maze 438](../maps/ratdom_maze_438.md), Entry: [Ratdom maze 635](../maps/ratdom_maze_635.md), Instrument maker: [Ratdom maze 455](../maps/ratdom_maze_455.md), Pub: [Ratdom maze 413](../maps/ratdom_maze_413.md), Pub: [Ratdom maze 432](../maps/ratdom_maze_432.md) (+5 more)

### Combat

| | |
|---|---|
| Class | Insect |
| HP | 75 |
| XP when defeated | 159 |
| Damage | 1 to 25 |
| AC | 95 |
| BC | 80 |
| DR | 2 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 0 to 3 |
| [Insect shell](../items/shell.md) | 30% | 1 |
| [Glass gem](../items/gem1.md) | 5% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Ratdom maze 413](../maps/ratdom_maze_413.md) | Pub | 2 | – |
| [Ratdom maze 432](../maps/ratdom_maze_432.md) | Pub | 2 | – |
| [Ratdom maze 437](../maps/ratdom_maze_437.md) | Bloskelt + Roskelt | 2 | – |
| [Ratdom maze 438](../maps/ratdom_maze_438.md) | Entry | 2 | – |
| [Ratdom maze 455](../maps/ratdom_maze_455.md) | Instrument maker | 2 | – |
| [Ratdom maze 542](../maps/ratdom_maze_542.md) | Skeleton dance | 2 | – |
| [Ratdom maze 566](../maps/ratdom_maze_566.md) | – | 2 | – |
| [Ratdom maze 626](../maps/ratdom_maze_626.md) | Pub | 10 | – |
| [Ratdom maze 635](../maps/ratdom_maze_635.md) | Entry | 2 | – |
| [Ratdom maze 638](../maps/ratdom_maze_638.md) | Roundlings | 2 | – |
| [Waterwaycave](../maps/waterwaycave.md) | – | 8 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Waterwaycave { #v-burrower_cr }

**Where:** [Waterwaycave](../maps/waterwaycave.md)

### Combat

| | |
|---|---|
| Class | Insect |
| HP | 175 |
| XP when defeated | 285 |
| Damage | 1 to 25 |
| AC | 95 |
| BC | 80 |
| DR | 2 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Oegyth crystal](../items/oegyth.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Waterwaycave](../maps/waterwaycave.md) | – | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Giant larval burrower. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: location, combat statistics, loot or shop stock.

| Entry | Type | Section |
|---|---|---|
| `burrower_4` | Enemy | [Bloskelt + Roskelt, Ratdom maze 437 and 10 more](#v-burrower_4) |
| `burrower_cr` | Enemy | [Waterwaycave](#v-burrower_cr) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: burrower_4"

    | | |
    |---|---|
    | Entry ID | `burrower_4` |
    | Type (wiki) | Enemy |
    | Spawn group | `burrower_3` |
    | Loot table | `burrower` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:165` |
    | Defined in | `res/raw/monsterlist_v0611_monsters1.json` |

    Raw data:

    ```json
    {
     "id": "burrower_4",
     "name": "Giant larval burrower",
     "iconID": "monsters_rltiles2:165",
     "maxHP": 75,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "insect",
     "attackDamage": {
      "min": 1,
      "max": 25
     },
     "spawnGroup": "burrower_3",
     "droplistID": "burrower",
     "attackCost": 5,
     "attackChance": 95,
     "blockChance": 80,
     "damageResistance": 2
    }
    ```

??? info "Technical information: burrower_cr"

    | | |
    |---|---|
    | Entry ID | `burrower_cr` |
    | Type (wiki) | Enemy |
    | Spawn group | `burrower_cr` |
    | Loot table | `oegyth1` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:165` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "burrower_cr",
     "name": "Giant larval burrower",
     "iconID": "monsters_rltiles2:165",
     "maxHP": 175,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "insect",
     "attackDamage": {
      "min": 1,
      "max": 25
     },
     "spawnGroup": "burrower_cr",
     "droplistID": "oegyth1",
     "attackCost": 5,
     "attackChance": 95,
     "blockChance": 80,
     "damageResistance": 2
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=burrower_4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=burrower_4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=burrower_4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=burrower_4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
