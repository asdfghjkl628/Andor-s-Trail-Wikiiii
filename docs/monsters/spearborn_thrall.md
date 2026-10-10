---
description: "Spearborn thrall is an enemy in Andor's Trail (humanoid) with 236 HP, worth 647 XP, found in Crackshot hideout 4. Drops: Small rock, Glass gem, Azure gem."
---

# ![](../assets/icons/monsters/monsters_newb_1_89.png){ .sprite } Spearborn thrall

**Found in:** [Crackshot hideout 4](../maps/crackshot_hideout4.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_1_89.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Crackshot hideout 4 |
| **Class** | Humanoid |
| **HP** | 236 |
| **XP when defeated** | 647 |
| **Introduced** | [v0.8.13](../versions/0.8.13.md) |

</div>

## Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 236 |
| XP when defeated | 647 |
| Damage | 12 to 13 |
| AC | 175 |
| BC | 165 |
| DR | 8 |
| Attacks per turn | 3 (4 AP each, 12 AP) |
| Crit chance | 9% (×1.5) |

**Its hits:** Restore AP: 1 to 2


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Small rock](../items/rock.md) | 95% | 1 to 5 |
| [Glass gem](../items/gem1.md) | 75% | 1 to 2 |
| [Azure gem](../items/gem6.md) | 3% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Crackshot hideout 4](../maps/crackshot_hideout4.md) | – | 6 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.13](../versions/0.8.13.md) | Added |

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
    | Entry ID | `spearborn_thrall` |
    | Type (wiki) | Enemy |
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


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spearborn_thrall.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spearborn_thrall.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spearborn_thrall.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spearborn_thrall.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
