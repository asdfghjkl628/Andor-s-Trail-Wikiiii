---
description: "Ferocious hirathil ghost is an enemy in Andor's Trail (ghost) with 79 HP, worth 335 XP, found in Lodarcave 1, Lodarcave 2, Lodarcave 3. Drops: Small empty vial, Glass gem, Runed scepter."
---

# ![](../assets/icons/monsters/monsters_rltiles2_41.png){ .sprite } Ferocious hirathil ghost

**Found in:** [Lodarcave 1](../maps/lodarcave1.md), [Lodarcave 2](../maps/lodarcave2.md), [Lodarcave 3](../maps/lodarcave3.md), [Lodarcave 4](../maps/lodarcave4.md) (+4 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_41.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Lodarcave 1, Lodarcave 2, Lodarcave 3 |
| **Class** | Ghost |
| **HP** | 79 |
| **XP when defeated** | 335 |
| **Immune to crits** | Yes |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat

| | |
|---|---|
| Class | Ghost |
| HP | 79 |
| XP when defeated | 335 |
| Damage | 6 to 7 |
| AC | 205 |
| BC | 80 |
| DR | 14 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 17% (×3.0) |

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
| [v0.7.2](../versions/0.7.2.md) | Renamed “Ferocious Hirathil ghost” → “Ferocious hirathil ghost” |

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
    | Entry ID | `hirathil3` |
    | Type (wiki) | Enemy |
    | Spawn group | `hirathil1` |
    | Loot table | `hirathil` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_rltiles2:41` |
    | Defined in | `res/raw/monsterlist_v070_lodarcave.json` |

    Raw data:

    ```json
    {
     "id": "hirathil3",
     "name": "Ferocious hirathil ghost",
     "iconID": "monsters_rltiles2:41",
     "maxHP": 79,
     "moveCost": 5,
     "monsterClass": "ghost",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 6,
      "max": 7
     },
     "spawnGroup": "hirathil1",
     "droplistID": "hirathil",
     "attackCost": 3,
     "attackChance": 205,
     "criticalSkill": 25,
     "criticalMultiplier": 3.0,
     "blockChance": 80,
     "damageResistance": 14
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hirathil3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hirathil3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hirathil3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hirathil3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
