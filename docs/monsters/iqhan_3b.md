---
description: "Iqhan master is an enemy in Andor's Trail (humanoid) with 67–71 HP, worth 162–185 XP, found in pwcave1, pwcave2, pwcave3, pwcave2, pwcave2a, pwcave3. Drops: Gold coins, Iqhan pendant, Torn shirt, Iron dagger."
---

# ![](../assets/icons/monsters/monsters_rltiles2_129.png){ .sprite } Iqhan master

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_129.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | pwcave1, pwcave2, pwcave3, pwcave2, pwcave2a, pwcave3 |
| **Class** | Humanoid |
| **HP** | 67–71 |
| **XP when defeated** | 162–185 |
| **Entries in game data** | 3 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "3 entries in the game data"
    The game's data files define 3 separate characters named Iqhan master. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: location, combat statistics, loot or shop stock, appearance. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`iqhan_3b`](#v-iqhan_3b) | Enemy | [pwcave1](../maps/pwcave1.md), [pwcave2](../maps/pwcave2.md) (+1 more) | – | 67 |
| [`iqhan_4a`](#v-iqhan_4a) | Enemy | [pwcave2](../maps/pwcave2.md), [pwcave2a](../maps/pwcave2a.md) (+2 more) | – | 69 |
| [`iqhan_4b`](#v-iqhan_4b) | Enemy | [pwcave2](../maps/pwcave2.md), [pwcave2a](../maps/pwcave2a.md) (+2 more) | – | 71 |

## Pwcave1 and 2 more (iqhan_3b) { #v-iqhan_3b }

**Entry ID:** `iqhan_3b` · **Type:** Enemy

**Location:** [pwcave1](../maps/pwcave1.md), [pwcave2](../maps/pwcave2.md), [pwcave3](../maps/pwcave3.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 67 |
| XP when defeated | 162 |
| Damage | 2 to 12 |
| Attack chance | 140 |
| Block chance | 60 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 20 |
| Critical multiplier | 2.0 |
| Critical hit chance | 15% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 1 to 5 |
| [Iqhan pendant](../items/iqhan_pendant.md) | 1% | 1 |
| [Torn shirt](../items/shirt_torn.md) | 5% | 1 |
| [Iron dagger](../items/dagger0.md) | 5% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [pwcave1](../maps/pwcave1.md) | – | 1 | – |
| [pwcave2](../maps/pwcave2.md) | – | 12 | – |
| [pwcave3](../maps/pwcave3.md) | – | 4 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | minor data change |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (iqhan_3b)"

    | | |
    |---|---|
    | Entry ID | `iqhan_3b` |
    | Spawn group | `iqhan_3` |
    | Loot table | `iqhan_lesser` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:129` |
    | Defined in | `res/raw/monsterlist_v0610_monsters2.json` |

    Raw data:

    ```json
    {
     "id": "iqhan_3b",
     "name": "Iqhan master",
     "iconID": "monsters_rltiles2:129",
     "maxHP": 67,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 2,
      "max": 12
     },
     "spawnGroup": "iqhan_3",
     "droplistID": "iqhan_lesser",
     "attackCost": 3,
     "attackChance": 140,
     "criticalSkill": 20,
     "criticalMultiplier": 2.0,
     "blockChance": 60
    }
    ```


## Pwcave2 and 3 more (iqhan_4a) { #v-iqhan_4a }

**Entry ID:** `iqhan_4a` · **Type:** Enemy

**Location:** [pwcave2](../maps/pwcave2.md), [pwcave2a](../maps/pwcave2a.md), [pwcave3](../maps/pwcave3.md), [pwcave4](../maps/pwcave4.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 69 |
| XP when defeated | 170 |
| Damage | 2 to 13 |
| Attack chance | 140 |
| Block chance | 60 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 20 |
| Critical multiplier | 2.0 |
| Critical hit chance | 15% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 1 to 5 |
| [Iqhan pendant](../items/iqhan_pendant.md) | 1% | 1 |
| [Torn shirt](../items/shirt_torn.md) | 5% | 1 |
| [Iron dagger](../items/dagger0.md) | 5% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [pwcave2](../maps/pwcave2.md) | – | 7 | – |
| [pwcave2a](../maps/pwcave2a.md) | – | 1 | – |
| [pwcave3](../maps/pwcave3.md) | – | 8 | – |
| [pwcave4](../maps/pwcave4.md) | – | 2 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | minor data change |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (iqhan_4a)"

    | | |
    |---|---|
    | Entry ID | `iqhan_4a` |
    | Spawn group | `iqhan_4` |
    | Loot table | `iqhan_lesser` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:129` |
    | Defined in | `res/raw/monsterlist_v0610_monsters2.json` |

    Raw data:

    ```json
    {
     "id": "iqhan_4a",
     "name": "Iqhan master",
     "iconID": "monsters_rltiles2:129",
     "maxHP": 69,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 2,
      "max": 13
     },
     "spawnGroup": "iqhan_4",
     "droplistID": "iqhan_lesser",
     "attackCost": 3,
     "attackChance": 140,
     "criticalSkill": 20,
     "criticalMultiplier": 2.0,
     "blockChance": 60
    }
    ```


## Pwcave2 and 3 more (iqhan_4b) { #v-iqhan_4b }

**Entry ID:** `iqhan_4b` · **Type:** Enemy

**Location:** [pwcave2](../maps/pwcave2.md), [pwcave2a](../maps/pwcave2a.md), [pwcave3](../maps/pwcave3.md), [pwcave4](../maps/pwcave4.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 71 |
| XP when defeated | 185 |
| Damage | 2 to 15 |
| Attack chance | 140 |
| Block chance | 60 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 20 |
| Critical multiplier | 2.0 |
| Critical hit chance | 15% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 1 to 9 |
| [Iqhan pendant](../items/iqhan_pendant.md) | 5% | 1 |
| [Wooden buckler](../items/shield1.md) | 5% | 1 |
| [Iron dagger](../items/dagger0.md) | 5% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [pwcave2](../maps/pwcave2.md) | – | 7 | – |
| [pwcave2a](../maps/pwcave2a.md) | – | 1 | – |
| [pwcave3](../maps/pwcave3.md) | – | 8 | – |
| [pwcave4](../maps/pwcave4.md) | – | 2 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | minor data change |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (iqhan_4b)"

    | | |
    |---|---|
    | Entry ID | `iqhan_4b` |
    | Spawn group | `iqhan_4` |
    | Loot table | `iqhan` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:133` |
    | Defined in | `res/raw/monsterlist_v0610_monsters2.json` |

    Raw data:

    ```json
    {
     "id": "iqhan_4b",
     "name": "Iqhan master",
     "iconID": "monsters_rltiles2:133",
     "maxHP": 71,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 2,
      "max": 15
     },
     "spawnGroup": "iqhan_4",
     "droplistID": "iqhan",
     "attackCost": 3,
     "attackChance": 140,
     "criticalSkill": 20,
     "criticalMultiplier": 2.0,
     "blockChance": 60
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_3b.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_3b.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_3b.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_3b.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
