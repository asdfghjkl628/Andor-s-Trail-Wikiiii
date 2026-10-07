---
description: "Emerald jelly is an enemy in Andor's Trail (construct) with 35 HP, worth 144 XP, found in Crossroads Guardhouse. Drops: Gold coins, Mundane ring, Polished ring, Mundane necklace."
---

# ![](../assets/icons/monsters/monsters_tometik2_4.png){ .sprite } Emerald jelly

**Found in:** Crossroads Guardhouse: [roadbeforecrossroads1](../maps/roadbeforecrossroads1.md), Crossroads Guardhouse: [roadcave0](../maps/roadcave0.md), [roadcave1](../maps/roadcave1.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik2_4.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Crossroads Guardhouse |
| **Class** | Construct |
| **HP** | 35 |
| **XP when defeated** | 144 |
| **Immune to critical hits** | Yes |
| **Entry ID** | `jelly2` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Construct |
| HP | 35 |
| XP when defeated | 144 |
| Damage | 7 to 8 |
| Attack chance | 95 |
| Block chance | 45 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 15 |
| Critical multiplier | 2.0 |
| Critical hit chance | 12% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.

**On hit:** On target: [Corrosive slime](../conditions/slime.md) (magnitude 1, 4 rounds, 40% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 20% | 0 to 2 |
| [Mundane ring](../items/ring1.md) | 5% | 1 |
| [Polished ring](../items/ring2.md) | 5% | 1 |
| [Mundane necklace](../items/junk_necklace0.md) | 5% | 1 |
| [Polished necklace](../items/junk_necklace1.md) | 5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [roadbeforecrossroads1](../maps/roadbeforecrossroads1.md) | Crossroads Guardhouse | 3 | – |
| [roadcave0](../maps/roadcave0.md) | Crossroads Guardhouse | 11 | – |
| [roadcave1](../maps/roadcave1.md) | – | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Corrosive slime](../conditions/slime.md) (magnitude 1, 4 rounds, 40% chance) → (magnitude 1, 4 rounds, 40% chance)<br>Renamed “Emerald Jelly” → “Emerald jelly” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `jelly2` |
    | Spawn group | `jelly1` |
    | Loot table | `jelly` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik2:4` |
    | Defined in | `res/raw/monsterlist_v070_roadcave.json` |

    Raw data:

    ```json
    {
     "id": "jelly2",
     "name": "Emerald jelly",
     "iconID": "monsters_tometik2:4",
     "maxHP": 35,
     "moveCost": 5,
     "monsterClass": "construct",
     "attackDamage": {
      "min": 7,
      "max": 8
     },
     "spawnGroup": "jelly1",
     "droplistID": "jelly",
     "attackCost": 3,
     "attackChance": 95,
     "criticalSkill": 15,
     "criticalMultiplier": 2.0,
     "blockChance": 45,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "slime",
        "magnitude": 1,
        "duration": 4,
        "chance": "40"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jelly2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jelly2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jelly2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jelly2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
