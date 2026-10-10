---
description: "Cave scorpion is an enemy in Andor's Trail (insect) with 30–150 HP, worth 121–544 XP, found in Laerothcave 3, Lakecave 0, Lakecave 2, Burial cave, Buried citadel. Drops: Gold coins, Scorpion sting."
---

# ![](../assets/icons/monsters/monsters_tometik3_74.png){ .sprite } Cave scorpion

**Where to find Cave scorpion:** [Laerothcave 3 and 3 more](#v-cave_scorpion_0), [Burial cave, Brightport cave 10 and 11 more](#v-brightport_scorpion)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_tometik3_74.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Laerothcave 3, Lakecave 0, Lakecave 2, Burial cave, Buried citadel |
| **Class** | Insect |
| **HP** | 30–150 |
| **XP when defeated** | 121–544 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Laerothcave 3 and 3 more { #v-cave_scorpion_0 }

**Where:** [Laerothcave 3](../maps/laerothcave3.md), [Lakecave 0](../maps/lakecave0.md), [Lakecave 2](../maps/lakecave2.md), [Secretpassage 0](../maps/secretpassage0.md)

### Combat

| | |
|---|---|
| Class | Insect |
| HP | 30 |
| XP when defeated | 121 |
| Damage | 3 to 6 |
| AC | 80 |
| BC | 100 |
| DR | 1 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | none |

**Its hits:** On target: [Minor sting](../conditions/sting_minor.md) (magnitude 1, 3 rounds, 20% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 1 to 3 |
| [Scorpion sting](../items/scorpion_sting.md) | 20% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Laerothcave 3](../maps/laerothcave3.md) | – | 4 | – |
| [Lakecave 0](../maps/lakecave0.md) | – | 6 | – |
| [Lakecave 2](../maps/lakecave2.md) | – | 2 | – |
| [Secretpassage 0](../maps/secretpassage0.md) | – | 2 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Burial cave, Brightport cave 10 and 11 more { #v-brightport_scorpion }

**Where:** Burial cave: [Brightport cave 10](../maps/brightport_cave10.md), Burial cave: [Brightport cave 11](../maps/brightport_cave11.md), Burial cave: [Brightport cave 12](../maps/brightport_cave12.md), Burial cave: [Brightport cave 13](../maps/brightport_cave13.md), Burial cave: [Brightport cave 9](../maps/brightport_cave9.md), Buried citadel: [Brightport cave 18](../maps/brightport_cave18.md) (+6 more)

### Combat

| | |
|---|---|
| Class | Insect |
| HP | 150 |
| XP when defeated | 544 |
| Damage | 16 to 30 |
| AC | 230 |
| BC | 150 |
| DR | 4 |
| Attacks per turn | 2 (6 AP each, 12 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Brightport cave 1](../maps/brightport_cave1.md) | – | 2 | – |
| [Brightport cave 10](../maps/brightport_cave10.md) | Burial cave | 1 | – |
| [Brightport cave 11](../maps/brightport_cave11.md) | Burial cave | 2 | – |
| [Brightport cave 12](../maps/brightport_cave12.md) | Burial cave | 3 | – |
| [Brightport cave 13](../maps/brightport_cave13.md) | Burial cave | 2 | – |
| [Brightport cave 14](../maps/brightport_cave14.md) | – | 1 | – |
| [Brightport cave 15](../maps/brightport_cave15.md) | – | 2 | – |
| [Brightport cave 18](../maps/brightport_cave18.md) | Buried citadel | 2 | – |
| [Brightport cave 3](../maps/brightport_cave3.md) | Buried citadel | 3 | – |
| [Brightport cave 4](../maps/brightport_cave4.md) | Buried citadel | 1 | – |
| [Brightport cave 9](../maps/brightport_cave9.md) | Burial cave | 5 | – |
| [Brightport smugglercave 1](../maps/brightport_smugglercave1.md) | – | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Cave scorpion. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: location, combat statistics, loot or shop stock, faction, appearance, movement.

| Entry | Type | Section |
|---|---|---|
| `cave_scorpion_0` | Enemy | [Laerothcave 3 and 3 more](#v-cave_scorpion_0) |
| `brightport_scorpion` | Enemy | [Burial cave, Brightport cave 10 and 11 more](#v-brightport_scorpion) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: cave_scorpion_0"

    | | |
    |---|---|
    | Entry ID | `cave_scorpion_0` |
    | Type (wiki) | Enemy |
    | Spawn group | `scorpion_1` |
    | Loot table | `cave_scorpion` |
    | Conversation | – |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_tometik3:74` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "cave_scorpion_0",
     "name": "Cave scorpion",
     "iconID": "monsters_tometik3:74",
     "maxHP": 30,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "insect",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 3,
      "max": 6
     },
     "spawnGroup": "scorpion_1",
     "droplistID": "cave_scorpion",
     "attackCost": 3,
     "attackChance": 80,
     "blockChance": 100,
     "damageResistance": 1,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "sting_minor",
        "magnitude": 1,
        "duration": 3,
        "chance": "20"
       }
      ]
     }
    }
    ```

??? info "Technical information: brightport_scorpion"

    | | |
    |---|---|
    | Entry ID | `brightport_scorpion` |
    | Type (wiki) | Enemy |
    | Spawn group | `` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik3:76` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_scorpion",
     "name": "Cave scorpion",
     "iconID": "monsters_tometik3:76",
     "maxHP": 150,
     "maxAP": 12,
     "moveCost": 6,
     "monsterClass": "insect",
     "attackDamage": {
      "min": 16,
      "max": 30
     },
     "spawnGroup": "",
     "faction": "",
     "attackCost": 6,
     "attackChance": 230,
     "criticalSkill": 15,
     "criticalMultiplier": 1.0,
     "blockChance": 150,
     "damageResistance": 4
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cave_scorpion_0.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cave_scorpion_0.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cave_scorpion_0.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cave_scorpion_0.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
