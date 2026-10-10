---
description: "Restless dead is an enemy in Andor's Trail (ghost) with 25 HP, worth 70 XP, found in Prim, Blackwater Mountain, Blackwater Mountain. Drops: Gold coins, Polished gem, Minor vial of health, Bone."
---

# ![](../assets/icons/monsters/monsters_rltiles1_47.png){ .sprite } Restless dead

**Where to find Restless dead:** [Blackwater Mountain, Blackwater mountain 51 and 4 more](#v-restless_dead), [Blackwater Mountain, Blackwater mountain 72](#v-bwm_dead)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_rltiles1_47.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Prim, Blackwater Mountain, Blackwater Mountain |
| **Class** | Ghost |
| **HP** | 25 |
| **XP when defeated** | 70 |
| **Immune to crits** | Yes |
| **Introduced** | v0.7.0 or earlier |

</div>

## Blackwater Mountain, Blackwater mountain 51 and 4 more { #v-restless_dead }

**Where:** Blackwater Mountain: [Blackwater mountain 51](../maps/blackwater_mountain51.md), Blackwater Mountain: [Blackwater mountain 52](../maps/blackwater_mountain52.md), Prim: [Blackwater mountain 12](../maps/blackwater_mountain12.md), Prim: [Blackwater mountain 33](../maps/blackwater_mountain33.md), [Blackwater mountain 34](../maps/blackwater_mountain34.md)

### Combat

| | |
|---|---|
| Class | Ghost |
| HP | 25 |
| XP when defeated | 70 |
| Damage | 0 to 3 |
| AC | 50 |
| BC | 140 |
| DR | 3 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | 35% (×2.0) |

**Immune to critical hits.**


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 20 to 29 |
| [Polished gem](../items/gem3.md) | 10% | 1 |
| [Minor vial of health](../items/health_minor.md) | 10% | 1 |
| [Bone](../items/bone.md) | 10% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Blackwater mountain 12](../maps/blackwater_mountain12.md) | Prim | 1 | – |
| [Blackwater mountain 33](../maps/blackwater_mountain33.md) | Prim | 7 | – |
| [Blackwater mountain 34](../maps/blackwater_mountain34.md) | – | 4 | – |
| [Blackwater mountain 51](../maps/blackwater_mountain51.md) | Blackwater Mountain | 2 | – |
| [Blackwater mountain 52](../maps/blackwater_mountain52.md) | Blackwater Mountain | 4 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Formatting change only (no gameplay effect) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Blackwater Mountain, Blackwater mountain 72 { #v-bwm_dead }

**Where:** Blackwater Mountain: [Blackwater mountain 72](../maps/blackwater_mountain72.md)

### Combat

| | |
|---|---|
| Class | Ghost |
| HP | 25 |
| XP when defeated | 70 |
| Damage | 0 to 3 |
| AC | 50 |
| BC | 140 |
| DR | 3 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | 35% (×2.0) |

**Immune to critical hits.**


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 20 to 29 |
| [Polished gem](../items/gem3.md) | 10% | 1 |
| [Minor vial of health](../items/health_minor.md) | 10% | 1 |
| [Bone](../items/bone.md) | 10% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Blackwater mountain 72](../maps/blackwater_mountain72.md) | Blackwater Mountain | 2 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Restless dead. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: location, movement.

| Entry | Type | Section |
|---|---|---|
| `restless_dead` | Enemy | [Blackwater Mountain, Blackwater mountain 51 and 4 more](#v-restless_dead) |
| `bwm_dead` | Enemy | [Blackwater Mountain, Blackwater mountain 72](#v-bwm_dead) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: restless_dead"

    | | |
    |---|---|
    | Entry ID | `restless_dead` |
    | Type (wiki) | Enemy |
    | Spawn group | `restless_dead_1` |
    | Loot table | `restless_dead_1` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:47` |
    | Defined in | `res/raw/monsterlist_v069_monsters.json` |

    Raw data:

    ```json
    {
     "id": "restless_dead",
     "name": "Restless dead",
     "iconID": "monsters_rltiles1:47",
     "maxHP": 25,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "ghost",
     "attackDamage": {
      "min": 0,
      "max": 3
     },
     "spawnGroup": "restless_dead_1",
     "droplistID": "restless_dead_1",
     "attackCost": 5,
     "attackChance": 50,
     "criticalSkill": 80,
     "criticalMultiplier": 2.0,
     "blockChance": 140,
     "damageResistance": 3
    }
    ```

??? info "Technical information: bwm_dead"

    | | |
    |---|---|
    | Entry ID | `bwm_dead` |
    | Type (wiki) | Enemy |
    | Spawn group | `bwm_dead` |
    | Loot table | `restless_dead_1` |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_rltiles1:47` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "bwm_dead",
     "name": "Restless dead",
     "iconID": "monsters_rltiles1:47",
     "maxHP": 25,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "ghost",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 0,
      "max": 3
     },
     "spawnGroup": "bwm_dead",
     "droplistID": "restless_dead_1",
     "attackCost": 5,
     "attackChance": 50,
     "criticalSkill": 80,
     "criticalMultiplier": 2.0,
     "blockChance": 140,
     "damageResistance": 3
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=restless_dead.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=restless_dead.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=restless_dead.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=restless_dead.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
