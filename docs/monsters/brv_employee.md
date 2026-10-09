---
description: "Stebbarik is a non-player character (NPC) in Andor's Trail, found in Brimhaven. Starts Work for debts."
---

# ![](../assets/icons/monsters/monsters_ld1_34.png){ .sprite } Stebbarik

**Where to find Stebbarik:** [Brimhaven, Brimhaven employee](#v-brv_employee), [Brimhaven, Brimhaven tavern 1](#v-brv_employee2)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_34.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Starts [Work for debts](../quests/brv_employee.md) |
| **Found in** | Brimhaven |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

## Brimhaven, Brimhaven employee { #v-brv_employee }

**Where:** Brimhaven: [Brimhaven employee](../maps/brimhaven_employee.md#pin-npc-brv_employee) · **Role:** Starts [Work for debts](../quests/brv_employee.md)

### Quests

- [Work for debts](../quests/brv_employee.md): stage 10

### Dialogue simulator

Set your quest stages and items, then talk to Stebbarik. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_employee.json" data-npc="Stebbarik" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (11 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_employee-brv_employee"></span>**`brv_employee`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 90 of [Work for debts](../quests/brv_employee.md#stage-90))* → [brv_employee_90](#d-brv_employee-brv_employee_90)
    - branch 2 *(if reached stage 40 of [Work for debts](../quests/brv_employee.md#stage-40))* → [brv_employee_40](#d-brv_employee-brv_employee_40)
    - branch 3 *(if reached stage 30 of [Work for debts](../quests/brv_employee.md#stage-30))* → [brv_employee_30](#d-brv_employee-brv_employee_30)
    - branch 4 *(if reached stage 10 of [Work for debts](../quests/brv_employee.md#stage-10))* → [brv_employee_10](#d-brv_employee-brv_employee_10)
    - branch 5 → [brv_employee_01](#d-brv_employee-brv_employee_01)

    <span id="d-brv_employee-brv_employee_90"></span>**`brv_employee_90`** Stebbarik: “Thank you for your help!”

    - “Was a pleasure.” → *conversation ends*

    <span id="d-brv_employee-brv_employee_40"></span>**`brv_employee_40`** Stebbarik: “Did you start working already?”

    - “Yes. It is hard work, really.” → *conversation ends*

    <span id="d-brv_employee-brv_employee_30"></span>**`brv_employee_30`** Stebbarik: “Did you talk to Gnossath?”

    - “Yes. He wants me to carry heavy boulders.” → *conversation ends*

    <span id="d-brv_employee-brv_employee_10"></span>**`brv_employee_10`** Stebbarik: “Did you talk to Gnossath?”

    - “Not yet.” → *conversation ends*

    <span id="d-brv_employee-brv_employee_01"></span>**`brv_employee_01`** Stebbarik: “Ooh. Oooooh!”

    - “Hey, what's the matter with you?” → [brv_employee_02](#d-brv_employee-brv_employee_02)

    <span id="d-brv_employee-brv_employee_02"></span>**`brv_employee_02`** Stebbarik: “I feel so bad.”

    - “Looks like a bit of a fever. Just stay in bed for a few days.” → [brv_employee_03](#d-brv_employee-brv_employee_03)

    <span id="d-brv_employee-brv_employee_03"></span>**`brv_employee_03`** Stebbarik: “But I can't! I mustn't! Gnossath would kill me.”

    - “Gnossath would kill you? Why?” → [brv_employee_04](#d-brv_employee-brv_employee_04)

    <span id="d-brv_employee-brv_employee_04"></span>**`brv_employee_04`** Stebbarik: “I am working for him.”

    - Next → [brv_employee_05](#d-brv_employee-brv_employee_05)

    <span id="d-brv_employee-brv_employee_05"></span>**`brv_employee_05`** Stebbarik: “He lent me money, so that I could afford this house. But no work - no money. I fear that if I can't pay my debts, Gnossath will take my house.”

    - “Maybe I could help you? I could do your work.” → [brv_employee_06](#d-brv_employee-brv_employee_06)
    - “That's the way it goes, man. Have a nice day.” → *conversation ends*

    <span id="d-brv_employee-brv_employee_06"></span>**`brv_employee_06`** Stebbarik: “You would do that? Oh, thank you! Thank you!” — **effects:** sets stage 10 of [Work for debts](../quests/brv_employee.md#stage-10)

    - “And you - get healthy again!” → *conversation ends*
    - “I have too good a heart.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 11 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven tavern 1 { #v-brv_employee2 }

**Where:** Brimhaven: [Brimhaven tavern 1](../maps/brimhaven_tavern1.md#pin-npc-brv_employee2)

### Dialogue simulator

Set your quest stages and items, then talk to Stebbarik. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_employee2.json" data-npc="Stebbarik" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_employee2-brv_employee2"></span>**`brv_employee2`** Stebbarik: “Hey kid! Come and have a drink with me!” — **effects:** clears stage 11 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-11)

    - “No, thank you.” → *conversation ends*
    - “I thought you were ill?” *(if reached stage 90 of [Work for debts](../quests/brv_employee.md#stage-90))* → [brv_employee2_10](#d-brv_employee2-brv_employee2_10)

    <span id="d-brv_employee2-brv_employee2_10"></span>**`brv_employee2_10`** Stebbarik: “I am still ill - just taking my medicine here.”




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Stebbarik. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location.

| Entry | Type | Section |
|---|---|---|
| `brv_employee` | NPC | [Brimhaven, Brimhaven employee](#v-brv_employee) |
| `brv_employee2` | NPC | [Brimhaven, Brimhaven tavern 1](#v-brv_employee2) |

??? info "Technical information: brv_employee"

    | | |
    |---|---|
    | Entry ID | `brv_employee` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_employee` |
    | Loot table | – |
    | Conversation | `brv_employee` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:34` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_employee",
     "name": "Stebbarik",
     "iconID": "monsters_ld1:34",
     "moveCost": 5,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_employee",
     "phraseID": "brv_employee"
    }
    ```

??? info "Technical information: brv_employee2"

    | | |
    |---|---|
    | Entry ID | `brv_employee2` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_employee2` |
    | Loot table | – |
    | Conversation | `brv_employee2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:34` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_employee2",
     "name": "Stebbarik",
     "iconID": "monsters_ld1:34",
     "moveCost": 5,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_employee2",
     "phraseID": "brv_employee2"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_employee.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_employee.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_employee.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_employee.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
