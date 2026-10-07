---
description: "Wild boar is an enemy in Andor's Trail (animal) with 20 HP, worth 33 XP, found in Flagstone Prison, Blackwater Mountain, Fallhaven. Drops: Gold coins, Animal hair, Meat, Leather boots."
---

# ![](../assets/icons/monsters/monsters_dogs_6.png){ .sprite } Wild boar

**Found in:** Blackwater Mountain: [mywild18](../maps/mywild18.md), Blackwater Mountain: [wild6](../maps/wild6.md), Fallhaven: [roadbeforecrossroads5](../maps/roadbeforecrossroads5.md), Fallhaven: [wild10](../maps/wild10.md) (+7 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_dogs_6.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Flagstone Prison, Blackwater Mountain, Fallhaven |
| **Class** | Animal |
| **HP** | 20 |
| **XP when defeated** | 33 |
| **Entry ID** | `wild_boar` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 20 |
| XP when defeated | 33 |
| Damage | 3 |
| Attack chance | 110 |
| Block chance | 30 |
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
| [Gold coins](../items/gold.md) | 70% | 1 |
| [Animal hair](../items/hair.md) | 30% | 1 |
| [Meat](../items/meat.md) | 30% | 1 |
| [Leather boots](../items/boots1.md) | 5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [blackwater_mountain0](../maps/blackwater_mountain0.md) | Flagstone Prison | 4 | – |
| [flagstone0](../maps/flagstone0.md) | Flagstone Prison | 2 | – |
| [mywild18](../maps/mywild18.md) | Blackwater Mountain | 2 | – |
| [roadbeforecrossroads5](../maps/roadbeforecrossroads5.md) | Fallhaven | 1 | – |
| [wild10](../maps/wild10.md) | Fallhaven | 2 | – |
| [wild12](../maps/wild12.md) | Fallhaven | 2 | – |
| [wild13](../maps/wild13.md) | Fallhaven | 3 | – |
| [wild16](../maps/wild16.md) | Flagstone Prison | 2 | – |
| [wild18](../maps/wild18.md) | Flagstone Prison | 1 | – |
| [wild5](../maps/wild5.md) | Fallhaven | 3 | – |
| [wild6](../maps/wild6.md) | Blackwater Mountain | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Renamed “Wild Boar” → “Wild boar” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `wild_boar` |
    | Spawn group | `forestboar2` |
    | Loot table | `canineboss` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_dogs:6` |
    | Defined in | `res/raw/monsterlist_wilderness.json` |

    Raw data:

    ```json
    {
     "id": "wild_boar",
     "name": "Wild boar",
     "iconID": "monsters_dogs:6",
     "maxHP": 20,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 3,
      "max": 3
     },
     "spawnGroup": "forestboar2",
     "droplistID": "canineboss",
     "attackCost": 5,
     "attackChance": 110,
     "blockChance": 30
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wild_boar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wild_boar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wild_boar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wild_boar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
