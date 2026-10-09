---
description: "Brenor is a non-player character (NPC) in Andor's Trail, found in Undertell 1 0."
---

# ![](../assets/icons/monsters/monsters_newb_1_45.png){ .sprite } Brenor

**Where to find Brenor:** [Undertell 1 0](../maps/undertell_1_0.md#pin-npc-brenor)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_1_45.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Undertell 1 0 |
| **Entry ID** | `brenor` |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Quests

- [Undertell: What was not written](../quests/undertell_book.md): stages 50, 80
- [Undertell story flags (hidden flag)](../quests/undertell_hidden.md): stage 100

## Dialogue simulator

Set your quest stages and items, then talk to Brenor. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brenor_selector.json" data-npc="Brenor" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (15 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brenor_selector"></span>**`brenor_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if carry 1× [Heartstone](../items/heartstone.md))* → [brenor_refuse_10](#d-brenor_refuse_10)
    - branch 2 *(if wearing [#heartsteel_filter](../items/#heartsteel_filter.md))* → [brenor_heartsteel_10](#d-brenor_heartsteel_10)
    - branch 3 *(if NOT carry 1× [Heartstone](../items/heartstone.md))* → [brenor_intro_10](#d-brenor_intro_10)

    <span id="d-brenor_refuse_10"></span>**`brenor_refuse_10`** Brenor: “I will not speak while that glowing stone is in your pack. It stirs old pain. Set it down and return if you want my words.”

    - “All right. I will set it down.” → *conversation ends*
    - “Then we are done here.” → *conversation ends*

    <span id="d-brenor_heartsteel_10"></span>**`brenor_heartsteel_10`** Brenor: “That weapon...must you hold it where I can see it? Even in death I know its glow.”

    - “Is something wrong with it?” → [brenor_heartsteel_20](#d-brenor_heartsteel_20)

    <span id="d-brenor_intro_10"></span>**`brenor_intro_10`** Brenor: “The pick is light in my hand and heavy in my memory. We were driven into the deep seams with only a lamp and a promise. Many never climbed back.”

    - “Who are you?” *(if reached stage 40 of [Undertell: What was not written](../quests/undertell_book.md#stage-40))* → [brenor_who_20](#d-brenor_who_20)
    - “What was it like down there?” *(if reached stage 50 of [Undertell: What was not written](../quests/undertell_book.md#stage-50))* → [brenor_story_30](#d-brenor_story_30)
    - “I should go.” → *conversation ends*

    <span id="d-brenor_heartsteel_20"></span>**`brenor_heartsteel_20`** Brenor: “Wrong? To you it is a finely forged weapon. To us...it was an executioner's tool.”

    - “Executioner's tool?” → [brenor_heartsteel_30](#d-brenor_heartsteel_30)

    <span id="d-brenor_who_20"></span>**`brenor_who_20`** Brenor: “My name was Brenor. I came from the lands ruled by Feygard, back when its people still followed Elythara. I was taken during the rise of Garthan I, when those who held to the Light were chained and sent below the mountain. I swung this…” — **effects:** sets stage 50 of [Undertell: What was not written](../quests/undertell_book.md#stage-50)

    - “I am sorry, Brenor.” → *conversation ends*
    - “What happened in the mines?” → [brenor_story_30](#d-brenor_story_30)
    - “I will leave you be.” → *conversation ends*

    <span id="d-brenor_story_30"></span>**`brenor_story_30`** Brenor: “Dark, cold, and full of smoke. The tunnels shook when the rock groaned. We dug at glowing seams until our hands bled. The overseers said the ore was precious to Nor City, though none of us were told why. We were tools, nothing more.”

    - “You endured much hardship.” → [brenor_memory_40](#d-brenor_memory_40)
    - “Is there anything I can do to honor you?” → [brenor_help_50](#d-brenor_help_50)
    - “I must continue my search.” *(if reached stage 50 of [Undertell: What was not written](../quests/undertell_book.md#stage-50); reached stage 60 of [Undertell: What was not written](../quests/undertell_book.md#stage-60); reached stage 70 of [Undertell: What was not written](../quests/undertell_book.md#stage-70); NOT reached stage 80 of [Undertell: What was not written](../quests/undertell_book.md#stage-80))* → [brenor_reward_qs80](#d-brenor_reward_qs80)
    - “I must go now.” → *conversation ends*

    <span id="d-brenor_heartsteel_30"></span>**`brenor_heartsteel_30`** Brenor: “When the Shadow rose, many who came for the Elytharans carried heartsteel. It cut through armor with frightening ease, but that was never what we feared most.” — **effects:** sets stage 100 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-100)

    - “What did you fear?” → [brenor_heartsteel_40](#d-brenor_heartsteel_40)

    <span id="d-brenor_memory_40"></span>**`brenor_memory_40`** Brenor: “Hardship was the only thing we owned. The mountain took the rest. But remembering us is enough. Few living souls do.”

    - “I will remember that, but I must continue my search.” *(if reached stage 50 of [Undertell: What was not written](../quests/undertell_book.md#stage-50); reached stage 60 of [Undertell: What was not written](../quests/undertell_book.md#stage-60); reached stage 70 of [Undertell: What was not written](../quests/undertell_book.md#stage-70); NOT reached stage 80 of [Undertell: What was not written](../quests/undertell_book.md#stage-80))* → [brenor_reward_qs80](#d-brenor_reward_qs80)
    - “I will remember that.” → *conversation ends*

    <span id="d-brenor_help_50"></span>**`brenor_help_50`** Brenor: “Speak the names of the lost when you can. We were men once, not shadows in stone. That is all a slave could hope for.”

    - “I will honor your memory by continuing my search.” *(if reached stage 50 of [Undertell: What was not written](../quests/undertell_book.md#stage-50); reached stage 60 of [Undertell: What was not written](../quests/undertell_book.md#stage-60); reached stage 70 of [Undertell: What was not written](../quests/undertell_book.md#stage-70); NOT reached stage 80 of [Undertell: What was not written](../quests/undertell_book.md#stage-80))* → [brenor_reward_qs80](#d-brenor_reward_qs80)
    - “I will honor your memory.” → *conversation ends*

    <span id="d-brenor_reward_qs80"></span>**`brenor_reward_qs80`** Brenor: “Sure, you do that.” — **effects:** sets stage 80 of [Undertell: What was not written](../quests/undertell_book.md#stage-80)


    <span id="d-brenor_heartsteel_40"></span>**`brenor_heartsteel_40`** Brenor: “Those struck down by heartsteel often found no peace. Too many never reached Elythara's embrace. Instead, they lingered...as you see us now.”

    - “So these weapons created the ghosts?” → [brenor_heartsteel_50](#d-brenor_heartsteel_50)

    <span id="d-brenor_heartsteel_50"></span>**`brenor_heartsteel_50`** Brenor: “No. The weapon was only a tool. It was those who wielded it, and the darkness they served, that filled our halls with restless souls.”

    - “I never knew any of this.” → [brenor_heartsteel_60](#d-brenor_heartsteel_60)

    <span id="d-brenor_heartsteel_60"></span>**`brenor_heartsteel_60`** Brenor: “I believe you. Had I thought otherwise, I would not have spoken with you. Keep your weapon if you must, but remember what it once meant to my people.”

    - “Thank you for telling me.” → [brenor_heartsteel_70](#d-brenor_heartsteel_70)

    <span id="d-brenor_heartsteel_70"></span>**`brenor_heartsteel_70`** Brenor: “If you want to talk about something else, then please, get it out of my sight.”

    - “Understood.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 15 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brenor` |
    | Spawn group | `brenor` |
    | Loot table | – |
    | Conversation | `brenor_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_newb_1:45` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "brenor",
     "name": "Brenor",
     "iconID": "monsters_newb_1:45",
     "phraseID": "brenor_selector"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brenor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brenor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brenor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brenor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
