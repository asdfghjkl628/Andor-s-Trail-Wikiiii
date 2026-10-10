---
description: "Burrowing glow worm is an enemy in Andor's Trail (reptile) with 48 HP, worth 256 XP, found in Gamjee well 1 1, Gamjee well 1 3, Gamjee well 2 1. Drops: Gold coins, Poison gland, Worm meat."
---

# ![](../assets/icons/monsters/monsters_tometik4_20.png){ .sprite } Burrowing glow worm

**Found in:** [Gamjee well 1 1](../maps/gamjee_well_1_1.md), [Gamjee well 1 3](../maps/gamjee_well_1_3.md), [Gamjee well 2 1](../maps/gamjee_well_2_1.md), [Gamjee well exit](../maps/gamjee_well_exit.md) (+5 more)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_tometik4_20.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Gamjee well 1 1, Gamjee well 1 3, Gamjee well 2 1 |
| **Class** | Reptile |
| **HP** | 48 |
| **XP when defeated** | 256 |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

</div>

## Combat

| | |
|---|---|
| Class | Reptile |
| HP | 48 |
| XP when defeated | 256 |
| Damage | 4 to 7 |
| AC | 101 |
| BC | 109 |
| DR | 7 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 35% (×2.0) |

**Its hits:** On target: [Weak Poison](../conditions/poison_weak.md) (magnitude 2, 3 rounds, 30% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 30% | 1 to 7 |
| [Poison gland](../items/gland.md) | 5% | 1 |
| [Worm meat](../items/meat3.md) | 25% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Gamjee well 1 1](../maps/gamjee_well_1_1.md) | – | 2 | – |
| [Gamjee well 1 3](../maps/gamjee_well_1_3.md) | – | 1 | – |
| [Gamjee well 2 1](../maps/gamjee_well_2_1.md) | – | 2 | – |
| [Gamjee well exit](../maps/gamjee_well_exit.md) | – | 1 | – |
| [Gamjee well jail cells](../maps/gamjee_well_jail_cells.md) | – | 1 | – |
| [Lodar 16](../maps/lodar16.md) | – | 15 | – |
| [Lodar 20](../maps/lodar20.md) | – | 2 | – |
| [Lodar 21](../maps/lodar21.md) | – | 2 | – |
| [Lodar 8](../maps/lodar8.md) | – | 4 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `burrowing_glow_worm` |
    | Type (wiki) | Enemy |
    | Spawn group | `vscale1` |
    | Loot table | `burrowing_glow_worm_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik4:20` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "burrowing_glow_worm",
     "name": "Burrowing glow worm",
     "iconID": "monsters_tometik4:20",
     "maxHP": 48,
     "moveCost": 5,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 4,
      "max": 7
     },
     "spawnGroup": "vscale1",
     "droplistID": "burrowing_glow_worm_dl",
     "attackCost": 3,
     "attackChance": 101,
     "criticalSkill": 80,
     "criticalMultiplier": 2.0,
     "blockChance": 109,
     "damageResistance": 7,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "poison_weak",
        "magnitude": 2,
        "duration": 3,
        "chance": "30"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=burrowing_glow_worm.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=burrowing_glow_worm.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=burrowing_glow_worm.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=burrowing_glow_worm.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
