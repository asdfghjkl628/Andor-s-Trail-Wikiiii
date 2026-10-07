---
description: "Zachlanny is an NPC who can also be fought in Andor's Trail, found in aidem_base_2, aidem_camp, aidem_base_2, Fallhaven, Sullengard."
---

# ![](../assets/icons/monsters/monsters_ld1_65.png){ .sprite } Zachlanny

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_65.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | aidem_base_2, aidem_camp, aidem_base_2, Fallhaven, Sullengard |
| **Class** | Humanoid |
| **HP** | 329 |
| **XP when defeated** | 707 |
| **Entries in game data** | 4 |
| **Introduced** | [v0.8.8](../versions/0.8.8.md) |

</div>

!!! info "4 entries in the game data"
    The game's data files define 4 separate characters named Zachlanny. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location, combat statistics, loot or shop stock, movement. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`aidem_camp_zachlanny`](#v-aidem_camp_zachlanny) | NPC | [aidem_base_2](../maps/aidem_base_2.md#pin-npc-aidem_camp_zachlanny), [aidem_camp](../maps/aidem_camp.md#pin-npc-aidem_camp_zachlanny) | – | – |
| [`aidem_base_zachlanny_aggressive`](#v-aidem_base_zachlanny_aggressive) | Enemy | [aidem_base_2](../maps/aidem_base_2.md) | – | 329 |
| [`aidem_jail_zachlanny`](#v-aidem_jail_zachlanny) | Enemy | Fallhaven: [guildbrig2](../maps/guildbrig2.md) | – | 1 |
| [`guild04_rebcomrade_3`](#v-guild04_rebcomrade_3) | NPC | Sullengard: [sullengard_tavern_basement](../maps/sullengard_tavern_basement.md#pin-npc-guild04_rebcomrade_3) | – | – |

## Aidem base 2 and 1 more (aidem_camp_zachlanny) { #v-aidem_camp_zachlanny }

**Entry ID:** `aidem_camp_zachlanny` · **Type:** NPC

**Location:** [aidem_base_2](../maps/aidem_base_2.md#pin-npc-aidem_camp_zachlanny), [aidem_camp](../maps/aidem_camp.md#pin-npc-aidem_camp_zachlanny)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [aidem_base_2](../maps/aidem_base_2.md) | – | 1 | Appears later, during a quest |
| [aidem_camp](../maps/aidem_camp.md) | – | 1 | Appears later, during a quest |

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Zachlanny. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/aidem_camp_zachlanny_10.json" data-npc="Zachlanny" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-aidem_camp_zachlanny-aidem_camp_zachlanny_10"></span>**`aidem_camp_zachlanny_10`** Zachlanny: “Are you lost, kid?”




### Version history

| Version | Change |
|---|---|
| [v0.8.8](../versions/0.8.8.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (aidem_camp_zachlanny)"

    | | |
    |---|---|
    | Entry ID | `aidem_camp_zachlanny` |
    | Spawn group | `aidem_camp_zachlanny` |
    | Loot table | `aidem_camp_zachlanny_dl` |
    | Conversation | `aidem_camp_zachlanny_10` |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_ld1:65` |
    | Defined in | `res/raw/monsterlist_mt_galmore.json` |

    Raw data:

    ```json
    {
     "id": "aidem_camp_zachlanny",
     "name": "Zachlanny",
     "iconID": "monsters_ld1:65",
     "maxHP": 1,
     "moveCost": 10,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "helpOthers",
     "phraseID": "aidem_camp_zachlanny_10",
     "droplistID": "aidem_camp_zachlanny_dl"
    }
    ```


## Aidem base 2 (aidem_base_zachlanny_aggressive) { #v-aidem_base_zachlanny_aggressive }

**Entry ID:** `aidem_base_zachlanny_aggressive` · **Type:** Enemy

**Location:** [aidem_base_2](../maps/aidem_base_2.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 329 |
| XP when defeated | 707 |
| Damage | 7 to 9 |
| Attack chance | 158 |
| Block chance | 170 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 2 AP |
| Critical skill | 3 |
| Critical multiplier | 2.0 |
| Critical hit chance | 2% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Zachlanny ring](../items/zachlanny_ring.md) | 100% | 1 |
| [Gold coins](../items/gold.md) | 100% | 2000 to 3500 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [aidem_base_2](../maps/aidem_base_2.md) | – | 1 | Appears later, during a quest |

### Quests that count defeats

- [Wanted men](../quests/wanted_men.md#stage-76) with stepping on a trigger on [aidem_base_2](../maps/aidem_base_2.md) checks that this enemy has been defeated.


### Version history

| Version | Change |
|---|---|
| [v0.8.8](../versions/0.8.8.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (aidem_base_zachlanny_aggressive)"

    | | |
    |---|---|
    | Entry ID | `aidem_base_zachlanny_aggressive` |
    | Spawn group | `help_defy` |
    | Loot table | `aidem_camp_zachlanny_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:65` |
    | Defined in | `res/raw/monsterlist_mt_galmore.json` |

    Raw data:

    ```json
    {
     "id": "aidem_base_zachlanny_aggressive",
     "name": "Zachlanny",
     "iconID": "monsters_ld1:65",
     "maxHP": 329,
     "moveCost": 2,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 7,
      "max": 9
     },
     "spawnGroup": "help_defy",
     "droplistID": "aidem_camp_zachlanny_dl",
     "attackCost": 3,
     "attackChance": 158,
     "criticalSkill": 3,
     "criticalMultiplier": 2.0,
     "blockChance": 170
    }
    ```


## Fallhaven, Guildbrig2 (aidem_jail_zachlanny) { #v-aidem_jail_zachlanny }

**Entry ID:** `aidem_jail_zachlanny` · **Type:** Enemy

**Location:** Fallhaven: [guildbrig2](../maps/guildbrig2.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 1 |
| XP when defeated | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [guildbrig2](../maps/guildbrig2.md) | Fallhaven | 1 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.8.8](../versions/0.8.8.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (aidem_jail_zachlanny)"

    | | |
    |---|---|
    | Entry ID | `aidem_jail_zachlanny` |
    | Spawn group | `aidem_jail_zachlanny` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:65` |
    | Defined in | `res/raw/monsterlist_mt_galmore.json` |

    Raw data:

    ```json
    {
     "id": "aidem_jail_zachlanny",
     "name": "Zachlanny",
     "iconID": "monsters_ld1:65",
     "monsterClass": "humanoid"
    }
    ```


## Sullengard, Sullengard tavern basement (guild04_rebcomrade_3) { #v-guild04_rebcomrade_3 }

**Entry ID:** `guild04_rebcomrade_3` · **Type:** NPC

**Location:** Sullengard: [sullengard_tavern_basement](../maps/sullengard_tavern_basement.md#pin-npc-guild04_rebcomrade_3)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Zachlanny. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/smuggler6_1.json" data-npc="Zachlanny" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guild04_rebcomrade_3-smuggler6_1"></span>**`smuggler6_1`** Zachlanny: “Can you spare some gold?”

    - “Get away from me!” → *conversation ends*
    - “Here's 5 gold.” *(if pay 5 gold)* → [smuggler6_3](#d-guild04_rebcomrade_3-smuggler6_3)
    - “Here's 50 gold.” *(if pay 50 gold)* → [smuggler6_3](#d-guild04_rebcomrade_3-smuggler6_3)
    - “Here's 100 gold.” *(if pay 100 gold)* → [smuggler6_2](#d-guild04_rebcomrade_3-smuggler6_2)

    <span id="d-guild04_rebcomrade_3-smuggler6_3"></span>**`smuggler6_3`** Zachlanny: “Is that all you have?”


    <span id="d-guild04_rebcomrade_3-smuggler6_2"></span>**`smuggler6_2`** Zachlanny: “Oh, oh! I haven't seen that much gold in my whole life. I'm finally rich!”




### Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added |
| [v0.8.8](../versions/0.8.8.md) | Attack chance: removed (was 110)<br>Attack cost: removed (was 5)<br>Attack damage: removed (was 5–10)<br>Block chance: removed (was 100)<br>Critical multiplier: removed (was 2)<br>Critical skill: removed (was 10)<br>Damage resistance: removed (was 2)<br>Loot table removed<br>Max HP: removed (was 70)<br>Move cost: removed (was 5)<br>(+1 more) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guild04_rebcomrade_3)"

    | | |
    |---|---|
    | Entry ID | `guild04_rebcomrade_3` |
    | Spawn group | `guild04_comrade_3` |
    | Loot table | – |
    | Conversation | `smuggler6_1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:65` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "guild04_rebcomrade_3",
     "name": "Zachlanny",
     "iconID": "monsters_ld1:65",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "guild04_comrade_3",
     "phraseID": "smuggler6_1"
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=aidem_camp_zachlanny.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=aidem_camp_zachlanny.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=aidem_camp_zachlanny.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=aidem_camp_zachlanny.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
