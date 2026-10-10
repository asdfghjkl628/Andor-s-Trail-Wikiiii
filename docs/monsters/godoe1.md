---
description: "Godoe is a non-player character (NPC) in Andor's Trail, found in Guynmart wood 18."
---

# ![](../assets/icons/monsters/monsters_ld1_20.png){ .sprite } Godoe

**Where to find Godoe:** [Guynmart wood 18](#v-godoe1), [Guynmart wood 18](#v-godoe2)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld1_20.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Guynmart wood 18 |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

</div>

## Guynmart wood 18 { #v-godoe1 }

**Where:** [Guynmart wood 18](../maps/guynmart_wood_18.md#pin-npc-godoe1)

### Quests

- [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md): stage 80

### Dialogue simulator

Talk to Godoe as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/godoe.json" data-npc="Godoe" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-godoe1-godoe"></span>**`godoe`** Godoe: “Hello, strange kid. Wanna pass?”

    - “Yes, please.” → [godoe_2](#d-godoe1-godoe_2)

    <span id="d-godoe1-godoe_2"></span>**`godoe_2`** Godoe: “Gimme 5 red glassy stones, and I'll open the path for you.”

    - “Sure, I have plenty of them.” *(if hand over 5× [Ruby gem](../items/gem2.md))* → [godoe_10](#d-godoe1-godoe_10)
    - “Are 5 shiny gold coins OK too?” *(if have 5 gold)* → [godoe_4](#d-godoe1-godoe_4)

    <span id="d-godoe1-godoe_10"></span>**`godoe_10`** Godoe: “Good, good! Here you go. But don't waste time.” — **effects:** sets stage 80 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-80), faction “guynmart18” set to 0


    <span id="d-godoe1-godoe_4"></span>**`godoe_4`** Godoe: “Did I hear 500?”

    - “Eh, sure. 500 shiny gold coins.” *(if pay 500 gold)* → [godoe_10](#d-godoe1-godoe_10)
    - “Forget it.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Guynmart wood 18 (2) { #v-godoe2 }

**Where:** [Guynmart wood 18](../maps/guynmart_wood_18.md#pin-npc-godoe2)

### Quests

- [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md): stage 80

### Dialogue simulator

Talk to Godoe as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/godoe.json" data-npc="Godoe" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [godoe](#d-godoe1-godoe).


### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Godoe. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: appearance.

| Entry | Type | Section |
|---|---|---|
| `godoe1` | NPC | [Guynmart wood 18](#v-godoe1) |
| `godoe2` | NPC | [Guynmart wood 18](#v-godoe2) |

??? info "Technical information: godoe1"

    | | |
    |---|---|
    | Entry ID | `godoe1` |
    | Type (wiki) | NPC |
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

??? info "Technical information: godoe2"

    | | |
    |---|---|
    | Entry ID | `godoe2` |
    | Type (wiki) | NPC |
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
