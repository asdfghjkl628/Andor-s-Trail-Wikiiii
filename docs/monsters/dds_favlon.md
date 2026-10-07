---
description: "Favlon is a non-player character (NPC) in Andor's Trail, found in Nw sullengard 1."
---

# ![](../assets/icons/monsters/monsters_rltiles1_5.png){ .sprite } Favlon

**Where to find Favlon:** [Nw sullengard 1](../maps/nw_sullengard_1.md#pin-npc-dds_favlon)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_5.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Nw sullengard 1 |
| **Entry ID** | `dds_favlon` |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Quests

- [Shadows](../quests/shadows.md): stages 130, 140

## Dialogue simulator

Set your quest stages and items, then talk to Favlon. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/dds_favlon.json" data-npc="Favlon" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (16 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-dds_favlon"></span>**`dds_favlon`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 140 of [Shadows](../quests/shadows.md#stage-140))* → [dds_favlon_2](#d-dds_favlon_2)
    - branch 2 → [dds_favlon_10](#d-dds_favlon_10)

    <span id="d-dds_favlon_2"></span>**`dds_favlon_2`** Favlon: “Ah, my brave Shadow warrior. I hope you could help Borvis.”

    - “Not yet.” *(if NOT reached stage 250 of [Shadows](../quests/shadows.md#stage-250))* → *conversation ends*
    - “Yes, we have saved the world.” *(if reached stage 250 of [Shadows](../quests/shadows.md#stage-250))* → *conversation ends*
    - “Your 'blessings' has worn off too early. Could you give them again?” *(if reached stage 140 of [Shadows](../quests/shadows.md#stage-140); NOT reached stage 160 of [Shadows](../quests/shadows.md#stage-160); NOT affected by fatigue1)* → [dds_favlon_90](#d-dds_favlon_90)

    <span id="d-dds_favlon_10"></span>**`dds_favlon_10`** Favlon: “By the Shadow - a kid! Here? How? Why?”

    - “Jolnor sent me to find you here.” → [dds_favlon_12](#d-dds_favlon_12)

    <span id="d-dds_favlon_90"></span>**`dds_favlon_90`** Favlon: “That's no problem at all.”

    - “I'm glad about that.” → [dds_favlon_92](#d-dds_favlon_92)

    <span id="d-dds_favlon_12"></span>**`dds_favlon_12`** Favlon: “He did?”

    - “Borvis wants me to help him take care of a renegade Shadow priest. So, he asked me to get some 'blessings' - of which…” → [dds_favlon_14](#d-dds_favlon_14)

    <span id="d-dds_favlon_92"></span>**`dds_favlon_92`** Favlon: “It'll just cost you another 10 cooked meat.”

    - “Sure. Here, enjoy.” *(if carry 10× [Cooked meat](../items/meat_cooked.md))* → [dds_favlon_50](#d-dds_favlon_50)
    - “I don't have that much with me. I'll be back.” *(if NOT carry 10× [Cooked meat](../items/meat_cooked.md))* → *conversation ends*

    <span id="d-dds_favlon_14"></span>**`dds_favlon_14`** Favlon: “And Jolnor says I can bestow them?”

    - “Exactly. I need Fatigue and Life Drain.” → [dds_favlon_20](#d-dds_favlon_20)

    <span id="d-dds_favlon_50"></span>**`dds_favlon_50`** Favlon: “I'll eat while I work the chants. You are sure that you still want them?”

    - “Yes, I'm sure.” *(if hand over 10× [Cooked meat](../items/meat_cooked.md))* → [dds_favlon_60](#d-dds_favlon_60)
    - “Maybe I'd better think about it again.” → *conversation ends*

    <span id="d-dds_favlon_20"></span>**`dds_favlon_20`** Favlon: “Is Borvis that weak that he can't get them himself?”

    - “He said a Shadow warrior is needed, not a Shadow priest.” → [dds_favlon_30](#d-dds_favlon_30)

    <span id="d-dds_favlon_60"></span>**`dds_favlon_60`** Favlon: “Here you go. Take them to Borvis with care.” — **effects:** applies condition fatigue1, applies condition life_drain, sets stage 140 of [Shadows](../quests/shadows.md#stage-140)

    - “Thank you. Bye.” → *conversation ends*
    - “Ugh! What a terrible feeling. Thanks nevertheless.” → [dds_favlon_70](#d-dds_favlon_70)

    <span id="d-dds_favlon_30"></span>**`dds_favlon_30`** Favlon: “A likely story!”

    - “So you can't do it?” → [dds_favlon_40](#d-dds_favlon_40)

    <span id="d-dds_favlon_70"></span>**`dds_favlon_70`** Favlon: “Take care! The return journey will be dangerous”

    - “See you!” → [dds_favlon_80](#d-dds_favlon_80)

    <span id="d-dds_favlon_40"></span>**`dds_favlon_40`** Favlon: “No insults, please. Of course I can!”

    - Next → [dds_favlon_42](#d-dds_favlon_42)

    <span id="d-dds_favlon_80"></span>**`dds_favlon_80`** Favlon: “[Muttering] Sending a kid to do a priest's job?! How lazy!”


    <span id="d-dds_favlon_42"></span>**`dds_favlon_42`** Favlon: “Do you have any cooked meat? I've been living on berries for so long, some meat can give me strength.”

    - “How many do you need?” → [dds_favlon_44](#d-dds_favlon_44)

    <span id="d-dds_favlon_44"></span>**`dds_favlon_44`** Favlon: “Ten should be enough.” — **effects:** sets stage 130 of [Shadows](../quests/shadows.md#stage-130)

    - “OK, I have it here.” *(if carry 10× [Cooked meat](../items/meat_cooked.md))* → [dds_favlon_50](#d-dds_favlon_50)
    - “I have to fetch some.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 16 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `dds_favlon` |
    | Spawn group | `dds_favlon` |
    | Loot table | – |
    | Conversation | `dds_favlon` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:5` |
    | Defined in | `res/raw/monsterlist_darknessanddaylight.json` |

    Raw data:

    ```json
    {
     "id": "dds_favlon",
     "name": "Favlon",
     "iconID": "monsters_rltiles1:5",
     "monsterClass": "humanoid",
     "spawnGroup": "dds_favlon",
     "phraseID": "dds_favlon"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_favlon.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_favlon.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_favlon.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_favlon.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
