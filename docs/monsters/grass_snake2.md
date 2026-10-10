---
description: "Tough grasslands snake is an enemy in Andor's Trail (reptile) with 38 HP, worth 80 XP, found in Loneford, Crossroads Guardhouse, Guynmart Castle. Drops: Gold coins, Poison gland, Mundane ring."
---

# ![](../assets/icons/monsters/monsters_rltiles2_25.png){ .sprite } Tough grasslands snake

**Found in:** Crossroads Guardhouse: [Loneford 1](../maps/loneford1.md), Guynmart Castle: [Swamp 1](../maps/swamp1.md), Guynmart Castle: [Swamp 3](../maps/swamp3.md), Loneford: [Fields 4](../maps/fields4.md) (+4 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_25.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Loneford, Crossroads Guardhouse, Guynmart Castle |
| **Class** | Reptile |
| **HP** | 38 |
| **XP when defeated** | 80 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat

| | |
|---|---|
| Class | Reptile |
| HP | 38 |
| XP when defeated | 80 |
| Damage | 1 to 7 |
| AC | 125 |
| BC | 80 |
| DR | 0 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 3 to 15 |
| [Poison gland](../items/gland.md) | 30% | 1 |
| [Mundane ring](../items/ring1.md) | 5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Fields 3](../maps/fields3.md) | – | 2 | – |
| [Fields 4](../maps/fields4.md) | Loneford | 2 | – |
| [Loneford 1](../maps/loneford1.md) | Crossroads Guardhouse | 1 | – |
| [Swamp 1](../maps/swamp1.md) | Guynmart Castle | 2 | – |
| [Swamp 3](../maps/swamp3.md) | Guynmart Castle | 2 | – |
| [Swamp 4](../maps/swamp4.md) | – | 2 | – |
| [Swamp 5](../maps/swamp5.md) | – | 2 | – |
| [Swamp 6](../maps/swamp6.md) | – | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

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
    | Entry ID | `grass_snake2` |
    | Type (wiki) | Enemy |
    | Spawn group | `fieldcritter_2` |
    | Loot table | `fieldcritter_2` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:25` |
    | Defined in | `res/raw/monsterlist_v0610_monsters1.json` |

    Raw data:

    ```json
    {
     "id": "grass_snake2",
     "name": "Tough grasslands snake",
     "iconID": "monsters_rltiles2:25",
     "maxHP": 38,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 1,
      "max": 7
     },
     "spawnGroup": "fieldcritter_2",
     "droplistID": "fieldcritter_2",
     "attackCost": 3,
     "attackChance": 125,
     "blockChance": 80
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=grass_snake2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=grass_snake2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=grass_snake2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=grass_snake2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
