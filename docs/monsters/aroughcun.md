---
description: "Aroughcun is an enemy in Andor's Trail (animal) with 204 HP, worth 670 XP, found in Mt. Galmore. Drops: Bramblefin, Rotten fish, Headless fish, Rotten meat."
---

# ![](../assets/icons/monsters/monsters_newb_1_275.png){ .sprite } Aroughcun

**Found in:** Mt. Galmore: [Galmore 55](../maps/galmore_55.md), Mt. Galmore: [Galmore 57](../maps/galmore_57.md), Mt. Galmore: [Galmore 63](../maps/galmore_63.md), Mt. Galmore: [Galmore 64](../maps/galmore_64.md) (+5 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_1_275.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Mt. Galmore |
| **Class** | Animal |
| **HP** | 204 |
| **XP when defeated** | 670 |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Combat

| | |
|---|---|
| Class | Animal |
| HP | 204 |
| XP when defeated | 670 |
| Damage | 13 to 18 |
| AC | 191 |
| BC | 176 |
| DR | 9 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | 11% (×2.75) |

**Its hits:** On target: [Rabies](../conditions/rabies.md) (magnitude 2, 2 rounds, 30% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Bramblefin](../items/bramblefin_fish.md) | 25% | 1 |
| [Rotten fish](../items/rotten_fish.md) | 30% | 1 |
| [Headless fish](../items/headless_fish.md) | 25% | 1 |
| [Rotten meat](../items/meat2.md) | 35% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Galmore 55](../maps/galmore_55.md) | Mt. Galmore | 6 | – |
| [Galmore 57](../maps/galmore_57.md) | Mt. Galmore | 5 | – |
| [Galmore 63](../maps/galmore_63.md) | Mt. Galmore | 8 | – |
| [Galmore 64](../maps/galmore_64.md) | Mt. Galmore | 12 | – |
| [Galmore 65](../maps/galmore_65.md) | Mt. Galmore | 9 | – |
| [Galmore 66](../maps/galmore_66.md) | Mt. Galmore | 7 | – |
| [Galmore 67](../maps/galmore_67.md) | Mt. Galmore | 9 | – |
| [Galmore 68](../maps/galmore_68.md) | Mt. Galmore | 9 | – |
| [Galmore 73](../maps/galmore_73.md) | Mt. Galmore | 8 | – |


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
    | Entry ID | `aroughcun` |
    | Type (wiki) | Enemy |
    | Spawn group | `aroughcun` |
    | Loot table | `aroughcun_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_newb_1:275` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "aroughcun",
     "name": "Aroughcun",
     "iconID": "monsters_newb_1:275",
     "maxHP": 204,
     "moveCost": 4,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 13,
      "max": 18
     },
     "droplistID": "aroughcun_dl",
     "attackCost": 4,
     "attackChance": 191,
     "criticalSkill": 13,
     "criticalMultiplier": 2.75,
     "blockChance": 176,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "rabies",
        "magnitude": 2,
        "duration": 2,
        "chance": "30"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=aroughcun.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=aroughcun.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=aroughcun.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=aroughcun.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
