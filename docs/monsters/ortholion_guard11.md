---
description: "Drunken Feygard patrol is a non-player character (NPC) in Andor's Trail, found in Elm mine 1."
---

# ![](../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite } Drunken Feygard patrol

**Where to find Drunken Feygard patrol:** [Elm mine 1](../maps/elm_mine1.md#pin-npc-ortholion_guard11)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_rltiles3_14.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Elm mine 1 |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

## Dialogue simulator

Talk to Drunken Feygard patrol as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/ortholion_guard10_s.json" data-npc="Drunken Feygard patrol" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (5 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-ortholion_guard10_s"></span>**`ortholion_guard10_s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (1/4%))* → [ortholion_guard10_1](#d-ortholion_guard10_1)
    - branch 2 *(if random chance (1/3%))* → [ortholion_guard10_2](#d-ortholion_guard10_2)
    - branch 3 *(if random chance (1/2%))* → [ortholion_guard10_3](#d-ortholion_guard10_3)
    - branch 4 → [ortholion_guard10_4](#d-ortholion_guard10_4)

    <span id="d-ortholion_guard10_1"></span>**`ortholion_guard10_1`** Drunken Feygard patrol: “[hic] Drink! [hic] Drink for those who've fallen!”


    <span id="d-ortholion_guard10_2"></span>**`ortholion_guard10_2`** Drunken Feygard patrol: “No! [looks at you] This is my beeeeeer, kid! [hic]”

    - “Uh... How did you get drunk that fast?” → *conversation ends*
    - “Mead isn't my cup of tea, goodbye.” → *conversation ends*
    - “Get out of my way, drunkard!” → *conversation ends*

    <span id="d-ortholion_guard10_3"></span>**`ortholion_guard10_3`** Drunken Feygard patrol: “H..Halt! [hic] Kids not allowed!”

    - “I'll go where I please in this mine! Hmpf...” → *conversation ends*
    - “I'm here to see your general, now go sleep it off.” → *conversation ends*

    <span id="d-ortholion_guard10_4"></span>**`ortholion_guard10_4`** Drunken Feygard patrol: “This guard drinks his jar of mead ceaselessly, ignoring your presence.”




## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added<br>Dialogue: 5 lines added |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 3 lines changed<br>· text: “*hic* Drink! *hic* Drink for those who've fallen!” → “[hic] Drink! [hic] Drink for those who've fallen!”<br>· text: “No! *looks at you* This is my beeeeeer, kid! *hic*” → “No! [looks at you] This is my beeeeeer, kid! [hic]” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `ortholion_guard11` |
    | Type (wiki) | NPC |
    | Spawn group | `ortholion_guard11` |
    | Loot table | – |
    | Conversation | `ortholion_guard10_s` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_rltiles3:14` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "ortholion_guard11",
     "name": "Drunken Feygard patrol",
     "iconID": "monsters_rltiles3:14",
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "phraseID": "ortholion_guard10_s"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard11.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard11.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard11.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard11.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
