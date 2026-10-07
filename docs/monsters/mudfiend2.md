---
description: "Tough mudfiend is an enemy in Andor's Trail (construct) with 41 HP, worth 93 XP, found in Loneford. Drops: Gold coins, Mundane ring, Mundane necklace, Mudfiend goo."
---

# ![](../assets/icons/monsters/monsters_ld2_133.png){ .sprite } Tough mudfiend

**Found in:** Loneford: [lodar1](../maps/lodar1.md), [lodar1cave0](../maps/lodar1cave0.md), [lodar8cave0](../maps/lodar8cave0.md), [shortcut_lodar0](../maps/shortcut_lodar0.md) (+4 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld2_133.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Loneford |
| **Class** | Construct |
| **HP** | 41 |
| **XP when defeated** | 93 |
| **Immune to critical hits** | Yes |
| **Entry ID** | `mudfiend2` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Construct |
| HP | 41 |
| XP when defeated | 93 |
| Damage | 5 to 6 |
| Attack chance | 78 |
| Block chance | 45 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 45 |
| Critical multiplier | 4.0 |
| Critical hit chance | 25% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 20% | 0 to 2 |
| [Mundane ring](../items/ring1.md) | 5% | 1 |
| [Mundane necklace](../items/junk_necklace0.md) | 5% | 1 |
| [Mudfiend goo](../items/mudfiend.md) | 20% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [lodar1](../maps/lodar1.md) | Loneford | 1 | – |
| [lodar1cave0](../maps/lodar1cave0.md) | – | 8 | – |
| [lodar8cave0](../maps/lodar8cave0.md) | – | 15 | – |
| [shortcut_lodar0](../maps/shortcut_lodar0.md) | – | 1 | – |
| [shortcut_lodar1](../maps/shortcut_lodar1.md) | – | 2 | – |
| [shortcut_lodar2](../maps/shortcut_lodar2.md) | – | 1 | – |
| [shortcut_lodar3](../maps/shortcut_lodar3.md) | – | 1 | – |
| [shortcut_lodar4](../maps/shortcut_lodar4.md) | – | 5 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | minor data change |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `mudfiend2` |
    | Spawn group | `mudfiend` |
    | Loot table | `mudfiend` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:133` |
    | Defined in | `res/raw/monsterlist_v070_lodar1cave.json` |

    Raw data:

    ```json
    {
     "id": "mudfiend2",
     "name": "Tough mudfiend",
     "iconID": "monsters_ld2:133",
     "maxHP": 41,
     "moveCost": 5,
     "monsterClass": "construct",
     "attackDamage": {
      "min": 5,
      "max": 6
     },
     "spawnGroup": "mudfiend",
     "droplistID": "mudfiend",
     "attackCost": 5,
     "attackChance": 78,
     "criticalSkill": 45,
     "criticalMultiplier": 4.0,
     "blockChance": 45
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mudfiend2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mudfiend2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mudfiend2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mudfiend2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
