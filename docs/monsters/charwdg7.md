---
description: "Aggressive Charwood goblin is an enemy in Andor's Trail (humanoid) with 103 HP, worth 193 XP, found in Charwood. Drops: Gold coins, Iron mace, Broken wooden buckler, Ointment of bleeding wounds."
---

# ![](../assets/icons/monsters/monsters_rltiles4_23.png){ .sprite } Aggressive Charwood goblin

**Found in:** Charwood: [lostmine0](../maps/lostmine0.md), Charwood: [lostmine1](../maps/lostmine1.md), Charwood: [lostmine2](../maps/lostmine2.md), Charwood: [minerhouse0](../maps/minerhouse0.md) (+6 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles4_23.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Charwood |
| **Class** | Humanoid |
| **HP** | 103 |
| **XP when defeated** | 193 |
| **Entry ID** | `charwdg7` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 103 |
| XP when defeated | 193 |
| Damage | 8 to 9 |
| Attack chance | 146 |
| Block chance | 64 |
| Damage resistance | 4 |
| Max AP | 10 |
| Attack cost | 6 AP |
| Attacks per turn | 1 |
| Move cost | 5 AP |
| Critical skill | 30 |
| Critical multiplier | 3.0 |
| Critical hit chance | 19% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 30% | 1 to 20 |
| [Iron mace](../items/mace_iron.md) | 1% | 1 |
| [Broken wooden buckler](../items/broken_buckler.md) | 1% | 1 |
| [Ointment of bleeding wounds](../items/pot_bleeding_ointment.md) | 5% | 1 |
| [Raw perch](../items/rawperch.md) | 10% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [lostmine0](../maps/lostmine0.md) | Charwood | 5 | – |
| [lostmine1](../maps/lostmine1.md) | Charwood | 10 | – |
| [lostmine2](../maps/lostmine2.md) | Charwood | 5 | – |
| [lostmine2a](../maps/lostmine2a.md) | – | 5 | – |
| [minerhouse0](../maps/minerhouse0.md) | Charwood | 2 | – |
| [minerhouse1](../maps/minerhouse1.md) | Charwood | 2 | – |
| [minerhouse6](../maps/minerhouse6.md) | Charwood | 3 | – |
| [minerhouse8](../maps/minerhouse8.md) | Charwood | 3 | – |
| [waytolostmine2](../maps/waytolostmine2.md) | Charwood | 3 | – |
| [waytolostmine3](../maps/waytolostmine3.md) | Charwood | 7 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | minor data change |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `charwdg7` |
    | Spawn group | `charwdg3` |
    | Loot table | `charwdg` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles4:23` |
    | Defined in | `res/raw/monsterlist_v070_charwood.json` |

    Raw data:

    ```json
    {
     "id": "charwdg7",
     "name": "Aggressive Charwood goblin",
     "iconID": "monsters_rltiles4:23",
     "maxHP": 103,
     "moveCost": 5,
     "attackDamage": {
      "min": 8,
      "max": 9
     },
     "spawnGroup": "charwdg3",
     "droplistID": "charwdg",
     "attackCost": 6,
     "attackChance": 146,
     "criticalSkill": 30,
     "criticalMultiplier": 3.0,
     "blockChance": 64,
     "damageResistance": 4
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=charwdg7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=charwdg7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=charwdg7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=charwdg7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
