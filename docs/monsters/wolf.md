---
description: "Wolf is an enemy in Andor's Trail (animal) with 30 HP, worth 49 XP, found in Flagstone Prison, Blackwater Mountain, Guynmart Castle. Drops: Gold coins, Glass gem, Meat."
---

# ![](../assets/icons/monsters/monsters_dogs_4.png){ .sprite } Wolf

**Found in:** Blackwater Mountain: [Bwmfill 1](../maps/bwmfill1.md), Blackwater Mountain: [Mywild 18](../maps/mywild18.md), Blackwater Mountain: [Wild 6](../maps/wild6.md), Blackwater Mountain: [Wild 7](../maps/wild7.md) (+24 more)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_dogs_4.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Flagstone Prison, Blackwater Mountain, Guynmart Castle |
| **Class** | Animal |
| **HP** | 30 |
| **XP when defeated** | 49 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat

| | |
|---|---|
| Class | Animal |
| HP | 30 |
| XP when defeated | 49 |
| Damage | 3 to 6 |
| AC | 110 |
| BC | 30 |
| DR | 0 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 3 to 6 |
| [Glass gem](../items/gem1.md) | 5% | 1 |
| [Meat](../items/meat.md) | 30% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Blackwater mountain 0](../maps/blackwater_mountain0.md) | Flagstone Prison | 6 | – |
| [Bwmfill 1](../maps/bwmfill1.md) | Blackwater Mountain | 2 | – |
| [Flagstone 0](../maps/flagstone0.md) | Flagstone Prison | 2 | – |
| [Flagstone filler east 1](../maps/flagstone_filler_east_1.md) | Flagstone Prison | 4 | – |
| [Flagstone filler east 2](../maps/flagstone_filler_east_2.md) | Flagstone Prison | 1 | – |
| [Guynmart wood 1](../maps/guynmart_wood_1.md) | Guynmart Castle | 2 | – |
| [Guynmart wood 12](../maps/guynmart_wood_12.md) | Guynmart Castle | 2 | – |
| [Guynmart wood 13](../maps/guynmart_wood_13.md) | Guynmart Castle | 2 | – |
| [Guynmart wood 18](../maps/guynmart_wood_18.md) | – | 2 | – |
| [Guynmart wood 2](../maps/guynmart_wood_2.md) | Guynmart Castle | 2 | – |
| [Guynmart wood 3](../maps/guynmart_wood_3.md) | Guynmart Castle | 3 | – |
| [Guynmart wood 4](../maps/guynmart_wood_4.md) | Guynmart Castle | 1 | – |
| [Lake shore road 0](../maps/lake_shore_road_0.md) | Flagstone Prison | 3 | – |
| [Lake shore road 1](../maps/lake_shore_road_1.md) | Flagstone Prison | 6 | – |
| [Mywild 18](../maps/mywild18.md) | Blackwater Mountain | 6 | – |
| [Mywild 19](../maps/mywild19.md) | Fallhaven | 3 | – |
| [Mywild 20](../maps/mywild20.md) | Fallhaven | 1 | – |
| [Mywildcave](../maps/mywildcave.md) | – | 6 | – |
| [Road 2](../maps/road2.md) | Foaming Flask Tavern | 1 | – |
| [Roadbeforecrossroads](../maps/roadbeforecrossroads.md) | Crossroads Guardhouse | 3 | – |
| [Roadbeforecrossroads 2](../maps/roadbeforecrossroads2.md) | Fallhaven | 6 | – |
| [Wild 11](../maps/wild11.md) | Fallhaven | 2 | – |
| [Wild 14](../maps/wild14.md) | Foaming Flask Tavern | 1 | – |
| [Wild 17](../maps/wild17.md) | Stoutford | 2 | – |
| [Wild 19](../maps/wild19.md) | Stoutford | 4 | – |
| [Wild 6](../maps/wild6.md) | Blackwater Mountain | 3 | – |
| [Wild 7](../maps/wild7.md) | Blackwater Mountain | 2 | – |
| [Wild 9](../maps/wild9.md) | Fallhaven | 5 | – |


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
    | Entry ID | `wolf` |
    | Type (wiki) | Enemy |
    | Spawn group | `forestwolf1` |
    | Loot table | `canine` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_dogs:4` |
    | Defined in | `res/raw/monsterlist_wilderness.json` |

    Raw data:

    ```json
    {
     "id": "wolf",
     "name": "Wolf",
     "iconID": "monsters_dogs:4",
     "maxHP": 30,
     "maxAP": 10,
     "moveCost": 3,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 3,
      "max": 6
     },
     "spawnGroup": "forestwolf1",
     "droplistID": "canine",
     "attackCost": 5,
     "attackChance": 110,
     "blockChance": 30
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wolf.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wolf.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wolf.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wolf.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
