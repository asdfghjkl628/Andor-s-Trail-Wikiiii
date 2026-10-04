# ![](../assets/icons/monsters/monsters_rltiles1_84.png){ .sprite } Prim evoker

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 0 |
| Max AP | 10 |
| Attack cost | 10 |
| Move cost | 10 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Found on

- [blackwater_mountain11](../maps/blackwater_mountain11.md)

## Quests

- [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md): stages 10

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Prim evoker. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/prim_commoner4.json" data-npc="Prim evoker" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (8 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-prim_commoner4"></span>**`prim_commoner4`** Prim evoker: “Hello. Who are you? Are you here to help us?”

    - “I am looking for my brother. Would you by any chance have happened to see him around here?” → [prim_commoner4_1](#d-prim_commoner4_1)
    - “Yes, I have come to help your village.” → [prim_commoner4_3](#d-prim_commoner4_3)
    - “[Lie] Yes, I have come to help your village.” → [prim_commoner4_3](#d-prim_commoner4_3)
    - “What do you know about Lorn's accident?” *(if reached stage 20 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-20); NOT reached stage 21 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-21))* → [prim_commoner4_4](#d-prim_commoner4_4)

    <span id="d-prim_commoner4_1"></span>**`prim_commoner4_1`** Prim evoker: “Your brother? Son, you should know that we do not get many visitors around here.”

    - Next → [prim_commoner4_2](#d-prim_commoner4_2)

    <span id="d-prim_commoner4_3"></span>**`prim_commoner4_3`** Prim evoker: “Oh thank you. We could really use some help around here.”


    <span id="d-prim_commoner4_4"></span>**`prim_commoner4_4`** Prim evoker: “Lorn? Nothing. I barely know him, or his comrades, Duala and...sorry, I forget the name. What's wrong with him?”

    - “He was killed several days ago.” → [prim_commoner4_5a](#d-prim_commoner4_5a)
    - “He had an accident while climbing down the mountain.” → [prim_commoner4_5b](#d-prim_commoner4_5b)

    <span id="d-prim_commoner4_2"></span>**`prim_commoner4_2`** Prim evoker: “So, no. I cannot help you.”


    <span id="d-prim_commoner4_5a"></span>**`prim_commoner4_5a`** Prim evoker: “Oh. I'm sorry. May the Shadow guide his way to a better world.”

    - “Right, uhm...don't you remember anything about him?” → [prim_commoner4_6](#d-prim_commoner4_6)

    <span id="d-prim_commoner4_5b"></span>**`prim_commoner4_5b`** Prim evoker: “Yes, that's why climbing up the mountain is forbidden now.”

    - “Anything more?” → [prim_commoner4_6](#d-prim_commoner4_6)

    <span id="d-prim_commoner4_6"></span>**`prim_commoner4_6`** Prim evoker: “Uhm, well. I heard Lorn was popular among the children here in Prim because of his scary stories about, you know, the monsters.” — **effects:** sets stage 10 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-10)

    - “Gonna ask some child. Thanks.” → *conversation ends*
    - “My father probably told me scarier stories. Bye.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed |
| [v0.7.14](../versions/0.7.14.md) | Dialogue: 4 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_evoker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_evoker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_evoker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_evoker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `prim_evoker` · Data from v0.8.18</small>
