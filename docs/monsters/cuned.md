---
description: "Cuned is a non-player character (NPC) in Andor's Trail, found in Lake Laeroth."
---

# ![](../assets/icons/monsters/monsters_gisons_9.png){ .sprite } Cuned

**Where to find Cuned:** Lake Laeroth: [laerothtomb1](../maps/laerothtomb1.md#pin-npc-cuned)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_gisons_9.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Lake Laeroth |
| **Entry ID** | `cuned` |
| **Introduced** | [v0.8.11](../versions/0.8.11.md) |

</div>

## Quests

- [Take care of the caretaker](../quests/laeroth_caretaker.md): stage 90

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Cuned. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/cuned_2a.json" data-npc="Cuned" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-cuned_2a"></span>**`cuned_2a`** [Cuned](../monsters/cuned.md): “What do you want? I was at peace until you brought me back!”

    - “I am $playername. Apologies for distubing you, but I need some help.” → [cuned_3](#d-cuned_3)

    <span id="d-cuned_3"></span>**`cuned_3`** Cuned: “What do you want?”

    - “Your family has left Laeroth, and it is now abandoned. But the caretaker is still here. He is bound by an oath his…” → [cuned_4](#d-cuned_4)

    <span id="d-cuned_4"></span>**`cuned_4`** Cuned: “Eyvipa was not made Lord because he was lazy and irresponsible. If he chose to he could release the caretaker, but he is obviously still irresponsible. I am afraid Verigil is correct. I cannot release him either. You will have to talk to…” — **effects:** removes monsters from laerothtomb1, sets stage 90 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-90), gives 1× [Very diminished oegyth crystal](../items/oegyth3.md)

    - Next → *NPC leaves*



## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `cuned` |
    | Spawn group | `cuned` |
    | Loot table | – |
    | Conversation | `cuned_2a` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_gisons:9` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "cuned",
     "name": "Cuned",
     "iconID": "monsters_gisons:9",
     "monsterClass": "undead",
     "movementAggressionType": "none",
     "spawnGroup": "cuned",
     "phraseID": "cuned_2a"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cuned.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cuned.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cuned.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cuned.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
