---
description: "Rubiano is a non-player character (NPC) in Andor's Trail, found in Brightport."
---

# ![](../assets/icons/monsters/monsters_ld1_77.png){ .sprite } Rubiano

**Where to find Rubiano:** Brightport: [Brightport bakery 3](../maps/brightport_bakery3.md#pin-npc-brightport_mayor)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_77.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Brightport |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Dialogue simulator

Set your quest stages and items, then talk to Rubiano. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_mayor.json" data-npc="Rubiano" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (13 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightport_mayor"></span>**`brightport_mayor`** Rubiano: “I'm Rubiano, the Doughe of Brightport, speak up.”

    - “Have you seen my brother Andor?” *(if NOT reached stage 900 of [Main quest endings (hidden flag)](../quests/andor_ending.md#stage-900))* → [brightport_mayor0](#d-brightport_mayor0)
    - “What's the history of the town?” → [brightport_mayor5](#d-brightport_mayor5)
    - “What's a doughe?” → [brightport_mayor1](#d-brightport_mayor1)
    - “Can you give Freya permission to sell me better equipment?” *(if reached stage 236 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-236))* → [brightport_mayor8](#d-brightport_mayor8)

    <span id="d-brightport_mayor0"></span>**`brightport_mayor0`** Rubiano: “Your brother, you say? Let's see... [Rubiano pulls out a small folder from his desk and starts browsing through it, muttering to himself.] Andor, Andor...”

    - Next → [brightport_mayor3](#d-brightport_mayor3)

    <span id="d-brightport_mayor5"></span>**`brightport_mayor5`** Rubiano: “Brightport was founded by my ancestors over 700 years ago. Sir Lucient of House De Lucent and his loyal squires were the first to set foot on this shore of the bright lake.”

    - Next → [brightport_mayor6](#d-brightport_mayor6)

    <span id="d-brightport_mayor1"></span>**`brightport_mayor1`** Rubiano: “The Doughe is the one who oversees Brightport, much like a mayor. The title is chosen by the council from among the De Lucent family, as we've guided the township's administration since its founding.”

    - “Begging your pardon, but are you of noble blood, sir?” → [brightport_mayor2](#d-brightport_mayor2)

    <span id="d-brightport_mayor8"></span>**`brightport_mayor8`** *(silent check: the first matching branch below is taken)*

    - Next → [brightport_mayor9](#d-brightport_mayor9)

    <span id="d-brightport_mayor3"></span>**`brightport_mayor3`** Rubiano: “I see an Andor listed here, graduated from our academy a while ago. He left Brightport then. Has he not made it back?”

    - “He has, but he went missing recently, so my father sent me out to search for him.” → [brightport_mayor4](#d-brightport_mayor4)

    <span id="d-brightport_mayor6"></span>**`brightport_mayor6`** Rubiano: “First, they built the manor, followed soon after by the bakery to sustain the house's trade. The squires and their families became the first commonfolk, joined over the centuries by merchants who chose to settle and make Brightport their…”

    - Next → [brightport_mayor7](#d-brightport_mayor7)

    <span id="d-brightport_mayor2"></span>**`brightport_mayor2`** Rubiano: “Haha, think nothing of it! We're Brightporters, like any other. So, what brings you here?”

    - “Have you seen my brother Andor?” *(if NOT reached stage 900 of [Main quest endings (hidden flag)](../quests/andor_ending.md#stage-900))* → [brightport_mayor0](#d-brightport_mayor0)
    - “What's the history of the town?” → [brightport_mayor5](#d-brightport_mayor5)

    <span id="d-brightport_mayor9"></span>**`brightport_mayor9`** Rubiano: “That would be a no.”

    - “Huh, why?” → [brightport_mayor10](#d-brightport_mayor10)

    <span id="d-brightport_mayor4"></span>**`brightport_mayor4`** Rubiano: “Braving these lands for your brother, impressive. You have courage, but I cannot help you more than to pray the Shadow to watch over you.”

    - “I have no Shadow of a doubt it won't be doing that.” → *conversation ends*
    - “May the Shadow watch over you too.” → *conversation ends*

    <span id="d-brightport_mayor7"></span>**`brightport_mayor7`** Rubiano: “We of the De Lucent family have been guiding the town ever since. But regrettably, the late Doughe chose the side of Nor City in the noble wars. After the loss, he was executed by decree of the King. Since then, we've had to answer not to…”

    - “Thanks for telling me this story, I'll be on my way.” → *conversation ends*

    <span id="d-brightport_mayor10"></span>**`brightport_mayor10`** Rubiano: “Many years ago, when my father was the Doughe, Brightport was attacked by a large group of lizardmen, and many lives were lost.”

    - Next → [brightport_mayor11](#d-brightport_mayor11)

    <span id="d-brightport_mayor11"></span>**`brightport_mayor11`** Rubiano: “More recently, strange creatures have begun appearing near the cursed, festering land that was once a green forest. With such threats present we cannot afford to sell our equipment to just any adventurer with a pretty purse.”

    - “I see, bye.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 13 lines added |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 2 lines changed<br>· text: “Haha, don't sweat it! We're Brightporters, like any other. So, what b…” → “Haha, think nothing of it! We're Brightporters, like any other. So, w…”<br>· text: “Im Rubiano, the Doughe of Brightport, speak up.” → “I'm Rubiano, the Doughe of Brightport, speak up.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightport_mayor` |
    | Type (wiki) | NPC |
    | Spawn group | `brightport_mayor` |
    | Loot table | – |
    | Conversation | `brightport_mayor` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:77` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_mayor",
     "name": "Rubiano",
     "iconID": "monsters_ld1:77",
     "phraseID": "brightport_mayor"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_mayor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_mayor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_mayor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_mayor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
