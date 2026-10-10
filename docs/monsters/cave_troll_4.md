---
description: "Cave troll shaman is an enemy in Andor's Trail (giant) with 300–370 HP, worth 365–563 XP, found in Lakecave 0, Lakecave 2, Lakecave 0. Drops: Gold coins, Helm of Foreseeing, Polished gem, Iron club."
---

# ![](../assets/icons/monsters/monsters_tometik5_17.png){ .sprite } Cave troll shaman

**Where to find Cave troll shaman:** [Lakecave 0 and 1 more](#v-cave_troll_4), [Lakecave 0](#v-cave_troll_6)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_tometik5_17.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Lakecave 0, Lakecave 2, Lakecave 0 |
| **Class** | Giant |
| **HP** | 300–370 |
| **XP when defeated** | 365–563 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Lakecave 0 and 1 more { #v-cave_troll_4 }

**Where:** [Lakecave 0](../maps/lakecave0.md), [Lakecave 2](../maps/lakecave2.md)

### Combat

| | |
|---|---|
| Class | Giant |
| HP | 300 |
| XP when defeated | 365 |
| Damage | 1 to 15 |
| AC | 60 |
| BC | 40 |
| DR | 0 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |

**Its hits:** On target: [Stunned](../conditions/stunned.md) (magnitude 1, 2 rounds, 15% chance); [Dazed](../conditions/dazed.md) (magnitude 1, 3 rounds, 10% chance); [Minor fatigue](../conditions/fatigue_minor.md) (magnitude 1, 4 rounds, 10% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 1 to 8 |
| [Helm of Foreseeing](../items/Helm_foreseeing.md) | 0.01% | 1 |
| [Polished gem](../items/gem3.md) | 5% | 1 |
| [Iron club](../items/club3.md) | 5% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Lakecave 0](../maps/lakecave0.md) | – | 4 | – |
| [Lakecave 2](../maps/lakecave2.md) | – | 6 | – |

### Quests that count defeats

- [A secret garden](../quests/secret_garden.md#stage-55) with stepping on a trigger on [Lakecave 0](../maps/lakecave0.md), stepping on a trigger on [Lakecave 2](../maps/lakecave2.md) checks that at least 7 of these enemies have been defeated.


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Lakecave 0 { #v-cave_troll_6 }

**Where:** [Lakecave 0](../maps/lakecave0.md)

### Combat

| | |
|---|---|
| Class | Giant |
| HP | 370 |
| XP when defeated | 563 |
| Damage | 7 to 18 |
| AC | 90 |
| BC | 70 |
| DR | 4 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |

**Its hits:** On target: [Stunned](../conditions/stunned.md) (magnitude 1, 2 rounds, 15% chance); [Dazed](../conditions/dazed.md) (magnitude 1, 3 rounds, 10% chance); [Minor fatigue](../conditions/fatigue_minor.md) (magnitude 1, 4 rounds, 10% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Oegyth crystal](../items/oegyth.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Lakecave 0](../maps/lakecave0.md) | – | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Cave troll shaman. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: location, combat statistics, loot or shop stock.

| Entry | Type | Section |
|---|---|---|
| `cave_troll_4` | Enemy | [Lakecave 0 and 1 more](#v-cave_troll_4) |
| `cave_troll_6` | Enemy | [Lakecave 0](#v-cave_troll_6) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: cave_troll_4"

    | | |
    |---|---|
    | Entry ID | `cave_troll_4` |
    | Type (wiki) | Enemy |
    | Spawn group | `cave_troll_4` |
    | Loot table | `cave_troll_2` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik5:17` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "cave_troll_4",
     "name": "Cave troll shaman",
     "iconID": "monsters_tometik5:17",
     "maxHP": 300,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "giant",
     "attackDamage": {
      "min": 1,
      "max": 15
     },
     "spawnGroup": "cave_troll_4",
     "droplistID": "cave_troll_2",
     "attackCost": 5,
     "attackChance": 60,
     "blockChance": 40,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "stunned",
        "magnitude": 1,
        "duration": 2,
        "chance": "15"
       },
       {
        "condition": "dazed",
        "magnitude": 1,
        "duration": 3,
        "chance": "10"
       },
       {
        "condition": "fatigue_minor",
        "magnitude": 1,
        "duration": 4,
        "chance": "10"
       }
      ]
     }
    }
    ```

??? info "Technical information: cave_troll_6"

    | | |
    |---|---|
    | Entry ID | `cave_troll_6` |
    | Type (wiki) | Enemy |
    | Spawn group | `cave_troll_6` |
    | Loot table | `cave_troll_3` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik5:17` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "cave_troll_6",
     "name": "Cave troll shaman",
     "iconID": "monsters_tometik5:17",
     "maxHP": 370,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "giant",
     "attackDamage": {
      "min": 7,
      "max": 18
     },
     "spawnGroup": "cave_troll_6",
     "droplistID": "cave_troll_3",
     "attackCost": 5,
     "attackChance": 90,
     "blockChance": 70,
     "damageResistance": 4,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "stunned",
        "magnitude": 1,
        "duration": 2,
        "chance": "15"
       },
       {
        "condition": "dazed",
        "magnitude": 1,
        "duration": 3,
        "chance": "10"
       },
       {
        "condition": "fatigue_minor",
        "magnitude": 1,
        "duration": 4,
        "chance": "10"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cave_troll_4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cave_troll_4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cave_troll_4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cave_troll_4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
