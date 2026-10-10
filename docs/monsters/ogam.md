---
description: "Ogam is a non-player character (NPC) in Andor's Trail, found in Vilegard."
---

# ![](../assets/icons/monsters/monsters_men_0.png){ .sprite } Ogam

**Where to find Ogam:** Vilegard: [Vilegard ogam](../maps/vilegard_ogam.md#pin-npc-ogam)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Vilegard |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [A lost potion](../quests/lodar.md): stage 20

## Dialogue simulator

Set your quest stages and items, then talk to Ogam. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/ogam_1.json" data-npc="Ogam" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (11 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-ogam_1"></span>**`ogam_1`** Ogam: “Belief. Power. Struggle.”

    - “What?” → [ogam_2](#d-ogam_2)
    - “I was told to see you.” *(if reached stage 15 of [A lost potion](../quests/lodar.md#stage-15))* → [ogam_2](#d-ogam_2)

    <span id="d-ogam_2"></span>**`ogam_2`** Ogam: “Backwards is the burden high and low.”

    - “What?” → [ogam_3](#d-ogam_3)
    - “Please go on.” → [ogam_3](#d-ogam_3)
    - “Hello? Umar in the Fallhaven Thieves' Guild sent me to see you.” *(if reached stage 15 of [A lost potion](../quests/lodar.md#stage-15))* → [ogam_3](#d-ogam_3)

    <span id="d-ogam_3"></span>**`ogam_3`** Ogam: “Hiding in the Shadow.”

    - Next → [ogam_4](#d-ogam_4)

    <span id="d-ogam_4"></span>**`ogam_4`** Ogam: “Two alike in body and mind.”

    - “Are you going to make any sense?” → [ogam_5](#d-ogam_5)
    - “What do you mean?” → [ogam_5](#d-ogam_5)

    <span id="d-ogam_5"></span>**`ogam_5`** Ogam: “The lawful and the chaotic.”

    - “Hello? Do you know how I can reach Lodar's hideaway?” *(if reached stage 15 of [A lost potion](../quests/lodar.md#stage-15))* → [ogam_lodar_1](#d-ogam_lodar_1)
    - “I don't understand.” → [ogam_6](#d-ogam_6)

    <span id="d-ogam_lodar_1"></span>**`ogam_lodar_1`** Ogam: “Lodar? Clear, tingling, hurt.”

    - Next → [ogam_6](#d-ogam_6)

    <span id="d-ogam_6"></span>**`ogam_6`** Ogam: “Yes. The true form. Behold.”

    - Next → [ogam_7](#d-ogam_7)

    <span id="d-ogam_7"></span>**`ogam_7`** Ogam: “Hiding in the Shadow.”

    - “The Shadow?” → [ogam_4](#d-ogam_4)
    - “Are you even listening to what I say?” → [ogam_4](#d-ogam_4)
    - “Hello? Do you know how I can reach Lodar's hideaway?” *(if reached stage 15 of [A lost potion](../quests/lodar.md#stage-15))* → [ogam_lodar_2](#d-ogam_lodar_2)

    <span id="d-ogam_lodar_2"></span>**`ogam_lodar_2`** Ogam: “Lodar, halfway between the Shadow and the light. Rocky formations.”

    - “OK, halfway between two places. Some rocks?” → [ogam_lodar_3](#d-ogam_lodar_3)
    - “Uh. Could you repeat that?” → [ogam_lodar_3](#d-ogam_lodar_3)

    <span id="d-ogam_lodar_3"></span>**`ogam_lodar_3`** Ogam: “Guardian. Glow of the Shadow.” — **effects:** sets stage 20 of [A lost potion](../quests/lodar.md#stage-20)

    - “Glow of the Shadow? Are those the words the guardian needs to hear?” → [ogam_lodar_4](#d-ogam_lodar_4)
    - “'Glow of the Shadow'? I recognize that from somewhere.” *(if reached stage 30 of [Disallowed substance](../quests/bonemeal.md#stage-30))* → [ogam_lodar_4](#d-ogam_lodar_4)

    <span id="d-ogam_lodar_4"></span>**`ogam_lodar_4`** Ogam: “Turning. Twisting. Clear form.”

    - “What does that mean?” → [ogam_1](#d-ogam_1)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 6 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `ogam` |
    | Type (wiki) | NPC |
    | Spawn group | `ogam` |
    | Loot table | – |
    | Conversation | `ogam_1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:0` |
    | Defined in | `res/raw/monsterlist_v068_npcs.json` |

    Raw data:

    ```json
    {
     "id": "ogam",
     "name": "Ogam",
     "iconID": "monsters_men:0",
     "monsterClass": "humanoid",
     "spawnGroup": "ogam",
     "phraseID": "ogam_1"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ogam.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ogam.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ogam.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ogam.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
