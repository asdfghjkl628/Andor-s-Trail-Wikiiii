---
description: "Isolated man is a non-player character (NPC) in Andor's Trail, found in Brightport."
---

# ![](../assets/icons/monsters/monsters_ld2_52.png){ .sprite } Isolated man

**Where to find Isolated man:** Brightport: [waterway_forest2](../maps/waterway_forest2.md#pin-npc-isolated_man)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld2_52.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Brightport |
| **Entry ID** | `isolated_man` |
| **Introduced** | [v0.8.11](../versions/0.8.11.md) |

</div>

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Isolated man. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/waterway_forest_isolated_man.json" data-npc="Isolated man" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-waterway_forest_isolated_man"></span>**`waterway_forest_isolated_man`** Isolated man: “What were you doing in my house!”

    - “I've come a long distance in the persuit of my brother Andor. So I peeked inside to see if he was in there.” → [waterway_forest_isolated_man_5](#d-waterway_forest_isolated_man_5)
    - “I am looking for someone that could explain why that land over there [pointing west] is poisoned.” → [waterway_forest_isolated_man_5](#d-waterway_forest_isolated_man_5)
    - “I was looking for help in getting into that cave just west of here.” *(if NOT reached stage 46 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-46))* → [waterway_forest_isolated_man_5](#d-waterway_forest_isolated_man_5)

    <span id="d-waterway_forest_isolated_man_5"></span>**`waterway_forest_isolated_man_5`** Isolated man: “Do you really think that I believe that? Who are you?! What do you really want?!”

    - “I don't care what you don't believe because that's the truth.” → [waterway_forest_isolated_man_dog](#d-waterway_forest_isolated_man_dog)
    - “Can you just answer my question now or I will go back in your house?” → [waterway_forest_isolated_man_dog](#d-waterway_forest_isolated_man_dog)

    <span id="d-waterway_forest_isolated_man_dog"></span>**`waterway_forest_isolated_man_dog`** Isolated man: “Well, with that attitude, you better get out of here now before I unleash my hounds on you.”

    - “OK, calm down. I'm leaving.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `isolated_man` |
    | Spawn group | `isolated_man` |
    | Loot table | – |
    | Conversation | `waterway_forest_isolated_man` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:52` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "isolated_man",
     "name": "Isolated man",
     "iconID": "monsters_ld2:52",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "waterway_forest_isolated_man"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=isolated_man.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=isolated_man.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=isolated_man.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=isolated_man.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
