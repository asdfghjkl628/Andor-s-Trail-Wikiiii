---
description: "Giant Cave Arulir is an enemy in Andor's Trail (giant) with 380 HP, worth 503 XP, found in Arulircave 1, Arulircave 2, Arulircave 3. Drops: Gold coins, Meat, Animal hair, Arulir skin."
---

# ![](../assets/icons/monsters/monsters_arulirs_1.png){ .sprite } Giant Cave Arulir

**Found in:** [Arulircave 1](../maps/arulircave1.md), [Arulircave 2](../maps/arulircave2.md), [Arulircave 3](../maps/arulircave3.md), [Arulirmountain 1](../maps/arulirmountain1.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_arulirs_1.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Arulircave 1, Arulircave 2, Arulircave 3 |
| **Class** | Giant |
| **HP** | 380 |
| **XP when defeated** | 503 |
| **Introduced** | [v0.7.8](../versions/0.7.8.md) |

</div>

## Combat

| | |
|---|---|
| Class | Giant |
| HP | 380 |
| XP when defeated | 503 |
| Damage | 3 to 22 |
| AC | 80 |
| BC | 28 |
| DR | 10 |
| Attacks per turn | 1 (5 AP each, 5 AP) |
| Crit chance | 24% (×3.0) |

**Its hits:** On target: [Stunned](../conditions/stunned.md) (magnitude 1, 4 rounds, 26% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 1 to 12 |
| [Meat](../items/meat.md) | 5% | 1 |
| [Animal hair](../items/hair.md) | 10% | 1 |
| [Arulir skin](../items/arulir_skin.md) | 1% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Arulircave 1](../maps/arulircave1.md) | – | 18 | – |
| [Arulircave 2](../maps/arulircave2.md) | – | 5 | – |
| [Arulircave 3](../maps/arulircave3.md) | – | 4 | – |
| [Arulirmountain 1](../maps/arulirmountain1.md) | – | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added |

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
    | Entry ID | `arulir_4` |
    | Type (wiki) | Enemy |
    | Spawn group | `arulir_2` |
    | Loot table | `arulir` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_arulirs:1` |
    | Defined in | `res/raw/monsterlist_arulir_mountain.json` |

    Raw data:

    ```json
    {
     "id": "arulir_4",
     "name": "Giant Cave Arulir",
     "iconID": "monsters_arulirs:1",
     "maxHP": 380,
     "maxAP": 5,
     "moveCost": 5,
     "monsterClass": "giant",
     "attackDamage": {
      "min": 3,
      "max": 22
     },
     "spawnGroup": "arulir_2",
     "droplistID": "arulir",
     "attackCost": 5,
     "attackChance": 80,
     "criticalSkill": 44,
     "criticalMultiplier": 3.0,
     "blockChance": 28,
     "damageResistance": 10,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "stunned",
        "magnitude": 1,
        "duration": 4,
        "chance": "26"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arulir_4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arulir_4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arulir_4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arulir_4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
