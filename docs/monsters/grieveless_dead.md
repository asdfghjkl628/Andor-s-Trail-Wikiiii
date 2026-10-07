---
description: "Grieveless dead is an enemy in Andor's Trail (ghost) with 189 HP, worth 587 XP, found in Haunted cemetery 1, Haunted cemetery 2, Haunted forest 17. Drops: Gold coins, Tonic of blood."
---

# ![](../assets/icons/monsters/monsters_tometik8_4.png){ .sprite } Grieveless dead

**Found in:** [Haunted cemetery 1](../maps/haunted_cemetery1.md), [Haunted cemetery 2](../maps/haunted_cemetery2.md), [Haunted forest 17](../maps/haunted_forest17.md), [Haunted forest 20](../maps/haunted_forest20.md) (+9 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik8_4.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Haunted cemetery 1, Haunted cemetery 2, Haunted forest 17 |
| **Class** | Ghost |
| **HP** | 189 |
| **XP when defeated** | 587 |
| **Immune to critical hits** | Yes |
| **Entry ID** | `grieveless_dead` |
| **Introduced** | [v0.8.3](../versions/0.8.3.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Ghost |
| HP | 189 |
| XP when defeated | 587 |
| Damage | 14 to 21 |
| Attack chance | 137 |
| Block chance | 177 |
| Damage resistance | 11 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 3 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.

**When hit:** On self: [Regeneration](../conditions/regen2.md) (magnitude 6, 1 round)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 45% | 10 to 17 |
| [Tonic of blood](../items/tonic_of_blood.md) | 8% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Haunted cemetery 1](../maps/haunted_cemetery1.md) | – | 7 | – |
| [Haunted cemetery 2](../maps/haunted_cemetery2.md) | – | 1 | – |
| [Haunted forest 17](../maps/haunted_forest17.md) | – | 1 | – |
| [Haunted forest 20](../maps/haunted_forest20.md) | – | 1 | – |
| [Haunted forest 21](../maps/haunted_forest21.md) | – | 3 | – |
| [Haunted forest 22](../maps/haunted_forest22.md) | – | 2 | – |
| [Haunted forest 23](../maps/haunted_forest23.md) | – | 1 | – |
| [Haunted forest 24](../maps/haunted_forest24.md) | – | 1 | – |
| [Haunted forest 25](../maps/haunted_forest25.md) | – | 4 | – |
| [Haunted forest 9](../maps/haunted_forest9.md) | – | 4 | – |
| [Haunted forest way to house 2](../maps/haunted_forest_way_to_house2.md) | – | 1 | – |
| [Haunted forest way to house 5](../maps/haunted_forest_way_to_house5.md) | – | 1 | – |
| [Vilegard sullengard filler 1](../maps/vilegard_sullengard_filler1.md) | – | 3 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.3](../versions/0.8.3.md) | Added |
| [v0.8.4](../versions/0.8.4.md) | Class: undead → ghost |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `grieveless_dead` |
    | Spawn group | `grieveless_dead` |
    | Loot table | `grieveless_dead_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_tometik8:4` |
    | Defined in | `res/raw/monsterlist_haunted_forest.json` |

    Raw data:

    ```json
    {
     "id": "grieveless_dead",
     "name": "Grieveless dead",
     "iconID": "monsters_tometik8:4",
     "maxHP": 189,
     "moveCost": 3,
     "monsterClass": "ghost",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 14,
      "max": 21
     },
     "droplistID": "grieveless_dead_dl",
     "attackCost": 3,
     "attackChance": 137,
     "blockChance": 177,
     "damageResistance": 11,
     "hitReceivedEffect": {
      "conditionsSource": [
       {
        "condition": "regen2",
        "magnitude": 6,
        "duration": 1,
        "chance": "100"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=grieveless_dead.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=grieveless_dead.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=grieveless_dead.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=grieveless_dead.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
