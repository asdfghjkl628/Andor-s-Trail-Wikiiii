---
description: "Mourning woman is a non-player character (NPC) in Andor's Trail, found in Brimhaven, Fallhaven, Loneford, Mt. Galmore, Loneford."
---

# ![](../assets/icons/monsters/monsters_men_6.png){ .sprite } Mourning woman

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_6.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Brimhaven, Fallhaven, Loneford, Mt. Galmore, Loneford |
| **Entries in game data** | 2 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Mourning woman. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`chapelgoer`](#v-chapelgoer) | NPC | Brimhaven: [brimhaven_church](../maps/brimhaven_church.md#pin-npc-chapelgoer), Fallhaven: [fallhaven_church](../maps/fallhaven_church.md#pin-npc-chapelgoer) (+3 more) | – |
| [`dds_mourning_woman`](#v-dds_mourning_woman) | NPC | Loneford: [loneford4](../maps/loneford4.md#pin-npc-dds_mourning_woman), Mt. Galmore: [galmore_45](../maps/galmore_45.md#pin-npc-dds_mourning_woman) | – |

## Brimhaven, Brimhaven church and 4 more (chapelgoer) { #v-chapelgoer }

**Entry ID:** `chapelgoer` · **Type:** NPC

**Location:** Brimhaven: [brimhaven_church](../maps/brimhaven_church.md#pin-npc-chapelgoer), Fallhaven: [fallhaven_church](../maps/fallhaven_church.md#pin-npc-chapelgoer), Loneford: [loneford4](../maps/loneford4.md#pin-npc-chapelgoer), Remgard: [remgard_church](../maps/remgard_church.md#pin-npc-chapelgoer), Vilegard: [vilegard_chapel](../maps/vilegard_chapel.md#pin-npc-chapelgoer)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [brimhaven_church](../maps/brimhaven_church.md) | Brimhaven | 3 | – |
| [fallhaven_church](../maps/fallhaven_church.md) | Fallhaven | 3 | – |
| [loneford4](../maps/loneford4.md) | Loneford | 1 | – |
| [remgard_church](../maps/remgard_church.md) | Remgard | 2 | – |
| [vilegard_chapel](../maps/vilegard_chapel.md) | Vilegard | 2 | – |

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Mourning woman. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/chapelgoer.json" data-npc="Mourning woman" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-chapelgoer-chapelgoer"></span>**`chapelgoer`** Mourning woman: “Shadow, embrace me.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (chapelgoer)"

    | | |
    |---|---|
    | Entry ID | `chapelgoer` |
    | Spawn group | `chapelgoer` |
    | Loot table | – |
    | Conversation | `chapelgoer` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:6` |
    | Defined in | `res/raw/monsterlist_fallhaven_npcs.json` |

    Raw data:

    ```json
    {
     "id": "chapelgoer",
     "name": "Mourning woman",
     "iconID": "monsters_men:6",
     "monsterClass": "humanoid",
     "spawnGroup": "chapelgoer",
     "phraseID": "chapelgoer"
    }
    ```


## Loneford, Loneford4 and 1 more (dds_mourning_woman) { #v-dds_mourning_woman }

**Entry ID:** `dds_mourning_woman` · **Type:** NPC

**Location:** Loneford: [loneford4](../maps/loneford4.md#pin-npc-dds_mourning_woman), Mt. Galmore: [galmore_45](../maps/galmore_45.md#pin-npc-dds_mourning_woman)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [galmore_45](../maps/galmore_45.md) | Mt. Galmore | 1 | Appears later, during a quest |
| [loneford4](../maps/loneford4.md) | Loneford | 1 | Appears later, during a quest |

### Quests

- [Darkness in the Daylight](../quests/darkness_in_daylight.md): stages 198, 200, 210, 220, 232, 240
- [Shadows](../quests/shadows.md): stages 178, 180, 190, 200, 212, 220

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Mourning woman. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/dds_mourning_woman.json" data-npc="Mourning woman" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (38 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-dds_mourning_woman-dds_mourning_woman"></span>**`dds_mourning_woman`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 220 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-220))* → [dds_mourning_woman_2](#d-dds_mourning_woman-dds_mourning_woman_2)
    - branch 2 *(if reached stage 200 of [Shadows](../quests/shadows.md#stage-200))* → [dds_mourning_woman_4](#d-dds_mourning_woman-dds_mourning_woman_4)
    - branch 3 *(if NOT killed 1× [Kazaul statue](../monsters/dds_kazaul_statue.md))* → [dds_mourning_woman_10](#d-dds_mourning_woman-dds_mourning_woman_10)
    - branch 4 → [dds_mourning_woman_20](#d-dds_mourning_woman-dds_mourning_woman_20)

    <span id="d-dds_mourning_woman-dds_mourning_woman_2"></span>**`dds_mourning_woman_2`** Mourning woman: “Go away. I will never be happy in my life.” — **effects:** sets stage 232 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-232)


    <span id="d-dds_mourning_woman-dds_mourning_woman_4"></span>**`dds_mourning_woman_4`** Mourning woman: “Go away. I will never be happy in my life.” — **effects:** sets stage 212 of [Shadows](../quests/shadows.md#stage-212)


    <span id="d-dds_mourning_woman-dds_mourning_woman_10"></span>**`dds_mourning_woman_10`** Mourning woman: “[mumbling chants]”


    <span id="d-dds_mourning_woman-dds_mourning_woman_20"></span>**`dds_mourning_woman_20`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 190 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-190))* → [dds_mourning_woman_22](#d-dds_mourning_woman-dds_mourning_woman_22)
    - branch 2 *(if reached stage 165 of [Shadows](../quests/shadows.md#stage-165))* → [dds_mourning_woman_222](#d-dds_mourning_woman-dds_mourning_woman_222)

    <span id="d-dds_mourning_woman-dds_mourning_woman_22"></span>**`dds_mourning_woman_22`** Mourning woman: “Nooooo!” — **effects:** sets stage 198 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-198)

    - Next → [dds_mourning_woman_24](#d-dds_mourning_woman-dds_mourning_woman_24)

    <span id="d-dds_mourning_woman-dds_mourning_woman_222"></span>**`dds_mourning_woman_222`** Mourning woman: “Nooooo!” — **effects:** sets stage 178 of [Shadows](../quests/shadows.md#stage-178)

    - Next → [dds_mourning_woman_224](#d-dds_mourning_woman-dds_mourning_woman_224)

    <span id="d-dds_mourning_woman-dds_mourning_woman_24"></span>**`dds_mourning_woman_24`** Mourning woman: “Now the spell is broken. Everything is in vain!”

    - Next → [dds_mourning_woman_30](#d-dds_mourning_woman-dds_mourning_woman_30)

    <span id="d-dds_mourning_woman-dds_mourning_woman_224"></span>**`dds_mourning_woman_224`** Mourning woman: “Now the spell is broken. Everything is in vain!”

    - Next → [dds_mourning_woman_230](#d-dds_mourning_woman-dds_mourning_woman_230)

    <span id="d-dds_mourning_woman-dds_mourning_woman_30"></span>**`dds_mourning_woman_30`** Mourning woman: “Why did you do that? Who gave you the right?”

    - “Do you know what you were doing?” → [dds_mourning_woman_40](#d-dds_mourning_woman-dds_mourning_woman_40)

    <span id="d-dds_mourning_woman-dds_mourning_woman_230"></span>**`dds_mourning_woman_230`** Mourning woman: “Why did you do that? Who gave you the right?”

    - “Do you know what you were doing?” → [dds_mourning_woman_240](#d-dds_mourning_woman-dds_mourning_woman_240)

    <span id="d-dds_mourning_woman-dds_mourning_woman_40"></span>**`dds_mourning_woman_40`** Mourning woman: “I was getting my husband back from the afterlife!” — **effects:** sets stage 200 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-200), spawns monsters on galmore_45

    - Next → [dds_mourning_woman_50](#d-dds_mourning_woman-dds_mourning_woman_50)

    <span id="d-dds_mourning_woman-dds_mourning_woman_240"></span>**`dds_mourning_woman_240`** Mourning woman: “I was getting my husband back from the afterlife!” — **effects:** sets stage 180 of [Shadows](../quests/shadows.md#stage-180), spawns monsters on galmore_45

    - Next → [dds_mourning_woman_250](#d-dds_mourning_woman-dds_mourning_woman_250)

    <span id="d-dds_mourning_woman-dds_mourning_woman_50"></span>**`dds_mourning_woman_50`** [Miri](../monsters/dds_miri.md): “Is that what you think?”

    - “Miri? When did you get here?” → [dds_mourning_woman_60](#d-dds_mourning_woman-dds_mourning_woman_60)

    <span id="d-dds_mourning_woman-dds_mourning_woman_250"></span>**`dds_mourning_woman_250`** [Borvis](../monsters/dds_borvis.md): “Is that what you think?”

    - “Borvis? I didn't expect you already.” → [dds_mourning_woman_260](#d-dds_mourning_woman-dds_mourning_woman_260)

    <span id="d-dds_mourning_woman-dds_mourning_woman_60"></span>**`dds_mourning_woman_60`** Mourning woman: “I came with all haste. Too bad the poison is slowing me down.”

    - Next → [dds_mourning_woman_62](#d-dds_mourning_woman-dds_mourning_woman_62)

    <span id="d-dds_mourning_woman-dds_mourning_woman_260"></span>**`dds_mourning_woman_260`** Mourning woman: “I came with all haste. You were faster.”

    - Next → [dds_mourning_woman_262](#d-dds_mourning_woman-dds_mourning_woman_262)

    <span id="d-dds_mourning_woman-dds_mourning_woman_62"></span>**`dds_mourning_woman_62`** Mourning woman: “[To the mourning woman] The ritual was not to bring back your husband - it is to bring Kazaul's powerful monsters into Dhayavar.”

    - Next → [dds_mourning_woman_70](#d-dds_mourning_woman-dds_mourning_woman_70)

    <span id="d-dds_mourning_woman-dds_mourning_woman_262"></span>**`dds_mourning_woman_262`** Mourning woman: “[To the mourning woman] The ritual was not to bring back your husband - it is to bring Kazaul's powerful monsters into Dhayavar.”

    - Next → [dds_mourning_woman_270](#d-dds_mourning_woman-dds_mourning_woman_270)

    <span id="d-dds_mourning_woman-dds_mourning_woman_70"></span>**`dds_mourning_woman_70`** [Mourning woman](../monsters/chapelgoer.md#v-dds_mourning_woman): “You lie! You don't want my happiness.”

    - Next → [dds_mourning_woman_72](#d-dds_mourning_woman-dds_mourning_woman_72)

    <span id="d-dds_mourning_woman-dds_mourning_woman_270"></span>**`dds_mourning_woman_270`** [Mourning woman](../monsters/chapelgoer.md#v-dds_mourning_woman): “You lie! You don't want my happiness.”

    - Next → [dds_mourning_woman_272](#d-dds_mourning_woman-dds_mourning_woman_272)

    <span id="d-dds_mourning_woman-dds_mourning_woman_72"></span>**`dds_mourning_woman_72`** [Miri](../monsters/dds_miri.md): “Do you think monsters would have assisted you? And a barrier would have sprung up? Just for one person?”

    - Next → [dds_mourning_woman_80](#d-dds_mourning_woman-dds_mourning_woman_80)

    <span id="d-dds_mourning_woman-dds_mourning_woman_272"></span>**`dds_mourning_woman_272`** [Borvis](../monsters/dds_borvis.md): “Do you think monsters would have assisted you? And a barrier would have sprung up? Just for one person?”

    - Next → [dds_mourning_woman_280](#d-dds_mourning_woman-dds_mourning_woman_280)

    <span id="d-dds_mourning_woman-dds_mourning_woman_80"></span>**`dds_mourning_woman_80`** [Mourning woman](../monsters/chapelgoer.md#v-dds_mourning_woman): “I don't believe you.”

    - Next → [dds_mourning_woman_82](#d-dds_mourning_woman-dds_mourning_woman_82)

    <span id="d-dds_mourning_woman-dds_mourning_woman_280"></span>**`dds_mourning_woman_280`** [Mourning woman](../monsters/chapelgoer.md#v-dds_mourning_woman): “I don't believe you.”

    - Next → [dds_mourning_woman_282](#d-dds_mourning_woman-dds_mourning_woman_282)

    <span id="d-dds_mourning_woman-dds_mourning_woman_82"></span>**`dds_mourning_woman_82`** [Miri](../monsters/dds_miri.md): “Then why did the ritual not include something that links to your husband? Something precious to him?” — **effects:** sets stage 210 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-210)

    - Next → [dds_mourning_woman_90](#d-dds_mourning_woman-dds_mourning_woman_90)

    <span id="d-dds_mourning_woman-dds_mourning_woman_282"></span>**`dds_mourning_woman_282`** [Borvis](../monsters/dds_borvis.md): “Then why did the ritual not include something that links to your husband? Something precious to him?” — **effects:** sets stage 190 of [Shadows](../quests/shadows.md#stage-190)

    - Next → [dds_mourning_woman_290](#d-dds_mourning_woman-dds_mourning_woman_290)

    <span id="d-dds_mourning_woman-dds_mourning_woman_90"></span>**`dds_mourning_woman_90`** [Mourning woman](../monsters/chapelgoer.md#v-dds_mourning_woman): “Oh no! What do I do now? He's gone.”

    - Next → [dds_mourning_woman_92](#d-dds_mourning_woman-dds_mourning_woman_92)

    <span id="d-dds_mourning_woman-dds_mourning_woman_290"></span>**`dds_mourning_woman_290`** [Mourning woman](../monsters/chapelgoer.md#v-dds_mourning_woman): “Oh no! What do I do now? He's gone.”

    - Next → [dds_mourning_woman_292](#d-dds_mourning_woman-dds_mourning_woman_292)

    <span id="d-dds_mourning_woman-dds_mourning_woman_92"></span>**`dds_mourning_woman_92`** [Miri](../monsters/dds_miri.md): “Pray where have you been praying. And tell me who put you up to this?”

    - “Yes, who put you up to this?” → [dds_mourning_woman_100](#d-dds_mourning_woman-dds_mourning_woman_100)

    <span id="d-dds_mourning_woman-dds_mourning_woman_292"></span>**`dds_mourning_woman_292`** [Borvis](../monsters/dds_borvis.md): “Pray where have you been praying. And tell me who put you up to this?”

    - “Yes, who put you up to this?” → [dds_mourning_woman_300](#d-dds_mourning_woman-dds_mourning_woman_300)

    <span id="d-dds_mourning_woman-dds_mourning_woman_100"></span>**`dds_mourning_woman_100`** [Mourning woman](../monsters/chapelgoer.md#v-dds_mourning_woman): “Why? That famous miracle priest who walks on lava, west of here. Do you need me anymore? Then I'm going home to mourn again.” — **effects:** sets stage 220 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-220), removes monsters from galmore_45, spawns monsters on loneford4

    - Next → [dds_mourning_woman_110](#d-dds_mourning_woman-dds_mourning_woman_110)

    <span id="d-dds_mourning_woman-dds_mourning_woman_300"></span>**`dds_mourning_woman_300`** [Mourning woman](../monsters/chapelgoer.md#v-dds_mourning_woman): “Why? That famous miracle priest who walks on lava, west of here. Do you need me anymore? Then I'm going home to mourn again.” — **effects:** sets stage 200 of [Shadows](../quests/shadows.md#stage-200), removes monsters from galmore_45, spawns monsters on loneford4

    - Next → [dds_mourning_woman_310](#d-dds_mourning_woman-dds_mourning_woman_310)

    <span id="d-dds_mourning_woman-dds_mourning_woman_110"></span>**`dds_mourning_woman_110`** [Miri](../monsters/dds_miri.md): “Yes, you go back to your village. And we will have a chat with this famous miracle priest.”

    - “Nice job.” → [dds_miri_500](#d-dds_mourning_woman-dds_miri_500)

    <span id="d-dds_mourning_woman-dds_mourning_woman_310"></span>**`dds_mourning_woman_310`** [Borvis](../monsters/dds_borvis.md): “Yes, you go back to your village. And we will have a chat with this famous miracle priest.”

    - “Nice job.” → [dds_borvis_500](#d-dds_mourning_woman-dds_borvis_500)

    <span id="d-dds_mourning_woman-dds_miri_500"></span>**`dds_miri_500`** Mourning woman: “It's not done yet. Can you talk to this priest? And tackle him as he deserves?” — **effects:** sets stage 240 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-240), spawns monsters on galmore_41

    - “Of course! On my way!” → *conversation ends*

    <span id="d-dds_mourning_woman-dds_borvis_500"></span>**`dds_borvis_500`** Mourning woman: “It's not done yet. Can you talk to this priest? And tackle him as he deserves?” — **effects:** sets stage 220 of [Shadows](../quests/shadows.md#stage-220), spawns monsters on galmore_41

    - “Of course! On my way!” → *conversation ends*
    - “Why not you?” → [dds_borvis_502](#d-dds_mourning_woman-dds_borvis_502)

    <span id="d-dds_mourning_woman-dds_borvis_502"></span>**`dds_borvis_502`** Mourning woman: “You'll be faster. Don't worry, I'll follow you.”

    - “Of course! On my way!” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 38 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (dds_mourning_woman)"

    | | |
    |---|---|
    | Entry ID | `dds_mourning_woman` |
    | Spawn group | `dds_mourning_woman` |
    | Loot table | – |
    | Conversation | `dds_mourning_woman` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:6` |
    | Defined in | `res/raw/monsterlist_darknessanddaylight.json` |

    Raw data:

    ```json
    {
     "id": "dds_mourning_woman",
     "name": "Mourning woman",
     "iconID": "monsters_men:6",
     "monsterClass": "humanoid",
     "spawnGroup": "dds_mourning_woman",
     "phraseID": "dds_mourning_woman"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=chapelgoer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=chapelgoer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=chapelgoer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=chapelgoer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
