---
description: "Mariora is a non-player character (NPC) in Andor's Trail, found in Sullengard."
---

# ![](../assets/icons/monsters/monsters_ld1_223.png){ .sprite } Mariora

**Where to find Mariora:** Sullengard: [Sullengard 2 garden house](../maps/sullengard2_garden_house.md#pin-npc-sullengard_mariora)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_223.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Sullengard |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Dialogue simulator

Set your quest stages and items, then talk to Mariora. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/sullengard_mariora_0.json" data-npc="Mariora" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-sullengard_mariora_0"></span>**`sullengard_mariora_0`** Mariora: “Hello. Isn't Sullengard a beautiful town?”

    - “Yes, but not as beautiful as you are.” → [sullengard_mariora_10](#d-sullengard_mariora_10)
    - “It's probably one of the nicest towns that I have visited.” → [sullengard_mariora_20](#d-sullengard_mariora_20)

    <span id="d-sullengard_mariora_10"></span>**`sullengard_mariora_10`** Mariora: “Oh, aren't you the sweetest thing in all of Dhayavar.”

    - “[Now blushing, you are nervous and desperate for this feeling to go away.] Well, I try to be when in the presence of…” → *conversation ends*

    <span id="d-sullengard_mariora_20"></span>**`sullengard_mariora_20`** Mariora: “What can I do for you, cutie.”

    - “Umm...I forget know..umm....oh, yeah, I am wondering if you know about or seen anything related to the armory break-in…” *(if NOT reached stage 40 of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-40); reached stage 10 of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-10))* → [sull_recover_items_generic_response](#d-sull_recover_items_generic_response)
    - “Umm...I think I should leave now.” → *conversation ends*

    <span id="d-sull_recover_items_generic_response"></span>**`sull_recover_items_generic_response`** Mariora: “I'm sorry, I have not. In fact, this is the first that I am hearing about it.”




## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `sullengard_mariora` |
    | Type (wiki) | NPC |
    | Spawn group | `sullengard_mariora` |
    | Loot table | – |
    | Conversation | `sullengard_mariora_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:223` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "sullengard_mariora",
     "name": "Mariora",
     "iconID": "monsters_ld1:223",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "sullengard_mariora",
     "phraseID": "sullengard_mariora_0"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_mariora.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_mariora.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_mariora.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_mariora.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
