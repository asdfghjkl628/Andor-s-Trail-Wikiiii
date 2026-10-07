---
description: "Osric is a non-player character (NPC) in Andor's Trail, found in Wexlow Village, gamjee_well_jail_cells."
---

# ![](../assets/icons/monsters/monsters_ld1_130.png){ .sprite } Osric

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_130.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Wexlow Village, gamjee_well_jail_cells |
| **Entries in game data** | 2 |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Osric. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`wexlow_osric`](#v-wexlow_osric) | NPC | Wexlow Village: [wexlow_village](../maps/wexlow_village.md#pin-npc-wexlow_osric) | – |
| [`troll_hollow_osric`](#v-troll_hollow_osric) | NPC | [gamjee_well_jail_cells](../maps/gamjee_well_jail_cells.md#pin-npc-troll_hollow_osric) | – |

## Wexlow Village, Wexlow village (wexlow_osric) { #v-wexlow_osric }

**Entry ID:** `wexlow_osric` · **Type:** NPC

**Location:** Wexlow Village: [wexlow_village](../maps/wexlow_village.md#pin-npc-wexlow_osric)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Osric. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/wexlow_osric_start.json" data-npc="Osric" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-wexlow_osric-wexlow_osric_start"></span>**`wexlow_osric_start`** Osric: “Thank you! Thank you! We men tried to rescue our wives, but you succeeded. Thank you!”

    - “How did the troll manage to capture all of you without anyone noticing?” → [wexlow_osric_1](#d-wexlow_osric-wexlow_osric_1)
    - “What about the state of your village? How will you repair it?” → [wexlow_osric_cleanup](#d-wexlow_osric-wexlow_osric_cleanup)

    <span id="d-wexlow_osric-wexlow_osric_1"></span>**`wexlow_osric_1`** Osric: “Once the women were taken, the troll mimicked their voices, calling out to us men. We thought our wives needed help, but it was a trap.”

    - “Scary.” → [wexlow_osric_2](#d-wexlow_osric-wexlow_osric_2)

    <span id="d-wexlow_osric-wexlow_osric_cleanup"></span>**`wexlow_osric_cleanup`** Osric: “It's like the village itself fell into a deep sleep, just like us. Now, we have to wake it up again, clean out the overgrowth, and hope the roots haven't gone too deep. This'll take every bit of strength we've got.”

    - “Oh, it most certainly will.” → *conversation ends*

    <span id="d-wexlow_osric-wexlow_osric_2"></span>**`wexlow_osric_2`** Osric: “Each of us was lured by what we thought were our loved ones. By the time we realized the truth, it was too late.”

    - “But after one of you men was grabbed, how did the last two of you stll fall for this trap?” → [wexlow_osric_3](#d-wexlow_osric-wexlow_osric_3)

    <span id="d-wexlow_osric-wexlow_osric_3"></span>**`wexlow_osric_3`** Osric: “Each of us was taken silently and swiftly. By the time we realized something was wrong, it was too late.”

    - “I guess that makes some sense.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (wexlow_osric)"

    | | |
    |---|---|
    | Entry ID | `wexlow_osric` |
    | Spawn group | `wexlow_osric` |
    | Loot table | – |
    | Conversation | `wexlow_osric_start` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_ld1:130` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "wexlow_osric",
     "name": "Osric",
     "iconID": "monsters_ld1:130",
     "moveCost": 10,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "phraseID": "wexlow_osric_start"
    }
    ```


## Gamjee well jail cells (troll_hollow_osric) { #v-troll_hollow_osric }

**Entry ID:** `troll_hollow_osric` · **Type:** NPC

**Location:** [gamjee_well_jail_cells](../maps/gamjee_well_jail_cells.md#pin-npc-troll_hollow_osric)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Osric. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/gamjee_well_osric_1.json" data-npc="Osric" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-troll_hollow_osric-gamjee_well_osric_1"></span>**`gamjee_well_osric_1`** Osric: “Please meet us back to Wexlow Village.”

    - “Sounds good.” → [gamjee_well_osric_2](#d-troll_hollow_osric-gamjee_well_osric_2)
    - “Wexlow Village? Where's that?” → [gamjee_well_osric_3](#d-troll_hollow_osric-gamjee_well_osric_3)

    <span id="d-troll_hollow_osric-gamjee_well_osric_2"></span>**`gamjee_well_osric_2`** Osric: “Bye.” — **effects:** removes monsters from gamjee_well_jail_cells


    <span id="d-troll_hollow_osric-gamjee_well_osric_3"></span>**`gamjee_well_osric_3`** Osric: “Didn't you find us after visiting our village and our well?”

    - Next → [gamjee_well_osric_4](#d-troll_hollow_osric-gamjee_well_osric_4)

    <span id="d-troll_hollow_osric-gamjee_well_osric_4"></span>**`gamjee_well_osric_4`** Osric: “Yes, that place. I am leaving now. I will see you there.” — **effects:** removes monsters from gamjee_well_jail_cells




### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (troll_hollow_osric)"

    | | |
    |---|---|
    | Entry ID | `troll_hollow_osric` |
    | Spawn group | `troll_hollow_osric` |
    | Loot table | – |
    | Conversation | `gamjee_well_osric_1` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_ld1:130` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "troll_hollow_osric",
     "name": "Osric",
     "iconID": "monsters_ld1:130",
     "moveCost": 3,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "phraseID": "gamjee_well_osric_1"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wexlow_osric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wexlow_osric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wexlow_osric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wexlow_osric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
