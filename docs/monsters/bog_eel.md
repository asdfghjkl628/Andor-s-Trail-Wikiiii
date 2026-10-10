---
description: "Bog eel is an enemy in Andor's Trail (reptile) with 121 HP, worth 489 XP, found in Galmore 18, Galmore 28, Galmore 38. Drops: Leech, Shimmering opal, Gold coins."
---

# ![](../assets/icons/monsters/monsters_rltiles2_25.png){ .sprite } Bog eel

**Where to find Bog eel:** [Galmore 18 and 2 more](#v-bog_eel), [Galmore 18 and 2 more](#v-bog_eel_leech)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_rltiles2_25.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Galmore 18, Galmore 28, Galmore 38 |
| **Class** | Reptile |
| **HP** | 121 |
| **XP when defeated** | 489 |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Galmore 18 and 2 more { #v-bog_eel }

**Where:** [Galmore 18](../maps/galmore_18.md), [Galmore 28](../maps/galmore_28.md), [Galmore 38](../maps/galmore_38.md)

### Combat

| | |
|---|---|
| Class | Reptile |
| HP | 121 |
| XP when defeated | 489 |
| Damage | 8 to 13 |
| AC | 191 |
| BC | 209 |
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
| [Galmore 18](../maps/galmore_18.md) | – | 2 | – |
| [Galmore 28](../maps/galmore_28.md) | – | 3 | – |
| [Galmore 38](../maps/galmore_38.md) | – | 3 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Galmore 18 and 2 more (2) { #v-bog_eel_leech }

**Where:** [Galmore 18](../maps/galmore_18.md), [Galmore 28](../maps/galmore_28.md), [Galmore 38](../maps/galmore_38.md)

### Combat

| | |
|---|---|
| Class | Reptile |
| HP | 121 |
| XP when defeated | 489 |
| Damage | 8 to 13 |
| AC | 191 |
| BC | 209 |
| DR | 9 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 11% (×2.5) |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Leech](../items/leech_usable.md) | 5% | 1 to 2 |
| [Shimmering opal](../items/gem7.md) | 3% | 1 |
| [Gold coins](../items/gold.md) | 65% | 1 to 2 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Galmore 18](../maps/galmore_18.md) | – | 2 | Appears later, during a quest |
| [Galmore 28](../maps/galmore_28.md) | – | 3 | Appears later, during a quest |
| [Galmore 38](../maps/galmore_38.md) | – | 3 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Bog eel. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: loot or shop stock.

| Entry | Type | Section |
|---|---|---|
| `bog_eel` | Enemy | [Galmore 18 and 2 more](#v-bog_eel) |
| `bog_eel_leech` | Enemy | [Galmore 18 and 2 more](#v-bog_eel_leech) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: bog_eel"

    | | |
    |---|---|
    | Entry ID | `bog_eel` |
    | Type (wiki) | Enemy |
    | Spawn group | `bog_eel` |
    | Loot table | `swamp_eel_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:25` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "bog_eel",
     "name": "Bog eel",
     "iconID": "monsters_rltiles2:25",
     "maxHP": 121,
     "moveCost": 4,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 8,
      "max": 13
     },
     "droplistID": "swamp_eel_dl",
     "attackCost": 3,
     "attackChance": 191,
     "criticalSkill": 14,
     "criticalMultiplier": 2.5,
     "blockChance": 209,
     "damageResistance": 9
    }
    ```

??? info "Technical information: bog_eel_leech"

    | | |
    |---|---|
    | Entry ID | `bog_eel_leech` |
    | Type (wiki) | Enemy |
    | Spawn group | `bog_eel_leech` |
    | Loot table | `swamp_eel_leech_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:25` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "bog_eel_leech",
     "name": "Bog eel",
     "iconID": "monsters_rltiles2:25",
     "maxHP": 121,
     "moveCost": 4,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 8,
      "max": 13
     },
     "droplistID": "swamp_eel_leech_dl",
     "attackCost": 3,
     "attackChance": 191,
     "criticalSkill": 14,
     "criticalMultiplier": 2.5,
     "blockChance": 209,
     "damageResistance": 9
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bog_eel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bog_eel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bog_eel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bog_eel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
