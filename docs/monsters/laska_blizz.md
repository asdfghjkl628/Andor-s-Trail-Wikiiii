---
description: "Laska blizz is an enemy in Andor's Trail (giant) with 300 HP, worth 832 XP, found in Mt. Galmore. Drops: Laska blizz fur, Bramblefin, Galmore ice."
---

# ![](../assets/icons/monsters/monsters_rltiles4_26.png){ .sprite } Laska blizz

**Found in:** Mt. Galmore: [Galmore 76](../maps/galmore_76.md), Mt. Galmore: [Galmore 85](../maps/galmore_85.md), Mt. Galmore: [Galmore 86](../maps/galmore_86.md)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_rltiles4_26.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Mt. Galmore |
| **Class** | Giant |
| **HP** | 300 |
| **XP when defeated** | 832 |
| **Introduced** | [v0.8.8](../versions/0.8.8.md) |

</div>

## Combat

| | |
|---|---|
| Class | Giant |
| HP | 300 |
| XP when defeated | 832 |
| Damage | 25 to 27 |
| AC | 130 |
| BC | 200 |
| DR | 11 |
| Attacks per turn | 1 (7 AP each, 10 AP) |
| Crit chance | 7% (×2.0) |

**Its hits:** On target: [Frostbite](../conditions/frostbite.md) (magnitude 3, 4 rounds, 15% chance); [Head wound](../conditions/head_wound.md) (magnitude 1, 3 rounds, 25% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Laska blizz fur](../items/laska_fur.md) | 5% | 1 |
| [Bramblefin](../items/bramblefin_fish.md) | 15% | 1 to 2 |
| [Galmore ice](../items/galmore_ice.md) | 10% | 1 to 2 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Galmore 76](../maps/galmore_76.md) | Mt. Galmore | 1 | – |
| [Galmore 85](../maps/galmore_85.md) | Mt. Galmore | 2 | – |
| [Galmore 86](../maps/galmore_86.md) | Mt. Galmore | 8 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.8](../versions/0.8.8.md) | Added |
| [v0.8.14](../versions/0.8.14.md) | Attack chance: added (130)<br>Attack cost: added (7)<br>Attack damage: added (25–27)<br>Block chance: added (200)<br>Critical multiplier: added (2)<br>Critical skill: added (8)<br>Damage resistance: added (11)<br>Loot table added<br>On hit, condition on target: added [Frostbite](../conditions/frostbite.md) (magnitude 3, 4 rounds, 15% chance)<br>On hit, condition on target: added [Head wound](../conditions/head_wound.md) (magnitude 1, 3 rounds, 25% chance)<br>(+3 more) |

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
    | Entry ID | `laska_blizz` |
    | Type (wiki) | Enemy |
    | Spawn group | `laska_blizz` |
    | Loot table | `laska_blizz_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles4:26` |
    | Defined in | `res/raw/monsterlist_mt_galmore.json` |

    Raw data:

    ```json
    {
     "id": "laska_blizz",
     "name": "Laska blizz",
     "iconID": "monsters_rltiles4:26",
     "maxHP": 300,
     "monsterClass": "giant",
     "attackDamage": {
      "min": 25,
      "max": 27
     },
     "droplistID": "laska_blizz_dl",
     "attackCost": 7,
     "attackChance": 130,
     "criticalSkill": 8,
     "criticalMultiplier": 2.0,
     "blockChance": 200,
     "damageResistance": 11,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "frostbite",
        "magnitude": 3,
        "duration": 4,
        "chance": "15"
       },
       {
        "condition": "head_wound",
        "magnitude": 1,
        "duration": 3,
        "chance": "25"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=laska_blizz.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=laska_blizz.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=laska_blizz.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=laska_blizz.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
