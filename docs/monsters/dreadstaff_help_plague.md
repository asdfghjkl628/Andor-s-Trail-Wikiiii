# ![](../assets/icons/monsters/monsters_antison_2.png){ .sprite } Dreadstaff lich

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_antison_2.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `dreadstaff_help_plague` |
| **Type** | Enemy |
| **Class** | Undead |
| **HP** | 285 |
| **XP when killed** | 822 |
| **Found in** | undertell_3_lava_01, undertell_3_lava_10 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 285 |
| Damage | 10 to 13 |
| Attack chance | 210 |
| Block chance | 185 |
| Damage resistance | 11 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 3 AP |
| Critical skill | 15 |
| Critical multiplier | 2.1 |
| Crit chance | 12% |

**On hit:** On target: Kazaul exposure (magnitude 2, 3 rounds, 18% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 40% | 9 to 12 |
| [Lich dust](../items/lich_dust.md) | 10% | 1 |
| [Major potion of health](../items/health_major2.md) | 30% | 1 to 3 |
| [Kazaul bonemeal](../items/pot_bm_kazaul.md) | 5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [undertell_3_lava_01](../maps/undertell_3_lava_01.md) | – | 2 | – |
| [undertell_3_lava_10](../maps/undertell_3_lava_10.md) | – | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dreadstaff_help_plague.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dreadstaff_help_plague.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dreadstaff_help_plague.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dreadstaff_help_plague.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `dreadstaff_help_plague` |
    | Spawn group | `helpPlagueLich` |
    | Loot table | `dreadblade_lich_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_antison:2` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "dreadstaff_help_plague",
     "name": "Dreadstaff lich",
     "iconID": "monsters_antison:2",
     "maxHP": 285,
     "moveCost": 3,
     "monsterClass": "undead",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 10,
      "max": 13
     },
     "spawnGroup": "helpPlagueLich",
     "horizontalFlipChance": 50,
     "droplistID": "dreadblade_lich_dl",
     "attackCost": 4,
     "attackChance": 210,
     "criticalSkill": 15,
     "criticalMultiplier": 2.1,
     "blockChance": 185,
     "damageResistance": 11,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "kazaul_exposure",
        "magnitude": 2,
        "duration": 3,
        "chance": "18"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
