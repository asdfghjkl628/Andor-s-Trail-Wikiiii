---
description: "Tavern guest is a non-player character (NPC) in Andor's Trail, found in Vilegard, Remgard."
---

# ![](../assets/icons/monsters/monsters_men_0.png){ .sprite } Tavern guest

**Where to find Tavern guest:** [Vilegard, Vilegard tavern](#v-tavern_guest), [Remgard, Remgard tavern 0](#v-remgard_d1), [Remgard, Remgard tavern 0](#v-remgard_d2)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Vilegard, Remgard |
| **Introduced** | v0.7.0 or earlier |

</div>

## Vilegard, Vilegard tavern { #v-tavern_guest }

**Where:** Vilegard: [Vilegard tavern](../maps/vilegard_tavern.md#pin-npc-tavern_guest)

### Dialogue simulator

Set your quest stages and items, then talk to Tavern guest. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/vilegard_tavern_drunk_1.json" data-npc="Tavern guest" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-tavern_guest-vilegard_tavern_drunk_1"></span>**`vilegard_tavern_drunk_1`** Tavern guest: “Oh look, a lost kid. Here, have some mead kid.”

    - “No thanks.” → *conversation ends*
    - “Watch your tongue, drunkard.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Remgard, Remgard tavern 0 { #v-remgard_d1 }

**Where:** Remgard: [Remgard tavern 0](../maps/remgard_tavern0.md#pin-npc-remgard_d1)

### Dialogue simulator

Set your quest stages and items, then talk to Tavern guest. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/remgard_drunk1.json" data-npc="Tavern guest" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-remgard_d1-remgard_drunk1"></span>**`remgard_drunk1`** Tavern guest: “*burp* Ha ha! I never thought she would! Or was it the other way around? I can't remember.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Remgard, Remgard tavern 0 (2) { #v-remgard_d2 }

**Where:** Remgard: [Remgard tavern 0](../maps/remgard_tavern0.md#pin-npc-remgard_d2)

### Dialogue simulator

Set your quest stages and items, then talk to Tavern guest. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/remgard_drunk2.json" data-npc="Tavern guest" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-remgard_d2-remgard_drunk2"></span>**`remgard_drunk2`** Tavern guest: “*burp* This is the best place in all of the northern lands!”

    - Next → [remgard_drunk2_2](#d-remgard_d2-remgard_drunk2_2)

    <span id="d-remgard_d2-remgard_drunk2_2"></span>**`remgard_drunk2_2`** Tavern guest: “Oh, hello there. *burp* Kid, I tell you, don't go looking for trouble even if you think you can handle it.”

    - Next → [remgard_drunk2_3](#d-remgard_d2-remgard_drunk2_3)

    <span id="d-remgard_d2-remgard_drunk2_3"></span>**`remgard_drunk2_3`** Tavern guest: “I did once, and ended up in those horrid caverns of Mount Galmore.”

    - Next → [remgard_drunk2_4](#d-remgard_d2-remgard_drunk2_4)

    <span id="d-remgard_d2-remgard_drunk2_4"></span>**`remgard_drunk2_4`** Tavern guest: “That place twists your mind. I tell you, don't go there, even if you think you want to!”

    - “Mount Galmore, where is that?” *(if NOT reached stage 10 of [The swamp healer](../quests/swamp_healer.md#stage-10))* → [remgard_drunk2_5](#d-remgard_d2-remgard_drunk2_5)
    - “Mount Galmore twists your mind? Oh, I see. You mean Undertell?” *(if reached stage 5 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-5))* → [remgard_drunk2_5](#d-remgard_d2-remgard_drunk2_5)
    - “I'll keep that in mind.” → *conversation ends*
    - “Get out of my way!” → *conversation ends*

    <span id="d-remgard_d2-remgard_drunk2_5"></span>**`remgard_drunk2_5`** Tavern guest: “[burp] What was that? Were you saying something?”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed<br>· text: “That place twists your mind. I tell you, don't go there, even if you …” → “That place twists your mind. I tell you, don't go there, even if you …” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 2 lines changed<br>· text: “*burp* What was that? Were you saying something?” → “[burp] What was that? Were you saying something?” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**3 entries.** The game data defines 3 separate characters named Tavern guest. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location, appearance.

| Entry | Type | Section |
|---|---|---|
| `tavern_guest` | NPC | [Vilegard, Vilegard tavern](#v-tavern_guest) |
| `remgard_d1` | NPC | [Remgard, Remgard tavern 0](#v-remgard_d1) |
| `remgard_d2` | NPC | [Remgard, Remgard tavern 0](#v-remgard_d2) |

??? info "Technical information: tavern_guest"

    | | |
    |---|---|
    | Entry ID | `tavern_guest` |
    | Type (wiki) | NPC |
    | Spawn group | `vg_tavern_drunk` |
    | Loot table | – |
    | Conversation | `vilegard_tavern_drunk_1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:0` |
    | Defined in | `res/raw/monsterlist_v068_npcs.json` |

    Raw data:

    ```json
    {
     "id": "tavern_guest",
     "name": "Tavern guest",
     "iconID": "monsters_men:0",
     "monsterClass": "humanoid",
     "spawnGroup": "vg_tavern_drunk",
     "phraseID": "vilegard_tavern_drunk_1"
    }
    ```

??? info "Technical information: remgard_d1"

    | | |
    |---|---|
    | Entry ID | `remgard_d1` |
    | Type (wiki) | NPC |
    | Spawn group | `remgard_drunk` |
    | Loot table | – |
    | Conversation | `remgard_drunk1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:18` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "remgard_d1",
     "name": "Tavern guest",
     "iconID": "monsters_ld1:18",
     "monsterClass": "humanoid",
     "spawnGroup": "remgard_drunk",
     "phraseID": "remgard_drunk1"
    }
    ```

??? info "Technical information: remgard_d2"

    | | |
    |---|---|
    | Entry ID | `remgard_d2` |
    | Type (wiki) | NPC |
    | Spawn group | `remgard_drunk` |
    | Loot table | – |
    | Conversation | `remgard_drunk2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:81` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "remgard_d2",
     "name": "Tavern guest",
     "iconID": "monsters_rltiles2:81",
     "monsterClass": "humanoid",
     "spawnGroup": "remgard_drunk",
     "phraseID": "remgard_drunk2"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tavern_guest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tavern_guest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tavern_guest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tavern_guest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
