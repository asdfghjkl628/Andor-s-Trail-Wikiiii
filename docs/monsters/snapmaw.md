---
description: "Snapmaw is an enemy in Andor's Trail (reptile) with 114 HP, worth 516 XP, found in Mt. Galmore."
---

# ![](../assets/icons/monsters/monsters_newb_1_213.png){ .sprite } Snapmaw

**Found in:** Mt. Galmore: [Galmore 25](../maps/galmore_25.md), [Galmore 14](../maps/galmore_14.md), [Galmore 15](../maps/galmore_15.md), [Galmore 16](../maps/galmore_16.md) (+3 more)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_newb_1_213.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Mt. Galmore |
| **Class** | Reptile |
| **HP** | 114 |
| **XP when defeated** | 516 |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Combat

| | |
|---|---|
| Class | Reptile |
| HP | 114 |
| XP when defeated | 516 |
| Damage | 13 to 25 |
| AC | 140 |
| BC | 250 |
| DR | 25 |
| Attacks per turn | 1 (7 AP each, 13 AP) |
| Crit chance | 15% (×2.0) |

**Its hits:** Restore AP: 0 to 1

**When you hit it:** On self: [Bark skin](../conditions/barkskin.md) (magnitude 1, 3 rounds, 15% chance); On target: [Bleeding wound](../conditions/bleeding_wound.md) (magnitude 4, 4 rounds, 15% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Galmore 14](../maps/galmore_14.md) | – | 6 | – |
| [Galmore 15](../maps/galmore_15.md) | – | 10 | – |
| [Galmore 16](../maps/galmore_16.md) | – | 5 | – |
| [Galmore 25](../maps/galmore_25.md) | Mt. Galmore | 14 | – |
| [Galmore 26](../maps/galmore_26.md) | – | 13 | – |
| [Galmore 27](../maps/galmore_27.md) | – | 3 | – |
| [Galmore 37](../maps/galmore_37.md) | – | 8 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

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
    | Entry ID | `snapmaw` |
    | Type (wiki) | Enemy |
    | Spawn group | `snapmaw` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_newb_1:213` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "snapmaw",
     "name": "Snapmaw",
     "iconID": "monsters_newb_1:213",
     "maxHP": 114,
     "maxAP": 13,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 13,
      "max": 25
     },
     "attackCost": 7,
     "attackChance": 140,
     "criticalSkill": 20,
     "criticalMultiplier": 2.0,
     "blockChance": 250,
     "damageResistance": 25,
     "hitEffect": {
      "increaseCurrentAP": {
       "min": 0,
       "max": 1
      }
     },
     "hitReceivedEffect": {
      "conditionsSource": [
       {
        "condition": "barkskin",
        "magnitude": 1,
        "duration": 3,
        "chance": "15"
       }
      ],
      "conditionsTarget": [
       {
        "condition": "bleeding_wound",
        "magnitude": 4,
        "duration": 4,
        "chance": "15"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=snapmaw.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=snapmaw.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=snapmaw.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=snapmaw.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
