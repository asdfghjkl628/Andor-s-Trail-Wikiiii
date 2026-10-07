# ![](../assets/icons/monsters/monsters_newb_1_653.png){ .sprite } Elytharan cooker slave

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_1_653.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `elytharan_cook_slave` |
| **Type** | NPC |
| **Class** | Ghost |
| **HP** | 1 |
| **Found in** | undertell_1_1 |
| **Immune to crits** | Yes |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

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

!!! note "Immune to critical hits"
    Ghosts, constructs and demons can't be critically hit. Your crit build will have to sit this one out.

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [undertell_1_1](../maps/undertell_1_1.md) | – | 1 | – |


## Quests

- [Undertell: What was not written](../quests/undertell_book.md): stages 60, 80

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Elytharan cooker slave. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/elytharan_cooker_slave_default.json" data-npc="Elytharan cooker slave" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-elytharan_cooker_slave_default"></span>**`elytharan_cooker_slave_default`** Elytharan cooker slave: “Tell those ingrates over in the other room that their dinner is almost ready!”

    - “[Lie] Sure, I'll do that right now.” → *conversation ends*
    - “What still needs to be done?” → [elytharan_cooker_intro](#d-elytharan_cooker_intro)

    <span id="d-elytharan_cooker_intro"></span>**`elytharan_cooker_intro`** Elytharan cooker slave: “The fire must be watched. The pots must not boil dry. When the bell rings, the bowls are filled.”

    - “I see, but...” *(if reached stage 50 of [Undertell: What was not written](../quests/undertell_book.md#stage-50); reached stage 60 of [Undertell: What was not written](../quests/undertell_book.md#stage-60); reached stage 70 of [Undertell: What was not written](../quests/undertell_book.md#stage-70); NOT reached stage 80 of [Undertell: What was not written](../quests/undertell_book.md#stage-80))* → [elytharan_cooker_reward_qs80](#d-elytharan_cooker_reward_qs80)
    - “Who do you cook for?” *(if reached stage 40 of [Undertell: What was not written](../quests/undertell_book.md#stage-40); NOT reached stage 60 of [Undertell: What was not written](../quests/undertell_book.md#stage-60))* → [elytharan_cooker_loop_60](#d-elytharan_cooker_loop_60)
    - “Do you remember Elythara?” *(if reached stage 40 of [Undertell: What was not written](../quests/undertell_book.md#stage-40); NOT reached stage 60 of [Undertell: What was not written](../quests/undertell_book.md#stage-60))* → [elytharan_cooker_loop_60](#d-elytharan_cooker_loop_60)
    - “I should go.” → [elytharan_cooker_end](#d-elytharan_cooker_end)

    <span id="d-elytharan_cooker_reward_qs80"></span>**`elytharan_cooker_reward_qs80`** Elytharan cooker slave: “When the bell rings, the bowls are filled.” — **effects:** sets stage 80 of [Undertell: What was not written](../quests/undertell_book.md#stage-80)


    <span id="d-elytharan_cooker_loop_60"></span>**`elytharan_cooker_loop_60`** Elytharan cooker slave: “Those who work, eat. Those who eat return to work. The bell decides.” — **effects:** sets stage 60 of [Undertell: What was not written](../quests/undertell_book.md#stage-60)

    - “I see, but...” *(if reached stage 50 of [Undertell: What was not written](../quests/undertell_book.md#stage-50); reached stage 60 of [Undertell: What was not written](../quests/undertell_book.md#stage-60); reached stage 70 of [Undertell: What was not written](../quests/undertell_book.md#stage-70); NOT reached stage 80 of [Undertell: What was not written](../quests/undertell_book.md#stage-80))* → [elytharan_cooker_reward_qs80](#d-elytharan_cooker_reward_qs80)
    - “I see.” → [elytharan_cooker_end](#d-elytharan_cooker_end)

    <span id="d-elytharan_cooker_end"></span>**`elytharan_cooker_end`** Elytharan cooker slave: “When the bell rings, the bowls are filled.”




## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elytharan_cook_slave.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elytharan_cook_slave.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elytharan_cook_slave.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elytharan_cook_slave.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `elytharan_cook_slave` |
    | Spawn group | `elytharan_cook_slave` |
    | Loot table | – |
    | Conversation | `elytharan_cooker_slave_default` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_newb_1:653` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "elytharan_cook_slave",
     "name": "Elytharan cooker slave",
     "iconID": "monsters_newb_1:653",
     "monsterClass": "ghost",
     "horizontalFlipChance": 50,
     "phraseID": "elytharan_cooker_slave_default"
    }
    ```


<small>Data from v0.8.18</small>
