---
description: "Lord Erwyn is an NPC who can also be fought in Andor's Trail, found in Flagstone Prison."
---

# ![](../assets/icons/monsters/monsters_tometik8_46.png){ .sprite } Lord Erwyn

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik8_46.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Flagstone Prison |
| **Class** | Undead |
| **HP** | 110 |
| **XP when defeated** | 373 |
| **Entries in game data** | 2 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

!!! info "2 entries in the game data"
    The game data defines 2 separate characters named Lord Erwyn. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: loot or shop stock. Each entry has its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`erwyn`](#v-erwyn) | NPC/Enemy | Flagstone Prison: [Stoutford castle 0](../maps/stoutford_castle0.md#pin-npc-erwyn) | – | 110 |
| [`erwyn2`](#v-erwyn2) | NPC/Enemy | Flagstone Prison: [Stoutford castle 0](../maps/stoutford_castle0.md#pin-npc-erwyn2) | – | 110 |

## Flagstone Prison, Stoutford castle 0 (erwyn) { #v-erwyn }

**Entry ID:** `erwyn` · **Type:** NPC/Enemy

**Location:** Flagstone Prison: [Stoutford castle 0](../maps/stoutford_castle0.md#pin-npc-erwyn)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 110 |
| XP when defeated | 373 |
| Damage | 13 to 22 |
| Attack chance | 130 |
| Block chance | 80 |
| Damage resistance | 5 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 20 |
| Critical multiplier | 3.0 |
| Critical hit chance | 15% |

**On hit:** Heal HP: 3; On target: [Weak Poison](../conditions/poison_weak.md) (magnitude 2, 4 rounds, 40% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Stoutford castle 0](../maps/stoutford_castle0.md) | Flagstone Prison | 1 | – |

### Quests that count defeats

- A conversation with [Tahalendor](../monsters/tahalendor.md) ([Stoutford church](../maps/stoutford_church.md)) checks that this enemy has been defeated.
- A conversation with stepping on a trigger on [Stoutford castle 0](../maps/stoutford_castle0.md) checks that this enemy has been defeated.
- [Stoutford's old castle](../quests/stoutford_castle.md#stage-5) with stepping on a trigger on [Stoutford castle 0](../maps/stoutford_castle0.md) checks that at least 2 of these enemies have been defeated.

### Quests

- [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md): stages 48, 148

### Dialogue simulator

Set your quest stages and items, then talk to Lord Erwyn. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stoutford_castle_3.json" data-npc="Lord Erwyn" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (9 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-erwyn-stoutford_castle_3"></span>**`stoutford_castle_3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 148 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-148); reached stage 49 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-49))* → [stoutford_castle_3_2](#d-erwyn-stoutford_castle_3_2)
    - branch 2 *(if reached stage 148 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-148))* → [stoutford_castle_3a](#d-erwyn-stoutford_castle_3a)
    - branch 3 → [stoutford_castle_3_1](#d-erwyn-stoutford_castle_3_1)

    <span id="d-erwyn-stoutford_castle_3_2"></span>**`stoutford_castle_3_2`** [Lord Erwyn](../monsters/erwyn.md#v-erwyn2): “Did you come to serve me? On your knees!”

    - “What would I gain from that?” → [stoutford_castle_3b](#d-erwyn-stoutford_castle_3b)
    - “You are very rude and poorly educated. Maybe I should introduce myself? $playername is my name.” → [stoutford_castle_3c](#d-erwyn-stoutford_castle_3c)
    - “I will serve you - my weapon. Attack!” → [stoutford_castle_5](#d-erwyn-stoutford_castle_5)

    <span id="d-erwyn-stoutford_castle_3a"></span>**`stoutford_castle_3a`** [Lord Erwyn](../monsters/erwyn.md): “Did you come to serve me? On your knees!”

    - “What would I gain from that?” → [stoutford_castle_3b](#d-erwyn-stoutford_castle_3b)
    - “You are very rude and poorly educated. Maybe I should introduce myself? $playername is my name.” → [stoutford_castle_3c](#d-erwyn-stoutford_castle_3c)
    - “I will serve you - my weapon. Attack!” → [stoutford_castle_5](#d-erwyn-stoutford_castle_5)

    <span id="d-erwyn-stoutford_castle_3_1"></span>**`stoutford_castle_3_1`** [Dummy NPC](../monsters/none.md): “You see a heavily armed and cloaked skeleton moving towards you. This must be Lord Erwyn himself.” — **effects:** sets stage 148 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-148)

    - Next → [stoutford_castle_3_1a](#d-erwyn-stoutford_castle_3_1a)

    <span id="d-erwyn-stoutford_castle_3b"></span>**`stoutford_castle_3b`** Lord Erwyn: “Gain? I am the one who gains!”

    - “No, that's not acceptable. Do you have anything better to offer?” → [stoutford_castle_4](#d-erwyn-stoutford_castle_4)

    <span id="d-erwyn-stoutford_castle_3c"></span>**`stoutford_castle_3c`** Lord Erwyn: “Your name does not matter. Are you going to kneel now?”

    - “No. The floor is not clean here.” → [stoutford_castle_4](#d-erwyn-stoutford_castle_4)

    <span id="d-erwyn-stoutford_castle_5"></span>**`stoutford_castle_5`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 48 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-48)

    - branch 1 → *fight starts*

    <span id="d-erwyn-stoutford_castle_3_1a"></span>**`stoutford_castle_3_1a`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 49 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-49))* → [stoutford_castle_3_2](#d-erwyn-stoutford_castle_3_2)
    - branch 2 → [stoutford_castle_3a](#d-erwyn-stoutford_castle_3a)

    <span id="d-erwyn-stoutford_castle_4"></span>**`stoutford_castle_4`** Lord Erwyn: “You shall die now mortal!”

    - “No, you are going to die once and for all!” → [stoutford_castle_5](#d-erwyn-stoutford_castle_5)
    - “For the Shadow!” → [stoutford_castle_5](#d-erwyn-stoutford_castle_5)



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 9 lines added |
| [v0.7.4](../versions/0.7.4.md) | Attack cost: 53 → 5<br>Attack damage: 5–7 → 13–22<br>Damage resistance: added (5)<br>On hit, HP restored: added (3) |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 1 line changed<br>· text: “Gain? I am the the one who gains!” → “Gain? I am the one who gains!” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (erwyn)"

    | | |
    |---|---|
    | Entry ID | `erwyn` |
    | Spawn group | `erwyn` |
    | Loot table | – |
    | Conversation | `stoutford_castle_3` |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_tometik8:46` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "erwyn",
     "name": "Lord Erwyn",
     "iconID": "monsters_tometik8:46",
     "maxHP": 110,
     "unique": 1,
     "monsterClass": "undead",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 13,
      "max": 22
     },
     "spawnGroup": "erwyn",
     "phraseID": "stoutford_castle_3",
     "attackCost": 5,
     "attackChance": 130,
     "criticalSkill": 20,
     "criticalMultiplier": 3.0,
     "blockChance": 80,
     "damageResistance": 5,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 3,
       "max": 3
      },
      "conditionsTarget": [
       {
        "condition": "poison_weak",
        "magnitude": 2,
        "duration": 4,
        "chance": "40"
       }
      ]
     }
    }
    ```


## Flagstone Prison, Stoutford castle 0 (erwyn2) { #v-erwyn2 }

**Entry ID:** `erwyn2` · **Type:** NPC/Enemy

**Location:** Flagstone Prison: [Stoutford castle 0](../maps/stoutford_castle0.md#pin-npc-erwyn2)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 110 |
| XP when defeated | 373 |
| Damage | 13 to 22 |
| Attack chance | 130 |
| Block chance | 80 |
| Damage resistance | 5 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 20 |
| Critical multiplier | 3.0 |
| Critical hit chance | 15% |

**On hit:** Heal HP: 3; On target: [Weak Poison](../conditions/poison_weak.md) (magnitude 2, 4 rounds, 40% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Lord Erwyn's ring](../items/erwyn_ring.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Stoutford castle 0](../maps/stoutford_castle0.md) | Flagstone Prison | 1 | Appears later, during a quest |

### Quests that count defeats

- A conversation with stepping on a trigger on [Stoutford castle 0](../maps/stoutford_castle0.md) checks that this enemy has been defeated.
- A conversation with [Yolgen](../monsters/yolgen.md) ([Stoutford church](../maps/stoutford_church.md)) checks that this enemy has been defeated.
- [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-47) with stepping on a trigger on [Waytogalmore 0](../maps/waytogalmore0.md), stepping on a trigger on [Wild 18](../maps/wild18.md) checks that this enemy has been defeated.

### Quests

- [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md): stages 48, 148

### Dialogue simulator

Set your quest stages and items, then talk to Lord Erwyn. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stoutford_castle_3.json" data-npc="Lord Erwyn" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [stoutford_castle_3](#d-erwyn-stoutford_castle_3).


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 9 lines added |
| [v0.7.4](../versions/0.7.4.md) | Attack cost: 53 → 5<br>Attack damage: 5–7 → 13–22<br>Damage resistance: added (5)<br>On hit, HP restored: added (3) |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 1 line changed<br>· text: “Gain? I am the the one who gains!” → “Gain? I am the one who gains!” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (erwyn2)"

    | | |
    |---|---|
    | Entry ID | `erwyn2` |
    | Spawn group | `erwyn2` |
    | Loot table | `erwyn` |
    | Conversation | `stoutford_castle_3` |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_tometik8:46` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "erwyn2",
     "name": "Lord Erwyn",
     "iconID": "monsters_tometik8:46",
     "maxHP": 110,
     "unique": 1,
     "monsterClass": "undead",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 13,
      "max": 22
     },
     "spawnGroup": "erwyn2",
     "phraseID": "stoutford_castle_3",
     "droplistID": "erwyn",
     "attackCost": 5,
     "attackChance": 130,
     "criticalSkill": 20,
     "criticalMultiplier": 3.0,
     "blockChance": 80,
     "damageResistance": 5,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 3,
       "max": 3
      },
      "conditionsTarget": [
       {
        "condition": "poison_weak",
        "magnitude": 2,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
