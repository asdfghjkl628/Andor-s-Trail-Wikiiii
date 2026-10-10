---
description: "Kazaul Hex-Binder lich is an enemy in Andor's Trail (undead) with 263 HP, worth 760 XP, found in Undertell 3 lava 10, Undertell 3 lava 11, Undertell 4 10, Undertell 3 lava 00. Drops: Gold coins, Lich dust, Major potion of health, Liquid courage."
---

# ![](../assets/icons/monsters/monsters_antison_4.png){ .sprite } Kazaul Hex-Binder lich

**Where to find Kazaul Hex-Binder lich:** [Undertell 3 lava 10 and 3 more](#v-hexbinder), [Undertell 3 lava 00](#v-hexbinder_help_liches)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_antison_4.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Undertell 3 lava 10, Undertell 3 lava 11, Undertell 4 10, Undertell 3 lava 00 |
| **Class** | Undead |
| **HP** | 263 |
| **XP when defeated** | 760 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Undertell 3 lava 10 and 3 more { #v-hexbinder }

**Where:** [Undertell 3 lava 10](../maps/undertell_3_lava_10.md), [Undertell 3 lava 11](../maps/undertell_3_lava_11.md), [Undertell 4 10](../maps/undertell_4_10.md), [Undertell 5](../maps/undertell_5.md)

### Combat

| | |
|---|---|
| Class | Undead |
| HP | 263 |
| XP when defeated | 760 |
| Damage | 8 to 10 |
| AC | 198 |
| BC | 180 |
| DR | 9 |
| Attacks per turn | 3 (4 AP each, 12 AP) |
| Crit chance | 9% (×2.0) |

**Its hits:** On target: [Withering Focus](../conditions/withering_focus.md) (magnitude 4, 3 rounds, 28% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 40% | 7 to 12 |
| [Lich dust](../items/lich_dust.md) | 9% | 1 |
| [Major potion of health](../items/health_major2.md) | 30% | 1 to 2 |
| [Liquid courage](../items/pot_courage.md) | 10% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Undertell 3 lava 10](../maps/undertell_3_lava_10.md) | – | 5 | – |
| [Undertell 3 lava 11](../maps/undertell_3_lava_11.md) | – | 3 | – |
| [Undertell 4 10](../maps/undertell_4_10.md) | – | 1 | – |
| [Undertell 5](../maps/undertell_5.md) | – | 4 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Undertell 3 lava 00 { #v-hexbinder_help_liches }

**Where:** [Undertell 3 lava 00](../maps/undertell_3_lava_00.md)

### Combat

| | |
|---|---|
| Class | Undead |
| HP | 263 |
| XP when defeated | 760 |
| Damage | 8 to 10 |
| AC | 198 |
| BC | 180 |
| DR | 9 |
| Attacks per turn | 3 (4 AP each, 12 AP) |
| Crit chance | 9% (×2.0) |

**Its hits:** On target: [Withering Focus](../conditions/withering_focus.md) (magnitude 4, 3 rounds, 28% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 40% | 7 to 12 |
| [Lich dust](../items/lich_dust.md) | 9% | 1 |
| [Major potion of health](../items/health_major2.md) | 30% | 1 to 2 |
| [Liquid courage](../items/pot_courage.md) | 10% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Undertell 3 lava 00](../maps/undertell_3_lava_00.md) | – | 2 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Kazaul Hex-Binder lich. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: location, movement.

| Entry | Type | Section |
|---|---|---|
| `hexbinder` | Enemy | [Undertell 3 lava 10 and 3 more](#v-hexbinder) |
| `hexbinder_help_liches` | Enemy | [Undertell 3 lava 00](#v-hexbinder_help_liches) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: hexbinder"

    | | |
    |---|---|
    | Entry ID | `hexbinder` |
    | Type (wiki) | Enemy |
    | Spawn group | `hexbinder` |
    | Loot table | `hexbinder_lich_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_antison:4` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "hexbinder",
     "name": "Kazaul Hex-Binder lich",
     "iconID": "monsters_antison:4",
     "maxHP": 263,
     "maxAP": 12,
     "moveCost": 4,
     "monsterClass": "undead",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 8,
      "max": 10
     },
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

??? info "Technical information: hexbinder_help_liches"

    | | |
    |---|---|
    | Entry ID | `hexbinder_help_liches` |
    | Type (wiki) | Enemy |
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


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hexbinder.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hexbinder.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hexbinder.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hexbinder.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
