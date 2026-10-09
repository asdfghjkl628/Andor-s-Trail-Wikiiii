---
description: "Dibella is a non-player character (NPC) in Andor's Trail, found in Brightport. Starts No rest for the wicked."
---

# ![](../assets/icons/monsters/monsters_ld1_188.png){ .sprite } Dibella

**Where to find Dibella:** Brightport: [Brightport school](../maps/brightport_school.md#pin-npc-brightportnpc3)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_188.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Starts [No rest for the wicked](../quests/Stanwickquest.md) |
| **Found in** | Brightport |
| **Entry ID** | `brightportnpc3` |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Quests

- [No rest for the wicked](../quests/Stanwickquest.md): stages 5, 15, 16, 31
- [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md): stages 66, 231

## Dialogue simulator

Set your quest stages and items, then talk to Dibella. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_dibella.json" data-npc="Dibella" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (16 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightport_dibella"></span>**`brightport_dibella`** Dibella: “Welcome to the Brightport Academy. I'm Dibella, the Headmaster's assistant.” — **effects:** sets stage 231 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-231)

    - Next *(if NOT reached stage 40 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-40))* → [brightport_dibella_selector](#d-brightport_dibella_selector)

    <span id="d-brightport_dibella_selector"></span>**`brightport_dibella_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 40 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-40))* → [brightport_dibella0](#d-brightport_dibella0)
    - Next → [brightport_dibella1](#d-brightport_dibella1)

    <span id="d-brightport_dibella0"></span>**`brightport_dibella0`** Dibella: “Is there something I can assist you with?”

    - “My brother has been missing, so I'm here to ask his friend Stanwick for a clue regarding his whereabouts. Could you…” *(if reached stage 110 of [Search for Andor](../quests/andor.md#stage-110); NOT reached stage 66 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-66))* → [brightport_dibella4](#d-brightport_dibella4)
    - “I have this batch of fruit that Janwick asked me to bring to his grandson in his stead.” *(if NOT reached stage 15 of [No rest for the wicked](../quests/Stanwickquest.md#stage-15); carry 1× [Fresh fruit for Stanwick](../items/brightport_fruit.md); reached stage 16 of [No rest for the wicked](../quests/Stanwickquest.md#stage-16); reached stage 66 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-66))* → [brightport_dibella2](#d-brightport_dibella2)
    - “Could you tell me about the incident again?” *(if NOT reached stage 96 of [No rest for the wicked](../quests/Stanwickquest.md#stage-96); reached stage 66 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-66))* → [brightport_dibella6](#d-brightport_dibella6)
    - “Could you tell me what you know about the library theft?” *(if reached stage 25 of [No rest for the wicked](../quests/Stanwickquest.md#stage-25); NOT reached stage 96 of [No rest for the wicked](../quests/Stanwickquest.md#stage-96))* → [brightport_dibella9](#d-brightport_dibella9)
    - “No, thanks.” → *conversation ends*

    <span id="d-brightport_dibella1"></span>**`brightport_dibella1`** Dibella: “It's time for the history lecture. If you hurry, you might still make it to the lecture room on time!”

    - “My brother has been missing for a while, so I'm here to ask his friend Stanwick for a clue regarding his whereabouts.…” *(if NOT reached stage 16 of [No rest for the wicked](../quests/Stanwickquest.md#stage-16); reached stage 110 of [Search for Andor](../quests/andor.md#stage-110))* → [brightport_dibella4](#d-brightport_dibella4)
    - “I have this batch of fruit that Janwick asked me to bring to his grandson in his stead.” *(if NOT reached stage 15 of [No rest for the wicked](../quests/Stanwickquest.md#stage-15); carry 1× [Fresh fruit for Stanwick](../items/brightport_fruit.md); reached stage 66 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-66))* → [brightport_dibella2](#d-brightport_dibella2)
    - “Could you tell me about the incident again?” *(if NOT reached stage 96 of [No rest for the wicked](../quests/Stanwickquest.md#stage-96); reached stage 66 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-66))* → [brightport_dibella6](#d-brightport_dibella6)
    - “Could you tell me what you know about the library theft?” *(if reached stage 25 of [No rest for the wicked](../quests/Stanwickquest.md#stage-25); NOT reached stage 96 of [No rest for the wicked](../quests/Stanwickquest.md#stage-96))* → [brightport_dibella9](#d-brightport_dibella9)

    <span id="d-brightport_dibella4"></span>**`brightport_dibella4`** Dibella: “Stanwick is on strict house arrest following the recent library incident, have you not heard of it? No one is allowed to enter his room except for his roommate and family.” — **effects:** sets stage 5 of [No rest for the wicked](../quests/Stanwickquest.md#stage-5)

    - “What incident?” → [brightport_dibella5](#d-brightport_dibella5)

    <span id="d-brightport_dibella2"></span>**`brightport_dibella2`** Dibella: “Let me see... That should be fine. I can make an exception if grandpa Janwick asked you.”

    - Next → [brightport_dibella3](#d-brightport_dibella3)

    <span id="d-brightport_dibella6"></span>**`brightport_dibella6`** Dibella: “Several days ago, Headmaster Oswald discovered that an extremely important document went missing from the basement archive of the library.”

    - Next → [brightport_dibella7](#d-brightport_dibella7)

    <span id="d-brightport_dibella9"></span>**`brightport_dibella9`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 35 of [No rest for the wicked](../quests/Stanwickquest.md#stage-35))* → [brightport_dibella9_2](#d-brightport_dibella9_2)
    - Next *(if reached stage 35 of [No rest for the wicked](../quests/Stanwickquest.md#stage-35))* → [brightport_dibella9_1](#d-brightport_dibella9_1)

    <span id="d-brightport_dibella5"></span>**`brightport_dibella5`** Dibella: “Oh, I thought you were a student here. My memory must be mistaken.”

    - Next → [brightport_dibella6](#d-brightport_dibella6)

    <span id="d-brightport_dibella3"></span>**`brightport_dibella3`** Dibella: “Go via the hallway on the left until you reach the dorms, Stanwick's room is the second door in the middle, if you knock two times he should open it.” — **effects:** sets stage 15 of [No rest for the wicked](../quests/Stanwickquest.md#stage-15)

    - “Thank you miss.” → *conversation ends*

    <span id="d-brightport_dibella7"></span>**`brightport_dibella7`** Dibella: “Stanwick looks after the library, so after questioning the teachers and students, the headmaster decided that Stanwick would stay in his room until the end of the investigation.” — **effects:** sets stage 66 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-66), sets stage 16 of [No rest for the wicked](../quests/Stanwickquest.md#stage-16)

    - “Judging by that, it sounds like this document was really important. Do you know what it was?” → [brightport_dibella8](#d-brightport_dibella8)

    <span id="d-brightport_dibella9_2"></span>**`brightport_dibella9_2`** Dibella: “I take it you are looking to help your friend Stanwick? Very well, but you need to ask the headmaster first for permission.”

    - “I'll go ask him right away.” → *conversation ends*

    <span id="d-brightport_dibella9_1"></span>**`brightport_dibella9_1`** Dibella: “Now that you've spoken to the headmaster we can talk. But there isn't much I know about the stolen document. Only why Stanwick had to be involved.”

    - Next → [brightport_dibella10](#d-brightport_dibella10)

    <span id="d-brightport_dibella8"></span>**`brightport_dibella8`** Dibella: “No, I don't. I keep any documents necessary for my work inside my desk. The important ones are locked in a box in the archive, that only the headmaster is allowed to open. It must have been very important.”

    - “[I should seek out a way to get permission to visit Stanwick.]” *(if NOT reached stage 15 of [No rest for the wicked](../quests/Stanwickquest.md#stage-15))* → *conversation ends*
    - “I see, bye.” *(if reached stage 15 of [No rest for the wicked](../quests/Stanwickquest.md#stage-15))* → *conversation ends*

    <span id="d-brightport_dibella10"></span>**`brightport_dibella10`** Dibella: “He is an honor student and the library's supervisor. Unfortunately, the importance of a secret document passed down to each generation's Headmaster far outweighs his merits.”

    - Next → [brightport_dibella11](#d-brightport_dibella11)

    <span id="d-brightport_dibella11"></span>**`brightport_dibella11`** Dibella: “Being the supervisor put him closest to the theft. Regardless of how his reputation might be ruined, the headmaster and town council had to place him under room arrest.” — **effects:** sets stage 31 of [No rest for the wicked](../quests/Stanwickquest.md#stage-31)

    - “Interesting, thanks.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 16 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightportnpc3` |
    | Spawn group | `brightportnpc3` |
    | Loot table | – |
    | Conversation | `brightport_dibella` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:188` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportnpc3",
     "name": "Dibella",
     "iconID": "monsters_ld1:188",
     "unique": 1,
     "phraseID": "brightport_dibella"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
