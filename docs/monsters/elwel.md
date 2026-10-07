---
description: "Elwel is a non-player character (NPC) in Andor's Trail, found in Remgard."
---

# ![](../assets/icons/monsters/monsters_ld1_188.png){ .sprite } Elwel

**Where to find Elwel:** Remgard: [remgard_villager5](../maps/remgard_villager5.md#pin-npc-elwel)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_188.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Remgard |
| **Entry ID** | `elwel` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [A difference of opinion](../quests/sisterfight.md): stage 21

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Elwel. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/elwel.json" data-npc="Elwel" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (6 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-elwel"></span>**`elwel`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 71 of [A difference of opinion](../quests/sisterfight.md#stage-71))* → [elwel_4](#d-elwel_4)
    - branch 2 *(if reached stage 20 of [A difference of opinion](../quests/sisterfight.md#stage-20))* → [elwel_3](#d-elwel_3)
    - branch 3 → [elwel_1](#d-elwel_1)

    <span id="d-elwel_4"></span>**`elwel_4`** Elwel: “Now look what you did!” — **effects:** sets stage 21 of [A difference of opinion](../quests/sisterfight.md#stage-21)

    - Next → [elwyl_2](#d-elwyl_2)

    <span id="d-elwel_3"></span>**`elwel_3`** Elwel: “I saw you talking to that cursed sister of mine. Don't listen to her, she always tries her best to portray me in the worst way possible.” — **effects:** sets stage 21 of [A difference of opinion](../quests/sisterfight.md#stage-21)


    <span id="d-elwel_1"></span>**`elwel_1`** Elwel: “Go away, I don't want to talk to you!”

    - “Wow, you're the friendly type, aren't you?” → [elwel_2](#d-elwel_2)
    - “Goodbye.” → *conversation ends*

    <span id="d-elwyl_2"></span>**`elwyl_2`** Elwel: “Bah. Leave, before I call the guards over here!”


    <span id="d-elwel_2"></span>**`elwel_2`** Elwel: “[Elwel mutters to herself] Stupid kids...”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines changed<br>· text: “(Elwel mutters to herself) Stupid kids ..” → “[Elwel mutters to herself] Stupid kids...” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `elwel` |
    | Spawn group | `elwel` |
    | Loot table | – |
    | Conversation | `elwel` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:188` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "elwel",
     "name": "Elwel",
     "iconID": "monsters_ld1:188",
     "monsterClass": "humanoid",
     "spawnGroup": "elwel",
     "phraseID": "elwel"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elwel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elwel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elwel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elwel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
