---
description: "Gaelian is a non-player character (NPC) in Andor's Trail, found in Sullengard."
---

# ![](../assets/icons/monsters/monsters_ld1_97.png){ .sprite } Gaelian

**Where to find Gaelian:** Sullengard: [Sullengard tavern basement](../maps/sullengard_tavern_basement.md#pin-npc-sullengard_gaelian)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld1_97.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Sullengard |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Quests

- [Recovering stolen property](../quests/sullengard_recover_items.md): stage 30

## Dialogue simulator

Talk to Gaelian as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/sullengard_gaelian_0.json" data-npc="Gaelian" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (5 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-sullengard_gaelian_0"></span>**`sullengard_gaelian_0`** Gaelian: “This is no place for a kid.”

    - “I'm looking into the armory break-in and robbery.” *(if latest stage of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-20) is 20)* → [sullengard_gaelian_30](#d-sullengard_gaelian_30)
    - “What is this place?” → [sullengard_gaelian_20](#d-sullengard_gaelian_20)

    <span id="d-sullengard_gaelian_30"></span>**`sullengard_gaelian_30`** Gaelian: “[Laughing] Zaccheria deserves it for his lack of customer respect and shady business practices.”

    - “I was told that maybe you know some information about these crimes.” *(if NOT latest stage of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-30) is 30)* → [sullengard_gaelian_40](#d-sullengard_gaelian_40)
    - “Can you tell me again what you know about this crime?” *(if latest stage of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-30) is 30)* → [sullengard_gaelian_41](#d-sullengard_gaelian_41)

    <span id="d-sullengard_gaelian_20"></span>**`sullengard_gaelian_20`** Gaelian: “This is the heart and soul of Sullengard. This is our brewery. The place where the magic happens.”

    - “I can see that. Thank you.” → *conversation ends*
    - “I feel smarter now after having been told this. Thank you.” → *conversation ends*

    <span id="d-sullengard_gaelian_40"></span>**`sullengard_gaelian_40`** Gaelian: “I know nothing except that Zaccheria deserved it.” — **effects:** sets stage 30 of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-30)

    - “OK, but you are on my list.” → *conversation ends*

    <span id="d-sullengard_gaelian_41"></span>**`sullengard_gaelian_41`** Gaelian: “I know nothing except that Zaccheria deserved it.”

    - “OK, but you are on my list.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `sullengard_gaelian` |
    | Type (wiki) | NPC |
    | Spawn group | `sullengard_gaelian` |
    | Loot table | – |
    | Conversation | `sullengard_gaelian_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:97` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "sullengard_gaelian",
     "name": "Gaelian",
     "iconID": "monsters_ld1:97",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "sullengard_gaelian",
     "phraseID": "sullengard_gaelian_0"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_gaelian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_gaelian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_gaelian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_gaelian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
