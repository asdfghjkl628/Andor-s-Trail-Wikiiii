# ![](../assets/icons/monsters/monsters_ld1_146.png){ .sprite } Egrinda

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 255 |
| Max AP | 12 |
| Attack cost | 2 |
| Move cost | 3 |
| Damage | 8 to 16 |
| Attack chance | 270 |
| Block chance | 130 |
| Damage resistance | 19 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## On hit

- **On target:** Baited strike (magnitude 4, 2 rounds, 50% chance)

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 1 |
| [Oaken staff](../items/oaken_staff.md) | 100% | 1 |

## Found on

- [way_to_sullengard_west_3](../maps/way_to_sullengard_west_3.md)

## Quests

- [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md): stages 61

??? quote "Dialogue (13 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-egrinda_selector"></span>**`egrinda_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 61 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-61))* → [egrinda_already_given_gold_10](#d-egrinda_already_given_gold_10)
    - branch 2 → [egrinda_wants_gold_10](#d-egrinda_wants_gold_10)

    <span id="d-egrinda_already_given_gold_10"></span>**`egrinda_already_given_gold_10`** Egrinda: “This gold will really help me rebuild my life. Now I just need to decide where to do that.”

    - “May I suggest Feygard?” → [egrinda_already_given_gold_20](#d-egrinda_already_given_gold_20)
    - “May I suggest Nor City?” → [egrinda_already_given_gold_15](#d-egrinda_already_given_gold_15)

    <span id="d-egrinda_wants_gold_10"></span>**`egrinda_wants_gold_10`** Egrinda: “That gold you're holding... it belonged to my family. Stolen from us not long ago, taken by hands no better than yours.”

    - Next → [egrinda_wants_gold_narrator_1](#d-egrinda_wants_gold_narrator_1)

    <span id="d-egrinda_already_given_gold_20"></span>**`egrinda_already_given_gold_20`** Egrinda: “Feygard? Why would I ever want to live there?”

    - “Well, I've heard such wonderful things about that glorious city. There's so many opportunities for almost anyone.” → [egrinda_already_given_gold_30](#d-egrinda_already_given_gold_30)

    <span id="d-egrinda_already_given_gold_15"></span>**`egrinda_already_given_gold_15`** Egrinda: “Nor City? Why would I ever want to live there?”

    - “I'm really not sure why except that I've met so many Shadow folk that rave about that place.” → [egrinda_already_given_gold_25](#d-egrinda_already_given_gold_25)

    <span id="d-egrinda_wants_gold_narrator_1"></span>**`egrinda_wants_gold_narrator_1`** [Dummy NPC](../monsters/none.md): “She takes a cautious step forward.”

    - Next → [egrinda_wants_gold_20](#d-egrinda_wants_gold_20)

    <span id="d-egrinda_already_given_gold_30"></span>**`egrinda_already_given_gold_30`** Egrinda: “Feygard? I don't know, maybe. But thank you for your suggestion.”

    - “Good luck!” → *conversation ends*

    <span id="d-egrinda_already_given_gold_25"></span>**`egrinda_already_given_gold_25`** Egrinda: “Nor City? I don't know, maybe. But thank you for your suggestion.”

    - “Good luck!” → *conversation ends*

    <span id="d-egrinda_wants_gold_20"></span>**`egrinda_wants_gold_20`** [Egrinda](../monsters/egrinda.md): “You can do right and give it back. Or you can learn what happens to those who carry what's not theirs.”

    - “If it's truly yours, then take it. [Hand over the recently looted gold.]” *(if pay 10,000 gold)* → [egrinda_wants_gold_reward_qs61](#d-egrinda_wants_gold_reward_qs61)
    - “Oh, you mean that gold that now belongs to me? It's now mine.” → [egrinda_wants_gold_fight](#d-egrinda_wants_gold_fight)
    - “[Lie] Oh, you mean the 500 gold pieces that I found back there? [Pointing west.]” → [egrinda_wants_gold_lier](#d-egrinda_wants_gold_lier)

    <span id="d-egrinda_wants_gold_reward_qs61"></span>**`egrinda_wants_gold_reward_qs61`** Egrinda: “Thank you very much!” — **effects:** sets stage 61 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-61)

    - Next → [egrinda_already_given_gold_10](#d-egrinda_already_given_gold_10)

    <span id="d-egrinda_wants_gold_fight"></span>**`egrinda_wants_gold_fight`** [Dummy NPC](../monsters/none.md): “Egrinda lunges at you.” — **effects:** faction “egrinda” set to -1

    - “You will not survive this!” → [egrinda_fight](#d-egrinda_fight)

    <span id="d-egrinda_wants_gold_lier"></span>**`egrinda_wants_gold_lier`** Egrinda: “Liar!”

    - Next → [egrinda_wants_gold_fight](#d-egrinda_wants_gold_fight)

    <span id="d-egrinda_fight"></span>**`egrinda_fight`** *(silent check: the first matching branch below is taken)*

    - branch 1 → *fight starts*



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=egrinda.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=egrinda.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=egrinda.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=egrinda.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `egrinda` · Data from v0.8.18</small>
