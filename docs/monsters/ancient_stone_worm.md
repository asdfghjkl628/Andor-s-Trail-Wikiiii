---
description: "Ancient stone worm is an enemy in Andor's Trail (reptile) with 42 HP, worth 163 XP, found in Mywildcave, Mywildcave 2, Mywildcave 3. Drops: Gold coins, Meat, Lithic scales."
---

# ![](../assets/icons/monsters/monsters_rltiles2_149.png){ .sprite } Ancient stone worm

**Found in:** [Mywildcave](../maps/mywildcave.md), [Mywildcave 2](../maps/mywildcave2.md), [Mywildcave 3](../maps/mywildcave3.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_149.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Mywildcave, Mywildcave 2, Mywildcave 3 |
| **Class** | Reptile |
| **HP** | 42 |
| **XP when defeated** | 163 |
| **Introduced** | [v0.7.13](../versions/0.7.13.md) |

</div>

## Combat

| | |
|---|---|
| Class | Reptile |
| HP | 42 |
| XP when defeated | 163 |
| Damage | 3 to 4 |
| AC | 103 |
| BC | 120 |
| DR | 4 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | none |

**Its hits:** On target: [Dazed](../conditions/dazed.md) (magnitude 1, 8 rounds, 15% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 50% | 1 to 5 |
| [Meat](../items/meat.md) | 20% | 1 |
| [Lithic scales](../items/lithic_scale.md) | 5% | 1 to 2 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Mywildcave](../maps/mywildcave.md) | – | 3 | – |
| [Mywildcave 2](../maps/mywildcave2.md) | – | 1 | – |
| [Mywildcave 3](../maps/mywildcave3.md) | – | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added |

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
    | Entry ID | `ancient_stone_worm` |
    | Type (wiki) | Enemy |
    | Spawn group | `stoneworm3` |
    | Loot table | `stoneworm3` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:149` |
    | Defined in | `res/raw/monsterlist_gison.json` |

    Raw data:

    ```json
    {
     "id": "ancient_stone_worm",
     "name": "Ancient stone worm",
     "iconID": "monsters_rltiles2:149",
     "maxHP": 42,
     "moveCost": 5,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 3,
      "max": 4
     },
     "spawnGroup": "stoneworm3",
     "droplistID": "stoneworm3",
     "attackCost": 3,
     "attackChance": 103,
     "blockChance": 120,
     "damageResistance": 4,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "dazed",
        "magnitude": 1,
        "duration": 8,
        "chance": "15"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ancient_stone_worm.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ancient_stone_worm.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ancient_stone_worm.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ancient_stone_worm.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
