---
description: "Anklebiter is an enemy in Andor's Trail (animal) with 31 HP, worth 92 XP, found in Crossroads Guardhouse, Flagstone Prison, Guynmart Castle. Drops: Gold coins, Glass gem, Meat, Animal hair."
---

# ![](../assets/icons/monsters/monsters_dogs_6.png){ .sprite } Anklebiter

**Found in:** Crossroads Guardhouse: [crossroads](../maps/crossroads.md), Fallhaven: [roadbeforecrossroads2](../maps/roadbeforecrossroads2.md), Fallhaven: [roadbeforecrossroads3](../maps/roadbeforecrossroads3.md), Fallhaven: [roadbeforecrossroads4](../maps/roadbeforecrossroads4.md) (+14 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_dogs_6.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Crossroads Guardhouse, Flagstone Prison, Guynmart Castle |
| **Class** | Animal |
| **HP** | 31 |
| **XP when defeated** | 92 |
| **Entry ID** | `anklebiter` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 31 |
| XP when defeated | 92 |
| Damage | 3 to 9 |
| Attack chance | 150 |
| Block chance | 60 |
| Damage resistance | 3 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 3 to 25 |
| [Glass gem](../items/gem1.md) | 5% | 1 |
| [Meat](../items/meat.md) | 30% | 1 |
| [Animal hair](../items/hair.md) | 30% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [cabin_norcity_road1](../maps/cabin_norcity_road1.md) | – | 3 | – |
| [crossroads](../maps/crossroads.md) | Crossroads Guardhouse | 4 | – |
| [flagstone0](../maps/flagstone0.md) | Flagstone Prison | 1 | – |
| [guynmart_wood_11](../maps/guynmart_wood_11.md) | Guynmart Castle | 2 | – |
| [guynmart_wood_12](../maps/guynmart_wood_12.md) | Guynmart Castle | 1 | – |
| [guynmart_wood_13](../maps/guynmart_wood_13.md) | Guynmart Castle | 2 | – |
| [road3](../maps/road3.md) | Foaming Flask Tavern | 1 | – |
| [road4](../maps/road4.md) | Foaming Flask Tavern | 1 | – |
| [road5](../maps/road5.md) | – | 1 | – |
| [roadbeforecrossroads2](../maps/roadbeforecrossroads2.md) | Fallhaven | 2 | – |
| [roadbeforecrossroads3](../maps/roadbeforecrossroads3.md) | Fallhaven | 2 | – |
| [roadbeforecrossroads4](../maps/roadbeforecrossroads4.md) | Fallhaven | 3 | – |
| [roadbeforecrossroads5](../maps/roadbeforecrossroads5.md) | Fallhaven | 3 | – |
| [roadbeforecrossroads6](../maps/roadbeforecrossroads6.md) | Fallhaven | 1 | – |
| [roadbeforecrossroads7](../maps/roadbeforecrossroads7.md) | Fallhaven | 2 | – |
| [wild14_cave](../maps/wild14_cave.md) | Foaming Flask Tavern | 1 | – |
| [wild14_clearing](../maps/wild14_clearing.md) | – | 1 | – |
| [wild16](../maps/wild16.md) | Flagstone Prison | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `anklebiter` |
    | Spawn group | `forestboar3` |
    | Loot table | `canine2` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_dogs:6` |
    | Defined in | `res/raw/monsterlist_wilderness.json` |

    Raw data:

    ```json
    {
     "id": "anklebiter",
     "name": "Anklebiter",
     "iconID": "monsters_dogs:6",
     "maxHP": 31,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 3,
      "max": 9
     },
     "spawnGroup": "forestboar3",
     "droplistID": "canine2",
     "attackCost": 5,
     "attackChance": 150,
     "blockChance": 60,
     "damageResistance": 3
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=anklebiter.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=anklebiter.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=anklebiter.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=anklebiter.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
