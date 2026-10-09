---
description: "Erupting pyreling is an enemy in Andor's Trail (construct) with 246 HP, worth 662 XP, found in Mt. Galmore. Drops: Small rock, Glass gem, Red Crystals, Garnet stone."
---

# ![](../assets/icons/monsters/monsters_newb_1_1204.png){ .sprite } Erupting pyreling

**Found in:** Mt. Galmore: [Galmore 42](../maps/galmore_42.md), Mt. Galmore: [Galmore 43](../maps/galmore_43.md), Mt. Galmore: [Galmore 52](../maps/galmore_52.md), Mt. Galmore: [Galmore 53](../maps/galmore_53.md) (+6 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_1_1204.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Mt. Galmore |
| **Class** | Construct |
| **HP** | 246 |
| **XP when defeated** | 662 |
| **Immune to crits** | Yes |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Combat

| | |
|---|---|
| Class | Construct |
| HP | 246 |
| XP when defeated | 662 |
| Damage | 19 to 26 |
| AC | 150 |
| BC | 214 |
| DR | 8 |
| Attacks per turn | 1 (6 AP each, 10 AP) |
| Crit chance | none |

**Immune to critical hits.**


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Small rock](../items/rock.md) | 85% | 1 to 5 |
| [Glass gem](../items/gem1.md) | 100% | 1 to 2 |
| [Red Crystals](../items/crystal_red.md) | 2% | 1 |
| [Garnet stone](../items/garnet_stone.md) | 3% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Galmore 41](../maps/galmore_41.md) | – | 6 | – |
| [Galmore 42](../maps/galmore_42.md) | Mt. Galmore | 12 | – |
| [Galmore 43](../maps/galmore_43.md) | Mt. Galmore | 1 | – |
| [Galmore 52](../maps/galmore_52.md) | Mt. Galmore | 3 | – |
| [Galmore 53](../maps/galmore_53.md) | Mt. Galmore | 14 | – |
| [Undertell 00](../maps/undertell_00.md) | – | 3 | – |
| [Undertell 3 lava 00](../maps/undertell_3_lava_00.md) | – | 3 | – |
| [Undertell 3 lava 01](../maps/undertell_3_lava_01.md) | – | 4 | – |
| [Undertell 3 lava 10](../maps/undertell_3_lava_10.md) | – | 3 | – |
| [Undertell 3 lava 11](../maps/undertell_3_lava_11.md) | – | 2 | – |


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
    | Entry ID | `erupting_pyreling` |
    | Type (wiki) | Enemy |
    | Spawn group | `erupting_pyreling` |
    | Loot table | `erupting_pyreling_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_newb_1:1204` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "erupting_pyreling",
     "name": "Erupting pyreling",
     "iconID": "monsters_newb_1:1204",
     "maxHP": 246,
     "moveCost": 8,
     "monsterClass": "construct",
     "attackDamage": {
      "min": 19,
      "max": 26
     },
     "droplistID": "erupting_pyreling_dl",
     "attackCost": 6,
     "attackChance": 150,
     "blockChance": 214,
     "damageResistance": 8
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erupting_pyreling.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erupting_pyreling.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erupting_pyreling.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erupting_pyreling.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
