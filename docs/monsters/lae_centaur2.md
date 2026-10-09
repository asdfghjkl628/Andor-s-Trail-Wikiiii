---
description: "Callista, the centaur is a non-player character (NPC) in Andor's Trail, found in Island 2. Starts Not Pony Island."
---

# ![](../assets/icons/monsters/monsters_ld1_42.png){ .sprite } Callista, the centaur

**Where to find Callista, the centaur:** [Island 2](../maps/island2.md#pin-npc-lae_centaur2)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_42.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Starts [Not Pony Island](../quests/lae_centaurs.md) |
| **Found in** | Island 2 |
| **Entry ID** | `lae_centaur2` |
| **Introduced** | [v0.8.11](../versions/0.8.11.md) |

</div>

## Quests

- [Not Pony Island](../quests/lae_centaurs.md): stage 10
- [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md): stage 212

## Dialogue simulator

Set your quest stages and items, then talk to Callista, the centaur. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_centaur2.json" data-npc="Callista, the centaur" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (13 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-lae_centaur2"></span>**`lae_centaur2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 30 of [Not Pony Island](../quests/lae_centaurs.md#stage-30))* → [lae_centaur](#d-lae_centaur)
    - branch 2 *(if reached stage 212 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-212))* → [lae_centaur2_20](#d-lae_centaur2_20)
    - branch 3 → [lae_centaur2_1](#d-lae_centaur2_1)

    <span id="d-lae_centaur"></span>**`lae_centaur`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 300 of [Not Pony Island](../quests/lae_centaurs.md#stage-300))* → [lae_centaur8](#d-lae_centaur8)
    - branch 2 *(if reached stage 30 of [Not Pony Island](../quests/lae_centaurs.md#stage-30))* → [lae_centaur_20](#d-lae_centaur_20)
    - branch 3 → [lae_centaur_10](#d-lae_centaur_10)

    <span id="d-lae_centaur2_20"></span>**`lae_centaur2_20`** Callista, the centaur: “You are not wanted here.”


    <span id="d-lae_centaur2_1"></span>**`lae_centaur2_1`** Callista, the centaur: “What brings a human like you to our island?”

    - “Just passing through. No need to get defensive.” → [lae_centaur2_2](#d-lae_centaur2_2)

    <span id="d-lae_centaur8"></span>**`lae_centaur8`** Callista, the centaur: “The stars are bright tonight.”


    <span id="d-lae_centaur_20"></span>**`lae_centaur_20`** Callista, the centaur: “We have an eye on you.”


    <span id="d-lae_centaur_10"></span>**`lae_centaur_10`** Callista, the centaur: “You are not wanted here.”


    <span id="d-lae_centaur2_2"></span>**`lae_centaur2_2`** Callista, the centaur: “Defensive? Ha! We have every right to be wary of your kind. Humans have brought nothing but trouble to our land.”

    - “I'm not here to cause trouble.” → [lae_centaur2_3](#d-lae_centaur2_3)
    - “I'm just looking for...” → [lae_centaur2_3](#d-lae_centaur2_3)

    <span id="d-lae_centaur2_3"></span>**`lae_centaur2_3`** Callista, the centaur: “That's what they all say. But mark my words, human, if you step out of line, you'll regret it.”

    - “I assure you, I have no intentions of causing any harm.” → [lae_centaur2_4](#d-lae_centaur2_4)

    <span id="d-lae_centaur2_4"></span>**`lae_centaur2_4`** Callista, the centaur: “We'll see about that. Just remember, you're not welcome here.”

    - Next → [lae_centaur2_5](#d-lae_centaur2_5)

    <span id="d-lae_centaur2_5"></span>**`lae_centaur2_5`** Callista, the centaur: “We will have to decide what happens to you. You must therefore go to our leader now.”

    - “Fine, I'll go see him.” → [lae_centaur2_8](#d-lae_centaur2_8)
    - “It's okay, calm down. Where is this leader?” → [lae_centaur2_8](#d-lae_centaur2_8)

    <span id="d-lae_centaur2_8"></span>**`lae_centaur2_8`** Callista, the centaur: “Thalos, our wise guide, is currently in the northeast of the island.” — **effects:** sets stage 10 of [Not Pony Island](../quests/lae_centaurs.md#stage-10), sets stage 212 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-212)

    - “Fine, I'll go see him.” → [lae_centaur2_10](#d-lae_centaur2_10)
    - “Hopefully this Thalos will be a little more accommodating.” → [lae_centaur2_10](#d-lae_centaur2_10)

    <span id="d-lae_centaur2_10"></span>**`lae_centaur2_10`** Callista, the centaur: “Don't think about trying anything funny. We'll be watching you.”




## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 13 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `lae_centaur2` |
    | Spawn group | `lae_centaur2` |
    | Loot table | – |
    | Conversation | `lae_centaur2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:42` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_centaur2",
     "name": "Callista, the centaur",
     "iconID": "monsters_ld1:42",
     "monsterClass": "humanoid",
     "phraseID": "lae_centaur2"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_centaur2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_centaur2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_centaur2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_centaur2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
