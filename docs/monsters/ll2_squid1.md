---
description: "Squid is an enemy in Andor's Trail (animal) with 1 HP, worth 1 XP, found in Remgard, Lake Laeroth."
---

# ![](../assets/icons/monsters/monsters_nut_2.png){ .sprite } Squid

**Found in:** Lake Laeroth: [Mountainlake 2](../maps/mountainlake2.md), Lake Laeroth: [Mountainlake 21](../maps/mountainlake21.md), Lake Laeroth: [Mountainlake 31](../maps/mountainlake31.md), Lake Laeroth: [Mountainlake 36](../maps/mountainlake36.md) (+17 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_nut_2.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Remgard, Lake Laeroth |
| **Class** | Animal |
| **HP** | 1 |
| **XP when defeated** | 1 |
| **Entry ID** | `ll2_squid1` |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 1 |
| XP when defeated | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Mountainlake 13a](../maps/mountainlake13a.md) | Remgard | 3 | – |
| [Mountainlake 14](../maps/mountainlake14.md) | Remgard | 7 | – |
| [Mountainlake 15](../maps/mountainlake15.md) | Remgard | 8 | – |
| [Mountainlake 16](../maps/mountainlake16.md) | Remgard | 6 | – |
| [Mountainlake 17](../maps/mountainlake17.md) | Remgard | 6 | – |
| [Mountainlake 18](../maps/mountainlake18.md) | Remgard | 3 | – |
| [Mountainlake 19](../maps/mountainlake19.md) | – | 5 | – |
| [Mountainlake 2](../maps/mountainlake2.md) | Lake Laeroth | 3 | – |
| [Mountainlake 20](../maps/mountainlake20.md) | Remgard | 6 | – |
| [Mountainlake 21](../maps/mountainlake21.md) | Lake Laeroth | 5 | – |
| [Mountainlake 22](../maps/mountainlake22.md) | – | 4 | – |
| [Mountainlake 25](../maps/mountainlake25.md) | – | 3 | – |
| [Mountainlake 26](../maps/mountainlake26.md) | – | 4 | – |
| [Mountainlake 28](../maps/mountainlake28.md) | – | 4 | – |
| [Mountainlake 29](../maps/mountainlake29.md) | – | 5 | – |
| [Mountainlake 31](../maps/mountainlake31.md) | Lake Laeroth | 3 | – |
| [Mountainlake 34](../maps/mountainlake34.md) | – | 5 | – |
| [Mountainlake 35](../maps/mountainlake35.md) | – | 2 | – |
| [Mountainlake 36](../maps/mountainlake36.md) | Lake Laeroth | 3 | – |
| [Mountainlake 37](../maps/mountainlake37.md) | Lake Laeroth | 3 | – |
| [Remgard 1](../maps/remgard1.md) | Remgard | 4 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `ll2_squid1` |
    | Spawn group | `ll2_sealife` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_nut:2` |
    | Defined in | `res/raw/monsterlist_lake_laeroth_2.json` |

    Raw data:

    ```json
    {
     "id": "ll2_squid1",
     "name": "Squid",
     "iconID": "monsters_nut:2",
     "monsterClass": "animal",
     "spawnGroup": "ll2_sealife",
     "horizontalFlipChance": 50
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ll2_squid1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ll2_squid1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ll2_squid1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ll2_squid1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
