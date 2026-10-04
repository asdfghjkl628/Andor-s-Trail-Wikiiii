# ![](../assets/icons/monsters/monsters_ld1_195.png){ .sprite } Delon

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_195.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `brightportnpc10` |
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
| [brightport_bakery1](../maps/brightport_bakery1.md) | Brightport | 1 | – |


## Quests

- [Bread and circus](../quests/brightport_bakery.md): stages 5, 10, 16, 20

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Delon. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_delon_selector.json" data-npc="Delon" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (20 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightport_delon_selector"></span>**`brightport_delon_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 20 of [Bread and circus](../quests/brightport_bakery.md#stage-20))* → [brightport_delon18](#d-brightport_delon18)
    - Next *(if reached stage 16 of [Bread and circus](../quests/brightport_bakery.md#stage-16); NOT reached stage 20 of [Bread and circus](../quests/brightport_bakery.md#stage-20))* → [brightport_delon14](#d-brightport_delon14)
    - Next *(if reached stage 162 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-162); reached stage 163 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-163); reached stage 164 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-164))* → [brightport_delon12](#d-brightport_delon12)
    - Next *(if reached stage 207 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-207))* → [brightport_delon11](#d-brightport_delon11)
    - Next *(if NOT reached stage 207 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-207); reached stage 206 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-206))* → [brightport_delon10](#d-brightport_delon10)
    - Next *(if reached stage 195 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-195); NOT reached stage 206 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-206))* → [brightport_delon9](#d-brightport_delon9)
    - Next *(if reached stage 5 of [Bread and circus](../quests/brightport_bakery.md#stage-5); NOT reached stage 195 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-195))* → [brightport_delon6](#d-brightport_delon6)
    - Next → [brightport_delon0](#d-brightport_delon0)

    <span id="d-brightport_delon18"></span>**`brightport_delon18`** Delon: “Yawn... Your job's over, go away.”


    <span id="d-brightport_delon14"></span>**`brightport_delon14`** Delon: “Yawn. Is the flour sifted yet?”

    - “As white as powdered snow.” *(if reached stage 168 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-168))* → [brightport_delon15](#d-brightport_delon15)
    - “Not yet.” → *conversation ends*

    <span id="d-brightport_delon12"></span>**`brightport_delon12`** Delon: “Zzzz. Pastries... Zzzz...”

    - “Oh, so that's why you've been so quiet.” → [brightport_delon13](#d-brightport_delon13)

    <span id="d-brightport_delon11"></span>**`brightport_delon11`** Delon: “Mmm, yeah, sweep over there...”


    <span id="d-brightport_delon10"></span>**`brightport_delon10`** Delon: “You did a good job sweeping that part of the warehouse. With my help, of course. Now finish the rest.”


    <span id="d-brightport_delon9"></span>**`brightport_delon9`** Delon: “You have a broom, what are you doing here instead of sweeping?”

    - “I'm on it.” → *conversation ends*

    <span id="d-brightport_delon6"></span>**`brightport_delon6`** Delon: “Yes my underling, how is the sweeping going.”

    - “I haven't even started.” → [brightport_delon7](#d-brightport_delon7)

    <span id="d-brightport_delon0"></span>**`brightport_delon0`** Delon: “What do you want? Can't you see I'm busy resti... I mean, working.”

    - “What do you do here?” → [brightport_delon1](#d-brightport_delon1)
    - “Allares hired me for today, he told me to see you.” *(if reached stage 1 of [Bread and circus](../quests/brightport_bakery.md#stage-1); NOT reached stage 5 of [Bread and circus](../quests/brightport_bakery.md#stage-5))* → [brightport_delon3](#d-brightport_delon3)

    <span id="d-brightport_delon15"></span>**`brightport_delon15`** Delon: “Good work $playername. Now what should I have you do next...”

    - Next → [brightport_delon16](#d-brightport_delon16)

    <span id="d-brightport_delon13"></span>**`brightport_delon13`** Delon: “Zzz... Huh? Er... Wha, what?”

    - “I finally finished sweeping the whole warehouse!” → [brightport_delon8](#d-brightport_delon8)

    <span id="d-brightport_delon7"></span>**`brightport_delon7`** Delon: “Well, then go and do it.”


    <span id="d-brightport_delon1"></span>**`brightport_delon1`** Delon: “Me? Well it might look like I'm just laying around in the warehouse, but I've got a secret, and I'm only gonna tell you this. One day I'll open my own bakery in Nor City, ten times better than here.”

    - “There's no harm in dreaming” → [brightport_delon2](#d-brightport_delon2)

    <span id="d-brightport_delon3"></span>**`brightport_delon3`** Delon: “Allares, my assistant, he did well acquiring me an underling. Hmm... Now what work should I have you do?”

    - “Huh aren't we working together?” → [brightport_delon4](#d-brightport_delon4)

    <span id="d-brightport_delon16"></span>**`brightport_delon16`** Delon: “Hmm, I think that was all of it. I would make you peel apples but I don't see any fresh apples from the orchard around, which is odd because they were supposed to be delivered already.”

    - “Can you tell me more about it?” → [brightport_delon17](#d-brightport_delon17)

    <span id="d-brightport_delon8"></span>**`brightport_delon8`** Delon: “[Yawning] See that sack of flour over there? Go sift through it so there's no rat dung inside or anything.” — **effects:** sets stage 16 of [Bread and circus](../quests/brightport_bakery.md#stage-16)

    - “More work?” → *conversation ends*

    <span id="d-brightport_delon2"></span>**`brightport_delon2`** Delon: “Like bread I rest, and great I rise.”


    <span id="d-brightport_delon4"></span>**`brightport_delon4`** Delon: “What?! Of course not. I'm the supervisor, you're the worker. Now go sweep the floor so I can see what you're capable of.” — **effects:** sets stage 5 of [Bread and circus](../quests/brightport_bakery.md#stage-5)

    - “Fine. And what am I supposed to use to sweep the floor? Do you have a broom?” → [brightport_delon5](#d-brightport_delon5)

    <span id="d-brightport_delon17"></span>**`brightport_delon17`** Delon: “No I can't, that's not my job. Go ask Allares if you want to know more. Now, I'm glad you're finally getting off my back. I don't want you interrupting my important work.” — **effects:** sets stage 20 of [Bread and circus](../quests/brightport_bakery.md#stage-20)

    - “Sure, whatever you say sleepyhead.” → *conversation ends*

    <span id="d-brightport_delon5"></span>**`brightport_delon5`** Delon: “Hmm. We might have had something like that, but I'm not sure. You can go and buy a new one.” — **effects:** sets stage 10 of [Bread and circus](../quests/brightport_bakery.md#stage-10)




## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 20 lines added |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed<br>· text: “Hmm, I think that was all of it. I would make you peel apples but I d…” → “Hmm, I think that was all of it. I would make you peel apples but I d…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc10.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc10.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc10.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc10.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `brightportnpc10` |
    | Spawn group | `brightportnpc10` |
    | Loot table | – |
    | Conversation | `brightport_delon_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:195` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportnpc10",
     "name": "Delon",
     "iconID": "monsters_ld1:195",
     "phraseID": "brightport_delon_selector"
    }
    ```


<small>Data from v0.8.18</small>
