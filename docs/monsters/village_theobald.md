---
description: "Theobald is a non-player character (NPC) in Andor's Trail, found in Wexlow Village, Gamjee well jail cells."
---

# ![](../assets/icons/monsters/monsters_ld1_121.png){ .sprite } Theobald

**Where to find Theobald:** [Wexlow Village, Wexlow village](#v-village_theobald), [Gamjee well jail cells](#v-troll_hollow_theobald)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld1_121.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Wexlow Village, Gamjee well jail cells |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

</div>

## Wexlow Village, Wexlow village { #v-village_theobald }

**Where:** Wexlow Village: [Wexlow village](../maps/wexlow_village.md#pin-npc-village_theobald)

### Dialogue simulator

Talk to Theobald as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/village_theobald_start.json" data-npc="Theobald" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (8 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-village_theobald-village_theobald_start"></span>**`village_theobald_start`** Theobald: “We are indebted to you now. Your heroism will never be forgotten by the members of this tiny village.”

    - “Why do you live in this "tiny village" anyway?” → [village_theobald_1](#d-village_theobald-village_theobald_1)

    <span id="d-village_theobald-village_theobald_1"></span>**`village_theobald_1`** Theobald: “That is indeed an excellent question.”

    - Next → [village_theobald_2](#d-village_theobald-village_theobald_2)

    <span id="d-village_theobald-village_theobald_2"></span>**`village_theobald_2`** Theobald: “Let me explain.”

    - “Please, go ahead.” → [village_theobald_3](#d-village_theobald-village_theobald_3)

    <span id="d-village_theobald-village_theobald_3"></span>**`village_theobald_3`** Theobald: “You see, all eight of us were born and raised in the glorious city of Feygard. In fact, we grew up together. Best friends too! But for various reasons, things started to change for us.”

    - “Really? I am intrigued to hear more.” → [village_theobald_4](#d-village_theobald-village_theobald_4)

    <span id="d-village_theobald-village_theobald_4"></span>**`village_theobald_4`** Theobald: “Well, I don't want to speak for everyone else, but for Theodora and I, we began to desire a quieter, more laid back lifestyle.”

    - “That makes sense. But what about the others?” → [village_theobald_5](#d-village_theobald-village_theobald_5)
    - “But do you ever miss it? I mean, if Feygard is so glorious, then you must miss it?” → [village_theobald_miss_feygard](#d-village_theobald-village_theobald_miss_feygard)

    <span id="d-village_theobald-village_theobald_5"></span>**`village_theobald_5`** Theobald: “Well, like I said before, I don't want to talk for them, but Osric is my best friend, so I know he longed for the days he could raise a garden and live off the land.”


    <span id="d-village_theobald-village_theobald_miss_feygard"></span>**`village_theobald_miss_feygard`** Theobald: “Oh, I do miss it a lot. Well, I miss most of it a lot. I miss my family. I miss my old customers coming into my market.”

    - “"Most of it"?” → [village_theobald_miss_feygard_2](#d-village_theobald-village_theobald_miss_feygard_2)

    <span id="d-village_theobald-village_theobald_miss_feygard_2"></span>**`village_theobald_miss_feygard_2`** Theobald: “Yeah. I don't miss the noise and the hustle and bustle of the city at all hours of the day. It gets tiresome.”

    - “Thank you for that. It really helped to hear about Feygard from one of its citizens.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 8 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Gamjee well jail cells { #v-troll_hollow_theobald }

**Where:** [Gamjee well jail cells](../maps/gamjee_well_jail_cells.md)


### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Theobald. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location.

| Entry | Type | Section |
|---|---|---|
| `village_theobald` | NPC | [Wexlow Village, Wexlow village](#v-village_theobald) |
| `troll_hollow_theobald` | Scenery | [Gamjee well jail cells](#v-troll_hollow_theobald) |

- `troll_hollow_theobald` has no conversation and no combat statistics. Other conversations use it as their speaker (the `switchToNPC` field), which is how its name and picture appear in dialogue. The game data also places it on [Gamjee well jail cells](../maps/gamjee_well_jail_cells.md).

??? info "Technical information: village_theobald"

    | | |
    |---|---|
    | Entry ID | `village_theobald` |
    | Type (wiki) | NPC |
    | Spawn group | `village_theobald` |
    | Loot table | – |
    | Conversation | `village_theobald_start` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_ld1:121` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "village_theobald",
     "name": "Theobald",
     "iconID": "monsters_ld1:121",
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "phraseID": "village_theobald_start"
    }
    ```

??? info "Technical information: troll_hollow_theobald"

    | | |
    |---|---|
    | Entry ID | `troll_hollow_theobald` |
    | Type (wiki) | Scenery |
    | Spawn group | `troll_hollow_theobald` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_ld1:121` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "troll_hollow_theobald",
     "name": "Theobald",
     "iconID": "monsters_ld1:121",
     "moveCost": 7,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_theobald.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_theobald.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_theobald.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_theobald.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
