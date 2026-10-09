---
description: "Glowing flame is an enemy in Andor's Trail (construct) with 112 HP, worth 300 XP, found in Lostmine 10, Lostmine 9. Drops: Burnt ash, Glass gem."
---

# ![](../assets/icons/monsters/monsters_rltiles1_2.png){ .sprite } Glowing flame

**Found in:** [Lostmine 10](../maps/lostmine10.md), [Lostmine 9](../maps/lostmine9.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_2.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Lostmine 10, Lostmine 9 |
| **Class** | Construct |
| **HP** | 112 |
| **XP when defeated** | 300 |
| **Immune to critical hits** | Yes |
| **Entry ID** | `fire5` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Construct |
| HP | 112 |
| XP when defeated | 300 |
| Damage | 0 to 9 |
| Attack chance | 153 |
| Block chance | 94 |
| Damage resistance | 6 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 15 |
| Critical multiplier | 2.5 |
| Critical hit chance | 12% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.

**On hit:** On target: [Ablaze](../conditions/fire.md) (magnitude 1, 5 rounds, 20% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Burnt ash](../items/ash.md) | 10% | 0 to 1 |
| [Glass gem](../items/gem1.md) | 100% | 1 to 3 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Lostmine 10](../maps/lostmine10.md) | – | 7 | – |
| [Lostmine 9](../maps/lostmine9.md) | – | 6 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Attack damage: 0–9 → 0–9<br>Critical multiplier: 2.5 → 2.5<br>On hit, condition on target: [Ablaze](../conditions/fire.md) (magnitude 1, 5 rounds, 20% chance) → (magnitude 1, 5 rounds, 20% chance) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `fire5` |
    | Spawn group | `fire3` |
    | Loot table | `fire` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:2` |
    | Defined in | `res/raw/monsterlist_v070_charwood2.json` |

    Raw data:

    ```json
    {
     "id": "fire5",
     "name": "Glowing flame",
     "iconID": "monsters_rltiles1:2",
     "maxHP": 112,
     "moveCost": 5,
     "monsterClass": "construct",
     "attackDamage": {
      "min": 0,
      "max": 9
     },
     "spawnGroup": "fire3",
     "droplistID": "fire",
     "attackCost": 3,
     "attackChance": 153,
     "criticalSkill": 15,
     "criticalMultiplier": 2.5,
     "blockChance": 94,
     "damageResistance": 6,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "fire",
        "magnitude": 1,
        "duration": 5,
        "chance": "20"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fire5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fire5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fire5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fire5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
