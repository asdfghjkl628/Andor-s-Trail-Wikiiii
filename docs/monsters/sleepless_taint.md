---
description: "Sleepless taint is an enemy in Andor's Trail (ghost) with 180 HP, worth 715 XP, found in Haunted underground 1, Haunted underground 2, Haunted underground 3. Drops: Gold coins, Regular potion of health."
---

# ![](../assets/icons/monsters/monsters_rltiles2_140.png){ .sprite } Sleepless taint

**Found in:** [Haunted underground 1](../maps/haunted_underground_1.md), [Haunted underground 2](../maps/haunted_underground_2.md), [Haunted underground 3](../maps/haunted_underground_3.md), [Haunted underground 4](../maps/haunted_underground_4.md) (+1 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_140.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Haunted underground 1, Haunted underground 2, Haunted underground 3 |
| **Class** | Ghost |
| **HP** | 180 |
| **XP when defeated** | 715 |
| **Immune to crits** | Yes |
| **Introduced** | [v0.8.3](../versions/0.8.3.md) |

</div>

## Combat

| | |
|---|---|
| Class | Ghost |
| HP | 180 |
| XP when defeated | 715 |
| Damage | 11 to 12 |
| AC | 185 |
| BC | 265 |
| DR | 9 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 5% (×2.0) |

**Immune to critical hits.**

**Its hits:** On target: [Sleepwalking](../conditions/sleepwalking.md) (magnitude 1, 2 rounds, 40% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 15% | 20 to 22 |
| [Regular potion of health](../items/health.md) | 25% | 2 to 3 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Haunted underground 1](../maps/haunted_underground_1.md) | – | 1 | – |
| [Haunted underground 2](../maps/haunted_underground_2.md) | – | 3 | – |
| [Haunted underground 3](../maps/haunted_underground_3.md) | – | 3 | – |
| [Haunted underground 4](../maps/haunted_underground_4.md) | – | 6 | – |
| [Haunted underground 5](../maps/haunted_underground_5.md) | – | 4 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.3](../versions/0.8.3.md) | Added |
| [v0.8.4](../versions/0.8.4.md) | Class: undead → ghost |

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
    | Entry ID | `sleepless_taint` |
    | Type (wiki) | Enemy |
    | Spawn group | `sleepless_taint` |
    | Loot table | `sleepless_taint_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_rltiles2:140` |
    | Defined in | `res/raw/monsterlist_haunted_forest.json` |

    Raw data:

    ```json
    {
     "id": "sleepless_taint",
     "name": "Sleepless taint",
     "iconID": "monsters_rltiles2:140",
     "maxHP": 180,
     "moveCost": 3,
     "monsterClass": "ghost",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 11,
      "max": 12
     },
     "droplistID": "sleepless_taint_dl",
     "attackCost": 3,
     "attackChance": 185,
     "criticalSkill": 5,
     "criticalMultiplier": 2.0,
     "blockChance": 265,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "sleepwalking",
        "magnitude": 1,
        "duration": 2,
        "chance": "40"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sleepless_taint.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sleepless_taint.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sleepless_taint.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sleepless_taint.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
