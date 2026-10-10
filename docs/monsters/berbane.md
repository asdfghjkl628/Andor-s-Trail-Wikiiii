---
description: "Lord Berbane is a non-player character (NPC) in Andor's Trail, found in Stoutford."
---

# ![](../assets/icons/monsters/monsters_tometik2_42.png){ .sprite } Lord Berbane

**Where to find Lord Berbane:** Stoutford: [Stoutford tavern](../maps/stoutford_tavern.md#pin-npc-berbane)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_tometik2_42.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Stoutford |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Quests

- [Lost girl looking for lost things](../quests/stn_quest_gyra.md): stages 90, 92, 99, 199
- [General story flags (hidden flag)](../quests/nondisplay.md): stage 149
- [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md): stages 44, 45

## Dialogue simulator

Talk to Lord Berbane as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/berbane.json" data-npc="Lord Berbane" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (21 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-berbane"></span>**`berbane`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 45 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-45))* → [berbane_200](#d-berbane_200)
    - branch 2 *(if reached stage 90 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-90))* → [berbane_90](#d-berbane_90)
    - branch 3 *(if reached stage 44 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-44))* → [berbane_100](#d-berbane_100)
    - branch 4 → [berbane_10](#d-berbane_10)

    <span id="d-berbane_200"></span>**`berbane_200`** [Dummy NPC](../monsters/none.md): “Lord Berbane is singing merrily about his heroic deeds.”

    - “Psst. I have something for you.” *(if carry 1× [Stoutford chief's helmet](../items/stoutford_helmet.md))* → [berbane_200_1](#d-berbane_200_1)
    - “Lalala lala lala” → *conversation ends*

    <span id="d-berbane_90"></span>**`berbane_90`** [Dummy NPC](../monsters/none.md): “Lord Berbane looks sadly at his bottle, but still shows no sign of getting up.”

    - “The castle is clean of undead now.” *(if reached stage 47 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-47); reached stage 20 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-20))* → [berbane_100](#d-berbane_100)
    - “Hey, up!” → [berbane_90](#d-berbane_90)

    <span id="d-berbane_100"></span>**`berbane_100`** [Dummy NPC](../monsters/none.md): “Lord Berbane jumps up and cries with a loud voice: SILENCE!”

    - “...?” → [berbane_102](#d-berbane_102)

    <span id="d-berbane_10"></span>**`berbane_10`** [Dummy NPC](../monsters/none.md): “The richly dressed man does not react.”

    - “Who are you?” → [berbane_10](#d-berbane_10)
    - “Yolgen asked me to help clear the castle of undead. Shall we do it together?” *(if reached stage 10 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-10); NOT reached stage 47 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-47))* → [berbane_10](#d-berbane_10)
    - “Gyra found your helmet and asked me to give it to you, so that you could start to clear the castle.” *(if reached stage 70 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-70); carry 1× [Stoutford chief's helmet](../items/stoutford_helmet.md))* → [berbane_20](#d-berbane_20)
    - “The castle is clean of undead now.” *(if reached stage 47 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-47); reached stage 20 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-20))* → [berbane_100](#d-berbane_100)

    <span id="d-berbane_200_1"></span>**`berbane_200_1`** [Lord Berbane](../monsters/berbane.md): “Why are you disturbing my song?”

    - “Gyra found your helmet and asked me to give it to you.” *(if hand over 1× [Stoutford chief's helmet](../items/stoutford_helmet.md))* → [berbane_200_2](#d-berbane_200_2)
    - “Eh, nothing. Sing on.” → [berbane_200](#d-berbane_200)

    <span id="d-berbane_102"></span>**`berbane_102`** [Lord Berbane](../monsters/berbane.md): “[Loud voice] Pay attention and listen everybody! The castle is free! The trembling is over!” — **effects:** sets stage 44 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-44)

    - “...??” → [berbane_110](#d-berbane_110)

    <span id="d-berbane_20"></span>**`berbane_20`** [Lord Berbane](../monsters/berbane.md): “Gyra? My dearest and most eager listener?”

    - “Seems so.” → [berbane_30](#d-berbane_30)

    <span id="d-berbane_200_2"></span>**`berbane_200_2`** Lord Berbane: “Ah yes, one of my helmets. Thank you.”

    - Next → [berbane_200_3](#d-berbane_200_3)

    <span id="d-berbane_110"></span>**`berbane_110`** Lord Berbane: “[Loud voice] My trainee and I, we were in the castle. I demonstrated how to fight properly. Lord Erwyn himself was an especially good demonstration object.”

    - “But...” → [berbane_120](#d-berbane_120)

    <span id="d-berbane_30"></span>**`berbane_30`** Lord Berbane: “Many of my songs are about this magical helmet. But it's all just songs.”

    - “Will you make the songs a reality now?” *(if hand over 1× [Stoutford chief's helmet](../items/stoutford_helmet.md))* → [berbane_32](#d-berbane_32)
    - “I cleared the castle of undead already.” *(if reached stage 47 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-47))* → [berbane_100](#d-berbane_100)

    <span id="d-berbane_200_3"></span>**`berbane_200_3`** Lord Berbane: “Anything else?”

    - “Here you go. You're welcome. No, I don't need a reward. I always like to help without appreciation. Everything is OK.…” → *conversation ends*

    <span id="d-berbane_120"></span>**`berbane_120`** Lord Berbane: “[Loud voice] But we will come to the details later - after the next round.”

    - “No, I have...” → [berbane_130](#d-berbane_130)

    <span id="d-berbane_32"></span>**`berbane_32`** [Dummy NPC](../monsters/none.md): “He sighs and slowly takes the helmet.” — **effects:** sets stage 90 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-90), sets stage 149 of [General story flags (hidden flag)](../quests/nondisplay.md#stage-149)

    - “Let's go now.” → [berbane_90](#d-berbane_90)

    <span id="d-berbane_130"></span>**`berbane_130`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if hand over 1× [Stoutford chief's helmet](../items/stoutford_helmet.md))* → [berbane_132](#d-berbane_132)
    - branch 2 → [berbane_134](#d-berbane_134)

    <span id="d-berbane_132"></span>**`berbane_132`** Lord Berbane: “[Loud voice] Yes, he has carried my magical helmet for me. I will take it back now.” — **effects:** sets stage 92 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-92), sets stage 149 of [General story flags (hidden flag)](../quests/nondisplay.md#stage-149)

    - “I give up.” → [berbane_140](#d-berbane_140)

    <span id="d-berbane_134"></span>**`berbane_134`** Lord Berbane: “[Loud voice] Yes, he has learned much from me. But no need to thank me now.”

    - “I give up.” → [berbane_140](#d-berbane_140)

    <span id="d-berbane_140"></span>**`berbane_140`** *(silent check: the first matching branch below is taken)* — **effects:** gives 1× [Mead](../items/mead.md), sets stage 45 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-45)

    - branch 1 *(if reached stage 70 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-70))* → [berbane_144](#d-berbane_144)
    - branch 2 → [berbane_142](#d-berbane_142)

    <span id="d-berbane_144"></span>**`berbane_144`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 199 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-199)

    - branch 1 → [berbane_146](#d-berbane_146)

    <span id="d-berbane_142"></span>**`berbane_142`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 99 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-99)

    - branch 1 → [berbane_146](#d-berbane_146)

    <span id="d-berbane_146"></span>**`berbane_146`** Lord Berbane: “[Low voice] Well-behaved. [Loud voice] And now: Mead for everyone! Let's be merry! Forget all sorrows!”




## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 21 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `berbane` |
    | Type (wiki) | NPC |
    | Spawn group | `berbane` |
    | Loot table | – |
    | Conversation | `berbane` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik2:42` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "berbane",
     "name": "Lord Berbane",
     "iconID": "monsters_tometik2:42",
     "spawnGroup": "berbane",
     "phraseID": "berbane"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=berbane.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=berbane.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=berbane.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=berbane.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
