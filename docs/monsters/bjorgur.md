---
description: "Bjorgur is a non-player character (NPC) in Andor's Trail, found in Prim. Starts Awoken from slumber."
---

# ![](../assets/icons/monsters/monsters_karvis2_7.png){ .sprite } Bjorgur

**Where to find Bjorgur:** Prim: [blackwater_mountain26](../maps/blackwater_mountain26.md#pin-npc-bjorgur)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_karvis2_7.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Starts [Awoken from slumber](../quests/bjorgur_grave.md) |
| **Found in** | Prim |
| **Entry ID** | `bjorgur` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [Awoken from slumber](../quests/bjorgur_grave.md): stages 10, 15, 50

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Bjorgur. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/bjorgur_start.json" data-npc="Bjorgur" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (16 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-bjorgur_start"></span>**`bjorgur_start`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 50 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-50))* → [bjorgur_return_1](#d-bjorgur_return_1)
    - branch 2 *(if reached stage 15 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-15))* → [bjorgur_return_2](#d-bjorgur_return_2)
    - branch 3 → [bjorgur_1](#d-bjorgur_1)

    <span id="d-bjorgur_return_1"></span>**`bjorgur_return_1`** Bjorgur: “Hello again, friend. Thank you for your assistance with my family grave earlier.”


    <span id="d-bjorgur_return_2"></span>**`bjorgur_return_2`** Bjorgur: “Hello again. Have you investigated if anything has happened to my family grave?”

    - “No, not yet.” → [bjorgur_9](#d-bjorgur_9)
    - “[Lie] I went to check on the grave. Everything seems to be normal. You must be imagining things.” *(if reached stage 60 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-60))* → [bjorgur_return_3](#d-bjorgur_return_3)
    - “What was I supposed to do again?” → [bjorgur_3](#d-bjorgur_3)
    - “Yes. I killed the intruder and restored the dagger to its original place.” *(if reached stage 40 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-40))* → [bjorgur_complete_1](#d-bjorgur_complete_1)

    <span id="d-bjorgur_1"></span>**`bjorgur_1`** Bjorgur: “Hello there. You wouldn't happen to know anything about a grave to the southwest of Prim would you?”

    - “I have been there. I met someone on one of the lower levels.” *(if reached stage 30 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-30))* → [bjorgur_2](#d-bjorgur_2)
    - “What about it?” → [bjorgur_3](#d-bjorgur_3)
    - “No, sorry.” → [bjorgur_3](#d-bjorgur_3)

    <span id="d-bjorgur_9"></span>**`bjorgur_9`** Bjorgur: “Please hurry, and return here to tell me of your progress once you find out something.”


    <span id="d-bjorgur_return_3"></span>**`bjorgur_return_3`** Bjorgur: “Nothing you say? But I was sure something must have happened over there. Anyway. Thank you for checking it for me.”


    <span id="d-bjorgur_3"></span>**`bjorgur_3`** Bjorgur: “My family grave is located in the tomb to the southwest of Prim right outside the Elm mine. I fear that something has disturbed the peace there.”

    - Next → [bjorgur_4](#d-bjorgur_4)

    <span id="d-bjorgur_complete_1"></span>**`bjorgur_complete_1`** Bjorgur: “An intruder? Oh thank you for dealing with this matter.”

    - Next → [bjorgur_complete_2](#d-bjorgur_complete_2)

    <span id="d-bjorgur_2"></span>**`bjorgur_2`** Bjorgur: “You have been there?”

    - Next → [bjorgur_3](#d-bjorgur_3)

    <span id="d-bjorgur_4"></span>**`bjorgur_4`** Bjorgur: “You see, my grandfather was very fond of a particular valuable dagger that our family used to possess. He wore it with him always.”

    - Next → [bjorgur_5](#d-bjorgur_5)

    <span id="d-bjorgur_complete_2"></span>**`bjorgur_complete_2`** Bjorgur: “You say you restored the dagger to it's original place? Thank you. Now I might be able to rest during the nights ahead.”

    - Next → [bjorgur_complete_3](#d-bjorgur_complete_3)

    <span id="d-bjorgur_5"></span>**`bjorgur_5`** Bjorgur: “The dagger would of course attract treasure hunters, but up until now we seem to have been spared of this.”

    - Next → [bjorgur_6](#d-bjorgur_6)

    <span id="d-bjorgur_complete_3"></span>**`bjorgur_complete_3`** Bjorgur: “Thank you again. I'm afraid I can't give you anything except my gratitude. You should go see my relatives in Feygard if you get the chance to travel up there.” — **effects:** sets stage 50 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-50)


    <span id="d-bjorgur_6"></span>**`bjorgur_6`** Bjorgur: “Now I fear something has happened to the grave. I have not been sleeping well the last couple of nights, and I am sure this must be the cause.” — **effects:** sets stage 10 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-10)

    - Next → [bjorgur_7](#d-bjorgur_7)

    <span id="d-bjorgur_7"></span>**`bjorgur_7`** Bjorgur: “You wouldn't happen to want to go check on the grave and see what is happening over there?”

    - “Sure. I will go check on your parents grave.” → [bjorgur_8](#d-bjorgur_8)
    - “A treasure you say? I'm interested.” → [bjorgur_8](#d-bjorgur_8)
    - “I have actually already been there and restored the dagger to its original place.” *(if reached stage 40 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-40))* → [bjorgur_complete_2](#d-bjorgur_complete_2)

    <span id="d-bjorgur_8"></span>**`bjorgur_8`** Bjorgur: “Thank you. Please see if anything has happened to the grave, and what could be the cause of my nightly anxiety.” — **effects:** sets stage 15 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-15)

    - Next → [bjorgur_9](#d-bjorgur_9)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 4 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `bjorgur` |
    | Spawn group | `bjorgur` |
    | Loot table | – |
    | Conversation | `bjorgur_start` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:7` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "bjorgur",
     "name": "Bjorgur",
     "iconID": "monsters_karvis2:7",
     "monsterClass": "humanoid",
     "spawnGroup": "bjorgur",
     "phraseID": "bjorgur_start"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bjorgur.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bjorgur.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bjorgur.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bjorgur.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
