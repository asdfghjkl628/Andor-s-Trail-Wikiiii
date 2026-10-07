---
description: "Venomous cave serpent is an enemy in Andor's Trail (reptile) with 30 HP, worth 108 XP, found in basiliskcave1_1_3, basiliskcave1_1_4, basiliskcave1_1_5. Drops: Gold coins, Meat, Poison gland."
---

# ![](../assets/icons/monsters/monsters_tometik4_19.png){ .sprite } Venomous cave serpent

**Found in:** [basiliskcave1_1_3](../maps/basiliskcave1_1_3.md), [basiliskcave1_1_4](../maps/basiliskcave1_1_4.md), [basiliskcave1_1_5](../maps/basiliskcave1_1_5.md), [basiliskcave2](../maps/basiliskcave2.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik4_19.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | basiliskcave1_1_3, basiliskcave1_1_4, basiliskcave1_1_5 |
| **Class** | Reptile |
| **HP** | 30 |
| **XP when defeated** | 108 |
| **Entry ID** | `venomous_cave_serpent` |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Reptile |
| HP | 30 |
| XP when defeated | 108 |
| Damage | 3 to 7 |
| Attack chance | 100 |
| Block chance | 45 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 14 |
| Critical multiplier | 2.0 |
| Critical hit chance | 11% |

**On hit:** On target: [Venom](../conditions/venom.md) (magnitude 1, 3 rounds, 10% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 3 to 10 |
| [Meat](../items/meat.md) | 5% | 1 |
| [Poison gland](../items/gland.md) | 5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [basiliskcave1_1_3](../maps/basiliskcave1_1_3.md) | – | 6 | – |
| [basiliskcave1_1_4](../maps/basiliskcave1_1_4.md) | – | 3 | – |
| [basiliskcave1_1_5](../maps/basiliskcave1_1_5.md) | – | 3 | – |
| [basiliskcave2](../maps/basiliskcave2.md) | – | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added |
| [v0.7.13](../versions/0.7.13.md) | Loot table added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `venomous_cave_serpent` |
    | Spawn group | `cave_serpent_2` |
    | Loot table | `cave_serpent` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik4:19` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "venomous_cave_serpent",
     "name": "Venomous cave serpent",
     "iconID": "monsters_tometik4:19",
     "maxHP": 30,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 3,
      "max": 7
     },
     "spawnGroup": "cave_serpent_2",
     "droplistID": "cave_serpent",
     "attackCost": 5,
     "attackChance": 100,
     "criticalSkill": 14,
     "criticalMultiplier": 2.0,
     "blockChance": 45,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "venom",
        "magnitude": 1,
        "duration": 3,
        "chance": "10"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=venomous_cave_serpent.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=venomous_cave_serpent.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=venomous_cave_serpent.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=venomous_cave_serpent.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
