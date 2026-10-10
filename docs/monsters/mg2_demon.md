---
description: "Demon is an enemy in Andor's Trail (demon) with 180 HP, worth 313 XP, found in Mt. Galmore. Drops: Gold coins, Wanted poster."
---

# ![](../assets/icons/monsters/monsters_ld2_238.png){ .sprite } Demon

**Found in:** Mt. Galmore: [Galmore 52](../maps/galmore_52.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld2_238.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Mt. Galmore |
| **Class** | Demon |
| **HP** | 180 |
| **XP when defeated** | 313 |
| **Immune to crits** | Yes |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Combat

| | |
|---|---|
| Class | Demon |
| HP | 180 |
| XP when defeated | 313 |
| Damage | 3 to 20 |
| AC | 90 |
| BC | 75 |
| DR | 2 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 12% (×1.5) |

**Immune to critical hits.**

**Its hits:** Heal HP: 2

**When you hit it:** Heal HP: 2; increaseAttackerCurrentHP: -2


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 30 to 130 |
| [Wanted poster](../items/mg2_andor_wanted.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Galmore 52](../maps/galmore_52.md) | Mt. Galmore | 3 | Appears later, during a quest |


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
    | Entry ID | `mg2_demon` |
    | Type (wiki) | Enemy |
    | Spawn group | `mg2_demon` |
    | Loot table | `mg2_demon` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:238` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "mg2_demon",
     "name": "Demon",
     "iconID": "monsters_ld2:238",
     "maxHP": 180,
     "moveCost": 5,
     "monsterClass": "demon",
     "attackDamage": {
      "min": 3,
      "max": 20
     },
     "droplistID": "mg2_demon",
     "attackCost": 3,
     "attackChance": 90,
     "criticalSkill": 15,
     "criticalMultiplier": 1.5,
     "blockChance": 75,
     "damageResistance": 2,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 2,
       "max": 2
      }
     },
     "hitReceivedEffect": {
      "increaseCurrentHP": {
       "min": 2,
       "max": 2
      },
      "increaseAttackerCurrentHP": {
       "min": -2,
       "max": -2
      }
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_demon.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_demon.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_demon.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_demon.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
