---
description: "Gornaud is an enemy in Andor's Trail (giant) with 95 HP, worth 197 XP, found in Blackwater Mountain. Drops: Gold coins, Meat, Animal hair."
---

# ![](../assets/icons/monsters/monsters_rltiles2_29.png){ .sprite } Gornaud

**Found in:** Blackwater Mountain: [blackwater_mountain15](../maps/blackwater_mountain15.md), Blackwater Mountain: [blackwater_mountain16](../maps/blackwater_mountain16.md), Blackwater Mountain: [blackwater_mountain17](../maps/blackwater_mountain17.md), Blackwater Mountain: [blackwater_mountain18](../maps/blackwater_mountain18.md) (+10 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_29.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Blackwater Mountain |
| **Class** | Giant |
| **HP** | 95 |
| **XP when defeated** | 197 |
| **Entry ID** | `gornaud` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Giant |
| HP | 95 |
| XP when defeated | 197 |
| Damage | 0 to 15 |
| Attack chance | 70 |
| Block chance | 50 |
| Damage resistance | 4 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

**On hit:** On target: Dazed (magnitude 1, 5 rounds, 50% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 1 to 40 |
| [Meat](../items/meat.md) | 5% | 1 to 2 |
| [Animal hair](../items/hair.md) | 10% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [blackwater_mountain15](../maps/blackwater_mountain15.md) | Blackwater Mountain | 4 | – |
| [blackwater_mountain16](../maps/blackwater_mountain16.md) | Blackwater Mountain | 11 | – |
| [blackwater_mountain17](../maps/blackwater_mountain17.md) | Blackwater Mountain | 2 | – |
| [blackwater_mountain18](../maps/blackwater_mountain18.md) | Blackwater Mountain | 7 | – |
| [blackwater_mountain3](../maps/blackwater_mountain3.md) | – | 2 | – |
| [blackwater_mountain4](../maps/blackwater_mountain4.md) | – | 5 | – |
| [blackwater_mountain5](../maps/blackwater_mountain5.md) | – | 4 | – |
| [blackwater_mountain53](../maps/blackwater_mountain53.md) | Blackwater Mountain | 4 | – |
| [blackwater_mountain56](../maps/blackwater_mountain56.md) | Blackwater Mountain | 2 | – |
| [blackwater_mountain5a](../maps/blackwater_mountain5a.md) | – | 3 | – |
| [blackwater_mountain70](../maps/blackwater_mountain70.md) | Blackwater Mountain | 2 | – |
| [bwmfill1](../maps/bwmfill1.md) | Blackwater Mountain | 1 | – |
| [bwmfill2](../maps/bwmfill2.md) | Blackwater Mountain | 3 | – |
| [bwmfill8](../maps/bwmfill8.md) | Blackwater Mountain | 2 | – |

## Quests that count defeats

- A conversation with [General's henchman](../monsters/ortholion_guard1.md) ([blackwater_mountain11](../maps/blackwater_mountain11.md)), [Feygard scout](../monsters/feygard_scout.md#v-ortholion_guard6) ([blackwater_mountain10](../maps/blackwater_mountain10.md)) checks that at least 100 of these enemies have been defeated.
- A conversation with [Jern](../monsters/prim_bar_regular.md) ([blackwater_mountain22](../maps/blackwater_mountain22.md)) checks that at least 50 of these enemies have been defeated.


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | hitEffect: {"conditionsTarget": [{"chance": 50, "c… → {"conditionsTarget": [{"chance": "50", … |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `gornaud` |
    | Spawn group | `gornaud_2` |
    | Loot table | `gornaud_2` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:29` |
    | Defined in | `res/raw/monsterlist_v069_monsters.json` |

    Raw data:

    ```json
    {
     "id": "gornaud",
     "name": "Gornaud",
     "iconID": "monsters_rltiles2:29",
     "maxHP": 95,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "giant",
     "attackDamage": {
      "min": 0,
      "max": 15
     },
     "spawnGroup": "gornaud_2",
     "droplistID": "gornaud_2",
     "attackCost": 5,
     "attackChance": 70,
     "blockChance": 50,
     "damageResistance": 4,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "dazed",
        "magnitude": 1,
        "duration": 5,
        "chance": "50"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gornaud.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gornaud.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gornaud.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gornaud.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
