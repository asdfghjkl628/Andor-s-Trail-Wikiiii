# ![](../assets/icons/monsters/monsters_rltiles1_75.png){ .sprite } Laeroth prisoner

| Stat | Value |
|---|---|
| Class | undead |
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

## Quests

- [Shadow of the torturer](../quests/lae_torturer.md): stages 5, 10, 20, 80, 130

??? quote "Dialogue (13 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-lae_prison_01"></span>**`lae_prison_01`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 25 of [Shadow of the torturer](../quests/lae_torturer.md#stage-25))* → [lae_prison_end](#d-lae_prison_end)
    - branch 2 *(if reached stage 31 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-31); reached stage 33 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-33); reached stage 34 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-34))* → [lae_prison_02](#d-lae_prison_02)
    - branch 3 → [lae_prison_01a](#d-lae_prison_01a)

    <span id="d-lae_prison_end"></span>**`lae_prison_end`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if killed 1× [Kotheses](../monsters/kotheses.md); NOT reached stage 80 of [Shadow of the torturer](../quests/lae_torturer.md#stage-80))* → [lae_prison_end_10](#d-lae_prison_end_10)
    - branch 2 *(if killed 1× [Kotheses](../monsters/kotheses.md))* → [lae_prison_end_20](#d-lae_prison_end_20)
    - branch 3 *(if reached stage 114 of [Shadow of the torturer](../quests/lae_torturer.md#stage-114); NOT reached stage 130 of [Shadow of the torturer](../quests/lae_torturer.md#stage-130))* → [lae_prison_end_30](#d-lae_prison_end_30)
    - branch 4 *(if reached stage 25 of [Shadow of the torturer](../quests/lae_torturer.md#stage-25); NOT killed 1× [Kotheses](../monsters/kotheses.md))* → [lae_prison_3a](#d-lae_prison_3a)

    <span id="d-lae_prison_02"></span>**`lae_prison_02`** Laeroth prisoner: “Please, can you help us?”

    - “What sort of help?” → [lae_prison_02a](#d-lae_prison_02a)

    <span id="d-lae_prison_01a"></span>**`lae_prison_01a`** Laeroth prisoner: “Please, can you help us?”

    - “What sort of help?” → [lae_prison_01b](#d-lae_prison_01b)

    <span id="d-lae_prison_end_10"></span>**`lae_prison_end_10`** [Laeroth prisoner](../monsters/lae_prisoner.md): “Oh, the kid is back. Just look!”

    - “You can finally find peace. Kotheses, the torturer is dead.” → [lae_prison_end_20](#d-lae_prison_end_20)

    <span id="d-lae_prison_end_20"></span>**`lae_prison_end_20`** [Laeroth prisoner](../monsters/lae_prisoner.md): “Ooooh! We are eternally grateful!” — **effects:** sets stage 80 of [Shadow of the torturer](../quests/lae_torturer.md#stage-80)


    <span id="d-lae_prison_end_30"></span>**`lae_prison_end_30`** Laeroth prisoner: “Everything is in order now. The prisoners are back in their cells, and the Demon guards are on duty again.” — **effects:** sets stage 130 of [Shadow of the torturer](../quests/lae_torturer.md#stage-130)

    - Next → [lae_prison_3a](#d-lae_prison_3a)

    <span id="d-lae_prison_3a"></span>**`lae_prison_3a`** [Laeroth prisoner](../monsters/lae_prisoner.md): “Ohhh! What will become of us?” — **effects:** sets stage 20 of [Shadow of the torturer](../quests/lae_torturer.md#stage-20)


    <span id="d-lae_prison_02a"></span>**`lae_prison_02a`** Laeroth prisoner: “The prison torturer died, but he took the life force of us prisoners in the hope to live again.”

    - Next → [lae_prison_02b](#d-lae_prison_02b)

    <span id="d-lae_prison_01b"></span>**`lae_prison_01b`** Laeroth prisoner: “Please open the other cells and free us all! Hurry! Then come back to me.”

    - “OK, just a second ...” → *conversation ends*

    <span id="d-lae_prison_02b"></span>**`lae_prison_02b`** Laeroth prisoner: “It didn't work, because we had so little life left anyway.” — **effects:** sets stage 5 of [Shadow of the torturer](../quests/lae_torturer.md#stage-5), changes map laerothprison4

    - Next → [lae_prison_02c](#d-lae_prison_02c)

    <span id="d-lae_prison_02c"></span>**`lae_prison_02c`** Laeroth prisoner: “But now we cannot rest in peace, because he is still here, somewhere in the lower caves. He needs to be destroyed, but we cannot do it because he has control over us.”

    - “OK. I'll do it. I am not afraid of a few monsters!” *(if NOT reached stage 20 of [Shadow of the torturer](../quests/lae_torturer.md#stage-20))* → [lae_prison_03](#d-lae_prison_03)
    - “No thanks. Seems dangerous, and there's nothing in it for me.” *(if NOT reached stage 10 of [Shadow of the torturer](../quests/lae_torturer.md#stage-10))* → [lae_prison_3a](#d-lae_prison_3a)

    <span id="d-lae_prison_03"></span>**`lae_prison_03`** Laeroth prisoner: “Thank you! But beware! He has guards that are like him. They may appear to be human at first glance, but they are not!” — **effects:** sets stage 10 of [Shadow of the torturer](../quests/lae_torturer.md#stage-10)




## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 13 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_prisoner4a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_prisoner4a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_prisoner4a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_prisoner4a.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `lae_prisoner4a` · Data from v0.8.18</small>
