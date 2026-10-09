---
description: "Shadow gargoyle master is an enemy in Andor's Trail (undead) with 35 HP, worth 111 XP, found in Gargoylecave 2, Gargoylecave 3, Gargoylecave 4. Drops: Gold coins, Ruby gem, Polished gem, Regular potion of health."
---

# ![](../assets/icons/monsters/monsters_liches_1.png){ .sprite } Shadow gargoyle master

**Found in:** [Gargoylecave 2](../maps/gargoylecave2.md), [Gargoylecave 3](../maps/gargoylecave3.md), [Gargoylecave 4](../maps/gargoylecave4.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_liches_1.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Gargoylecave 2, Gargoylecave 3, Gargoylecave 4 |
| **Class** | Undead |
| **HP** | 35 |
| **XP when defeated** | 111 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat

| | |
|---|---|
| Class | Undead |
| HP | 35 |
| XP when defeated | 111 |
| Damage | 3 to 6 |
| AC | 125 |
| BC | 90 |
| DR | 5 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | 10% (×3.0) |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 16 to 23 |
| [Ruby gem](../items/gem2.md) | 25% | 1 |
| [Polished gem](../items/gem3.md) | 10% | 1 |
| [Regular potion of health](../items/health.md) | 25% | 1 |
| [Small rock](../items/rock.md) | 25% | 1 |
| [Ring of lesser Shadow](../items/ring_shadow0.md) | 0.01% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Gargoylecave 2](../maps/gargoylecave2.md) | – | 1 | – |
| [Gargoylecave 3](../maps/gargoylecave3.md) | – | 3 | – |
| [Gargoylecave 4](../maps/gargoylecave4.md) | – | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Formatting change only (no gameplay effect) |

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
    | Entry ID | `shadow_gargoyle_master` |
    | Type (wiki) | Enemy |
    | Spawn group | `shadowgarg4` |
    | Loot table | `shadowgarg3` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_liches:1` |
    | Defined in | `res/raw/monsterlist_v068_npcs.json` |

    Raw data:

    ```json
    {
     "id": "shadow_gargoyle_master",
     "name": "Shadow gargoyle master",
     "iconID": "monsters_liches:1",
     "maxHP": 35,
     "monsterClass": "undead",
     "attackDamage": {
      "min": 3,
      "max": 6
     },
     "spawnGroup": "shadowgarg4",
     "droplistID": "shadowgarg3",
     "attackCost": 5,
     "attackChance": 125,
     "criticalSkill": 12,
     "criticalMultiplier": 3.0,
     "blockChance": 90,
     "damageResistance": 5
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shadow_gargoyle_master.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shadow_gargoyle_master.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shadow_gargoyle_master.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shadow_gargoyle_master.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
