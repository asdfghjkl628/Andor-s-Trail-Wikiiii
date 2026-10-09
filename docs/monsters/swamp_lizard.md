---
description: "Swamp lizard is an enemy in Andor's Trail (reptile) with 130 HP, worth 511 XP, found in Galmore 18, Galmore 28, Galmore 38. Drops: Leech, Shimmering opal, Gold coins, Lizard skin."
---

# ![](../assets/icons/monsters/monsters_newb_1_373.png){ .sprite } Swamp lizard

**Where to find Swamp lizard:** [Galmore 18 and 2 more](#v-swamp_lizard), [Galmore 18 and 2 more](#v-swamp_lizard_leech)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_1_373.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Galmore 18, Galmore 28, Galmore 38 |
| **Class** | Reptile |
| **HP** | 130 |
| **XP when defeated** | 511 |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Galmore 18 and 2 more { #v-swamp_lizard }

**Where:** [Galmore 18](../maps/galmore_18.md), [Galmore 28](../maps/galmore_28.md), [Galmore 38](../maps/galmore_38.md)

### Combat

| | |
|---|---|
| Class | Reptile |
| HP | 130 |
| XP when defeated | 511 |
| Damage | 10 to 15 |
| AC | 191 |
| BC | 176 |
| DR | 9 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 11% (×2.5) |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Leech](../items/leech.md) | 8% | 1 to 2 |
| [Shimmering opal](../items/gem7.md) | 3% | 1 |
| [Gold coins](../items/gold.md) | 65% | 1 to 2 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Galmore 18](../maps/galmore_18.md) | – | 3 | – |
| [Galmore 28](../maps/galmore_28.md) | – | 4 | – |
| [Galmore 38](../maps/galmore_38.md) | – | 3 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Galmore 18 and 2 more (2) { #v-swamp_lizard_leech }

**Where:** [Galmore 18](../maps/galmore_18.md), [Galmore 28](../maps/galmore_28.md), [Galmore 38](../maps/galmore_38.md)

### Combat

| | |
|---|---|
| Class | Reptile |
| HP | 130 |
| XP when defeated | 511 |
| Damage | 10 to 15 |
| AC | 191 |
| BC | 176 |
| DR | 9 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 11% (×2.5) |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Leech](../items/leech_usable.md) | 5% | 1 to 2 |
| [Lizard skin](../items/lizard_skin.md) | 30% | 1 |
| [Shimmering opal](../items/gem7.md) | 3% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Galmore 18](../maps/galmore_18.md) | – | 3 | Appears later, during a quest |
| [Galmore 28](../maps/galmore_28.md) | – | 4 | Appears later, during a quest |
| [Galmore 38](../maps/galmore_38.md) | – | 3 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Swamp lizard. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: loot or shop stock.

| Entry | Type | Section |
|---|---|---|
| `swamp_lizard` | Enemy | [Galmore 18 and 2 more](#v-swamp_lizard) |
| `swamp_lizard_leech` | Enemy | [Galmore 18 and 2 more](#v-swamp_lizard_leech) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: swamp_lizard"

    | | |
    |---|---|
    | Entry ID | `swamp_lizard` |
    | Type (wiki) | Enemy |
    | Spawn group | `swamp_lizard` |
    | Loot table | `swamp_eel_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_newb_1:373` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "swamp_lizard",
     "name": "Swamp lizard",
     "iconID": "monsters_newb_1:373",
     "maxHP": 130,
     "moveCost": 4,
     "monsterClass": "reptile",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 10,
      "max": 15
     },
     "droplistID": "swamp_eel_dl",
     "attackCost": 3,
     "attackChance": 191,
     "criticalSkill": 14,
     "criticalMultiplier": 2.5,
     "blockChance": 176,
     "damageResistance": 9
    }
    ```

??? info "Technical information: swamp_lizard_leech"

    | | |
    |---|---|
    | Entry ID | `swamp_lizard_leech` |
    | Type (wiki) | Enemy |
    | Spawn group | `swamp_lizard_leech` |
    | Loot table | `swamp_lizard_leetch_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_newb_1:373` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "swamp_lizard_leech",
     "name": "Swamp lizard",
     "iconID": "monsters_newb_1:373",
     "maxHP": 130,
     "moveCost": 4,
     "monsterClass": "reptile",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 10,
      "max": 15
     },
     "droplistID": "swamp_lizard_leetch_dl",
     "attackCost": 3,
     "attackChance": 191,
     "criticalSkill": 14,
     "criticalMultiplier": 2.5,
     "blockChance": 176,
     "damageResistance": 9
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=swamp_lizard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=swamp_lizard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=swamp_lizard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=swamp_lizard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
