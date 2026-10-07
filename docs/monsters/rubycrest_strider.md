---
description: "Rubycrest strider is an enemy in Andor's Trail (animal) with 293 HP, worth 1065 XP, found in Stoutford. Drops: Paintbrush, Rubycrest feather."
---

# ![](../assets/icons/monsters/monsters_newb_1_216.png){ .sprite } Rubycrest strider

**Found in:** Stoutford: [stoutford_filler_1](../maps/stoutford_filler_1.md), Stoutford: [stoutford_filler_2](../maps/stoutford_filler_2.md), Stoutford: [stoutford_filler_3](../maps/stoutford_filler_3.md), [stoutford_filler_4](../maps/stoutford_filler_4.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_1_216.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Stoutford |
| **Class** | Animal |
| **HP** | 293 |
| **XP when defeated** | 1,065 |
| **Entry ID** | `rubycrest_strider` |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 293 |
| XP when defeated | 1,065 |
| Damage | 6 to 18 |
| Attack chance | 175 |
| Block chance | 280 |
| Damage resistance | 10 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 3 AP |
| Critical skill | 15 |
| Critical multiplier | 2.0 |
| Critical hit chance | 12% |

**On hit:** On target: Head wound (magnitude 1, 2 rounds, 20% chance)

**When hit:** On self: Minor speed (magnitude 1, 1 rounds, 50% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Paintbrush](../items/paint_brush.md) | 100% | 1 |
| [Rubycrest feather](../items/rubycrest_feather.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [stoutford_filler_1](../maps/stoutford_filler_1.md) | Stoutford | 1 | Appears later, during a quest |
| [stoutford_filler_2](../maps/stoutford_filler_2.md) | Stoutford | 1 | Appears later, during a quest |
| [stoutford_filler_3](../maps/stoutford_filler_3.md) | Stoutford | 2 | Appears later, during a quest |
| [stoutford_filler_4](../maps/stoutford_filler_4.md) | – | 1 | Appears later, during a quest |

## Quests that count defeats

- [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-57) with stepping on a trigger on [stoutford_filler_1](../maps/stoutford_filler_1.md), stepping on a trigger on [stoutford_filler_2](../maps/stoutford_filler_2.md) checks that this enemy has been defeated.


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `rubycrest_strider` |
    | Spawn group | `rubycrest_strider` |
    | Loot table | `rubycrest_strider_dl` |
    | Conversation | – |
    | Faction | `rubycrest_strider` |
    | Movement | – |
    | Icon | `monsters_newb_1:216` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "rubycrest_strider",
     "name": "Rubycrest strider",
     "iconID": "monsters_newb_1:216",
     "maxHP": 293,
     "moveCost": 3,
     "unique": 1,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 6,
      "max": 18
     },
     "faction": "rubycrest_strider",
     "droplistID": "rubycrest_strider_dl",
     "attackCost": 3,
     "attackChance": 175,
     "criticalSkill": 15,
     "criticalMultiplier": 2.0,
     "blockChance": 280,
     "damageResistance": 10,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "head_wound",
        "magnitude": 1,
        "duration": 2,
        "chance": "20"
       }
      ]
     },
     "hitReceivedEffect": {
      "conditionsSource": [
       {
        "condition": "speed_minor",
        "magnitude": 1,
        "duration": 1,
        "chance": "50"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rubycrest_strider.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rubycrest_strider.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rubycrest_strider.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rubycrest_strider.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
