---
description: "Great fungi is an enemy in Andor's Trail (animal) with 175 HP, worth 316 XP, found in Mushroom m 3 2. Drops: Spores of the giant mushroom, Bogsten's mushroom."
---

# ![](../assets/icons/monsters/monsters_bosses_2x2_0.png){ .sprite } Great fungi

**Found in:** [Mushroom m 3 2](../maps/mushroom_m3_2.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_bosses_2x2_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Mushroom m 3 2 |
| **Class** | Animal |
| **HP** | 175 |
| **XP when defeated** | 316 |
| **Entry ID** | `boss_fungi` |
| **Introduced** | [v0.7.13](../versions/0.7.13.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 175 |
| XP when defeated | 316 |
| Damage | 3 to 6 |
| Attack chance | 120 |
| Block chance | 60 |
| Damage resistance | 1 |
| Max AP | 20 |
| Attack cost | 5 AP |
| Attacks per turn | 4 |
| Move cost | 6 AP |
| Critical skill | 20 |
| Critical multiplier | 2.0 |
| Critical hit chance | 15% |

**On hit:** On target: [Spore poisoning](../conditions/spore_poison.md) (magnitude 2, 5 rounds, 20% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Spores of the giant mushroom](../items/fungi_panic_spores.md) | 100% | 1 to 2 |
| [Bogsten's mushroom](../items/mushroom_bogsten.md) | 25% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Mushroom m 3 2](../maps/mushroom_m3_2.md) | – | 1 | – |

## Quests that count defeats

- [Fungi Panic story flags (hidden flag)](../quests/fungi_panic_nondisplayed.md#stage-90) with stepping on a trigger on [Mushroom m 3 2](../maps/mushroom_m3_2.md) checks that this enemy has been defeated.


## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `boss_fungi` |
    | Spawn group | `boss_fungi` |
    | Loot table | `dangerous_fungi_1` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_bosses_2x2:0` |
    | Defined in | `res/raw/monsterlist_fungi_panic.json` |

    Raw data:

    ```json
    {
     "id": "boss_fungi",
     "name": "Great fungi",
     "iconID": "monsters_bosses_2x2:0",
     "maxHP": 175,
     "maxAP": 20,
     "moveCost": 6,
     "unique": 1,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 3,
      "max": 6
     },
     "spawnGroup": "boss_fungi",
     "droplistID": "dangerous_fungi_1",
     "attackCost": 5,
     "attackChance": 120,
     "criticalSkill": 20,
     "criticalMultiplier": 2.0,
     "blockChance": 60,
     "damageResistance": 1,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "spore_poison",
        "magnitude": 2,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=boss_fungi.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=boss_fungi.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=boss_fungi.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=boss_fungi.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
