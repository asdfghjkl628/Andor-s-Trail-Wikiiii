---
description: "Verigil is a non-player character (NPC) in Andor's Trail, found in Lake Laeroth."
---

# ![](../assets/icons/monsters/monsters_gisons_13.png){ .sprite } Verigil

**Where to find Verigil:** Lake Laeroth: [laerothtomb1](../maps/laerothtomb1.md#pin-npc-verigil)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_gisons_13.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Lake Laeroth |
| **Entry ID** | `verigil` |
| **Introduced** | [v0.8.11](../versions/0.8.11.md) |

</div>

## Quests

- [Take care of the caretaker](../quests/laeroth_caretaker.md): stage 40

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Verigil. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/verigil_0.json" data-npc="Verigil" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-verigil_0"></span>**`verigil_0`** [Verigil](../monsters/verigil.md): “Who dares to disturb my rest?” — **effects:** spawns monsters on laerothtomb1

    - “I am $playername. Sorry to disturb you, but I need some help.” → [verigil_1](#d-verigil_1)

    <span id="d-verigil_1"></span>**`verigil_1`** Verigil: “With what?”

    - “Your son has left Laeroth, and his whereabouts are unknown. However, the caretaker remains, bound by an oath to look…” → [verigil_2](#d-verigil_2)

    <span id="d-verigil_2"></span>**`verigil_2`** Verigil: “I cannot. It is not my branch of the family that bound him. You must talk to my uncle, Eyvipa. Now let me rest. [You take the oegyth crystal, but decide to leave the ring.]” — **effects:** removes monsters from laerothtomb1, sets stage 40 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-40), gives 1× [Slightly diminished oegyth crystal](../items/oegyth1.md)

    - Next → *NPC leaves*



## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `verigil` |
    | Spawn group | `verigil` |
    | Loot table | – |
    | Conversation | `verigil_0` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_gisons:13` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "verigil",
     "name": "Verigil",
     "iconID": "monsters_gisons:13",
     "monsterClass": "undead",
     "movementAggressionType": "none",
     "spawnGroup": "verigil",
     "phraseID": "verigil_0"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=verigil.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=verigil.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=verigil.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=verigil.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
