# ![](../assets/icons/monsters/monsters_ld1_94.png){ .sprite } Brightport guard

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_94.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `brightportnorthguard` |
| **Type** | NPC |
| **Class** | ? |
| **HP** | 1 |
| **Found in** | Brightport |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 1 |
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
| [brightport4](../maps/brightport4.md) | Brightport | 1 | – |


## Quests

- [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md): stages 251

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Brightport guard. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_guard_north1.json" data-npc="Brightport guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightport_guard_north1"></span>**`brightport_guard_north1`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 249 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-249))* → [brightport_guard_north0](#d-brightport_guard_north0)
    - Next *(if reached stage 250 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-250))* → [brightport_guard_north2](#d-brightport_guard_north2)

    <span id="d-brightport_guard_north0"></span>**`brightport_guard_north0`** Brightport guard: “Coming in from the north? Then you must have seen the terrible state of the forest. Some say it's a curse sent upon Brightport by the Shadow for what happened at the Great Water Temple.”

    - “Can you tell me more about that?” → [brightport_guard_north3](#d-brightport_guard_north3)

    <span id="d-brightport_guard_north2"></span>**`brightport_guard_north2`** Brightport guard: “The road north runs through that forsaken forest, but it's still better than heading south. Keep yourself safe.”

    - “What's happening to the south?” → [brightport_guard_north4](#d-brightport_guard_north4)

    <span id="d-brightport_guard_north3"></span>**`brightport_guard_north3`** Brightport guard: “I wouldn't know. I'm from Feygard, but you could ask at the small temple in town.” — **effects:** sets stage 251 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-251)


    <span id="d-brightport_guard_north4"></span>**`brightport_guard_north4`** Brightport guard: “The deer started attacking people. It's odd, but they tend to stay away if you're traveling in a group.”

    - “Terrible times to be a lone traveler.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnorthguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnorthguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnorthguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnorthguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `brightportnorthguard` |
    | Spawn group | `brightportnorthguard` |
    | Loot table | – |
    | Conversation | `brightport_guard_north1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:94` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportnorthguard",
     "name": "Brightport guard",
     "iconID": "monsters_ld1:94",
     "phraseID": "brightport_guard_north1"
    }
    ```


<small>Data from v0.8.18</small>
