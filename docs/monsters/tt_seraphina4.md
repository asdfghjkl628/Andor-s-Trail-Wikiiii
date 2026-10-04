# ![](../assets/icons/monsters/monsters_tometik7_38.png){ .sprite } Sly Seraphina

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

- [crackshot_hideout4](../maps/crackshot_hideout4.md)

## Quests

- [Troubling times](../quests/troubling_times.md): stages 250, 252
- [troubling_times_nd (hidden flag)](../quests/troubling_times_nd.md): stages 30

??? quote "Dialogue (10 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-tt_sly4"></span>**`tt_sly4`** Sly Seraphina: “It's good to ... see you are alive, kid.” — **effects:** faction “tt_sly_attack3” +999

    - “You look terrible.” *(if NOT reached stage 250 of [Troubling times](../quests/troubling_times.md#stage-250))* → [tt_sly4_2](#d-tt_sly4_2)
    - “You are severely wounded.” *(if NOT reached stage 250 of [Troubling times](../quests/troubling_times.md#stage-250))* → [tt_sly4_10](#d-tt_sly4_10)
    - “You look better now.” *(if reached stage 250 of [Troubling times](../quests/troubling_times.md#stage-250))* → [tt_sly4_4](#d-tt_sly4_4)
    - “Hey, I'm back. Don't be alarmed, I'll squeeze past you.” *(if NOT reached stage 30 of [troubling_times_nd (hidden flag)](../quests/troubling_times_nd.md#stage-30))* → [tt_sly4_6](#d-tt_sly4_6)

    <span id="d-tt_sly4_2"></span>**`tt_sly4_2`** [Sly Seraphina](../monsters/tt_seraphina4.md): “Nice compliment, kid. Ooouw ...”

    - “You are severely wounded.” → [tt_sly4_10](#d-tt_sly4_10)

    <span id="d-tt_sly4_10"></span>**`tt_sly4_10`** Sly Seraphina: “Give me some healing potion ... please ...”

    - “Here, have a minor vial of health.” *(if hand over 1× [Minor vial of health](../items/health_minor.md))* → [tt_sly4_12](#d-tt_sly4_12)
    - “Here, have a minor vial of health.” *(if hand over 1× [Minor potion of health](../items/health_minor2.md))* → [tt_sly4_12](#d-tt_sly4_12)
    - “Here, have a potion of health.” *(if hand over 1× [Regular potion of health](../items/health.md))* → [tt_sly4_20](#d-tt_sly4_20)
    - “Here, have a major potion of health.” *(if hand over 1× [Major potion of health](../items/health_major2.md))* → [tt_sly4_20](#d-tt_sly4_20)
    - “Here, have a major flask of health.” *(if hand over 1× [Major flask of health](../items/health_major.md))* → [tt_sly4_20](#d-tt_sly4_20)
    - “Here, have a bonemeal potion.” *(if hand over 1× [Bonemeal potion](../items/bonemeal_potion.md))* → [tt_sly4_20](#d-tt_sly4_20)
    - “Here, have a bonemeal potion from Lodar.” *(if hand over 1× [Lodar's bonemeal potion](../items/pot_bm_lodar.md))* → [tt_sly4_20](#d-tt_sly4_20)
    - “Here, have this nice potion. [give her a poison potion]” *(if NOT reached stage 252 of [Troubling times](../quests/troubling_times.md#stage-252); hand over 1× [Weak poison](../items/pot_poison_weak.md))* → [tt_sly4_22](#d-tt_sly4_22)

    <span id="d-tt_sly4_4"></span>**`tt_sly4_4`** Sly Seraphina: “Yes, thanks to you. Just give me a few seconds ...”


    <span id="d-tt_sly4_6"></span>**`tt_sly4_6`** *(silent check: the first matching branch below is taken)* — **effects:** moves you to [crackshot_hideout4](../maps/crackshot_hideout4.md), sets stage 30 of [troubling_times_nd (hidden flag)](../quests/troubling_times_nd.md#stage-30)


    <span id="d-tt_sly4_12"></span>**`tt_sly4_12`** Sly Seraphina: “That didn't work. My wounds are too deep.”

    - “Oh dear, wait, I'll get something different.” → [tt_sly4_10](#d-tt_sly4_10)

    <span id="d-tt_sly4_20"></span>**`tt_sly4_20`** Sly Seraphina: “Ahh, that's good. Thank you, kid ... $playername.” — **effects:** sets stage 250 of [Troubling times](../quests/troubling_times.md#stage-250)

    - “[Embarrassed] Sure thing.” → [tt_sly4_30](#d-tt_sly4_30)

    <span id="d-tt_sly4_22"></span>**`tt_sly4_22`** Sly Seraphina: “[Spits] What is this stuff?! Throw it away before you drink it yourself. It's rotten.” — **effects:** sets stage 252 of [Troubling times](../quests/troubling_times.md#stage-252)

    - “So - sorry.” → [tt_sly4_24](#d-tt_sly4_24)

    <span id="d-tt_sly4_30"></span>**`tt_sly4_30`** Sly Seraphina: “Now don't just stand around here. Look lively and find Luthor's ring.”

    - “Ah, you're back to your old self already.” → *conversation ends*

    <span id="d-tt_sly4_24"></span>**`tt_sly4_24`** [Dummy NPC](../monsters/none.md): “You hope that she doesn't notice your guilty conscience.”

    - “You are tough.” → [tt_sly4_2](#d-tt_sly4_2)



## Version history

| Version | Change |
|---|---|
| [v0.8.13](../versions/0.8.13.md) | Added<br>Dialogue: 10 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tt_seraphina4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tt_seraphina4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tt_seraphina4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tt_seraphina4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `tt_seraphina4` · Data from v0.8.18</small>
