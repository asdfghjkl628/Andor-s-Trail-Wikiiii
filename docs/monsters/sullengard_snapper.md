---
description: "Sullengard snapper is an NPC who can also be fought in Andor's Trail, found in Sullengard."
---

# ![](../assets/icons/monsters/monsters_tometik3_69.png){ .sprite } Sullengard snapper

**Where to find Sullengard snapper:** Sullengard: [sullengard5](../maps/sullengard5.md#pin-npc-sullengard_snapper), Sullengard: [sullengard_pond](../maps/sullengard_pond.md#pin-npc-sullengard_snapper), [sullengard_pond_east](../maps/sullengard_pond_east.md#pin-npc-sullengard_snapper), [way_to_sullengard_east10](../maps/way_to_sullengard_east10.md#pin-npc-sullengard_snapper) (+1 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik3_69.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Sullengard |
| **Class** | Reptile |
| **HP** | 100 |
| **XP when defeated** | 327 |
| **Entry ID** | `sullengard_snapper` |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Reptile |
| HP | 100 |
| XP when defeated | 327 |
| Damage | 11 to 15 |
| Attack chance | 130 |
| Block chance | 200 |
| Damage resistance | 10 |
| Max AP | 10 |
| Attack cost | 7 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 20 |
| Critical multiplier | 2.5 |
| Critical hit chance | 15% |

**When hit:** On self: [Bark skin](../conditions/barkskin.md) (magnitude 1, 5 rounds, 5% chance); On target: [Bleeding wound](../conditions/bleeding_wound.md) (magnitude 1, 5 rounds, 10% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Small rock](../items/rock.md) | 5% | 1 to 3 |
| [Gold coins](../items/gold.md) | 100% | 0 to 10 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [sullengard5](../maps/sullengard5.md) | Sullengard | 2 | – |
| [sullengard_pond](../maps/sullengard_pond.md) | Sullengard | 9 | – |
| [sullengard_pond_east](../maps/sullengard_pond_east.md) | – | 2 | – |
| [way_to_sullengard_east10](../maps/way_to_sullengard_east10.md) | – | 4 | – |
| [way_to_sullengard_pond_road](../maps/way_to_sullengard_pond_road.md) | – | 9 | – |

## Quests that count defeats

- [Pond safety](../quests/sullengard_pond_safety.md#stage-30) with [Nanette](../monsters/sullengard_nanette.md) ([sullengard2_northwest_house](../maps/sullengard2_northwest_house.md)) checks that at least 26 of these enemies have been defeated.

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Sullengard snapper. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/sullengard_snapper_00.json" data-npc="Sullengard snapper" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-sullengard_snapper_00"></span>**`sullengard_snapper_00`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if latest stage of [Pond safety](../quests/sullengard_pond_safety.md#stage-20) is 20)* → *fight starts*
    - Next → [sullengard_snapper_0](#d-sullengard_snapper_0)

    <span id="d-sullengard_snapper_0"></span>**`sullengard_snapper_0`** Sullengard snapper: “[You see the mouth open widely.]”

    - “Do you want a hug?” → [sullengard_snapper_1](#d-sullengard_snapper_1)
    - “Do you want some food?” → [sullengard_snapper_1](#d-sullengard_snapper_1)
    - “I better stay away.” → *conversation ends*

    <span id="d-sullengard_snapper_1"></span>**`sullengard_snapper_1`** Sullengard snapper: “[Snap].” — **effects:** applies condition bleeding_wound

    - “Ouch! Why did you bite me? Bad turtle!” → [sullengard_snapper_0](#d-sullengard_snapper_0)
    - “Ouch. Why are you mad at me? Angry turtle!” → [sullengard_snapper_0](#d-sullengard_snapper_0)



## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `sullengard_snapper` |
    | Spawn group | `sullengard_snapper` |
    | Loot table | `sullengard_snapper` |
    | Conversation | `sullengard_snapper_00` |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_tometik3:69` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "sullengard_snapper",
     "name": "Sullengard snapper",
     "iconID": "monsters_tometik3:69",
     "maxHP": 100,
     "unique": 1,
     "monsterClass": "reptile",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 11,
      "max": 15
     },
     "spawnGroup": "sullengard_snapper",
     "phraseID": "sullengard_snapper_00",
     "droplistID": "sullengard_snapper",
     "attackCost": 7,
     "attackChance": 130,
     "criticalSkill": 20,
     "criticalMultiplier": 2.5,
     "blockChance": 200,
     "damageResistance": 10,
     "hitReceivedEffect": {
      "conditionsSource": [
       {
        "condition": "barkskin",
        "magnitude": 1,
        "duration": 5,
        "chance": "5"
       }
      ],
      "conditionsTarget": [
       {
        "condition": "bleeding_wound",
        "magnitude": 1,
        "duration": 5,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_snapper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_snapper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_snapper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_snapper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
