# ![](../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite } Dying general's henchman

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

- [elm_mine5](../maps/elm_mine5.md)

## Quests

- [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md): stages 31, 32

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


<small>Monster ID: `ortholion_guard8` · Data from v0.8.18</small>
