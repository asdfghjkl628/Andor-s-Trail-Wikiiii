---
description: "Musty prowler is an enemy in Andor's Trail (ghost) with 177 HP, worth 522 XP, found in haunted_cemetery1, haunted_cemetery2, haunted_forest12. Drops: Gold coins, Tonic of blood."
---

# ![](../assets/icons/monsters/monsters_ld2_238.png){ .sprite } Musty prowler

**Found in:** [haunted_cemetery1](../maps/haunted_cemetery1.md), [haunted_cemetery2](../maps/haunted_cemetery2.md), [haunted_forest12](../maps/haunted_forest12.md), [haunted_forest13](../maps/haunted_forest13.md) (+10 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld2_238.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | haunted_cemetery1, haunted_cemetery2, haunted_forest12 |
| **Class** | Ghost |
| **HP** | 177 |
| **XP when defeated** | 522 |
| **Immune to critical hits** | Yes |
| **Entry ID** | `musty_prowler` |
| **Introduced** | [v0.8.3](../versions/0.8.3.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Ghost |
| HP | 177 |
| XP when defeated | 522 |
| Damage | 13 to 18 |
| Attack chance | 134 |
| Block chance | 180 |
| Damage resistance | 7 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 3 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.

**When hit:** On self: Regeneration (magnitude 4, 1 rounds, 100% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 40% | 9 to 15 |
| [Tonic of blood](../items/tonic_of_blood.md) | 10% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [haunted_cemetery1](../maps/haunted_cemetery1.md) | – | 5 | – |
| [haunted_cemetery2](../maps/haunted_cemetery2.md) | – | 4 | – |
| [haunted_forest12](../maps/haunted_forest12.md) | – | 3 | – |
| [haunted_forest13](../maps/haunted_forest13.md) | – | 1 | – |
| [haunted_forest16](../maps/haunted_forest16.md) | – | 1 | – |
| [haunted_forest17](../maps/haunted_forest17.md) | – | 1 | – |
| [haunted_forest19](../maps/haunted_forest19.md) | – | 1 | – |
| [haunted_forest20](../maps/haunted_forest20.md) | – | 5 | – |
| [haunted_forest21](../maps/haunted_forest21.md) | – | 2 | – |
| [haunted_forest22](../maps/haunted_forest22.md) | – | 2 | – |
| [haunted_forest24](../maps/haunted_forest24.md) | – | 1 | – |
| [haunted_forest7](../maps/haunted_forest7.md) | – | 2 | – |
| [haunted_forest_way_to_house5](../maps/haunted_forest_way_to_house5.md) | – | 3 | – |
| [vilegard_sullengard_filler1](../maps/vilegard_sullengard_filler1.md) | – | 4 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.3](../versions/0.8.3.md) | Added |
| [v0.8.4](../versions/0.8.4.md) | monsterClass: undead → ghost |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `musty_prowler` |
    | Spawn group | `musty_prowler` |
    | Loot table | `musty_prowler_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:238` |
    | Defined in | `res/raw/monsterlist_haunted_forest.json` |

    Raw data:

    ```json
    {
     "id": "musty_prowler",
     "name": "Musty prowler",
     "iconID": "monsters_ld2:238",
     "maxHP": 177,
     "moveCost": 3,
     "monsterClass": "ghost",
     "attackDamage": {
      "min": 13,
      "max": 18
     },
     "droplistID": "musty_prowler_dl",
     "attackCost": 3,
     "attackChance": 134,
     "blockChance": 180,
     "damageResistance": 7,
     "hitEffect": {},
     "hitReceivedEffect": {
      "conditionsSource": [
       {
        "condition": "regen2",
        "magnitude": 4,
        "duration": 1,
        "chance": "100"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=musty_prowler.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=musty_prowler.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=musty_prowler.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=musty_prowler.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
