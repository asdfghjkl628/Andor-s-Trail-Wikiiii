---
description: "Waterway traveler is a non-player character (NPC) in Andor's Trail, found in Graveyard 0."
---

# ![](../assets/icons/monsters/monsters_ld1_6.png){ .sprite } Waterway traveler

**Where to find Waterway traveler:** [Graveyard 0](../maps/graveyard0.md#pin-npc-graveyard_traveler)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld1_6.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Graveyard 0 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Quests

- [Mine for the taking](../quests/graveyard_quest.md): stages 20, 30

## Dialogue simulator

Talk to Waterway traveler as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/graveyardtraveler_begin.json" data-npc="Waterway traveler" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (10 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-graveyardtraveler_begin"></span>**`graveyardtraveler_begin`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 10 of [Mine for the taking](../quests/graveyard_quest.md#stage-10); NOT reached stage 40 of [Mine for the taking](../quests/graveyard_quest.md#stage-40))* → [graveyardtraveler_10](#d-graveyardtraveler_10)
    - Next → [graveyardtraveler_00](#d-graveyardtraveler_00)

    <span id="d-graveyardtraveler_10"></span>**`graveyardtraveler_10`** Waterway traveler: “Hey, did you try to open that treasure chest?”

    - “Yes.” → [graveyardtraveler_20](#d-graveyardtraveler_20)
    - “No.” → *conversation ends*

    <span id="d-graveyardtraveler_00"></span>**`graveyardtraveler_00`** Waterway traveler: “Greetings, young traveler.”

    - “I opened that chest and got a powerful sword.” *(if reached stage 80 of [Mine for the taking](../quests/graveyard_quest.md#stage-80); NOT reached stage 90 of [Mine for the taking](../quests/graveyard_quest.md#stage-90); NOT reached stage 95 of [Mine for the taking](../quests/graveyard_quest.md#stage-95))* → [graveyardtraveler_99](#d-graveyardtraveler_99)

    <span id="d-graveyardtraveler_20"></span>**`graveyardtraveler_20`** Waterway traveler: “That chest is something of a local legend. Been there for generations. They say it is sealed with magic and can only be opened with a special key, which hangs on the neck of one of the undead that roam in a cemetery directly south of here.” — **effects:** sets stage 20 of [Mine for the taking](../quests/graveyard_quest.md#stage-20)

    - “Killing the undead is my specialty.” → [graveyardtraveler_30](#d-graveyardtraveler_30)
    - “Undead? I would love to hear the rest of your story but I am on a mission to find my brother.” → *conversation ends*

    <span id="d-graveyardtraveler_99"></span>**`graveyardtraveler_99`** Waterway traveler: “I should not have doubted you. Well done.”


    <span id="d-graveyardtraveler_30"></span>**`graveyardtraveler_30`** Waterway traveler: “You don't think someone has already tried? It's a treasure chest ... left outside ... in plain view ... unguarded.”

    - Next → [graveyardtraveler_40](#d-graveyardtraveler_40)

    <span id="d-graveyardtraveler_40"></span>**`graveyardtraveler_40`** Waterway traveler: “Listen kid. A hundred 'adventurers' before you have tried and failed to open that chest. The problem isn't killing some undead. It's getting into the cemetery, because it's protected by a magical barrier that prevents anyone from entering.”

    - “Interesting. Is there anything else you can tell me about the chest or cemetery?” → [graveyardtraveler_50](#d-graveyardtraveler_50)

    <span id="d-graveyardtraveler_50"></span>**`graveyardtraveler_50`** Waterway traveler: “That is all I know ... Come to think of it ... Hagale from the Wood Settlement was out here a few weeks ago asking about the chest. Something about him struck me as odd. It was as if he was in a trance.” — **effects:** sets stage 30 of [Mine for the taking](../quests/graveyard_quest.md#stage-30)

    - Next → [graveyardtraveler_60](#d-graveyardtraveler_60)

    <span id="d-graveyardtraveler_60"></span>**`graveyardtraveler_60`** Waterway traveler: “Maybe he knows more. You should give him a visit.”

    - “OK, I'll do that.” → *conversation ends*
    - “Where is the Wood settlement?” → [graveyardtraveler61](#d-graveyardtraveler61)

    <span id="d-graveyardtraveler61"></span>**`graveyardtraveler61`** Waterway traveler: “South of the Duleian road, close to Fallhaven.”

    - “OK. I'll go there now.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 10 lines added |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 1 line changed<br>· text: “Maybe he knows more. You should give him a visit.” → “Maybe he knows more. You should give him a visit.” |
| [v0.7.9](../versions/0.7.9.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `graveyard_traveler` |
    | Type (wiki) | NPC |
    | Spawn group | `graveyard_traveler` |
    | Loot table | – |
    | Conversation | `graveyardtraveler_begin` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:6` |
    | Defined in | `res/raw/monsterlist_graveyard1.json` |

    Raw data:

    ```json
    {
     "id": "graveyard_traveler",
     "name": "Waterway traveler",
     "iconID": "monsters_ld1:6",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "graveyard_traveler",
     "phraseID": "graveyardtraveler_begin"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=graveyard_traveler.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=graveyard_traveler.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=graveyard_traveler.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=graveyard_traveler.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
