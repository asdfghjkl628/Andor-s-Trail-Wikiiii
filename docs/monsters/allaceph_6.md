---
description: "Ancient allaceph is an enemy in Andor's Trail (demon) with 133–333 HP, worth 315–616 XP, found in waytobrimhavencave3, waytobrimhavencave3a, waytobrimhavencave3b, waytobrimhavencave3. Drops: Gold coins, Sharpened gem, Regular potion of health, Empty vial."
---

# ![](../assets/icons/monsters/monsters_rltiles2_103.png){ .sprite } Ancient allaceph

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_103.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | waytobrimhavencave3, waytobrimhavencave3a, waytobrimhavencave3b, waytobrimhavencave3 |
| **Class** | Demon |
| **HP** | 133–333 |
| **XP when defeated** | 315–616 |
| **Immune to critical hits** | Yes |
| **Entries in game data** | 2 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Ancient allaceph. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: location, combat statistics, loot or shop stock. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`allaceph_6`](#v-allaceph_6) | Enemy | [waytobrimhavencave3](../maps/waytobrimhavencave3.md), [waytobrimhavencave3a](../maps/waytobrimhavencave3a.md) (+1 more) | – | 133 |
| [`allaceph_cr`](#v-allaceph_cr) | Enemy | [waytobrimhavencave3](../maps/waytobrimhavencave3.md) | – | 333 |

## Waytobrimhavencave3 and 2 more (allaceph_6) { #v-allaceph_6 }

**Entry ID:** `allaceph_6` · **Type:** Enemy

**Location:** [waytobrimhavencave3](../maps/waytobrimhavencave3.md), [waytobrimhavencave3a](../maps/waytobrimhavencave3a.md), [waytobrimhavencave3b](../maps/waytobrimhavencave3b.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Demon |
| HP | 133 |
| XP when defeated | 315 |
| Damage | 3 to 7 |
| Attack chance | 80 |
| Block chance | 115 |
| Damage resistance | 3 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 40 |
| Critical multiplier | 2.0 |
| Critical hit chance | 23% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.

**On hit:** Heal HP: 7; On target: [Minor weapon feebleness](../conditions/feebleness_minor.md) (magnitude 3, 3 rounds, 20% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 30% | 1 to 20 |
| [Sharpened gem](../items/gem4.md) | 30% | 1 |
| [Regular potion of health](../items/health.md) | 30% | 1 to 2 |
| [Empty vial](../items/vial_empty2.md) | 5% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [waytobrimhavencave3](../maps/waytobrimhavencave3.md) | – | 6 | – |
| [waytobrimhavencave3a](../maps/waytobrimhavencave3a.md) | – | 5 | – |
| [waytobrimhavencave3b](../maps/waytobrimhavencave3b.md) | – | 2 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Minor weapon feebleness](../conditions/feebleness_minor.md) (magnitude 3, 3 rounds, 20% chance) → (magnitude 3, 3 rounds, 20% chance)<br>Renamed “Ancient Allaceph” → “Ancient allaceph” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (allaceph_6)"

    | | |
    |---|---|
    | Entry ID | `allaceph_6` |
    | Spawn group | `allaceph_3` |
    | Loot table | `allaceph_b` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:103` |
    | Defined in | `res/raw/monsterlist_v0611_monsters1.json` |

    Raw data:

    ```json
    {
     "id": "allaceph_6",
     "name": "Ancient allaceph",
     "iconID": "monsters_rltiles2:103",
     "maxHP": 133,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "demon",
     "attackDamage": {
      "min": 3,
      "max": 7
     },
     "spawnGroup": "allaceph_3",
     "droplistID": "allaceph_b",
     "attackCost": 3,
     "attackChance": 80,
     "criticalSkill": 40,
     "criticalMultiplier": 2.0,
     "blockChance": 115,
     "damageResistance": 3,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 7,
       "max": 7
      },
      "conditionsTarget": [
       {
        "condition": "feebleness_minor",
        "magnitude": 3,
        "duration": 3,
        "chance": "20"
       }
      ]
     }
    }
    ```


## Waytobrimhavencave3 (allaceph_cr) { #v-allaceph_cr }

**Entry ID:** `allaceph_cr` · **Type:** Enemy

**Location:** [waytobrimhavencave3](../maps/waytobrimhavencave3.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Demon |
| HP | 333 |
| XP when defeated | 616 |
| Damage | 3 to 7 |
| Attack chance | 80 |
| Block chance | 115 |
| Damage resistance | 3 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 40 |
| Critical multiplier | 2.0 |
| Critical hit chance | 23% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.

**On hit:** Heal HP: 7; On target: [Minor weapon feebleness](../conditions/feebleness_minor.md) (magnitude 3, 3 rounds, 20% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Oegyth crystal](../items/oegyth.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [waytobrimhavencave3](../maps/waytobrimhavencave3.md) | – | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Minor weapon feebleness](../conditions/feebleness_minor.md) (magnitude 3, 3 rounds, 20% chance) → (magnitude 3, 3 rounds, 20% chance)<br>Renamed “Ancient Allaceph” → “Ancient allaceph” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (allaceph_cr)"

    | | |
    |---|---|
    | Entry ID | `allaceph_cr` |
    | Spawn group | `allaceph_cr` |
    | Loot table | `oegyth1` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:103` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "allaceph_cr",
     "name": "Ancient allaceph",
     "iconID": "monsters_rltiles2:103",
     "maxHP": 333,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "demon",
     "attackDamage": {
      "min": 3,
      "max": 7
     },
     "spawnGroup": "allaceph_cr",
     "droplistID": "oegyth1",
     "attackCost": 3,
     "attackChance": 80,
     "criticalSkill": 40,
     "criticalMultiplier": 2.0,
     "blockChance": 115,
     "damageResistance": 3,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 7,
       "max": 7
      },
      "conditionsTarget": [
       {
        "condition": "feebleness_minor",
        "magnitude": 3,
        "duration": 3,
        "chance": "20"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=allaceph_6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=allaceph_6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=allaceph_6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=allaceph_6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
