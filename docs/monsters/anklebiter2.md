---
description: "Small horned anklebiter is an enemy in Andor's Trail (animal) with 38 HP, worth 78 XP, found in Loneford. Drops: Gold coins, Ruby gem, Meat, Animal hair."
---

# ![](../assets/icons/monsters/monsters_tometik4_56.png){ .sprite } Small horned anklebiter

**Found in:** Loneford: [Lodar 0](../maps/lodar0.md), Loneford: [Lodar 2](../maps/lodar2.md), Loneford: [Lodar 5](../maps/lodar5.md), [Lodar 11](../maps/lodar11.md) (+7 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik4_56.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Loneford |
| **Class** | Animal |
| **HP** | 38 |
| **XP when defeated** | 78 |
| **Entry ID** | `anklebiter2` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 38 |
| XP when defeated | 78 |
| Damage | 3 to 7 |
| Attack chance | 96 |
| Block chance | 53 |
| Damage resistance | 1 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 50% | 0 to 5 |
| [Ruby gem](../items/gem2.md) | 5% | 1 |
| [Meat](../items/meat.md) | 10% | 1 |
| [Animal hair](../items/hair.md) | 30% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Lodar 0](../maps/lodar0.md) | Loneford | 3 | – |
| [Lodar 11](../maps/lodar11.md) | – | 2 | – |
| [Lodar 14](../maps/lodar14.md) | – | 1 | – |
| [Lodar 17](../maps/lodar17.md) | – | 2 | – |
| [Lodar 19](../maps/lodar19.md) | – | 2 | – |
| [Lodar 2](../maps/lodar2.md) | Loneford | 4 | – |
| [Lodar 4](../maps/lodar4.md) | – | 2 | – |
| [Lodar 5](../maps/lodar5.md) | Loneford | 2 | – |
| [Lodar 7](../maps/lodar7.md) | – | 3 | – |
| [Lodar 8](../maps/lodar8.md) | – | 1 | – |
| [Lodar 9](../maps/lodar9.md) | – | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `anklebiter2` |
    | Spawn group | `hanklbit1` |
    | Loot table | `anklebiter` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik4:56` |
    | Defined in | `res/raw/monsterlist_v070_lodarmaze.json` |

    Raw data:

    ```json
    {
     "id": "anklebiter2",
     "name": "Small horned anklebiter",
     "iconID": "monsters_tometik4:56",
     "maxHP": 38,
     "moveCost": 5,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 3,
      "max": 7
     },
     "spawnGroup": "hanklbit1",
     "droplistID": "anklebiter",
     "attackCost": 3,
     "attackChance": 96,
     "blockChance": 53,
     "damageResistance": 1
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=anklebiter2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=anklebiter2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=anklebiter2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=anklebiter2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
