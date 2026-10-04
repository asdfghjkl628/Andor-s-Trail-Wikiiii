# ![](../assets/icons/monsters/monsters_ld1_42.png){ .sprite } Orion, the centaur

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

- [island1](../maps/island1.md)

## Quests

- [Not Pony Island](../quests/lae_centaurs.md): stages 10
- [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md): stages 211

??? quote "Dialogue (13 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-lae_centaur1"></span>**`lae_centaur1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 30 of [Not Pony Island](../quests/lae_centaurs.md#stage-30))* → [lae_centaur](#d-lae_centaur)
    - branch 2 *(if reached stage 211 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-211))* → [lae_centaur1_20](#d-lae_centaur1_20)
    - branch 3 → [lae_centaur1_1](#d-lae_centaur1_1)

    <span id="d-lae_centaur"></span>**`lae_centaur`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 300 of [Not Pony Island](../quests/lae_centaurs.md#stage-300))* → [lae_centaur8](#d-lae_centaur8)
    - branch 2 *(if reached stage 30 of [Not Pony Island](../quests/lae_centaurs.md#stage-30))* → [lae_centaur_20](#d-lae_centaur_20)
    - branch 3 → [lae_centaur_10](#d-lae_centaur_10)

    <span id="d-lae_centaur1_20"></span>**`lae_centaur1_20`** Orion, the centaur: “You are not wanted here.”


    <span id="d-lae_centaur1_1"></span>**`lae_centaur1_1`** Orion, the centaur: “You there, human.”

    - “What do you want?” → [lae_centaur1_2](#d-lae_centaur1_2)

    <span id="d-lae_centaur8"></span>**`lae_centaur8`** Orion, the centaur: “The stars are bright tonight.”


    <span id="d-lae_centaur_20"></span>**`lae_centaur_20`** Orion, the centaur: “We have an eye on you.”


    <span id="d-lae_centaur_10"></span>**`lae_centaur_10`** Orion, the centaur: “You are not wanted here.”


    <span id="d-lae_centaur1_2"></span>**`lae_centaur1_2`** Orion, the centaur: “Our leader wants to see you. Now.”

    - “Why?” → [lae_centaur1_3](#d-lae_centaur1_3)
    - “Who is your leader?” → [lae_centaur1_3](#d-lae_centaur1_3)

    <span id="d-lae_centaur1_3"></span>**`lae_centaur1_3`** Orion, the centaur: “Don't ask questions. Just do as you're told.”

    - “Fine. Lead the way.” → [lae_centaur1_5](#d-lae_centaur1_5)
    - “And if I refuse?” → [lae_centaur1_4](#d-lae_centaur1_4)

    <span id="d-lae_centaur1_5"></span>**`lae_centaur1_5`** Orion, the centaur: “I have better things to do than play tour guide to useless intruders.”

    - “Then just tell me where he is.” → [lae_centaur1_8](#d-lae_centaur1_8)

    <span id="d-lae_centaur1_4"></span>**`lae_centaur1_4`** Orion, the centaur: “Then you'll regret it. Trust me, you don't want to anger our leader.”

    - “It's okay, calm down. Where is this leader?” → [lae_centaur1_8](#d-lae_centaur1_8)

    <span id="d-lae_centaur1_8"></span>**`lae_centaur1_8`** Orion, the centaur: “Thalos, our wise guide, is currently in the northeast of the island.” — **effects:** sets stage 10 of [Not Pony Island](../quests/lae_centaurs.md#stage-10), sets stage 211 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-211)

    - “Fine, I'll go see him.” → [lae_centaur1_10](#d-lae_centaur1_10)
    - “Hopefully this Thalos will be a little more accommodating.” → [lae_centaur1_10](#d-lae_centaur1_10)

    <span id="d-lae_centaur1_10"></span>**`lae_centaur1_10`** Orion, the centaur: “Hurry up now. And don't try anything stupid.”




## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 13 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_centaur1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_centaur1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_centaur1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_centaur1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `lae_centaur1` · Data from v0.8.18</small>
