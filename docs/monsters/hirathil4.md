---
description: "Restless hirathil ghost is an enemy in Andor's Trail (ghost) with 83 HP, worth 345 XP, found in Lodarcave 1, Lodarcave 2, Lodarcave 3. Drops: Small empty vial, Glass gem, Runed scepter."
---

# ![](../assets/icons/monsters/monsters_rltiles2_42.png){ .sprite } Restless hirathil ghost

**Found in:** [Lodarcave 1](../maps/lodarcave1.md), [Lodarcave 2](../maps/lodarcave2.md), [Lodarcave 3](../maps/lodarcave3.md), [Lodarcave 4](../maps/lodarcave4.md) (+4 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_42.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Lodarcave 1, Lodarcave 2, Lodarcave 3 |
| **Class** | Ghost |
| **HP** | 83 |
| **XP when defeated** | 345 |
| **Immune to critical hits** | Yes |
| **Entry ID** | `hirathil4` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Ghost |
| HP | 83 |
| XP when defeated | 345 |
| Damage | 7 to 16 |
| Attack chance | 136 |
| Block chance | 152 |
| Damage resistance | 10 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 35 |
| Critical multiplier | 3.0 |
| Critical hit chance | 21% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Small empty vial](../items/vial_empty1.md) | 5% | 1 |
| [Glass gem](../items/gem1.md) | 5% | 1 |
| [Runed scepter](../items/scptr_runed.md) | 1% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Lodarcave 1](../maps/lodarcave1.md) | – | 1 | – |
| [Lodarcave 2](../maps/lodarcave2.md) | – | 2 | – |
| [Lodarcave 3](../maps/lodarcave3.md) | – | 6 | – |
| [Lodarcave 4](../maps/lodarcave4.md) | – | 14 | – |
| [Lodarcave 5](../maps/lodarcave5.md) | – | 16 | – |
| [Lodarcave 6](../maps/lodarcave6.md) | – | 12 | – |
| [Lodarcave 7](../maps/lodarcave7.md) | – | 6 | – |
| [Shortcut lodar 0](../maps/shortcut_lodar0.md) | – | 4 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Renamed “Restless Hirathil ghost” → “Restless hirathil ghost” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `hirathil4` |
    | Spawn group | `hirathil1` |
    | Loot table | `hirathil` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_rltiles2:42` |
    | Defined in | `res/raw/monsterlist_v070_lodarcave.json` |

    Raw data:

    ```json
    {
     "id": "hirathil4",
     "name": "Restless hirathil ghost",
     "iconID": "monsters_rltiles2:42",
     "maxHP": 83,
     "moveCost": 5,
     "monsterClass": "ghost",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 7,
      "max": 16
     },
     "spawnGroup": "hirathil1",
     "droplistID": "hirathil",
     "attackCost": 5,
     "attackChance": 136,
     "criticalSkill": 35,
     "criticalMultiplier": 3.0,
     "blockChance": 152,
     "damageResistance": 10
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hirathil4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hirathil4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hirathil4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hirathil4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
