---
description: "Wild fox is an enemy in Andor's Trail (animal) with 25 HP, worth 44 XP, found in Crossroads Guardhouse, Fallhaven, Blackwater Mountain. Drops: Gold coins, Glass gem, Meat."
---

# ![](../assets/icons/monsters/monsters_dogs_3.png){ .sprite } Wild fox

**Found in:** Blackwater Mountain: [wild6](../maps/wild6.md), Crossroads Guardhouse: [roadbeforecrossroads](../maps/roadbeforecrossroads.md), Crossroads Guardhouse: [roadbeforecrossroads1](../maps/roadbeforecrossroads1.md), Fallhaven: [roadbeforecrossroads2](../maps/roadbeforecrossroads2.md) (+3 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_dogs_3.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Crossroads Guardhouse, Fallhaven, Blackwater Mountain |
| **Class** | Animal |
| **HP** | 25 |
| **XP when defeated** | 44 |
| **Entry ID** | `wild_fox` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 25 |
| XP when defeated | 44 |
| Damage | 4 to 5 |
| Attack chance | 100 |
| Block chance | 40 |
| Damage resistance | 0 |
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
| [Gold coins](../items/gold.md) | 70% | 3 to 6 |
| [Glass gem](../items/gem1.md) | 5% | 1 |
| [Meat](../items/meat.md) | 30% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [roadbeforecrossroads](../maps/roadbeforecrossroads.md) | Crossroads Guardhouse | 1 | – |
| [roadbeforecrossroads1](../maps/roadbeforecrossroads1.md) | Crossroads Guardhouse | 1 | – |
| [roadbeforecrossroads2](../maps/roadbeforecrossroads2.md) | Fallhaven | 8 | – |
| [roadbeforecrossroads3](../maps/roadbeforecrossroads3.md) | Fallhaven | 2 | – |
| [roadbeforecrossroads6](../maps/roadbeforecrossroads6.md) | Fallhaven | 1 | – |
| [wild5](../maps/wild5.md) | Fallhaven | 2 | – |
| [wild6](../maps/wild6.md) | Blackwater Mountain | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | name: Wild Fox → Wild fox |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `wild_fox` |
    | Spawn group | `fox2` |
    | Loot table | `canine` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_dogs:3` |
    | Defined in | `res/raw/monsterlist_wilderness.json` |

    Raw data:

    ```json
    {
     "id": "wild_fox",
     "name": "Wild fox",
     "iconID": "monsters_dogs:3",
     "maxHP": 25,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 4,
      "max": 5
     },
     "spawnGroup": "fox2",
     "droplistID": "canine",
     "attackCost": 5,
     "attackChance": 100,
     "blockChance": 40
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wild_fox.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wild_fox.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wild_fox.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wild_fox.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
