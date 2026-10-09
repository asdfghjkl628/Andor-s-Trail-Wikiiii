---
description: "Strong mountain wolf is an enemy in Andor's Trail (animal) with 73 HP, worth 159–205 XP, found in Mountainlake 10, Mountainlake 11, Waytolake 10. Drops: Gold coins, Ruby gem, Meat, Animal hair."
---

# ![](../assets/icons/monsters/monsters_dogs_4.png){ .sprite } Strong mountain wolf

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_dogs_4.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Mountainlake 10, Mountainlake 11, Waytolake 10 |
| **Class** | Animal |
| **HP** | 73 |
| **XP when defeated** | 159–205 |
| **Entries in game data** | 2 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "2 entries in the game data"
    The game data defines 2 separate characters named Strong mountain wolf. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: location, combat statistics, loot or shop stock, appearance. Each entry has its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`mwolf_7`](#v-mwolf_7) | Enemy | [Mountainlake 10](../maps/mountainlake10.md), [Mountainlake 11](../maps/mountainlake11.md) (+2 more) | – | 73 |
| [`mountain_wolf_3`](#v-mountain_wolf_3) | Enemy | Not on a map | – | 73 |

## Mountainlake 10 and 3 more (mwolf_7) { #v-mwolf_7 }

**Entry ID:** `mwolf_7` · **Type:** Enemy

**Location:** [Mountainlake 10](../maps/mountainlake10.md), [Mountainlake 11](../maps/mountainlake11.md), [Waytolake 10](../maps/waytolake10.md), [Waytolake 11](../maps/waytolake11.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 73 |
| XP when defeated | 159 |
| Damage | 3 to 9 |
| Attack chance | 90 |
| Block chance | 57 |
| Damage resistance | 6 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 10 |
| Critical multiplier | 2.0 |
| Critical hit chance | 9% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 50% | 1 to 5 |
| [Ruby gem](../items/gem2.md) | 1% | 1 |
| [Meat](../items/meat.md) | 5% | 1 |
| [Animal hair](../items/hair.md) | 30% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Mountainlake 10](../maps/mountainlake10.md) | – | 3 | – |
| [Mountainlake 11](../maps/mountainlake11.md) | – | 6 | – |
| [Waytolake 10](../maps/waytolake10.md) | – | 5 | – |
| [Waytolake 11](../maps/waytolake11.md) | – | 6 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Formatting change only (no gameplay effect) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (mwolf_7)"

    | | |
    |---|---|
    | Entry ID | `mwolf_7` |
    | Spawn group | `mwolf_3` |
    | Loot table | `mwolf` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_dogs:4` |
    | Defined in | `res/raw/monsterlist_v0611_monsters1.json` |

    Raw data:

    ```json
    {
     "id": "mwolf_7",
     "name": "Strong mountain wolf",
     "iconID": "monsters_dogs:4",
     "maxHP": 73,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 3,
      "max": 9
     },
     "spawnGroup": "mwolf_3",
     "droplistID": "mwolf",
     "attackCost": 3,
     "attackChance": 90,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 57,
     "damageResistance": 6
    }
    ```


## Not placed on a map (mountain_wolf_3) { #v-mountain_wolf_3 }

**Entry ID:** `mountain_wolf_3` · **Type:** Enemy

**Location:** not placed on any map; this entry is added to the world by a quest or scripted event.

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 73 |
| XP when defeated | 205 |
| Damage | 9 to 17 |
| Attack chance | 160 |
| Block chance | 80 |
| Damage resistance | 4 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 4 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

**On hit:** On self: [Haste](../conditions/haste.md) (magnitude 1, 2 rounds, 15% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


### Version history

| Version | Change |
|---|---|
| [v0.8.10](../versions/0.8.10.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (mountain_wolf_3)"

    | | |
    |---|---|
    | Entry ID | `mountain_wolf_3` |
    | Spawn group | `primwolf3` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:107` |
    | Defined in | `res/raw/monsterlist_bwmfill.json` |

    Raw data:

    ```json
    {
     "id": "mountain_wolf_3",
     "name": "Strong mountain wolf",
     "iconID": "monsters_rltiles2:107",
     "maxHP": 73,
     "maxAP": 10,
     "moveCost": 4,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 9,
      "max": 17
     },
     "spawnGroup": "primwolf3",
     "attackCost": 4,
     "attackChance": 160,
     "blockChance": 80,
     "damageResistance": 4,
     "hitEffect": {
      "conditionsSource": [
       {
        "condition": "haste",
        "magnitude": 1,
        "duration": 2,
        "chance": "15"
       }
      ]
     }
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mwolf_7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mwolf_7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mwolf_7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mwolf_7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
