---
description: "Young roundling is an enemy in Andor's Trail (animal) with 30 HP, worth 67 XP, found in Pub, Museum, Roundlings."
---

# ![](../assets/icons/monsters/monsters_eye1_0.png){ .sprite } Young roundling

**Found in:** Museum: [Ratdom maze 625](../maps/ratdom_maze_625.md), Pub: [Ratdom maze 616](../maps/ratdom_maze_616.md), Roundlings: [Ratdom maze 627](../maps/ratdom_maze_627.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_eye1_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Pub, Museum, Roundlings |
| **Class** | Animal |
| **HP** | 30 |
| **XP when defeated** | 67 |
| **Introduced** | [v0.8.5](../versions/0.8.5.md) |

</div>

## Combat

| | |
|---|---|
| Class | Animal |
| HP | 30 |
| XP when defeated | 67 |
| Damage | 5 |
| AC | 110 |
| BC | 20 |
| DR | 0 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | 23% (×2.0) |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Ratdom maze 616](../maps/ratdom_maze_616.md) | Pub | 2 | – |
| [Ratdom maze 625](../maps/ratdom_maze_625.md) | Museum | 2 | – |
| [Ratdom maze 627](../maps/ratdom_maze_627.md) | Roundlings | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

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
    | Entry ID | `ratdom_m13a` |
    | Type (wiki) | Enemy |
    | Spawn group | `ratdom_m13` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_eye1:0` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_m13a",
     "name": "Young roundling",
     "iconID": "monsters_eye1:0",
     "maxHP": 30,
     "maxAP": 10,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 5,
      "max": 5
     },
     "spawnGroup": "ratdom_m13",
     "attackCost": 5,
     "attackChance": 110,
     "criticalSkill": 40,
     "criticalMultiplier": 2.0,
     "blockChance": 20
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_m13a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_m13a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_m13a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_m13a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
