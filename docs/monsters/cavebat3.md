---
description: "Brown cave bat is an enemy in Andor's Trail (animal) with 36 HP, worth 121 XP, found in Lake Laeroth. Drops: Bat wing."
---

# ![](../assets/icons/monsters/monsters_tometik4_2.png){ .sprite } Brown cave bat

**Found in:** Lake Laeroth: [Laerothbasement 0](../maps/laerothbasement0.md), [Laerothcave 1](../maps/laerothcave1.md), [Lodar 12cave 0](../maps/lodar12cave0.md), [Lodar 12cave 1](../maps/lodar12cave1.md) (+21 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik4_2.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Lake Laeroth |
| **Class** | Animal |
| **HP** | 36 |
| **XP when defeated** | 121 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat

| | |
|---|---|
| Class | Animal |
| HP | 36 |
| XP when defeated | 121 |
| Damage | 1 to 7 |
| AC | 62 |
| BC | 25 |
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
| [Laerothbasement 0](../maps/laerothbasement0.md) | Lake Laeroth | 3 | – |
| [Laerothcave 1](../maps/laerothcave1.md) | – | 5 | – |
| [Lodar 12cave 0](../maps/lodar12cave0.md) | – | 5 | – |
| [Lodar 12cave 1](../maps/lodar12cave1.md) | – | 5 | – |
| [Lodar 1cave 0](../maps/lodar1cave0.md) | – | 4 | – |
| [Lodar 5cave 0](../maps/lodar5cave0.md) | – | 13 | – |
| [Lodar 5cave 1](../maps/lodar5cave1.md) | – | 7 | – |
| [Lodar 5cave 2](../maps/lodar5cave2.md) | – | 7 | – |
| [Lodar 8cave 0](../maps/lodar8cave0.md) | – | 6 | – |
| [Lodarcave 0](../maps/lodarcave0.md) | – | 4 | – |
| [Lodarcave 1](../maps/lodarcave1.md) | – | 3 | – |
| [Lodarcave 2](../maps/lodarcave2.md) | – | 3 | – |
| [Lodarcave 3](../maps/lodarcave3.md) | – | 3 | – |
| [Lodarcave 4](../maps/lodarcave4.md) | – | 3 | – |
| [Lodarcave 5](../maps/lodarcave5.md) | – | 4 | – |
| [Lodarcave 6](../maps/lodarcave6.md) | – | 6 | – |
| [Lodarcave 7](../maps/lodarcave7.md) | – | 3 | – |
| [Mushroom m 2 1](../maps/mushroom_m2_1.md) | – | 3 | – |
| [Mushroom m 2 2](../maps/mushroom_m2_2.md) | – | 3 | – |
| [Mushroom m 3 2](../maps/mushroom_m3_2.md) | – | 2 | – |
| [Secretpassage 0](../maps/secretpassage0.md) | – | 3 | – |
| [Shortcut lodar 1](../maps/shortcut_lodar1.md) | – | 4 | – |
| [Shortcut lodar 2](../maps/shortcut_lodar2.md) | – | 4 | – |
| [Shortcut lodar 3](../maps/shortcut_lodar3.md) | – | 5 | – |
| [Shortcut lodar 4](../maps/shortcut_lodar4.md) | – | 3 | – |


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
    | Entry ID | `cavebat3` |
    | Type (wiki) | Enemy |
    | Spawn group | `cavebat1` |
    | Loot table | `cavebat` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_tometik4:2` |
    | Defined in | `res/raw/monsterlist_v070_lodar5cave.json` |

    Raw data:

    ```json
    {
     "id": "cavebat3",
     "name": "Brown cave bat",
     "iconID": "monsters_tometik4:2",
     "maxHP": 36,
     "moveCost": 5,
     "monsterClass": "animal",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 1,
      "max": 7
     },
     "spawnGroup": "cavebat1",
     "droplistID": "cavebat",
     "attackCost": 2,
     "attackChance": 62,
     "criticalSkill": 80,
     "criticalMultiplier": 3.0,
     "blockChance": 25
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cavebat3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cavebat3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cavebat3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cavebat3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
