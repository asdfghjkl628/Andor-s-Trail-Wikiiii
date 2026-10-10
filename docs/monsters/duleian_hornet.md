---
description: "Duleian buzzer is an enemy in Andor's Trail (insect) with 77 HP, worth 281 XP, found in Wexlow Village. Drops: Insect wing, Insect stinger."
---

# ![](../assets/icons/monsters/monsters_ld2_222.png){ .sprite } Duleian buzzer

**Found in:** Wexlow Village: [Way to wexlow 1](../maps/way_to_wexlow1.md), Wexlow Village: [Wayto feygard duleian 1](../maps/wayto_feygard_duleian_1.md), [Cabin norcity road 1](../maps/cabin_norcity_road1.md), [Cabin norcity road 2](../maps/cabin_norcity_road2.md) (+6 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld2_222.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Wexlow Village |
| **Class** | Insect |
| **HP** | 77 |
| **XP when defeated** | 281 |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Combat

| | |
|---|---|
| Class | Insect |
| HP | 77 |
| XP when defeated | 281 |
| Damage | 4 to 5 |
| AC | 89 |
| BC | 175 |
| DR | 9 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | none |

**Its hits:** On target: [Insect contagion](../conditions/contagion.md) (magnitude 1, 3 rounds, 33% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Insect wing](../items/insectwing.md) | 10% | 1 |
| [Insect stinger](../items/insect_stinger.md) | 10% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Cabin norcity road 1](../maps/cabin_norcity_road1.md) | – | 1 | – |
| [Cabin norcity road 2](../maps/cabin_norcity_road2.md) | – | 7 | – |
| [Cabin norcity road 3](../maps/cabin_norcity_road3.md) | – | 4 | – |
| [Way to sullengard east 1](../maps/way_to_sullengard_east1.md) | – | 9 | – |
| [Way to wexlow 1](../maps/way_to_wexlow1.md) | Wexlow Village | 1 | – |
| [Wayto feygard duleian 1](../maps/wayto_feygard_duleian_1.md) | Wexlow Village | 8 | – |
| [Wayto feygard duleian 2](../maps/wayto_feygard_duleian_2.md) | – | 6 | – |
| [Waytobrightport 3](../maps/waytobrightport3.md) | – | 2 | – |
| [Waytobrightport 6](../maps/waytobrightport6.md) | – | 4 | – |
| [Waytobrightport 8](../maps/waytobrightport8.md) | – | 7 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added |

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
    | Entry ID | `duleian_hornet` |
    | Type (wiki) | Enemy |
    | Spawn group | `duleian_hornet` |
    | Loot table | `flying_insect_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_ld2:222` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "duleian_hornet",
     "name": "Duleian buzzer",
     "iconID": "monsters_ld2:222",
     "maxHP": 77,
     "moveCost": 4,
     "monsterClass": "insect",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 4,
      "max": 5
     },
     "spawnGroup": "duleian_hornet",
     "droplistID": "flying_insect_dl",
     "attackCost": 3,
     "attackChance": 89,
     "blockChance": 175,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "contagion",
        "magnitude": 1,
        "duration": 3,
        "chance": "33"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=duleian_hornet.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=duleian_hornet.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=duleian_hornet.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=duleian_hornet.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
