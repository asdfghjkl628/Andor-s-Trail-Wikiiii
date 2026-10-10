---
description: "Oromir is a non-player character (NPC) in Andor's Trail, found in Crossglen."
---

# ![](../assets/icons/monsters/monsters_man1_0.png){ .sprite } Oromir

**Where to find Oromir:** [Crossglen, Crossglen](#v-oromir), [Crossglen, Crossglen farmhouse basement](#v-oromir_basement), [Crossglen, Crossglen farmhouse basement](#v-oromir_basement_help), [Crossglen, Crossglen](#v-oromir_behind_haystack), [Crossglen, Crossglen](#v-oromir_behind_haystack_help), [Crossglen, Crossglen](#v-oromir_behind_inn), [Crossglen, Crossglen](#v-oromir_behind_inn_help)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_man1_0.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Crossglen |
| **Introduced** | v0.7.0 or earlier |

</div>

## Crossglen, Crossglen { #v-oromir }

**Where:** Crossglen: [Crossglen](../maps/crossglen.md#pin-npc-oromir)

### Quests

- [Missing husband](../quests/leta.md): stages 20, 25

### Dialogue simulator

Talk to Oromir as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/oromir1.json" data-npc="Oromir" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-oromir-oromir1"></span>**`oromir1`** Oromir: “Oh you startled me. Hello.”

    - “Hello.” → [oromir2](#d-oromir-oromir2)

    <span id="d-oromir-oromir2"></span>**`oromir2`** Oromir: “I'm hiding here from my wife Leta. She is always getting angry at me for not helping out on the farm. Please don't tell her that I'm here.” — **effects:** sets stage 20 of [Missing husband](../quests/leta.md#stage-20)

    - “[Lie] OK.” → *conversation ends*
    - “Your secret is safe with me.” *(if NOT reached stage 100 of [Missing husband](../quests/leta.md#stage-100))* → [oromir_trees_help_10](#d-oromir-oromir_trees_help_10)

    <span id="d-oromir-oromir_trees_help_10"></span>**`oromir_trees_help_10`** Oromir: “Thank you, friend.” — **effects:** sets stage 25 of [Missing husband](../quests/leta.md#stage-25)




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines changed |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 1 line added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Crossglen, Crossglen farmhouse basement { #v-oromir_basement }

**Where:** Crossglen: [Crossglen farmhouse basement](../maps/crossglen_farmhouse_basement.md#pin-npc-oromir_basement)

### Quests

- [Missing husband](../quests/leta.md): stage 80

### Dialogue simulator

Talk to Oromir as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/oromir_basement_10.json" data-npc="Oromir" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-oromir_basement-oromir_basement_10"></span>**`oromir_basement_10`** Oromir: “You did it again? Stop telling Leta where I am.”

    - “I'm sorry, but I think that it's better if I'm on Leta's side.” → [oromir_basement_20](#d-oromir_basement-oromir_basement_20)

    <span id="d-oromir_basement-oromir_basement_20"></span>**`oromir_basement_20`** Oromir: “Yep. That's something that I've not learnt to do.” — **effects:** sets stage 80 of [Missing husband](../quests/leta.md#stage-80)




### Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Crossglen, Crossglen farmhouse basement (2) { #v-oromir_basement_help }

**Where:** Crossglen: [Crossglen farmhouse basement](../maps/crossglen_farmhouse_basement.md#pin-npc-oromir_basement_help)

### Quests

- [Missing husband](../quests/leta.md): stage 105

### Dialogue simulator

Talk to Oromir as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/oromir_basement_help_10.json" data-npc="Oromir" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-oromir_basement_help-oromir_basement_help_10"></span>**`oromir_basement_help_10`** Oromir: “Thank you for not telling my wife where I've been.”

    - “Why are you back in the house?” *(if reached stage 45 of [Missing husband](../quests/leta.md#stage-45))* → [oromir_basement_help_20](#d-oromir_basement_help-oromir_basement_help_20)
    - “You're welcome.” *(if reached stage 105 of [Missing husband](../quests/leta.md#stage-105))* → [oromir_basement_help_15](#d-oromir_basement_help-oromir_basement_help_15)

    <span id="d-oromir_basement_help-oromir_basement_help_20"></span>**`oromir_basement_help_20`** Oromir: “That mysterious looking man in the inn saw me and ratted me out and now I'm down here cleaning as a punishment.”

    - “I'm sorry to hear that.” *(if NOT reached stage 105 of [Missing husband](../quests/leta.md#stage-105))* → [oromir_basement_help_30](#d-oromir_basement_help-oromir_basement_help_30)
    - “I'm sorry to hear that.” *(if reached stage 105 of [Missing husband](../quests/leta.md#stage-105))* → *conversation ends*

    <span id="d-oromir_basement_help-oromir_basement_help_15"></span>**`oromir_basement_help_15`** Oromir: “Goodbye.”


    <span id="d-oromir_basement_help-oromir_basement_help_30"></span>**`oromir_basement_help_30`** Oromir: “While cleaning, I found your kid brother's boots. Please take them as my gift to you for all of your help.” — **effects:** sets stage 105 of [Missing husband](../quests/leta.md#stage-105), gives 1× [Kid's boots](../items/kids_boots.md)




### Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Crossglen, Crossglen (2) { #v-oromir_behind_haystack }

**Where:** Crossglen: [Crossglen](../maps/crossglen.md#pin-npc-oromir_behind_haystack)

### Quests

- [Missing husband](../quests/leta.md): stage 60

### Dialogue simulator

Talk to Oromir as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/oromir_behind_haystack_10.json" data-npc="Oromir" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-oromir_behind_haystack-oromir_behind_haystack_10"></span>**`oromir_behind_haystack_10`** Oromir: “You did it again? Stop telling Leta where I am.”

    - “A happy wife is a happy life. Go home.” → [oromir_behind_haystack_20](#d-oromir_behind_haystack-oromir_behind_haystack_20)

    <span id="d-oromir_behind_haystack-oromir_behind_haystack_20"></span>**`oromir_behind_haystack_20`** Oromir: “No thanks. I'm staying here.” — **effects:** sets stage 60 of [Missing husband](../quests/leta.md#stage-60)




### Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Crossglen, Crossglen (3) { #v-oromir_behind_haystack_help }

**Where:** Crossglen: [Crossglen](../maps/crossglen.md#pin-npc-oromir_behind_haystack_help)

### Quests

- [Missing husband](../quests/leta.md): stage 45

### Dialogue simulator

Talk to Oromir as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/oromir_behind_haystack_help_10.json" data-npc="Oromir" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-oromir_behind_haystack_help-oromir_behind_haystack_help_10"></span>**`oromir_behind_haystack_help_10`** Oromir: “I had a feeling that Leta was close to finding me, so I moved here.”

    - “That's a wise move because she has asked me to inform her of your whereabouts. But I won't do so.” → [oromir_behind_haystack_help_20](#d-oromir_behind_haystack_help-oromir_behind_haystack_help_20)

    <span id="d-oromir_behind_haystack_help-oromir_behind_haystack_help_20"></span>**`oromir_behind_haystack_help_20`** Oromir: “Thank you, friend.” — **effects:** sets stage 45 of [Missing husband](../quests/leta.md#stage-45)




### Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Crossglen, Crossglen (4) { #v-oromir_behind_inn }

**Where:** Crossglen: [Crossglen](../maps/crossglen.md#pin-npc-oromir_behind_inn)

### Quests

- [Missing husband](../quests/leta.md): stage 40

### Dialogue simulator

Talk to Oromir as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/oromir_behind_inn_10.json" data-npc="Oromir" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-oromir_behind_inn-oromir_behind_inn_10"></span>**`oromir_behind_inn_10`** Oromir: “Why did you tell Leta where I was?”

    - “You are needed at home.” → [oromir_behind_inn_20](#d-oromir_behind_inn-oromir_behind_inn_20)

    <span id="d-oromir_behind_inn-oromir_behind_inn_20"></span>**`oromir_behind_inn_20`** Oromir: “I see.” — **effects:** sets stage 40 of [Missing husband](../quests/leta.md#stage-40)




### Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Crossglen, Crossglen (5) { #v-oromir_behind_inn_help }

**Where:** Crossglen: [Crossglen](../maps/crossglen.md#pin-npc-oromir_behind_inn_help)

### Quests

- [Missing husband](../quests/leta.md): stage 35

### Dialogue simulator

Talk to Oromir as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/oromir_behind_inn_help_10.json" data-npc="Oromir" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-oromir_behind_inn_help-oromir_behind_inn_help_10"></span>**`oromir_behind_inn_help_10`** Oromir: “I had a feeling that Leta was close to finding me, so I moved here.”

    - “That's a wise move because she has asked me to inform her of your whereabouts. But I won't do so.” → [oromir_behind_inn_help_20](#d-oromir_behind_inn_help-oromir_behind_inn_help_20)

    <span id="d-oromir_behind_inn_help-oromir_behind_inn_help_20"></span>**`oromir_behind_inn_help_20`** Oromir: “Thank you, friend.” — **effects:** sets stage 35 of [Missing husband](../quests/leta.md#stage-35)




### Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**7 entries.** The game data defines 7 separate characters named Oromir. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location, movement.

| Entry | Type | Section |
|---|---|---|
| `oromir` | NPC | [Crossglen, Crossglen](#v-oromir) |
| `oromir_basement` | NPC | [Crossglen, Crossglen farmhouse basement](#v-oromir_basement) |
| `oromir_basement_help` | NPC | [Crossglen, Crossglen farmhouse basement](#v-oromir_basement_help) |
| `oromir_behind_haystack` | NPC | [Crossglen, Crossglen](#v-oromir_behind_haystack) |
| `oromir_behind_haystack_help` | NPC | [Crossglen, Crossglen](#v-oromir_behind_haystack_help) |
| `oromir_behind_inn` | NPC | [Crossglen, Crossglen](#v-oromir_behind_inn) |
| `oromir_behind_inn_help` | NPC | [Crossglen, Crossglen](#v-oromir_behind_inn_help) |

??? info "Technical information: oromir"

    | | |
    |---|---|
    | Entry ID | `oromir` |
    | Type (wiki) | NPC |
    | Spawn group | `oromir` |
    | Loot table | – |
    | Conversation | `oromir1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_man1:0` |
    | Defined in | `res/raw/monsterlist_crossglen_npcs.json` |

    Raw data:

    ```json
    {
     "id": "oromir",
     "name": "Oromir",
     "iconID": "monsters_man1:0",
     "monsterClass": "humanoid",
     "spawnGroup": "oromir",
     "phraseID": "oromir1"
    }
    ```

??? info "Technical information: oromir_basement"

    | | |
    |---|---|
    | Entry ID | `oromir_basement` |
    | Type (wiki) | NPC |
    | Spawn group | `oromir_basement` |
    | Loot table | – |
    | Conversation | `oromir_basement_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_man1:0` |
    | Defined in | `res/raw/monsterlist_brimhaven_2.json` |

    Raw data:

    ```json
    {
     "id": "oromir_basement",
     "name": "Oromir",
     "iconID": "monsters_man1:0",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "oromir_basement",
     "phraseID": "oromir_basement_10"
    }
    ```

??? info "Technical information: oromir_basement_help"

    | | |
    |---|---|
    | Entry ID | `oromir_basement_help` |
    | Type (wiki) | NPC |
    | Spawn group | `oromir_basement_help` |
    | Loot table | – |
    | Conversation | `oromir_basement_help_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_man1:0` |
    | Defined in | `res/raw/monsterlist_brimhaven_2.json` |

    Raw data:

    ```json
    {
     "id": "oromir_basement_help",
     "name": "Oromir",
     "iconID": "monsters_man1:0",
     "monsterClass": "humanoid",
     "phraseID": "oromir_basement_help_10"
    }
    ```

??? info "Technical information: oromir_behind_haystack"

    | | |
    |---|---|
    | Entry ID | `oromir_behind_haystack` |
    | Type (wiki) | NPC |
    | Spawn group | `oromir_behind_haystack` |
    | Loot table | – |
    | Conversation | `oromir_behind_haystack_10` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_man1:0` |
    | Defined in | `res/raw/monsterlist_brimhaven_2.json` |

    Raw data:

    ```json
    {
     "id": "oromir_behind_haystack",
     "name": "Oromir",
     "iconID": "monsters_man1:0",
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "spawnGroup": "oromir_behind_haystack",
     "phraseID": "oromir_behind_haystack_10"
    }
    ```

??? info "Technical information: oromir_behind_haystack_help"

    | | |
    |---|---|
    | Entry ID | `oromir_behind_haystack_help` |
    | Type (wiki) | NPC |
    | Spawn group | `oromir_behind_haystack_help` |
    | Loot table | – |
    | Conversation | `oromir_behind_haystack_help_10` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_man1:0` |
    | Defined in | `res/raw/monsterlist_brimhaven_2.json` |

    Raw data:

    ```json
    {
     "id": "oromir_behind_haystack_help",
     "name": "Oromir",
     "iconID": "monsters_man1:0",
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "spawnGroup": "oromir_behind_haystack_help",
     "phraseID": "oromir_behind_haystack_help_10"
    }
    ```

??? info "Technical information: oromir_behind_inn"

    | | |
    |---|---|
    | Entry ID | `oromir_behind_inn` |
    | Type (wiki) | NPC |
    | Spawn group | `oromir_behind_inn` |
    | Loot table | – |
    | Conversation | `oromir_behind_inn_10` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_man1:0` |
    | Defined in | `res/raw/monsterlist_brimhaven_2.json` |

    Raw data:

    ```json
    {
     "id": "oromir_behind_inn",
     "name": "Oromir",
     "iconID": "monsters_man1:0",
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "spawnGroup": "oromir_behind_inn",
     "phraseID": "oromir_behind_inn_10"
    }
    ```

??? info "Technical information: oromir_behind_inn_help"

    | | |
    |---|---|
    | Entry ID | `oromir_behind_inn_help` |
    | Type (wiki) | NPC |
    | Spawn group | `oromir_behind_inn_help` |
    | Loot table | – |
    | Conversation | `oromir_behind_inn_help_10` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_man1:0` |
    | Defined in | `res/raw/monsterlist_brimhaven_2.json` |

    Raw data:

    ```json
    {
     "id": "oromir_behind_inn_help",
     "name": "Oromir",
     "iconID": "monsters_man1:0",
     "unique": 1,
     "movementAggressionType": "none",
     "spawnGroup": "oromir_behind_inn_help",
     "phraseID": "oromir_behind_inn_help_10"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=oromir.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=oromir.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=oromir.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=oromir.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
