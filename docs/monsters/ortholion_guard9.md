# ![](../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite } Ortholion's henchman

| Stat | Value |
|---|---|
| Class | ? |
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

- [elm_3f](../maps/elm_3f.md)

## Quests

- [Climbing up is forbidden](../quests/Omi2_bwm1.md): stages 50
- [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md): stages 34, 35

??? quote "Dialogue (16 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ortholion_guard9_s"></span>**`ortholion_guard9_s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 35 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-35))* → [ortholion_guard9_11](#d-ortholion_guard9_11)
    - branch 2 *(if reached stage 50 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-50))* → [ortholion_guard9_10a](#d-ortholion_guard9_10a)
    - branch 3 *(if 6 rounds passed since timer “elm3f_grow”)* → [ortholion_guard9_3](#d-ortholion_guard9_3)
    - branch 4 → [ortholion_guard9_1](#d-ortholion_guard9_1)

    <span id="d-ortholion_guard9_11"></span>**`ortholion_guard9_11`** Ortholion's henchman: “I will leave this place right now and come back with more men anyway! Kids these days...Annoying.” — **effects:** clears stage 34 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-34), sets stage 50 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-50), sets stage 35 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-35)

    - “Goodbye!” → *NPC leaves*
    - “Whatever, I'm leaving.” → *NPC leaves*

    <span id="d-ortholion_guard9_10a"></span>**`ortholion_guard9_10a`** Ortholion's henchman: “I knew I could count on you! This sign of bravery won't be forgotten.” — **effects:** clears stage 34 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-34), sets stage 50 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-50)

    - “See you soon, sir.” → *NPC leaves*
    - “Whatever. Step aside, I'm leading the way!” → *NPC leaves*

    <span id="d-ortholion_guard9_3"></span>**`ortholion_guard9_3`** Ortholion's henchman: “Unbelievable...”

    - “Where's the general?” → [ortholion_guard9_4](#d-ortholion_guard9_4)
    - “Uhm, whatever. I have to go.” → *conversation ends*

    <span id="d-ortholion_guard9_1"></span>**`ortholion_guard9_1`** Ortholion's henchman: “Be quiet.”

    - “What?” → [ortholion_guard9_1](#d-ortholion_guard9_1)
    - “Why?” *(if NOT reached stage 34 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-34))* → [orhtolion_guard9_2](#d-orhtolion_guard9_2)

    <span id="d-ortholion_guard9_4"></span>**`ortholion_guard9_4`** Ortholion's henchman: “General...Oh! That's right. I don't think this is the right way.”

    - Next → [ortholion_guard9_5](#d-ortholion_guard9_5)

    <span id="d-orhtolion_guard9_2"></span>**`orhtolion_guard9_2`** Ortholion's henchman: “Look *points to the large crystals*...It grows.” — **effects:** sets stage 34 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-34), starts timer “elm3f_grow”

    - “[Look]” → *conversation ends*

    <span id="d-ortholion_guard9_5"></span>**`ortholion_guard9_5`** Ortholion's henchman: “This no longer seems to be part of the Elm mine. Look at all these strange creatures... Uh, I'm the only one that has gone this far. My partners must have discovered the right path.”

    - “Half of your partners are dead and the other half are too scared to even go inside the mine.” → [ortholion_guard9_6b](#d-ortholion_guard9_6b)
    - “I haven't seen any other way. This is the right one.” → [ortholion_guard9_6a](#d-ortholion_guard9_6a)

    <span id="d-ortholion_guard9_6b"></span>**`ortholion_guard9_6b`** Ortholion's henchman: “That cannot be... Damn it! I knew those screams were not from these creatures.”

    - “I'm sorry.” → [ortholion_guard9_8c](#d-ortholion_guard9_8c)
    - “Save your breath. We still have a mission, and monsters to slay.” → [ortholion_guard9_8b](#d-ortholion_guard9_8b)
    - “It was their fault.” → [ortholion_guard9_8a](#d-ortholion_guard9_8a)

    <span id="d-ortholion_guard9_6a"></span>**`ortholion_guard9_6a`** Ortholion's henchman: “You sure?”

    - Next → [ortholion_guard9_7](#d-ortholion_guard9_7)

    <span id="d-ortholion_guard9_8c"></span>**`ortholion_guard9_8c`** Ortholion's henchman: “No, It's not your fault. You could have done nothing.”

    - Next → [ortholion_guard9_9](#d-ortholion_guard9_9)

    <span id="d-ortholion_guard9_8b"></span>**`ortholion_guard9_8b`** Ortholion's henchman: “Yes...”

    - Next → [ortholion_guard9_9](#d-ortholion_guard9_9)

    <span id="d-ortholion_guard9_8a"></span>**`ortholion_guard9_8a`** Ortholion's henchman: “But...Ugh, you're dead right. Soliders of Feygard MUST NOT SHRINK FROM DANGER!”

    - “Calm down, please.” → [ortholion_guard9_9](#d-ortholion_guard9_9)
    - “HONOR!!” → [ortholion_guard9_9](#d-ortholion_guard9_9)

    <span id="d-ortholion_guard9_7"></span>**`ortholion_guard9_7`** Ortholion's henchman: “Where are my partners then?”

    - “Dead...Most of them.” → [ortholion_guard9_6b](#d-ortholion_guard9_6b)
    - “They were all consumed by those crystals that you were amazed by.” → [ortholion_guard9_6b](#d-ortholion_guard9_6b)

    <span id="d-ortholion_guard9_9"></span>**`ortholion_guard9_9`** Ortholion's henchman: “OK...You're strong and valiant, but are you reliable enough? I will go all the way back and call for reinforcements. I want you to explore this cavern. If you find something too dangerous, please return to the mine, will you?”

    - “That was my plan until you distracted me.” → [ortholion_guard9_10b](#d-ortholion_guard9_10b)
    - “Anything for the glory of Feygard!” → [ortholion_guard9_10a](#d-ortholion_guard9_10a)
    - “Hmpf, just this time.” → [ortholion_guard9_10a](#d-ortholion_guard9_10a)

    <span id="d-ortholion_guard9_10b"></span>**`ortholion_guard9_10b`** Ortholion's henchman: “Will you help me or not?”

    - “Hmpf, OK.” → [ortholion_guard9_11](#d-ortholion_guard9_11)
    - “Maybe some other time.” → [ortholion_guard9_11](#d-ortholion_guard9_11)



## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added<br>Dialogue: 16 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard9.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard9.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard9.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard9.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `ortholion_guard9` · Data from v0.8.18</small>
