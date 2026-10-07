---
description: "Jan is a non-player character (NPC) in Andor's Trail, found in Stoutford. Starts Fallen friends."
---

# ![](../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite } Jan

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Starts [Fallen friends](../quests/jan.md) |
| **Found in** | Stoutford |
| **Entries in game data** | 2 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Jan. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location, appearance. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`jan`](#v-jan) | NPC | Not on a map | starts [Fallen friends](../quests/jan.md) |
| [`stoutford_farmer_jan`](#v-stoutford_farmer_jan) | NPC | Stoutford: [stoutford_farmhouse1](../maps/stoutford_farmhouse1.md#pin-npc-stoutford_farmer_jan) | – |

## Not placed on a map (jan) { #v-jan }

**Entry ID:** `jan` · **Type:** NPC · **Role:** Starts [Fallen friends](../quests/jan.md)

**Location:** not placed on any map; this entry is added to the world by a quest or scripted event.

### Quests

- [Fallen friends](../quests/jan.md): stages 10, 100

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Jan. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/jan_start_select.json" data-npc="Jan" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (20 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-jan-jan_start_select"></span>**`jan_start_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 100 of [Fallen friends](../quests/jan.md#stage-100))* → [jan_complete2](#d-jan-jan_complete2)
    - branch 2 *(if reached stage 10 of [Fallen friends](../quests/jan.md#stage-10))* → [jan_return](#d-jan-jan_return)
    - branch 3 → [jan_default](#d-jan-jan_default)

    <span id="d-jan-jan_complete2"></span>**`jan_complete2`** Jan: “Thanks for dealing with Irogotu earlier! I am forever in debt to you.”

    - “Bye.” → *conversation ends*

    <span id="d-jan-jan_return"></span>**`jan_return`** Jan: “Hello again kid. Did you find Irogotu down in the cave?”

    - “No, not yet.” → [jan_default14](#d-jan-jan_default14)
    - “Can you tell me your story again?” → [jan_background](#d-jan-jan_background)
    - “Yes, I have killed Irogotu.” *(if hand over 1× [Gandir's ring](../items/ring_gandir.md))* → [jan_complete](#d-jan-jan_complete)

    <span id="d-jan-jan_default"></span>**`jan_default`** Jan: “Hello kid. Please leave me to my mourning.”

    - “What is the problem?” → [jan_default2](#d-jan-jan_default2)
    - “Do you want to talk about it?” → [jan_default2](#d-jan-jan_default2)
    - “OK, bye.” → *conversation ends*

    <span id="d-jan-jan_default14"></span>**`jan_default14`** Jan: “Return to me when you are done. Bring me Gandir's ring from Irogotu down in the cave.”

    - “OK, bye.” → *conversation ends*

    <span id="d-jan-jan_background"></span>**`jan_background`** Jan: “Didn't you listen the first time I told you the story? Do I really have to tell you the story one more time?”

    - “Yes, please tell me the story again.” → [jan_default3](#d-jan-jan_default3)
    - “I wasn't listening that much the first time you told it. What was that about a treasure?” → [jan_default4](#d-jan-jan_default4)
    - “No, never mind. I remember it now.” → [jan_default14](#d-jan-jan_default14)

    <span id="d-jan-jan_complete"></span>**`jan_complete`** Jan: “Wait, what? You actually went down there and returned alive? How did you manage that? Wow, I almost died going into that cave. Oh thank you so much for bringing me back Gandir's ring! Now I can have something to remember him by.” — **effects:** sets stage 100 of [Fallen friends](../quests/jan.md#stage-100)

    - “Glad that I could help. Goodbye.” → *conversation ends*
    - “Shadow be with you. Goodbye.” → *conversation ends*
    - “Whatever. I only did it for the loot.” → *conversation ends*

    <span id="d-jan-jan_default2"></span>**`jan_default2`** Jan: “Oh, it's so sad. I really don't want to talk about it.”

    - “Please do.” → [jan_default3](#d-jan-jan_default3)
    - “OK, bye.” → *conversation ends*

    <span id="d-jan-jan_default3"></span>**`jan_default3`** Jan: “Well, I guess it's OK to tell you. You seem to be a nice enough kid.”

    - Next → [jan_default4](#d-jan-jan_default4)

    <span id="d-jan-jan_default4"></span>**`jan_default4`** Jan: “My friend Gandir, his friend Irogotu, and I were down here digging this hole. We had heard there was a hidden treasure down here.”

    - Next → [jan_default5](#d-jan-jan_default5)

    <span id="d-jan-jan_default5"></span>**`jan_default5`** Jan: “We started digging and finally broke through to the cave system below. That's when we discovered them. The critters and bugs.”

    - Next → [jan_default6](#d-jan-jan_default6)

    <span id="d-jan-jan_default6"></span>**`jan_default6`** Jan: “Oh those critters. Damn bastards. Nearly killed me they did. Gandir and I told Irogotu that we should stop the digging and leave while we still could.”

    - Next → [jan_default7](#d-jan-jan_default7)

    <span id="d-jan-jan_default7"></span>**`jan_default7`** Jan: “But Irogotu wanted to continue deeper into the dungeon. He and Gandir got into an argument and started fighting.”

    - Next → [jan_default8](#d-jan-jan_default8)

    <span id="d-jan-jan_default8"></span>**`jan_default8`** Jan: “That's when it happened. *sob* Oh what have we done?”

    - “Please go on.” → [jan_default9](#d-jan-jan_default9)

    <span id="d-jan-jan_default9"></span>**`jan_default9`** Jan: “Irogotu killed Gandir with his bare hands. You could see the fire in his eyes. He almost seemed to enjoy it.”

    - Next → [jan_default10](#d-jan-jan_default10)

    <span id="d-jan-jan_default10"></span>**`jan_default10`** Jan: “I fled and haven't dared go back down there because of the critters and Irogotu himself.”

    - Next → [jan_default11](#d-jan-jan_default11)

    <span id="d-jan-jan_default11"></span>**`jan_default11`** Jan: “Oh that damn Irogotu. If only I could get to him. I'd show him one thing and another.”

    - “Do you think I could help?” → [jan_default11_1](#d-jan-jan_default11_1)

    <span id="d-jan-jan_default11_1"></span>**`jan_default11_1`** Jan: “Do you think you could help me?”

    - “Sure, there may be some treasure in this for me.” → [jan_default12](#d-jan-jan_default12)
    - “Sure. Irogotu should pay for what he did.” → [jan_default12](#d-jan-jan_default12)
    - “No thanks, I would rather not be involved in this. It sounds dangerous.” → *conversation ends*

    <span id="d-jan-jan_default12"></span>**`jan_default12`** Jan: “Really? You think you could help? Hmm, maybe you could. Beware of those bugs though, they're really tough bastards.” — **effects:** sets stage 10 of [Fallen friends](../quests/jan.md#stage-10)

    - Next → [jan_default13](#d-jan-jan_default13)

    <span id="d-jan-jan_default13"></span>**`jan_default13`** Jan: “If you really want to help, go find Irogotu down in the cave, and get me back Gandir's ring.”

    - “Sure, I'll help.” → [jan_default14](#d-jan-jan_default14)
    - “Can you tell me the story again?” → [jan_background](#d-jan-jan_background)
    - “Never mind, goodbye.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 8 lines changed<br>· text: “Well, I guess it's ok to tell you. You seem to be a nice enough kid.” → “Well, I guess it's OK to tell you. You seem to be a nice enough kid.”<br>· text: “Really? You think you could help? Hm, maybe you could. Beware of thos…” → “Really? You think you could help? Hmm, maybe you could. Beware of tho…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (jan)"

    | | |
    |---|---|
    | Entry ID | `jan` |
    | Spawn group | `jan` |
    | Loot table | – |
    | Conversation | `jan_start_select` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles3:14` |
    | Defined in | `res/raw/monsterlist_crossglen_npcs.json` |

    Raw data:

    ```json
    {
     "id": "jan",
     "name": "Jan",
     "iconID": "monsters_rltiles3:14",
     "monsterClass": "humanoid",
     "spawnGroup": "jan",
     "phraseID": "jan_start_select"
    }
    ```


## Stoutford, Stoutford farmhouse1 (stoutford_farmer_jan) { #v-stoutford_farmer_jan }

**Entry ID:** `stoutford_farmer_jan` · **Type:** NPC

**Location:** Stoutford: [stoutford_farmhouse1](../maps/stoutford_farmhouse1.md#pin-npc-stoutford_farmer_jan)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Jan. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/stoutford_farmer_jan_0.json" data-npc="Jan" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-stoutford_farmer_jan-stoutford_farmer_jan_0"></span>**`stoutford_farmer_jan_0`** Jan: “Can't you see I'm busy? Go talk to my brother Jen, he's always slacking off in the field.”




### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (stoutford_farmer_jan)"

    | | |
    |---|---|
    | Entry ID | `stoutford_farmer_jan` |
    | Spawn group | `stoutford_farmer_jan` |
    | Loot table | – |
    | Conversation | `stoutford_farmer_jan_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:1` |
    | Defined in | `res/raw/monsterlist_stoutford.json` |

    Raw data:

    ```json
    {
     "id": "stoutford_farmer_jan",
     "name": "Jan",
     "iconID": "monsters_karvis2:1",
     "phraseID": "stoutford_farmer_jan_0"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
