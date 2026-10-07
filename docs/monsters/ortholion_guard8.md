# ![](../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite } Dying general's henchman

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `ortholion_guard8` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | elm_mine5 |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

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
| [elm_mine5](../maps/elm_mine5.md) | – | 1 | – |


## Quests

- [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md): stages 31, 32

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Dying general's henchman. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/ortholion_guard8.json" data-npc="Dying general&#x27;s henchman" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (6 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ortholion_guard8"></span>**`ortholion_guard8`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if 1 rounds passed since timer “elm5_corpse”)* → [ortholion_guard8_consumed](#d-ortholion_guard8_consumed)
    - branch 2 *(if reached stage 32 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-32))* → [ortholion_guard8_dead](#d-ortholion_guard8_dead)
    - branch 3 → [ortholion_guard8_1](#d-ortholion_guard8_1)

    <span id="d-ortholion_guard8_consumed"></span>**`ortholion_guard8_consumed`** [Dummy NPC](../monsters/none.md): “Of the soldier you met inside here, only dust remains.” — **effects:** removes monsters from elm_mine5


    <span id="d-ortholion_guard8_dead"></span>**`ortholion_guard8_dead`** [Dummy NPC](../monsters/none.md): “On the top of the stairs lies a dead soldier. He is no longer breathing.”

    - “Leave.” → *conversation ends*
    - “Plunder.” *(if NOT reached stage 31 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-31))* → [ortholion_guard8_plunder](#d-ortholion_guard8_plunder)

    <span id="d-ortholion_guard8_1"></span>**`ortholion_guard8_1`** Dying general's henchman: “Wh... *cough* ...at the heck?! *cough*, *cough*, *cough* Kid, go away. This thing... *cough*, *cough*... GO AWAY!”

    - “What's wrong?” → [ortholion_guard8_2](#d-ortholion_guard8_2)
    - “Whatever, I'll go down anyway.” → [ortholion_guard8_2](#d-ortholion_guard8_2)

    <span id="d-ortholion_guard8_plunder"></span>**`ortholion_guard8_plunder`** Dying general's henchman: “You try to pull off the armor first but you soon discover both the man and the armor itself are covered by that glowing ore. You instantly stop grabbing it. The glowing ore is somehow growing.” — **effects:** sets stage 31 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-31), starts timer “elm5_corpse”


    <span id="d-ortholion_guard8_2"></span>**`ortholion_guard8_2`** Dying general's henchman: “*ignoring you*... You idiot kid... *cough*. It's a trap, THE WHOLE THING *cough*, *cough* is... ...This mine is... cur...” — **effects:** sets stage 32 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-32)

    - Next → [ortholion_guard8_dead](#d-ortholion_guard8_dead)



## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added<br>Dialogue: 6 lines added |
| [v0.8.4](../versions/0.8.4.md) | Dialogue: 1 line changed<br>· text: “You try to put off the armor first but you soon discover both the man…” → “You try to pull off the armor first but you soon discover both the ma…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard8.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard8.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard8.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard8.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `ortholion_guard8` |
    | Spawn group | `ortholion_guard8` |
    | Loot table | – |
    | Conversation | `ortholion_guard8` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles3:14` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "ortholion_guard8",
     "name": "Dying general's henchman",
     "iconID": "monsters_rltiles3:14",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "ortholion_guard8"
    }
    ```


<small>Data from v0.8.18</small>
