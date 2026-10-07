---
description: "Frantic forest wasp is an enemy in Andor's Trail (insect) with 29–70 HP, worth 89–246 XP, found in Crossroads Guardhouse. Drops: Gold coins, Insect wing, Giant wasp wing."
---

# ![](../assets/icons/monsters/monsters_insects_1.png){ .sprite } Frantic forest wasp

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_insects_1.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Crossroads Guardhouse |
| **Class** | Insect |
| **HP** | 29–70 |
| **XP when defeated** | 89–246 |
| **Entries in game data** | 4 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "4 entries in the game data"
    The game's data files define 4 separate characters named Frantic forest wasp. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: location, combat statistics, loot or shop stock. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`fieldwasp_0`](#v-fieldwasp_0) | Enemy | Crossroads Guardhouse: [crossroads](../maps/crossroads.md), Crossroads Guardhouse: [fields0](../maps/fields0.md) (+1 more) | – | 29 |
| [`fieldwasp_1`](#v-fieldwasp_1) | Enemy | Crossroads Guardhouse: [fields8](../maps/fields8.md), Crossroads Guardhouse: [roadtocarntower0](../maps/roadtocarntower0.md) | – | 32 |
| [`fieldwasp_2`](#v-fieldwasp_2) | Enemy | Crossroads Guardhouse: [fields9](../maps/fields9.md), Crossroads Guardhouse: [roadtocarntower2](../maps/roadtocarntower2.md) | – | 35 |
| [`fieldwasp_unique`](#v-fieldwasp_unique) | Enemy | Crossroads Guardhouse: [crossroads](../maps/crossroads.md), Crossroads Guardhouse: [fields8](../maps/fields8.md) (+3 more) | – | 70 |

## Crossroads Guardhouse, Crossroads and 2 more (fieldwasp_0) { #v-fieldwasp_0 }

**Entry ID:** `fieldwasp_0` · **Type:** Enemy

**Location:** Crossroads Guardhouse: [crossroads](../maps/crossroads.md), Crossroads Guardhouse: [fields0](../maps/fields0.md), Crossroads Guardhouse: [roadtocarntower1](../maps/roadtocarntower1.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Insect |
| HP | 29 |
| XP when defeated | 89 |
| Damage | 2 to 6 |
| Attack chance | 70 |
| Block chance | 95 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 60 |
| Critical multiplier | 3.0 |
| Critical hit chance | 29% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 0 to 10 |
| [Insect wing](../items/insectwing.md) | 30% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [crossroads](../maps/crossroads.md) | Crossroads Guardhouse | 2 | – |
| [fields0](../maps/fields0.md) | Crossroads Guardhouse | 1 | – |
| [roadtocarntower1](../maps/roadtocarntower1.md) | Crossroads Guardhouse | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | minor data change |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (fieldwasp_0)"

    | | |
    |---|---|
    | Entry ID | `fieldwasp_0` |
    | Spawn group | `fieldwasp_0` |
    | Loot table | `fieldwasp` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_insects:1` |
    | Defined in | `res/raw/monsterlist_v0610_monsters1.json` |

    Raw data:

    ```json
    {
     "id": "fieldwasp_0",
     "name": "Frantic forest wasp",
     "iconID": "monsters_insects:1",
     "maxHP": 29,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "insect",
     "attackDamage": {
      "min": 2,
      "max": 6
     },
     "spawnGroup": "fieldwasp_0",
     "droplistID": "fieldwasp",
     "attackCost": 3,
     "attackChance": 70,
     "criticalSkill": 60,
     "criticalMultiplier": 3.0,
     "blockChance": 95
    }
    ```


## Crossroads Guardhouse, Fields8 and 1 more (fieldwasp_1) { #v-fieldwasp_1 }

**Entry ID:** `fieldwasp_1` · **Type:** Enemy

**Location:** Crossroads Guardhouse: [fields8](../maps/fields8.md), Crossroads Guardhouse: [roadtocarntower0](../maps/roadtocarntower0.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Insect |
| HP | 32 |
| XP when defeated | 106 |
| Damage | 2 to 6 |
| Attack chance | 70 |
| Block chance | 125 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 70 |
| Critical multiplier | 3.0 |
| Critical hit chance | 32% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 0 to 10 |
| [Insect wing](../items/insectwing.md) | 30% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [fields8](../maps/fields8.md) | Crossroads Guardhouse | 6 | – |
| [roadtocarntower0](../maps/roadtocarntower0.md) | Crossroads Guardhouse | 5 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | minor data change |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (fieldwasp_1)"

    | | |
    |---|---|
    | Entry ID | `fieldwasp_1` |
    | Spawn group | `fieldwasp_1` |
    | Loot table | `fieldwasp` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_insects:1` |
    | Defined in | `res/raw/monsterlist_v0610_monsters1.json` |

    Raw data:

    ```json
    {
     "id": "fieldwasp_1",
     "name": "Frantic forest wasp",
     "iconID": "monsters_insects:1",
     "maxHP": 32,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "insect",
     "attackDamage": {
      "min": 2,
      "max": 6
     },
     "spawnGroup": "fieldwasp_1",
     "droplistID": "fieldwasp",
     "attackCost": 3,
     "attackChance": 70,
     "criticalSkill": 70,
     "criticalMultiplier": 3.0,
     "blockChance": 125
    }
    ```


## Crossroads Guardhouse, Fields9 and 1 more (fieldwasp_2) { #v-fieldwasp_2 }

**Entry ID:** `fieldwasp_2` · **Type:** Enemy

**Location:** Crossroads Guardhouse: [fields9](../maps/fields9.md), Crossroads Guardhouse: [roadtocarntower2](../maps/roadtocarntower2.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Insect |
| HP | 35 |
| XP when defeated | 114 |
| Damage | 2 to 6 |
| Attack chance | 70 |
| Block chance | 130 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 75 |
| Critical multiplier | 3.0 |
| Critical hit chance | 33% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 0 to 10 |
| [Insect wing](../items/insectwing.md) | 30% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [fields9](../maps/fields9.md) | Crossroads Guardhouse | 6 | – |
| [roadtocarntower2](../maps/roadtocarntower2.md) | Crossroads Guardhouse | 3 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | minor data change |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (fieldwasp_2)"

    | | |
    |---|---|
    | Entry ID | `fieldwasp_2` |
    | Spawn group | `fieldwasp_2` |
    | Loot table | `fieldwasp` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_insects:1` |
    | Defined in | `res/raw/monsterlist_v0610_monsters1.json` |

    Raw data:

    ```json
    {
     "id": "fieldwasp_2",
     "name": "Frantic forest wasp",
     "iconID": "monsters_insects:1",
     "maxHP": 35,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "insect",
     "attackDamage": {
      "min": 2,
      "max": 6
     },
     "spawnGroup": "fieldwasp_2",
     "droplistID": "fieldwasp",
     "attackCost": 3,
     "attackChance": 70,
     "criticalSkill": 75,
     "criticalMultiplier": 3.0,
     "blockChance": 130
    }
    ```


## Crossroads Guardhouse, Crossroads and 4 more (fieldwasp_unique) { #v-fieldwasp_unique }

**Entry ID:** `fieldwasp_unique` · **Type:** Enemy

**Location:** Crossroads Guardhouse: [crossroads](../maps/crossroads.md), Crossroads Guardhouse: [fields8](../maps/fields8.md), Crossroads Guardhouse: [fields9](../maps/fields9.md), Crossroads Guardhouse: [roadtocarntower0](../maps/roadtocarntower0.md), Crossroads Guardhouse: [roadtocarntower2](../maps/roadtocarntower2.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Insect |
| HP | 70 |
| XP when defeated | 246 |
| Damage | 2 to 6 |
| Attack chance | 70 |
| Block chance | 150 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 200 |
| Critical multiplier | 3.0 |
| Critical hit chance | 58% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 0 to 10 |
| [Giant wasp wing](../items/hadracor_waspwing.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [crossroads](../maps/crossroads.md) | Crossroads Guardhouse | 1 | – |
| [fields8](../maps/fields8.md) | Crossroads Guardhouse | 1 | – |
| [fields9](../maps/fields9.md) | Crossroads Guardhouse | 2 | – |
| [roadtocarntower0](../maps/roadtocarntower0.md) | Crossroads Guardhouse | 1 | – |
| [roadtocarntower2](../maps/roadtocarntower2.md) | Crossroads Guardhouse | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | minor data change |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (fieldwasp_unique)"

    | | |
    |---|---|
    | Entry ID | `fieldwasp_unique` |
    | Spawn group | `fieldwasp_unique` |
    | Loot table | `fieldwasp_unique` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_insects:1` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "fieldwasp_unique",
     "name": "Frantic forest wasp",
     "iconID": "monsters_insects:1",
     "maxHP": 70,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "insect",
     "attackDamage": {
      "min": 2,
      "max": 6
     },
     "spawnGroup": "fieldwasp_unique",
     "droplistID": "fieldwasp_unique",
     "attackCost": 3,
     "attackChance": 70,
     "criticalSkill": 200,
     "criticalMultiplier": 3.0,
     "blockChance": 150
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fieldwasp_0.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fieldwasp_0.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fieldwasp_0.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fieldwasp_0.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
