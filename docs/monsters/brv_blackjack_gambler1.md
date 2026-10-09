---
description: "Gambler is an NPC who can also be fought in Andor's Trail, found in Brimhaven."
---

# ![](../assets/icons/monsters/monsters_ld1_133.png){ .sprite } Gambler

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_133.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Brimhaven |
| **Class** | Humanoid |
| **HP** | 25 |
| **XP when defeated** | 36–48 |
| **Entries in game data** | 4 |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

!!! info "4 entries in the game data"
    The game data defines 4 separate characters named Gambler. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation, combat statistics, loot or shop stock, appearance, movement. Each entry has its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`brv_blackjack_gambler1`](#v-brv_blackjack_gambler1) | NPC | Brimhaven: [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md#pin-npc-brv_blackjack_gambler1) | – | – |
| [`brv_blackjack_gambler1_evil`](#v-brv_blackjack_gambler1_evil) | Enemy | Brimhaven: [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md) | – | 25 |
| [`brv_blackjack_gambler2`](#v-brv_blackjack_gambler2) | NPC | Brimhaven: [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md#pin-npc-brv_blackjack_gambler2) | – | – |
| [`brv_blackjack_gambler2_evil`](#v-brv_blackjack_gambler2_evil) | Enemy | Brimhaven: [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md) | – | 25 |

## Brimhaven, Brimhaven tavern west back (brv_blackjack_gambler1) { #v-brv_blackjack_gambler1 }

**Entry ID:** `brv_blackjack_gambler1` · **Type:** NPC

**Location:** Brimhaven: [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md#pin-npc-brv_blackjack_gambler1)

### Dialogue simulator

Set your quest stages and items, then talk to Gambler. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/blackjack_gambler1.json" data-npc="Gambler" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_blackjack_gambler1-blackjack_gambler1"></span>**`blackjack_gambler1`** Gambler: “What a bad day. I was losing all the time.”




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brv_blackjack_gambler1)"

    | | |
    |---|---|
    | Entry ID | `brv_blackjack_gambler1` |
    | Spawn group | `brv_blackjack_gambler1` |
    | Loot table | – |
    | Conversation | `blackjack_gambler1` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_ld1:133` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_blackjack_gambler1",
     "name": "Gambler",
     "iconID": "monsters_ld1:133",
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "spawnGroup": "brv_blackjack_gambler1",
     "phraseID": "blackjack_gambler1"
    }
    ```


## Brimhaven, Brimhaven tavern west back (brv_blackjack_gambler1_evil) { #v-brv_blackjack_gambler1_evil }

**Entry ID:** `brv_blackjack_gambler1_evil` · **Type:** Enemy

**Location:** Brimhaven: [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 25 |
| XP when defeated | 36 |
| Damage | 1 to 3 |
| Attack chance | 70 |
| Block chance | 40 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 10 |
| Critical multiplier | 2.0 |
| Critical hit chance | 9% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 50 to 100 |
| [Cloth shirt](../items/shirt1.md) | 50% | 1 |
| [Iron dagger](../items/dagger0.md) | 50% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md) | Brimhaven | 1 | Appears later, during a quest |

### Quests that count defeats

- [Fair play?](../quests/brv_blackjack.md#stage-60) with [Guard](../monsters/guard.md#v-brv_tavern_west_guard) ([Brimhaven tavern west](../maps/brimhaven_tavern_west.md)), walking into a blocked passage on [Brimhaven tavern west](../maps/brimhaven_tavern_west.md) checks that this enemy has been defeated.
- [Fair play?](../quests/brv_blackjack.md#stage-60) with stepping on a trigger on [Brimhaven tavern west](../maps/brimhaven_tavern_west.md) checks that this enemy has been defeated.


### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brv_blackjack_gambler1_evil)"

    | | |
    |---|---|
    | Entry ID | `brv_blackjack_gambler1_evil` |
    | Spawn group | `brv_blackjack_gambler1_evil` |
    | Loot table | `brv_gambler` |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:133` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_blackjack_gambler1_evil",
     "name": "Gambler",
     "iconID": "monsters_ld1:133",
     "maxHP": 25,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 1,
      "max": 3
     },
     "spawnGroup": "brv_blackjack_gambler1_evil",
     "droplistID": "brv_gambler",
     "attackCost": 3,
     "attackChance": 70,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 40
    }
    ```


## Brimhaven, Brimhaven tavern west back (brv_blackjack_gambler2) { #v-brv_blackjack_gambler2 }

**Entry ID:** `brv_blackjack_gambler2` · **Type:** NPC

**Location:** Brimhaven: [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md#pin-npc-brv_blackjack_gambler2)

### Dialogue simulator

Set your quest stages and items, then talk to Gambler. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/blackjack_gambler2.json" data-npc="Gambler" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_blackjack_gambler2-blackjack_gambler2"></span>**`blackjack_gambler2`** Gambler: “I already made a fortune. Want to join us? Then take a seat in the empty chair and talk to the dealer.”

    - “Excuse me sir, but you look like someone that may be able to help me.” *(if reached stage 130 of [A strange looking dagger](../quests/brv_dagger.md#stage-130); NOT reached stage 200 of [A strange looking dagger](../quests/brv_dagger.md#stage-200); NOT reached stage 230 of [A strange looking dagger](../quests/brv_dagger.md#stage-230))* → [blackjack_gambler2_asd_10](#d-brv_blackjack_gambler2-blackjack_gambler2_asd_10)

    <span id="d-brv_blackjack_gambler2-blackjack_gambler2_asd_10"></span>**`blackjack_gambler2_asd_10`** Gambler: “What do you mean by "I look like someone that may be able to help"?”

    - “Um...I mean let's be honest, you may be someone who likes to play on the other side of the law.” → [blackjack_gambler2_asd_20](#d-brv_blackjack_gambler2-blackjack_gambler2_asd_20)

    <span id="d-brv_blackjack_gambler2-blackjack_gambler2_asd_20"></span>**`blackjack_gambler2_asd_20`** Gambler: “You got that right, kid. Now what do you want to know?”

    - “I'm wondering, do you know anything about Lawellyn's death?” → [blackjack_gambler2_asd_30](#d-brv_blackjack_gambler2-blackjack_gambler2_asd_30)

    <span id="d-brv_blackjack_gambler2-blackjack_gambler2_asd_30"></span>**`blackjack_gambler2_asd_30`** Gambler: “If you want to know about a murder, you should probably ask on the east side of town.”




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 1 line added |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 3 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brv_blackjack_gambler2)"

    | | |
    |---|---|
    | Entry ID | `brv_blackjack_gambler2` |
    | Spawn group | `brv_blackjack_gambler2` |
    | Loot table | – |
    | Conversation | `blackjack_gambler2` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_rltiles1:64` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_blackjack_gambler2",
     "name": "Gambler",
     "iconID": "monsters_rltiles1:64",
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "spawnGroup": "brv_blackjack_gambler2",
     "phraseID": "blackjack_gambler2"
    }
    ```


## Brimhaven, Brimhaven tavern west back (brv_blackjack_gambler2_evil) { #v-brv_blackjack_gambler2_evil }

**Entry ID:** `brv_blackjack_gambler2_evil` · **Type:** Enemy

**Location:** Brimhaven: [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 25 |
| XP when defeated | 48 |
| Damage | 1 to 5 |
| Attack chance | 80 |
| Block chance | 80 |
| Damage resistance | 1 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 50 to 100 |
| [Cloth shirt](../items/shirt1.md) | 50% | 1 |
| [Iron dagger](../items/dagger0.md) | 50% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md) | Brimhaven | 1 | Appears later, during a quest |

### Quests that count defeats

- [Fair play?](../quests/brv_blackjack.md#stage-60) with stepping on a trigger on [Brimhaven tavern west](../maps/brimhaven_tavern_west.md) checks that this enemy has been defeated.


### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brv_blackjack_gambler2_evil)"

    | | |
    |---|---|
    | Entry ID | `brv_blackjack_gambler2_evil` |
    | Spawn group | `brv_blackjack_gambler2_evil` |
    | Loot table | `brv_gambler` |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_rltiles1:64` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_blackjack_gambler2_evil",
     "name": "Gambler",
     "iconID": "monsters_rltiles1:64",
     "maxHP": 25,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 1,
      "max": 5
     },
     "spawnGroup": "brv_blackjack_gambler2_evil",
     "droplistID": "brv_gambler",
     "attackCost": 5,
     "attackChance": 80,
     "blockChance": 80,
     "damageResistance": 1
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_blackjack_gambler1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_blackjack_gambler1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_blackjack_gambler1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_blackjack_gambler1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
