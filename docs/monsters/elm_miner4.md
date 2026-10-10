---
description: "Prim guard skeleton is an enemy in Andor's Trail (undead) with 104–364 HP, worth 399–894 XP, found in Elm 5f 1, Elm 5f 2, Elm 4f 1, Elm 5f 2. Drops: Bone, Human skull, Gold coins, Small empty vial."
---

# ![](../assets/icons/monsters/monsters_omi2_19.png){ .sprite } Prim guard skeleton

**Where to find Prim guard skeleton:** [Elm 5f 1 and 4 more](#v-elm_miner4), [Elm 5f 2](#v-elm_miner4a)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_omi2_19.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Elm 5f 1, Elm 5f 2, Elm 4f 1, Elm 5f 2 |
| **Class** | Undead |
| **HP** | 104–364 |
| **XP when defeated** | 399–894 |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

## Elm 5f 1 and 4 more { #v-elm_miner4 }

**Where:** [Elm 5f 1](../maps/elm5f_1.md), [Elm 5f 2](../maps/elm5f_2.md), [Elm 4f 1](../maps/elm_4f_1.md), [Elm 4f 3](../maps/elm_4f_3.md), [Elm 4f 4](../maps/elm_4f_4.md)

### Combat

| | |
|---|---|
| Class | Undead |
| HP | 104 |
| XP when defeated | 399 |
| Damage | 12 to 16 |
| AC | 172 |
| BC | 144 |
| DR | 7 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | 9% (×2.5) |

**Its hits:** Heal HP: 2 to 4; On target: [Bleeding wound](../conditions/bleeding_wound.md) (magnitude 5, 2 rounds, 25% chance)

**When you hit it:** On target: [Nausea](../conditions/nausea.md) (magnitude 5, 2 rounds, 25% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Bone](../items/bone.md) | 16.6667% | 1 to 3 |
| [Human skull](../items/skull1.md) | 16.6667% | 1 |
| [Gold coins](../items/gold.md) | 100% | 8 to 21 |
| [Small empty vial](../items/vial_empty1.md) | 11.1111% | 1 |
| [Small vial of mountain water](../items/bwm_water0.md) | 5% | 1 |
| [Ring of surehit](../items/ring_atkch1.md) | 2.5% | 1 |
| [Pine spear](../items/spear1.md) | 0.8% | 1 |
| [Steel cuirass](../items/cuirass_steel.md) | 0.4% | 1 |
| [Blackwater rusted pickaxe](../items/bwm_pick.md) | 0.8% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Elm 5f 1](../maps/elm5f_1.md) | – | 8 | – |
| [Elm 5f 2](../maps/elm5f_2.md) | – | 7 | – |
| [Elm 4f 1](../maps/elm_4f_1.md) | – | 2 | – |
| [Elm 4f 3](../maps/elm_4f_3.md) | – | 2 | – |
| [Elm 4f 4](../maps/elm_4f_4.md) | – | 2 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Elm 5f 2 { #v-elm_miner4a }

**Where:** [Elm 5f 2](../maps/elm5f_2.md)

### Combat

| | |
|---|---|
| Class | Undead |
| HP | 364 |
| XP when defeated | 894 |
| Damage | 12 to 16 |
| AC | 182 |
| BC | 154 |
| DR | 10 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | 9% (×2.5) |

**Its hits:** Heal HP: 2 to 4; On target: [Bleeding wound](../conditions/bleeding_wound.md) (magnitude 5, 2 rounds, 25% chance)

**When you hit it:** On target: [Nausea](../conditions/nausea.md) (magnitude 5, 2 rounds, 25% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Bone](../items/bone.md) | 100% | 1 to 2 |
| [Oegyth crystal](../items/oegyth.md) | 100% | 1 |
| [Gold coins](../items/gold.md) | 100% | 60 to 180 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Elm 5f 2](../maps/elm5f_2.md) | – | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |
| [v0.8.5](../versions/0.8.5.md) | Max HP: 104 → 364 |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Prim guard skeleton. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: location, combat statistics, loot or shop stock.

| Entry | Type | Section |
|---|---|---|
| `elm_miner4` | Enemy | [Elm 5f 1 and 4 more](#v-elm_miner4) |
| `elm_miner4a` | Enemy | [Elm 5f 2](#v-elm_miner4a) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: elm_miner4"

    | | |
    |---|---|
    | Entry ID | `elm_miner4` |
    | Type (wiki) | Enemy |
    | Spawn group | `elm_mine5` |
    | Loot table | `elm_miner2` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_omi2:19` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "elm_miner4",
     "name": "Prim guard skeleton",
     "iconID": "monsters_omi2:19",
     "maxHP": 104,
     "moveCost": 4,
     "monsterClass": "undead",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 12,
      "max": 16
     },
     "spawnGroup": "elm_mine5",
     "droplistID": "elm_miner2",
     "attackCost": 5,
     "attackChance": 172,
     "criticalSkill": 10,
     "criticalMultiplier": 2.5,
     "blockChance": 144,
     "damageResistance": 7,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 2,
       "max": 4
      },
      "conditionsTarget": [
       {
        "condition": "bleeding_wound",
        "magnitude": 5,
        "duration": 2,
        "chance": "25"
       }
      ]
     },
     "hitReceivedEffect": {
      "conditionsTarget": [
       {
        "condition": "nausea",
        "magnitude": 5,
        "duration": 2,
        "chance": "25"
       }
      ]
     },
     "deathEffect": {}
    }
    ```

??? info "Technical information: elm_miner4a"

    | | |
    |---|---|
    | Entry ID | `elm_miner4a` |
    | Type (wiki) | Enemy |
    | Spawn group | `elm_mine4a` |
    | Loot table | `elm_miner4a` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_omi2:19` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "elm_miner4a",
     "name": "Prim guard skeleton",
     "iconID": "monsters_omi2:19",
     "maxHP": 364,
     "moveCost": 4,
     "unique": 1,
     "monsterClass": "undead",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 12,
      "max": 16
     },
     "spawnGroup": "elm_mine4a",
     "droplistID": "elm_miner4a",
     "attackCost": 5,
     "attackChance": 182,
     "criticalSkill": 10,
     "criticalMultiplier": 2.5,
     "blockChance": 154,
     "damageResistance": 10,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 2,
       "max": 4
      },
      "conditionsTarget": [
       {
        "condition": "bleeding_wound",
        "magnitude": 5,
        "duration": 2,
        "chance": "25"
       }
      ]
     },
     "hitReceivedEffect": {
      "conditionsTarget": [
       {
        "condition": "nausea",
        "magnitude": 5,
        "duration": 2,
        "chance": "25"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_miner4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_miner4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_miner4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_miner4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
