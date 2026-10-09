---
description: "Celdar is a non-player character (NPC) in Andor's Trail, found in Crossroads Guardhouse."
---

# ![](../assets/icons/monsters/monsters_rltiles1_94.png){ .sprite } Celdar

**Where to find Celdar:** Crossroads Guardhouse: [Houseatcrossroads 0](../maps/houseatcrossroads0.md#pin-npc-celdar)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_94.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Crossroads Guardhouse |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [Restless in the grave](../quests/mg_restless_grave.md): stage 130
- [Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md): stage 19

## Dialogue simulator

Set your quest stages and items, then talk to Celdar. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/celdar.json" data-npc="Celdar" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (24 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-celdar"></span>**`celdar`** Celdar: “And who might you be? Come to sell me one of those trinkets that you people sell, eh?”

    - Next → [celdar_1](#d-celdar_1)

    <span id="d-celdar_1"></span>**`celdar_1`** Celdar: “No, let me guess - you want to know if I have any items to trade?”

    - Next → [celdar_2](#d-celdar_2)

    <span id="d-celdar_2"></span>**`celdar_2`** Celdar: “Let me tell you something. I do not want to buy anything from you, nor do I want to sell you anything. I just want to be left alone here, now that I have made it all the way to this safe haven.”

    - Next → [celdar_3](#d-celdar_3)

    <span id="d-celdar_3"></span>**`celdar_3`** Celdar: “I have travelled all the way from my home town of Sullengard, and on my way to Brimhaven, I have stopped at this place to get a break from all the commoners that always bother me with their trinkets and whatnots.”

    - Next → [celdar_4](#d-celdar_4)

    <span id="d-celdar_4"></span>**`celdar_4`** Celdar: “So, if you will excuse me, I really need my well deserved rest here. Without you bothering me.”

    - “OK, I will leave.” → *conversation ends*
    - “Wow, you're the friendly type aren't you?” → [celdar_5](#d-celdar_5)
    - “I should put my sword through you for talking like that.” → [celdar_5](#d-celdar_5)
    - “I'm here to give you a gift from Eryndor. He died, but I was told to give you something from him.” *(if reached stage 123 of [Restless in the grave](../quests/mg_restless_grave.md#stage-123); NOT reached stage 130 of [Restless in the grave](../quests/mg_restless_grave.md#stage-130))* → [celdar_musicbox_10](#d-celdar_musicbox_10)

    <span id="d-celdar_5"></span>**`celdar_5`** Celdar: “Are you still around? Did you not listen to what I said?”


    <span id="d-celdar_musicbox_10"></span>**`celdar_musicbox_10`** Celdar: “Eryndor? That scoundrel finally got what was coming to him, did he? And now you're here, dangling a prize in front of me, expecting what? Gratitude? Payment? Hah! Whatever trick you think you're playing, I'm not biting.”

    - Next → [celdar_musicbox_15](#d-celdar_musicbox_15)

    <span id="d-celdar_musicbox_15"></span>**`celdar_musicbox_15`** [Dummy NPC](../monsters/none.md): “Celdar pauses, and narrows her eyes as she assesses you.”

    - “I have this music box. [Showing it to her.]” → [celdar_musicbox_20](#d-celdar_musicbox_20)

    <span id="d-celdar_musicbox_20"></span>**`celdar_musicbox_20`** [Celdar](../monsters/celdar.md): “Wait... you're serious, aren't you? He actually sent you to bring me the music box? Hmph. That doesn't sound like him. He was always the type to take, not give.”

    - “He wanted to do the right thing.” → [celdar_musicbox_25](#d-celdar_musicbox_25)

    <span id="d-celdar_musicbox_25"></span>**`celdar_musicbox_25`** Celdar: “The right thing? Eryndor always did have a flair for the dramatic, but this... this is unexpected.”

    - Next → [celdar_musicbox_30](#d-celdar_musicbox_30)

    <span id="d-celdar_musicbox_30"></span>**`celdar_musicbox_30`** [Dummy NPC](../monsters/none.md): “While crossing her arms, she begins to study you.”

    - Next → [celdar_musicbox_35](#d-celdar_musicbox_35)

    <span id="d-celdar_musicbox_35"></span>**`celdar_musicbox_35`** [Celdar](../monsters/celdar.md): “I spent years chasing that wretched box, only for him to snatch it out from under me. And now, after death, he decides to hand it over? What, am I supposed to be touched?”

    - Next → [celdar_musicbox_40](#d-celdar_musicbox_40)

    <span id="d-celdar_musicbox_40"></span>**`celdar_musicbox_40`** [Dummy NPC](../monsters/none.md): “She scoffs but reaches out for the box.”

    - “You reach out, your hands meet with the mysterious music box held between your hands and she takes it from you.” *(if hand over 1× [Mysterious music box](../items/mg_music_box.md))* → [celdar_musicbox_45](#d-celdar_musicbox_45)
    - “I can't believe this, but I forgot to bring the music box. Sorry. I will have to come back later. Stay here.” *(if NOT carry 1× [Mysterious music box](../items/mg_music_box.md))* → *conversation ends*
    - “I just gave you that music box...” *(if reached stage 19 of [Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md#stage-19); NOT reached stage 130 of [Restless in the grave](../quests/mg_restless_grave.md#stage-130))* → [celdar_musicbox_50](#d-celdar_musicbox_50)

    <span id="d-celdar_musicbox_45"></span>**`celdar_musicbox_45`** [Celdar](../monsters/celdar.md): “Hmph. Fine. If he truly meant it, then I'll take it. Not that it changes anything. Eryndor and I were never friends, and his little gesture won't rewrite history. But... at least he finally understood what was mine to begin with.” — **effects:** sets stage 19 of [Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md#stage-19)

    - Next → [celdar_musicbox_50](#d-celdar_musicbox_50)

    <span id="d-celdar_musicbox_50"></span>**`celdar_musicbox_50`** [Dummy NPC](../monsters/none.md): “She examines the box for a moment, running a hand over it before giving you a final look.”

    - Next → [celdar_musicbox_55](#d-celdar_musicbox_55)

    <span id="d-celdar_musicbox_55"></span>**`celdar_musicbox_55`** [Celdar](../monsters/celdar.md): “Here, take this longsword, I have no need for it. But...” — **effects:** gives 1× [Blood seeker](../items/bloodseeker.md), sets stage 130 of [Restless in the grave](../quests/mg_restless_grave.md#stage-130)

    - Next → [celdar_musicbox_60](#d-celdar_musicbox_60)

    <span id="d-celdar_musicbox_60"></span>**`celdar_musicbox_60`** Celdar: “Tell me, does he rest easy now, or is he still out there, clinging to unfinished business?”

    - “No, he's not at peace. He's still out there, lingering about, bound by unfinished business.” → [celdar_musicbox_65](#d-celdar_musicbox_65)

    <span id="d-celdar_musicbox_65"></span>**`celdar_musicbox_65`** [Dummy NPC](../monsters/none.md): “Celdar exhales sharply, her fingers tightening around the music box as she looks away for a brief moment.”

    - Next → [celdar_musicbox_70](#d-celdar_musicbox_70)

    <span id="d-celdar_musicbox_70"></span>**`celdar_musicbox_70`** [Celdar](../monsters/celdar.md): “Hmph. Figures. The stubborn fool never knew when to let go.”

    - Next → [celdar_musicbox_75](#d-celdar_musicbox_75)

    <span id="d-celdar_musicbox_75"></span>**`celdar_musicbox_75`** [Dummy NPC](../monsters/none.md): “She turns the box over in her hands, her expression briefly unreadable. Then, softer, almost to herself:”

    - Next → [celdar_musicbox_80](#d-celdar_musicbox_80)

    <span id="d-celdar_musicbox_80"></span>**`celdar_musicbox_80`** [Celdar](../monsters/celdar.md): “Chasing relics, chasing victories, chasing debts that can never be repaid... I suppose it doesn't matter now.”

    - Next → [celdar_musicbox_85](#d-celdar_musicbox_85)

    <span id="d-celdar_musicbox_85"></span>**`celdar_musicbox_85`** [Dummy NPC](../monsters/none.md): “She shakes her head, composing herself before glancing at you once more.”

    - Next → [celdar_musicbox_90](#d-celdar_musicbox_90)

    <span id="d-celdar_musicbox_90"></span>**`celdar_musicbox_90`** [Celdar](../monsters/celdar.md): “Well, he made his choices. And I made mine. But... I wouldn't wish that kind of fate on anyone. Not even him.”

    - Next → [celdar_musicbox_95](#d-celdar_musicbox_95)

    <span id="d-celdar_musicbox_95"></span>**`celdar_musicbox_95`** [Dummy NPC](../monsters/none.md): “With that, she straightens her posture, her usual sharpness returning, though the moment of reflection lingers in her eyes.”

    - “I hope that in the future, that music box brings your happiness.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 1 line changed<br>· text: “Let me tell you something son. I do not want to buy anything from you…” → “Let me tell you something. I do not want to buy anything from you, no…” |
| [v0.8.14](../versions/0.8.14.md) | Dialogue: 18 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `celdar` |
    | Type (wiki) | NPC |
    | Spawn group | `celdar` |
    | Loot table | – |
    | Conversation | `celdar` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:94` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "celdar",
     "name": "Celdar",
     "iconID": "monsters_rltiles1:94",
     "monsterClass": "humanoid",
     "spawnGroup": "celdar",
     "phraseID": "celdar"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=celdar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=celdar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=celdar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=celdar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
