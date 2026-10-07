---
description: "Godoe is a non-player character (NPC) in Andor's Trail, found in guynmart_wood_18."
---

# ![](../assets/icons/monsters/monsters_ld1_20.png){ .sprite } Godoe

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_20.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | guynmart_wood_18 |
| **Entries in game data** | 2 |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Godoe. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: appearance. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`godoe1`](#v-godoe1) | NPC | [guynmart_wood_18](../maps/guynmart_wood_18.md#pin-npc-godoe1) | – |
| [`godoe2`](#v-godoe2) | NPC | [guynmart_wood_18](../maps/guynmart_wood_18.md#pin-npc-godoe2) | – |

## Guynmart wood 18 (godoe1) { #v-godoe1 }

**Entry ID:** `godoe1` · **Type:** NPC

**Location:** [guynmart_wood_18](../maps/guynmart_wood_18.md#pin-npc-godoe1)

### Quests

- [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md): stage 80

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Godoe. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/godoe.json" data-npc="Godoe" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-godoe1-godoe"></span>**`godoe`** Godoe: “Hello, strange kid. Wanna pass?”

    - “Yes, please.” → [godoe_2](#d-godoe1-godoe_2)

    <span id="d-godoe1-godoe_2"></span>**`godoe_2`** Godoe: “Gimme 5 red glassy stones, and I'll open the path for you.”

    - “Sure, I have plenty of them.” *(if hand over 5× [Ruby gem](../items/gem2.md))* → [godoe_10](#d-godoe1-godoe_10)
    - “Are 5 shiny gold coins OK too?” *(if have 5 gold)* → [godoe_4](#d-godoe1-godoe_4)

    <span id="d-godoe1-godoe_10"></span>**`godoe_10`** Godoe: “Good, good! Here you go. But don't waste time.” — **effects:** sets stage 80 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-80), faction “guynmart18” set to 0


    <span id="d-godoe1-godoe_4"></span>**`godoe_4`** Godoe: “Did I hear 500?”

    - “Eh, sure. 500 shiny gold coins.” *(if pay 500 gold)* → [godoe_10](#d-godoe1-godoe_10)
    - “Forget it.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (godoe1)"

    | | |
    |---|---|
    | Entry ID | `godoe1` |
    | Spawn group | `godoe1` |
    | Loot table | – |
    | Conversation | `godoe` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:20` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "godoe1",
     "name": "Godoe",
     "iconID": "monsters_ld1:20",
     "moveCost": 4,
     "monsterClass": "humanoid",
     "phraseID": "godoe"
    }
    ```


## Guynmart wood 18 (godoe2) { #v-godoe2 }

**Entry ID:** `godoe2` · **Type:** NPC

**Location:** [guynmart_wood_18](../maps/guynmart_wood_18.md#pin-npc-godoe2)

### Quests

- [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md): stage 80

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Godoe. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/godoe.json" data-npc="Godoe" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [godoe](#d-godoe1-godoe).


### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (godoe2)"

    | | |
    |---|---|
    | Entry ID | `godoe2` |
    | Spawn group | `godoe2` |
    | Loot table | – |
    | Conversation | `godoe` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:21` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "godoe2",
     "name": "Godoe",
     "iconID": "monsters_ld1:21",
     "moveCost": 4,
     "monsterClass": "humanoid",
     "phraseID": "godoe"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=godoe1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=godoe1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=godoe1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=godoe1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
