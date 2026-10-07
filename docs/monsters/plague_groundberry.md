---
description: "Plague groundberry is an enemy in Andor's Trail (construct) with 149 HP, worth 588 XP, found in sullengard_woods11, sullengard_woods12, sullengard_woods3. Drops: Poison gland, Poisonous spores."
---

# ![](../assets/icons/monsters/monsters_tometik4_12.png){ .sprite } Plague groundberry

**Found in:** [sullengard_woods11](../maps/sullengard_woods11.md), [sullengard_woods12](../maps/sullengard_woods12.md), [sullengard_woods3](../maps/sullengard_woods3.md), [sullengard_woods4](../maps/sullengard_woods4.md) (+2 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik4_12.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | sullengard_woods11, sullengard_woods12, sullengard_woods3 |
| **Class** | Construct |
| **HP** | 149 |
| **XP when defeated** | 588 |
| **Immune to critical hits** | Yes |
| **Entry ID** | `plague_groundberry` |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Construct |
| HP | 149 |
| XP when defeated | 588 |
| Damage | 10 to 12 |
| Attack chance | 178 |
| Block chance | 243 |
| Damage resistance | 9 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 3 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.

**On hit:** On target: Weak Poison (magnitude 4, 3 rounds, 50% chance); Spore contagion (magnitude 1, 3 rounds, 15% chance); Nausea (magnitude 2, 2 rounds, 25% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Poison gland](../items/gland.md) | 20% | 1 |
| [Poisonous spores](../items/poisonous_spores.md) | 35% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [sullengard_woods11](../maps/sullengard_woods11.md) | – | 2 | – |
| [sullengard_woods12](../maps/sullengard_woods12.md) | – | 6 | – |
| [sullengard_woods3](../maps/sullengard_woods3.md) | – | 3 | – |
| [sullengard_woods4](../maps/sullengard_woods4.md) | – | 5 | – |
| [sullengard_woods5](../maps/sullengard_woods5.md) | – | 8 | – |
| [sullengard_woods7](../maps/sullengard_woods7.md) | – | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `plague_groundberry` |
    | Spawn group | `plague_groundberry` |
    | Loot table | `plague_groundberry_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_tometik4:12` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "plague_groundberry",
     "name": "Plague groundberry",
     "iconID": "monsters_tometik4:12",
     "maxHP": 149,
     "moveCost": 3,
     "monsterClass": "construct",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 10,
      "max": 12
     },
     "spawnGroup": "plague_groundberry",
     "droplistID": "plague_groundberry_dl",
     "attackCost": 3,
     "attackChance": 178,
     "blockChance": 243,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "poison_weak",
        "magnitude": 4,
        "duration": 3,
        "chance": "50"
       },
       {
        "condition": "contagion2",
        "magnitude": 1,
        "duration": 3,
        "chance": "15"
       },
       {
        "condition": "nausea",
        "magnitude": 2,
        "duration": 2,
        "chance": "25"
       }
      ]
     }
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=plague_groundberry.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=plague_groundberry.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=plague_groundberry.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=plague_groundberry.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
