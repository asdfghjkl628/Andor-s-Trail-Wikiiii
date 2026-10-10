---
description: "Izthiel guardian is an enemy in Andor's Trail (reptile) with 54–354 HP, worth 218–554 XP, found in Brimhaven, Waterway 10. Drops: Gold coins, Izthiel claw, Jinxed ring of damage resistance, Polished ring."
---

# ![](../assets/icons/monsters/monsters_rltiles2_52.png){ .sprite } Izthiel guardian

**Where to find Izthiel guardian:** [Brimhaven, Waterway 6 and 6 more](#v-izthiel_4), [Waterway 10](#v-izthiel_cr)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_52.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Brimhaven, Waterway 10 |
| **Class** | Reptile |
| **HP** | 54–354 |
| **XP when defeated** | 218–554 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Brimhaven, Waterway 6 and 6 more { #v-izthiel_4 }

**Where:** Brimhaven: [Waterway 6](../maps/waterway6.md), [Waterway 1](../maps/waterway1.md), [Waterway 4](../maps/waterway4.md), [Waterway 5](../maps/waterway5.md), [Waterway 8](../maps/waterway8.md), [Waterway 9](../maps/waterway9.md) (+1 more)

### Combat

| | |
|---|---|
| Class | Reptile |
| HP | 54 |
| XP when defeated | 218 |
| Damage | 3 to 7 |
| AC | 120 |
| BC | 60 |
| DR | 11 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | none |

**Its hits:** On target: [Bleeding wound](../conditions/bleeding_wound.md) (magnitude 3, 5 rounds, 50% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 3 to 40 |
| [Izthiel claw](../items/izthiel_claw.md) | 30% | 1 |
| [Jinxed ring of damage resistance](../items/ring_jinxed1.md) | 1% | 1 |
| [Polished ring](../items/ring2.md) | 20% | 1 |
| [Shadowfang](../items/shadowfang.md) | 0.1% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Waterway 1](../maps/waterway1.md) | – | 1 | – |
| [Waterway 4](../maps/waterway4.md) | – | 2 | – |
| [Waterway 5](../maps/waterway5.md) | – | 4 | – |
| [Waterway 6](../maps/waterway6.md) | Brimhaven | 2 | – |
| [Waterway 8](../maps/waterway8.md) | – | 2 | – |
| [Waterway 9](../maps/waterway9.md) | – | 3 | – |
| [Waterwayextention](../maps/waterwayextention.md) | – | 2 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Bleeding wound](../conditions/bleeding_wound.md) (magnitude 3, 5 rounds, 50% chance) → (magnitude 3, 5 rounds, 50% chance)<br>Renamed “Izthiel Guardian” → “Izthiel guardian” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Waterway 10 { #v-izthiel_cr }

**Where:** [Waterway 10](../maps/waterway10.md)

### Combat

| | |
|---|---|
| Class | Reptile |
| HP | 354 |
| XP when defeated | 554 |
| Damage | 3 to 7 |
| AC | 120 |
| BC | 60 |
| DR | 11 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | none |

**Its hits:** On target: [Bleeding wound](../conditions/bleeding_wound.md) (magnitude 3, 5 rounds, 50% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Oegyth crystal](../items/oegyth.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Waterway 10](../maps/waterway10.md) | – | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Bleeding wound](../conditions/bleeding_wound.md) (magnitude 3, 5 rounds, 50% chance) → (magnitude 3, 5 rounds, 50% chance)<br>Renamed “Izthiel Guardian” → “Izthiel guardian” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Izthiel guardian. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: location, combat statistics, loot or shop stock.

| Entry | Type | Section |
|---|---|---|
| `izthiel_4` | Enemy | [Brimhaven, Waterway 6 and 6 more](#v-izthiel_4) |
| `izthiel_cr` | Enemy | [Waterway 10](#v-izthiel_cr) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: izthiel_4"

    | | |
    |---|---|
    | Entry ID | `izthiel_4` |
    | Type (wiki) | Enemy |
    | Spawn group | `izthiel_4` |
    | Loot table | `izthiel_4` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:52` |
    | Defined in | `res/raw/monsterlist_v0610_monsters1.json` |

    Raw data:

    ```json
    {
     "id": "izthiel_4",
     "name": "Izthiel guardian",
     "iconID": "monsters_rltiles2:52",
     "maxHP": 54,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 3,
      "max": 7
     },
     "spawnGroup": "izthiel_4",
     "droplistID": "izthiel_4",
     "attackCost": 3,
     "attackChance": 120,
     "blockChance": 60,
     "damageResistance": 11,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "bleeding_wound",
        "magnitude": 3,
        "duration": 5,
        "chance": "50"
       }
      ]
     }
    }
    ```

??? info "Technical information: izthiel_cr"

    | | |
    |---|---|
    | Entry ID | `izthiel_cr` |
    | Type (wiki) | Enemy |
    | Spawn group | `izthiel_cr` |
    | Loot table | `oegyth1` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:52` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "izthiel_cr",
     "name": "Izthiel guardian",
     "iconID": "monsters_rltiles2:52",
     "maxHP": 354,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 3,
      "max": 7
     },
     "spawnGroup": "izthiel_cr",
     "droplistID": "oegyth1",
     "attackCost": 3,
     "attackChance": 120,
     "blockChance": 60,
     "damageResistance": 11,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "bleeding_wound",
        "magnitude": 3,
        "duration": 5,
        "chance": "50"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=izthiel_4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=izthiel_4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=izthiel_4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=izthiel_4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
