---
description: "Matpat is a non-player character (NPC) in Andor's Trail, found in Sullengard."
---

# ![](../assets/icons/monsters/monsters_ld1_132.png){ .sprite } Matpat

**Where to find Matpat:** Sullengard: [Sullengard 1 northeast house](../maps/sullengard1_northeast_house.md#pin-npc-sullengard_matpat)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_132.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Sullengard |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Quests

- [Another ruthless Crackshot](../quests/Thieves04.md): stage 50

## Dialogue simulator

Set your quest stages and items, then talk to Matpat. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/sullengard_matpat.json" data-npc="Matpat" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (7 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-sullengard_matpat"></span>**`sullengard_matpat`** Matpat: “Hello there, kid. Happy 20th beer celebration.”

    - “Cheers!” → *conversation ends*
    - “Do you know where Defy is?” *(if reached stage 40 of [Another ruthless Crackshot](../quests/Thieves04.md#stage-40))* → [sullengard_matpat_2](#d-sullengard_matpat_2)
    - “I'm looking into the armory break-in and robbery and I am wondering if you saw or know anything about it?” *(if NOT reached stage 40 of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-40); reached stage 10 of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-10))* → [sull_recover_items_generic_response](#d-sull_recover_items_generic_response)

    <span id="d-sullengard_matpat_2"></span>**`sullengard_matpat_2`** Matpat: “Defy has left Sullengard.”

    - “Why?” → [sullengard_matpat_3](#d-sullengard_matpat_3)
    - “Where is he going?” → [sullengard_matpat_3](#d-sullengard_matpat_3)

    <span id="d-sull_recover_items_generic_response"></span>**`sull_recover_items_generic_response`** Matpat: “I'm sorry, I have not. In fact, this is the first that I am hearing about it.”


    <span id="d-sullengard_matpat_3"></span>**`sullengard_matpat_3`** Matpat: “I don't know, kid. Others are also looking for him and his crew. I'm still busy taking care of my firstborn child.”

    - “This is bad.” → [sullengard_matpat_4](#d-sullengard_matpat_4)
    - “I'll find him.” → [sullengard_matpat_4](#d-sullengard_matpat_4)

    <span id="d-sullengard_matpat_4"></span>**`sullengard_matpat_4`** Matpat: “We should find him or else what shall we do?”

    - Next → [sullengard_matpat_5](#d-sullengard_matpat_5)

    <span id="d-sullengard_matpat_5"></span>**`sullengard_matpat_5`** Matpat: “More importantly, how could I raise my firstborn child without the share to buy expensive foods and pay high rents here?”

    - “Calm down. I will find a way to help you.” → [sullengard_matpat_6](#d-sullengard_matpat_6)

    <span id="d-sullengard_matpat_6"></span>**`sullengard_matpat_6`** Matpat: “Thank you. You are my only hope here. I don't trust those unlawful Feygard soldiers. You should talk to the head of the Thieves' Guild about this.” — **effects:** sets stage 50 of [Another ruthless Crackshot](../quests/Thieves04.md#stage-50)

    - “I'm going now. Stay strong.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 7 lines added |
| [v0.8.13](../versions/0.8.13.md) | Dialogue: 1 line changed<br>· text: “Thank you. You are my only hope here. I don't trust those unlawful Fe…” → “Thank you. You are my only hope here. I don't trust those unlawful Fe…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `sullengard_matpat` |
    | Type (wiki) | NPC |
    | Spawn group | `matpat` |
    | Loot table | – |
    | Conversation | `sullengard_matpat` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:132` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "sullengard_matpat",
     "name": "Matpat",
     "iconID": "monsters_ld1:132",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "matpat",
     "phraseID": "sullengard_matpat"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_matpat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_matpat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_matpat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_matpat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
