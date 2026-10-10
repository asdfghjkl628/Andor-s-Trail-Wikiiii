---
description: "Lindauer is a non-player character (NPC) in Andor's Trail, found in Sullengard."
---

# ![](../assets/icons/monsters/monsters_ld1_132.png){ .sprite } Lindauer

**Where to find Lindauer:** Sullengard: [Sullengard 1](../maps/sullengard1.md#pin-npc-sullengard_cat_seeker)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_132.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Sullengard |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Dialogue simulator

Set your quest stages and items, then talk to Lindauer. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/sullengard_cat_seeker_0.json" data-npc="Lindauer" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-sullengard_cat_seeker_0"></span>**`sullengard_cat_seeker_0`** Lindauer: “Hey there. You haven't seen my cat by any chance have you?”

    - “What does your cat look like?” → [sullengard_cat_seeker_10](#d-sullengard_cat_seeker_10)

    <span id="d-sullengard_cat_seeker_10"></span>**`sullengard_cat_seeker_10`** Lindauer: “He is entirely white. He looks like a fresh coat of snow.”

    - “Oh, yes, in fact I have! He is over there. [Pointing to the southeast.]” *(if reached stage 31 of [Sullengard story flags (hidden flag)](../quests/sullengard_hidden.md#stage-31))* → [sullengard_cat_seeker_20](#d-sullengard_cat_seeker_20)
    - “[Lie] No, I have not.” *(if reached stage 31 of [Sullengard story flags (hidden flag)](../quests/sullengard_hidden.md#stage-31))* → *conversation ends*
    - “No, I have not. Sorry.” *(if NOT reached stage 31 of [Sullengard story flags (hidden flag)](../quests/sullengard_hidden.md#stage-31))* → *conversation ends*

    <span id="d-sullengard_cat_seeker_20"></span>**`sullengard_cat_seeker_20`** Lindauer: “Oh, thank you so much!”




## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 3 lines added |
| [v0.8.8](../versions/0.8.8.md) | Dialogue: 1 line changed<br>· text: “He is entirely white. He looks look a freash coat of snow.” → “He is entirely white. He looks look a fresh coat of snow.” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed<br>· text: “He is entirely white. He looks look a fresh coat of snow.” → “He is entirely white. He looks like a fresh coat of snow.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `sullengard_cat_seeker` |
    | Type (wiki) | NPC |
    | Spawn group | `sullengard_cat_seeker` |
    | Loot table | – |
    | Conversation | `sullengard_cat_seeker_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:132` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "sullengard_cat_seeker",
     "name": "Lindauer",
     "iconID": "monsters_ld1:132",
     "spawnGroup": "sullengard_cat_seeker",
     "phraseID": "sullengard_cat_seeker_0"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_cat_seeker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_cat_seeker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_cat_seeker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_cat_seeker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
