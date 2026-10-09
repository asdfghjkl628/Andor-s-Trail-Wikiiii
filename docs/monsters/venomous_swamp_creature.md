---
description: "Venomous swamp creature is an enemy in Andor's Trail (giant) with 301 HP, worth 1175 XP, found in Galmore 28. Drops: Leech, Gold coins, Small rock, Poison gland."
---

# ![](../assets/icons/monsters/monsters_newb_3_1.png){ .sprite } Venomous swamp creature

**Found in:** [Galmore 28](../maps/galmore_28.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_3_1.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Galmore 28 |
| **Class** | Giant |
| **HP** | 301 |
| **XP when defeated** | 1,175 |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Combat

| | |
|---|---|
| Class | Giant |
| HP | 301 |
| XP when defeated | 1,175 |
| Damage | 28 to 33 |
| AC | 130 |
| BC | 301 |
| DR | 18 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | none |

**Its hits:** On target: [Potent venom](../conditions/potent_venom.md) (magnitude 1, 3 rounds, 15% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Leech](../items/leech.md) | 100% | 3 to 10 |
| [Gold coins](../items/gold.md) | 100% | 19 to 89 |
| [Small rock](../items/rock.md) | 100% | 1 to 5 |
| [Poison gland](../items/gland.md) | 100% | 3 to 10 |
| [Corrupted swamp core](../items/corrupted_swamp_core.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Galmore 28](../maps/galmore_28.md) | – | 1 | Appears later, during a quest |

## Quests that count defeats

- A conversation with stepping on a trigger on [Galmore 28](../maps/galmore_28.md) checks that this enemy has been defeated.


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
    | Entry ID | `venomous_swamp_creature` |
    | Type (wiki) | Enemy |
    | Spawn group | `venomous_swamp_creature` |
    | Loot table | `venomous_swamp_creature_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_newb_3:1` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "venomous_swamp_creature",
     "name": "Venomous swamp creature",
     "iconID": "monsters_newb_3:1",
     "maxHP": 301,
     "moveCost": 9,
     "unique": 1,
     "monsterClass": "giant",
     "attackDamage": {
      "min": 28,
      "max": 33
     },
     "droplistID": "venomous_swamp_creature_dl",
     "attackCost": 4,
     "attackChance": 130,
     "blockChance": 301,
     "damageResistance": 18,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "potent_venom",
        "magnitude": 1,
        "duration": 3,
        "chance": "15"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=venomous_swamp_creature.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=venomous_swamp_creature.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=venomous_swamp_creature.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=venomous_swamp_creature.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
