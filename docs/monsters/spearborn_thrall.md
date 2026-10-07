# ![](../assets/icons/monsters/monsters_newb_1_89.png){ .sprite } Spearborn thrall

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_1_89.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `spearborn_thrall` |
| **Type** | Enemy |
| **Class** | Humanoid |
| **HP** | 236 |
| **XP when killed** | 647 |
| **Found in** | crackshot_hideout4 |
| **Introduced** | [v0.8.13](../versions/0.8.13.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 236 |
| Damage | 12 to 13 |
| Attack chance | 175 |
| Block chance | 165 |
| Damage resistance | 8 |
| Max AP | 12 |
| Attack cost | 4 AP |
| Attacks per turn | 3 |
| Move cost | 4 AP |
| Critical skill | 10 |
| Critical multiplier | 1.5 |
| Crit chance | 9% |

**On hit:** Restore AP: 1 to 2

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Small rock](../items/rock.md) | 95% | 1 to 5 |
| [Glass gem](../items/gem1.md) | 75% | 1 to 2 |
| [Azure gem](../items/gem6.md) | 3% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [crackshot_hideout4](../maps/crackshot_hideout4.md) | – | 6 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.13](../versions/0.8.13.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spearborn_thrall.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spearborn_thrall.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spearborn_thrall.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spearborn_thrall.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `spearborn_thrall` |
    | Spawn group | `spearborn_thrall` |
    | Loot table | `molten_pyreling_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_newb_1:89` |
    | Defined in | `res/raw/monsterlist_troubling_times.json` |

    Raw data:

    ```json
    {
     "id": "spearborn_thrall",
     "name": "Spearborn thrall",
     "iconID": "monsters_newb_1:89",
     "maxHP": 236,
     "maxAP": 12,
     "moveCost": 4,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 12,
      "max": 13
     },
     "droplistID": "molten_pyreling_dl",
     "attackCost": 4,
     "attackChance": 175,
     "criticalSkill": 10,
     "criticalMultiplier": 1.5,
     "blockChance": 165,
     "damageResistance": 8,
     "hitEffect": {
      "increaseCurrentAP": {
       "min": 1,
       "max": 2
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
