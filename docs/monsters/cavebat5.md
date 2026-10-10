---
description: "Aggressive cave bat is an enemy in Andor's Trail (animal) with 41 HP, worth 137 XP, found in Lake Laeroth. Drops: Bat wing."
---

# ![](../assets/icons/monsters/monsters_tometik4_4.png){ .sprite } Aggressive cave bat

**Found in:** Lake Laeroth: [Laerothbasement 1](../maps/laerothbasement1.md), [Korhald cave bear](../maps/korhald_cave_bear.md), [Laerothcave 2](../maps/laerothcave2.md), [Lodar 5cave 1](../maps/lodar5cave1.md) (+7 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik4_4.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Lake Laeroth |
| **Class** | Animal |
| **HP** | 41 |
| **XP when defeated** | 137 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat

| | |
|---|---|
| Class | Animal |
| HP | 41 |
| XP when defeated | 137 |
| Damage | 1 to 7 |
| AC | 69 |
| BC | 32 |
| DR | 0 |
| Attacks per turn | 5 (2 AP each, 10 AP) |
| Crit chance | 35% (×3.0) |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Bat wing](../items/bat_wing.md) | 20% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Korhald cave bear](../maps/korhald_cave_bear.md) | – | 1 | – |
| [Laerothbasement 1](../maps/laerothbasement1.md) | Lake Laeroth | 4 | – |
| [Laerothcave 2](../maps/laerothcave2.md) | – | 5 | – |
| [Lodar 5cave 1](../maps/lodar5cave1.md) | – | 1 | – |
| [Lodar 5cave 2](../maps/lodar5cave2.md) | – | 4 | – |
| [Lodarcave 4a](../maps/lodarcave4a.md) | – | 4 | – |
| [Secretpassage 1](../maps/secretpassage1.md) | – | 6 | – |
| [Shortcut lodar 0](../maps/shortcut_lodar0.md) | – | 4 | – |
| [Shortcut lodar 1](../maps/shortcut_lodar1.md) | – | 5 | – |
| [Shortcut lodar 2](../maps/shortcut_lodar2.md) | – | 2 | – |
| [Shortcut lodar 3](../maps/shortcut_lodar3.md) | – | 3 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Formatting change only (no gameplay effect) |

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
    | Entry ID | `cavebat5` |
    | Type (wiki) | Enemy |
    | Spawn group | `cavebat2` |
    | Loot table | `cavebat` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_tometik4:4` |
    | Defined in | `res/raw/monsterlist_v070_lodar5cave.json` |

    Raw data:

    ```json
    {
     "id": "cavebat5",
     "name": "Aggressive cave bat",
     "iconID": "monsters_tometik4:4",
     "maxHP": 41,
     "moveCost": 5,
     "monsterClass": "animal",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 1,
      "max": 7
     },
     "spawnGroup": "cavebat2",
     "droplistID": "cavebat",
     "attackCost": 2,
     "attackChance": 69,
     "criticalSkill": 80,
     "criticalMultiplier": 3.0,
     "blockChance": 32
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cavebat5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cavebat5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cavebat5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cavebat5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
