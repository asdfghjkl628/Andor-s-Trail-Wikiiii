---
description: "Old Leta is a non-player character (NPC) in Andor's Trail, found in Crossglen."
---

# ![](../assets/icons/monsters/monsters_karvis2_6.png){ .sprite } Old Leta

**Where to find Old Leta:** Crossglen: [Crossglen farmhouse](../maps/crossglen_farmhouse.md#pin-npc-old_leta)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_karvis2_6.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Crossglen |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Quests

- [A familiar shadow](../quests/familiar_shadow.md): stage 70

## Dialogue simulator

Talk to Old Leta as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/old_leta_initial_phrase.json" data-npc="Old Leta" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (6 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-old_leta_initial_phrase"></span>**`old_leta_initial_phrase`** Old Leta: “[Calm, almost welcoming.] Ah, there you are. You've come back to see us, then.”

    - “Leta? What happened to you two? You look...different.” *(if latest stage of [A familiar shadow](../quests/familiar_shadow.md#stage-60) is 60)* → [old_leta_10](#d-old_leta_10)
    - “Oh, it's still so hard to see you like this, so I should leave now.” *(if reached stage 70 of [A familiar shadow](../quests/familiar_shadow.md#stage-70))* → *conversation ends*

    <span id="d-old_leta_10"></span>**`old_leta_10`** [Old Leta](../monsters/old_leta.md): “Different? Yes, I suppose we are. Some more than others.”

    - Next → [old_leta_oromir_responds_10](#d-old_leta_oromir_responds_10)

    <span id="d-old_leta_oromir_responds_10"></span>**`old_leta_oromir_responds_10`** [Old Oromir](../monsters/old_oromir.md): “[frail, but confidenty] Don't mind her. She's just not use to me being so assertive.”

    - “Oromir...this isn't normal. You look like you've aged decades overnight. How can you be so calm about this?” → [old_oromir_leta_responds_20](#d-old_oromir_leta_responds_20)

    <span id="d-old_oromir_leta_responds_20"></span>**`old_oromir_leta_responds_20`** [Old Leta](../monsters/old_leta.md): “Oh, time catches up to us all, doesn't it? Better to find peace than cling to what's already gone. Whatever you did, thank you. Truly.”

    - “I didn't do this to you. This doesn't feel right. What happened after the spirit was defeated?” → [old_oromir_20](#d-old_oromir_20)

    <span id="d-old_oromir_20"></span>**`old_oromir_20`** [Old Oromir](../monsters/old_oromir.md): “[Firmly, but not unkindly.] What happened doesn't matter anymore. What matters is that the darkness is gone, and we can finally live. You should do the same. Let it rest. Ease your mind and later, if you still have questions, please visit…”

    - Next → [old_oromir_and_leta_narrator_10](#d-old_oromir_and_leta_narrator_10)

    <span id="d-old_oromir_and_leta_narrator_10"></span>**`old_oromir_and_leta_narrator_10`** [Dummy NPC](../monsters/none.md): “While looking between Leta and Oromir, you are unsettled by their calm acceptance. The house feels peaceful, but the air is heavy with unanswered questions. Leta and Oromir's transformations are undeniable. Their peace is haunting, a…” — **effects:** sets stage 70 of [A familiar shadow](../quests/familiar_shadow.md#stage-70)




## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 6 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `old_leta` |
    | Type (wiki) | NPC |
    | Spawn group | `old_leta` |
    | Loot table | – |
    | Conversation | `old_leta_initial_phrase` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:6` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "old_leta",
     "name": "Old Leta",
     "iconID": "monsters_karvis2:6",
     "monsterClass": "humanoid",
     "phraseID": "old_leta_initial_phrase"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=old_leta.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=old_leta.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=old_leta.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=old_leta.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
