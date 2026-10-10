---
description: "Ghostly visage is an enemy in Andor's Trail (ghost) with 16 HP, worth 29 XP, found in Fallhaven. Drops: Gold coins, Ruby gem, Regular potion of health, Empty vial."
---

# ![](../assets/icons/monsters/monsters_ghost1_0.png){ .sprite } Ghostly visage

**Found in:** Fallhaven: [Catacombs 2](../maps/catacombs2.md), Fallhaven: [Catacombs 3](../maps/catacombs3.md), [Hauntedhouse 3](../maps/hauntedhouse3.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ghost1_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Fallhaven |
| **Class** | Ghost |
| **HP** | 16 |
| **XP when defeated** | 29 |
| **Immune to crits** | Yes |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat

| | |
|---|---|
| Class | Ghost |
| HP | 16 |
| XP when defeated | 29 |
| Damage | 1 to 4 |
| AC | 20 |
| BC | 20 |
| DR | 2 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |

**Immune to critical hits.**


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 4 to 12 |
| [Ruby gem](../items/gem2.md) | 25% | 1 |
| [Regular potion of health](../items/health.md) | 25% | 1 |
| [Empty vial](../items/vial_empty2.md) | 25% | 1 |
| [Leather gloves](../items/gloves1.md) | 5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Catacombs 2](../maps/catacombs2.md) | Fallhaven | 5 | – |
| [Catacombs 3](../maps/catacombs3.md) | Fallhaven | 4 | – |
| [Hauntedhouse 3](../maps/hauntedhouse3.md) | – | 2 | – |


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
    | Entry ID | `ghostly_visage` |
    | Type (wiki) | Enemy |
    | Spawn group | `catacombguard2` |
    | Loot table | `catacombguard` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ghost1:0` |
    | Defined in | `res/raw/monsterlist_fallhaven_animals.json` |

    Raw data:

    ```json
    {
     "id": "ghostly_visage",
     "name": "Ghostly visage",
     "iconID": "monsters_ghost1:0",
     "maxHP": 16,
     "maxAP": 10,
     "moveCost": 10,
     "monsterClass": "ghost",
     "attackDamage": {
      "min": 1,
      "max": 4
     },
     "spawnGroup": "catacombguard2",
     "droplistID": "catacombguard",
     "attackCost": 5,
     "attackChance": 20,
     "blockChance": 20,
     "damageResistance": 2
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ghostly_visage.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ghostly_visage.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ghostly_visage.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ghostly_visage.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
