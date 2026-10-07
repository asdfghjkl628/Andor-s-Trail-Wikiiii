# ![](../assets/icons/monsters/monsters_tometik8_42.png){ .sprite } Bone-Marshal lich

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik8_42.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `bone_marshal_lich_pearl` |
| **Type** | Enemy |
| **Class** | Undead |
| **HP** | 232 |
| **XP when killed** | 693 |
| **Found in** | undertell_21, undertell_3_lava_01, undertell_4_01 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 232 |
| Damage | 9 to 11 |
| Attack chance | 202 |
| Block chance | 195 |
| Damage resistance | 9 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 4 AP |
| Critical skill | 13 |
| Critical multiplier | 2.0 |
| Crit chance | 11% |

**On hit:** On target: Kazaul exposure (magnitude 1, 2 rounds, 25% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Soul pearl](../items/soul_pearl.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [undertell_21](../maps/undertell_21.md) | – | 1 | appears later in a quest |
| [undertell_3_lava_01](../maps/undertell_3_lava_01.md) | – | 1 | appears later in a quest |
| [undertell_4_01](../maps/undertell_4_01.md) | – | 1 | appears later in a quest |
| [undertell_5](../maps/undertell_5.md) | – | 1 | appears later in a quest |
| [undertell_7_10](../maps/undertell_7_10.md) | – | 1 | appears later in a quest |


## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bone_marshal_lich_pearl.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bone_marshal_lich_pearl.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bone_marshal_lich_pearl.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bone_marshal_lich_pearl.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `bone_marshal_lich_pearl` |
    | Spawn group | `lich_spawn1` |
    | Loot table | `soul_pearl_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik8:42` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "bone_marshal_lich_pearl",
     "name": "Bone-Marshal lich",
     "iconID": "monsters_tometik8:42",
     "maxHP": 232,
     "moveCost": 4,
     "unique": 1,
     "monsterClass": "undead",
     "attackDamage": {
      "min": 9,
      "max": 11
     },
     "spawnGroup": "lich_spawn1",
     "horizontalFlipChance": 50,
     "droplistID": "soul_pearl_dl",
     "attackCost": 4,
     "attackChance": 202,
     "criticalSkill": 13,
     "criticalMultiplier": 2.0,
     "blockChance": 195,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "kazaul_exposure",
        "magnitude": 1,
        "duration": 2,
        "chance": "25"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
