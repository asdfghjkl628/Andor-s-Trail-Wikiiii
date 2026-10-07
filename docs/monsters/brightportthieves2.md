---
description: "Counterfeit is a non-player character (NPC) in Andor's Trail, found in Brightport."
---

# ![](../assets/icons/monsters/monsters_rltiles3_18.png){ .sprite } Counterfeit

**Where to find Counterfeit:** Brightport: [brightport_thieves](../maps/brightport_thieves.md#pin-npc-brightportthieves2)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles3_18.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Brightport |
| **Entry ID** | `brightportthieves2` |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Quests

- [No rest for the wicked](../quests/Stanwickquest.md): stage 50

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Counterfeit. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_counterfeit.json" data-npc="Counterfeit" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightport_counterfeit"></span>**`brightport_counterfeit`** [Counterfeit](../monsters/brightportthieves2.md): “Hello kid. Name's Counterfeit. I specialize in exactly that. Now please leave me be, I have work to do.”

    - “I need a copy of the key for the library here in Brightport. Could you help me with that” *(if reached stage 46 of [No rest for the wicked](../quests/Stanwickquest.md#stage-46); NOT reached stage 50 of [No rest for the wicked](../quests/Stanwickquest.md#stage-50); NOT reached stage 47 of [No rest for the wicked](../quests/Stanwickquest.md#stage-47))* → [brightport_counterfeit1](#d-brightport_counterfeit1)
    - “I seriously doubt that's your real name.” → [brightport_counterfeit3](#d-brightport_counterfeit3)

    <span id="d-brightport_counterfeit1"></span>**`brightport_counterfeit1`** [Counterfeit](../monsters/brightportthieves2.md): “Normally, I'd need the original. Lucky for you kid, I was a student here years ago and made a copy. You can have it for 2,000 gold.”

    - “OK, here's the gold.” *(if pay 2,000 gold)* → [brightport_counterfeit2](#d-brightport_counterfeit2)
    - “I don't have that gold on me.” *(if NOT pay 500 gold)* → *conversation ends*

    <span id="d-brightport_counterfeit3"></span>**`brightport_counterfeit3`** Counterfeit: “Yes, it's not my real name. So what? What people call me is what matters.”

    - “A false name? Fitting for someone in the Guild.” → *conversation ends*

    <span id="d-brightport_counterfeit2"></span>**`brightport_counterfeit2`** [Counterfeit](../monsters/brightportthieves2.md): “Alright, here you go. Now hush off. I've got work to do.” — **effects:** sets stage 50 of [No rest for the wicked](../quests/Stanwickquest.md#stage-50), gives 1× [Library key](../items/brightport_key.md)




## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 4 lines added |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed<br>· text: “Normally, I'd need the original. Lucky for you kid, I was a student h…” → “Normally, I'd need the original. Lucky for you kid, I was a student h…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightportthieves2` |
    | Spawn group | `brightportthieves2` |
    | Loot table | – |
    | Conversation | `brightport_counterfeit` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles3:18` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportthieves2",
     "name": "Counterfeit",
     "iconID": "monsters_rltiles3:18",
     "unique": 1,
     "phraseID": "brightport_counterfeit"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportthieves2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportthieves2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportthieves2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportthieves2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
