---
description: "Iqhan chaos evoker is an enemy in Andor's Trail (humanoid) with 73–75 HP, worth 237–240 XP, found in Pwcave 2, Pwcave 2a, Pwcave 3. Drops: Gold coins, Iqhan pendant, Wooden buckler, Iron dagger."
---

# ![](../assets/icons/monsters/monsters_rltiles2_135.png){ .sprite } Iqhan chaos evoker

**Where to find Iqhan chaos evoker:** [Pwcave 2 and 3 more](#v-iqhan_ch_1a), [Pwcave 2 and 3 more](#v-iqhan_ch_1b)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_135.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Pwcave 2, Pwcave 2a, Pwcave 3 |
| **Class** | Humanoid |
| **HP** | 73–75 |
| **XP when defeated** | 237–240 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Pwcave 2 and 3 more { #v-iqhan_ch_1a }

**Where:** [Pwcave 2](../maps/pwcave2.md), [Pwcave 2a](../maps/pwcave2a.md), [Pwcave 3](../maps/pwcave3.md), [Pwcave 4](../maps/pwcave4.md)

### Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 73 |
| XP when defeated | 237 |
| Damage | 2 to 15 |
| AC | 140 |
| BC | 60 |
| DR | 0 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 15% (×2.0) |

**Its hits:** On target: [Chaotic grip](../conditions/chaotic_grip.md) (magnitude 2, 5 rounds, 20% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 1 to 9 |
| [Iqhan pendant](../items/iqhan_pendant.md) | 5% | 1 |
| [Wooden buckler](../items/shield1.md) | 5% | 1 |
| [Iron dagger](../items/dagger0.md) | 5% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Pwcave 2](../maps/pwcave2.md) | – | 1 | – |
| [Pwcave 2a](../maps/pwcave2a.md) | – | 5 | – |
| [Pwcave 3](../maps/pwcave3.md) | – | 8 | – |
| [Pwcave 4](../maps/pwcave4.md) | – | 2 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Chaotic grip](../conditions/chaotic_grip.md) (magnitude 2, 5 rounds, 20% chance) → (magnitude 2, 5 rounds, 20% chance) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Pwcave 2 and 3 more (2) { #v-iqhan_ch_1b }

**Where:** [Pwcave 2](../maps/pwcave2.md), [Pwcave 2a](../maps/pwcave2a.md), [Pwcave 3](../maps/pwcave3.md), [Pwcave 4](../maps/pwcave4.md)

### Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 75 |
| XP when defeated | 240 |
| Damage | 2 to 14 |
| AC | 150 |
| BC | 60 |
| DR | 0 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 15% (×2.0) |

**Its hits:** On target: [Chaotic grip](../conditions/chaotic_grip.md) (magnitude 2, 5 rounds, 20% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 1 to 9 |
| [Iqhan pendant](../items/iqhan_pendant.md) | 5% | 1 |
| [Wooden buckler](../items/shield1.md) | 5% | 1 |
| [Iron dagger](../items/dagger0.md) | 5% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Pwcave 2](../maps/pwcave2.md) | – | 1 | – |
| [Pwcave 2a](../maps/pwcave2a.md) | – | 5 | – |
| [Pwcave 3](../maps/pwcave3.md) | – | 8 | – |
| [Pwcave 4](../maps/pwcave4.md) | – | 2 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Chaotic grip](../conditions/chaotic_grip.md) (magnitude 2, 5 rounds, 20% chance) → (magnitude 2, 5 rounds, 20% chance) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Iqhan chaos evoker. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: combat statistics.

| Entry | Type | Section |
|---|---|---|
| `iqhan_ch_1a` | Enemy | [Pwcave 2 and 3 more](#v-iqhan_ch_1a) |
| `iqhan_ch_1b` | Enemy | [Pwcave 2 and 3 more](#v-iqhan_ch_1b) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: iqhan_ch_1a"

    | | |
    |---|---|
    | Entry ID | `iqhan_ch_1a` |
    | Type (wiki) | Enemy |
    | Spawn group | `iqhan_ch_1` |
    | Loot table | `iqhan` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:135` |
    | Defined in | `res/raw/monsterlist_v0610_monsters2.json` |

    Raw data:

    ```json
    {
     "id": "iqhan_ch_1a",
     "name": "Iqhan chaos evoker",
     "iconID": "monsters_rltiles2:135",
     "maxHP": 73,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 2,
      "max": 15
     },
     "spawnGroup": "iqhan_ch_1",
     "droplistID": "iqhan",
     "attackCost": 3,
     "attackChance": 140,
     "criticalSkill": 20,
     "criticalMultiplier": 2.0,
     "blockChance": 60,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "chaotic_grip",
        "magnitude": 2,
        "duration": 5,
        "chance": "20"
       }
      ]
     }
    }
    ```

??? info "Technical information: iqhan_ch_1b"

    | | |
    |---|---|
    | Entry ID | `iqhan_ch_1b` |
    | Type (wiki) | Enemy |
    | Spawn group | `iqhan_ch_1` |
    | Loot table | `iqhan` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:135` |
    | Defined in | `res/raw/monsterlist_v0610_monsters2.json` |

    Raw data:

    ```json
    {
     "id": "iqhan_ch_1b",
     "name": "Iqhan chaos evoker",
     "iconID": "monsters_rltiles2:135",
     "maxHP": 75,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 2,
      "max": 14
     },
     "spawnGroup": "iqhan_ch_1",
     "droplistID": "iqhan",
     "attackCost": 3,
     "attackChance": 150,
     "criticalSkill": 20,
     "criticalMultiplier": 2.0,
     "blockChance": 60,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "chaotic_grip",
        "magnitude": 2,
        "duration": 5,
        "chance": "20"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_ch_1a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_ch_1a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_ch_1a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_ch_1a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
