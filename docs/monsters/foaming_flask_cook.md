---
description: "Foaming Flask cook is a non-player character (NPC) in Andor's Trail, found in Foaming Flask Tavern."
---

# ![](../assets/icons/monsters/monsters_men_0.png){ .sprite } Foaming Flask cook

**Where to find Foaming Flask cook:** Foaming Flask Tavern: [foaming_flask](../maps/foaming_flask.md#pin-npc-foaming_flask_cook)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Foaming Flask Tavern |
| **Entry ID** | `foaming_flask_cook` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Foaming Flask cook. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/ff_cook_1.json" data-npc="Foaming Flask cook" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ff_cook_1"></span>**`ff_cook_1`** Foaming Flask cook: “Hello. Do you want something from the kitchen?”

    - “Sure, let me see what food you have to sell.” → [ff_cook_3](#d-ff_cook_3)
    - “That smells horrible. What are you cooking?” → [ff_cook_2](#d-ff_cook_2)
    - “That smells wonderful. What are you cooking?” → [ff_cook_2](#d-ff_cook_2)

    <span id="d-ff_cook_3"></span>**`ff_cook_3`** Foaming Flask cook: “No sorry, I don't have any food to sell. Go talk to Torilo over there if you want some drink or ready-made food.”


    <span id="d-ff_cook_2"></span>**`ff_cook_2`** Foaming Flask cook: “Oh this? This is supposed to be a stew of anklebiter. Needs more seasoning I guess.”

    - “I look forward to trying it when it is done. Good luck cooking.” → *conversation ends*
    - “Yuck, that sounds awful. Can you really eat those things? I'm grossed out, goodbye.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed<br>· text: “Oh this? This is supposed to be a stew of Anklebiter. Needs more seas…” → “Oh this? This is supposed to be a stew of anklebiter. Needs more seas…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `foaming_flask_cook` |
    | Spawn group | `ff_cook` |
    | Loot table | – |
    | Conversation | `ff_cook_1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:0` |
    | Defined in | `res/raw/monsterlist_v068_npcs.json` |

    Raw data:

    ```json
    {
     "id": "foaming_flask_cook",
     "name": "Foaming Flask cook",
     "iconID": "monsters_men:0",
     "monsterClass": "humanoid",
     "spawnGroup": "ff_cook",
     "phraseID": "ff_cook_1"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=foaming_flask_cook.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=foaming_flask_cook.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=foaming_flask_cook.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=foaming_flask_cook.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
