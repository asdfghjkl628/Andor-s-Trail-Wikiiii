---
description: "Erumen lizard is an enemy in Andor's Trail (reptile) with 45 HP, worth 126 XP, found in Brimhaven, Brightport, Loneford. Drops: Gold coins, Glass gem."
---

# ![](../assets/icons/monsters/monsters_rltiles2_114.png){ .sprite } Erumen lizard

**Found in:** Brightport: [Waterway forest 2](../maps/waterway_forest2.md), Brightport: [Waytobrightport 21](../maps/waytobrightport21.md), Brightport: [Waytobrightport 22](../maps/waytobrightport22.md), Brightport: [Waytobrightport 23](../maps/waytobrightport23.md) (+12 more)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_rltiles2_114.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Brimhaven, Brightport, Loneford |
| **Class** | Reptile |
| **HP** | 45 |
| **XP when defeated** | 126 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat

| | |
|---|---|
| Class | Reptile |
| HP | 45 |
| XP when defeated | 126 |
| Damage | 2 to 9 |
| AC | 125 |
| BC | 80 |
| DR | 4 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 0 to 3 |
| [Glass gem](../items/gem1.md) | 10% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Basiliskcave 1 1 4](../maps/basiliskcave1_1_4.md) | – | 4 | – |
| [Basiliskcave 1 1 5](../maps/basiliskcave1_1_5.md) | – | 1 | – |
| [Waterway 11](../maps/waterway11.md) | – | 3 | – |
| [Waterway 12](../maps/waterway12.md) | Brimhaven | 2 | – |
| [Waterway 13](../maps/waterway13.md) | – | 6 | – |
| [Waterway 8](../maps/waterway8.md) | – | 4 | – |
| [Waterway 9](../maps/waterway9.md) | – | 2 | – |
| [Waterway forest 1](../maps/waterway_forest1.md) | – | 4 | – |
| [Waterway forest 2](../maps/waterway_forest2.md) | Brightport | 4 | – |
| [Waytobrightport 21](../maps/waytobrightport21.md) | Brightport | 1 | – |
| [Waytobrightport 22](../maps/waytobrightport22.md) | Brightport | 1 | – |
| [Waytobrightport 23](../maps/waytobrightport23.md) | Brightport | 1 | – |
| [Waytobrimhaven 2](../maps/waytobrimhaven2.md) | Loneford | 7 | – |
| [Waytobrimhaven 3](../maps/waytobrimhaven3.md) | Brimhaven | 6 | – |
| [Waytobrimhavencave 0](../maps/waytobrimhavencave0.md) | – | 2 | – |
| [Waytobrimhavencave 4](../maps/waytobrimhavencave4.md) | – | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Renamed “Erumem Lizard” → “Erumen lizard” |

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
    | Entry ID | `erumen_3` |
    | Type (wiki) | Enemy |
    | Spawn group | `erumen_2` |
    | Loot table | `erumen` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:114` |
    | Defined in | `res/raw/monsterlist_v0611_monsters1.json` |

    Raw data:

    ```json
    {
     "id": "erumen_3",
     "name": "Erumen lizard",
     "iconID": "monsters_rltiles2:114",
     "maxHP": 45,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 2,
      "max": 9
     },
     "spawnGroup": "erumen_2",
     "droplistID": "erumen",
     "attackCost": 3,
     "attackChance": 125,
     "blockChance": 80,
     "damageResistance": 4
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erumen_3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erumen_3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erumen_3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erumen_3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
