---
description: "Ancient basilisk is an enemy in Andor's Trail (reptile) with 120 HP, worth 290 XP, found in Basiliskcave 2. Drops: Engraved steel helmet, Gold coins."
---

# ![](../assets/icons/monsters/monsters_giantbasilisk_0.png){ .sprite } Ancient basilisk

**Found in:** [Basiliskcave 2](../maps/basiliskcave2.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_giantbasilisk_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Basiliskcave 2 |
| **Class** | Reptile |
| **HP** | 120 |
| **XP when defeated** | 290 |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

## Combat

| | |
|---|---|
| Class | Reptile |
| HP | 120 |
| XP when defeated | 290 |
| Damage | 5 to 8 |
| AC | 80 |
| BC | 130 |
| DR | 8 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 15% (×2.0) |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Engraved steel helmet](../items/brimhaven_engraved_steel_helmet.md) | 100% | 1 |
| [Gold coins](../items/gold.md) | 100% | 200 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Basiliskcave 2](../maps/basiliskcave2.md) | – | 1 | – |

## Quests that count defeats

- [A quick glance](../quests/quick_glance.md#stage-90) with [Anakis](../monsters/anakis.md) ([Brimhaven 7](../maps/brimhaven7.md)) checks that this enemy has been defeated.
- A conversation with stepping on a trigger on [Basiliskcave 2](../maps/basiliskcave2.md) checks that this enemy has been defeated.
- [A quick glance](../quests/quick_glance.md#stage-80) with stepping on a trigger on [Basiliskcave 2](../maps/basiliskcave2.md) checks that this enemy has been defeated.
- [Quick glance: statue found (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-60) with [Fangwurm](../monsters/fangwurm.md) ([Brimhaven church](../maps/brimhaven_church.md)) checks that this enemy has been defeated.


## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added |

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
    | Entry ID | `old_basilisk` |
    | Type (wiki) | Enemy |
    | Spawn group | `basiliskcave2_boss` |
    | Loot table | `old_basilisk` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_giantbasilisk:0` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "old_basilisk",
     "name": "Ancient basilisk",
     "iconID": "monsters_giantbasilisk:0",
     "maxHP": 120,
     "unique": 1,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 5,
      "max": 8
     },
     "spawnGroup": "basiliskcave2_boss",
     "faction": "",
     "droplistID": "old_basilisk",
     "attackCost": 3,
     "attackChance": 80,
     "criticalSkill": 20,
     "criticalMultiplier": 2.0,
     "blockChance": 130,
     "damageResistance": 8,
     "deathEffect": {}
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=old_basilisk.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=old_basilisk.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=old_basilisk.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=old_basilisk.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
