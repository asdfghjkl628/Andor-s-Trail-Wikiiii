---
description: "Black fog is a non-player character (NPC) in Andor's Trail, found in Bogsten 4, Mushroom m 2 3, Mushroom m 2 6, Mushroom m 2 8, Mushroom m 3 1, Mywildcave 4."
---

# ![](../assets/icons/monsters/monsters_tometik3_44.png){ .sprite } Black fog

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik3_44.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Bogsten 4, Mushroom m 2 3, Mushroom m 2 6, Mushroom m 2 8, Mushroom m 3 1, Mywildcave 4 |
| **Entries in game data** | 5 |
| **Introduced** | [v0.7.13](../versions/0.7.13.md) |

</div>

!!! info "5 entries in the game data"
    The game data defines 5 separate characters named Black fog. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation, location. Each entry has its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`zuul_khan1_blocker`](#v-zuul_khan1_blocker) | NPC | [Bogsten 4](../maps/bogsten4.md#pin-npc-zuul_khan1_blocker) | – |
| [`zuul_khan2_blocker`](#v-zuul_khan2_blocker) | NPC | [Mushroom m 2 3](../maps/mushroom_m2_3.md#pin-npc-zuul_khan2_blocker) | – |
| [`zuul_khan3_blocker`](#v-zuul_khan3_blocker) | NPC | [Mushroom m 2 6](../maps/mushroom_m2_6.md#pin-npc-zuul_khan3_blocker) | – |
| [`zuul_khan4_blocker`](#v-zuul_khan4_blocker) | NPC | [Mushroom m 2 8](../maps/mushroom_m2_8.md#pin-npc-zuul_khan4_blocker) | – |
| [`zuul_khan9_blocker`](#v-zuul_khan9_blocker) | NPC | [Mushroom m 3 1](../maps/mushroom_m3_1.md#pin-npc-zuul_khan9_blocker), [Mywildcave 4](../maps/mywildcave4.md#pin-npc-zuul_khan9_blocker) | – |

## Bogsten 4 (zuul_khan1_blocker) { #v-zuul_khan1_blocker }

**Entry ID:** `zuul_khan1_blocker` · **Type:** NPC

**Location:** [Bogsten 4](../maps/bogsten4.md#pin-npc-zuul_khan1_blocker)

### Quests

- [Fungi panic](../quests/fungi_panic.md): stage 161

### Dialogue simulator

Set your quest stages and items, then talk to Black fog. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/zuul_khan1_blocker.json" data-npc="Black fog" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-zuul_khan1_blocker-zuul_khan1_blocker"></span>**`zuul_khan1_blocker`** Black fog: “You shall not pass.”

    - “Your foul master is gone.” *(if killed 1× [Zuul'khan](../monsters/zuul_khan.md))* → [zuul_khan1_blocker_10](#d-zuul_khan1_blocker-zuul_khan1_blocker_10)
    - “[Lie] Your master has told me to go here. Out of my way now!” *(if reached stage 155 of [Fungi panic](../quests/fungi_panic.md#stage-155))* → [zuul_khan1_blocker_10](#d-zuul_khan1_blocker-zuul_khan1_blocker_10)
    - “For now.” → *conversation ends*

    <span id="d-zuul_khan1_blocker-zuul_khan1_blocker_10"></span>**`zuul_khan1_blocker_10`** [Dummy NPC](../monsters/none.md): “The black fog hisses and instantly vanishes.” — **effects:** removes monsters from bogsten4, removes monsters from bogsten4, sets stage 161 of [Fungi panic](../quests/fungi_panic.md#stage-161)

    - “Oh, that was easy.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (zuul_khan1_blocker)"

    | | |
    |---|---|
    | Entry ID | `zuul_khan1_blocker` |
    | Spawn group | `zuul_khan1_blocker` |
    | Loot table | – |
    | Conversation | `zuul_khan1_blocker` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik3:44` |
    | Defined in | `res/raw/monsterlist_fungi_panic.json` |

    Raw data:

    ```json
    {
     "id": "zuul_khan1_blocker",
     "name": "Black fog",
     "iconID": "monsters_tometik3:44",
     "moveCost": 5,
     "monsterClass": "animal",
     "spawnGroup": "zuul_khan1_blocker",
     "phraseID": "zuul_khan1_blocker"
    }
    ```


## Mushroom m 2 3 (zuul_khan2_blocker) { #v-zuul_khan2_blocker }

**Entry ID:** `zuul_khan2_blocker` · **Type:** NPC

**Location:** [Mushroom m 2 3](../maps/mushroom_m2_3.md#pin-npc-zuul_khan2_blocker)

### Quests

- [Fungi panic](../quests/fungi_panic.md): stage 162

### Dialogue simulator

Set your quest stages and items, then talk to Black fog. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/zuul_khan2_blocker.json" data-npc="Black fog" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-zuul_khan2_blocker-zuul_khan2_blocker"></span>**`zuul_khan2_blocker`** Black fog: “You shall not pass.”

    - “Your foul master is gone again...” *(if killed 1× [Zuul'khan](../monsters/zuul_khan.md#v-zuul_khan2))* → [zuul_khan2_blocker_10](#d-zuul_khan2_blocker-zuul_khan2_blocker_10)
    - “I think I have seen you before...” → *conversation ends*

    <span id="d-zuul_khan2_blocker-zuul_khan2_blocker_10"></span>**`zuul_khan2_blocker_10`** [Dummy NPC](../monsters/none.md): “The black fog hisses and instantly vanishes.” — **effects:** removes monsters from mushroom_m2_3, sets stage 162 of [Fungi panic](../quests/fungi_panic.md#stage-162)

    - “Yes, now I remember.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (zuul_khan2_blocker)"

    | | |
    |---|---|
    | Entry ID | `zuul_khan2_blocker` |
    | Spawn group | `zuul_khan2_blocker` |
    | Loot table | – |
    | Conversation | `zuul_khan2_blocker` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik3:44` |
    | Defined in | `res/raw/monsterlist_fungi_panic.json` |

    Raw data:

    ```json
    {
     "id": "zuul_khan2_blocker",
     "name": "Black fog",
     "iconID": "monsters_tometik3:44",
     "moveCost": 5,
     "monsterClass": "animal",
     "spawnGroup": "zuul_khan2_blocker",
     "phraseID": "zuul_khan2_blocker"
    }
    ```


## Mushroom m 2 6 (zuul_khan3_blocker) { #v-zuul_khan3_blocker }

**Entry ID:** `zuul_khan3_blocker` · **Type:** NPC

**Location:** [Mushroom m 2 6](../maps/mushroom_m2_6.md#pin-npc-zuul_khan3_blocker)

### Quests

- [Fungi panic](../quests/fungi_panic.md): stage 163

### Dialogue simulator

Set your quest stages and items, then talk to Black fog. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/zuul_khan3_blocker.json" data-npc="Black fog" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-zuul_khan3_blocker-zuul_khan3_blocker"></span>**`zuul_khan3_blocker`** Black fog: “You shall not pass.”

    - “Your foul master is once more gone...” *(if killed 1× [Zuul'khan](../monsters/zuul_khan.md#v-zuul_khan3))* → [zuul_khan3_blocker_10](#d-zuul_khan3_blocker-zuul_khan3_blocker_10)
    - “Sigh.” → *conversation ends*

    <span id="d-zuul_khan3_blocker-zuul_khan3_blocker_10"></span>**`zuul_khan3_blocker_10`** [Dummy NPC](../monsters/none.md): “The black fog hisses and instantly vanishes.” — **effects:** removes monsters from mushroom_m2_6, sets stage 163 of [Fungi panic](../quests/fungi_panic.md#stage-163)

    - “Great.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (zuul_khan3_blocker)"

    | | |
    |---|---|
    | Entry ID | `zuul_khan3_blocker` |
    | Spawn group | `zuul_khan3_blocker` |
    | Loot table | – |
    | Conversation | `zuul_khan3_blocker` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik3:44` |
    | Defined in | `res/raw/monsterlist_fungi_panic.json` |

    Raw data:

    ```json
    {
     "id": "zuul_khan3_blocker",
     "name": "Black fog",
     "iconID": "monsters_tometik3:44",
     "moveCost": 5,
     "monsterClass": "animal",
     "spawnGroup": "zuul_khan3_blocker",
     "phraseID": "zuul_khan3_blocker"
    }
    ```


## Mushroom m 2 8 (zuul_khan4_blocker) { #v-zuul_khan4_blocker }

**Entry ID:** `zuul_khan4_blocker` · **Type:** NPC

**Location:** [Mushroom m 2 8](../maps/mushroom_m2_8.md#pin-npc-zuul_khan4_blocker)

### Quests

- [Fungi panic](../quests/fungi_panic.md): stage 164

### Dialogue simulator

Set your quest stages and items, then talk to Black fog. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/zuul_khan4_blocker.json" data-npc="Black fog" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-zuul_khan4_blocker-zuul_khan4_blocker"></span>**`zuul_khan4_blocker`** Black fog: “You shall not pass.”

    - “Oh my. How often?” *(if killed 1× [Zuul'khan](../monsters/zuul_khan.md#v-zuul_khan4))* → [zuul_khan4_blocker_10](#d-zuul_khan4_blocker-zuul_khan4_blocker_10)
    - “Sigh.” → *conversation ends*

    <span id="d-zuul_khan4_blocker-zuul_khan4_blocker_10"></span>**`zuul_khan4_blocker_10`** [Dummy NPC](../monsters/none.md): “The black fog hisses and instantly vanishes.” — **effects:** removes monsters from mushroom_m2_8, sets stage 164 of [Fungi panic](../quests/fungi_panic.md#stage-164)

    - “You could be a little more varied.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (zuul_khan4_blocker)"

    | | |
    |---|---|
    | Entry ID | `zuul_khan4_blocker` |
    | Spawn group | `zuul_khan4_blocker` |
    | Loot table | – |
    | Conversation | `zuul_khan4_blocker` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik3:44` |
    | Defined in | `res/raw/monsterlist_fungi_panic.json` |

    Raw data:

    ```json
    {
     "id": "zuul_khan4_blocker",
     "name": "Black fog",
     "iconID": "monsters_tometik3:44",
     "moveCost": 5,
     "monsterClass": "animal",
     "spawnGroup": "zuul_khan4_blocker",
     "phraseID": "zuul_khan4_blocker"
    }
    ```


## Mushroom m 3 1 and 1 more (zuul_khan9_blocker) { #v-zuul_khan9_blocker }

**Entry ID:** `zuul_khan9_blocker` · **Type:** NPC

**Location:** [Mushroom m 3 1](../maps/mushroom_m3_1.md#pin-npc-zuul_khan9_blocker), [Mywildcave 4](../maps/mywildcave4.md#pin-npc-zuul_khan9_blocker)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Mushroom m 3 1](../maps/mushroom_m3_1.md) | – | 1 | – |
| [Mywildcave 4](../maps/mywildcave4.md) | – | 1 | – |

### Quests

- [Fungi panic](../quests/fungi_panic.md): stages 169, 170

### Dialogue simulator

Set your quest stages and items, then talk to Black fog. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/zuul_khan9_blocker.json" data-npc="Black fog" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-zuul_khan9_blocker-zuul_khan9_blocker"></span>**`zuul_khan9_blocker`** Black fog: “You shall not pass.”

    - “Your master is dead. Begone!” *(if killed 1× [Zuul'khan](../monsters/zuul_khan.md#v-zuul_khan9); NOT killed 1× [Zuul'khan](../monsters/zuul_khan.md#v-gison_thiefboss))* → [zuul_khan9_blocker_20](#d-zuul_khan9_blocker-zuul_khan9_blocker_20)
    - “Your master is dead forever now. Begone!” *(if killed 1× [Zuul'khan](../monsters/zuul_khan.md#v-gison_thiefboss))* → [zuul_khan9_blocker_10](#d-zuul_khan9_blocker-zuul_khan9_blocker_10)
    - “Why me? What have I done to deserve this?” → *conversation ends*

    <span id="d-zuul_khan9_blocker-zuul_khan9_blocker_20"></span>**`zuul_khan9_blocker_20`** Black fog: “No. We were expecting you to say so. We were told not to leave.” — **effects:** sets stage 169 of [Fungi panic](../quests/fungi_panic.md#stage-169)

    - “I need to know what's behind this, but obviously I can't get past that way. I had best try to find another way.” *(if NOT reached stage 40 of [A raid for a cookbook](../quests/gison_cookbook.md#stage-40))* → *conversation ends*
    - “Well, you are learning.” → *conversation ends*

    <span id="d-zuul_khan9_blocker-zuul_khan9_blocker_10"></span>**`zuul_khan9_blocker_10`** [Dummy NPC](../monsters/none.md): “The black fog hisses and instantly vanishes.” — **effects:** removes monsters from mywildcave4, removes monsters from mushroom_m3_1, sets stage 170 of [Fungi panic](../quests/fungi_panic.md#stage-170)

    - “At last.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (zuul_khan9_blocker)"

    | | |
    |---|---|
    | Entry ID | `zuul_khan9_blocker` |
    | Spawn group | `zuul_khan9_blocker` |
    | Loot table | – |
    | Conversation | `zuul_khan9_blocker` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik3:44` |
    | Defined in | `res/raw/monsterlist_fungi_panic.json` |

    Raw data:

    ```json
    {
     "id": "zuul_khan9_blocker",
     "name": "Black fog",
     "iconID": "monsters_tometik3:44",
     "moveCost": 5,
     "monsterClass": "animal",
     "spawnGroup": "zuul_khan9_blocker",
     "phraseID": "zuul_khan9_blocker"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=zuul_khan1_blocker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=zuul_khan1_blocker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=zuul_khan1_blocker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=zuul_khan1_blocker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
