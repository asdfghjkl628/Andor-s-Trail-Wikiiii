---
description: "Iqhan chaos beast is an enemy in Andor's Trail (construct) with 122–140 HP, worth 262–280 XP, found in Pwcave 2a, Pwcave 4. Drops: Gold coins, Chaosreaper, Regular potion of health."
---

# ![](../assets/icons/monsters/monsters_rltiles1_19.png){ .sprite } Iqhan chaos beast

**Where to find Iqhan chaos beast:** [Pwcave 2a and 1 more](#v-iqhan_chb_1a), [Pwcave 2a and 1 more](#v-iqhan_chb_1b)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_rltiles1_19.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Pwcave 2a, Pwcave 4 |
| **Class** | Construct |
| **HP** | 122–140 |
| **XP when defeated** | 262–280 |
| **Immune to crits** | Yes |
| **Introduced** | v0.7.0 or earlier |

</div>

## Pwcave 2a and 1 more { #v-iqhan_chb_1a }

**Where:** [Pwcave 2a](../maps/pwcave2a.md), [Pwcave 4](../maps/pwcave4.md)

### Combat

| | |
|---|---|
| Class | Construct |
| HP | 122 |
| XP when defeated | 262 |
| Damage | 0 to 15 |
| AC | 150 |
| BC | 45 |
| DR | 9 |
| Attacks per turn | 1 (9 AP each, 10 AP) |
| Crit chance | 9% (×3.0) |

**Immune to critical hits.**

**Its hits:** On target: [Chaotic grip](../conditions/chaotic_grip.md) (magnitude 5, 5 rounds, 50% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 0 to 1 |
| [Chaosreaper](../items/chaosreaper.md) | 0.1% | 1 |
| [Regular potion of health](../items/health.md) | 5% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Pwcave 2a](../maps/pwcave2a.md) | – | 1 | – |
| [Pwcave 4](../maps/pwcave4.md) | – | 7 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Chaotic grip](../conditions/chaotic_grip.md) (magnitude 5, 5 rounds, 50% chance) → (magnitude 5, 5 rounds, 50% chance) |
| [v0.7.4](../versions/0.7.4.md) | Attack cost: 10 → 9 |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Pwcave 2a and 1 more (2) { #v-iqhan_chb_1b }

**Where:** [Pwcave 2a](../maps/pwcave2a.md), [Pwcave 4](../maps/pwcave4.md)

### Combat

| | |
|---|---|
| Class | Construct |
| HP | 140 |
| XP when defeated | 280 |
| Damage | 0 to 15 |
| AC | 150 |
| BC | 45 |
| DR | 9 |
| Attacks per turn | 1 (9 AP each, 10 AP) |
| Crit chance | 9% (×3.0) |

**Immune to critical hits.**

**Its hits:** On target: [Chaotic grip](../conditions/chaotic_grip.md) (magnitude 5, 5 rounds, 50% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 0 to 1 |
| [Chaosreaper](../items/chaosreaper.md) | 0.1% | 1 |
| [Regular potion of health](../items/health.md) | 5% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Pwcave 2a](../maps/pwcave2a.md) | – | 1 | – |
| [Pwcave 4](../maps/pwcave4.md) | – | 7 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Chaotic grip](../conditions/chaotic_grip.md) (magnitude 5, 5 rounds, 50% chance) → (magnitude 5, 5 rounds, 50% chance) |
| [v0.7.4](../versions/0.7.4.md) | Attack cost: 10 → 9 |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Iqhan chaos beast. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: combat statistics.

| Entry | Type | Section |
|---|---|---|
| `iqhan_chb_1a` | Enemy | [Pwcave 2a and 1 more](#v-iqhan_chb_1a) |
| `iqhan_chb_1b` | Enemy | [Pwcave 2a and 1 more](#v-iqhan_chb_1b) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: iqhan_chb_1a"

    | | |
    |---|---|
    | Entry ID | `iqhan_chb_1a` |
    | Type (wiki) | Enemy |
    | Spawn group | `iqhan_chb_1` |
    | Loot table | `iqhan_beast` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:19` |
    | Defined in | `res/raw/monsterlist_v0610_monsters2.json` |

    Raw data:

    ```json
    {
     "id": "iqhan_chb_1a",
     "name": "Iqhan chaos beast",
     "iconID": "monsters_rltiles1:19",
     "maxHP": 122,
     "maxAP": 10,
     "moveCost": 10,
     "monsterClass": "construct",
     "attackDamage": {
      "min": 0,
      "max": 15
     },
     "spawnGroup": "iqhan_chb_1",
     "droplistID": "iqhan_beast",
     "attackCost": 9,
     "attackChance": 150,
     "criticalSkill": 10,
     "criticalMultiplier": 3.0,
     "blockChance": 45,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "chaotic_grip",
        "magnitude": 5,
        "duration": 5,
        "chance": "50"
       }
      ]
     }
    }
    ```

??? info "Technical information: iqhan_chb_1b"

    | | |
    |---|---|
    | Entry ID | `iqhan_chb_1b` |
    | Type (wiki) | Enemy |
    | Spawn group | `iqhan_chb_1` |
    | Loot table | `iqhan_beast` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:19` |
    | Defined in | `res/raw/monsterlist_v0610_monsters2.json` |

    Raw data:

    ```json
    {
     "id": "iqhan_chb_1b",
     "name": "Iqhan chaos beast",
     "iconID": "monsters_rltiles1:19",
     "maxHP": 140,
     "maxAP": 10,
     "moveCost": 10,
     "monsterClass": "construct",
     "attackDamage": {
      "min": 0,
      "max": 15
     },
     "spawnGroup": "iqhan_chb_1",
     "droplistID": "iqhan_beast",
     "attackCost": 9,
     "attackChance": 150,
     "criticalSkill": 10,
     "criticalMultiplier": 3.0,
     "blockChance": 45,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "chaotic_grip",
        "magnitude": 5,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_chb_1a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_chb_1a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_chb_1a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_chb_1a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
