---
description: "Erwyn's soldier is an NPC who can also be fought in Andor's Trail, found in Stoutford, Prim, Flagstone Prison, Flagstone Prison, Stoutford, Flagstone Prison."
---

# ![](../assets/icons/monsters/monsters_tometik8_38.png){ .sprite } Erwyn's soldier

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik8_38.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Stoutford, Prim, Flagstone Prison, Flagstone Prison, Stoutford, Flagstone Prison |
| **Class** | Undead, Humanoid |
| **HP** | 65 |
| **XP when defeated** | 99 |
| **Entries in game data** | 3 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

!!! info "3 entries in the game data"
    The game's data files define 3 separate characters named Erwyn's soldier. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location, movement. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`erwyn_soldier`](#v-erwyn_soldier) | NPC/Enemy | Flagstone Prison: [stoutford_castle_tower0](../maps/stoutford_castle_tower0.md#pin-npc-erwyn_soldier), Flagstone Prison: [waytogalmore0](../maps/waytogalmore0.md#pin-npc-erwyn_soldier) (+6 more) | – | 65 |
| [`erwyn_soldier2`](#v-erwyn_soldier2) | NPC/Enemy | Flagstone Prison: [waytogalmore0](../maps/waytogalmore0.md#pin-npc-erwyn_soldier2), Flagstone Prison: [waytogalmore1](../maps/waytogalmore1.md#pin-npc-erwyn_soldier2) (+1 more) | – | 65 |
| [`erwyn_soldier3`](#v-erwyn_soldier3) | NPC/Enemy | Flagstone Prison: [waytogalmore1](../maps/waytogalmore1.md#pin-npc-erwyn_soldier3) | – | 65 |

## Flagstone Prison, Stoutford castle tower0 and 7 more (erwyn_soldier) { #v-erwyn_soldier }

**Entry ID:** `erwyn_soldier` · **Type:** NPC/Enemy

**Location:** Flagstone Prison: [stoutford_castle_tower0](../maps/stoutford_castle_tower0.md#pin-npc-erwyn_soldier), Flagstone Prison: [waytogalmore0](../maps/waytogalmore0.md#pin-npc-erwyn_soldier), Flagstone Prison: [waytogalmore1](../maps/waytogalmore1.md#pin-npc-erwyn_soldier), Flagstone Prison: [wild18](../maps/wild18.md#pin-npc-erwyn_soldier), Prim: [stoutford_castle_barrack2](../maps/stoutford_castle_barrack2.md#pin-npc-erwyn_soldier), Stoutford: [stoutford_castle_barrack0](../maps/stoutford_castle_barrack0.md#pin-npc-erwyn_soldier) (+2 more)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 65 |
| XP when defeated | 99 |
| Damage | 4 to 5 |
| Attack chance | 90 |
| Block chance | 60 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [stoutford_castle_barrack0](../maps/stoutford_castle_barrack0.md) | Stoutford | 2 | – |
| [stoutford_castle_barrack2](../maps/stoutford_castle_barrack2.md) | Prim | 2 | – |
| [stoutford_castle_tower0](../maps/stoutford_castle_tower0.md) | Flagstone Prison | 1 | – |
| [stoutford_tower4](../maps/stoutford_tower4.md) | – | 1 | – |
| [waytogalmore0](../maps/waytogalmore0.md) | Flagstone Prison | 2 | – |
| [waytogalmore1](../maps/waytogalmore1.md) | Flagstone Prison | 1 | – |
| [wild18](../maps/wild18.md) | Flagstone Prison | 1 | – |
| [wild22](../maps/wild22.md) | Stoutford | 3 | – |

### Quests that count defeats

- A conversation with [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) checks that at least 2 of these enemies have been defeated.
- [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-46) with stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md), stepping on a trigger on [wild18](../maps/wild18.md) checks that at least 13 of these enemies have been defeated.
- A conversation with [Colonel Lutarc](../monsters/stn_colonel.md) ([waytogalmore0](../maps/waytogalmore0.md)), stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) checks that this enemy has been defeated.

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Erwyn's soldier. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/stoutford_castle_1.json" data-npc="Erwyn&#x27;s soldier" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-erwyn_soldier-stoutford_castle_1"></span>**`stoutford_castle_1`** Erwyn's soldier: “What do I seee? A mortal? Your bonesss shall be clattering on the ground soon enoughhh!”

    - “How about you show me what that would look like?” → *fight starts*



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (erwyn_soldier)"

    | | |
    |---|---|
    | Entry ID | `erwyn_soldier` |
    | Spawn group | `erwyn_soldier` |
    | Loot table | – |
    | Conversation | `stoutford_castle_1` |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_tometik8:38` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "erwyn_soldier",
     "name": "Erwyn's soldier",
     "iconID": "monsters_tometik8:38",
     "maxHP": 65,
     "unique": 1,
     "monsterClass": "undead",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 4,
      "max": 5
     },
     "spawnGroup": "erwyn_soldier",
     "phraseID": "stoutford_castle_1",
     "attackCost": 3,
     "attackChance": 90,
     "blockChance": 60,
     "damageResistance": 0
    }
    ```


## Flagstone Prison, Waytogalmore0 and 2 more (erwyn_soldier2) { #v-erwyn_soldier2 }

**Entry ID:** `erwyn_soldier2` · **Type:** NPC/Enemy

**Location:** Flagstone Prison: [waytogalmore0](../maps/waytogalmore0.md#pin-npc-erwyn_soldier2), Flagstone Prison: [waytogalmore1](../maps/waytogalmore1.md#pin-npc-erwyn_soldier2), Stoutford: [wild22](../maps/wild22.md#pin-npc-erwyn_soldier2)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 65 |
| XP when defeated | 99 |
| Damage | 4 to 5 |
| Attack chance | 90 |
| Block chance | 60 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [waytogalmore0](../maps/waytogalmore0.md) | Flagstone Prison | 2 | – |
| [waytogalmore1](../maps/waytogalmore1.md) | Flagstone Prison | 2 | – |
| [wild22](../maps/wild22.md) | Stoutford | 3 | – |

### Quests that count defeats

- [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-46) with stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md), stepping on a trigger on [wild18](../maps/wild18.md) checks that at least 7 of these enemies have been defeated.

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Erwyn's soldier. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/stoutford_castle_1b.json" data-npc="Erwyn&#x27;s soldier" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-erwyn_soldier2-stoutford_castle_1b"></span>**`stoutford_castle_1b`** Erwyn's soldier: “Ah, your ssskull will be my favorite cup!”

    - “Yes, but I also like it very much. So I'd rather keep it.” → *fight starts*



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |
| [v0.8.9](../versions/0.8.9.md) | movementAggressionType: helpOthers → protectSpawn |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (erwyn_soldier2)"

    | | |
    |---|---|
    | Entry ID | `erwyn_soldier2` |
    | Spawn group | `erwyn_soldier2` |
    | Loot table | – |
    | Conversation | `stoutford_castle_1b` |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_tometik8:38` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "erwyn_soldier2",
     "name": "Erwyn's soldier",
     "iconID": "monsters_tometik8:38",
     "maxHP": 65,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 4,
      "max": 5
     },
     "spawnGroup": "erwyn_soldier2",
     "phraseID": "stoutford_castle_1b",
     "attackCost": 3,
     "attackChance": 90,
     "blockChance": 60,
     "damageResistance": 0
    }
    ```


## Flagstone Prison, Waytogalmore1 (erwyn_soldier3) { #v-erwyn_soldier3 }

**Entry ID:** `erwyn_soldier3` · **Type:** NPC/Enemy

**Location:** Flagstone Prison: [waytogalmore1](../maps/waytogalmore1.md#pin-npc-erwyn_soldier3)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 65 |
| XP when defeated | 99 |
| Damage | 4 to 5 |
| Attack chance | 90 |
| Block chance | 60 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [waytogalmore1](../maps/waytogalmore1.md) | Flagstone Prison | 4 | – |

### Quests that count defeats

- [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-46) with stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md), stepping on a trigger on [wild18](../maps/wild18.md) checks that at least 4 of these enemies have been defeated.

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Erwyn's soldier. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/stoutford_castle_1c.json" data-npc="Erwyn&#x27;s soldier" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-erwyn_soldier3-stoutford_castle_1c"></span>**`stoutford_castle_1c`** Erwyn's soldier: “Bonesss! Niccce little bonesss!!”

    - “But not for you, sorry.” → *fight starts*



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (erwyn_soldier3)"

    | | |
    |---|---|
    | Entry ID | `erwyn_soldier3` |
    | Spawn group | `erwyn_soldier3` |
    | Loot table | – |
    | Conversation | `stoutford_castle_1c` |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_tometik8:38` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "erwyn_soldier3",
     "name": "Erwyn's soldier",
     "iconID": "monsters_tometik8:38",
     "maxHP": 65,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 4,
      "max": 5
     },
     "spawnGroup": "erwyn_soldier3",
     "phraseID": "stoutford_castle_1c",
     "attackCost": 3,
     "attackChance": 90,
     "blockChance": 60,
     "damageResistance": 0
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn_soldier.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn_soldier.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn_soldier.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn_soldier.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
