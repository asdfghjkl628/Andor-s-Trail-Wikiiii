---
description: "Jerelin is a non-player character (NPC) in Andor's Trail, found in Lake Laeroth."
---

# ![](../assets/icons/monsters/monsters_gisons_10.png){ .sprite } Jerelin

**Where to find Jerelin:** [Lake Laeroth, Laerothtomb 1](#v-jerelin), [Lake Laeroth, Laerothtomb 1](#v-jerelin_b)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_gisons_10.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Lake Laeroth |
| **Introduced** | [v0.8.11](../versions/0.8.11.md) |

</div>

## Lake Laeroth, Laerothtomb 1 { #v-jerelin }

**Where:** Lake Laeroth: [Laerothtomb 1](../maps/laerothtomb1.md#pin-npc-jerelin)

### Quests

- [Take care of the caretaker](../quests/laeroth_caretaker.md): stage 110

### Dialogue simulator

Set your quest stages and items, then talk to Jerelin. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/jerelin_0.json" data-npc="Jerelin" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-jerelin-jerelin_0"></span>**`jerelin_0`** [Jerelin](../monsters/jerelin.md): “I dislike being disturbed. I disliked it when I was alive, and I dislike it even more now!” — **effects:** spawns monsters on laerothtomb1

    - Next → [jerelin_1](#d-jerelin-jerelin_1)

    <span id="d-jerelin-jerelin_1"></span>**`jerelin_1`** Jerelin: “Hmpff. Go away! [You take the rather dull looking oegyth crystal.]” — **effects:** removes monsters from laerothtomb1, gives 1× [Heavily diminished oegyth crystal](../items/oegyth4.md), sets stage 110 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-110)

    - Next → *NPC leaves*



### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Lake Laeroth, Laerothtomb 1 (2) { #v-jerelin_b }

**Where:** Lake Laeroth: [Laerothtomb 1](../maps/laerothtomb1.md#pin-npc-jerelin_b)

### Quests

- [Take care of the caretaker](../quests/laeroth_caretaker.md): stage 170

### Dialogue simulator

Set your quest stages and items, then talk to Jerelin. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/jerelin_b_2a.json" data-npc="Jerelin" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-jerelin_b-jerelin_b_2a"></span>**`jerelin_b_2a`** [Jerelin](../monsters/jerelin.md#v-jerelin_b): “Again? I told you I don't like being disturbed!” — **effects:** spawns monsters on laerothtomb1

    - “I spoke to Audela. She said to tell you that she insists you do this. She even made some kind of threat about reaching…” → [jerelin_b_3](#d-jerelin_b-jerelin_b_3)

    <span id="d-jerelin_b-jerelin_b_3"></span>**`jerelin_b_3`** Jerelin: “It seems I can't escape my nagging wife even in death! OK, I release the caretaker from the oath. But there is a condition. He needs to do one more thing, which is to move my grave away from my wife's grave so that I can rest in peace.…” — **effects:** gives 1× [Depleted oegyth crystal](../items/oegyth7.md), sets stage 170 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-170), removes monsters from laerothtomb1




### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Jerelin. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation.

| Entry | Type | Section |
|---|---|---|
| `jerelin` | NPC | [Lake Laeroth, Laerothtomb 1](#v-jerelin) |
| `jerelin_b` | NPC | [Lake Laeroth, Laerothtomb 1](#v-jerelin_b) |

??? info "Technical information: jerelin"

    | | |
    |---|---|
    | Entry ID | `jerelin` |
    | Type (wiki) | NPC |
    | Spawn group | `jerelin` |
    | Loot table | – |
    | Conversation | `jerelin_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_gisons:10` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "jerelin",
     "name": "Jerelin",
     "iconID": "monsters_gisons:10",
     "monsterClass": "undead",
     "spawnGroup": "jerelin",
     "phraseID": "jerelin_0"
    }
    ```

??? info "Technical information: jerelin_b"

    | | |
    |---|---|
    | Entry ID | `jerelin_b` |
    | Type (wiki) | NPC |
    | Spawn group | `jerelin_b` |
    | Loot table | – |
    | Conversation | `jerelin_b_2a` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_gisons:10` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "jerelin_b",
     "name": "Jerelin",
     "iconID": "monsters_gisons:10",
     "monsterClass": "undead",
     "spawnGroup": "jerelin_b",
     "phraseID": "jerelin_b_2a"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jerelin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jerelin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jerelin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jerelin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
