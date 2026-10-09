---
description: "Reinkarr is a non-player character (NPC) in Andor's Trail, found in Remgard."
---

# ![](../assets/icons/monsters/monsters_rltiles1_66.png){ .sprite } Reinkarr

**Where to find Reinkarr:** Remgard: [Remgard 3](../maps/remgard3.md#pin-npc-reinkarr)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_66.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Remgard |
| **Introduced** | v0.7.0 or earlier |

</div>

## Dialogue simulator

Set your quest stages and items, then talk to Reinkarr. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/reinkarr.json" data-npc="Reinkarr" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (14 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-reinkarr"></span>**`reinkarr`** Reinkarr: “You look just like an adventurer. Tell me child, what brings you here?”

    - “Who are you?” → [reinkarr_3](#d-reinkarr_3)
    - “I'm looking for my brother Andor.” → [reinkarr_1](#d-reinkarr_1)
    - “I'm just looking for trouble.” → [reinkarr_2](#d-reinkarr_2)

    <span id="d-reinkarr_3"></span>**`reinkarr_3`** Reinkarr: “I am Reinkarr. I guess you could call me an adventurer of sorts.”

    - “Any good tales to tell?” → [reinkarr_4](#d-reinkarr_4)

    <span id="d-reinkarr_1"></span>**`reinkarr_1`** Reinkarr: “OK then. Good luck with that.”

    - “Who are you?” → [reinkarr_3](#d-reinkarr_3)

    <span id="d-reinkarr_2"></span>**`reinkarr_2`** Reinkarr: “Ha ha, that sure sounds like an adventurer! Guts, that's what you need to be a successful adventurer, child. You don't seem to lack courage, if I may say so.”

    - “Who are you?” → [reinkarr_3](#d-reinkarr_3)

    <span id="d-reinkarr_4"></span>**`reinkarr_4`** Reinkarr: “No, not really. I never got the hang of the whole adventuring business. Me and some other fellows went looking for these ... crystals ... that we had heard about.”

    - “What crystals?” → [reinkarr_5](#d-reinkarr_5)

    <span id="d-reinkarr_5"></span>**`reinkarr_5`** Reinkarr: “Doesn't really matter. We never found any of them anyway.”

    - “What crystals were you looking for?” → [reinkarr_6](#d-reinkarr_6)

    <span id="d-reinkarr_6"></span>**`reinkarr_6`** Reinkarr: “They were called 'Oegyth crystals'. Supposedly very powerful and worth a fortune.”

    - “I have one of those.” *(if carry 1× [Oegyth crystal](../items/oegyth.md))* → [reinkarr_oeg_1](#d-reinkarr_oeg_1)
    - “So what made you stop looking?” → [reinkarr_8](#d-reinkarr_8)
    - “What are they?” → [reinkarr_7](#d-reinkarr_7)

    <span id="d-reinkarr_oeg_1"></span>**`reinkarr_oeg_1`** Reinkarr: “What!? You actually have one of those things? Let me see. Yes, that sure matches the description I read.”

    - Next → [reinkarr_oeg_2](#d-reinkarr_oeg_2)

    <span id="d-reinkarr_8"></span>**`reinkarr_8`** Reinkarr: “Just the boredom of it, I guess. We never were any good at the whole fighting thing, and as such we never found one of those things.”

    - Next → [reinkarr_9](#d-reinkarr_9)

    <span id="d-reinkarr_7"></span>**`reinkarr_7`** Reinkarr: “Actually, all I know is that they are some sort of crystal. As I said, they are supposedly very powerful. We were only looking for them so that we could sell them and become rich.”

    - “What made you stop looking?” → [reinkarr_8](#d-reinkarr_8)

    <span id="d-reinkarr_oeg_2"></span>**`reinkarr_oeg_2`** Reinkarr: “You would do well to keep that to yourself, kid. Whatever you do, don't lose it, and don't go around showing it to everyone you might meet. You could get in serious trouble.”

    - “What can I do with it?” → [reinkarr_oeg_3](#d-reinkarr_oeg_3)

    <span id="d-reinkarr_9"></span>**`reinkarr_9`** Reinkarr: “Anyway, it's been nice talking to you, kid. Take care.”


    <span id="d-reinkarr_oeg_3"></span>**`reinkarr_oeg_3`** Reinkarr: “I hear there are merchants that would do anything to get their hands on some of those crystals. You should seek out the merchants in one of the larger cities, and ask them.”

    - Next → [reinkarr_oeg_4](#d-reinkarr_oeg_4)

    <span id="d-reinkarr_oeg_4"></span>**`reinkarr_oeg_4`** Reinkarr: “Please be careful though!”

    - Next → [reinkarr_9](#d-reinkarr_9)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines changed<br>· text: “Ok then. Good luck with that.” → “OK then. Good luck with that.”<br>· text: “No, not really. I never got the hang of the whole adventuring busines…” → “No, not really. I never got the hang of the whole adventuring busines…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `reinkarr` |
    | Type (wiki) | NPC |
    | Spawn group | `reinkarr` |
    | Loot table | – |
    | Conversation | `reinkarr` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:66` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "reinkarr",
     "name": "Reinkarr",
     "iconID": "monsters_rltiles1:66",
     "monsterClass": "humanoid",
     "spawnGroup": "reinkarr",
     "phraseID": "reinkarr"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=reinkarr.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=reinkarr.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=reinkarr.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=reinkarr.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
