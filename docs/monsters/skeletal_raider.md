---
description: "Skeletal raider is an enemy in Andor's Trail (undead) with 227 HP, worth 506 XP, found in Haunted forest 14, Haunted forest 15, Haunted forest 19. Drops: Skeletal remains, Gold coins."
---

# ![](../assets/icons/monsters/monsters_tometik8_10.png){ .sprite } Skeletal raider

**Found in:** [Haunted forest 14](../maps/haunted_forest14.md), [Haunted forest 15](../maps/haunted_forest15.md), [Haunted forest 19](../maps/haunted_forest19.md), [Haunted forest 21](../maps/haunted_forest21.md) (+5 more)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_tometik8_10.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Haunted forest 14, Haunted forest 15, Haunted forest 19 |
| **Class** | Undead |
| **HP** | 227 |
| **XP when defeated** | 506 |
| **Introduced** | [v0.8.3](../versions/0.8.3.md) |

</div>

## Combat

| | |
|---|---|
| Class | Undead |
| HP | 227 |
| XP when defeated | 506 |
| Damage | 15 to 19 |
| AC | 199 |
| BC | 84 |
| DR | 0 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Skeletal remains](../items/skeletal_remains.md) | 10% | 1 to 2 |
| [Gold coins](../items/gold.md) | 45% | 11 to 19 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Haunted forest 14](../maps/haunted_forest14.md) | – | 4 | – |
| [Haunted forest 15](../maps/haunted_forest15.md) | – | 3 | – |
| [Haunted forest 19](../maps/haunted_forest19.md) | – | 4 | – |
| [Haunted forest 21](../maps/haunted_forest21.md) | – | 3 | – |
| [Haunted forest 22](../maps/haunted_forest22.md) | – | 2 | – |
| [Haunted forest 24](../maps/haunted_forest24.md) | – | 3 | – |
| [Haunted forest 25](../maps/haunted_forest25.md) | – | 2 | – |
| [Haunted forest way to house 4](../maps/haunted_forest_way_to_house4.md) | – | 4 | – |
| [Vilegard sullengard filler 1](../maps/vilegard_sullengard_filler1.md) | – | 3 | – |


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
    | Entry ID | `skeletal_raider` |
    | Type (wiki) | Enemy |
    | Spawn group | `skeletal_raider` |
    | Loot table | `skeletal_raider_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik8:10` |
    | Defined in | `res/raw/monsterlist_haunted_forest.json` |

    Raw data:

    ```json
    {
     "id": "skeletal_raider",
     "name": "Skeletal raider",
     "iconID": "monsters_tometik8:10",
     "maxHP": 227,
     "moveCost": 4,
     "monsterClass": "undead",
     "attackDamage": {
      "min": 15,
      "max": 19
     },
     "droplistID": "skeletal_raider_dl",
     "attackCost": 3,
     "attackChance": 199,
     "blockChance": 84
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=skeletal_raider.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=skeletal_raider.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=skeletal_raider.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=skeletal_raider.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
