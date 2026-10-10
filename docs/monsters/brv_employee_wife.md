---
description: "Hettah is a non-player character (NPC) in Andor's Trail, found in Brimhaven."
---

# ![](../assets/icons/monsters/monsters_ld1_155.png){ .sprite } Hettah

**Where to find Hettah:** [Brimhaven, Brimhaven employee](#v-brv_employee_wife), [Brimhaven, Brimhaven tavern 1](#v-brv_employee_wife2)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_155.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Brimhaven |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

## Brimhaven, Brimhaven employee { #v-brv_employee_wife }

**Where:** Brimhaven: [Brimhaven employee](../maps/brimhaven_employee.md#pin-npc-brv_employee_wife)

### Dialogue simulator

Set your quest stages and items, then talk to Hettah. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_employee_wife.json" data-npc="Hettah" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_employee_wife-brv_employee_wife"></span>**`brv_employee_wife`** Hettah: “Who are you? Stebbarik, my husband, is not at home.”

    - Next → [brv_employee_wife_10](#d-brv_employee_wife-brv_employee_wife_10)

    <span id="d-brv_employee_wife-brv_employee_wife_10"></span>**`brv_employee_wife_10`** Hettah: “Not at home, no. He never is.”

    - Next → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven tavern 1 { #v-brv_employee_wife2 }

**Where:** Brimhaven: [Brimhaven tavern 1](../maps/brimhaven_tavern1.md#pin-npc-brv_employee_wife2)

### Dialogue simulator

Set your quest stages and items, then talk to Hettah. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_employee_wife2.json" data-npc="Hettah" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_employee_wife2-brv_employee_wife2"></span>**`brv_employee_wife2`** Hettah: “Hey kid! Come and have a drink with me!”

    - “No, thank you.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Hettah. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location.

| Entry | Type | Section |
|---|---|---|
| `brv_employee_wife` | NPC | [Brimhaven, Brimhaven employee](#v-brv_employee_wife) |
| `brv_employee_wife2` | NPC | [Brimhaven, Brimhaven tavern 1](#v-brv_employee_wife2) |

??? info "Technical information: brv_employee_wife"

    | | |
    |---|---|
    | Entry ID | `brv_employee_wife` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_employee_wife` |
    | Loot table | – |
    | Conversation | `brv_employee_wife` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:155` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_employee_wife",
     "name": "Hettah",
     "iconID": "monsters_ld1:155",
     "moveCost": 5,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_employee_wife",
     "phraseID": "brv_employee_wife"
    }
    ```

??? info "Technical information: brv_employee_wife2"

    | | |
    |---|---|
    | Entry ID | `brv_employee_wife2` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_employee_wife2` |
    | Loot table | – |
    | Conversation | `brv_employee_wife2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:155` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_employee_wife2",
     "name": "Hettah",
     "iconID": "monsters_ld1:155",
     "moveCost": 5,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_employee_wife2",
     "phraseID": "brv_employee_wife2"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_employee_wife.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_employee_wife.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_employee_wife.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_employee_wife.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
