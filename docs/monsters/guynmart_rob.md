---
description: "Rob is a non-player character (NPC) in Andor's Trail, found in Guynmart Castle."
---

# ![](../assets/icons/monsters/monsters_ld1_62.png){ .sprite } Rob

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_62.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Guynmart Castle |
| **Entries in game data** | 6 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

!!! info "6 entries in the game data"
    The game data defines 6 separate characters named Rob. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation, location. Each entry has its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`guynmart_rob`](#v-guynmart_rob) | NPC | Guynmart Castle: [Guynmart main 3](../maps/guynmart_main_3.md#pin-npc-guynmart_rob) | – |
| [`guynmart_rob2`](#v-guynmart_rob2) | NPC | Guynmart Castle: [Guynmart](../maps/guynmart.md#pin-npc-guynmart_rob2) | – |
| [`guynmart_rob3`](#v-guynmart_rob3) | NPC | Guynmart Castle: [Guynmart tower 3](../maps/guynmart_tower_3.md#pin-npc-guynmart_rob3) | – |
| [`guynmart_rob4`](#v-guynmart_rob4) | NPC | Guynmart Castle: [Guynmart tower 2](../maps/guynmart_tower_2.md#pin-npc-guynmart_rob4) | – |
| [`guynmart_rob5`](#v-guynmart_rob5) | NPC | Guynmart Castle: [Guynmart wood 6](../maps/guynmart_wood_6.md#pin-npc-guynmart_rob5) | – |
| [`guynmart_rob6`](#v-guynmart_rob6) | NPC | Guynmart Castle: [Guynmart wood 7](../maps/guynmart_wood_7.md#pin-npc-guynmart_rob6) | – |

## Guynmart Castle, Guynmart main 3 (guynmart_rob) { #v-guynmart_rob }

**Entry ID:** `guynmart_rob` · **Type:** NPC

**Location:** Guynmart Castle: [Guynmart main 3](../maps/guynmart_main_3.md#pin-npc-guynmart_rob)

### Quests

- [Roses](../quests/guynmart.md): stage 45
- [Guynmart Castle shutters (hidden flag)](../quests/guynmart_qRpl_shutters.md): stage 1

### Dialogue simulator

Set your quest stages and items, then talk to Rob. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_rob_10.json" data-npc="Rob" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (8 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_rob-guynmart_rob_10"></span>**`guynmart_rob_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 1 of [Guynmart Castle shutters (hidden flag)](../quests/guynmart_qRpl_shutters.md#stage-1))* → [guynmart_rob_50](#d-guynmart_rob-guynmart_rob_50)
    - branch 2 → [guynmart_rob_12](#d-guynmart_rob-guynmart_rob_12)

    <span id="d-guynmart_rob-guynmart_rob_50"></span>**`guynmart_rob_50`** Rob: “Hi $playername! We could play together in the tower. It is so boring here as the only kid.”

    - “Hmm. Maybe later. I have to go now.” → *conversation ends*
    - “Sorry. I am too old to play childish games. Please leave me alone.” → [guynmart_rob_52](#d-guynmart_rob-guynmart_rob_52)
    - “Where is your father?” → [guynmart_rob_60](#d-guynmart_rob-guynmart_rob_60)
    - “Where is Hannah?” → [guynmart_rob_70](#d-guynmart_rob-guynmart_rob_70)

    <span id="d-guynmart_rob-guynmart_rob_12"></span>**`guynmart_rob_12`** Rob: “Hey - you found me at last! That was fun! I am Robalyrius, Guynmart's son, but please call me Rob. Who are you? Wait, I will open the shutters, so that we can see each other.” — **effects:** sets stage 1 of [Guynmart Castle shutters (hidden flag)](../quests/guynmart_qRpl_shutters.md#stage-1), sets stage 45 of [Roses](../quests/guynmart.md#stage-45)

    - “Hi, I am $playername. I am glad that you are not really a ghost.” → *conversation ends*

    <span id="d-guynmart_rob-guynmart_rob_52"></span>**`guynmart_rob_52`** Rob: “No problem, see you later.”

    - “I hope not.” → *NPC leaves*

    <span id="d-guynmart_rob-guynmart_rob_60"></span>**`guynmart_rob_60`** Rob: “I don't know myself. He has been uproad for a week now. But he often is, so this is not unusual. I hope that he will take me with him on such missions.”

    - “And where is Hannah?” → [guynmart_rob_70](#d-guynmart_rob-guynmart_rob_70)

    <span id="d-guynmart_rob-guynmart_rob_70"></span>**`guynmart_rob_70`** Rob: “My sister is not in her room. She is probably at the top of the tower again, watching for a sign of Lovis.”

    - Next → [guynmart_rob_72](#d-guynmart_rob-guynmart_rob_72)

    <span id="d-guynmart_rob-guynmart_rob_72"></span>**`guynmart_rob_72`** Rob: “They want to marry, but a few days ago he vanished and has not returned. Hannah now weeps all the time. I hope for Lovis that he has a good reason for making my sister so sad.”

    - Next → [guynmart_rob_80](#d-guynmart_rob-guynmart_rob_80)

    <span id="d-guynmart_rob-guynmart_rob_80"></span>**`guynmart_rob_80`** Rob: “Maybe you should speak to Hannah's maiden? She is in the next room.”




### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 8 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_rob)"

    | | |
    |---|---|
    | Entry ID | `guynmart_rob` |
    | Spawn group | `guynmart_rob` |
    | Loot table | – |
    | Conversation | `guynmart_rob_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:62` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_rob",
     "name": "Rob",
     "iconID": "monsters_ld1:62",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_rob_10"
    }
    ```


## Guynmart Castle, Guynmart (guynmart_rob2) { #v-guynmart_rob2 }

**Entry ID:** `guynmart_rob2` · **Type:** NPC

**Location:** Guynmart Castle: [Guynmart](../maps/guynmart.md#pin-npc-guynmart_rob2)

### Dialogue simulator

Set your quest stages and items, then talk to Rob. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_rob2_10.json" data-npc="Rob" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_rob2-guynmart_rob2_10"></span>**`guynmart_rob2_10`** Rob: “I am throwing little pebbles at the guard down there. Do you want to try too?”

    - “You shouldn't do that, you naughty boy.” → *conversation ends*
    - “Here, take a few bigger rocks. That guard has earned it.” *(if hand over 6× [Small rock](../items/rock.md))* → [guynmart_rob2_12](#d-guynmart_rob2-guynmart_rob2_12)

    <span id="d-guynmart_rob2-guynmart_rob2_12"></span>**`guynmart_rob2_12`** Rob: “[6 rocks taken] Great! Let's see if I can knock his helmet off...”




### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_rob2)"

    | | |
    |---|---|
    | Entry ID | `guynmart_rob2` |
    | Spawn group | `guynmart_rob2` |
    | Loot table | – |
    | Conversation | `guynmart_rob2_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:62` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_rob2",
     "name": "Rob",
     "iconID": "monsters_ld1:62",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_rob2_10"
    }
    ```


## Guynmart Castle, Guynmart tower 3 (guynmart_rob3) { #v-guynmart_rob3 }

**Entry ID:** `guynmart_rob3` · **Type:** NPC

**Location:** Guynmart Castle: [Guynmart tower 3](../maps/guynmart_tower_3.md#pin-npc-guynmart_rob3)

### Quests

- [Roses](../quests/guynmart.md): stage 110

### Dialogue simulator

Set your quest stages and items, then talk to Rob. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_rob3_10.json" data-npc="Rob" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_rob3-guynmart_rob3_10"></span>**`guynmart_rob3_10`** Rob: “What shall we play now?”

    - “I want to go to the dungeon.” → [guynmart_rob3_20](#d-guynmart_rob3-guynmart_rob3_20)

    <span id="d-guynmart_rob3-guynmart_rob3_20"></span>**`guynmart_rob3_20`** Rob: “The guards would not let us. But I could help you.”

    - Next → [guynmart_rob3_30](#d-guynmart_rob3-guynmart_rob3_30)

    <span id="d-guynmart_rob3-guynmart_rob3_30"></span>**`guynmart_rob3_30`** Rob: “I will distract the guards, while you slip down the stairway, OK?”

    - “Great idea.” → [guynmart_rob3_40](#d-guynmart_rob3-guynmart_rob3_40)

    <span id="d-guynmart_rob3-guynmart_rob3_40"></span>**`guynmart_rob3_40`** Rob: “Follow me in a minute - but make no noise.” — **effects:** sets stage 110 of [Roses](../quests/guynmart.md#stage-110), spawns monsters on guynmart_tower_2, removes monsters from guynmart_tower_3

    - “OK.” → *NPC leaves*



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_rob3)"

    | | |
    |---|---|
    | Entry ID | `guynmart_rob3` |
    | Spawn group | `guynmart_rob3` |
    | Loot table | – |
    | Conversation | `guynmart_rob3_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:62` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_rob3",
     "name": "Rob",
     "iconID": "monsters_ld1:62",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_rob3_10"
    }
    ```


## Guynmart Castle, Guynmart tower 2 (guynmart_rob4) { #v-guynmart_rob4 }

**Entry ID:** `guynmart_rob4` · **Type:** NPC

**Location:** Guynmart Castle: [Guynmart tower 2](../maps/guynmart_tower_2.md#pin-npc-guynmart_rob4)

### Dialogue simulator

Set your quest stages and items, then talk to Rob. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_rob4_10.json" data-npc="Rob" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_rob4-guynmart_rob4_10"></span>**`guynmart_rob4_10`** Rob: “Quick! Downstairs!”




### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_rob4)"

    | | |
    |---|---|
    | Entry ID | `guynmart_rob4` |
    | Spawn group | `guynmart_rob4` |
    | Loot table | – |
    | Conversation | `guynmart_rob4_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:62` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_rob4",
     "name": "Rob",
     "iconID": "monsters_ld1:62",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_rob4_10"
    }
    ```


## Guynmart Castle, Guynmart wood 6 (guynmart_rob5) { #v-guynmart_rob5 }

**Entry ID:** `guynmart_rob5` · **Type:** NPC

**Location:** Guynmart Castle: [Guynmart wood 6](../maps/guynmart_wood_6.md#pin-npc-guynmart_rob5)

### Quests

- [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md): stage 50

### Dialogue simulator

Set your quest stages and items, then talk to Rob. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_rob5_10.json" data-npc="Rob" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (9 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_rob5-guynmart_rob5_10"></span>**`guynmart_rob5_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 59 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-59))* → [guynmart_rob5_59](#d-guynmart_rob5-guynmart_rob5_59)
    - branch 2 *(if reached stage 55 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-55))* → [guynmart_rob5_55](#d-guynmart_rob5-guynmart_rob5_55)
    - branch 3 *(if reached stage 54 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-54))* → [guynmart_rob5_54](#d-guynmart_rob5-guynmart_rob5_54)
    - branch 4 *(if reached stage 53 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-53))* → [guynmart_rob5_53](#d-guynmart_rob5-guynmart_rob5_53)
    - branch 5 *(if reached stage 52 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-52))* → [guynmart_rob5_52](#d-guynmart_rob5-guynmart_rob5_52)
    - branch 6 *(if reached stage 50 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-50))* → [guynmart_rob5_51](#d-guynmart_rob5-guynmart_rob5_51)
    - branch 7 → [guynmart_rob5_20](#d-guynmart_rob5-guynmart_rob5_20)

    <span id="d-guynmart_rob5-guynmart_rob5_59"></span>**`guynmart_rob5_59`** Rob: “Back to normal.”


    <span id="d-guynmart_rob5-guynmart_rob5_55"></span>**`guynmart_rob5_55`** Rob: “This is strange!”


    <span id="d-guynmart_rob5-guynmart_rob5_54"></span>**`guynmart_rob5_54`** Rob: “I don't even know what this is supposed to be!”


    <span id="d-guynmart_rob5-guynmart_rob5_53"></span>**`guynmart_rob5_53`** Rob: “A little too hot for my taste.”


    <span id="d-guynmart_rob5-guynmart_rob5_52"></span>**`guynmart_rob5_52`** Rob: “I like the clearing best this way.”


    <span id="d-guynmart_rob5-guynmart_rob5_51"></span>**`guynmart_rob5_51`** Rob: “Cool place here, isn't it?”


    <span id="d-guynmart_rob5-guynmart_rob5_20"></span>**`guynmart_rob5_20`** Rob: “Hey! You are the first one that has found the way to my clearing!”

    - Next → [guynmart_rob5_30](#d-guynmart_rob5-guynmart_rob5_30)

    <span id="d-guynmart_rob5-guynmart_rob5_30"></span>**`guynmart_rob5_30`** Rob: “I like this place very much. Each time I return here, I get a surprise.” — **effects:** sets stage 50 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-50)




### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 9 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_rob5)"

    | | |
    |---|---|
    | Entry ID | `guynmart_rob5` |
    | Spawn group | `guynmart_rob5` |
    | Loot table | – |
    | Conversation | `guynmart_rob5_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:62` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_rob5",
     "name": "Rob",
     "iconID": "monsters_ld1:62",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_rob5_10"
    }
    ```


## Guynmart Castle, Guynmart wood 7 (guynmart_rob6) { #v-guynmart_rob6 }

**Entry ID:** `guynmart_rob6` · **Type:** NPC

**Location:** Guynmart Castle: [Guynmart wood 7](../maps/guynmart_wood_7.md#pin-npc-guynmart_rob6)

### Quests

- [Guynmart rope (hidden flag)](../quests/guynmart_r_rope.md): stage 11

### Dialogue simulator

Set your quest stages and items, then talk to Rob. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_rob6_10.json" data-npc="Rob" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_rob6-guynmart_rob6_10"></span>**`guynmart_rob6_10`** Rob: “Hello $playername. Do you wish to climb up to me?”

    - “Yes. Could you drop the rope down?” → [guynmart_rob6_30](#d-guynmart_rob6-guynmart_rob6_30)
    - “No thanks.” → *conversation ends*

    <span id="d-guynmart_rob6-guynmart_rob6_30"></span>**`guynmart_rob6_30`** Rob: “Of course. There. But I am in a hurry and must leave now.” — **effects:** sets stage 11 of [Guynmart rope (hidden flag)](../quests/guynmart_r_rope.md#stage-11), removes monsters from guynmart_wood_7

    - “Great! I'll climb up now.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_rob6)"

    | | |
    |---|---|
    | Entry ID | `guynmart_rob6` |
    | Spawn group | `guynmart_rob6` |
    | Loot table | – |
    | Conversation | `guynmart_rob6_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:62` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_rob6",
     "name": "Rob",
     "iconID": "monsters_ld1:62",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_rob6_10"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_rob.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_rob.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_rob.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_rob.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
