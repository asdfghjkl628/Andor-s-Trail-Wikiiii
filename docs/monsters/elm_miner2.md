---
description: "Foul miner's skeleton is an enemy in Andor's Trail (undead) with 82 HP, worth 282 XP, found in elm5f_1, elm5f_2, elm_4f_2. Drops: Bone, Blackwater rusted pickaxe, Empty vial, Gold coins."
---

# ![](../assets/icons/monsters/monsters_tometik9_55.png){ .sprite } Foul miner's skeleton

**Found in:** [elm5f_1](../maps/elm5f_1.md), [elm5f_2](../maps/elm5f_2.md), [elm_4f_2](../maps/elm_4f_2.md), [elm_4f_3](../maps/elm_4f_3.md) (+2 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik9_55.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | elm5f_1, elm5f_2, elm_4f_2 |
| **Class** | Undead |
| **HP** | 82 |
| **XP when defeated** | 282 |
| **Entry ID** | `elm_miner2` |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 82 |
| XP when defeated | 282 |
| Damage | 6 to 12 |
| Attack chance | 151 |
| Block chance | 137 |
| Damage resistance | 4 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 3 AP |
| Critical skill | 15 |
| Critical multiplier | 1.5 |
| Critical hit chance | 12% |

**On hit:** Heal HP: 3; On target: Blood poisoning (magnitude 4, 2 rounds, 30% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Bone](../items/bone.md) | 16.6667% | 1 to 3 |
| [Blackwater rusted pickaxe](../items/bwm_pick.md) | 3.33333% | 1 |
| [Empty vial](../items/vial_empty2.md) | 8.33333% | 1 |
| [Gold coins](../items/gold.md) | 100% | 6 to 18 |
| [Rough ring of damage](../items/ring_rough_damage.md) | 3.33333% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [elm5f_1](../maps/elm5f_1.md) | – | 3 | – |
| [elm5f_2](../maps/elm5f_2.md) | – | 11 | – |
| [elm_4f_2](../maps/elm_4f_2.md) | – | 4 | – |
| [elm_4f_3](../maps/elm_4f_3.md) | – | 12 | – |
| [elm_4f_4](../maps/elm_4f_4.md) | – | 6 | – |
| [elm_4f_5](../maps/elm_4f_5.md) | – | 3 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `elm_miner2` |
    | Spawn group | `elm_mine4` |
    | Loot table | `elm_miner1` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_tometik9:55` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "elm_miner2",
     "name": "Foul miner's skeleton",
     "iconID": "monsters_tometik9:55",
     "maxHP": 82,
     "moveCost": 3,
     "monsterClass": "undead",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 6,
      "max": 12
     },
     "spawnGroup": "elm_mine4",
     "droplistID": "elm_miner1",
     "attackCost": 4,
     "attackChance": 151,
     "criticalSkill": 15,
     "criticalMultiplier": 1.5,
     "blockChance": 137,
     "damageResistance": 4,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 3,
       "max": 3
      },
      "conditionsTarget": [
       {
        "condition": "poison_blood",
        "magnitude": 4,
        "duration": 2,
        "chance": "30"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_miner2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_miner2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_miner2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_miner2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
