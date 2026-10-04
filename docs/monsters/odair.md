# ![](../assets/icons/monsters/monsters_men_8.png){ .sprite } Odair

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

- [crossglen](../maps/crossglen.md)

## Quests

- [Rat infestation](../quests/odair.md): stages 10, 100

??? quote "Dialogue (10 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-odair1"></span>**`odair1`** Odair: “Oh, it's you. You with that brother of yours. Always causing trouble.”

    - Next → [odair_select](#d-odair_select)

    <span id="d-odair_select"></span>**`odair_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 100 of [Rat infestation](../quests/odair.md#stage-100))* → [odair_complete2](#d-odair_complete2)
    - branch 2 *(if reached stage 10 of [Rat infestation](../quests/odair.md#stage-10))* → [odair_continue](#d-odair_continue)
    - branch 3 → [odair2](#d-odair2)

    <span id="d-odair_complete2"></span>**`odair_complete2`** Odair: “Thanks a lot for your help earlier. Now we might start using that cave as our old supply cave again.”

    - “Bye.” → *conversation ends*

    <span id="d-odair_continue"></span>**`odair_continue`** Odair: “Did you kill that large rat in the cave west of here?”

    - “Yes, I have killed the large rat.” *(if hand over 1× [Cave rat tail](../items/tail_caverat.md))* → [odair_complete](#d-odair_complete)
    - “What was I supposed to do again?” → [odair5](#d-odair5)
    - “No, not yet.” → [odair_cowards](#d-odair_cowards)

    <span id="d-odair2"></span>**`odair2`** Odair: “Hmm, maybe you could be of use to me. Do you think you could help me with a small task?”

    - “Tell me more about this task.” → [odair3](#d-odair3)
    - “Sure, if there is anything I can gain from it.” → [odair3](#d-odair3)

    <span id="d-odair_complete"></span>**`odair_complete`** Odair: “Thanks a lot for your help kid! Maybe you and that brother of yours aren't as cowardly as I thought. Here, take these coins for your help.” — **effects:** sets stage 100 of [Rat infestation](../quests/odair.md#stage-100), gives [Gold coins](../items/gold.md)

    - “Thanks.” → *conversation ends*

    <span id="d-odair5"></span>**`odair5`** Odair: “I need you to get into that cave and kill the large rat, that way maybe we can stop the rat infestation in the cave and start using it as our old supply cave again.” — **effects:** sets stage 10 of [Rat infestation](../quests/odair.md#stage-10)

    - “OK.” → *conversation ends*
    - “On second thought, I don't think I will help you after all.” → [odair_cowards](#d-odair_cowards)

    <span id="d-odair_cowards"></span>**`odair_cowards`** Odair: “I didn't think so either. You and that brother of yours always were cowards.”

    - “Bye.” → *conversation ends*

    <span id="d-odair3"></span>**`odair3`** Odair: “I recently went in to that cave over there [points west], to check on our supplies. But apparently, the cave has been infested with rats.”

    - Next → [odair4](#d-odair4)

    <span id="d-odair4"></span>**`odair4`** Odair: “In particular, I saw one rat that was larger than the other rats. Do you think you have what it takes to help eliminate them?”

    - “Sure, I'll help you so that Crossglen can use the supply cave again.” → [odair5](#d-odair5)
    - “Sure, I'll help you. But only because there might be some gain for me in this.” → [odair5](#d-odair5)
    - “No thanks.” → [odair_cowards](#d-odair_cowards)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 7 lines changed<br>· text: “I recently went in to that cave over there *points west*, to check on…” → “I recently went in to that cave over there [points west], to check on…” |
| [v0.7.10](../versions/0.7.10.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=odair.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=odair.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=odair.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=odair.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `odair` · Data from v0.8.18</small>
