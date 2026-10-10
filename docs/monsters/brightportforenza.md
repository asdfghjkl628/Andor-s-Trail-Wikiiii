---
description: "Sylvester is a non-player character (NPC) in Andor's Trail, found in Brightport."
---

# ![](../assets/icons/monsters/monsters_ld1_101.png){ .sprite } Sylvester

**Where to find Sylvester:** Brightport: [Brightport forenza](../maps/brightport_forenza.md#pin-npc-brightportforenza)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld1_101.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Brightport |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Quests

- [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md): stage 182

## Dialogue simulator

Talk to Sylvester as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_sylverster_selector.json" data-npc="Sylvester" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (9 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightport_sylverster_selector"></span>**`brightport_sylverster_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 183 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-183))* → [brightport_sylvester2](#d-brightport_sylvester2)
    - Next *(if reached stage 182 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-182); NOT reached stage 183 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-183))* → [brightport_sylvester5](#d-brightport_sylvester5)
    - Next *(if NOT reached stage 182 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-182))* → [brightport_sylvester0](#d-brightport_sylvester0)

    <span id="d-brightport_sylvester2"></span>**`brightport_sylvester2`** [Sylvester](../monsters/brightportforenza.md): “You are our guest, $playername. Feel free to use our couch to rest while you're here. I will be returning to my work now.”

    - “While cleaning at the bakery I found this paper recording the bakery's revenue, weren't you the accountant?” *(if carry 1× [Bakery ledger](../items/brightport_documents.md); reached stage 242 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-242))* → [brightport_sylvester](#d-brightport_sylvester)

    <span id="d-brightport_sylvester5"></span>**`brightport_sylvester5`** Sylvester: “I'm really thankful that you found that ledger for me.”


    <span id="d-brightport_sylvester0"></span>**`brightport_sylvester0`** Sylvester: “Do you need something, or are you just wandering into people's houses?”

    - Next → [brightport_sylvester1](#d-brightport_sylvester1)

    <span id="d-brightport_sylvester"></span>**`brightport_sylvester`** [Sylvester](../monsters/brightportforenza.md): “Did I hear that correctly, you found a paper? Let me see!”

    - “Sure.” *(if hand over 1× [Bakery ledger](../items/brightport_documents.md))* → [brightport_sylvester3](#d-brightport_sylvester3)

    <span id="d-brightport_sylvester1"></span>**`brightport_sylvester1`** [Florencia](../monsters/brightportforenza1.md): “Ah, he's always grumpy when he's working. Did you wish to ask something child?”

    - “Have you seen my brother Andor?” *(if NOT reached stage 900 of [Main quest endings (hidden flag)](../quests/andor_ending.md#stage-900))* → [brightport_florencia1](#d-brightport_florencia1)
    - “While cleaning at the bakery I found this paper recording the bakery's revenue, wasn't your husband the accountant?” *(if reached stage 243 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-243); carry 1× [Bakery ledger](../items/brightport_documents.md); reached stage 242 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-242))* → [brightport_sylvester](#d-brightport_sylvester)

    <span id="d-brightport_sylvester3"></span>**`brightport_sylvester3`** Sylvester: “Good heavens, that's the missing ledger I was losing sleep over! I was beginning to suspect someone stole and hid it, I'm glad you found it.”

    - Next → [brightport_sylvester4](#d-brightport_sylvester4)

    <span id="d-brightport_florencia1"></span>**`brightport_florencia1`** [Florencia](../monsters/brightportforenza1.md): “No sorry, I don't think we have, but you could ask the Doughe. His chambers are on the Bakery's second floor.”

    - “Thanks.” → *conversation ends*

    <span id="d-brightport_sylvester4"></span>**`brightport_sylvester4`** Sylvester: “You saved me a headache worth a fortune in medicine, you have my permission to take some gold from the vault.” — **effects:** sets stage 182 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-182)




## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 9 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightportforenza` |
    | Type (wiki) | NPC |
    | Spawn group | `brightportforenza` |
    | Loot table | – |
    | Conversation | `brightport_sylverster_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:101` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportforenza",
     "name": "Sylvester",
     "iconID": "monsters_ld1:101",
     "phraseID": "brightport_sylverster_selector"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportforenza.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportforenza.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportforenza.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportforenza.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
