---
description: "Iqhan chaos servant is an enemy in Andor's Trail (humanoid) with 78–79 HP, worth 244–254 XP, found in pwcave3, pwcave4. Drops: Gold coins, Iqhan pendant, Wooden buckler, Iron dagger."
---

# ![](../assets/icons/monsters/monsters_rltiles2_134.png){ .sprite } Iqhan chaos servant

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_134.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | pwcave3, pwcave4 |
| **Class** | Humanoid |
| **HP** | 78–79 |
| **XP when defeated** | 244–254 |
| **Entries in game data** | 2 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Iqhan chaos servant. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: combat statistics. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`iqhan_ch_2a`](#v-iqhan_ch_2a) | Enemy | [pwcave3](../maps/pwcave3.md), [pwcave4](../maps/pwcave4.md) | – | 78 |
| [`iqhan_ch_2b`](#v-iqhan_ch_2b) | Enemy | [pwcave3](../maps/pwcave3.md), [pwcave4](../maps/pwcave4.md) | – | 79 |

## Pwcave3 and 1 more (iqhan_ch_2a) { #v-iqhan_ch_2a }

**Entry ID:** `iqhan_ch_2a` · **Type:** Enemy

**Location:** [pwcave3](../maps/pwcave3.md), [pwcave4](../maps/pwcave4.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 78 |
| XP when defeated | 244 |
| Damage | 2 to 14 |
| Attack chance | 150 |
| Block chance | 60 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 20 |
| Critical multiplier | 2.0 |
| Critical hit chance | 15% |

**On hit:** On target: [Chaotic grip](../conditions/chaotic_grip.md) (magnitude 4, 5 rounds, 50% chance)


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
| [pwcave3](../maps/pwcave3.md) | – | 5 | – |
| [pwcave4](../maps/pwcave4.md) | – | 2 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Chaotic grip](../conditions/chaotic_grip.md) (magnitude 4, 5 rounds, 50% chance) → (magnitude 4, 5 rounds, 50% chance) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (iqhan_ch_2a)"

    | | |
    |---|---|
    | Entry ID | `iqhan_ch_2a` |
    | Spawn group | `iqhan_ch_2` |
    | Loot table | `iqhan` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:134` |
    | Defined in | `res/raw/monsterlist_v0610_monsters2.json` |

    Raw data:

    ```json
    {
     "id": "iqhan_ch_2a",
     "name": "Iqhan chaos servant",
     "iconID": "monsters_rltiles2:134",
     "maxHP": 78,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 2,
      "max": 14
     },
     "spawnGroup": "iqhan_ch_2",
     "droplistID": "iqhan",
     "attackCost": 3,
     "attackChance": 150,
     "criticalSkill": 20,
     "criticalMultiplier": 2.0,
     "blockChance": 60,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "chaotic_grip",
        "magnitude": 4,
        "duration": 5,
        "chance": "50"
       }
      ]
     }
    }
    ```


## Pwcave3 and 1 more (iqhan_ch_2b) { #v-iqhan_ch_2b }

**Entry ID:** `iqhan_ch_2b` · **Type:** Enemy

**Location:** [pwcave3](../maps/pwcave3.md), [pwcave4](../maps/pwcave4.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 79 |
| XP when defeated | 254 |
| Damage | 2 to 13 |
| Attack chance | 150 |
| Block chance | 75 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 25 |
| Critical multiplier | 2.0 |
| Critical hit chance | 17% |

**On hit:** On target: [Chaotic grip](../conditions/chaotic_grip.md) (magnitude 4, 5 rounds, 50% chance)


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
| [pwcave3](../maps/pwcave3.md) | – | 5 | – |
| [pwcave4](../maps/pwcave4.md) | – | 2 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Chaotic grip](../conditions/chaotic_grip.md) (magnitude 4, 5 rounds, 50% chance) → (magnitude 4, 5 rounds, 50% chance) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (iqhan_ch_2b)"

    | | |
    |---|---|
    | Entry ID | `iqhan_ch_2b` |
    | Spawn group | `iqhan_ch_2` |
    | Loot table | `iqhan` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:134` |
    | Defined in | `res/raw/monsterlist_v0610_monsters2.json` |

    Raw data:

    ```json
    {
     "id": "iqhan_ch_2b",
     "name": "Iqhan chaos servant",
     "iconID": "monsters_rltiles2:134",
     "maxHP": 79,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 2,
      "max": 13
     },
     "spawnGroup": "iqhan_ch_2",
     "droplistID": "iqhan",
     "attackCost": 3,
     "attackChance": 150,
     "criticalSkill": 25,
     "criticalMultiplier": 2.0,
     "blockChance": 75,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "chaotic_grip",
        "magnitude": 4,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_ch_2a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_ch_2a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_ch_2a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_ch_2a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
