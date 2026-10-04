# ![](../assets/icons/monsters/monsters_ld1_42.png){ .sprite } Silvanus, the centaur

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

- [island3](../maps/island3.md)

## Quests

- [Not Pony Island](../quests/lae_centaurs.md): stages 10
- [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md): stages 213

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Silvanus, the centaur. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_centaur3.json" data-npc="Silvanus, the centaur" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (12 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-lae_centaur3"></span>**`lae_centaur3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 30 of [Not Pony Island](../quests/lae_centaurs.md#stage-30))* → [lae_centaur](#d-lae_centaur)
    - branch 2 *(if reached stage 213 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-213))* → [lae_centaur3_10](#d-lae_centaur3_10)
    - branch 3 → [lae_centaur3_1](#d-lae_centaur3_1)

    <span id="d-lae_centaur"></span>**`lae_centaur`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 300 of [Not Pony Island](../quests/lae_centaurs.md#stage-300))* → [lae_centaur8](#d-lae_centaur8)
    - branch 2 *(if reached stage 30 of [Not Pony Island](../quests/lae_centaurs.md#stage-30))* → [lae_centaur_20](#d-lae_centaur_20)
    - branch 3 → [lae_centaur_10](#d-lae_centaur_10)

    <span id="d-lae_centaur3_10"></span>**`lae_centaur3_10`** Silvanus, the centaur: “Go talk to Thalos. Although I'd rather you just disappear altogether.”


    <span id="d-lae_centaur3_1"></span>**`lae_centaur3_1`** Silvanus, the centaur: “What do you want, human?”

    - “Just passing through. No need to be hostile.” → [lae_centaur3_2](#d-lae_centaur3_2)

    <span id="d-lae_centaur8"></span>**`lae_centaur8`** Silvanus, the centaur: “The stars are bright tonight.”


    <span id="d-lae_centaur_20"></span>**`lae_centaur_20`** Silvanus, the centaur: “We have an eye on you.”


    <span id="d-lae_centaur_10"></span>**`lae_centaur_10`** Silvanus, the centaur: “You are not wanted here.”


    <span id="d-lae_centaur3_2"></span>**`lae_centaur3_2`** Silvanus, the centaur: “We don't take kindly to your kind here. You humans always cause trouble.”

    - “I'm not looking for trouble. Just trying to explore.” → [lae_centaur3_3](#d-lae_centaur3_3)
    - “I'm just looking for...” → [lae_centaur3_3](#d-lae_centaur3_3)

    <span id="d-lae_centaur3_3"></span>**`lae_centaur3_3`** Silvanus, the centaur: “Well, you're not welcome here. Keep moving before you cause any problems.”

    - “I don't mean any harm. Can't we just talk?” → [lae_centaur3_4](#d-lae_centaur3_4)

    <span id="d-lae_centaur3_4"></span>**`lae_centaur3_4`** Silvanus, the centaur: “Talking won't change anything. You humans are all the same. You should have just left us alone.”

    - “Fine. I'll go. But I won't forget how unwelcoming you've been.” → [lae_centaur3_5](#d-lae_centaur3_5)
    - “Enough now. I want to speak to your boss.” → [lae_centaur3_8](#d-lae_centaur3_8)

    <span id="d-lae_centaur3_5"></span>**`lae_centaur3_5`** Silvanus, the centaur: “We don't care what you think. Just leave our island and never come back.”


    <span id="d-lae_centaur3_8"></span>**`lae_centaur3_8`** Silvanus, the centaur: “Thalos, our wise guide, is currently in the northeast of the island.” — **effects:** sets stage 10 of [Not Pony Island](../quests/lae_centaurs.md#stage-10), sets stage 213 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-213)

    - “Fine, I'll go see him.” → [lae_centaur3_10](#d-lae_centaur3_10)
    - “Hopefully this Thalos will be a little more accommodating.” → [lae_centaur3_10](#d-lae_centaur3_10)



## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 12 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_centaur3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_centaur3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_centaur3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_centaur3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `lae_centaur3` · Data from v0.8.18</small>
