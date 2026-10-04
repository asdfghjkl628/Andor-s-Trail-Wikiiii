# ![](../assets/icons/monsters/monsters_gisons_8.png){ .sprite } Lethgar slave ghost

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_gisons_8.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `lethgar_female_ghost` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | undertell_1_1 |
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

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [undertell_1_1](../maps/undertell_1_1.md) | – | 1 | – |


## Quests

- [hidden_undertell (hidden flag)](../quests/undertell_hidden.md): stages 80, 82

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Lethgar slave ghost. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/lethgar_female_ghost_selector.json" data-npc="Lethgar slave ghost" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (14 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-lethgar_female_ghost_selector"></span>**`lethgar_female_ghost_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 80 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-80))* → [lethgar_female_ghost_default](#d-lethgar_female_ghost_default)
    - branch 2 → [lethgar_female_ghost_welcome_10](#d-lethgar_female_ghost_welcome_10)

    <span id="d-lethgar_female_ghost_default"></span>**`lethgar_female_ghost_default`** Lethgar slave ghost: “Oh, a real live human here? I don't believe it.”

    - Next → [lethgar_female_ghost_pinch_10](#d-lethgar_female_ghost_pinch_10)

    <span id="d-lethgar_female_ghost_welcome_10"></span>**`lethgar_female_ghost_welcome_10`** Lethgar slave ghost: “What brings you to me now?”

    - “Can I rest here?” *(if NOT reached stage 450 of [hidden_devotion (hidden flag)](../quests/hidden_devotion.md#stage-450); reached stage 81 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-81))* → [lethgar_female_ghost_rest_no](#d-lethgar_female_ghost_rest_no)
    - “I would really like to rest here now.” *(if reached stage 450 of [hidden_devotion (hidden flag)](../quests/hidden_devotion.md#stage-450); reached stage 81 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-81))* → [lethgar_female_ghost_rest_yes](#d-lethgar_female_ghost_rest_yes)
    - “Are you a Lethgar?” *(if reached stage 85 of [No rest for the wicked](../quests/Stanwickquest.md#stage-85))* → [lethgar_female_ghost_lethgar_10](#d-lethgar_female_ghost_lethgar_10)
    - “Nothing right now. Thanks anyway.” → *conversation ends*

    <span id="d-lethgar_female_ghost_pinch_10"></span>**`lethgar_female_ghost_pinch_10`** Lethgar slave ghost: “She reaches out and pinches your arm to confirm that you are in fact human.” — **effects:** sets stage 80 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-80)

    - “Ouch!” → [lethgar_female_ghost_welcome_10](#d-lethgar_female_ghost_welcome_10)

    <span id="d-lethgar_female_ghost_rest_no"></span>**`lethgar_female_ghost_rest_no`** Lethgar slave ghost: “No, I'm sorry, but you don't need to rest here. You need to experience this place more before you decide whether or not you want to get cozy with a dark pillow.”

    - “What is that supposed to mean?” → [lethgar_female_ghost_rest_no_explain](#d-lethgar_female_ghost_rest_no_explain)

    <span id="d-lethgar_female_ghost_rest_yes"></span>**`lethgar_female_ghost_rest_yes`** Lethgar slave ghost: “The Kha'zaan are no more, thanks to you. So yes, you are free to sleep in any of the desirable beds.” — **effects:** sets stage 82 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-82)

    - “Finally! Thank you.” → *conversation ends*

    <span id="d-lethgar_female_ghost_lethgar_10"></span>**`lethgar_female_ghost_lethgar_10`** Lethgar slave ghost: “I am. Born Lethgar, died Lethgar, and it seems I am doomed to remain so long after any of it mattered.”

    - “I have seen a statue near Brightport that bears the Lethgar name. Do you know of it?” → [lethgar_female_ghost_lethgar_20](#d-lethgar_female_ghost_lethgar_20)

    <span id="d-lethgar_female_ghost_rest_no_explain"></span>**`lethgar_female_ghost_rest_no_explain`** Lethgar slave ghost: “For your protection, you can not rest in our beds...right now anyway.”

    - “So I can later? If so, when is 'later'?” → [lethgar_female_ghost_rest_no_explain_more](#d-lethgar_female_ghost_rest_no_explain_more)

    <span id="d-lethgar_female_ghost_lethgar_20"></span>**`lethgar_female_ghost_lethgar_20`** Lethgar slave ghost: “Near Brightport? Child, my people never reached that far north. We were here, beneath this mountain. We built, we dug, we died. The northern lands were not ours to know.”

    - “Then why would a statue carry your people's name up there?” → [lethgar_female_ghost_lethgar_30](#d-lethgar_female_ghost_lethgar_30)

    <span id="d-lethgar_female_ghost_rest_no_explain_more"></span>**`lethgar_female_ghost_rest_no_explain_more`** Lethgar slave ghost: “When you have a better understanding of this place.”


    <span id="d-lethgar_female_ghost_lethgar_30"></span>**`lethgar_female_ghost_lethgar_30`** Lethgar slave ghost: “I cannot say with any certainty.”

    - Next → [lethgar_female_ghost_lethgar_40](#d-lethgar_female_ghost_lethgar_40)

    <span id="d-lethgar_female_ghost_lethgar_40"></span>**`lethgar_female_ghost_lethgar_40`** Lethgar slave ghost: “But the Kazaul were never above reshaping the truth to suit their purposes. They renamed places, rewrote histories, left their marks upon things that were never theirs. A statue bearing our name in a land we never walked...that is not…”

    - “You think the Kazaul put it there to mislead people?” → [lethgar_female_ghost_lethgar_50](#d-lethgar_female_ghost_lethgar_50)

    <span id="d-lethgar_female_ghost_lethgar_50"></span>**`lethgar_female_ghost_lethgar_50`** Lethgar slave ghost: “I think the Kazaul are ancient, patient, and very skilled at making the living doubt what stands before them. A name here, a stone there. Given enough time, even a carefully placed lie begins to look like history.”

    - “That is a troubling thought.” → [lethgar_female_ghost_lethgar_60](#d-lethgar_female_ghost_lethgar_60)

    <span id="d-lethgar_female_ghost_lethgar_60"></span>**`lethgar_female_ghost_lethgar_60`** Lethgar slave ghost: “Good. You should be troubled. It means you have not yet stopped thinking for yourself. Now, was there something else you needed?”

    - “Can I rest here?” *(if NOT reached stage 450 of [hidden_devotion (hidden flag)](../quests/hidden_devotion.md#stage-450); reached stage 81 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-81))* → [lethgar_female_ghost_rest_no](#d-lethgar_female_ghost_rest_no)
    - “I would really like to rest here now.” *(if reached stage 450 of [hidden_devotion (hidden flag)](../quests/hidden_devotion.md#stage-450); reached stage 81 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-81))* → [lethgar_female_ghost_rest_yes](#d-lethgar_female_ghost_rest_yes)
    - “Nothing else. Thank you.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 14 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lethgar_female_ghost.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lethgar_female_ghost.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lethgar_female_ghost.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lethgar_female_ghost.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `lethgar_female_ghost` |
    | Spawn group | `lethgar_female_ghost` |
    | Loot table | – |
    | Conversation | `lethgar_female_ghost_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_gisons:8` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "lethgar_female_ghost",
     "name": "Lethgar slave ghost",
     "iconID": "monsters_gisons:8",
     "monsterClass": "humanoid",
     "phraseID": "lethgar_female_ghost_selector"
    }
    ```


<small>Data from v0.8.18</small>
