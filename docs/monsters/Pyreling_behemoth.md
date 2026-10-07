---
description: "Pyreling behemoth is an enemy in Andor's Trail (construct) with 360 HP, worth 997 XP, found in galmore_71. Drops: Blazebite, Major potion of health, Emberwylde, Glass gem."
---

# ![](../assets/icons/monsters/monsters_newb_3_11.png){ .sprite } Pyreling behemoth

**Found in:** [galmore_71](../maps/galmore_71.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_3_11.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | galmore_71 |
| **Class** | Construct |
| **HP** | 360 |
| **XP when defeated** | 997 |
| **Immune to critical hits** | Yes |
| **Entry ID** | `Pyreling_behemoth` |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Construct |
| HP | 360 |
| XP when defeated | 997 |
| Damage | 28 to 20 |
| Attack chance | 170 |
| Block chance | 229 |
| Damage resistance | 13 |
| Max AP | 10 |
| Attack cost | 6 AP |
| Attacks per turn | 1 |
| Move cost | 9 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.

**When hit:** On target: Ablaze (magnitude 2, 4 rounds, 75% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Blazebite](../items/blazebite.md) | 100% | 1 |
| [Major potion of health](../items/health_major2.md) | 100% | 3 to 5 |
| [Emberwylde](../items/emberwylde.md) | 100% | 1 |
| [Glass gem](../items/gem1.md) | 100% | 5 to 15 |
| [Azure gem](../items/gem6.md) | 100% | 1 to 5 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [galmore_71](../maps/galmore_71.md) | – | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `Pyreling_behemoth` |
    | Spawn group | `Pyreling_behemoth` |
    | Loot table | `Pyreling_behemoth_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_newb_3:11` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "Pyreling_behemoth",
     "name": "Pyreling behemoth",
     "iconID": "monsters_newb_3:11",
     "maxHP": 360,
     "moveCost": 9,
     "unique": 1,
     "monsterClass": "construct",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 28,
      "max": 20
     },
     "droplistID": "Pyreling_behemoth_dl",
     "attackCost": 6,
     "attackChance": 170,
     "blockChance": 229,
     "damageResistance": 13,
     "hitReceivedEffect": {
      "conditionsTarget": [
       {
        "condition": "fire",
        "magnitude": 2,
        "duration": 4,
        "chance": "75"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=Pyreling_behemoth.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=Pyreling_behemoth.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=Pyreling_behemoth.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=Pyreling_behemoth.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
