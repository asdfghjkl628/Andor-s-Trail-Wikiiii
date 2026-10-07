---
description: "Charybdis is a non-player character (NPC) in Andor's Trail, found in Lake Laeroth, mountainlake_sub."
---

# ![](../assets/icons/monsters/monsters_nut_81.png){ .sprite } Charybdis

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_nut_81.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Lake Laeroth, mountainlake_sub |
| **Entries in game data** | 2 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Charybdis. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`ll2_whirl`](#v-ll2_whirl) | NPC | Lake Laeroth: [mountainlake31](../maps/mountainlake31.md#pin-npc-ll2_whirl), Lake Laeroth: [mountainlake36](../maps/mountainlake36.md#pin-npc-ll2_whirl) (+4 more) | – |
| [`ll2_whirl_return`](#v-ll2_whirl_return) | NPC | [mountainlake_sub](../maps/mountainlake_sub.md#pin-npc-ll2_whirl_return) | – |

## Lake Laeroth, Mountainlake31 and 5 more (ll2_whirl) { #v-ll2_whirl }

**Entry ID:** `ll2_whirl` · **Type:** NPC

**Location:** Lake Laeroth: [mountainlake31](../maps/mountainlake31.md#pin-npc-ll2_whirl), Lake Laeroth: [mountainlake36](../maps/mountainlake36.md#pin-npc-ll2_whirl), Lake Laeroth: [mountainlake37](../maps/mountainlake37.md#pin-npc-ll2_whirl), [mountainlake33](../maps/mountainlake33.md#pin-npc-ll2_whirl), [mountainlake34](../maps/mountainlake34.md#pin-npc-ll2_whirl), [mountainlake35](../maps/mountainlake35.md#pin-npc-ll2_whirl)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [mountainlake31](../maps/mountainlake31.md) | Lake Laeroth | 1 | Appears later, during a quest |
| [mountainlake33](../maps/mountainlake33.md) | – | 1 | Appears later, during a quest |
| [mountainlake34](../maps/mountainlake34.md) | – | 1 | Appears later, during a quest |
| [mountainlake35](../maps/mountainlake35.md) | – | 1 | Appears later, during a quest |
| [mountainlake36](../maps/mountainlake36.md) | Lake Laeroth | 1 | Appears later, during a quest |
| [mountainlake37](../maps/mountainlake37.md) | Lake Laeroth | 1 | Appears later, during a quest |

### Quests

- [A map of the Great Lake Laeroth](../quests/lake_map.md): stage 70

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Charybdis. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/ll2_whirl.json" data-npc="Charybdis" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ll2_whirl-ll2_whirl"></span>**`ll2_whirl`** Charybdis: “It swirls around you, faster and faster, until everything is black. You wake up in a daze. The ship survived the maelstrom!” — **effects:** clears stage 20 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-20), moves you to [mountainlake_sub](../maps/mountainlake_sub.md), sets stage 70 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-70)




### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ll2_whirl)"

    | | |
    |---|---|
    | Entry ID | `ll2_whirl` |
    | Spawn group | `ll2_whirl` |
    | Loot table | – |
    | Conversation | `ll2_whirl` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_nut:81` |
    | Defined in | `res/raw/monsterlist_lake_laeroth_2.json` |

    Raw data:

    ```json
    {
     "id": "ll2_whirl",
     "name": "Charybdis",
     "iconID": "monsters_nut:81",
     "monsterClass": "construct",
     "spawnGroup": "ll2_whirl",
     "phraseID": "ll2_whirl"
    }
    ```


## Mountainlake sub (ll2_whirl_return) { #v-ll2_whirl_return }

**Entry ID:** `ll2_whirl_return` · **Type:** NPC

**Location:** [mountainlake_sub](../maps/mountainlake_sub.md#pin-npc-ll2_whirl_return)

### Quests

- [A map of the Great Lake Laeroth](../quests/lake_map.md): stage 78

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Charybdis. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/ll2_whirl_return.json" data-npc="Charybdis" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (7 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ll2_whirl_return-ll2_whirl_return"></span>**`ll2_whirl_return`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 37 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-37))* → [ll2_whirl_return_to_37](#d-ll2_whirl_return-ll2_whirl_return_to_37)
    - branch 2 *(if reached stage 36 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-36))* → [ll2_whirl_return_to_36](#d-ll2_whirl_return-ll2_whirl_return_to_36)
    - branch 3 *(if reached stage 35 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-35))* → [ll2_whirl_return_to_35](#d-ll2_whirl_return-ll2_whirl_return_to_35)
    - branch 4 *(if reached stage 34 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-34))* → [ll2_whirl_return_to_34](#d-ll2_whirl_return-ll2_whirl_return_to_34)
    - branch 5 *(if reached stage 33 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-33))* → [ll2_whirl_return_to_33](#d-ll2_whirl_return-ll2_whirl_return_to_33)
    - branch 6 → [ll2_whirl_return_to_31](#d-ll2_whirl_return-ll2_whirl_return_to_31)

    <span id="d-ll2_whirl_return-ll2_whirl_return_to_37"></span>**`ll2_whirl_return_to_37`** Charybdis: “The ship has made it back up again!” — **effects:** moves you to [mountainlake37](../maps/mountainlake37.md), sets stage 78 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-78)


    <span id="d-ll2_whirl_return-ll2_whirl_return_to_36"></span>**`ll2_whirl_return_to_36`** Charybdis: “The ship has made it back up again!” — **effects:** moves you to [mountainlake36](../maps/mountainlake36.md), sets stage 78 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-78)


    <span id="d-ll2_whirl_return-ll2_whirl_return_to_35"></span>**`ll2_whirl_return_to_35`** Charybdis: “The ship has made it back up again!” — **effects:** moves you to [mountainlake35](../maps/mountainlake35.md), sets stage 78 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-78)


    <span id="d-ll2_whirl_return-ll2_whirl_return_to_34"></span>**`ll2_whirl_return_to_34`** Charybdis: “The ship has made it back up again!” — **effects:** moves you to [mountainlake34](../maps/mountainlake34.md), sets stage 78 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-78)


    <span id="d-ll2_whirl_return-ll2_whirl_return_to_33"></span>**`ll2_whirl_return_to_33`** Charybdis: “The ship has made it back up again!” — **effects:** moves you to [mountainlake33](../maps/mountainlake33.md), sets stage 78 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-78)


    <span id="d-ll2_whirl_return-ll2_whirl_return_to_31"></span>**`ll2_whirl_return_to_31`** Charybdis: “The ship has made it back up again!” — **effects:** moves you to [mountainlake31](../maps/mountainlake31.md), sets stage 78 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-78)




### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 7 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ll2_whirl_return)"

    | | |
    |---|---|
    | Entry ID | `ll2_whirl_return` |
    | Spawn group | `ll2_whirl_return` |
    | Loot table | – |
    | Conversation | `ll2_whirl_return` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_nut:81` |
    | Defined in | `res/raw/monsterlist_lake_laeroth_2.json` |

    Raw data:

    ```json
    {
     "id": "ll2_whirl_return",
     "name": "Charybdis",
     "iconID": "monsters_nut:81",
     "monsterClass": "construct",
     "spawnGroup": "ll2_whirl_return",
     "phraseID": "ll2_whirl_return"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ll2_whirl.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ll2_whirl.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ll2_whirl.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ll2_whirl.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
