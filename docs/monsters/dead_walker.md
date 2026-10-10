---
description: "Deadwalker is an enemy in Andor's Trail (undead) with 203 HP, worth 428 XP, found in Haunted forest 1, Haunted forest 14, Haunted forest 19. Drops: Human skull, Gold coins, Skeletal remains."
---

# ![](../assets/icons/monsters/monsters_ld2_228.png){ .sprite } Deadwalker

**Found in:** [Haunted forest 1](../maps/haunted_forest1.md), [Haunted forest 14](../maps/haunted_forest14.md), [Haunted forest 19](../maps/haunted_forest19.md), [Haunted forest 2](../maps/haunted_forest2.md) (+13 more)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld2_228.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Haunted forest 1, Haunted forest 14, Haunted forest 19 |
| **Class** | Undead |
| **HP** | 203 |
| **XP when defeated** | 428 |
| **Introduced** | [v0.8.3](../versions/0.8.3.md) |

</div>

## Combat

| | |
|---|---|
| Class | Undead |
| HP | 203 |
| XP when defeated | 428 |
| Damage | 15 to 17 |
| AC | 199 |
| BC | 97 |
| DR | 0 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | 5% (×2.0) |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Human skull](../items/human_skull.md) | 1% | 1 |
| [Gold coins](../items/gold.md) | 50% | 8 to 20 |
| [Skeletal remains](../items/skeletal_remains.md) | 35% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Haunted forest 1](../maps/haunted_forest1.md) | – | 3 | – |
| [Haunted forest 14](../maps/haunted_forest14.md) | – | 5 | – |
| [Haunted forest 19](../maps/haunted_forest19.md) | – | 1 | – |
| [Haunted forest 2](../maps/haunted_forest2.md) | – | 1 | – |
| [Haunted forest 23](../maps/haunted_forest23.md) | – | 1 | – |
| [Haunted forest 25](../maps/haunted_forest25.md) | – | 1 | – |
| [Haunted forest 3](../maps/haunted_forest3.md) | – | 2 | – |
| [Haunted forest 4](../maps/haunted_forest4.md) | – | 1 | – |
| [Haunted forest 5](../maps/haunted_forest5.md) | – | 1 | – |
| [Haunted forest 6](../maps/haunted_forest6.md) | – | 6 | – |
| [Haunted forest 7](../maps/haunted_forest7.md) | – | 4 | – |
| [Haunted forest 9](../maps/haunted_forest9.md) | – | 1 | – |
| [Haunted forest coffin 1](../maps/haunted_forest_coffin1.md) | – | 1 | – |
| [Haunted forest coffin 2](../maps/haunted_forest_coffin2.md) | – | 4 | – |
| [Haunted forest filler](../maps/haunted_forest_filler.md) | – | 1 | – |
| [Haunted forest way to house 2](../maps/haunted_forest_way_to_house2.md) | – | 2 | – |
| [Vilegard sullengard filler 1](../maps/vilegard_sullengard_filler1.md) | – | 1 | – |


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
    | Entry ID | `dead_walker` |
    | Type (wiki) | Enemy |
    | Spawn group | `dead_walker` |
    | Loot table | `deadwalker_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:228` |
    | Defined in | `res/raw/monsterlist_haunted_forest.json` |

    Raw data:

    ```json
    {
     "id": "dead_walker",
     "name": "Deadwalker",
     "iconID": "monsters_ld2:228",
     "maxHP": 203,
     "moveCost": 5,
     "monsterClass": "undead",
     "attackDamage": {
      "min": 15,
      "max": 17
     },
     "droplistID": "deadwalker_dl",
     "attackCost": 4,
     "attackChance": 199,
     "criticalSkill": 5,
     "criticalMultiplier": 2.0,
     "blockChance": 97
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dead_walker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dead_walker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dead_walker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dead_walker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
