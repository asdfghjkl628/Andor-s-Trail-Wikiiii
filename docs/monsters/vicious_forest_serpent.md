---
description: "Vicious forest serpent is an enemy in Andor's Trail (reptile) with 27 HP, worth 82 XP, found in Guynmart Castle, Foaming Flask Tavern, Fallhaven. Drops: Gold coins, Meat, Poison gland."
---

# ![](../assets/icons/monsters/monsters_snakes_4.png){ .sprite } Vicious forest serpent

**Found in:** Fallhaven: [Roadbeforecrossroads 4](../maps/roadbeforecrossroads4.md), Fallhaven: [Roadbeforecrossroads 5](../maps/roadbeforecrossroads5.md), Fallhaven: [Roadbeforecrossroads 6](../maps/roadbeforecrossroads6.md), Flagstone Prison: [Wild 8](../maps/wild8.md) (+15 more)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_snakes_4.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Guynmart Castle, Foaming Flask Tavern, Fallhaven |
| **Class** | Reptile |
| **HP** | 27 |
| **XP when defeated** | 82 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat

| | |
|---|---|
| Class | Reptile |
| HP | 27 |
| XP when defeated | 82 |
| Damage | 3 to 4 |
| AC | 150 |
| BC | 50 |
| DR | 0 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 19% (×2.0) |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 7 to 12 |
| [Meat](../items/meat.md) | 30% | 1 |
| [Poison gland](../items/gland.md) | 5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Guynmart wood 11](../maps/guynmart_wood_11.md) | Guynmart Castle | 4 | – |
| [Guynmart wood 12](../maps/guynmart_wood_12.md) | Guynmart Castle | 3 | – |
| [Guynmart wood 13](../maps/guynmart_wood_13.md) | Guynmart Castle | 2 | – |
| [Guynmart wood 15](../maps/guynmart_wood_15.md) | – | 4 | – |
| [Guynmart wood 16](../maps/guynmart_wood_16.md) | – | 3 | – |
| [Guynmart wood 17](../maps/guynmart_wood_17.md) | – | 4 | – |
| [Guynmart wood 17b](../maps/guynmart_wood_17b.md) | – | 5 | – |
| [Guynmart wood 8](../maps/guynmart_wood_8.md) | Guynmart Castle | 5 | – |
| [Road 1](../maps/road1.md) | Foaming Flask Tavern | 1 | – |
| [Road 2](../maps/road2.md) | Foaming Flask Tavern | 1 | – |
| [Road 3](../maps/road3.md) | Foaming Flask Tavern | 1 | – |
| [Road 4](../maps/road4.md) | Foaming Flask Tavern | 1 | – |
| [Roadbeforecrossroads 4](../maps/roadbeforecrossroads4.md) | Fallhaven | 4 | – |
| [Roadbeforecrossroads 5](../maps/roadbeforecrossroads5.md) | Fallhaven | 3 | – |
| [Roadbeforecrossroads 6](../maps/roadbeforecrossroads6.md) | Fallhaven | 2 | – |
| [Roadbeforecrossroads 8](../maps/roadbeforecrossroads8.md) | Foaming Flask Tavern | 4 | – |
| [Roadbeforecrossroads 9](../maps/roadbeforecrossroads9.md) | Foaming Flask Tavern | 2 | – |
| [Wild 14](../maps/wild14.md) | Foaming Flask Tavern | 2 | – |
| [Wild 8](../maps/wild8.md) | Flagstone Prison | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Formatting change only (no gameplay effect) |

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
    | Entry ID | `vicious_forest_serpent` |
    | Type (wiki) | Enemy |
    | Spawn group | `forestserpent2` |
    | Loot table | `snake2` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_snakes:4` |
    | Defined in | `res/raw/monsterlist_wilderness.json` |

    Raw data:

    ```json
    {
     "id": "vicious_forest_serpent",
     "name": "Vicious forest serpent",
     "iconID": "monsters_snakes:4",
     "maxHP": 27,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 3,
      "max": 4
     },
     "spawnGroup": "forestserpent2",
     "droplistID": "snake2",
     "attackCost": 3,
     "attackChance": 150,
     "criticalSkill": 30,
     "criticalMultiplier": 2.0,
     "blockChance": 50
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vicious_forest_serpent.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vicious_forest_serpent.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vicious_forest_serpent.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vicious_forest_serpent.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
