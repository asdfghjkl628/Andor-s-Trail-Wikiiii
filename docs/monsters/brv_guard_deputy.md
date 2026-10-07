# ![](../assets/icons/monsters/monsters_ld1_109.png){ .sprite } Ito

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_109.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `brv_guard_deputy` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Brimhaven |
| **Introduced** | [v0.7.12](../versions/0.7.12.md) |

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
| [brimhaven2](../maps/brimhaven2.md) | Brimhaven | 1 | – |


## Quests

- [A strange looking dagger](../quests/brv_dagger.md): stages 220
- [brv_nondisplay_multipurpose (hidden flag)](../quests/brv_nondisplay_multipurpose.md): stages 60

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Ito. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_guard_deputy_10.json" data-npc="Ito" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brv_guard_deputy_10"></span>**`brv_guard_deputy_10`** Ito: “Hello. I am Ito. I help Mustura keep the law around here.”

    - “I'll bear that in mind.” → *conversation ends*
    - “I have proof that Ogea murdered Lawellyn and stole his prized dagger.” *(if reached stage 210 of [A strange looking dagger](../quests/brv_dagger.md#stage-210); carry 1× [Suspect's glove](../items/ogea_glove.md); NOT reached stage 220 of [A strange looking dagger](../quests/brv_dagger.md#stage-220))* → [brv_guard_deputy_asd_10](#d-brv_guard_deputy_asd_10)
    - “I want to discuss Ogea again.” *(if reached stage 60 of [brv_nondisplay_multipurpose (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-60); NOT reached stage 220 of [A strange looking dagger](../quests/brv_dagger.md#stage-220))* → [brv_guard_deputy_asd_20](#d-brv_guard_deputy_asd_20)

    <span id="d-brv_guard_deputy_asd_10"></span>**`brv_guard_deputy_asd_10`** Ito: “Let me hear it.”

    - “I found his glove at the scene of the murder covered in dried blood and a witness that says the glove is Ogea's. Ogea…” *(if hand over 1× [Suspect's glove](../items/ogea_glove.md))* → [brv_guard_deputy_asd_20](#d-brv_guard_deputy_asd_20)

    <span id="d-brv_guard_deputy_asd_20"></span>**`brv_guard_deputy_asd_20`** Ito: “Wow. You did a great job! Do you want a job on our team?” — **effects:** sets stage 60 of [brv_nondisplay_multipurpose (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-60)

    - “No, thanks. I just want Ogea punished.” → [brv_guard_deputy_asd_30](#d-brv_guard_deputy_asd_30)

    <span id="d-brv_guard_deputy_asd_30"></span>**`brv_guard_deputy_asd_30`** Ito: “That is as good as done.” — **effects:** sets stage 220 of [A strange looking dagger](../quests/brv_dagger.md#stage-220), removes monsters from brimhaven4, spawns monsters on brimhaven_prison

    - “Thanks.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added<br>Dialogue: 4 lines added |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 2 lines changed<br>· text: “That is as good as done” → “That is as good as done.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_guard_deputy.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_guard_deputy.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_guard_deputy.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_guard_deputy.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `brv_guard_deputy` |
    | Spawn group | `brv_guard_deputy` |
    | Loot table | – |
    | Conversation | `brv_guard_deputy_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:109` |
    | Defined in | `res/raw/monsterlist_brimhaven_2.json` |

    Raw data:

    ```json
    {
     "id": "brv_guard_deputy",
     "name": "Ito",
     "iconID": "monsters_ld1:109",
     "monsterClass": "humanoid",
     "spawnGroup": "brv_guard_deputy",
     "phraseID": "brv_guard_deputy_10"
    }
    ```


<small>Data from v0.8.18</small>
