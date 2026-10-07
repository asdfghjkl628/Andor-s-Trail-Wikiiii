---
description: "Snappy cave lizard is an enemy in Andor's Trail (reptile) with 30 HP, worth 117 XP, found in Bloskelt + Roskelt, Instrument maker, Entry."
---

# ![](../assets/icons/monsters/monsters_rltiles2_116.png){ .sprite } Snappy cave lizard

**Found in:** Bloskelt + Roskelt: [ratdom_maze_424](../maps/ratdom_maze_424.md), Bloskelt + Roskelt: [ratdom_maze_435](../maps/ratdom_maze_435.md), Entry: [ratdom_maze_467](../maps/ratdom_maze_467.md), Instrument maker: [ratdom_maze_445](../maps/ratdom_maze_445.md) (+4 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_116.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Bloskelt + Roskelt, Instrument maker, Entry |
| **Class** | Reptile |
| **HP** | 30 |
| **XP when defeated** | 117 |
| **Entry ID** | `ratdom_m7b` |
| **Introduced** | [v0.8.5](../versions/0.8.5.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Reptile |
| HP | 30 |
| XP when defeated | 117 |
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

**On hit:** On target: Weak Poison (magnitude 1, 3 rounds, 10% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [ratdom_maze_424](../maps/ratdom_maze_424.md) | Bloskelt + Roskelt | 2 | – |
| [ratdom_maze_435](../maps/ratdom_maze_435.md) | Bloskelt + Roskelt | 2 | – |
| [ratdom_maze_445](../maps/ratdom_maze_445.md) | Instrument maker | 2 | – |
| [ratdom_maze_455](../maps/ratdom_maze_455.md) | Instrument maker | 2 | – |
| [ratdom_maze_456](../maps/ratdom_maze_456.md) | Instrument maker | 2 | – |
| [ratdom_maze_467](../maps/ratdom_maze_467.md) | Entry | 1 | – |
| [ratdom_maze_558](../maps/ratdom_maze_558.md) | Labyrinth | 2 | – |
| [ratdom_maze_566](../maps/ratdom_maze_566.md) | – | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `ratdom_m7b` |
    | Spawn group | `ratdom_m7` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:116` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_m7b",
     "name": "Snappy cave lizard",
     "iconID": "monsters_rltiles2:116",
     "maxHP": 30,
     "maxAP": 10,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 5,
      "max": 5
     },
     "spawnGroup": "ratdom_m7",
     "attackCost": 5,
     "attackChance": 110,
     "criticalSkill": 40,
     "criticalMultiplier": 2.0,
     "blockChance": 20,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "poison_weak",
        "magnitude": 1,
        "duration": 3,
        "chance": "10"
       }
      ]
     }
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_m7b.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_m7b.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_m7b.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_m7b.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
