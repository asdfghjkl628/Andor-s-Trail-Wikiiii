---
description: "Ridgehowler is an enemy in Andor's Trail (animal) with 180 HP, worth 538 XP, found in Mt. Galmore. Drops: Meat, Gold coins, Bone."
---

# ![](../assets/icons/monsters/monsters_newb_1_305.png){ .sprite } Ridgehowler

**Found in:** Mt. Galmore: [Galmore 24](../maps/galmore_24.md), Mt. Galmore: [Galmore 25](../maps/galmore_25.md), Mt. Galmore: [Galmore 34](../maps/galmore_34.md), Mt. Galmore: [Galmore 35](../maps/galmore_35.md) (+4 more)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_newb_1_305.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Mt. Galmore |
| **Class** | Animal |
| **HP** | 180 |
| **XP when defeated** | 538 |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Combat

| | |
|---|---|
| Class | Animal |
| HP | 180 |
| XP when defeated | 538 |
| Damage | 19 |
| AC | 150 |
| BC | 205 |
| DR | 0 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | 11% (×2.0) |

**When you hit it:** On self: [Minor berserker rage](../conditions/rage_minor.md) (magnitude 1, 1 round, 50% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Meat](../items/meat.md) | 20% | 1 to 2 |
| [Gold coins](../items/gold.md) | 15% | 8 to 20 |
| [Bone](../items/bone.md) | 25% | 1 to 2 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Galmore 24](../maps/galmore_24.md) | Mt. Galmore | 2 | – |
| [Galmore 25](../maps/galmore_25.md) | Mt. Galmore | 9 | – |
| [Galmore 34](../maps/galmore_34.md) | Mt. Galmore | 3 | – |
| [Galmore 35](../maps/galmore_35.md) | Mt. Galmore | 10 | – |
| [Galmore 36](../maps/galmore_36.md) | Mt. Galmore | 6 | – |
| [Galmore 44](../maps/galmore_44.md) | Mt. Galmore | 3 | – |
| [Galmore 45](../maps/galmore_45.md) | Mt. Galmore | 2 | – |
| [Galmore 46](../maps/galmore_46.md) | Mt. Galmore | 1 | – |


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
    | Entry ID | `ridgehowler` |
    | Type (wiki) | Enemy |
    | Spawn group | `ridgehowler` |
    | Loot table | `harrowback_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_newb_1:305` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "ridgehowler",
     "name": "Ridgehowler",
     "iconID": "monsters_newb_1:305",
     "maxHP": 180,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 19,
      "max": 19
     },
     "droplistID": "harrowback_dl",
     "attackCost": 5,
     "attackChance": 150,
     "criticalSkill": 14,
     "criticalMultiplier": 2.0,
     "blockChance": 205,
     "hitReceivedEffect": {
      "conditionsSource": [
       {
        "condition": "rage_minor",
        "magnitude": 1,
        "duration": 1,
        "chance": "50"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ridgehowler.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ridgehowler.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ridgehowler.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ridgehowler.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
