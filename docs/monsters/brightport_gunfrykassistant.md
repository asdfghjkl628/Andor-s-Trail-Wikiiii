---
description: "Leorio is a non-player character (NPC) in Andor's Trail, found in Brightport."
---

# ![](../assets/icons/monsters/monsters_ld1_11.png){ .sprite } Leorio

**Where to find Leorio:** Brightport: [Brightport guards 2](../maps/brightport_guards2.md#pin-npc-brightport_gunfrykassistant)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld1_11.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Brightport |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Dialogue simulator

Talk to Leorio as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_leorio_selector.json" data-npc="Leorio" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (7 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightport_leorio_selector"></span>**`brightport_leorio_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 100 of [Priceful vengeance](../quests/brightport_goons.md#stage-100))* → [brightport_leorio](#d-brightport_leorio)
    - Next *(if reached stage 152 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-152); reached stage 100 of [Priceful vengeance](../quests/brightport_goons.md#stage-100))* → [brightport_leorio](#d-brightport_leorio)
    - Next → [brightport_leorio_1](#d-brightport_leorio_1)

    <span id="d-brightport_leorio"></span>**`brightport_leorio`** Leorio: “Im Leorio, the commander's assistant. If you're looking for the commander he is inside the bakery.”

    - “What do you do here?” → [brightport_leorio1](#d-brightport_leorio1)

    <span id="d-brightport_leorio_1"></span>**`brightport_leorio_1`** Leorio: “What is it, can't you see im plenty busy already?”

    - “You don't look that busy.” → [brightport_leorio_2](#d-brightport_leorio_2)

    <span id="d-brightport_leorio1"></span>**`brightport_leorio1`** Leorio: “I help manage the Feygard troops and make sure Brightport's wealth gets collected in taxes. All for the glory of Lord Geomyr and Feygard's prosperity.”

    - “Makes sense, running a kingdom is expensive.” → [brightport_leorio3](#d-brightport_leorio3)
    - “Oh so you're stealing from the rural populace, got it.” → [brightport_leorio2](#d-brightport_leorio2)

    <span id="d-brightport_leorio_2"></span>**`brightport_leorio_2`** Leorio: “My senior, Commander Gunfryk, was slain by a lizardman. It was an honorable death, but now I carry his duties. So, if you would kindly show yourself out.”


    <span id="d-brightport_leorio3"></span>**`brightport_leorio3`** Leorio: “Exactly. It returns to the public, as it always should.”


    <span id="d-brightport_leorio2"></span>**`brightport_leorio2`** Leorio: “Ah, pesky kid. I shouldn't have entertained you in the first place. Go play your silly games, This place is for adults.”




## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 7 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightport_gunfrykassistant` |
    | Type (wiki) | NPC |
    | Spawn group | `brightport_gunfrykassistant` |
    | Loot table | – |
    | Conversation | `brightport_leorio_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:11` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_gunfrykassistant",
     "name": "Leorio",
     "iconID": "monsters_ld1:11",
     "phraseID": "brightport_leorio_selector"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_gunfrykassistant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_gunfrykassistant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_gunfrykassistant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_gunfrykassistant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
