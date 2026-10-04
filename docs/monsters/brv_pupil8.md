# ![](../assets/icons/monsters/monsters_ld1_17.png){ .sprite } Pupil

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_17.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `brv_pupil8` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Brimhaven |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

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
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [brimhaven_school](../maps/brimhaven_school.md) | Brimhaven | 5 | – |


## Quests

- [Lessons learned](../quests/brv_school2.md): stages 110
- [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md): stages 50

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Pupil. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_school_pupil.json" data-npc="Pupil" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brv_school_pupil"></span>**`brv_school_pupil`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 60 of [Lessons learned](../quests/brv_school2.md#stage-60))* → [brv_school_pupil_60_10](#d-brv_school_pupil_60_10)
    - branch 2 → [brv_school_pupil_10](#d-brv_school_pupil_10)

    <span id="d-brv_school_pupil_60_10"></span>**`brv_school_pupil_60_10`** [Dummy NPC](../monsters/none.md): “As you approach the little student, horror spreads on his face.”

    - “Don't panic. I'll go away again.” → *conversation ends*
    - “Wait, I'll show you...” → [brv_school_pupil_60_20](#d-brv_school_pupil_60_20)

    <span id="d-brv_school_pupil_10"></span>**`brv_school_pupil_10`** Pupil: “Hello, big one.”


    <span id="d-brv_school_pupil_60_20"></span>**`brv_school_pupil_60_20`** Pupil: “[He jumps up and runs screaming out of the room. The other little students follow in panic.]” — **effects:** sets stage 110 of [Lessons learned](../quests/brv_school2.md#stage-110), sets stage 50 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-50), removes monsters from brimhaven_school




## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_pupil8.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_pupil8.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_pupil8.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_pupil8.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `brv_pupil8` |
    | Spawn group | `brv_school_pupil` |
    | Loot table | – |
    | Conversation | `brv_school_pupil` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:17` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_pupil8",
     "name": "Pupil",
     "iconID": "monsters_ld1:17",
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_school_pupil",
     "phraseID": "brv_school_pupil"
    }
    ```


<small>Data from v0.8.18</small>
