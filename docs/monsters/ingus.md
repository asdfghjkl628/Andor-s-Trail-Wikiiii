---
description: "Ingus is a non-player character (NPC) in Andor's Trail, found in Remgard. Starts A difference of opinion."
---

# ![](../assets/icons/monsters/monsters_rltiles1_94.png){ .sprite } Ingus

**Where to find Ingus:** Remgard: [Remgard 0](../maps/remgard0.md#pin-npc-ingus)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_94.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Starts [A difference of opinion](../quests/sisterfight.md) |
| **Found in** | Remgard |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [A difference of opinion](../quests/sisterfight.md): stage 10

## Dialogue simulator

Set your quest stages and items, then talk to Ingus. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/ingus.json" data-npc="Ingus" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (21 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-ingus"></span>**`ingus`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 10 of [A difference of opinion](../quests/sisterfight.md#stage-10))* → [ingus_r1](#d-ingus_r1)
    - branch 2 → [ingus_1](#d-ingus_1)

    <span id="d-ingus_r1"></span>**`ingus_r1`** Ingus: “Hello again. I hope you enjoy your stay in Remgard.”

    - Next → [ingus_speak1](#d-ingus_speak1)

    <span id="d-ingus_1"></span>**`ingus_1`** Ingus: “Hello there. I don't think I have seen you here in Remgard before.”

    - Next → [ingus_speak1](#d-ingus_speak1)

    <span id="d-ingus_speak1"></span>**`ingus_speak1`** Ingus: “How may I help you?”

    - “What is there to do around here?” → [ingus_2](#d-ingus_2)
    - “Is there a shop in town?” → [ingus_s1](#d-ingus_s1)
    - “What is happening around town?” → [ingus_2](#d-ingus_2)

    <span id="d-ingus_2"></span>**`ingus_2`** Ingus: “Oh, there's not much happening around here. We try to keep the town as peaceful as possible.”

    - Next → [ingus_3](#d-ingus_3)

    <span id="d-ingus_s1"></span>**`ingus_s1`** Ingus: “Shop? Oh yes, of course. There's Rothses' and Arnal's shops right there. [Ingus points to the two nearby houses to the west]”

    - Next → [ingus_s2](#d-ingus_s2)

    <span id="d-ingus_3"></span>**`ingus_3`** Ingus: “We don't get many visitors up here in the mountains.”

    - Next → [ingus_4s](#d-ingus_4s)

    <span id="d-ingus_s2"></span>**`ingus_s2`** Ingus: “Also, if you have the coin, you can always spend it in the tavern down in town.”

    - “Thank you. What is happening around town?” → [ingus_2](#d-ingus_2)
    - “Thank you, goodbye.” → *conversation ends*

    <span id="d-ingus_4s"></span>**`ingus_4s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 45 of [What is that stench?](../quests/remgard2.md#stage-45))* → [ingus_4b](#d-ingus_4b)
    - branch 2 → [ingus_4a](#d-ingus_4a)

    <span id="d-ingus_4b"></span>**`ingus_4b`** Ingus: “Hopefully, we'll get a few more visitors now that you've helped us with figuring out what happened to the people that went missing.”

    - “You are welcome. Anything else?” → [ingus_t3](#d-ingus_t3)
    - “Is there a shop in town?” → [ingus_s1](#d-ingus_s1)

    <span id="d-ingus_4a"></span>**`ingus_4a`** Ingus: “However, lately there has been some trouble here in town.”

    - “What trouble?” → [ingus_t1](#d-ingus_t1)
    - “Never mind that, is there a shop in town?” → [ingus_s1](#d-ingus_s1)

    <span id="d-ingus_t3"></span>**`ingus_t3`** Ingus: “Well, there's always the Elwille sisters, fighting as always.”

    - Next → [ingus_t4s](#d-ingus_t4s)

    <span id="d-ingus_t1"></span>**`ingus_t1`** Ingus: “Oh, I don't know much about it. The guards say they have seen strange signs outside town, and some people have gone missing.”

    - Next → [ingus_t2](#d-ingus_t2)

    <span id="d-ingus_t4s"></span>**`ingus_t4s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 71 of [A difference of opinion](../quests/sisterfight.md#stage-71))* → [ingus_q1](#d-ingus_q1)
    - branch 2 → [ingus_t4](#d-ingus_t4)

    <span id="d-ingus_t2"></span>**`ingus_t2`** Ingus: “I try to keep out of it though. Sounds like trouble to me.”

    - “Anything else?” → [ingus_t3](#d-ingus_t3)
    - “Thank you, goodbye.” → *conversation ends*

    <span id="d-ingus_q1"></span>**`ingus_q1`** Ingus: “Unfortunately, for whatever reason, people that live in their neighborhood have been reporting the situation between the two of them has recently become more ... shall we say ... 'noticeable'.”

    - Next → [ingus_q2](#d-ingus_q2)

    <span id="d-ingus_t4"></span>**`ingus_t4`** Ingus: “Last night, they must have kept the whole town awake, the way they were shouting at each other.”

    - “What are they fighting about?” → [ingus_t5](#d-ingus_t5)

    <span id="d-ingus_q2"></span>**`ingus_q2`** Ingus: “I'm afraid that if they don't resolve their differences soon on their own, that the city council will have to act and resolve the matter for them.”

    - Next → [ingus_q3](#d-ingus_q3)

    <span id="d-ingus_t5"></span>**`ingus_t5`** Ingus: “Oh ... nothing ... everything. I don't know. No one really puts much weight in their squabbling.”

    - Next → [ingus_t6](#d-ingus_t6)

    <span id="d-ingus_q3"></span>**`ingus_q3`** Ingus: “It wouldn't be the first time the city council had to intervene in private matters that got out of hand.”


    <span id="d-ingus_t6"></span>**`ingus_t6`** Ingus: “They live in one of the cabins on the southern shore. [Ingus points to the south]” — **effects:** sets stage 10 of [A difference of opinion](../quests/sisterfight.md#stage-10)

    - “Thank you, I might go visit them. Goodbye.” → *conversation ends*
    - “Thank you. Goodbye.” → *conversation ends*
    - “Thank you. I wanted to ask you, is there a shop in town?” → [ingus_s1](#d-ingus_s1)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 7 lines changed<br>· text: “They live in one of the cabins on the southern shore. *Ingus points t…” → “They live in one of the cabins on the southern shore. [Ingus points t…”<br>· text: “Shop? Oh yes, of course. There's Rothses' and Arnal's shops right the…” → “Shop? Oh yes, of course. There's Rothses' and Arnal's shops right the…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `ingus` |
    | Type (wiki) | NPC |
    | Spawn group | `ingus` |
    | Loot table | – |
    | Conversation | `ingus` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:94` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "ingus",
     "name": "Ingus",
     "iconID": "monsters_rltiles1:94",
     "monsterClass": "humanoid",
     "spawnGroup": "ingus",
     "phraseID": "ingus"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ingus.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ingus.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ingus.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ingus.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
