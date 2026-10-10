---
description: "Wild boar is an enemy in Andor's Trail (animal) with 20 HP, worth 33 XP, found in Flagstone Prison, Blackwater Mountain, Fallhaven. Drops: Gold coins, Animal hair, Meat, Leather boots."
---

# ![](../assets/icons/monsters/monsters_dogs_6.png){ .sprite } Wild boar

**Found in:** Blackwater Mountain: [Mywild 18](../maps/mywild18.md), Blackwater Mountain: [Wild 6](../maps/wild6.md), Fallhaven: [Roadbeforecrossroads 5](../maps/roadbeforecrossroads5.md), Fallhaven: [Wild 10](../maps/wild10.md) (+7 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_dogs_6.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Flagstone Prison, Blackwater Mountain, Fallhaven |
| **Class** | Animal |
| **HP** | 20 |
| **XP when defeated** | 33 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat

| | |
|---|---|
| Class | Animal |
| HP | 20 |
| XP when defeated | 33 |
| Damage | 3 |
| AC | 110 |
| BC | 30 |
| DR | 0 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

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
| [Blackwater mountain 0](../maps/blackwater_mountain0.md) | Flagstone Prison | 4 | – |
| [Flagstone 0](../maps/flagstone0.md) | Flagstone Prison | 2 | – |
| [Mywild 18](../maps/mywild18.md) | Blackwater Mountain | 2 | – |
| [Roadbeforecrossroads 5](../maps/roadbeforecrossroads5.md) | Fallhaven | 1 | – |
| [Wild 10](../maps/wild10.md) | Fallhaven | 2 | – |
| [Wild 12](../maps/wild12.md) | Fallhaven | 2 | – |
| [Wild 13](../maps/wild13.md) | Fallhaven | 3 | – |
| [Wild 16](../maps/wild16.md) | Flagstone Prison | 2 | – |
| [Wild 18](../maps/wild18.md) | Flagstone Prison | 1 | – |
| [Wild 5](../maps/wild5.md) | Fallhaven | 3 | – |
| [Wild 6](../maps/wild6.md) | Blackwater Mountain | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Renamed “Wild Boar” → “Wild boar” |

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
    | Entry ID | `wild_boar` |
    | Type (wiki) | Enemy |
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
