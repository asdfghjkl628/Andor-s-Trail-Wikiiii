---
description: "Black cave bat is an enemy in Andor's Trail (animal) with 32 HP, worth 111 XP, found in Lake Laeroth. Drops: Bat wing."
---

# ![](../assets/icons/monsters/monsters_tometik4_0.png){ .sprite } Black cave bat

**Found in:** Lake Laeroth: [laerothbasement0](../maps/laerothbasement0.md), [laerothcave1](../maps/laerothcave1.md), [lodar12cave0](../maps/lodar12cave0.md), [lodar12cave1](../maps/lodar12cave1.md) (+21 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik4_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Lake Laeroth |
| **Class** | Animal |
| **HP** | 32 |
| **XP when defeated** | 111 |
| **Entry ID** | `cavebat2` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 32 |
| XP when defeated | 111 |
| Damage | 2 to 6 |
| Attack chance | 59 |
| Block chance | 35 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 2 AP |
| Attacks per turn | 5 |
| Move cost | 5 AP |
| Critical skill | 75 |
| Critical multiplier | 3.0 |
| Critical hit chance | 33% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Bat wing](../items/bat_wing.md) | 20% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [laerothbasement0](../maps/laerothbasement0.md) | Lake Laeroth | 3 | – |
| [laerothcave1](../maps/laerothcave1.md) | – | 5 | – |
| [lodar12cave0](../maps/lodar12cave0.md) | – | 5 | – |
| [lodar12cave1](../maps/lodar12cave1.md) | – | 5 | – |
| [lodar1cave0](../maps/lodar1cave0.md) | – | 4 | – |
| [lodar5cave0](../maps/lodar5cave0.md) | – | 13 | – |
| [lodar5cave1](../maps/lodar5cave1.md) | – | 7 | – |
| [lodar5cave2](../maps/lodar5cave2.md) | – | 7 | – |
| [lodar8cave0](../maps/lodar8cave0.md) | – | 6 | – |
| [lodarcave0](../maps/lodarcave0.md) | – | 4 | – |
| [lodarcave1](../maps/lodarcave1.md) | – | 3 | – |
| [lodarcave2](../maps/lodarcave2.md) | – | 3 | – |
| [lodarcave3](../maps/lodarcave3.md) | – | 3 | – |
| [lodarcave4](../maps/lodarcave4.md) | – | 3 | – |
| [lodarcave5](../maps/lodarcave5.md) | – | 4 | – |
| [lodarcave6](../maps/lodarcave6.md) | – | 6 | – |
| [lodarcave7](../maps/lodarcave7.md) | – | 3 | – |
| [mushroom_m2_1](../maps/mushroom_m2_1.md) | – | 3 | – |
| [mushroom_m2_2](../maps/mushroom_m2_2.md) | – | 3 | – |
| [mushroom_m3_2](../maps/mushroom_m3_2.md) | – | 2 | – |
| [secretpassage0](../maps/secretpassage0.md) | – | 3 | – |
| [shortcut_lodar1](../maps/shortcut_lodar1.md) | – | 4 | – |
| [shortcut_lodar2](../maps/shortcut_lodar2.md) | – | 4 | – |
| [shortcut_lodar3](../maps/shortcut_lodar3.md) | – | 5 | – |
| [shortcut_lodar4](../maps/shortcut_lodar4.md) | – | 3 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Formatting change only (no gameplay effect) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `cavebat2` |
    | Spawn group | `cavebat1` |
    | Loot table | `cavebat` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_tometik4:0` |
    | Defined in | `res/raw/monsterlist_v070_lodar5cave.json` |

    Raw data:

    ```json
    {
     "id": "cavebat2",
     "name": "Black cave bat",
     "iconID": "monsters_tometik4:0",
     "maxHP": 32,
     "moveCost": 5,
     "monsterClass": "animal",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 2,
      "max": 6
     },
     "spawnGroup": "cavebat1",
     "droplistID": "cavebat",
     "attackCost": 2,
     "attackChance": 59,
     "criticalSkill": 75,
     "criticalMultiplier": 3.0,
     "blockChance": 35
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cavebat2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cavebat2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cavebat2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cavebat2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
