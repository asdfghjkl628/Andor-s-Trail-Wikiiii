---
description: "Gravewing is an enemy in Andor's Trail (animal) with 138 HP, worth 561 XP, found in Undertell 03, Undertell 04, Undertell 05."
---

# ![](../assets/icons/monsters/monsters_rltiles2_71.png){ .sprite } Gravewing

**Found in:** [Undertell 03](../maps/undertell_03.md), [Undertell 04](../maps/undertell_04.md), [Undertell 05](../maps/undertell_05.md), [Undertell 13](../maps/undertell_13.md) (+7 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_71.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Undertell 03, Undertell 04, Undertell 05 |
| **Class** | Animal |
| **HP** | 138 |
| **XP when defeated** | 561 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Combat

| | |
|---|---|
| Class | Animal |
| HP | 138 |
| XP when defeated | 561 |
| Damage | 16 to 17 |
| AC | 165 |
| BC | 205 |
| DR | 0 |
| Attacks per turn | 3 (4 AP each, 12 AP) |
| Crit chance | 11% (×2.0) |

**Its hits:** On target: [Rabies](../conditions/rabies.md) (magnitude 1, 3 rounds, 15% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Undertell 03](../maps/undertell_03.md) | – | 1 | – |
| [Undertell 04](../maps/undertell_04.md) | – | 2 | – |
| [Undertell 05](../maps/undertell_05.md) | – | 2 | – |
| [Undertell 13](../maps/undertell_13.md) | – | 3 | – |
| [Undertell 14](../maps/undertell_14.md) | – | 4 | – |
| [Undertell 15](../maps/undertell_15.md) | – | 4 | – |
| [Undertell 22](../maps/undertell_22.md) | – | 2 | – |
| [Undertell 23](../maps/undertell_23.md) | – | 2 | – |
| [Undertell 24](../maps/undertell_24.md) | – | 2 | – |
| [Undertell 3 01](../maps/undertell_3_01.md) | – | 3 | – |
| [Undertell 3 11](../maps/undertell_3_11.md) | – | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

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
    | Entry ID | `undertell_bat` |
    | Type (wiki) | Enemy |
    | Spawn group | `undertell_bat` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_rltiles2:71` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "undertell_bat",
     "name": "Gravewing",
     "iconID": "monsters_rltiles2:71",
     "maxHP": 138,
     "maxAP": 12,
     "moveCost": 4,
     "monsterClass": "animal",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 16,
      "max": 17
     },
     "attackCost": 4,
     "attackChance": 165,
     "criticalSkill": 13,
     "criticalMultiplier": 2.0,
     "blockChance": 205,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "rabies",
        "magnitude": 1,
        "duration": 3,
        "chance": "15"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=undertell_bat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=undertell_bat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=undertell_bat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=undertell_bat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
