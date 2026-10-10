---
description: "River wretch is an enemy in Andor's Trail (humanoid) with 201 HP, worth 561–611 XP, found in Mt. Galmore. Drops: Bramblefin, Mountain eel meat, Gold coins."
---

# ![](../assets/icons/monsters/monsters_ld2_150.png){ .sprite } River wretch

**Where to find River wretch:** [Mt. Galmore, Galmore 46 and 4 more](#v-river_wretch), [Mt. Galmore, Galmore 56 and 3 more](#v-river_wretch2)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld2_150.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Mt. Galmore |
| **Class** | Humanoid |
| **HP** | 201 |
| **XP when defeated** | 561–611 |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Mt. Galmore, Galmore 46 and 4 more { #v-river_wretch }

**Where:** Mt. Galmore: [Galmore 46](../maps/galmore_46.md), Mt. Galmore: [Galmore 55](../maps/galmore_55.md), Mt. Galmore: [Galmore 56](../maps/galmore_56.md), Mt. Galmore: [Galmore 65](../maps/galmore_65.md), Mt. Galmore: [Galmore 66](../maps/galmore_66.md)

### Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 201 |
| XP when defeated | 611 |
| Damage | 9 to 13 |
| AC | 199 |
| BC | 176 |
| DR | 9 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | 11% (×2.0) |

**Its hits:** On target: [Soaked vision](../conditions/soaked_vision.md) (magnitude 1, 3 rounds, 8% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Bramblefin](../items/bramblefin_fish.md) | 10% | 1 to 2 |
| [Mountain eel meat](../items/eel_meat.md) | 8% | 1 |
| [Gold coins](../items/gold.md) | 30% | 5 to 6 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Galmore 46](../maps/galmore_46.md) | Mt. Galmore | 1 | – |
| [Galmore 55](../maps/galmore_55.md) | Mt. Galmore | 1 | – |
| [Galmore 56](../maps/galmore_56.md) | Mt. Galmore | 4 | – |
| [Galmore 65](../maps/galmore_65.md) | Mt. Galmore | 1 | – |
| [Galmore 66](../maps/galmore_66.md) | Mt. Galmore | 4 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Mt. Galmore, Galmore 56 and 3 more { #v-river_wretch2 }

**Where:** Mt. Galmore: [Galmore 56](../maps/galmore_56.md), Mt. Galmore: [Galmore 65](../maps/galmore_65.md), Mt. Galmore: [Galmore 66](../maps/galmore_66.md), Mt. Galmore: [Galmore 76](../maps/galmore_76.md)

### Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 201 |
| XP when defeated | 561 |
| Damage | 9 to 13 |
| AC | 199 |
| BC | 176 |
| DR | 9 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | 11% (×2.0) |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Bramblefin](../items/bramblefin_fish.md) | 10% | 1 to 2 |
| [Mountain eel meat](../items/eel_meat.md) | 8% | 1 |
| [Gold coins](../items/gold.md) | 30% | 5 to 6 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Galmore 56](../maps/galmore_56.md) | Mt. Galmore | 8 | – |
| [Galmore 65](../maps/galmore_65.md) | Mt. Galmore | 1 | – |
| [Galmore 66](../maps/galmore_66.md) | Mt. Galmore | 2 | – |
| [Galmore 76](../maps/galmore_76.md) | Mt. Galmore | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named River wretch. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: location, appearance, movement.

| Entry | Type | Section |
|---|---|---|
| `river_wretch` | Enemy | [Mt. Galmore, Galmore 46 and 4 more](#v-river_wretch) |
| `river_wretch2` | Enemy | [Mt. Galmore, Galmore 56 and 3 more](#v-river_wretch2) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: river_wretch"

    | | |
    |---|---|
    | Entry ID | `river_wretch` |
    | Type (wiki) | Enemy |
    | Spawn group | `river_wretch` |
    | Loot table | `river_wretch_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_ld2:150` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "river_wretch",
     "name": "River wretch",
     "iconID": "monsters_ld2:150",
     "maxHP": 201,
     "moveCost": 3,
     "monsterClass": "humanoid",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 9,
      "max": 13
     },
     "droplistID": "river_wretch_dl",
     "attackCost": 4,
     "attackChance": 199,
     "criticalSkill": 13,
     "criticalMultiplier": 2.0,
     "blockChance": 176,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "soaked_vision",
        "magnitude": 1,
        "duration": 3,
        "chance": "8"
       }
      ]
     }
    }
    ```

??? info "Technical information: river_wretch2"

    | | |
    |---|---|
    | Entry ID | `river_wretch2` |
    | Type (wiki) | Enemy |
    | Spawn group | `river_wretch2` |
    | Loot table | `river_wretch_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:110` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "river_wretch2",
     "name": "River wretch",
     "iconID": "monsters_ld2:110",
     "maxHP": 201,
     "moveCost": 3,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 9,
      "max": 13
     },
     "droplistID": "river_wretch_dl",
     "attackCost": 4,
     "attackChance": 199,
     "criticalSkill": 13,
     "criticalMultiplier": 2.0,
     "blockChance": 176,
     "damageResistance": 9
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=river_wretch.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=river_wretch.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=river_wretch.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=river_wretch.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
