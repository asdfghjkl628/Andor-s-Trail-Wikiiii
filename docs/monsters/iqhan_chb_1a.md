---
description: "Iqhan chaos beast is an enemy in Andor's Trail (construct) with 122–140 HP, worth 262–280 XP, found in pwcave2a, pwcave4. Drops: Gold coins, Chaosreaper, Regular potion of health."
---

# ![](../assets/icons/monsters/monsters_rltiles1_19.png){ .sprite } Iqhan chaos beast

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_19.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | pwcave2a, pwcave4 |
| **Class** | Construct |
| **HP** | 122–140 |
| **XP when defeated** | 262–280 |
| **Immune to critical hits** | Yes |
| **Entries in game data** | 2 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Iqhan chaos beast. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: combat statistics. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`iqhan_chb_1a`](#v-iqhan_chb_1a) | Enemy | [pwcave2a](../maps/pwcave2a.md), [pwcave4](../maps/pwcave4.md) | – | 122 |
| [`iqhan_chb_1b`](#v-iqhan_chb_1b) | Enemy | [pwcave2a](../maps/pwcave2a.md), [pwcave4](../maps/pwcave4.md) | – | 140 |

## Pwcave2a and 1 more (iqhan_chb_1a) { #v-iqhan_chb_1a }

**Entry ID:** `iqhan_chb_1a` · **Type:** Enemy

**Location:** [pwcave2a](../maps/pwcave2a.md), [pwcave4](../maps/pwcave4.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Construct |
| HP | 122 |
| XP when defeated | 262 |
| Damage | 0 to 15 |
| Attack chance | 150 |
| Block chance | 45 |
| Damage resistance | 9 |
| Max AP | 10 |
| Attack cost | 9 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 10 |
| Critical multiplier | 3.0 |
| Critical hit chance | 9% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.

**On hit:** On target: Chaotic grip (magnitude 5, 5 rounds, 50% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 0 to 1 |
| [Chaosreaper](../items/chaosreaper.md) | 0.1% | 1 |
| [Regular potion of health](../items/health.md) | 5% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [pwcave2a](../maps/pwcave2a.md) | – | 1 | – |
| [pwcave4](../maps/pwcave4.md) | – | 7 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | hitEffect: {"conditionsTarget": [{"chance": 50, "c… → {"conditionsTarget": [{"chance": "50", … |
| [v0.7.4](../versions/0.7.4.md) | attackCost: 10 → 9 |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (iqhan_chb_1a)"

    | | |
    |---|---|
    | Entry ID | `iqhan_chb_1a` |
    | Spawn group | `iqhan_chb_1` |
    | Loot table | `iqhan_beast` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:19` |
    | Defined in | `res/raw/monsterlist_v0610_monsters2.json` |

    Raw data:

    ```json
    {
     "id": "iqhan_chb_1a",
     "name": "Iqhan chaos beast",
     "iconID": "monsters_rltiles1:19",
     "maxHP": 122,
     "maxAP": 10,
     "moveCost": 10,
     "monsterClass": "construct",
     "attackDamage": {
      "min": 0,
      "max": 15
     },
     "spawnGroup": "iqhan_chb_1",
     "droplistID": "iqhan_beast",
     "attackCost": 9,
     "attackChance": 150,
     "criticalSkill": 10,
     "criticalMultiplier": 3.0,
     "blockChance": 45,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "chaotic_grip",
        "magnitude": 5,
        "duration": 5,
        "chance": "50"
       }
      ]
     }
    }
    ```


## Pwcave2a and 1 more (iqhan_chb_1b) { #v-iqhan_chb_1b }

**Entry ID:** `iqhan_chb_1b` · **Type:** Enemy

**Location:** [pwcave2a](../maps/pwcave2a.md), [pwcave4](../maps/pwcave4.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Construct |
| HP | 140 |
| XP when defeated | 280 |
| Damage | 0 to 15 |
| Attack chance | 150 |
| Block chance | 45 |
| Damage resistance | 9 |
| Max AP | 10 |
| Attack cost | 9 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 10 |
| Critical multiplier | 3.0 |
| Critical hit chance | 9% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.

**On hit:** On target: Chaotic grip (magnitude 5, 5 rounds, 50% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 0 to 1 |
| [Chaosreaper](../items/chaosreaper.md) | 0.1% | 1 |
| [Regular potion of health](../items/health.md) | 5% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [pwcave2a](../maps/pwcave2a.md) | – | 1 | – |
| [pwcave4](../maps/pwcave4.md) | – | 7 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | hitEffect: {"conditionsTarget": [{"chance": 50, "c… → {"conditionsTarget": [{"chance": "50", … |
| [v0.7.4](../versions/0.7.4.md) | attackCost: 10 → 9 |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (iqhan_chb_1b)"

    | | |
    |---|---|
    | Entry ID | `iqhan_chb_1b` |
    | Spawn group | `iqhan_chb_1` |
    | Loot table | `iqhan_beast` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:19` |
    | Defined in | `res/raw/monsterlist_v0610_monsters2.json` |

    Raw data:

    ```json
    {
     "id": "iqhan_chb_1b",
     "name": "Iqhan chaos beast",
     "iconID": "monsters_rltiles1:19",
     "maxHP": 140,
     "maxAP": 10,
     "moveCost": 10,
     "monsterClass": "construct",
     "attackDamage": {
      "min": 0,
      "max": 15
     },
     "spawnGroup": "iqhan_chb_1",
     "droplistID": "iqhan_beast",
     "attackCost": 9,
     "attackChance": 150,
     "criticalSkill": 10,
     "criticalMultiplier": 3.0,
     "blockChance": 45,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "chaotic_grip",
        "magnitude": 5,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_chb_1a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_chb_1a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_chb_1a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_chb_1a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
