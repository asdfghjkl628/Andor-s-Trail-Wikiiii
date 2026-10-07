---
description: "Fjoerkard is a non-player character (NPC) in Andor's Trail, found in Guynmart Castle."
---

# ![](../assets/icons/monsters/monsters_ld1_122.png){ .sprite } Fjoerkard

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_122.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Guynmart Castle |
| **Entries in game data** | 2 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

!!! info "2 entries in the game data"
    The game data defines 2 separate characters named Fjoerkard. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation. Each entry has its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`guynmart_drunkard1`](#v-guynmart_drunkard1) | NPC | Guynmart Castle: [Guynmart main 2](../maps/guynmart_main_2.md#pin-npc-guynmart_drunkard1) | – |
| [`guynmart_drunkard5`](#v-guynmart_drunkard5) | NPC | Guynmart Castle: [Guynmart main 2](../maps/guynmart_main_2.md#pin-npc-guynmart_drunkard5) | – |

## Guynmart Castle, Guynmart main 2 (guynmart_drunkard1) { #v-guynmart_drunkard1 }

**Entry ID:** `guynmart_drunkard1` · **Type:** NPC

**Location:** Guynmart Castle: [Guynmart main 2](../maps/guynmart_main_2.md#pin-npc-guynmart_drunkard1)

### Quests

- [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md): stage 4

### Dialogue simulator

Set your quest stages and items, then talk to Fjoerkard. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_drunkard1_10.json" data-npc="Fjoerkard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_drunkard1-guynmart_drunkard1_10"></span>**`guynmart_drunkard1_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if carry 1× [Wine](../items/guynmart_wine.md))* → [guynmart_drunkard1_30](#d-guynmart_drunkard1-guynmart_drunkard1_30)
    - branch 2 → [guynmart_drunkard1_20](#d-guynmart_drunkard1-guynmart_drunkard1_20)

    <span id="d-guynmart_drunkard1-guynmart_drunkard1_30"></span>**`guynmart_drunkard1_30`** Fjoerkard: “Hey, why don't you take a seat and open one of those bottles of wine you have. I could tell you things you wouldn't believe!” — **effects:** sets stage 4 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-4)

    - “OK, I'll sit down.” → *conversation ends*
    - “You should drink less.” → *conversation ends*

    <span id="d-guynmart_drunkard1-guynmart_drunkard1_20"></span>**`guynmart_drunkard1_20`** Fjoerkard: “Hey, get us some bottles of wine and then take a seat. I could tell you things you wouldn't believe!” — **effects:** sets stage 4 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-4)

    - “I'll go for the wine, wait a minute.” → *conversation ends*
    - “You should drink less.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_drunkard1)"

    | | |
    |---|---|
    | Entry ID | `guynmart_drunkard1` |
    | Spawn group | `guynmart_drunkard1` |
    | Loot table | – |
    | Conversation | `guynmart_drunkard1_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:122` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_drunkard1",
     "name": "Fjoerkard",
     "iconID": "monsters_ld1:122",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_drunkard1_10"
    }
    ```


## Guynmart Castle, Guynmart main 2 (guynmart_drunkard5) { #v-guynmart_drunkard5 }

**Entry ID:** `guynmart_drunkard5` · **Type:** NPC

**Location:** Guynmart Castle: [Guynmart main 2](../maps/guynmart_main_2.md#pin-npc-guynmart_drunkard5)

### Dialogue simulator

Set your quest stages and items, then talk to Fjoerkard. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_drunkard5_10.json" data-npc="Fjoerkard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (22 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_drunkard5-guynmart_drunkard5_10"></span>**`guynmart_drunkard5_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if carry 1× [Wine](../items/guynmart_wine.md); reached stage 5 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-5))* → [guynmart_drunkard5_100](#d-guynmart_drunkard5-guynmart_drunkard5_100)
    - branch 2 *(if carry 1× [Wine](../items/guynmart_wine.md))* → [guynmart_drunkard5_20](#d-guynmart_drunkard5-guynmart_drunkard5_20)
    - branch 3 *(if reached stage 4 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-4))* → [guynmart_drunkard5_12](#d-guynmart_drunkard5-guynmart_drunkard5_12)
    - branch 4 → [guynmart_drunkard5_13](#d-guynmart_drunkard5-guynmart_drunkard5_13)

    <span id="d-guynmart_drunkard5-guynmart_drunkard5_100"></span>**`guynmart_drunkard5_100`** [Fjoerkard](../monsters/guynmart_drunkard1.md#v-guynmart_drunkard5): “Let's have a sip, then I will tell you my story.”

    - “OK.” *(if hand over 1× [Wine](../items/guynmart_wine.md))* → [guynmart_drunkard5_102](#d-guynmart_drunkard5-guynmart_drunkard5_102)
    - “I think I had better keep the bottles in my bag.” → [guynmart_drunkard5_14](#d-guynmart_drunkard5-guynmart_drunkard5_14)

    <span id="d-guynmart_drunkard5-guynmart_drunkard5_20"></span>**`guynmart_drunkard5_20`** [Fjoerkard](../monsters/guynmart_drunkard1.md#v-guynmart_drunkard5): “You standing over me makes me feel uncomfortable. Take a seat next to me first.”


    <span id="d-guynmart_drunkard5-guynmart_drunkard5_12"></span>**`guynmart_drunkard5_12`** [Fjoerkard](../monsters/guynmart_drunkard1.md#v-guynmart_drunkard5): “I think you have forgotten something...?”

    - “Oh, yes, of course, I will get some bottles of wine.” → *conversation ends*

    <span id="d-guynmart_drunkard5-guynmart_drunkard5_13"></span>**`guynmart_drunkard5_13`** [Fjoerkard](../monsters/guynmart_drunkard1.md#v-guynmart_drunkard5): “Hey, get us some bottles of wine! I could tell you things you wouldn't believe!”

    - “Good idea! I'll go for the wine, wait a minute.” → *conversation ends*
    - “You should drink less.” → *conversation ends*

    <span id="d-guynmart_drunkard5-guynmart_drunkard5_102"></span>**`guynmart_drunkard5_102`** Fjoerkard: “[Fjoerkard empties a bottle] Oh yes, I remember it well ... It was a dark and stormy night up in the mountains.”

    - Next → [guynmart_drunkard5_110](#d-guynmart_drunkard5-guynmart_drunkard5_110)

    <span id="d-guynmart_drunkard5-guynmart_drunkard5_14"></span>**`guynmart_drunkard5_14`** Fjoerkard: “Oh. The wine bottles are all empty. Could you get some more?”

    - “Yes, of course. I will get some more bottles.” → *conversation ends*

    <span id="d-guynmart_drunkard5-guynmart_drunkard5_110"></span>**`guynmart_drunkard5_110`** Fjoerkard: “My men and I had been on the road for hours, without a break and without the slightest sign of getting closer to our goal.”

    - Next → [guynmart_drunkard5_120](#d-guynmart_drunkard5-guynmart_drunkard5_120)

    <span id="d-guynmart_drunkard5-guynmart_drunkard5_120"></span>**`guynmart_drunkard5_120`** Fjoerkard: “We silently trudged one by one up the tortuous path that led up the steep slope, always wary of the treacherous shadows of the bushes on either side, and always listening for signs of danger.”

    - Next → [guynmart_drunkard5_130](#d-guynmart_drunkard5-guynmart_drunkard5_130)

    <span id="d-guynmart_drunkard5-guynmart_drunkard5_130"></span>**`guynmart_drunkard5_130`** Fjoerkard: “You don't mind if I open another bottle?”

    - “Help yourself.” *(if carry 1× [Wine](../items/guynmart_wine.md))* → [guynmart_drunkard5_132](#d-guynmart_drunkard5-guynmart_drunkard5_132)
    - “Again? Another bottle?” → [guynmart_drunkard5_14](#d-guynmart_drunkard5-guynmart_drunkard5_14)

    <span id="d-guynmart_drunkard5-guynmart_drunkard5_132"></span>**`guynmart_drunkard5_132`** Fjoerkard: “[Fjoerkard empties the bottle] Gornauds were said to be roaming in those mountains. We had not seen any, by the shadow, but we had already crossed their traces several times. And there were rumors about even more dangerous creatures - I…”

    - Next *(if hand over 1× [Wine](../items/guynmart_wine.md))* → [guynmart_drunkard5_140](#d-guynmart_drunkard5-guynmart_drunkard5_140)

    <span id="d-guynmart_drunkard5-guynmart_drunkard5_140"></span>**`guynmart_drunkard5_140`** Fjoerkard: “A lonely hut came into sight. A friendly light in the midst of the wilderness. There we would ask to camp for the night. New strength flowed through us, when suddenly all hell broke loose.”

    - Next → [guynmart_drunkard5_150](#d-guynmart_drunkard5-guynmart_drunkard5_150)

    <span id="d-guynmart_drunkard5-guynmart_drunkard5_150"></span>**`guynmart_drunkard5_150`** Fjoerkard: “Gornauds jumped out from behind the rocks, so close that we could clearly see their facial features. For a few terrible seconds I thought that those would be our last seconds.”

    - Next → [guynmart_drunkard5_160](#d-guynmart_drunkard5-guynmart_drunkard5_160)

    <span id="d-guynmart_drunkard5-guynmart_drunkard5_160"></span>**`guynmart_drunkard5_160`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if hand over 1× [Wine](../items/guynmart_wine.md))* → [guynmart_drunkard5_162](#d-guynmart_drunkard5-guynmart_drunkard5_162)
    - branch 2 → [guynmart_drunkard5_14](#d-guynmart_drunkard5-guynmart_drunkard5_14)

    <span id="d-guynmart_drunkard5-guynmart_drunkard5_162"></span>**`guynmart_drunkard5_162`** Fjoerkard: “[Another bottle] But then we realized that the monsters were after an easier prey. A small figure was in front of us on the path. A child? Alone up there?”

    - Next → [guynmart_drunkard5_170](#d-guynmart_drunkard5-guynmart_drunkard5_170)

    <span id="d-guynmart_drunkard5-guynmart_drunkard5_170"></span>**`guynmart_drunkard5_170`** Fjoerkard: “Shaken, I closed my eyes, despite the great danger. I did not want to look at the slaughter. The dreadful noise lasted only a few seconds.”

    - Next → [guynmart_drunkard5_180](#d-guynmart_drunkard5-guynmart_drunkard5_180)

    <span id="d-guynmart_drunkard5-guynmart_drunkard5_180"></span>**`guynmart_drunkard5_180`** Fjoerkard: “The ground was soaked with red blood. But - it came from the gornauds! The child just wiped the weapon clean of blood, gave us a quick glance, and disappeared up the path.”

    - Next → [guynmart_drunkard5_190](#d-guynmart_drunkard5-guynmart_drunkard5_190)

    <span id="d-guynmart_drunkard5-guynmart_drunkard5_190"></span>**`guynmart_drunkard5_190`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if hand over 1× [Wine](../items/guynmart_wine.md))* → [guynmart_drunkard5_192](#d-guynmart_drunkard5-guynmart_drunkard5_192)
    - branch 2 → [guynmart_drunkard5_14](#d-guynmart_drunkard5-guynmart_drunkard5_14)

    <span id="d-guynmart_drunkard5-guynmart_drunkard5_192"></span>**`guynmart_drunkard5_192`** Fjoerkard: “[Another bottle] We had had enough of that cursed march. Panicked, we ran back down the path. Tired as we were, we ran without stopping even once, to the inn in the valley, from which we had departed in the morning.”

    - Next → [guynmart_drunkard5_200](#d-guynmart_drunkard5-guynmart_drunkard5_200)

    <span id="d-guynmart_drunkard5-guynmart_drunkard5_200"></span>**`guynmart_drunkard5_200`** Fjoerkard: “Never will I forget that useless journey. Often I see it again in a nightmare and then I seek the memory of a friendly inn. Where once there was a little girl, probably the daughter of the landlord.”

    - Next → [guynmart_drunkard5_210](#d-guynmart_drunkard5-guynmart_drunkard5_210)

    <span id="d-guynmart_drunkard5-guynmart_drunkard5_210"></span>**`guynmart_drunkard5_210`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if hand over 1× [Wine](../items/guynmart_wine.md))* → [guynmart_drunkard5_212](#d-guynmart_drunkard5-guynmart_drunkard5_212)
    - branch 2 → [guynmart_drunkard5_14](#d-guynmart_drunkard5-guynmart_drunkard5_14)

    <span id="d-guynmart_drunkard5-guynmart_drunkard5_212"></span>**`guynmart_drunkard5_212`** Fjoerkard: “[Yet another bottle] She got some wine for an old bearded guest and asked for a tale, and he began: Oh yes, I remember it well ... It was a dark and stormy night up in the mountains.”

    - Next → [guynmart_drunkard5_110](#d-guynmart_drunkard5-guynmart_drunkard5_110)



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 22 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_drunkard5)"

    | | |
    |---|---|
    | Entry ID | `guynmart_drunkard5` |
    | Spawn group | `guynmart_drunkard5` |
    | Loot table | – |
    | Conversation | `guynmart_drunkard5_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:122` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_drunkard5",
     "name": "Fjoerkard",
     "iconID": "monsters_ld1:122",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_drunkard5_10"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_drunkard1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_drunkard1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_drunkard1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_drunkard1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
