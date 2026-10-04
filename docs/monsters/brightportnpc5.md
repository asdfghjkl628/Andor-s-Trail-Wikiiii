# ![](../assets/icons/monsters/monsters_ld1_125.png){ .sprite } Frederich

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_125.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `brightportnpc5` |
| **Type** | NPC |
| **Class** | ? |
| **HP** | 120 |
| **XP when killed** | 84 |
| **Found in** | Brightport |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 120 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [brightport_school10](../maps/brightport_school10.md) | Brightport | 1 | – |


## Quests

- [No rest for the wicked](../quests/Stanwickquest.md): stages 40

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Frederich. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_frederich_selector.json" data-npc="Frederich" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (7 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightport_frederich_selector"></span>**`brightport_frederich_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 224 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-224))* → [brightport_frederich_afterlecture](#d-brightport_frederich_afterlecture)
    - Next *(if reached stage 225 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-225); NOT reached stage 224 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-224))* → [brightport_frederich_lecture](#d-brightport_frederich_lecture)
    - Next *(if NOT reached stage 225 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-225))* → [brightport_frederich_beforelecture](#d-brightport_frederich_beforelecture)

    <span id="d-brightport_frederich_afterlecture"></span>**`brightport_frederich_afterlecture`** Frederich: “The one student whose name I don't remember. The one that didn't bolt out of the door. What is it?”

    - “Could you tell me what you know about the library theft?” *(if reached stage 25 of [No rest for the wicked](../quests/Stanwickquest.md#stage-25); NOT reached stage 96 of [No rest for the wicked](../quests/Stanwickquest.md#stage-96))* → [brightport_frederich](#d-brightport_frederich)
    - “Nothing, bye.” → *conversation ends*

    <span id="d-brightport_frederich_lecture"></span>**`brightport_frederich_lecture`** Frederich: “Back to your seat, student! I will not have anyone interrupting my history lecture.”


    <span id="d-brightport_frederich_beforelecture"></span>**`brightport_frederich_beforelecture`** Frederich: “Class is about to begin, please sit down. I will accept questions after the lecture is over.”


    <span id="d-brightport_frederich"></span>**`brightport_frederich`** Frederich: “What is there to know, the case is solved!”

    - “Why do you think that?” → [brightport_frederich1](#d-brightport_frederich1)

    <span id="d-brightport_frederich1"></span>**`brightport_frederich1`** Frederich: “I always knew that boy Stanwick was up to no good. They made a poor choice entrusting the library to someone associated with those Nor City savages. It's obvious he was tasked to steal the scroll for them.” — **effects:** sets stage 40 of [No rest for the wicked](../quests/Stanwickquest.md#stage-40)

    - Next → [brightport_frederich2](#d-brightport_frederich2)

    <span id="d-brightport_frederich2"></span>**`brightport_frederich2`** Frederich: “It's only a matter of time before he spits out the names of his accomplices.”




## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 7 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `brightportnpc5` |
    | Spawn group | `brightportnpc5` |
    | Loot table | – |
    | Conversation | `brightport_frederich_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:125` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportnpc5",
     "name": "Frederich",
     "iconID": "monsters_ld1:125",
     "maxHP": 120,
     "phraseID": "brightport_frederich_selector"
    }
    ```


<small>Data from v0.8.18</small>
