---
description: "Wulfric is a non-player character (NPC) in Andor's Trail, found in Wexlow Village."
---

# ![](../assets/icons/monsters/monsters_tometik3_10.png){ .sprite } Wulfric

**Where to find Wulfric:** Wexlow Village: [Way to wexlow 1](../maps/way_to_wexlow1.md#pin-npc-wulfric)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_tometik3_10.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Wexlow Village |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

</div>

## Dialogue simulator

Talk to Wulfric as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/wulfric_ip.json" data-npc="Wulfric" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (6 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-wulfric_ip"></span>**`wulfric_ip`** Wulfric: “Hey there. I am "Wulfric the Wonderful".”

    - “I am wondering...” → [wulfric_wonder](#d-wulfric_wonder)

    <span id="d-wulfric_wonder"></span>**`wulfric_wonder`** Wulfric: “Why I'm so wonderful?”

    - “Well, yeah, but no, not really.” → [wulfric_ask_about_andor](#d-wulfric_ask_about_andor)
    - “Do you know where the residents of Wexlow Village are?” *(if reached stage 11 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-11); NOT reached stage 10 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-10))* → [wulfric_wexlow](#d-wulfric_wexlow)
    - “Yes, why are you so wonderful?” → [wulfric_wonder_answer](#d-wulfric_wonder_answer)

    <span id="d-wulfric_ask_about_andor"></span>**`wulfric_ask_about_andor`** Wulfric: “What then?”

    - “Whether you've seen my brother, Andor or not. You see, he looks like me, but not as good looking.” → [wulfric_andor](#d-wulfric_andor)

    <span id="d-wulfric_wexlow"></span>**`wulfric_wexlow`** Wulfric: “Wexlow Village? Where is that?”

    - “Oh, nevermind.” → *conversation ends*

    <span id="d-wulfric_wonder_answer"></span>**`wulfric_wonder_answer`** Wulfric: “Because all the ladies say that I am.”


    <span id="d-wulfric_andor"></span>**`wulfric_andor`** Wulfric: “Nope. Sorry. Is there anything else?”

    - “I am wondering...” → [wulfric_wonder](#d-wulfric_wonder)
    - “Nope.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 6 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `wulfric` |
    | Type (wiki) | NPC |
    | Spawn group | `wulfric` |
    | Loot table | – |
    | Conversation | `wulfric_ip` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik3:10` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "wulfric",
     "name": "Wulfric",
     "iconID": "monsters_tometik3:10",
     "monsterClass": "humanoid",
     "phraseID": "wulfric_ip"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wulfric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wulfric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wulfric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wulfric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
