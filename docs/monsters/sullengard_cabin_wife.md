---
description: "Hadena is a non-player character (NPC) in Andor's Trail, found in sullengard_ravine_cabin. Starts Getting home on time."
---

# ![](../assets/icons/monsters/monsters_ld1_221.png){ .sprite } Hadena

**Where to find Hadena:** [sullengard_ravine_cabin](../maps/sullengard_ravine_cabin.md#pin-npc-sullengard_cabin_wife)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_221.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Starts [Getting home on time](../quests/deebo_orchard_ght.md) |
| **Found in** | sullengard_ravine_cabin |
| **Entry ID** | `sullengard_cabin_wife` |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Quests

- [Getting home on time](../quests/deebo_orchard_ght.md): stages 10, 20, 60
- [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md): stage 16

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Hadena. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/sullengard_hadena_selector_0.json" data-npc="Hadena" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (8 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-sullengard_hadena_selector_0"></span>**`sullengard_hadena_selector_0`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 10 of [Getting home on time](../quests/deebo_orchard_ght.md#stage-10))* → [sullengard_hadena_0](#d-sullengard_hadena_0)
    - branch 2 *(if NOT reached stage 60 of [Getting home on time](../quests/deebo_orchard_ght.md#stage-60))* → [sullengard_hadena_6](#d-sullengard_hadena_6)
    - branch 3 *(if reached stage 60 of [Getting home on time](../quests/deebo_orchard_ght.md#stage-60))* → [sullengard_hadena_completed](#d-sullengard_hadena_completed)

    <span id="d-sullengard_hadena_0"></span>**`sullengard_hadena_0`** Hadena: “Andor, good timing! Your arrival is much appreciated because I need your help to get my husband home on time today.” — **effects:** sets stage 16 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-16)

    - “So, my brother Andor was here as well? I'm $playername and you are?” → [sullengard_hadena_1](#d-sullengard_hadena_1)
    - “You must be mistaken. I'm $playername and Andor is my brother, and you are?” → [sullengard_hadena_1](#d-sullengard_hadena_1)
    - “I'm sorry because I was only half listening to you earlier, so I am a little fuzzy on the details. But can you explain…” *(if latest stage of [Getting home on time](../quests/deebo_orchard_ght.md#stage-10) is 10)* → [sullengard_hadena_2](#d-sullengard_hadena_2)

    <span id="d-sullengard_hadena_6"></span>**`sullengard_hadena_6`** Hadena: “I'm waiting for my husband's arrival. Please, I want him home on time today.”

    - “What do yo want me to do again with your husband?” *(if latest stage of [Getting home on time](../quests/deebo_orchard_ght.md#stage-10) is 10)* → [sullengard_hadena_2](#d-sullengard_hadena_2)
    - “I'm not done yet.” *(if NOT reached stage 50 of [Getting home on time](../quests/deebo_orchard_ght.md#stage-50))* → *conversation ends*
    - “It is done. Ainsley will be home on time today.” *(if latest stage of [Getting home on time](../quests/deebo_orchard_ght.md#stage-50) is 50)* → [sullengard_hadena_7](#d-sullengard_hadena_7)

    <span id="d-sullengard_hadena_completed"></span>**`sullengard_hadena_completed`** Hadena: “Thank you for helping Ainsley and I.”


    <span id="d-sullengard_hadena_1"></span>**`sullengard_hadena_1`** Hadena: “Oh, I'm sorry. My name is Hadena. Andor used to visit here but I don't know why he doesn't anymore. Anyways, I really need your help...please.” — **effects:** sets stage 10 of [Getting home on time](../quests/deebo_orchard_ght.md#stage-10)

    - “How may I help you?” → [sullengard_hadena_2](#d-sullengard_hadena_2)
    - “I'm sorry I can't help you right now. I'm busy.” → *conversation ends*

    <span id="d-sullengard_hadena_2"></span>**`sullengard_hadena_2`** Hadena: “As I already said, I need your help to get my husband Ainsley home on time today.”

    - Next → [sullengard_hadena_4](#d-sullengard_hadena_4)

    <span id="d-sullengard_hadena_7"></span>**`sullengard_hadena_7`** Hadena: “Thank you so much for helping us. You are just like your brother.” — **effects:** sets stage 60 of [Getting home on time](../quests/deebo_orchard_ght.md#stage-60)

    - “Of course. He is my brother.” → *conversation ends*
    - “You're welcome.” → *conversation ends*

    <span id="d-sullengard_hadena_4"></span>**`sullengard_hadena_4`** Hadena: “He is working at Deebo's Orchard located southwest of here. Please go there and help him.” — **effects:** sets stage 20 of [Getting home on time](../quests/deebo_orchard_ght.md#stage-20)

    - “I'll go now to help get him home on time.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 8 lines added |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `sullengard_cabin_wife` |
    | Spawn group | `sullengard_cabin_wife` |
    | Loot table | – |
    | Conversation | `sullengard_hadena_selector_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:221` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "sullengard_cabin_wife",
     "name": "Hadena",
     "iconID": "monsters_ld1:221",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "sullengard_cabin_wife",
     "phraseID": "sullengard_hadena_selector_0"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_cabin_wife.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_cabin_wife.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_cabin_wife.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_cabin_wife.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
