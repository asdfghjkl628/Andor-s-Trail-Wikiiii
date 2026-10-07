---
description: "Odair is a non-player character (NPC) in Andor's Trail, found in Crossglen. Starts Rat infestation."
---

# ![](../assets/icons/monsters/monsters_men_8.png){ .sprite } Odair

**Where to find Odair:** Crossglen: [crossglen](../maps/crossglen.md#pin-npc-odair)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_8.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Starts [Rat infestation](../quests/odair.md) |
| **Found in** | Crossglen |
| **Entry ID** | `odair` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [Rat infestation](../quests/odair.md): stages 10, 100

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Odair. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/odair1.json" data-npc="Odair" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (10 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-odair1"></span>**`odair1`** Odair: “Oh, it's you. You with that brother of yours. Always causing trouble.”

    - Next → [odair_select](#d-odair_select)

    <span id="d-odair_select"></span>**`odair_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 100 of [Rat infestation](../quests/odair.md#stage-100))* → [odair_complete2](#d-odair_complete2)
    - branch 2 *(if reached stage 10 of [Rat infestation](../quests/odair.md#stage-10))* → [odair_continue](#d-odair_continue)
    - branch 3 → [odair2](#d-odair2)

    <span id="d-odair_complete2"></span>**`odair_complete2`** Odair: “Thanks a lot for your help earlier. Now we might start using that cave as our old supply cave again.”

    - “Bye.” → *conversation ends*

    <span id="d-odair_continue"></span>**`odair_continue`** Odair: “Did you kill that large rat in the cave west of here?”

    - “Yes, I have killed the large rat.” *(if hand over 1× [Cave rat tail](../items/tail_caverat.md))* → [odair_complete](#d-odair_complete)
    - “What was I supposed to do again?” → [odair5](#d-odair5)
    - “No, not yet.” → [odair_cowards](#d-odair_cowards)

    <span id="d-odair2"></span>**`odair2`** Odair: “Hmm, maybe you could be of use to me. Do you think you could help me with a small task?”

    - “Tell me more about this task.” → [odair3](#d-odair3)
    - “Sure, if there is anything I can gain from it.” → [odair3](#d-odair3)

    <span id="d-odair_complete"></span>**`odair_complete`** Odair: “Thanks a lot for your help kid! Maybe you and that brother of yours aren't as cowardly as I thought. Here, take these coins for your help.” — **effects:** sets stage 100 of [Rat infestation](../quests/odair.md#stage-100), gives [Gold coins](../items/gold.md)

    - “Thanks.” → *conversation ends*

    <span id="d-odair5"></span>**`odair5`** Odair: “I need you to get into that cave and kill the large rat, that way maybe we can stop the rat infestation in the cave and start using it as our old supply cave again.” — **effects:** sets stage 10 of [Rat infestation](../quests/odair.md#stage-10)

    - “OK.” → *conversation ends*
    - “On second thought, I don't think I will help you after all.” → [odair_cowards](#d-odair_cowards)

    <span id="d-odair_cowards"></span>**`odair_cowards`** Odair: “I didn't think so either. You and that brother of yours always were cowards.”

    - “Bye.” → *conversation ends*

    <span id="d-odair3"></span>**`odair3`** Odair: “I recently went in to that cave over there [points west], to check on our supplies. But apparently, the cave has been infested with rats.”

    - Next → [odair4](#d-odair4)

    <span id="d-odair4"></span>**`odair4`** Odair: “In particular, I saw one rat that was larger than the other rats. Do you think you have what it takes to help eliminate them?”

    - “Sure, I'll help you so that Crossglen can use the supply cave again.” → [odair5](#d-odair5)
    - “Sure, I'll help you. But only because there might be some gain for me in this.” → [odair5](#d-odair5)
    - “No thanks.” → [odair_cowards](#d-odair_cowards)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 7 lines changed<br>· text: “I recently went in to that cave over there *points west*, to check on…” → “I recently went in to that cave over there [points west], to check on…” |
| [v0.7.10](../versions/0.7.10.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `odair` |
    | Spawn group | `odair` |
    | Loot table | – |
    | Conversation | `odair1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:8` |
    | Defined in | `res/raw/monsterlist_crossglen_npcs.json` |

    Raw data:

    ```json
    {
     "id": "odair",
     "name": "Odair",
     "iconID": "monsters_men:8",
     "monsterClass": "humanoid",
     "spawnGroup": "odair",
     "phraseID": "odair1"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=odair.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=odair.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=odair.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=odair.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
