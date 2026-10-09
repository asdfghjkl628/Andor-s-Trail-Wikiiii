---
description: "Tough Charwood goblin is an enemy in Andor's Trail (humanoid) with 92 HP, worth 178 XP, found in Charwood. Drops: Gold coins, Iron mace, Broken wooden buckler, Ointment of bleeding wounds."
---

# ![](../assets/icons/monsters/monsters_rltiles4_21.png){ .sprite } Tough Charwood goblin

**Found in:** Charwood: [Lostmine 0](../maps/lostmine0.md), Charwood: [Lostmine 1](../maps/lostmine1.md), Charwood: [Lostmine 1a](../maps/lostmine1a.md), Charwood: [Lostmine 2](../maps/lostmine2.md) (+11 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles4_21.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Charwood |
| **Class** | Humanoid |
| **HP** | 92 |
| **XP when defeated** | 178 |
| **Entry ID** | `charwdg6` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 92 |
| XP when defeated | 178 |
| Damage | 8 to 9 |
| Attack chance | 143 |
| Block chance | 67 |
| Damage resistance | 4 |
| Max AP | 10 |
| Attack cost | 6 AP |
| Attacks per turn | 1 |
| Move cost | 5 AP |
| Critical skill | 25 |
| Critical multiplier | 3.0 |
| Critical hit chance | 17% |


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
| [Lostmine 0](../maps/lostmine0.md) | Charwood | 8 | – |
| [Lostmine 1](../maps/lostmine1.md) | Charwood | 4 | – |
| [Lostmine 1a](../maps/lostmine1a.md) | Charwood | 2 | – |
| [Lostmine 2](../maps/lostmine2.md) | Charwood | 3 | – |
| [Lostmine 2a](../maps/lostmine2a.md) | – | 1 | – |
| [Minerhouse 0](../maps/minerhouse0.md) | Charwood | 3 | – |
| [Minerhouse 1](../maps/minerhouse1.md) | Charwood | 2 | – |
| [Minerhouse 2](../maps/minerhouse2.md) | Charwood | 4 | – |
| [Minerhouse 3](../maps/minerhouse3.md) | Charwood | 6 | – |
| [Minerhouse 7](../maps/minerhouse7.md) | Charwood | 5 | – |
| [Minerhouse 8](../maps/minerhouse8.md) | Charwood | 1 | – |
| [Minerhouse 9](../maps/minerhouse9.md) | Charwood | 2 | – |
| [Waytolostmine 1](../maps/waytolostmine1.md) | Charwood | 8 | – |
| [Waytolostmine 2](../maps/waytolostmine2.md) | Charwood | 12 | – |
| [Waytolostmine 3](../maps/waytolostmine3.md) | Charwood | 19 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Formatting change only (no gameplay effect) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `charwdg6` |
    | Spawn group | `charwdg2` |
    | Loot table | `charwdg` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles4:21` |
    | Defined in | `res/raw/monsterlist_v070_charwood.json` |

    Raw data:

    ```json
    {
     "id": "charwdg6",
     "name": "Tough Charwood goblin",
     "iconID": "monsters_rltiles4:21",
     "maxHP": 92,
     "moveCost": 5,
     "attackDamage": {
      "min": 8,
      "max": 9
     },
     "spawnGroup": "charwdg2",
     "droplistID": "charwdg",
     "attackCost": 6,
     "attackChance": 143,
     "criticalSkill": 25,
     "criticalMultiplier": 3.0,
     "blockChance": 67,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=charwdg6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=charwdg6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=charwdg6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=charwdg6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
