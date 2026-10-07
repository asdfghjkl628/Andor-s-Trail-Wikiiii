---
description: "Krell is a non-player character (NPC) in Andor's Trail, found in Remgard."
---

# ![](../assets/icons/monsters/monsters_men2_6.png){ .sprite } Krell

**Where to find Krell:** Remgard: [remgard_tavern0](../maps/remgard_tavern0.md#pin-npc-krell)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men2_6.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Remgard |
| **Entry ID** | `krell` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [Everything in order](../quests/remgard.md): stages 62, 70

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Krell. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/krell.json" data-npc="Krell" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (25 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-krell"></span>**`krell`** *(silent check: the first matching branch below is taken)*

    - branch 1 → [krell_1](#d-krell_1)

    <span id="d-krell_1"></span>**`krell_1`** Krell: “Hey there. I am master Krell of the Knights of Elythom. How may we be of service?”

    - “Knights of Elythom? What's that?” → [krell_knights_1](#d-krell_knights_1)
    - “I was sent by Jhaeld to ask about the missing people.” *(if reached stage 52 of [Everything in order](../quests/remgard.md#stage-52))* → [krell_jhaeld1](#d-krell_jhaeld1)
    - “What do you do around here?” → [krell_2](#d-krell_2)

    <span id="d-krell_knights_1"></span>**`krell_knights_1`** Krell: “We are an order of knights that hail from Brimhaven.”

    - Next → [krell_knights_2](#d-krell_knights_2)

    <span id="d-krell_jhaeld1"></span>**`krell_jhaeld1`** Krell: “Shh, not so loud!”

    - Next → [krell_jhaeld2](#d-krell_jhaeld2)

    <span id="d-krell_2"></span>**`krell_2`** Krell: “Me and my band of knights are just visiting Remgard in ... shall we say ... unfinished business.”

    - Next → [krell_3](#d-krell_3)

    <span id="d-krell_knights_2"></span>**`krell_knights_2`** Krell: “You should visit our compound in Brimhaven, if you ever make your way there.”

    - Next → [krell_knights_3](#d-krell_knights_3)

    <span id="d-krell_jhaeld2"></span>**`krell_jhaeld2`** Krell: “Yes, we have heard the reports that people have gone missing here in Remgard. Most ... unfortunate.”

    - Next → [krell_jhaeld3](#d-krell_jhaeld3)

    <span id="d-krell_3"></span>**`krell_3`** Krell: “As to the nature of our business here, that is something I would rather not disclose.”

    - Next → [krell_4](#d-krell_4)

    <span id="d-krell_knights_3"></span>**`krell_knights_3`** Krell: “We serve all types of clients, from the wealthiest to even the poorest of poor.”

    - Next → [krell_knights_4](#d-krell_knights_4)

    <span id="d-krell_jhaeld3"></span>**`krell_jhaeld3`** Krell: “We even had one of our knights disappear on us. Now, due to the nature of our order, I presume you can see how that puts us in a ... peculiar situation.”

    - Next → [krell_jhaeld4](#d-krell_jhaeld4)

    <span id="d-krell_4"></span>**`krell_4`** Krell: “We serve the order of Elythom.”

    - “What's that?” → [krell_knights_1](#d-krell_knights_1)
    - “Jhaeld sent me to ask about the missing people.” *(if reached stage 52 of [Everything in order](../quests/remgard.md#stage-52))* → [krell_jhaeld1](#d-krell_jhaeld1)

    <span id="d-krell_knights_4"></span>**`krell_knights_4`** Krell: “Regardless, we always get the job done.”

    - “What types of work do you do?” → [krell_knights_5](#d-krell_knights_5)

    <span id="d-krell_jhaeld4"></span>**`krell_jhaeld4`** Krell: “You see, usually it is us knights that find ... missing people. Now, we have had one of our own disappear. This has never happened before, and we are really unsure about what to do about it.”

    - Next → [krell_jhaeld5](#d-krell_jhaeld5)

    <span id="d-krell_knights_5"></span>**`krell_knights_5`** Krell: “Mostly, we help people get back gold that other people owe them.”

    - Next → [krell_knights_6](#d-krell_knights_6)

    <span id="d-krell_jhaeld5"></span>**`krell_jhaeld5`** Krell: “Granted, people in our order have succumbed in combat to greater foes, but to just ... disappear without a trace, that's unheard of.”

    - Next → [krell_jhaeld6](#d-krell_jhaeld6)

    <span id="d-krell_knights_6"></span>**`krell_knights_6`** Krell: “We also help people find ... erm ... people that have gone missing.”

    - “About that, Jhaeld sent me to ask about the missing people.” *(if reached stage 52 of [Everything in order](../quests/remgard.md#stage-52))* → [krell_jhaeld1](#d-krell_jhaeld1)
    - “Good luck with that.” → *conversation ends*

    <span id="d-krell_jhaeld6"></span>**`krell_jhaeld6`** Krell: “We have a strong connection to each other, and to have someone leave the order would be unthinkable.”

    - Next → [krell_jhaeld7](#d-krell_jhaeld7)

    <span id="d-krell_jhaeld7"></span>**`krell_jhaeld7`** Krell: “As you can see, this puts us in a difficult situation.”

    - “What do you know about the knight that is missing?” → [krell_jhaeld8](#d-krell_jhaeld8)
    - “Is there anything else you have found out that you didn't tell the guards earlier?” → [krell_jhaeld8](#d-krell_jhaeld8)

    <span id="d-krell_jhaeld8"></span>**`krell_jhaeld8`** Krell: “Well, we told the guards everything we know so far. They also seem to find this situation rather embarrassing, that they can't even keep a knight safe here in their town.”

    - Next → [krell_jhaeld9](#d-krell_jhaeld9)

    <span id="d-krell_jhaeld9"></span>**`krell_jhaeld9`** Krell: “We have no clues apart from the fact that she is missing, unfortunately. Where our sister knight is, is still a mystery to us.”

    - Next → [krell_jhaeld_s_1](#d-krell_jhaeld_s_1)

    <span id="d-krell_jhaeld_s_1"></span>**`krell_jhaeld_s_1`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 62 of [Everything in order](../quests/remgard.md#stage-62)

    - branch 1 *(if reached stage 61 of [Everything in order](../quests/remgard.md#stage-61))* → [krell_jhaeld_s_2](#d-krell_jhaeld_s_2)
    - branch 2 → [krell_jhaeld10](#d-krell_jhaeld10)

    <span id="d-krell_jhaeld_s_2"></span>**`krell_jhaeld_s_2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 63 of [Everything in order](../quests/remgard.md#stage-63))* → [krell_jhaeld_s_3](#d-krell_jhaeld_s_3)
    - branch 2 → [krell_jhaeld10](#d-krell_jhaeld10)

    <span id="d-krell_jhaeld10"></span>**`krell_jhaeld10`** Krell: “For the sake of our order's reputation, please keep this to yourself if possible. We wouldn't want people to get the perception that the Knights of Elythom can be weakened in any way.”


    <span id="d-krell_jhaeld_s_3"></span>**`krell_jhaeld_s_3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 64 of [Everything in order](../quests/remgard.md#stage-64))* → [krell_jhaeld_s_4](#d-krell_jhaeld_s_4)
    - branch 2 → [krell_jhaeld10](#d-krell_jhaeld10)

    <span id="d-krell_jhaeld_s_4"></span>**`krell_jhaeld_s_4`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 70 of [Everything in order](../quests/remgard.md#stage-70)

    - branch 1 → [krell_jhaeld10](#d-krell_jhaeld10)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 11 lines changed<br>· text: “Me and my band of knights are just visiting Remgard in .. shall we sa…” → “Me and my band of knights are just visiting Remgard in ... shall we s…”<br>· text: “We also help people find .. erm .. people that have gone missing.” → “We also help people find ... erm ... people that have gone missing.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `krell` |
    | Spawn group | `krell` |
    | Loot table | – |
    | Conversation | `krell` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men2:6` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "krell",
     "name": "Krell",
     "iconID": "monsters_men2:6",
     "monsterClass": "humanoid",
     "spawnGroup": "krell",
     "phraseID": "krell"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=krell.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=krell.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=krell.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=krell.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
