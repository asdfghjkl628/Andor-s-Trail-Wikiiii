---
description: "Izthiel guardian is an enemy in Andor's Trail (reptile) with 54–354 HP, worth 218–554 XP, found in Brimhaven, waterway10. Drops: Gold coins, Izthiel claw, Jinxed ring of damage resistance, Polished ring."
---

# ![](../assets/icons/monsters/monsters_rltiles2_52.png){ .sprite } Izthiel guardian

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_52.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Brimhaven, waterway10 |
| **Class** | Reptile |
| **HP** | 54–354 |
| **XP when defeated** | 218–554 |
| **Entries in game data** | 2 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Izthiel guardian. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: location, combat statistics, loot or shop stock. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`izthiel_4`](#v-izthiel_4) | Enemy | Brimhaven: [waterway6](../maps/waterway6.md), [waterway1](../maps/waterway1.md) (+5 more) | – | 54 |
| [`izthiel_cr`](#v-izthiel_cr) | Enemy | [waterway10](../maps/waterway10.md) | – | 354 |

## Brimhaven, Waterway6 and 6 more (izthiel_4) { #v-izthiel_4 }

**Entry ID:** `izthiel_4` · **Type:** Enemy

**Location:** Brimhaven: [waterway6](../maps/waterway6.md), [waterway1](../maps/waterway1.md), [waterway4](../maps/waterway4.md), [waterway5](../maps/waterway5.md), [waterway8](../maps/waterway8.md), [waterway9](../maps/waterway9.md) (+1 more)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Reptile |
| HP | 54 |
| XP when defeated | 218 |
| Damage | 3 to 7 |
| Attack chance | 120 |
| Block chance | 60 |
| Damage resistance | 11 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

**On hit:** On target: [Bleeding wound](../conditions/bleeding_wound.md) (magnitude 3, 5 rounds, 50% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 3 to 40 |
| [Izthiel claw](../items/izthiel_claw.md) | 30% | 1 |
| [Jinxed ring of damage resistance](../items/ring_jinxed1.md) | 1% | 1 |
| [Polished ring](../items/ring2.md) | 20% | 1 |
| [Shadowfang](../items/shadowfang.md) | 0.1% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [waterway1](../maps/waterway1.md) | – | 1 | – |
| [waterway4](../maps/waterway4.md) | – | 2 | – |
| [waterway5](../maps/waterway5.md) | – | 4 | – |
| [waterway6](../maps/waterway6.md) | Brimhaven | 2 | – |
| [waterway8](../maps/waterway8.md) | – | 2 | – |
| [waterway9](../maps/waterway9.md) | – | 3 | – |
| [waterwayextention](../maps/waterwayextention.md) | – | 2 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Bleeding wound](../conditions/bleeding_wound.md) (magnitude 3, 5 rounds, 50% chance) → (magnitude 3, 5 rounds, 50% chance)<br>Renamed “Izthiel Guardian” → “Izthiel guardian” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (izthiel_4)"

    | | |
    |---|---|
    | Entry ID | `izthiel_4` |
    | Spawn group | `izthiel_4` |
    | Loot table | `izthiel_4` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:52` |
    | Defined in | `res/raw/monsterlist_v0610_monsters1.json` |

    Raw data:

    ```json
    {
     "id": "izthiel_4",
     "name": "Izthiel guardian",
     "iconID": "monsters_rltiles2:52",
     "maxHP": 54,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 3,
      "max": 7
     },
     "spawnGroup": "izthiel_4",
     "droplistID": "izthiel_4",
     "attackCost": 3,
     "attackChance": 120,
     "blockChance": 60,
     "damageResistance": 11,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "bleeding_wound",
        "magnitude": 3,
        "duration": 5,
        "chance": "50"
       }
      ]
     }
    }
    ```


## Waterway10 (izthiel_cr) { #v-izthiel_cr }

**Entry ID:** `izthiel_cr` · **Type:** Enemy

**Location:** [waterway10](../maps/waterway10.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Reptile |
| HP | 354 |
| XP when defeated | 554 |
| Damage | 3 to 7 |
| Attack chance | 120 |
| Block chance | 60 |
| Damage resistance | 11 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

**On hit:** On target: [Bleeding wound](../conditions/bleeding_wound.md) (magnitude 3, 5 rounds, 50% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Oegyth crystal](../items/oegyth.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [waterway10](../maps/waterway10.md) | – | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Bleeding wound](../conditions/bleeding_wound.md) (magnitude 3, 5 rounds, 50% chance) → (magnitude 3, 5 rounds, 50% chance)<br>Renamed “Izthiel Guardian” → “Izthiel guardian” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (izthiel_cr)"

    | | |
    |---|---|
    | Entry ID | `izthiel_cr` |
    | Spawn group | `izthiel_cr` |
    | Loot table | `oegyth1` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:52` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "izthiel_cr",
     "name": "Izthiel guardian",
     "iconID": "monsters_rltiles2:52",
     "maxHP": 354,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 3,
      "max": 7
     },
     "spawnGroup": "izthiel_cr",
     "droplistID": "oegyth1",
     "attackCost": 3,
     "attackChance": 120,
     "blockChance": 60,
     "damageResistance": 11,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "bleeding_wound",
        "magnitude": 3,
        "duration": 5,
        "chance": "50"
       }
      ]
     }
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=izthiel_4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=izthiel_4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=izthiel_4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=izthiel_4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
