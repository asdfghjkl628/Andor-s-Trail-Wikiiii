---
description: "Zorvan is a non-player character (NPC) in Andor's Trail, found in brimhaven_church_basement."
---

# ![](../assets/icons/monsters/monsters_rltiles1_83.png){ .sprite } Zorvan

**Where to find Zorvan:** [brimhaven_church_basement](../maps/brimhaven_church_basement.md#pin-npc-brv_undertaker)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_83.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | brimhaven_church_basement |
| **Entry ID** | `brv_undertaker` |
| **Introduced** | [v0.7.12](../versions/0.7.12.md) |

</div>

## Quests

- [A strange looking dagger](../quests/brv_dagger.md): stage 105

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Zorvan. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/zorvan_0.json" data-npc="Zorvan" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-zorvan_0"></span>**`zorvan_0`** Zorvan: “You shouldn't be down here. What do you want?”

    - “Who are you?” → [zorvan_1_0](#d-zorvan_1_0)
    - “Can you tell me anything about what happened to Lawellyn?” *(if reached stage 100 of [A strange looking dagger](../quests/brv_dagger.md#stage-100))* → [zorvan_2_0](#d-zorvan_2_0)
    - “Can you tell me anything about what happened to Lawellyn?” *(if reached stage 90 of [A strange looking dagger](../quests/brv_dagger.md#stage-90))* → [zorvan_2_0](#d-zorvan_2_0)
    - “Sorry. I'll leave.” → *conversation ends*

    <span id="d-zorvan_1_0"></span>**`zorvan_1_0`** Zorvan: “My name is Zorvan. I perform several duties at the church, but the most important is that I am the undertaker for Brimhaven.”

    - Next → [zorvan_1_1](#d-zorvan_1_1)

    <span id="d-zorvan_2_0"></span>**`zorvan_2_0`** Zorvan: “Not really. I buried him some time ago. The circumstances of his death were apparently suspicious, but I don't know anything more. My job is to put them in the ground, not to worry about how they died.” — **effects:** sets stage 105 of [A strange looking dagger](../quests/brv_dagger.md#stage-105)

    - “What is it that you do?” → [zorvan_1_0](#d-zorvan_1_0)
    - “OK. Thanks. I'll be going now.” → *conversation ends*

    <span id="d-zorvan_1_1"></span>**`zorvan_1_1`** Zorvan: “As such, I prepare dead bodies for burial, make the funeral arrangements, etc. I am also responsible for preparation of the grave.”

    - Next → [zorvan_1_2](#d-zorvan_1_2)

    <span id="d-zorvan_1_2"></span>**`zorvan_1_2`** Zorvan: “I don't actually dig the grave of course. Quasi, over there, does that. He's not very pretty, but he's strong, and he enjoys digging. Oddly, he seems to enjoy filling the soil back in on top of the casket even more. He's useful, so I…” — **effects:** sets stage 30 of [nondisplay_bhvt (hidden flag)](../quests/nondisplay_bhvt.md#stage-30)

    - “[Sarcasm] It sounds like you have a really fun job. Can you tell me anything about what happened to Lawellyn?” *(if reached stage 90 of [A strange looking dagger](../quests/brv_dagger.md#stage-90))* → [zorvan_2_0](#d-zorvan_2_0)
    - “[Sarcasm] It sounds like you have a really fun job. Can you tell me anything about what happened to Lawellyn?” *(if reached stage 100 of [A strange looking dagger](../quests/brv_dagger.md#stage-100))* → [zorvan_2_0](#d-zorvan_2_0)
    - “[Sarcasm] It sounds like you have a really fun job. I'll be leaving now.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brv_undertaker` |
    | Spawn group | `zorvan` |
    | Loot table | – |
    | Conversation | `zorvan_0` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_rltiles1:83` |
    | Defined in | `res/raw/monsterlist_brimhaven_2.json` |

    Raw data:

    ```json
    {
     "id": "brv_undertaker",
     "name": "Zorvan",
     "iconID": "monsters_rltiles1:83",
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "spawnGroup": "zorvan",
     "phraseID": "zorvan_0"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_undertaker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_undertaker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_undertaker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_undertaker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
