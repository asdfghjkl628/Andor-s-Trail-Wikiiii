---
description: "Strong larval burrower is an enemy in Andor's Trail (insect) with 35–44 HP, worth 67–120 XP, found in Brimhaven, Crossroads Guardhouse. Drops: Gold coins, Insect shell, Glass gem, Ruby gem."
---

# ![](../assets/icons/monsters/monsters_rltiles2_165.png){ .sprite } Strong larval burrower

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_165.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Brimhaven, Crossroads Guardhouse |
| **Class** | Insect |
| **HP** | 35–44 |
| **XP when defeated** | 67–120 |
| **Entries in game data** | 2 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "2 entries in the game data"
    The game data defines 2 separate characters named Strong larval burrower. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: location, combat statistics, loot or shop stock, appearance. Each entry has its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`burrower_3`](#v-burrower_3) | Enemy | Brimhaven: [Waterway 6](../maps/waterway6.md), [Waterway 14](../maps/waterway14.md) (+2 more) | – | 44 |
| [`larval_boss`](#v-larval_boss) | Enemy | Crossroads Guardhouse: [Woodcave 1](../maps/woodcave1.md) | – | 35 |

## Brimhaven, Waterway 6 and 3 more (burrower_3) { #v-burrower_3 }

**Entry ID:** `burrower_3` · **Type:** Enemy

**Location:** Brimhaven: [Waterway 6](../maps/waterway6.md), [Waterway 14](../maps/waterway14.md), [Waterway 15](../maps/waterway15.md), [Waterwaycave](../maps/waterwaycave.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Insect |
| HP | 44 |
| XP when defeated | 120 |
| Damage | 1 to 25 |
| Attack chance | 95 |
| Block chance | 80 |
| Damage resistance | 2 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 0 to 3 |
| [Insect shell](../items/shell.md) | 30% | 1 |
| [Glass gem](../items/gem1.md) | 5% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Waterway 14](../maps/waterway14.md) | – | 3 | – |
| [Waterway 15](../maps/waterway15.md) | – | 4 | – |
| [Waterway 6](../maps/waterway6.md) | Brimhaven | 2 | – |
| [Waterwaycave](../maps/waterwaycave.md) | – | 4 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (burrower_3)"

    | | |
    |---|---|
    | Entry ID | `burrower_3` |
    | Spawn group | `burrower_2` |
    | Loot table | `burrower` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:165` |
    | Defined in | `res/raw/monsterlist_v0611_monsters1.json` |

    Raw data:

    ```json
    {
     "id": "burrower_3",
     "name": "Strong larval burrower",
     "iconID": "monsters_rltiles2:165",
     "maxHP": 44,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "insect",
     "attackDamage": {
      "min": 1,
      "max": 25
     },
     "spawnGroup": "burrower_2",
     "droplistID": "burrower",
     "attackCost": 5,
     "attackChance": 95,
     "blockChance": 80,
     "damageResistance": 2
    }
    ```


## Crossroads Guardhouse, Woodcave 1 (larval_boss) { #v-larval_boss }

**Entry ID:** `larval_boss` · **Type:** Enemy

**Location:** Crossroads Guardhouse: [Woodcave 1](../maps/woodcave1.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Insect |
| HP | 35 |
| XP when defeated | 67 |
| Damage | 1 to 6 |
| Attack chance | 120 |
| Block chance | 25 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 35 |
| Critical multiplier | 3.0 |
| Critical hit chance | 21% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 0 to 9 |
| [Ruby gem](../items/gem2.md) | 100% | 1 |
| [Minor vial of health](../items/health_minor.md) | 100% | 1 |
| [Erinith's book](../items/erinith_book.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Woodcave 1](../maps/woodcave1.md) | Crossroads Guardhouse | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Formatting change only (no gameplay effect) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (larval_boss)"

    | | |
    |---|---|
    | Entry ID | `larval_boss` |
    | Spawn group | `larva_boss` |
    | Loot table | `larva_boss` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:164` |
    | Defined in | `res/raw/monsterlist_v0610_monsters1.json` |

    Raw data:

    ```json
    {
     "id": "larval_boss",
     "name": "Strong larval burrower",
     "iconID": "monsters_rltiles2:164",
     "maxHP": 35,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "insect",
     "attackDamage": {
      "min": 1,
      "max": 6
     },
     "spawnGroup": "larva_boss",
     "droplistID": "larva_boss",
     "attackCost": 5,
     "attackChance": 120,
     "criticalSkill": 35,
     "criticalMultiplier": 3.0,
     "blockChance": 25
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=burrower_3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=burrower_3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=burrower_3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=burrower_3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
