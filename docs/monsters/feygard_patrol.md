---
description: "Feygard patrol is a non-player character (NPC) in Andor's Trail, found in Foaming Flask Tavern."
---

# ![](../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite } Feygard patrol

**Where to find Feygard patrol:** Foaming Flask Tavern: [Foaming flask](../maps/foaming_flask.md#pin-npc-feygard_patrol)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Foaming Flask Tavern |
| **Entry ID** | `feygard_patrol` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Dialogue simulator

Set your quest stages and items, then talk to Feygard patrol. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/ff_guard_1.json" data-npc="Feygard patrol" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (7 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-ff_guard_1"></span>**`ff_guard_1`** Feygard patrol: “Ha ha, you tell him Garl! *burp*”

    - Next → [ff_guard_2](#d-ff_guard_2)

    <span id="d-ff_guard_2"></span>**`ff_guard_2`** Feygard patrol: “Sing, drink, fight! All who oppose Feygard will fall!”

    - Next → [ff_guard_3](#d-ff_guard_3)

    <span id="d-ff_guard_3"></span>**`ff_guard_3`** Feygard patrol: “We will stand tall. Feygard, city of peace!”

    - “I had better be going.” → *conversation ends*
    - “Feygard, where is that?” → [ff_guard_4](#d-ff_guard_4)
    - “Have you seen a boy called Rincel around here recently?” *(if reached stage 41 of [Uncertain cause](../quests/wrye.md#stage-41))* → [ff_guard_rincel_1](#d-ff_guard_rincel_1)

    <span id="d-ff_guard_4"></span>**`ff_guard_4`** Feygard patrol: “What, you haven't heard of Feygard, kid? Just follow the road northwest and you will see the great city of Feygard rise above the treetops.”

    - “Thanks. Bye.” → *conversation ends*

    <span id="d-ff_guard_rincel_1"></span>**`ff_guard_rincel_1`** Feygard patrol: “A boy?! Apart from you, there have been no children in here that I have seen.”

    - Next → [ff_guard_rincel_2](#d-ff_guard_rincel_2)

    <span id="d-ff_guard_rincel_2"></span>**`ff_guard_rincel_2`** Feygard patrol: “Check with the captain over there. He has been around here for longer than us.”

    - “Thank you, Goodbye.” → *conversation ends*
    - “Thank you. Shadow be with you.” → [ff_guard_shadow_1](#d-ff_guard_shadow_1)

    <span id="d-ff_guard_shadow_1"></span>**`ff_guard_shadow_1`** Feygard patrol: “Don't bring that cursed Shadow in here son. We want none of that. Now leave.”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines changed<br>· text: “Ha ha, you tell him Garl! *burp*” → “Ha ha, you tell him Garl! *burp*” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `feygard_patrol` |
    | Spawn group | `ff_guard` |
    | Loot table | – |
    | Conversation | `ff_guard_1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles3:14` |
    | Defined in | `res/raw/monsterlist_v068_npcs.json` |

    Raw data:

    ```json
    {
     "id": "feygard_patrol",
     "name": "Feygard patrol",
     "iconID": "monsters_rltiles3:14",
     "monsterClass": "humanoid",
     "spawnGroup": "ff_guard",
     "phraseID": "ff_guard_1"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_patrol.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_patrol.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_patrol.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_patrol.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
