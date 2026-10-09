---
description: "Molten pyreling is an enemy in Andor's Trail (construct) with 236 HP, worth 619 XP, found in Mt. Galmore. Drops: Small rock, Glass gem, Azure gem."
---

# ![](../assets/icons/monsters/monsters_newb_1_1201.png){ .sprite } Molten pyreling

**Found in:** Mt. Galmore: [Galmore 33](../maps/galmore_33.md), Mt. Galmore: [Galmore 42](../maps/galmore_42.md), Mt. Galmore: [Galmore 43](../maps/galmore_43.md), Mt. Galmore: [Galmore 53](../maps/galmore_53.md) (+8 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_1_1201.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Mt. Galmore |
| **Class** | Construct |
| **HP** | 236 |
| **XP when defeated** | 619 |
| **Immune to critical hits** | Yes |
| **Entry ID** | `molten_pyreling` |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Construct |
| HP | 236 |
| XP when defeated | 619 |
| Damage | 15 to 21 |
| Attack chance | 130 |
| Block chance | 214 |
| Damage resistance | 8 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Small rock](../items/rock.md) | 95% | 1 to 5 |
| [Glass gem](../items/gem1.md) | 75% | 1 to 2 |
| [Azure gem](../items/gem6.md) | 3% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Galmore 33](../maps/galmore_33.md) | Mt. Galmore | 2 | – |
| [Galmore 41](../maps/galmore_41.md) | – | 2 | – |
| [Galmore 42](../maps/galmore_42.md) | Mt. Galmore | 2 | – |
| [Galmore 43](../maps/galmore_43.md) | Mt. Galmore | 10 | – |
| [Galmore 53](../maps/galmore_53.md) | Mt. Galmore | 3 | – |
| [Undertell 00](../maps/undertell_00.md) | – | 5 | – |
| [Undertell 10](../maps/undertell_10.md) | – | 5 | – |
| [Undertell 11](../maps/undertell_11.md) | – | 4 | – |
| [Undertell 21](../maps/undertell_21.md) | – | 3 | – |
| [Undertell 3 lava 00](../maps/undertell_3_lava_00.md) | – | 2 | – |
| [Undertell 3 lava 01](../maps/undertell_3_lava_01.md) | – | 4 | – |
| [Undertell 3 lava 11](../maps/undertell_3_lava_11.md) | – | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `molten_pyreling` |
    | Spawn group | `molten_pyreling` |
    | Loot table | `molten_pyreling_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_newb_1:1201` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "molten_pyreling",
     "name": "Molten pyreling",
     "iconID": "monsters_newb_1:1201",
     "maxHP": 236,
     "moveCost": 10,
     "monsterClass": "construct",
     "attackDamage": {
      "min": 15,
      "max": 21
     },
     "droplistID": "molten_pyreling_dl",
     "attackCost": 10,
     "attackChance": 130,
     "blockChance": 214,
     "damageResistance": 8
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=molten_pyreling.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=molten_pyreling.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=molten_pyreling.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=molten_pyreling.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
