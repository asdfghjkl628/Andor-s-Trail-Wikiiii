---
description: "Tough ash spawn is an enemy in Andor's Trail (demon) with 87 HP, worth 152 XP, found in Lostmine 5, Lostmine 6, Lostmine 7. Drops: Burnt ash, Reinforced black axe, Gem of warmth."
---

# ![](../assets/icons/monsters/monsters_tometik2_11.png){ .sprite } Tough ash spawn

**Found in:** [Lostmine 5](../maps/lostmine5.md), [Lostmine 6](../maps/lostmine6.md), [Lostmine 7](../maps/lostmine7.md), [Lostmine 9](../maps/lostmine9.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik2_11.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Lostmine 5, Lostmine 6, Lostmine 7 |
| **Class** | Demon |
| **HP** | 87 |
| **XP when defeated** | 152 |
| **Immune to critical hits** | Yes |
| **Entry ID** | `ash7` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Demon |
| HP | 87 |
| XP when defeated | 152 |
| Damage | 0 to 5 |
| Attack chance | 146 |
| Block chance | 89 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 15 |
| Critical multiplier | 4.0 |
| Critical hit chance | 12% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Burnt ash](../items/ash.md) | 10% | 0 to 2 |
| [Reinforced black axe](../items/axe_black2.md) | 5% | 1 |
| [Gem of warmth](../items/gem_fire.md) | 0.1% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Lostmine 5](../maps/lostmine5.md) | – | 1 | – |
| [Lostmine 6](../maps/lostmine6.md) | – | 5 | – |
| [Lostmine 7](../maps/lostmine7.md) | – | 3 | – |
| [Lostmine 9](../maps/lostmine9.md) | – | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Attack damage: 0–5 → 0–5 |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `ash7` |
    | Spawn group | `ash4` |
    | Loot table | `ashsp` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik2:11` |
    | Defined in | `res/raw/monsterlist_v070_charwood2.json` |

    Raw data:

    ```json
    {
     "id": "ash7",
     "name": "Tough ash spawn",
     "iconID": "monsters_tometik2:11",
     "maxHP": 87,
     "moveCost": 5,
     "monsterClass": "demon",
     "attackDamage": {
      "min": 0,
      "max": 5
     },
     "spawnGroup": "ash4",
     "droplistID": "ashsp",
     "attackCost": 3,
     "attackChance": 146,
     "criticalSkill": 15,
     "criticalMultiplier": 4.0,
     "blockChance": 89
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ash7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ash7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ash7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ash7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
