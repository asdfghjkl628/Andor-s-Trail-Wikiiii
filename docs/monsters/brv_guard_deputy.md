# ![](../assets/icons/monsters/monsters_ld1_109.png){ .sprite } Ito

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

- [brimhaven2](../maps/brimhaven2.md)

## Quests

- [A strange looking dagger](../quests/brv_dagger.md): stages 220
- [brv_nondisplay_multipurpose (hidden flag)](../quests/brv_nondisplay_multipurpose.md): stages 60

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


<small>Monster ID: `brv_guard_deputy` · Data from v0.8.18</small>
