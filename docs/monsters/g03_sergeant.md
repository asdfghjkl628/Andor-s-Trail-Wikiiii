---
description: "Feygard patrol sergeant is a non-player character (NPC) in Andor's Trail, found in Crackshot hideout 3."
---

# ![](../assets/icons/monsters/monsters_rltiles1_76.png){ .sprite } Feygard patrol sergeant

**Where to find Feygard patrol sergeant:** [Crackshot hideout 3](../maps/crackshot_hideout3.md#pin-npc-g03_sergeant)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_76.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Crackshot hideout 3 |
| **Entry ID** | `g03_sergeant` |
| **Introduced** | [v0.7.8](../versions/0.7.8.md) |

</div>

## Quests

- [The ruthless Crackshot](../quests/Thieves03.md): stages 30, 31, 32
- [Thieves story flags (hidden flag)](../quests/thieves_hidden.md): stage 90

## Dialogue simulator

Set your quest stages and items, then talk to Feygard patrol sergeant. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/FeygardSerg_guild03_select.json" data-npc="Feygard patrol sergeant" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (14 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-FeygardSerg_guild03_select"></span>**`FeygardSerg_guild03_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if killed 1× [Crackshot](../monsters/g03_crackshot.md))* → [FeygardSerg_guild03_dead](#d-FeygardSerg_guild03_dead)
    - branch 2 *(if reached stage 31 of [The ruthless Crackshot](../quests/Thieves03.md#stage-31))* → [FeygardSerg_guild03_9b](#d-FeygardSerg_guild03_9b)
    - branch 3 *(if reached stage 30 of [The ruthless Crackshot](../quests/Thieves03.md#stage-30))* → [FeygardSerg_guild03_3](#d-FeygardSerg_guild03_3)
    - branch 4 → [FeygardSerg_guild03_1](#d-FeygardSerg_guild03_1)

    <span id="d-FeygardSerg_guild03_dead"></span>**`FeygardSerg_guild03_dead`** Feygard patrol sergeant: “You ... Argh ... [The sergeant takes one final breath and then dies. You should have come earlier. Now you will never get to know what he wanted to tell you.]” — **effects:** removes monsters from crackshot_hideout3, sets stage 90 of [Thieves story flags (hidden flag)](../quests/thieves_hidden.md#stage-90)


    <span id="d-FeygardSerg_guild03_9b"></span>**`FeygardSerg_guild03_9b`** Feygard patrol sergeant: “Kid, why are you still here? Leave me, I'm just resting a bit.”

    - “Don't be rude! I'm here to help you. Please leave and go to a safer place.” → [FeygardSerg_guild03_10](#d-FeygardSerg_guild03_10)
    - “Calm down. Take these supplies and call backup!” *(if hand over 1× [Cooked meat](../items/meat_cooked.md))* → [FeygardSerg_guild03_10](#d-FeygardSerg_guild03_10)

    <span id="d-FeygardSerg_guild03_3"></span>**`FeygardSerg_guild03_3`** Feygard patrol sergeant: “My whole patrol is dead! Why do you think you have any chance of success?”

    - “I managed to reach this place. Is that not enough for you?” → [FeygardSerg_guild03_4a](#d-FeygardSerg_guild03_4a)
    - “I'm not here to discuss that with you.” → [FeygardSerg_guild03_4b](#d-FeygardSerg_guild03_4b)

    <span id="d-FeygardSerg_guild03_1"></span>**`FeygardSerg_guild03_1`** [Feygard patrol sergeant](../monsters/g03_sergeant.md): “(Gives you a surprised look). How ...? Who are you kid?”

    - “Eh ... I am ...” → [FeygardSerg_guild03_2](#d-FeygardSerg_guild03_2)
    - “That doesn't ...” → [FeygardSerg_guild03_2](#d-FeygardSerg_guild03_2)

    <span id="d-FeygardSerg_guild03_10"></span>**`FeygardSerg_guild03_10`** Feygard patrol sergeant: “Agh, thank you. You are valiant, kid. I hope to see you when we are both out of here. I'll invite you for a drink!” — **effects:** sets stage 32 of [The ruthless Crackshot](../quests/Thieves03.md#stage-32), removes monsters from crackshot_hideout3

    - “OK, thank you. Now I have to run.” → *NPC leaves*
    - “Yeah, sounds good. For the glory of Feygard I'll avenge your mates!” → *NPC leaves*

    <span id="d-FeygardSerg_guild03_4a"></span>**`FeygardSerg_guild03_4a`** Feygard patrol sergeant: “It's your life, do whatever you want.”

    - “Please tell me what do you know about the current situation.” → [FeygardSerg_guild03_5](#d-FeygardSerg_guild03_5)

    <span id="d-FeygardSerg_guild03_4b"></span>**`FeygardSerg_guild03_4b`** Feygard patrol sergeant: “Indeed, I don't know why are you here!”

    - Next → [FeygardSerg_guild03_4a](#d-FeygardSerg_guild03_4a)

    <span id="d-FeygardSerg_guild03_2"></span>**`FeygardSerg_guild03_2`** Feygard patrol sergeant: “Wait! That's not actually important. Leave this dangerous place, right now!” — **effects:** sets stage 30 of [The ruthless Crackshot](../quests/Thieves03.md#stage-30)

    - “You are right. It would be better to leave.” → *conversation ends*
    - “Hah! No way, I won't give up.” → [FeygardSerg_guild03_3](#d-FeygardSerg_guild03_3)
    - “I'm here because ... I'm here to help you!” → [FeygardSerg_guild03_3](#d-FeygardSerg_guild03_3)

    <span id="d-FeygardSerg_guild03_5"></span>**`FeygardSerg_guild03_5`** Feygard patrol sergeant: “I don't know much. Only that me and my patrol were sent here to arrest a murderer. But what we found was unexpected.”

    - “Unexpected?” → [FeygardSerg_guild03_6](#d-FeygardSerg_guild03_6)

    <span id="d-FeygardSerg_guild03_6"></span>**`FeygardSerg_guild03_6`** Feygard patrol sergeant: “We reached these passages via a forest cavern, and went through the beasts without any major problem. Suddenly, the suspect appeared with a group of men, probably his allies or subordinates ...”

    - Next → [FeygardSerg_guild03_7](#d-FeygardSerg_guild03_7)

    <span id="d-FeygardSerg_guild03_7"></span>**`FeygardSerg_guild03_7`** Feygard patrol sergeant: “Those people were fast. Very fast and very dangerous. They killed them! My fellows, all of them defeated!”

    - Next → [FeygardSerg_guild03_8](#d-FeygardSerg_guild03_8)

    <span id="d-FeygardSerg_guild03_8"></span>**`FeygardSerg_guild03_8`** Feygard patrol sergeant: “I managed to get rid of most of them, but I'm severely wounded and unable to continue ...”

    - Next → [FeygardSerg_guild03_9a](#d-FeygardSerg_guild03_9a)

    <span id="d-FeygardSerg_guild03_9a"></span>**`FeygardSerg_guild03_9a`** Feygard patrol sergeant: “Don't you understand? You must leave this place before you can't. He's playing with us!” — **effects:** sets stage 31 of [The ruthless Crackshot](../quests/Thieves03.md#stage-31)

    - “You are right. I will leave.” → *conversation ends*
    - “Take these supplies and leave. I'll avenge your mates.” *(if hand over 1× [Cooked meat](../items/meat_cooked.md))* → [FeygardSerg_guild03_10](#d-FeygardSerg_guild03_10)
    - “Don't worry. You must report this before it is too late. I'll go there instead of you.” → [FeygardSerg_guild03_10](#d-FeygardSerg_guild03_10)



## Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added<br>Dialogue: 14 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `g03_sergeant` |
    | Spawn group | `g03_sergeant` |
    | Loot table | – |
    | Conversation | `FeygardSerg_guild03_select` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_rltiles1:76` |
    | Defined in | `res/raw/monsterlist_omicronrg9.json` |

    Raw data:

    ```json
    {
     "id": "g03_sergeant",
     "name": "Feygard patrol sergeant",
     "iconID": "monsters_rltiles1:76",
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "spawnGroup": "g03_sergeant",
     "phraseID": "FeygardSerg_guild03_select"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g03_sergeant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g03_sergeant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g03_sergeant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g03_sergeant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
