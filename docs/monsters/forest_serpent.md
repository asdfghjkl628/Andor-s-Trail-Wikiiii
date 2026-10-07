---
description: "Forest serpent is an enemy in Andor's Trail (reptile) with 20 HP, worth 61 XP, found in Flagstone Prison, Fallhaven, Crossroads Guardhouse. Drops: Gold coins, Meat, Poison gland."
---

# ![](../assets/icons/monsters/monsters_snakes_4.png){ .sprite } Forest serpent

**Found in:** Blackwater Mountain: [wild7](../maps/wild7.md), Crossroads Guardhouse: [roadbeforecrossroads](../maps/roadbeforecrossroads.md), Crossroads Guardhouse: [roadbeforecrossroads1](../maps/roadbeforecrossroads1.md), Fallhaven: [mywild19](../maps/mywild19.md) (+9 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_snakes_4.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Flagstone Prison, Fallhaven, Crossroads Guardhouse |
| **Class** | Reptile |
| **HP** | 20 |
| **XP when defeated** | 61 |
| **Entry ID** | `forest_serpent` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Reptile |
| HP | 20 |
| XP when defeated | 61 |
| Damage | 2 to 3 |
| Attack chance | 150 |
| Block chance | 60 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 30 |
| Critical multiplier | 2.0 |
| Critical hit chance | 19% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 7 to 12 |
| [Meat](../items/meat.md) | 30% | 1 |
| [Poison gland](../items/gland.md) | 5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [flagstone0](../maps/flagstone0.md) | Flagstone Prison | 1 | – |
| [flagstone_filler_east_2](../maps/flagstone_filler_east_2.md) | Flagstone Prison | 2 | – |
| [lake_shore_road_0](../maps/lake_shore_road_0.md) | Flagstone Prison | 5 | – |
| [lake_shore_road_1](../maps/lake_shore_road_1.md) | Flagstone Prison | 3 | – |
| [mywild19](../maps/mywild19.md) | Fallhaven | 5 | – |
| [mywild20](../maps/mywild20.md) | Fallhaven | 2 | – |
| [roadbeforecrossroads](../maps/roadbeforecrossroads.md) | Crossroads Guardhouse | 2 | – |
| [roadbeforecrossroads1](../maps/roadbeforecrossroads1.md) | Crossroads Guardhouse | 2 | – |
| [roadbeforecrossroads2](../maps/roadbeforecrossroads2.md) | Fallhaven | 1 | – |
| [wild10](../maps/wild10.md) | Fallhaven | 1 | – |
| [wild12](../maps/wild12.md) | Fallhaven | 2 | – |
| [wild13](../maps/wild13.md) | Fallhaven | 1 | – |
| [wild7](../maps/wild7.md) | Blackwater Mountain | 3 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | minor data change |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `forest_serpent` |
    | Spawn group | `forestserpent1` |
    | Loot table | `snake2` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_snakes:4` |
    | Defined in | `res/raw/monsterlist_wilderness.json` |

    Raw data:

    ```json
    {
     "id": "forest_serpent",
     "name": "Forest serpent",
     "iconID": "monsters_snakes:4",
     "maxHP": 20,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 2,
      "max": 3
     },
     "spawnGroup": "forestserpent1",
     "droplistID": "snake2",
     "attackCost": 3,
     "attackChance": 150,
     "criticalSkill": 30,
     "criticalMultiplier": 2.0,
     "blockChance": 60
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forest_serpent.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forest_serpent.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forest_serpent.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forest_serpent.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
