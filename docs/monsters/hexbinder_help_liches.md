# ![](../assets/icons/monsters/monsters_antison_4.png){ .sprite } Kazaul Hex-Binder lich

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_antison_4.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `hexbinder_help_liches` |
| **Type** | Enemy |
| **Class** | Undead |
| **HP** | 263 |
| **XP when killed** | 760 |
| **Found in** | undertell_3_lava_00 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 263 |
| Damage | 8 to 10 |
| Attack chance | 198 |
| Block chance | 180 |
| Damage resistance | 9 |
| Max AP | 12 |
| Attack cost | 4 AP |
| Attacks per turn | 3 |
| Move cost | 4 AP |
| Critical skill | 11 |
| Critical multiplier | 2.0 |
| Crit chance | 9% |

**On hit:** On target: Withering Focus (magnitude 4, 3 rounds, 28% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 40% | 7 to 12 |
| [Lich dust](../items/lich_dust.md) | 9% | 1 |
| [Major potion of health](../items/health_major2.md) | 30% | 1 to 2 |
| [Liquid courage](../items/pot_courage.md) | 10% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [undertell_3_lava_00](../maps/undertell_3_lava_00.md) | – | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hexbinder_help_liches.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hexbinder_help_liches.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hexbinder_help_liches.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hexbinder_help_liches.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `hexbinder_help_liches` |
    | Spawn group | `helpLich` |
    | Loot table | `hexbinder_lich_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_antison:4` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "hexbinder_help_liches",
     "name": "Kazaul Hex-Binder lich",
     "iconID": "monsters_antison:4",
     "maxHP": 263,
     "maxAP": 12,
     "moveCost": 4,
     "monsterClass": "undead",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 8,
      "max": 10
     },
     "spawnGroup": "helpLich",
     "droplistID": "hexbinder_lich_dl",
     "attackCost": 4,
     "attackChance": 198,
     "criticalSkill": 11,
     "criticalMultiplier": 2.0,
     "blockChance": 180,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "withering_focus",
        "magnitude": 4,
        "duration": 3,
        "chance": "28"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
