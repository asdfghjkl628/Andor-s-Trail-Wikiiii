---
description: "Fungi is an enemy in Andor's Trail (animal) with 25 HP, worth 83 XP, found in bogsten2, bogsten3, bogsten4. Drops: Spores of the giant mushroom, Bogsten's mushroom."
---

# ![](../assets/icons/monsters/monsters_gisons_4.png){ .sprite } Fungi

**Found in:** [bogsten2](../maps/bogsten2.md), [bogsten3](../maps/bogsten3.md), [bogsten4](../maps/bogsten4.md), [mushroom_m2_1](../maps/mushroom_m2_1.md) (+5 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_gisons_4.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | bogsten2, bogsten3, bogsten4 |
| **Class** | Animal |
| **HP** | 25 |
| **XP when defeated** | 83 |
| **Entry ID** | `mid_fungi` |
| **Introduced** | [v0.7.13](../versions/0.7.13.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 25 |
| XP when defeated | 83 |
| Damage | 2 to 3 |
| Attack chance | 110 |
| Block chance | 20 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

**On hit:** On target: Spore poisoning (magnitude 1, 2 rounds, 10% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Spores of the giant mushroom](../items/fungi_panic_spores.md) | 10% | 1 |
| [Bogsten's mushroom](../items/mushroom_bogsten.md) | 10% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [bogsten2](../maps/bogsten2.md) | – | 5 | – |
| [bogsten3](../maps/bogsten3.md) | – | 6 | – |
| [bogsten4](../maps/bogsten4.md) | – | 7 | – |
| [mushroom_m2_1](../maps/mushroom_m2_1.md) | – | 5 | – |
| [mushroom_m2_2](../maps/mushroom_m2_2.md) | – | 2 | – |
| [mushroom_m2_4](../maps/mushroom_m2_4.md) | – | 4 | – |
| [mushroom_m2_5](../maps/mushroom_m2_5.md) | – | 2 | – |
| [mushroom_m3_1](../maps/mushroom_m3_1.md) | – | 3 | – |
| [mushroom_m3_2](../maps/mushroom_m3_2.md) | – | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `mid_fungi` |
    | Spawn group | `mid_fungi` |
    | Loot table | `mid_fungi` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_gisons:4` |
    | Defined in | `res/raw/monsterlist_fungi_panic.json` |

    Raw data:

    ```json
    {
     "id": "mid_fungi",
     "name": "Fungi",
     "iconID": "monsters_gisons:4",
     "maxHP": 25,
     "maxAP": 10,
     "moveCost": 10,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 2,
      "max": 3
     },
     "spawnGroup": "mid_fungi",
     "droplistID": "mid_fungi",
     "attackCost": 5,
     "attackChance": 110,
     "blockChance": 20,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "spore_poison",
        "magnitude": 1,
        "duration": 2,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mid_fungi.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mid_fungi.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mid_fungi.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mid_fungi.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
