---
description: "Aemens is a non-player character (NPC) in Andor's Trail, found in Loneford."
---

# ![](../assets/icons/monsters/monsters_karvis2_6.png){ .sprite } Aemens

**Where to find Aemens:** Loneford: [Loneford 16](../maps/loneford16.md#pin-npc-aemens)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_karvis2_6.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Loneford |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Quests

- [General story flags 2 (hidden flag)](../quests/nondisplay_2.md): stages 50, 70

## Dialogue simulator

Set your quest stages and items, then talk to Aemens. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/aemens_0.json" data-npc="Aemens" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-aemens_0"></span>**`aemens_0`** Aemens: “Don't you know that it's rude to walk into someone's house without knocking?” — **effects:** sets stage 50 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-50)

    - “Your neighbor was right. He said you were not always a nice person.” *(if reached stage 60 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-60); NOT reached stage 75 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-75))* → [aemens_3](#d-aemens_3)
    - “Sorry. I'll leave.” → *conversation ends*
    - “Sorry. I'm looking for my brother, Andor. He looks a bit like me. Have you seen him?” → [aemens_1](#d-aemens_1)

    <span id="d-aemens_3"></span>**`aemens_3`** Aemens: “Did he now! Well, I'll have a word or two to say to him later! What do you want?” — **effects:** sets stage 70 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-70)

    - “Sorry. Nothing. I'll leave.” → *conversation ends*
    - “I'm looking for my brother, Andor. He looks a bit like me. Have you seen him?” → [aemens_1](#d-aemens_1)

    <span id="d-aemens_1"></span>**`aemens_1`** Aemens: “No. And little boys like you should not be wandering around on your own. I'm sure your father would not approve.”

    - “My father sent me to look for my brother.” → [aemens_2](#d-aemens_2)

    <span id="d-aemens_2"></span>**`aemens_2`** Aemens: “Then he must be a very bad father. He should look for your brother himself. Tell me, are your father and brother as rude as you?”

    - “Thank you for talking to me. I will leave now.” → *conversation ends*
    - “They are certainly not as rude as you. Goodbye.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `aemens` |
    | Type (wiki) | NPC |
    | Spawn group | `aemens` |
    | Loot table | – |
    | Conversation | `aemens_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:6` |
    | Defined in | `res/raw/monsterlist_graveyard1.json` |

    Raw data:

    ```json
    {
     "id": "aemens",
     "name": "Aemens",
     "iconID": "monsters_karvis2:6",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "aemens",
     "phraseID": "aemens_0"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=aemens.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=aemens.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=aemens.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=aemens.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
