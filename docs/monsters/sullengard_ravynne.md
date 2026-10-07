---
description: "Ravynne is a non-player character (NPC) in Andor's Trail, found in Sullengard."
---

# ![](../assets/icons/monsters/monsters_ld1_162.png){ .sprite } Ravynne

**Where to find Ravynne:** Sullengard: [sullengard1_southeast_house](../maps/sullengard1_southeast_house.md#pin-npc-sullengard_ravynne)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_162.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Sullengard |
| **Entry ID** | `sullengard_ravynne` |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Ravynne. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/ravynne_0.json" data-npc="Ravynne" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ravynne_0"></span>**`ravynne_0`** Ravynne: “I've never seen you before. Are you here for the 'beer festival'?”

    - “Yes.” → [ravynne_10](#d-ravynne_10)
    - “Actually, I am looking for Gaelian.” *(if latest stage of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-20) is 20)* → [ravynne_20](#d-ravynne_20)
    - “I'm looking into the armory break-in and robbery and I am wondering if you saw or know anything about it?” *(if reached stage 10 of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-10); NOT reached stage 40 of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-40))* → [sull_recover_items_generic_response](#d-sull_recover_items_generic_response)

    <span id="d-ravynne_10"></span>**`ravynne_10`** Ravynne: “Well, you are a few weeks early.”


    <span id="d-ravynne_20"></span>**`ravynne_20`** Ravynne: “Well, he is in the tavern basement working. But beware, he doesn't like to be interrupted while working.”

    - “Thanks.” → *conversation ends*

    <span id="d-sull_recover_items_generic_response"></span>**`sull_recover_items_generic_response`** Ravynne: “I'm sorry, I have not. In fact, this is the first that I am hearing about it.”




## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `sullengard_ravynne` |
    | Spawn group | `sullengard_ravynne` |
    | Loot table | – |
    | Conversation | `ravynne_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:162` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "sullengard_ravynne",
     "name": "Ravynne",
     "iconID": "monsters_ld1:162",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "sullengard_ravynne",
     "phraseID": "ravynne_0"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_ravynne.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_ravynne.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_ravynne.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_ravynne.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
