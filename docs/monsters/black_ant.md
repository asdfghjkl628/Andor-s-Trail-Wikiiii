---
description: "Black ant is an enemy in Andor's Trail (insect) with 3 HP, worth 5 XP, found in Crossglen, Guynmart Castle. Drops: Gold coins, Insect shell."
---

# ![](../assets/icons/monsters/monsters_insects_0.png){ .sprite } Black ant

**Found in:** Crossglen: [Crossglen](../maps/crossglen.md), Guynmart Castle: [Guynmart wood 3 hole](../maps/guynmart_wood_3_hole.md), [Guynmart wood 19](../maps/guynmart_wood_19.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_insects_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Crossglen, Guynmart Castle |
| **Class** | Insect |
| **HP** | 3 |
| **XP when defeated** | 5 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat

| | |
|---|---|
| Class | Insect |
| HP | 3 |
| XP when defeated | 5 |
| Damage | 1 to 2 |
| AC | 70 |
| BC | 0 |
| DR | 0 |
| Attacks per turn | 1 (9 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 2 to 4 |
| [Insect shell](../items/shell.md) | 30% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Crossglen](../maps/crossglen.md) | Crossglen | 3 | – |
| [Guynmart wood 19](../maps/guynmart_wood_19.md) | – | 4 | – |
| [Guynmart wood 3 hole](../maps/guynmart_wood_3_hole.md) | Guynmart Castle | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.4](../versions/0.7.4.md) | Attack cost: 10 → 9 |
| [v0.8.15](../versions/0.8.15.md) | Chance of appearing mirrored: added (25) |

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
    | Entry ID | `black_ant` |
    | Type (wiki) | Enemy |
    | Spawn group | `crossglen_ant` |
    | Loot table | `insect` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_insects:0` |
    | Defined in | `res/raw/monsterlist_crossglen_animals.json` |

    Raw data:

    ```json
    {
     "id": "black_ant",
     "name": "Black ant",
     "iconID": "monsters_insects:0",
     "maxHP": 3,
     "monsterClass": "insect",
     "attackDamage": {
      "min": 1,
      "max": 2
     },
     "spawnGroup": "crossglen_ant",
     "droplistID": "insect",
     "attackCost": 9,
     "attackChance": 70,
     "horizontalFlipChance": 25
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=black_ant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=black_ant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=black_ant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=black_ant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
