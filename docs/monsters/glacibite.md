---
description: "Glacibite is an enemy in Andor's Trail (humanoid) with 212 HP, worth 624 XP, found in Mt. Galmore. Drops: Galmore ice, Ice berries, Bramblefin."
---

# ![](../assets/icons/monsters/monsters_rltiles4_25.png){ .sprite } Glacibite

**Found in:** Mt. Galmore: [Galmore 75](../maps/galmore_75.md), Mt. Galmore: [Galmore 76](../maps/galmore_76.md), Mt. Galmore: [Galmore 85](../maps/galmore_85.md), Mt. Galmore: [Galmore 86](../maps/galmore_86.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles4_25.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Mt. Galmore |
| **Class** | Humanoid |
| **HP** | 212 |
| **XP when defeated** | 624 |
| **Entry ID** | `glacibite` |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 212 |
| XP when defeated | 624 |
| Damage | 9 to 11 |
| Attack chance | 202 |
| Block chance | 176 |
| Damage resistance | 9 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 3 AP |
| Critical skill | 13 |
| Critical multiplier | 2.0 |
| Critical hit chance | 11% |

**On hit:** On target: [Frostbite](../conditions/frostbite.md) (magnitude 2, 2 rounds, 15% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Galmore ice](../items/galmore_ice.md) | 8% | 1 |
| [Ice berries](../items/wild_berry2.md) | 20% | 1 to 2 |
| [Bramblefin](../items/bramblefin_fish.md) | 100% | 1 to 3 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Galmore 75](../maps/galmore_75.md) | Mt. Galmore | 8 | – |
| [Galmore 76](../maps/galmore_76.md) | Mt. Galmore | 7 | – |
| [Galmore 85](../maps/galmore_85.md) | Mt. Galmore | 13 | – |
| [Galmore 86](../maps/galmore_86.md) | Mt. Galmore | 4 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `glacibite` |
    | Spawn group | `glacibite` |
    | Loot table | `glacibite_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles4:25` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "glacibite",
     "name": "Glacibite",
     "iconID": "monsters_rltiles4:25",
     "maxHP": 212,
     "moveCost": 3,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 9,
      "max": 11
     },
     "droplistID": "glacibite_dl",
     "attackCost": 4,
     "attackChance": 202,
     "criticalSkill": 13,
     "criticalMultiplier": 2.0,
     "blockChance": 176,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "frostbite",
        "magnitude": 2,
        "duration": 2,
        "chance": "15"
       }
      ]
     }
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=glacibite.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=glacibite.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=glacibite.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=glacibite.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
