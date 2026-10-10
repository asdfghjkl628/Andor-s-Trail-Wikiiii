---
description: "Undead Kamelio is an enemy in Andor's Trail (undead) with 304 HP, worth 796 XP, found in Elm 5f 2. Drops: Gold coins, Prim arming sword, Fire opal necklace, Kazarite cloak."
---

# ![](../assets/icons/monsters/monsters_omi2_20.png){ .sprite } Undead Kamelio

**Found in:** [Elm 5f 2](../maps/elm5f_2.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_omi2_20.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Elm 5f 2 |
| **Class** | Undead |
| **HP** | 304 |
| **XP when defeated** | 796 |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

## Combat

| | |
|---|---|
| Class | Undead |
| HP | 304 |
| XP when defeated | 796 |
| Damage | 12 to 18 |
| AC | 181 |
| BC | 140 |
| DR | 12 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | 15% (×2.0) |

**Its hits:** Heal HP: 0 to 6; On target: [Bleeding wound](../conditions/bleeding_wound.md) (magnitude 4, 4 rounds, 30% chance)

**When you hit it:** On target: [Nausea](../conditions/nausea.md) (magnitude 4, 2 rounds, 30% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 3 to 9 |
| [Prim arming sword](../items/kamelio_drop1.md) | 100% | 1 |
| [Fire opal necklace](../items/kamelio_drop2.md) | 100% | 1 |
| [Kazarite cloak](../items/kamelio_drop3.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Elm 5f 2](../maps/elm5f_2.md) | – | 1 | Appears later, during a quest |

## Quests that count defeats

- [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-54) with stepping on a trigger on [Elm 5f 2](../maps/elm5f_2.md) checks that this enemy has been defeated.


## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |

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
    | Entry ID | `kamelio2` |
    | Type (wiki) | Enemy |
    | Spawn group | `kamelio2` |
    | Loot table | `kamelio2` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_omi2:20` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "kamelio2",
     "name": "Undead Kamelio",
     "iconID": "monsters_omi2:20",
     "maxHP": 304,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "undead",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 12,
      "max": 18
     },
     "droplistID": "kamelio2",
     "attackCost": 5,
     "attackChance": 181,
     "criticalSkill": 20,
     "criticalMultiplier": 2.0,
     "blockChance": 140,
     "damageResistance": 12,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 0,
       "max": 6
      },
      "conditionsTarget": [
       {
        "condition": "bleeding_wound",
        "magnitude": 4,
        "duration": 4,
        "chance": "30"
       }
      ]
     },
     "hitReceivedEffect": {
      "conditionsTarget": [
       {
        "condition": "nausea",
        "magnitude": 4,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kamelio2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kamelio2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kamelio2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kamelio2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
