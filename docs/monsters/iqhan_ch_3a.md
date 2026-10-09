---
description: "Iqhan chaos master is an enemy in Andor's Trail (humanoid) with 83–85 HP, worth 273–275 XP, found in Pwcave 2a, Pwcave 3, Pwcave 4. Drops: Gold coins, Iqhan pendant, Crude cloth gloves, Iron dagger."
---

# ![](../assets/icons/monsters/monsters_rltiles2_136.png){ .sprite } Iqhan chaos master

**Where to find Iqhan chaos master:** [Pwcave 2a and 2 more](#v-iqhan_ch_3a), [Pwcave 2a and 2 more](#v-iqhan_ch_3b)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_136.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Pwcave 2a, Pwcave 3, Pwcave 4 |
| **Class** | Humanoid |
| **HP** | 83–85 |
| **XP when defeated** | 273–275 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Pwcave 2a and 2 more { #v-iqhan_ch_3a }

**Where:** [Pwcave 2a](../maps/pwcave2a.md), [Pwcave 3](../maps/pwcave3.md), [Pwcave 4](../maps/pwcave4.md)

### Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 83 |
| XP when defeated | 273 |
| Damage | 2 to 13 |
| AC | 170 |
| BC | 75 |
| DR | 0 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 17% (×2.0) |

**Its hits:** On target: [Chaotic grip](../conditions/chaotic_grip.md) (magnitude 4, 5 rounds, 50% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 1 to 9 |
| [Iqhan pendant](../items/iqhan_pendant.md) | 5% | 1 |
| [Crude cloth gloves](../items/gloves_crude_cloth.md) | 5% | 1 |
| [Iron dagger](../items/dagger0.md) | 5% | 1 |
| [Regular potion of health](../items/health.md) | 5% | 1 to 3 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Pwcave 2a](../maps/pwcave2a.md) | – | 1 | – |
| [Pwcave 3](../maps/pwcave3.md) | – | 2 | – |
| [Pwcave 4](../maps/pwcave4.md) | – | 10 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Chaotic grip](../conditions/chaotic_grip.md) (magnitude 4, 5 rounds, 50% chance) → (magnitude 4, 5 rounds, 50% chance) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Pwcave 2a and 2 more (2) { #v-iqhan_ch_3b }

**Where:** [Pwcave 2a](../maps/pwcave2a.md), [Pwcave 3](../maps/pwcave3.md), [Pwcave 4](../maps/pwcave4.md)

### Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 85 |
| XP when defeated | 275 |
| Damage | 2 to 13 |
| AC | 170 |
| BC | 75 |
| DR | 0 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 17% (×2.0) |

**Its hits:** On target: [Chaotic grip](../conditions/chaotic_grip.md) (magnitude 4, 5 rounds, 50% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 1 to 9 |
| [Iqhan pendant](../items/iqhan_pendant.md) | 5% | 1 |
| [Crude cloth gloves](../items/gloves_crude_cloth.md) | 5% | 1 |
| [Iron dagger](../items/dagger0.md) | 5% | 1 |
| [Regular potion of health](../items/health.md) | 5% | 1 to 3 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Pwcave 2a](../maps/pwcave2a.md) | – | 1 | – |
| [Pwcave 3](../maps/pwcave3.md) | – | 2 | – |
| [Pwcave 4](../maps/pwcave4.md) | – | 10 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Chaotic grip](../conditions/chaotic_grip.md) (magnitude 4, 5 rounds, 50% chance) → (magnitude 4, 5 rounds, 50% chance) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Iqhan chaos master. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: combat statistics, appearance.

| Entry | Type | Section |
|---|---|---|
| `iqhan_ch_3a` | Enemy | [Pwcave 2a and 2 more](#v-iqhan_ch_3a) |
| `iqhan_ch_3b` | Enemy | [Pwcave 2a and 2 more](#v-iqhan_ch_3b) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: iqhan_ch_3a"

    | | |
    |---|---|
    | Entry ID | `iqhan_ch_3a` |
    | Type (wiki) | Enemy |
    | Spawn group | `iqhan_ch_3` |
    | Loot table | `iqhan_master` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:136` |
    | Defined in | `res/raw/monsterlist_v0610_monsters2.json` |

    Raw data:

    ```json
    {
     "id": "iqhan_ch_3a",
     "name": "Iqhan chaos master",
     "iconID": "monsters_rltiles2:136",
     "maxHP": 83,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 2,
      "max": 13
     },
     "spawnGroup": "iqhan_ch_3",
     "droplistID": "iqhan_master",
     "attackCost": 3,
     "attackChance": 170,
     "criticalSkill": 25,
     "criticalMultiplier": 2.0,
     "blockChance": 75,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "chaotic_grip",
        "magnitude": 4,
        "duration": 5,
        "chance": "50"
       }
      ]
     }
    }
    ```

??? info "Technical information: iqhan_ch_3b"

    | | |
    |---|---|
    | Entry ID | `iqhan_ch_3b` |
    | Type (wiki) | Enemy |
    | Spawn group | `iqhan_ch_3` |
    | Loot table | `iqhan_master` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:137` |
    | Defined in | `res/raw/monsterlist_v0610_monsters2.json` |

    Raw data:

    ```json
    {
     "id": "iqhan_ch_3b",
     "name": "Iqhan chaos master",
     "iconID": "monsters_rltiles2:137",
     "maxHP": 85,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 2,
      "max": 13
     },
     "spawnGroup": "iqhan_ch_3",
     "droplistID": "iqhan_master",
     "attackCost": 3,
     "attackChance": 170,
     "criticalSkill": 25,
     "criticalMultiplier": 2.0,
     "blockChance": 75,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "chaotic_grip",
        "magnitude": 4,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_ch_3a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_ch_3a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_ch_3a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_ch_3a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
