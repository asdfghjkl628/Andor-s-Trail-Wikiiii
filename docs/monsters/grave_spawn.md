---
description: "Grave spawn is an enemy in Andor's Trail (demon) with 45 HP, worth 91 XP, found in Prim, Blackwater Mountain, Blackwater Mountain. Drops: Gold coins, Polished gem, Minor vial of health, Bone."
---

# ![](../assets/icons/monsters/monsters_rltiles1_49.png){ .sprite } Grave spawn

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_49.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Prim, Blackwater Mountain, Blackwater Mountain |
| **Class** | Demon |
| **HP** | 45 |
| **XP when defeated** | 91 |
| **Immune to critical hits** | Yes |
| **Entries in game data** | 2 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "2 entries in the game data"
    The game data defines 2 separate characters named Grave spawn. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: location. Each entry has its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`grave_spawn`](#v-grave_spawn) | Enemy | Blackwater Mountain: [Blackwater mountain 51](../maps/blackwater_mountain51.md), Blackwater Mountain: [Blackwater mountain 52](../maps/blackwater_mountain52.md) (+3 more) | – | 45 |
| [`bwm_grave_spawn`](#v-bwm_grave_spawn) | Enemy | Blackwater Mountain: [Blackwater mountain 72](../maps/blackwater_mountain72.md) | – | 45 |

## Blackwater Mountain, Blackwater mountain 51 and 4 more (grave_spawn) { #v-grave_spawn }

**Entry ID:** `grave_spawn` · **Type:** Enemy

**Location:** Blackwater Mountain: [Blackwater mountain 51](../maps/blackwater_mountain51.md), Blackwater Mountain: [Blackwater mountain 52](../maps/blackwater_mountain52.md), Prim: [Blackwater mountain 12](../maps/blackwater_mountain12.md), Prim: [Blackwater mountain 33](../maps/blackwater_mountain33.md), [Blackwater mountain 34](../maps/blackwater_mountain34.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Demon |
| HP | 45 |
| XP when defeated | 91 |
| Damage | 2 to 5 |
| Attack chance | 110 |
| Block chance | 35 |
| Damage resistance | 3 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 40 |
| Critical multiplier | 2.0 |
| Critical hit chance | 23% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 20 to 29 |
| [Polished gem](../items/gem3.md) | 10% | 1 |
| [Minor vial of health](../items/health_minor.md) | 10% | 1 |
| [Bone](../items/bone.md) | 10% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Blackwater mountain 12](../maps/blackwater_mountain12.md) | Prim | 1 | – |
| [Blackwater mountain 33](../maps/blackwater_mountain33.md) | Prim | 7 | – |
| [Blackwater mountain 34](../maps/blackwater_mountain34.md) | – | 4 | – |
| [Blackwater mountain 51](../maps/blackwater_mountain51.md) | Blackwater Mountain | 2 | – |
| [Blackwater mountain 52](../maps/blackwater_mountain52.md) | Blackwater Mountain | 4 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Formatting change only (no gameplay effect) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (grave_spawn)"

    | | |
    |---|---|
    | Entry ID | `grave_spawn` |
    | Spawn group | `restless_dead_1` |
    | Loot table | `restless_dead_1` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:49` |
    | Defined in | `res/raw/monsterlist_v069_monsters.json` |

    Raw data:

    ```json
    {
     "id": "grave_spawn",
     "name": "Grave spawn",
     "iconID": "monsters_rltiles1:49",
     "maxHP": 45,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "demon",
     "attackDamage": {
      "min": 2,
      "max": 5
     },
     "spawnGroup": "restless_dead_1",
     "droplistID": "restless_dead_1",
     "attackCost": 5,
     "attackChance": 110,
     "criticalSkill": 40,
     "criticalMultiplier": 2.0,
     "blockChance": 35,
     "damageResistance": 3
    }
    ```


## Blackwater Mountain, Blackwater mountain 72 (bwm_grave_spawn) { #v-bwm_grave_spawn }

**Entry ID:** `bwm_grave_spawn` · **Type:** Enemy

**Location:** Blackwater Mountain: [Blackwater mountain 72](../maps/blackwater_mountain72.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Demon |
| HP | 45 |
| XP when defeated | 91 |
| Damage | 2 to 5 |
| Attack chance | 110 |
| Block chance | 35 |
| Damage resistance | 3 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 40 |
| Critical multiplier | 2.0 |
| Critical hit chance | 23% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 20 to 29 |
| [Polished gem](../items/gem3.md) | 10% | 1 |
| [Minor vial of health](../items/health_minor.md) | 10% | 1 |
| [Bone](../items/bone.md) | 10% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Blackwater mountain 72](../maps/blackwater_mountain72.md) | Blackwater Mountain | 3 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (bwm_grave_spawn)"

    | | |
    |---|---|
    | Entry ID | `bwm_grave_spawn` |
    | Spawn group | `bwm_grave_spawn` |
    | Loot table | `restless_dead_1` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:49` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "bwm_grave_spawn",
     "name": "Grave spawn",
     "iconID": "monsters_rltiles1:49",
     "maxHP": 45,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "demon",
     "attackDamage": {
      "min": 2,
      "max": 5
     },
     "spawnGroup": "bwm_grave_spawn",
     "droplistID": "restless_dead_1",
     "attackCost": 5,
     "attackChance": 110,
     "criticalSkill": 40,
     "criticalMultiplier": 2.0,
     "blockChance": 35,
     "damageResistance": 3
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=grave_spawn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=grave_spawn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=grave_spawn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=grave_spawn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
