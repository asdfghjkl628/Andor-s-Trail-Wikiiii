---
description: "Tobby is a non-player character (NPC) in Andor's Trail, found in guynmart_wood_19, guynmart_wood_18, guynmart_wood_17b, guynmart_wood_17, Fallhaven. Starts Sobby's Trail."
---

# ![](../assets/icons/monsters/monsters_ld1_65.png){ .sprite } Tobby

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_65.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Starts [Sobby's Trail](../quests/tobby.md) |
| **Found in** | guynmart_wood_19, guynmart_wood_18, guynmart_wood_17b, guynmart_wood_17, Fallhaven |
| **Entries in game data** | 7 |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

</div>

!!! info "7 entries in the game data"
    The game's data files define 7 separate characters named Tobby. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location, movement. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`tobby`](#v-tobby) | NPC | [guynmart_wood_19](../maps/guynmart_wood_19.md#pin-npc-tobby) | starts [Sobby's Trail](../quests/tobby.md) |
| [`tobby2`](#v-tobby2) | NPC | [guynmart_wood_19](../maps/guynmart_wood_19.md#pin-npc-tobby2) | – |
| [`tobby3`](#v-tobby3) | NPC | [guynmart_wood_18](../maps/guynmart_wood_18.md#pin-npc-tobby3) | – |
| [`tobby4a`](#v-tobby4a) | NPC | [guynmart_wood_17b](../maps/guynmart_wood_17b.md#pin-npc-tobby4a) | – |
| [`tobby4b`](#v-tobby4b) | NPC | [guynmart_wood_17b](../maps/guynmart_wood_17b.md#pin-npc-tobby4b) | – |
| [`tobby5`](#v-tobby5) | NPC | [guynmart_wood_17](../maps/guynmart_wood_17.md#pin-npc-tobby5) | – |
| [`tobby6`](#v-tobby6) | NPC | Fallhaven: [woodhouse1](../maps/woodhouse1.md#pin-npc-tobby6) | – |

## Guynmart wood 19 (tobby) { #v-tobby }

**Entry ID:** `tobby` · **Type:** NPC · **Role:** Starts [Sobby's Trail](../quests/tobby.md)

**Location:** [guynmart_wood_19](../maps/guynmart_wood_19.md#pin-npc-tobby)

### Quests

- [Sobby's Trail](../quests/tobby.md): stages 10, 20, 21, 22

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Tobby. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/tobby.json" data-npc="Tobby" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (14 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-tobby-tobby"></span>**`tobby`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 20 of [Sobby's Trail](../quests/tobby.md#stage-20))* → [tobby_20](#d-tobby-tobby_20)
    - branch 2 *(if reached stage 10 of [Sobby's Trail](../quests/tobby.md#stage-10))* → [tobby_10](#d-tobby-tobby_10)
    - branch 3 → [tobby_1](#d-tobby-tobby_1)

    <span id="d-tobby-tobby_20"></span>**`tobby_20`** Tobby: “I am glad you want to help me.” — **effects:** sets stage 20 of [Sobby's Trail](../quests/tobby.md#stage-20)

    - “Sure thing. We brother-seekers must stand together.” → [tobby_22](#d-tobby-tobby_22)

    <span id="d-tobby-tobby_10"></span>**`tobby_10`** Tobby: “My father had sent me to look for him. But I dare not pass the kobolds in the ravine.”

    - “You are sure your brother went that way?” → [tobby_12](#d-tobby-tobby_12)

    <span id="d-tobby-tobby_1"></span>**`tobby_1`** Tobby: “Oh good, somebody comes to help me. Hey kid!”

    - “What?” → [tobby_2](#d-tobby-tobby_2)

    <span id="d-tobby-tobby_22"></span>**`tobby_22`** Tobby: “I want to get some provisions from the house, just a second ...” — **effects:** removes monsters from guynmart_wood_19, spawns monsters on guynmart_wood_19

    - “Go ahead, I'll wait and when you are ready, you can follow me. We will head south.” → *conversation ends*
    - “OK. And tell your father that his rat problem is solved.” *(if killed 1× [Tiny rat](../monsters/tiny_rat.md#v-tobby_trainingrat))* → [tobby_30](#d-tobby-tobby_30)
    - “OK. And bring your father this loaf of bread.” *(if NOT killed 1× [Tiny rat](../monsters/tiny_rat.md#v-tobby_trainingrat); hand over 1× [Bread](../items/bread.md))* → [tobby_32](#d-tobby-tobby_32)

    <span id="d-tobby-tobby_12"></span>**`tobby_12`** Tobby: “Absolutely. Once he was told of a lovely village hidden in the forest to the southeast.”

    - Next → [tobby_14](#d-tobby-tobby_14)

    <span id="d-tobby-tobby_2"></span>**`tobby_2`** Tobby: “I am Tobby. Please, you must help me.”

    - “I am $playername. What can I do for you?” → [tobby_3](#d-tobby-tobby_3)

    <span id="d-tobby-tobby_30"></span>**`tobby_30`** Tobby: “Oh, how did you know?” — **effects:** sets stage 21 of [Sobby's Trail](../quests/tobby.md#stage-21)

    - “I just had an inspiration.” → *conversation ends*
    - “Also here, bring him a loaf of bread.” *(if hand over 1× [Bread](../items/bread.md))* → [tobby_32](#d-tobby-tobby_32)

    <span id="d-tobby-tobby_32"></span>**`tobby_32`** Tobby: “Now I'm speechless - thank you!” — **effects:** sets stage 22 of [Sobby's Trail](../quests/tobby.md#stage-22)

    - “Hurry now.” → *conversation ends*

    <span id="d-tobby-tobby_14"></span>**`tobby_14`** Tobby: “Since then not a single day passed when he didn't talk about it.”

    - Next → [tobby_16](#d-tobby-tobby_16)

    <span id="d-tobby-tobby_3"></span>**`tobby_3`** Tobby: “I can't seem to find my brother, Sobby. He hasn't been back since he left last year.” — **effects:** sets stage 10 of [Sobby's Trail](../quests/tobby.md#stage-10)

    - “Never mind, he will probably not be back too soon.” → [tobby_10](#d-tobby-tobby_10)

    <span id="d-tobby-tobby_16"></span>**`tobby_16`** Tobby: “And now he is gone.”

    - “And you neither dare pass the kobolds, nor tell your father that you give up.” → [tobby_18](#d-tobby-tobby_18)

    <span id="d-tobby-tobby_18"></span>**`tobby_18`** Tobby: “Well, yes.”

    - Next → [tobby_19](#d-tobby-tobby_19)

    <span id="d-tobby-tobby_19"></span>**`tobby_19`** Tobby: “You have come from the south, so you know how to pass these nasty kobolds, right?”

    - “Well, OK. I'll help you.” → [tobby_20](#d-tobby-tobby_20)



### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 14 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (tobby)"

    | | |
    |---|---|
    | Entry ID | `tobby` |
    | Spawn group | `tobby` |
    | Loot table | – |
    | Conversation | `tobby` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:65` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "tobby",
     "name": "Tobby",
     "iconID": "monsters_ld1:65",
     "moveCost": 5,
     "monsterClass": "humanoid",
     "phraseID": "tobby"
    }
    ```


## Guynmart wood 19 (tobby2) { #v-tobby2 }

**Entry ID:** `tobby2` · **Type:** NPC

**Location:** [guynmart_wood_19](../maps/guynmart_wood_19.md#pin-npc-tobby2)

### Quests

- [Sobby's Trail](../quests/tobby.md): stage 30

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Tobby. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/tobby2.json" data-npc="Tobby" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-tobby2-tobby2"></span>**`tobby2`** Tobby: “Ouch, my toes!”

    - “Sorry.” → *conversation ends*
    - “Booh!” → *NPC leaves*
    - “Go away, or I have to kill you.” → [tobby2_1](#d-tobby2-tobby2_1)

    <span id="d-tobby2-tobby2_1"></span>**`tobby2_1`** Tobby: “No, I can't!”

    - “I'll show you - attack!” → [tobby2_2](#d-tobby2-tobby2_2)
    - “Then try harder.” → *conversation ends*

    <span id="d-tobby2-tobby2_2"></span>**`tobby2_2`** Tobby: “Tobby cried out aloud and ran away like the wind. You monster!” — **effects:** removes monsters from guynmart_wood_19, removes monsters from guynmart_wood_18, removes monsters from guynmart_wood_17b, removes monsters from guynmart_wood_17b, sets stage 30 of [Sobby's Trail](../quests/tobby.md#stage-30)

    - Next → *NPC leaves*



### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (tobby2)"

    | | |
    |---|---|
    | Entry ID | `tobby2` |
    | Spawn group | `tobby2` |
    | Loot table | – |
    | Conversation | `tobby2` |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:65` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "tobby2",
     "name": "Tobby",
     "iconID": "monsters_ld1:65",
     "moveCost": 3,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "phraseID": "tobby2"
    }
    ```


## Guynmart wood 18 (tobby3) { #v-tobby3 }

**Entry ID:** `tobby3` · **Type:** NPC

**Location:** [guynmart_wood_18](../maps/guynmart_wood_18.md#pin-npc-tobby3)

### Quests

- [Sobby's Trail](../quests/tobby.md): stage 30

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Tobby. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/tobby2.json" data-npc="Tobby" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [tobby2](#d-tobby2-tobby2).


### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (tobby3)"

    | | |
    |---|---|
    | Entry ID | `tobby3` |
    | Spawn group | `tobby3` |
    | Loot table | – |
    | Conversation | `tobby2` |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:65` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "tobby3",
     "name": "Tobby",
     "iconID": "monsters_ld1:65",
     "moveCost": 3,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "phraseID": "tobby2"
    }
    ```


## Guynmart wood 17b (tobby4a) { #v-tobby4a }

**Entry ID:** `tobby4a` · **Type:** NPC

**Location:** [guynmart_wood_17b](../maps/guynmart_wood_17b.md#pin-npc-tobby4a)

### Quests

- [Sobby's Trail](../quests/tobby.md): stage 30

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Tobby. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/tobby2.json" data-npc="Tobby" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [tobby2](#d-tobby2-tobby2).


### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (tobby4a)"

    | | |
    |---|---|
    | Entry ID | `tobby4a` |
    | Spawn group | `tobby4a` |
    | Loot table | – |
    | Conversation | `tobby2` |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:65` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "tobby4a",
     "name": "Tobby",
     "iconID": "monsters_ld1:65",
     "moveCost": 3,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "phraseID": "tobby2"
    }
    ```


## Guynmart wood 17b (tobby4b) { #v-tobby4b }

**Entry ID:** `tobby4b` · **Type:** NPC

**Location:** [guynmart_wood_17b](../maps/guynmart_wood_17b.md#pin-npc-tobby4b)

### Quests

- [Sobby's Trail](../quests/tobby.md): stage 30

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Tobby. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/tobby2.json" data-npc="Tobby" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [tobby2](#d-tobby2-tobby2).


### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (tobby4b)"

    | | |
    |---|---|
    | Entry ID | `tobby4b` |
    | Spawn group | `tobby4b` |
    | Loot table | – |
    | Conversation | `tobby2` |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:65` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "tobby4b",
     "name": "Tobby",
     "iconID": "monsters_ld1:65",
     "moveCost": 3,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "phraseID": "tobby2"
    }
    ```


## Guynmart wood 17 (tobby5) { #v-tobby5 }

**Entry ID:** `tobby5` · **Type:** NPC

**Location:** [guynmart_wood_17](../maps/guynmart_wood_17.md#pin-npc-tobby5)

### Quests

- [Sobby's Trail](../quests/tobby.md): stage 40

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Tobby. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/tobby5_1.json" data-npc="Tobby" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-tobby5-tobby5_1"></span>**`tobby5_1`** [Tobby](../monsters/tobby.md#v-tobby5): “Wow, that was an adventure!”

    - “Was it? I have got used to such things by now.” → [tobby5_10](#d-tobby5-tobby5_10)

    <span id="d-tobby5-tobby5_10"></span>**`tobby5_10`** Tobby: “I think that I'll find Sobby by myself now. Thank you - hope we'll meet again!” — **effects:** removes monsters from guynmart_wood_17, spawns monsters on woodhouse1, sets stage 40 of [Sobby's Trail](../quests/tobby.md#stage-40)

    - “Good luck!” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (tobby5)"

    | | |
    |---|---|
    | Entry ID | `tobby5` |
    | Spawn group | `tobby5` |
    | Loot table | – |
    | Conversation | `tobby5_1` |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:65` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "tobby5",
     "name": "Tobby",
     "iconID": "monsters_ld1:65",
     "moveCost": 3,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "phraseID": "tobby5_1"
    }
    ```


## Fallhaven, Woodhouse1 (tobby6) { #v-tobby6 }

**Entry ID:** `tobby6` · **Type:** NPC

**Location:** Fallhaven: [woodhouse1](../maps/woodhouse1.md#pin-npc-tobby6)

### Quests

- [Sobby's Trail](../quests/tobby.md): stage 50

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Tobby. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/tobby6.json" data-npc="Tobby" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-tobby6-tobby6"></span>**`tobby6`** Tobby: “Hey $playername - great to see you again!”

    - “Tobby? What are you doing here?” → [tobby6_10](#d-tobby6-tobby6_10)

    <span id="d-tobby6-tobby6_10"></span>**`tobby6_10`** Tobby: “Thanks to you I have found my brother Sobby.” — **effects:** sets stage 50 of [Sobby's Trail](../quests/tobby.md#stage-50)

    - “Two-teeth ... is your brother?!” → [tobby6_20](#d-tobby6-tobby6_20)

    <span id="d-tobby6-tobby6_20"></span>**`tobby6_20`** Tobby: “Well, due to his rat poison he has lost a few things in here ...”

    - Next → [tobby6_22](#d-tobby6-tobby6_22)

    <span id="d-tobby6-tobby6_22"></span>**`tobby6_22`** Tobby: “like his gold, his memory, most of his teeth ...”

    - Next → [tobby6_30](#d-tobby6-tobby6_30)

    <span id="d-tobby6-tobby6_30"></span>**`tobby6_30`** Tobby: “But yes - of course this is Sobby, my brother! Don't you see how we look alike?”

    - “Eh, sure.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (tobby6)"

    | | |
    |---|---|
    | Entry ID | `tobby6` |
    | Spawn group | `tobby6` |
    | Loot table | – |
    | Conversation | `tobby6` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:65` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "tobby6",
     "name": "Tobby",
     "iconID": "monsters_ld1:65",
     "moveCost": 3,
     "monsterClass": "humanoid",
     "phraseID": "tobby6"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tobby.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tobby.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tobby.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tobby.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
