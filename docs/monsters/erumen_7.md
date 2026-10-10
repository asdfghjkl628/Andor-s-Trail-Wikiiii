---
description: "Hardened erumen lizard is an enemy in Andor's Trail (reptile) with 93 HP, worth 243 XP, found in Waterway 11, Waterway 11 east, Waterway 9. Drops: Gold coins, Ruby gem."
---

# ![](../assets/icons/monsters/monsters_rltiles2_117.png){ .sprite } Hardened erumen lizard

**Found in:** [Waterway 11](../maps/waterway11.md), [Waterway 11 east](../maps/waterway11_east.md), [Waterway 9](../maps/waterway9.md), [Waterway forest 1](../maps/waterway_forest1.md) (+1 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_117.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Waterway 11, Waterway 11 east, Waterway 9 |
| **Class** | Reptile |
| **HP** | 93 |
| **XP when defeated** | 243 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat

| | |
|---|---|
| Class | Reptile |
| HP | 93 |
| XP when defeated | 243 |
| Damage | 2 to 9 |
| AC | 125 |
| BC | 90 |
| DR | 12 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 0 to 9 |
| [Ruby gem](../items/gem2.md) | 30% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Waterway 11](../maps/waterway11.md) | – | 2 | – |
| [Waterway 11 east](../maps/waterway11_east.md) | – | 2 | – |
| [Waterway 9](../maps/waterway9.md) | – | 3 | – |
| [Waterway forest 1](../maps/waterway_forest1.md) | – | 2 | – |
| [Waytolake 7](../maps/waytolake7.md) | – | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Renamed “Hardened Erumen Lizard” → “Hardened erumen lizard” |

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
    | Entry ID | `erumen_7` |
    | Type (wiki) | Enemy |
    | Spawn group | `erumen_4` |
    | Loot table | `erumen_b` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:117` |
    | Defined in | `res/raw/monsterlist_v0611_monsters1.json` |

    Raw data:

    ```json
    {
     "id": "erumen_7",
     "name": "Hardened erumen lizard",
     "iconID": "monsters_rltiles2:117",
     "maxHP": 93,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 2,
      "max": 9
     },
     "spawnGroup": "erumen_4",
     "droplistID": "erumen_b",
     "attackCost": 3,
     "attackChance": 125,
     "blockChance": 90,
     "damageResistance": 12
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erumen_7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erumen_7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erumen_7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erumen_7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
