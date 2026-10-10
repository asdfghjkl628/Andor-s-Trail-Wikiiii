---
description: "Ancient hirathil ghost is an enemy in Andor's Trail (ghost) with 92 HP, worth 373 XP, found in Lodarcave 4a, Lodarcave 5, Lodarcave 6. Drops: Small empty vial, Glass gem, Runed scepter."
---

# ![](../assets/icons/monsters/monsters_rltiles2_43.png){ .sprite } Ancient hirathil ghost

**Found in:** [Lodarcave 4a](../maps/lodarcave4a.md), [Lodarcave 5](../maps/lodarcave5.md), [Lodarcave 6](../maps/lodarcave6.md), [Lodarcave 7](../maps/lodarcave7.md) (+1 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_43.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Lodarcave 4a, Lodarcave 5, Lodarcave 6 |
| **Class** | Ghost |
| **HP** | 92 |
| **XP when defeated** | 373 |
| **Immune to crits** | Yes |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat

| | |
|---|---|
| Class | Ghost |
| HP | 92 |
| XP when defeated | 373 |
| Damage | 7 to 16 |
| AC | 145 |
| BC | 157 |
| DR | 10 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | 21% (×3.0) |

**Immune to critical hits.**


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Small empty vial](../items/vial_empty1.md) | 5% | 1 |
| [Glass gem](../items/gem1.md) | 5% | 1 |
| [Runed scepter](../items/scptr_runed.md) | 1% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Lodarcave 4a](../maps/lodarcave4a.md) | – | 13 | – |
| [Lodarcave 5](../maps/lodarcave5.md) | – | 1 | – |
| [Lodarcave 6](../maps/lodarcave6.md) | – | 3 | – |
| [Lodarcave 7](../maps/lodarcave7.md) | – | 1 | – |
| [Shortcut lodar 0](../maps/shortcut_lodar0.md) | – | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Renamed “Ancient Hirathil ghost” → “Ancient hirathil ghost” |

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
    | Entry ID | `hirathil7` |
    | Type (wiki) | Enemy |
    | Spawn group | `hirathil2` |
    | Loot table | `hirathil` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_rltiles2:43` |
    | Defined in | `res/raw/monsterlist_v070_lodarcave.json` |

    Raw data:

    ```json
    {
     "id": "hirathil7",
     "name": "Ancient hirathil ghost",
     "iconID": "monsters_rltiles2:43",
     "maxHP": 92,
     "moveCost": 5,
     "monsterClass": "ghost",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 7,
      "max": 16
     },
     "spawnGroup": "hirathil2",
     "droplistID": "hirathil",
     "attackCost": 5,
     "attackChance": 145,
     "criticalSkill": 35,
     "criticalMultiplier": 3.0,
     "blockChance": 157,
     "damageResistance": 10
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hirathil7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hirathil7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hirathil7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hirathil7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
