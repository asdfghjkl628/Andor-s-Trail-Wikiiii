---
description: "Dangerous elvedridge is an enemy in Andor's Trail (animal) with 30 HP, worth 67 XP, found in Pub, Skeleton dance, Bloskelt + Roskelt. Drops: Gold coins, Meat, Poison gland."
---

# ![](../assets/icons/monsters/monsters_rltiles2_76.png){ .sprite } Dangerous elvedridge

**Found in:** Bloskelt + Roskelt: [Ratdom maze 534](../maps/ratdom_maze_534.md), Pub: [Ratdom maze 523](../maps/ratdom_maze_523.md), Skeleton dance: [Ratdom maze 533](../maps/ratdom_maze_533.md), Skeleton dance: [Ratdom maze 542](../maps/ratdom_maze_542.md) (+3 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_76.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Pub, Skeleton dance, Bloskelt + Roskelt |
| **Class** | Animal |
| **HP** | 30 |
| **XP when defeated** | 67 |
| **Entry ID** | `ratdom_m8b` |
| **Introduced** | [v0.8.5](../versions/0.8.5.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 30 |
| XP when defeated | 67 |
| Damage | 5 |
| Attack chance | 110 |
| Block chance | 20 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 40 |
| Critical multiplier | 2.0 |
| Critical hit chance | 23% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 3 to 6 |
| [Meat](../items/meat.md) | 30% | 1 |
| [Poison gland](../items/gland.md) | 5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Ratdom maze 523](../maps/ratdom_maze_523.md) | Pub | 2 | – |
| [Ratdom maze 532](../maps/ratdom_maze_532.md) | – | 2 | – |
| [Ratdom maze 533](../maps/ratdom_maze_533.md) | Skeleton dance | 2 | – |
| [Ratdom maze 534](../maps/ratdom_maze_534.md) | Bloskelt + Roskelt | 2 | – |
| [Ratdom maze 541](../maps/ratdom_maze_541.md) | – | 2 | – |
| [Ratdom maze 542](../maps/ratdom_maze_542.md) | Skeleton dance | 1 | – |
| [Ratdom maze 543](../maps/ratdom_maze_543.md) | Skeleton dance | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `ratdom_m8b` |
    | Spawn group | `ratdom_m8` |
    | Loot table | `snake` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:76` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_m8b",
     "name": "Dangerous elvedridge",
     "iconID": "monsters_rltiles2:76",
     "maxHP": 30,
     "maxAP": 10,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 5,
      "max": 5
     },
     "spawnGroup": "ratdom_m8",
     "droplistID": "snake",
     "attackCost": 5,
     "attackChance": 110,
     "criticalSkill": 40,
     "criticalMultiplier": 2.0,
     "blockChance": 20
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_m8b.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_m8b.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_m8b.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_m8b.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
