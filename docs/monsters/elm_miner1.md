# ![](../assets/icons/monsters/monsters_rltiles2_178.png){ .sprite } Resurrected miner's skeleton

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_178.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `elm_miner1` |
| **Type** | Enemy |
| **Class** | Undead |
| **HP** | 66 |
| **XP when killed** | 325 |
| **Found in** | elm5f_1, elm5f_2, elm_4f_2 |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 66 |
| Damage | 8 to 10 |
| Attack chance | 159 |
| Block chance | 144 |
| Damage resistance | 5 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 3 AP |
| Critical skill | 20 |
| Critical multiplier | 2.25 |
| Crit chance | 15% |

**On hit:** Heal HP: 5; On self: Flesh rot (magnitude 4, 2 rounds, 25% chance); On target: Flesh rot (magnitude 4, 2 rounds, 25% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

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
| [v0.8.8](../versions/0.8.8.md) | hitEffect: {"conditionsSource": [{"chance": "25", … → {"conditionsSource": [{"chance": "25", … |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_miner1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_miner1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_miner1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_miner1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `elm_miner1` |
    | Spawn group | `elm_mine4` |
    | Loot table | `elm_miner1` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_rltiles2:178` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "elm_miner1",
     "name": "Resurrected miner's skeleton",
     "iconID": "monsters_rltiles2:178",
     "maxHP": 66,
     "moveCost": 3,
     "monsterClass": "undead",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 8,
      "max": 10
     },
     "spawnGroup": "elm_mine4",
     "droplistID": "elm_miner1",
     "attackCost": 3,
     "attackChance": 159,
     "criticalSkill": 20,
     "criticalMultiplier": 2.25,
     "blockChance": 144,
     "damageResistance": 5,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 5,
       "max": 5
      },
      "conditionsSource": [
       {
        "condition": "flesh_rot",
        "magnitude": 4,
        "duration": 2,
        "chance": "25"
       }
      ],
      "conditionsTarget": [
       {
        "condition": "flesh_rot",
        "magnitude": 4,
        "duration": 2,
        "chance": "25"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
