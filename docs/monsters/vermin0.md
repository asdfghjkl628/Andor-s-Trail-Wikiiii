---
description: "Rat is an enemy in Andor's Trail (animal) with 5 HP, worth 7 XP, found in Fallhaven, Prim, Crossroads Guardhouse, Remgard, Wexlow Village. Drops: Gold coins, Glass gem, Rat tail."
---

# ![](../assets/icons/monsters/monsters_rats_0.png){ .sprite } Rat

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rats_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Fallhaven, Prim, Crossroads Guardhouse, Remgard, Wexlow Village |
| **Class** | Animal |
| **HP** | 5 |
| **XP when defeated** | 7 |
| **Entries in game data** | 3 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "3 entries in the game data"
    The game's data files define 3 separate characters named Rat. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: location, combat statistics, loot or shop stock, appearance. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`vermin0`](#v-vermin0) | Enemy | Fallhaven: [gapfillerhole](../maps/gapfillerhole.md), Fallhaven: [woodhouse2](../maps/woodhouse2.md) (+3 more) | – | 1 |
| [`crossroads_rat`](#v-crossroads_rat) | Enemy | Crossroads Guardhouse: [houseatcrossroads1](../maps/houseatcrossroads1.md), Remgard: [island_underground1](../maps/island_underground1.md) (+7 more) | – | 5 |
| [`vermin1`](#v-vermin1) | Enemy | Fallhaven: [gapfillerhole](../maps/gapfillerhole.md), Fallhaven: [woodhouse2](../maps/woodhouse2.md) (+3 more) | – | 1 |

## Fallhaven, Gapfillerhole and 4 more (vermin0) { #v-vermin0 }

**Entry ID:** `vermin0` · **Type:** Enemy

**Location:** Fallhaven: [gapfillerhole](../maps/gapfillerhole.md), Fallhaven: [woodhouse2](../maps/woodhouse2.md), Fallhaven: [woodsettlement0](../maps/woodsettlement0.md), Prim: [lodarhouse1](../maps/lodarhouse1.md), [woodhouse3](../maps/woodhouse3.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 1 |
| XP when defeated | 1 |
| Damage | 0 to 1 |
| Attack chance | 10 |
| Block chance | 5 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 20% | 0 to 1 |
| [Glass gem](../items/gem1.md) | 5% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [gapfillerhole](../maps/gapfillerhole.md) | Fallhaven | 1 | – |
| [lodarhouse1](../maps/lodarhouse1.md) | Prim | 2 | – |
| [woodhouse2](../maps/woodhouse2.md) | Fallhaven | 2 | – |
| [woodhouse3](../maps/woodhouse3.md) | – | 2 | – |
| [woodsettlement0](../maps/woodsettlement0.md) | Fallhaven | 4 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | attackDamage: {"max": 1} → {"max": 1, "min": 0} |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (vermin0)"

    | | |
    |---|---|
    | Entry ID | `vermin0` |
    | Spawn group | `vermin` |
    | Loot table | `vermin` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rats:0` |
    | Defined in | `res/raw/monsterlist_v070_lodarmaze.json` |

    Raw data:

    ```json
    {
     "id": "vermin0",
     "name": "Rat",
     "iconID": "monsters_rats:0",
     "monsterClass": "animal",
     "attackDamage": {
      "min": 0,
      "max": 1
     },
     "spawnGroup": "vermin",
     "droplistID": "vermin",
     "attackCost": 4,
     "attackChance": 10,
     "blockChance": 5
    }
    ```


## Crossroads Guardhouse, Houseatcrossroads1 and 8 more (crossroads_rat) { #v-crossroads_rat }

**Entry ID:** `crossroads_rat` · **Type:** Enemy

**Location:** Crossroads Guardhouse: [houseatcrossroads1](../maps/houseatcrossroads1.md), Remgard: [island_underground1](../maps/island_underground1.md), Remgard: [remgard_church_basement](../maps/remgard_church_basement.md), Wexlow Village: [wexlow_village](../maps/wexlow_village.md), [island_underground4b](../maps/island_underground4b.md), [island_underground5](../maps/island_underground5.md) (+3 more)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 5 |
| XP when defeated | 7 |
| Damage | 1 |
| Attack chance | 50 |
| Block chance | 30 |
| Damage resistance | 0 |
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
| [Gold coins](../items/gold.md) | 100% | 2 to 4 |
| [Rat tail](../items/rat_tail.md) | 30% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [houseatcrossroads1](../maps/houseatcrossroads1.md) | Crossroads Guardhouse | 1 | – |
| [island_underground1](../maps/island_underground1.md) | Remgard | 2 | – |
| [island_underground4b](../maps/island_underground4b.md) | – | 2 | – |
| [island_underground5](../maps/island_underground5.md) | – | 8 | – |
| [korhald_cave2](../maps/korhald_cave2.md) | – | 1 | – |
| [korhald_cave_hidden](../maps/korhald_cave_hidden.md) | – | 4 | – |
| [remgard_church_basement](../maps/remgard_church_basement.md) | Remgard | 3 | – |
| [wayto_feygard_duleian_2](../maps/wayto_feygard_duleian_2.md) | – | 1 | – |
| [wexlow_village](../maps/wexlow_village.md) | Wexlow Village | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (crossroads_rat)"

    | | |
    |---|---|
    | Entry ID | `crossroads_rat` |
    | Spawn group | `crossroads_rat` |
    | Loot table | `rat` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rats:0` |
    | Defined in | `res/raw/monsterlist_v0610_monsters1.json` |

    Raw data:

    ```json
    {
     "id": "crossroads_rat",
     "name": "Rat",
     "iconID": "monsters_rats:0",
     "maxHP": 5,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 1,
      "max": 1
     },
     "spawnGroup": "crossroads_rat",
     "droplistID": "rat",
     "attackCost": 5,
     "attackChance": 50,
     "blockChance": 30
    }
    ```


## Fallhaven, Gapfillerhole and 4 more (vermin1) { #v-vermin1 }

**Entry ID:** `vermin1` · **Type:** Enemy

**Location:** Fallhaven: [gapfillerhole](../maps/gapfillerhole.md), Fallhaven: [woodhouse2](../maps/woodhouse2.md), Fallhaven: [woodsettlement0](../maps/woodsettlement0.md), Prim: [lodarhouse1](../maps/lodarhouse1.md), [woodhouse3](../maps/woodhouse3.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 1 |
| XP when defeated | 1 |
| Damage | 0 to 1 |
| Attack chance | 10 |
| Block chance | 5 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 20% | 0 to 1 |
| [Glass gem](../items/gem1.md) | 5% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [gapfillerhole](../maps/gapfillerhole.md) | Fallhaven | 1 | – |
| [lodarhouse1](../maps/lodarhouse1.md) | Prim | 2 | – |
| [woodhouse2](../maps/woodhouse2.md) | Fallhaven | 2 | – |
| [woodhouse3](../maps/woodhouse3.md) | – | 2 | – |
| [woodsettlement0](../maps/woodsettlement0.md) | Fallhaven | 4 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | attackDamage: {"max": 1} → {"max": 1, "min": 0} |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (vermin1)"

    | | |
    |---|---|
    | Entry ID | `vermin1` |
    | Spawn group | `vermin` |
    | Loot table | `vermin` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:145` |
    | Defined in | `res/raw/monsterlist_v070_lodarmaze.json` |

    Raw data:

    ```json
    {
     "id": "vermin1",
     "name": "Rat",
     "iconID": "monsters_rltiles2:145",
     "monsterClass": "animal",
     "attackDamage": {
      "min": 0,
      "max": 1
     },
     "spawnGroup": "vermin",
     "droplistID": "vermin",
     "attackCost": 4,
     "attackChance": 10,
     "blockChance": 5
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vermin0.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vermin0.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vermin0.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vermin0.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
