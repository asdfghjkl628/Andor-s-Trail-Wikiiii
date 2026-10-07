---
description: "Fish is an enemy in Andor's Trail (animal) with 1 HP, worth 1 XP, found in Brimhaven, Guynmart Castle, Guynmart Castle, Lake Laeroth, Remgard, Lake Laeroth, Waterway."
---

# ![](../assets/icons/monsters/monsters_tometik2_30.png){ .sprite } Fish

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik2_30.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Brimhaven, Guynmart Castle, Guynmart Castle, Lake Laeroth, Remgard, Lake Laeroth, Waterway |
| **Class** | Animal, Humanoid |
| **HP** | 1 |
| **XP when defeated** | 1 |
| **Entries in game data** | 12 |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

!!! info "12 entries in the game data"
    The game's data files define 12 separate characters named Fish. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: location, appearance. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`brv_fish1`](#v-brv_fish1) | Enemy | Brimhaven: [brimhaven3](../maps/brimhaven3.md) | – | 1 |
| [`brv_fish2`](#v-brv_fish2) | Enemy | Brimhaven: [brimhaven3](../maps/brimhaven3.md) | – | 1 |
| [`guynmart_fish1`](#v-guynmart_fish1) | Enemy | Guynmart Castle: [guynmart_wood_2](../maps/guynmart_wood_2.md), [blackwater_mountain76](../maps/blackwater_mountain76.md) | – | 1 |
| [`guynmart_fish2`](#v-guynmart_fish2) | Enemy | Guynmart Castle: [guynmart_wood_2](../maps/guynmart_wood_2.md), Guynmart Castle: [guynmart_wood_3](../maps/guynmart_wood_3.md) (+4 more) | – | 1 |
| [`ll2_fish1`](#v-ll2_fish1) | Enemy | Lake Laeroth: [mountainlake2](../maps/mountainlake2.md), Lake Laeroth: [mountainlake21](../maps/mountainlake21.md) (+19 more) | – | 1 |
| [`ll2_fish2`](#v-ll2_fish2) | Enemy | Lake Laeroth: [mountainlake2](../maps/mountainlake2.md), Lake Laeroth: [mountainlake21](../maps/mountainlake21.md) (+19 more) | – | 1 |
| [`ll2_fish3`](#v-ll2_fish3) | Enemy | Lake Laeroth: [mountainlake2](../maps/mountainlake2.md), Lake Laeroth: [mountainlake21](../maps/mountainlake21.md) (+19 more) | – | 1 |
| [`ll2_fish4`](#v-ll2_fish4) | Enemy | Lake Laeroth: [mountainlake2](../maps/mountainlake2.md), Lake Laeroth: [mountainlake21](../maps/mountainlake21.md) (+19 more) | – | 1 |
| [`ll2_fish5`](#v-ll2_fish5) | Enemy | Lake Laeroth: [mountainlake2](../maps/mountainlake2.md), Lake Laeroth: [mountainlake21](../maps/mountainlake21.md) (+19 more) | – | 1 |
| [`ll2_fish6`](#v-ll2_fish6) | Enemy | Lake Laeroth: [mountainlake2](../maps/mountainlake2.md), Lake Laeroth: [mountainlake21](../maps/mountainlake21.md) (+19 more) | – | 1 |
| [`ratdom_water_fish1`](#v-ratdom_water_fish1) | Enemy | Waterway: [ratdom_maze_664](../maps/ratdom_maze_664.md) | – | 1 |
| [`ratdom_water_fish2`](#v-ratdom_water_fish2) | Enemy | Waterway: [ratdom_maze_664](../maps/ratdom_maze_664.md) | – | 1 |

## Brimhaven, Brimhaven3 (brv_fish1) { #v-brv_fish1 }

**Entry ID:** `brv_fish1` · **Type:** Enemy

**Location:** Brimhaven: [brimhaven3](../maps/brimhaven3.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 1 |
| XP when defeated | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [brimhaven3](../maps/brimhaven3.md) | Brimhaven | 2 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brv_fish1)"

    | | |
    |---|---|
    | Entry ID | `brv_fish1` |
    | Spawn group | `brv_fish` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik2:30` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_fish1",
     "name": "Fish",
     "iconID": "monsters_tometik2:30",
     "monsterClass": "animal",
     "spawnGroup": "brv_fish"
    }
    ```


## Brimhaven, Brimhaven3 (brv_fish2) { #v-brv_fish2 }

**Entry ID:** `brv_fish2` · **Type:** Enemy

**Location:** Brimhaven: [brimhaven3](../maps/brimhaven3.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 1 |
| XP when defeated | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [brimhaven3](../maps/brimhaven3.md) | Brimhaven | 2 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brv_fish2)"

    | | |
    |---|---|
    | Entry ID | `brv_fish2` |
    | Spawn group | `brv_fish` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik2:30` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_fish2",
     "name": "Fish",
     "iconID": "monsters_tometik2:30",
     "monsterClass": "animal",
     "spawnGroup": "brv_fish"
    }
    ```


## Guynmart Castle, Guynmart wood 2 and 1 more (guynmart_fish1) { #v-guynmart_fish1 }

**Entry ID:** `guynmart_fish1` · **Type:** Enemy

**Location:** Guynmart Castle: [guynmart_wood_2](../maps/guynmart_wood_2.md), [blackwater_mountain76](../maps/blackwater_mountain76.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 1 |
| XP when defeated | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [blackwater_mountain76](../maps/blackwater_mountain76.md) | – | 1 | – |
| [guynmart_wood_2](../maps/guynmart_wood_2.md) | Guynmart Castle | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_fish1)"

    | | |
    |---|---|
    | Entry ID | `guynmart_fish1` |
    | Spawn group | `guynmart_fish1` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik2:30` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_fish1",
     "name": "Fish",
     "iconID": "monsters_tometik2:30",
     "monsterClass": "animal"
    }
    ```


## Guynmart Castle, Guynmart wood 2 and 5 more (guynmart_fish2) { #v-guynmart_fish2 }

**Entry ID:** `guynmart_fish2` · **Type:** Enemy

**Location:** Guynmart Castle: [guynmart_wood_2](../maps/guynmart_wood_2.md), Guynmart Castle: [guynmart_wood_3](../maps/guynmart_wood_3.md), Lake Laeroth: [laerothisland0](../maps/laerothisland0.md), Lake Laeroth: [laerothisland1](../maps/laerothisland1.md), Lake Laeroth: [mountainlake10a](../maps/mountainlake10a.md), [blackwater_mountain76](../maps/blackwater_mountain76.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 1 |
| XP when defeated | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [blackwater_mountain76](../maps/blackwater_mountain76.md) | – | 1 | – |
| [guynmart_wood_2](../maps/guynmart_wood_2.md) | Guynmart Castle | 3 | – |
| [guynmart_wood_3](../maps/guynmart_wood_3.md) | Guynmart Castle | 2 | – |
| [laerothisland0](../maps/laerothisland0.md) | Lake Laeroth | 4 | – |
| [laerothisland1](../maps/laerothisland1.md) | Lake Laeroth | 3 | – |
| [mountainlake10a](../maps/mountainlake10a.md) | Lake Laeroth | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_fish2)"

    | | |
    |---|---|
    | Entry ID | `guynmart_fish2` |
    | Spawn group | `guynmart_fish2` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `items_misc_2:180` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_fish2",
     "name": "Fish",
     "iconID": "items_misc_2:180",
     "monsterClass": "animal"
    }
    ```


## Lake Laeroth, Mountainlake2 and 20 more (ll2_fish1) { #v-ll2_fish1 }

**Entry ID:** `ll2_fish1` · **Type:** Enemy

**Location:** Lake Laeroth: [mountainlake2](../maps/mountainlake2.md), Lake Laeroth: [mountainlake21](../maps/mountainlake21.md), Lake Laeroth: [mountainlake31](../maps/mountainlake31.md), Lake Laeroth: [mountainlake36](../maps/mountainlake36.md), Lake Laeroth: [mountainlake37](../maps/mountainlake37.md), Remgard: [mountainlake13a](../maps/mountainlake13a.md) (+15 more)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 1 |
| XP when defeated | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [mountainlake13a](../maps/mountainlake13a.md) | Remgard | 3 | – |
| [mountainlake14](../maps/mountainlake14.md) | Remgard | 7 | – |
| [mountainlake15](../maps/mountainlake15.md) | Remgard | 8 | – |
| [mountainlake16](../maps/mountainlake16.md) | Remgard | 6 | – |
| [mountainlake17](../maps/mountainlake17.md) | Remgard | 6 | – |
| [mountainlake18](../maps/mountainlake18.md) | Remgard | 3 | – |
| [mountainlake19](../maps/mountainlake19.md) | – | 5 | – |
| [mountainlake2](../maps/mountainlake2.md) | Lake Laeroth | 3 | – |
| [mountainlake20](../maps/mountainlake20.md) | Remgard | 6 | – |
| [mountainlake21](../maps/mountainlake21.md) | Lake Laeroth | 5 | – |
| [mountainlake22](../maps/mountainlake22.md) | – | 4 | – |
| [mountainlake25](../maps/mountainlake25.md) | – | 3 | – |
| [mountainlake26](../maps/mountainlake26.md) | – | 4 | – |
| [mountainlake28](../maps/mountainlake28.md) | – | 4 | – |
| [mountainlake29](../maps/mountainlake29.md) | – | 5 | – |
| [mountainlake31](../maps/mountainlake31.md) | Lake Laeroth | 3 | – |
| [mountainlake34](../maps/mountainlake34.md) | – | 5 | – |
| [mountainlake35](../maps/mountainlake35.md) | – | 2 | – |
| [mountainlake36](../maps/mountainlake36.md) | Lake Laeroth | 3 | – |
| [mountainlake37](../maps/mountainlake37.md) | Lake Laeroth | 3 | – |
| [remgard1](../maps/remgard1.md) | Remgard | 4 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ll2_fish1)"

    | | |
    |---|---|
    | Entry ID | `ll2_fish1` |
    | Spawn group | `ll2_sealife` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_nut:18` |
    | Defined in | `res/raw/monsterlist_lake_laeroth_2.json` |

    Raw data:

    ```json
    {
     "id": "ll2_fish1",
     "name": "Fish",
     "iconID": "monsters_nut:18",
     "monsterClass": "animal",
     "spawnGroup": "ll2_sealife",
     "horizontalFlipChance": 50
    }
    ```


## Lake Laeroth, Mountainlake2 and 20 more (ll2_fish2) { #v-ll2_fish2 }

**Entry ID:** `ll2_fish2` · **Type:** Enemy

**Location:** Lake Laeroth: [mountainlake2](../maps/mountainlake2.md), Lake Laeroth: [mountainlake21](../maps/mountainlake21.md), Lake Laeroth: [mountainlake31](../maps/mountainlake31.md), Lake Laeroth: [mountainlake36](../maps/mountainlake36.md), Lake Laeroth: [mountainlake37](../maps/mountainlake37.md), Remgard: [mountainlake13a](../maps/mountainlake13a.md) (+15 more)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 1 |
| XP when defeated | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [mountainlake13a](../maps/mountainlake13a.md) | Remgard | 3 | – |
| [mountainlake14](../maps/mountainlake14.md) | Remgard | 7 | – |
| [mountainlake15](../maps/mountainlake15.md) | Remgard | 8 | – |
| [mountainlake16](../maps/mountainlake16.md) | Remgard | 6 | – |
| [mountainlake17](../maps/mountainlake17.md) | Remgard | 6 | – |
| [mountainlake18](../maps/mountainlake18.md) | Remgard | 3 | – |
| [mountainlake19](../maps/mountainlake19.md) | – | 5 | – |
| [mountainlake2](../maps/mountainlake2.md) | Lake Laeroth | 3 | – |
| [mountainlake20](../maps/mountainlake20.md) | Remgard | 6 | – |
| [mountainlake21](../maps/mountainlake21.md) | Lake Laeroth | 5 | – |
| [mountainlake22](../maps/mountainlake22.md) | – | 4 | – |
| [mountainlake25](../maps/mountainlake25.md) | – | 3 | – |
| [mountainlake26](../maps/mountainlake26.md) | – | 4 | – |
| [mountainlake28](../maps/mountainlake28.md) | – | 4 | – |
| [mountainlake29](../maps/mountainlake29.md) | – | 5 | – |
| [mountainlake31](../maps/mountainlake31.md) | Lake Laeroth | 3 | – |
| [mountainlake34](../maps/mountainlake34.md) | – | 5 | – |
| [mountainlake35](../maps/mountainlake35.md) | – | 2 | – |
| [mountainlake36](../maps/mountainlake36.md) | Lake Laeroth | 3 | – |
| [mountainlake37](../maps/mountainlake37.md) | Lake Laeroth | 3 | – |
| [remgard1](../maps/remgard1.md) | Remgard | 4 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ll2_fish2)"

    | | |
    |---|---|
    | Entry ID | `ll2_fish2` |
    | Spawn group | `ll2_sealife` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_nut:18` |
    | Defined in | `res/raw/monsterlist_lake_laeroth_2.json` |

    Raw data:

    ```json
    {
     "id": "ll2_fish2",
     "name": "Fish",
     "iconID": "monsters_nut:18",
     "monsterClass": "animal",
     "spawnGroup": "ll2_sealife",
     "horizontalFlipChance": 50
    }
    ```


## Lake Laeroth, Mountainlake2 and 20 more (ll2_fish3) { #v-ll2_fish3 }

**Entry ID:** `ll2_fish3` · **Type:** Enemy

**Location:** Lake Laeroth: [mountainlake2](../maps/mountainlake2.md), Lake Laeroth: [mountainlake21](../maps/mountainlake21.md), Lake Laeroth: [mountainlake31](../maps/mountainlake31.md), Lake Laeroth: [mountainlake36](../maps/mountainlake36.md), Lake Laeroth: [mountainlake37](../maps/mountainlake37.md), Remgard: [mountainlake13a](../maps/mountainlake13a.md) (+15 more)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 1 |
| XP when defeated | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [mountainlake13a](../maps/mountainlake13a.md) | Remgard | 3 | – |
| [mountainlake14](../maps/mountainlake14.md) | Remgard | 7 | – |
| [mountainlake15](../maps/mountainlake15.md) | Remgard | 8 | – |
| [mountainlake16](../maps/mountainlake16.md) | Remgard | 6 | – |
| [mountainlake17](../maps/mountainlake17.md) | Remgard | 6 | – |
| [mountainlake18](../maps/mountainlake18.md) | Remgard | 3 | – |
| [mountainlake19](../maps/mountainlake19.md) | – | 5 | – |
| [mountainlake2](../maps/mountainlake2.md) | Lake Laeroth | 3 | – |
| [mountainlake20](../maps/mountainlake20.md) | Remgard | 6 | – |
| [mountainlake21](../maps/mountainlake21.md) | Lake Laeroth | 5 | – |
| [mountainlake22](../maps/mountainlake22.md) | – | 4 | – |
| [mountainlake25](../maps/mountainlake25.md) | – | 3 | – |
| [mountainlake26](../maps/mountainlake26.md) | – | 4 | – |
| [mountainlake28](../maps/mountainlake28.md) | – | 4 | – |
| [mountainlake29](../maps/mountainlake29.md) | – | 5 | – |
| [mountainlake31](../maps/mountainlake31.md) | Lake Laeroth | 3 | – |
| [mountainlake34](../maps/mountainlake34.md) | – | 5 | – |
| [mountainlake35](../maps/mountainlake35.md) | – | 2 | – |
| [mountainlake36](../maps/mountainlake36.md) | Lake Laeroth | 3 | – |
| [mountainlake37](../maps/mountainlake37.md) | Lake Laeroth | 3 | – |
| [remgard1](../maps/remgard1.md) | Remgard | 4 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ll2_fish3)"

    | | |
    |---|---|
    | Entry ID | `ll2_fish3` |
    | Spawn group | `ll2_sealife` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_nut:18` |
    | Defined in | `res/raw/monsterlist_lake_laeroth_2.json` |

    Raw data:

    ```json
    {
     "id": "ll2_fish3",
     "name": "Fish",
     "iconID": "monsters_nut:18",
     "monsterClass": "animal",
     "spawnGroup": "ll2_sealife",
     "horizontalFlipChance": 50
    }
    ```


## Lake Laeroth, Mountainlake2 and 20 more (ll2_fish4) { #v-ll2_fish4 }

**Entry ID:** `ll2_fish4` · **Type:** Enemy

**Location:** Lake Laeroth: [mountainlake2](../maps/mountainlake2.md), Lake Laeroth: [mountainlake21](../maps/mountainlake21.md), Lake Laeroth: [mountainlake31](../maps/mountainlake31.md), Lake Laeroth: [mountainlake36](../maps/mountainlake36.md), Lake Laeroth: [mountainlake37](../maps/mountainlake37.md), Remgard: [mountainlake13a](../maps/mountainlake13a.md) (+15 more)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 1 |
| XP when defeated | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [mountainlake13a](../maps/mountainlake13a.md) | Remgard | 3 | – |
| [mountainlake14](../maps/mountainlake14.md) | Remgard | 7 | – |
| [mountainlake15](../maps/mountainlake15.md) | Remgard | 8 | – |
| [mountainlake16](../maps/mountainlake16.md) | Remgard | 6 | – |
| [mountainlake17](../maps/mountainlake17.md) | Remgard | 6 | – |
| [mountainlake18](../maps/mountainlake18.md) | Remgard | 3 | – |
| [mountainlake19](../maps/mountainlake19.md) | – | 5 | – |
| [mountainlake2](../maps/mountainlake2.md) | Lake Laeroth | 3 | – |
| [mountainlake20](../maps/mountainlake20.md) | Remgard | 6 | – |
| [mountainlake21](../maps/mountainlake21.md) | Lake Laeroth | 5 | – |
| [mountainlake22](../maps/mountainlake22.md) | – | 4 | – |
| [mountainlake25](../maps/mountainlake25.md) | – | 3 | – |
| [mountainlake26](../maps/mountainlake26.md) | – | 4 | – |
| [mountainlake28](../maps/mountainlake28.md) | – | 4 | – |
| [mountainlake29](../maps/mountainlake29.md) | – | 5 | – |
| [mountainlake31](../maps/mountainlake31.md) | Lake Laeroth | 3 | – |
| [mountainlake34](../maps/mountainlake34.md) | – | 5 | – |
| [mountainlake35](../maps/mountainlake35.md) | – | 2 | – |
| [mountainlake36](../maps/mountainlake36.md) | Lake Laeroth | 3 | – |
| [mountainlake37](../maps/mountainlake37.md) | Lake Laeroth | 3 | – |
| [remgard1](../maps/remgard1.md) | Remgard | 4 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ll2_fish4)"

    | | |
    |---|---|
    | Entry ID | `ll2_fish4` |
    | Spawn group | `ll2_sealife` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_nut:18` |
    | Defined in | `res/raw/monsterlist_lake_laeroth_2.json` |

    Raw data:

    ```json
    {
     "id": "ll2_fish4",
     "name": "Fish",
     "iconID": "monsters_nut:18",
     "monsterClass": "animal",
     "spawnGroup": "ll2_sealife",
     "horizontalFlipChance": 50
    }
    ```


## Lake Laeroth, Mountainlake2 and 20 more (ll2_fish5) { #v-ll2_fish5 }

**Entry ID:** `ll2_fish5` · **Type:** Enemy

**Location:** Lake Laeroth: [mountainlake2](../maps/mountainlake2.md), Lake Laeroth: [mountainlake21](../maps/mountainlake21.md), Lake Laeroth: [mountainlake31](../maps/mountainlake31.md), Lake Laeroth: [mountainlake36](../maps/mountainlake36.md), Lake Laeroth: [mountainlake37](../maps/mountainlake37.md), Remgard: [mountainlake13a](../maps/mountainlake13a.md) (+15 more)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 1 |
| XP when defeated | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [mountainlake13a](../maps/mountainlake13a.md) | Remgard | 3 | – |
| [mountainlake14](../maps/mountainlake14.md) | Remgard | 7 | – |
| [mountainlake15](../maps/mountainlake15.md) | Remgard | 8 | – |
| [mountainlake16](../maps/mountainlake16.md) | Remgard | 6 | – |
| [mountainlake17](../maps/mountainlake17.md) | Remgard | 6 | – |
| [mountainlake18](../maps/mountainlake18.md) | Remgard | 3 | – |
| [mountainlake19](../maps/mountainlake19.md) | – | 5 | – |
| [mountainlake2](../maps/mountainlake2.md) | Lake Laeroth | 3 | – |
| [mountainlake20](../maps/mountainlake20.md) | Remgard | 6 | – |
| [mountainlake21](../maps/mountainlake21.md) | Lake Laeroth | 5 | – |
| [mountainlake22](../maps/mountainlake22.md) | – | 4 | – |
| [mountainlake25](../maps/mountainlake25.md) | – | 3 | – |
| [mountainlake26](../maps/mountainlake26.md) | – | 4 | – |
| [mountainlake28](../maps/mountainlake28.md) | – | 4 | – |
| [mountainlake29](../maps/mountainlake29.md) | – | 5 | – |
| [mountainlake31](../maps/mountainlake31.md) | Lake Laeroth | 3 | – |
| [mountainlake34](../maps/mountainlake34.md) | – | 5 | – |
| [mountainlake35](../maps/mountainlake35.md) | – | 2 | – |
| [mountainlake36](../maps/mountainlake36.md) | Lake Laeroth | 3 | – |
| [mountainlake37](../maps/mountainlake37.md) | Lake Laeroth | 3 | – |
| [remgard1](../maps/remgard1.md) | Remgard | 4 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ll2_fish5)"

    | | |
    |---|---|
    | Entry ID | `ll2_fish5` |
    | Spawn group | `ll2_sealife` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_nut:18` |
    | Defined in | `res/raw/monsterlist_lake_laeroth_2.json` |

    Raw data:

    ```json
    {
     "id": "ll2_fish5",
     "name": "Fish",
     "iconID": "monsters_nut:18",
     "monsterClass": "animal",
     "spawnGroup": "ll2_sealife",
     "horizontalFlipChance": 50
    }
    ```


## Lake Laeroth, Mountainlake2 and 20 more (ll2_fish6) { #v-ll2_fish6 }

**Entry ID:** `ll2_fish6` · **Type:** Enemy

**Location:** Lake Laeroth: [mountainlake2](../maps/mountainlake2.md), Lake Laeroth: [mountainlake21](../maps/mountainlake21.md), Lake Laeroth: [mountainlake31](../maps/mountainlake31.md), Lake Laeroth: [mountainlake36](../maps/mountainlake36.md), Lake Laeroth: [mountainlake37](../maps/mountainlake37.md), Remgard: [mountainlake13a](../maps/mountainlake13a.md) (+15 more)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 1 |
| XP when defeated | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [mountainlake13a](../maps/mountainlake13a.md) | Remgard | 3 | – |
| [mountainlake14](../maps/mountainlake14.md) | Remgard | 7 | – |
| [mountainlake15](../maps/mountainlake15.md) | Remgard | 8 | – |
| [mountainlake16](../maps/mountainlake16.md) | Remgard | 6 | – |
| [mountainlake17](../maps/mountainlake17.md) | Remgard | 6 | – |
| [mountainlake18](../maps/mountainlake18.md) | Remgard | 3 | – |
| [mountainlake19](../maps/mountainlake19.md) | – | 5 | – |
| [mountainlake2](../maps/mountainlake2.md) | Lake Laeroth | 3 | – |
| [mountainlake20](../maps/mountainlake20.md) | Remgard | 6 | – |
| [mountainlake21](../maps/mountainlake21.md) | Lake Laeroth | 5 | – |
| [mountainlake22](../maps/mountainlake22.md) | – | 4 | – |
| [mountainlake25](../maps/mountainlake25.md) | – | 3 | – |
| [mountainlake26](../maps/mountainlake26.md) | – | 4 | – |
| [mountainlake28](../maps/mountainlake28.md) | – | 4 | – |
| [mountainlake29](../maps/mountainlake29.md) | – | 5 | – |
| [mountainlake31](../maps/mountainlake31.md) | Lake Laeroth | 3 | – |
| [mountainlake34](../maps/mountainlake34.md) | – | 5 | – |
| [mountainlake35](../maps/mountainlake35.md) | – | 2 | – |
| [mountainlake36](../maps/mountainlake36.md) | Lake Laeroth | 3 | – |
| [mountainlake37](../maps/mountainlake37.md) | Lake Laeroth | 3 | – |
| [remgard1](../maps/remgard1.md) | Remgard | 4 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ll2_fish6)"

    | | |
    |---|---|
    | Entry ID | `ll2_fish6` |
    | Spawn group | `ll2_sealife` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_nut:18` |
    | Defined in | `res/raw/monsterlist_lake_laeroth_2.json` |

    Raw data:

    ```json
    {
     "id": "ll2_fish6",
     "name": "Fish",
     "iconID": "monsters_nut:18",
     "monsterClass": "animal",
     "spawnGroup": "ll2_sealife",
     "horizontalFlipChance": 50
    }
    ```


## Waterway, Ratdom maze 664 (ratdom_water_fish1) { #v-ratdom_water_fish1 }

**Entry ID:** `ratdom_water_fish1` · **Type:** Enemy

**Location:** Waterway: [ratdom_maze_664](../maps/ratdom_maze_664.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 1 |
| XP when defeated | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [ratdom_maze_664](../maps/ratdom_maze_664.md) | Waterway | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ratdom_water_fish1)"

    | | |
    |---|---|
    | Entry ID | `ratdom_water_fish1` |
    | Spawn group | `ratdom_water_fish1` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:147` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_water_fish1",
     "name": "Fish",
     "iconID": "monsters_rltiles1:147"
    }
    ```


## Waterway, Ratdom maze 664 (ratdom_water_fish2) { #v-ratdom_water_fish2 }

**Entry ID:** `ratdom_water_fish2` · **Type:** Enemy

**Location:** Waterway: [ratdom_maze_664](../maps/ratdom_maze_664.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 1 |
| XP when defeated | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [ratdom_maze_664](../maps/ratdom_maze_664.md) | Waterway | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ratdom_water_fish2)"

    | | |
    |---|---|
    | Entry ID | `ratdom_water_fish2` |
    | Spawn group | `ratdom_water_fish2` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_snakes:0` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_water_fish2",
     "name": "Fish",
     "iconID": "monsters_snakes:0"
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_fish1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_fish1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_fish1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_fish1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
