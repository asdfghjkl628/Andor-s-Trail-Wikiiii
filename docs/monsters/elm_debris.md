---
description: "Animated debris is an enemy in Andor's Trail (construct) with 70 HP, worth 317 XP, found in elm5f_2, elm_2f_1."
---

# ![](../assets/icons/monsters/monsters_omi2_16.png){ .sprite } Animated debris

**Found in:** [elm5f_2](../maps/elm5f_2.md), [elm_2f_1](../maps/elm_2f_1.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_omi2_16.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | elm5f_2, elm_2f_1 |
| **Class** | Construct |
| **HP** | 70 |
| **XP when defeated** | 317 |
| **Immune to critical hits** | Yes |
| **Entry ID** | `elm_debris` |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Construct |
| HP | 70 |
| XP when defeated | 317 |
| Damage | 1 to 9 |
| Attack chance | 91 |
| Block chance | 149 |
| Damage resistance | 21 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 10 |
| Critical multiplier | 3.0 |
| Critical hit chance | 9% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.

**On hit:** On self: Shadow's accuracy (magnitude 2, 2 rounds, 10% chance); On target: Bleeding wound (magnitude 3, 5 rounds, 20% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [elm5f_2](../maps/elm5f_2.md) | – | 2 | Appears later, during a quest |
| [elm_2f_1](../maps/elm_2f_1.md) | – | 2 | Appears later, during a quest |


## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `elm_debris` |
    | Spawn group | `elm_debris` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_omi2:16` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "elm_debris",
     "name": "Animated debris",
     "iconID": "monsters_omi2:16",
     "maxHP": 70,
     "unique": 1,
     "monsterClass": "construct",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 1,
      "max": 9
     },
     "attackChance": 91,
     "criticalSkill": 10,
     "criticalMultiplier": 3.0,
     "blockChance": 149,
     "damageResistance": 21,
     "hitEffect": {
      "conditionsSource": [
       {
        "condition": "shadow_acc",
        "magnitude": 2,
        "duration": 2,
        "chance": "10"
       }
      ],
      "conditionsTarget": [
       {
        "condition": "bleeding_wound",
        "magnitude": 3,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_debris.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_debris.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_debris.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_debris.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
