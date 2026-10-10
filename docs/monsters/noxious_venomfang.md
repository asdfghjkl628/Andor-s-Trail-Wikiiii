---
description: "Noxious venomfang is an enemy in Andor's Trail (reptile) with 44 HP, worth 177 XP, found in Blackwater Mountain. Drops: Poison gland, Meat, Gold coins, Ruby gem."
---

# ![](../assets/icons/monsters/monsters_omi2_8.png){ .sprite } Noxious venomfang

**Found in:** Blackwater Mountain: [Blackwater mountain 73](../maps/blackwater_mountain73.md), [Blackwater mountain 74](../maps/blackwater_mountain74.md), [Blackwater mountain 75](../maps/blackwater_mountain75.md), [Blackwater mountain 76](../maps/blackwater_mountain76.md) (+3 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_omi2_8.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Blackwater Mountain |
| **Class** | Reptile |
| **HP** | 44 |
| **XP when defeated** | 177 |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

## Combat

| | |
|---|---|
| Class | Reptile |
| HP | 44 |
| XP when defeated | 177 |
| Damage | 3 to 6 |
| AC | 155 |
| BC | 85 |
| DR | 4 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | none |

**Its hits:** On target: [Weak Poison](../conditions/poison_weak.md) (magnitude 1, 3 rounds, 60% chance)

**When it dies:** On self: [Weak Poison](../conditions/poison_weak.md) (magnitude 3, 2 rounds, 30% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Poison gland](../items/gland.md) | 5% | 0 to 2 |
| [Meat](../items/meat.md) | 5% | 1 |
| [Gold coins](../items/gold.md) | 100% | 1 to 12 |
| [Ruby gem](../items/gem2.md) | 5% | 1 |
| [Venomfang dirk](../items/venomfang_dagger.md) | 0.2% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Blackwater mountain 73](../maps/blackwater_mountain73.md) | Blackwater Mountain | 9 | – |
| [Blackwater mountain 74](../maps/blackwater_mountain74.md) | – | 3 | – |
| [Blackwater mountain 75](../maps/blackwater_mountain75.md) | – | 7 | – |
| [Blackwater mountain 76](../maps/blackwater_mountain76.md) | – | 2 | – |
| [Elm mine 2](../maps/elm_mine2.md) | – | 5 | – |
| [Elm mine 3](../maps/elm_mine3.md) | – | 4 | – |
| [Elm mine 5](../maps/elm_mine5.md) | – | 5 | – |


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
    | Entry ID | `noxious_venomfang` |
    | Type (wiki) | Enemy |
    | Spawn group | `venomfang_2` |
    | Loot table | `bwm_venomfang2` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_omi2:8` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "noxious_venomfang",
     "name": "Noxious venomfang",
     "iconID": "monsters_omi2:8",
     "maxHP": 44,
     "moveCost": 3,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 3,
      "max": 6
     },
     "spawnGroup": "venomfang_2",
     "droplistID": "bwm_venomfang2",
     "attackCost": 3,
     "attackChance": 155,
     "blockChance": 85,
     "damageResistance": 4,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "poison_weak",
        "magnitude": 1,
        "duration": 3,
        "chance": "60"
       }
      ]
     },
     "deathEffect": {
      "conditionsSource": [
       {
        "condition": "poison_weak",
        "magnitude": 3,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=noxious_venomfang.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=noxious_venomfang.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=noxious_venomfang.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=noxious_venomfang.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
