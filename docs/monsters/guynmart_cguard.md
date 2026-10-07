---
description: "Norgothla is a non-player character (NPC) in Andor's Trail, found in Guynmart Castle."
---

# ![](../assets/icons/monsters/monsters_ld1_41.png){ .sprite } Norgothla

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_41.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Guynmart Castle |
| **Entries in game data** | 2 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Norgothla. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`guynmart_cguard`](#v-guynmart_cguard) | NPC | Guynmart Castle: [guynmart_wood_4](../maps/guynmart_wood_4.md#pin-npc-guynmart_cguard) | – |
| [`guynmart_cguard2`](#v-guynmart_cguard2) | NPC | Guynmart Castle: [guynmart_main_0](../maps/guynmart_main_0.md#pin-npc-guynmart_cguard2), Guynmart Castle: [guynmart_main_1](../maps/guynmart_main_1.md#pin-npc-guynmart_cguard2) | – |

## Guynmart Castle, Guynmart wood 4 (guynmart_cguard) { #v-guynmart_cguard }

**Entry ID:** `guynmart_cguard` · **Type:** NPC

**Location:** Guynmart Castle: [guynmart_wood_4](../maps/guynmart_wood_4.md#pin-npc-guynmart_cguard)

### Quests

- [Roses](../quests/guynmart.md): stage 81

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Norgothla. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_cguard_10.json" data-npc="Norgothla" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (12 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guynmart_cguard-guynmart_cguard_10"></span>**`guynmart_cguard_10`** Norgothla: “Hello stranger. Who are you and where are you going?”

    - “I am $playername, and come from the castle.” → [guynmart_cguard_12](#d-guynmart_cguard-guynmart_cguard_12)

    <span id="d-guynmart_cguard-guynmart_cguard_12"></span>**`guynmart_cguard_12`** Norgothla: “From the castle? You did not come here the usual way.”

    - “You are right. I had a misunderstanding with Unkorh the steward and he threw me off the north wall. Now I am looking…” → [guynmart_cguard_20](#d-guynmart_cguard-guynmart_cguard_20)

    <span id="d-guynmart_cguard-guynmart_cguard_20"></span>**`guynmart_cguard_20`** Norgothla: “You were kicked out? And still want to go back? You must explain that.”

    - “I spoke to Lady Hannah there. She bade me to find her betrothed, who has been missing for a week now.” → [guynmart_cguard_30](#d-guynmart_cguard-guynmart_cguard_30)

    <span id="d-guynmart_cguard-guynmart_cguard_30"></span>**`guynmart_cguard_30`** Norgothla: “Lovis is missing? That is bad news. But where are my manners? I am questioning you and haven't even introduced myself. I am Norgothla, head of Guynmart's personal guard, and these are my men.”

    - “Nice to meet you, Norgothla.” → [guynmart_cguard_40](#d-guynmart_cguard-guynmart_cguard_40)

    <span id="d-guynmart_cguard-guynmart_cguard_40"></span>**`guynmart_cguard_40`** Norgothla: “You say Lovis is missing? I would like to look around the castle, but we are ordered to stay here.”

    - “Ordered?” → [guynmart_cguard_50](#d-guynmart_cguard-guynmart_cguard_50)

    <span id="d-guynmart_cguard-guynmart_cguard_50"></span>**`guynmart_cguard_50`** Norgothla: “I take orders only from Lord Guynmart himself. He told me and my men to go to this clearing and wait for him.”

    - “That is strange. I heard at the castle that Lord Guynmart was uproad for a week now.” → [guynmart_cguard_60](#d-guynmart_cguard-guynmart_cguard_60)

    <span id="d-guynmart_cguard-guynmart_cguard_60"></span>**`guynmart_cguard_60`** Norgothla: “Yes, Lord Guynmart was already on the way. Unkorh forwarded his order to me.”

    - “I also heard other things that I dare not tell.” → [guynmart_cguard_62](#d-guynmart_cguard-guynmart_cguard_62)

    <span id="d-guynmart_cguard-guynmart_cguard_62"></span>**`guynmart_cguard_62`** Norgothla: “You must tell me all that you know or think you know. I promise that you have nothing to fear.”

    - “I heard Unkorh saying that Guynmart is imprisoned in the dungeons. And Unkorh also wants to marry Lady Hannah.” → [guynmart_cguard_70](#d-guynmart_cguard-guynmart_cguard_70)

    <span id="d-guynmart_cguard-guynmart_cguard_70"></span>**`guynmart_cguard_70`** Norgothla: “Indeed? These are serious accusations. I hope you can prove them.”

    - “How can I? You may go to the castle and check for yourself.” → [guynmart_cguard_72](#d-guynmart_cguard-guynmart_cguard_72)

    <span id="d-guynmart_cguard-guynmart_cguard_72"></span>**`guynmart_cguard_72`** Norgothla: “Now I am really curious what is going on in the castle. But unfortunately Guynmart's order was very clear. Myself and all my men should wait for him in this clearing. I can't leave just based on the words of a kid.”

    - “And let Unkorh's dark plans be fulfilled? Leave Guynmart to probably die?” → [guynmart_cguard_74](#d-guynmart_cguard-guynmart_cguard_74)
    - “Maybe I could go back and bring some evidence?” → [guynmart_cguard_80](#d-guynmart_cguard-guynmart_cguard_80)

    <span id="d-guynmart_cguard-guynmart_cguard_74"></span>**`guynmart_cguard_74`** Norgothla: “Maybe you could go back to the castle and bring some evidence?”

    - “With pleasure, if this means you will believe me.” → [guynmart_cguard_80](#d-guynmart_cguard-guynmart_cguard_80)

    <span id="d-guynmart_cguard-guynmart_cguard_80"></span>**`guynmart_cguard_80`** Norgothla: “By doing this, you take a great burden from my heart. I get to know what is happening at the castle, but don't have to disobey my lords order. Please hurry, the path is not difficult to find.” — **effects:** sets stage 81 of [Roses](../quests/guynmart.md#stage-81)

    - “OK, I will be as quick as I can.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 12 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_cguard)"

    | | |
    |---|---|
    | Entry ID | `guynmart_cguard` |
    | Spawn group | `guynmart_cguard` |
    | Loot table | – |
    | Conversation | `guynmart_cguard_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:41` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_cguard",
     "name": "Norgothla",
     "iconID": "monsters_ld1:41",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_cguard_10"
    }
    ```


## Guynmart Castle, Guynmart main 0 and 1 more (guynmart_cguard2) { #v-guynmart_cguard2 }

**Entry ID:** `guynmart_cguard2` · **Type:** NPC

**Location:** Guynmart Castle: [guynmart_main_0](../maps/guynmart_main_0.md#pin-npc-guynmart_cguard2), Guynmart Castle: [guynmart_main_1](../maps/guynmart_main_1.md#pin-npc-guynmart_cguard2)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [guynmart_main_0](../maps/guynmart_main_0.md) | Guynmart Castle | 1 | Appears later, during a quest |
| [guynmart_main_1](../maps/guynmart_main_1.md) | Guynmart Castle | 1 | Appears later, during a quest |

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Norgothla. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_cguard2_10.json" data-npc="Norgothla" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guynmart_cguard2-guynmart_cguard2_10"></span>**`guynmart_cguard2_10`** Norgothla: “Hello $playername - great to meet you again!”

    - “Norgothla! So you made it here.” → [guynmart_cguard2_20](#d-guynmart_cguard2-guynmart_cguard2_20)

    <span id="d-guynmart_cguard2-guynmart_cguard2_20"></span>**`guynmart_cguard2_20`** Norgothla: “Yes. Unkorh is still on the run, but my men are close behind him, thanks to you.”

    - “It was you who did all the hard work, I just helped a bit.” → *conversation ends*
    - “I really would like to hunt him down.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_cguard2)"

    | | |
    |---|---|
    | Entry ID | `guynmart_cguard2` |
    | Spawn group | `guynmart_cguard2` |
    | Loot table | – |
    | Conversation | `guynmart_cguard2_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:41` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_cguard2",
     "name": "Norgothla",
     "iconID": "monsters_ld1:41",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_cguard2_10"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_cguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_cguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_cguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_cguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
