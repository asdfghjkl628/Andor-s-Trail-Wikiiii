---
description: "Forest hunter is an enemy in Andor's Trail (insect) with 90 HP, worth 356 XP, found in Haunted forest 1, Haunted forest 13, Haunted forest 14. Drops: Spider eggs, Dead spider."
---

# ![](../assets/icons/monsters/monsters_tometik10_50.png){ .sprite } Forest hunter

**Found in:** [Haunted forest 1](../maps/haunted_forest1.md), [Haunted forest 13](../maps/haunted_forest13.md), [Haunted forest 14](../maps/haunted_forest14.md), [Haunted forest 15](../maps/haunted_forest15.md) (+13 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik10_50.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Haunted forest 1, Haunted forest 13, Haunted forest 14 |
| **Class** | Insect |
| **HP** | 90 |
| **XP when defeated** | 356 |
| **Introduced** | [v0.8.3](../versions/0.8.3.md) |

</div>

## Combat

| | |
|---|---|
| Class | Insect |
| HP | 90 |
| XP when defeated | 356 |
| Damage | 12 to 21 |
| AC | 150 |
| BC | 160 |
| DR | 6 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | none |

**Its hits:** On target: [Insect contagion](../conditions/contagion.md) (magnitude 4, 5 rounds, 50% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Spider eggs](../items/spider_eggs.md) | 25% | 1 to 2 |
| [Dead spider](../items/spider.md) | 25% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Haunted forest 1](../maps/haunted_forest1.md) | – | 4 | – |
| [Haunted forest 13](../maps/haunted_forest13.md) | – | 1 | – |
| [Haunted forest 14](../maps/haunted_forest14.md) | – | 3 | – |
| [Haunted forest 15](../maps/haunted_forest15.md) | – | 2 | – |
| [Haunted forest 16](../maps/haunted_forest16.md) | – | 1 | – |
| [Haunted forest 19](../maps/haunted_forest19.md) | – | 1 | – |
| [Haunted forest 2](../maps/haunted_forest2.md) | – | 3 | – |
| [Haunted forest 25](../maps/haunted_forest25.md) | – | 2 | – |
| [Haunted forest 3](../maps/haunted_forest3.md) | – | 2 | – |
| [Haunted forest 4](../maps/haunted_forest4.md) | – | 2 | – |
| [Haunted forest 5](../maps/haunted_forest5.md) | – | 2 | – |
| [Haunted forest 6](../maps/haunted_forest6.md) | – | 2 | – |
| [Haunted forest 8](../maps/haunted_forest8.md) | – | 1 | – |
| [Haunted forest 9](../maps/haunted_forest9.md) | – | 1 | – |
| [Haunted forest filler](../maps/haunted_forest_filler.md) | – | 2 | – |
| [Haunted forest way to house 4](../maps/haunted_forest_way_to_house4.md) | – | 1 | – |
| [Vilegard sullengard filler 1](../maps/vilegard_sullengard_filler1.md) | – | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.3](../versions/0.8.3.md) | Added |

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
    | Entry ID | `forest_hunter` |
    | Type (wiki) | Enemy |
    | Spawn group | `forest_hunter` |
    | Loot table | `forest_hunter_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_tometik10:50` |
    | Defined in | `res/raw/monsterlist_haunted_forest.json` |

    Raw data:

    ```json
    {
     "id": "forest_hunter",
     "name": "Forest hunter",
     "iconID": "monsters_tometik10:50",
     "maxHP": 90,
     "moveCost": 4,
     "monsterClass": "insect",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 12,
      "max": 21
     },
     "droplistID": "forest_hunter_dl",
     "attackCost": 4,
     "attackChance": 150,
     "blockChance": 160,
     "damageResistance": 6,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "contagion",
        "magnitude": 4,
        "duration": 5,
        "chance": "50"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forest_hunter.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forest_hunter.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forest_hunter.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forest_hunter.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
