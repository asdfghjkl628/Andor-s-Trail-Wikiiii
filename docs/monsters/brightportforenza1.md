# ![](../assets/icons/monsters/monsters_ld1_206.png){ .sprite } Florencia

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

- [brightport_forenza](../maps/brightport_forenza.md)

## Quests

- [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md): stages 183, 242, 254

??? quote "Dialogue (7 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightport_florencia_selector"></span>**`brightport_florencia_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 115 of [The odd coin collector](../quests/odd_coin_collector.md#stage-115); NOT reached stage 183 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-183))* → [brightport_florencia0](#d-brightport_florencia0)
    - Next *(if reached stage 183 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-183))* → [brightport_florencia2](#d-brightport_florencia2)
    - Next *(if NOT reached stage 183 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-183))* → [brightport_florencia](#d-brightport_florencia)

    <span id="d-brightport_florencia0"></span>**`brightport_florencia0`** Florencia: “Hello, $playername! I received a letter from my father, Forenza, about how much you helped him on his travel.”

    - Next → [brightport_florencia3](#d-brightport_florencia3)

    <span id="d-brightport_florencia2"></span>**`brightport_florencia2`** Florencia: “Hello $playername, you're always welcome to come here and rest.”

    - “What is that vault there for.” → [brightport_florencia6](#d-brightport_florencia6)

    <span id="d-brightport_florencia"></span>**`brightport_florencia`** Florencia: “Hello. I don't believe we know each other.”

    - “That is an interesting vault you have there, what is it for?” → [brightport_florencia6](#d-brightport_florencia6)

    <span id="d-brightport_florencia3"></span>**`brightport_florencia3`** Florencia: “Please feel free to rest at our house any time you're in Brightport. The couch is over there, against the far wall.” — **effects:** sets stage 183 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-183)


    <span id="d-brightport_florencia6"></span>**`brightport_florencia6`** Florencia: “My husband, who is the bakery's accountant, keeps most of his paperwork there. But it was my father who made it to store his coin collection.” — **effects:** sets stage 242 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-242)

    - “Your father?” → [brightport_florencia7](#d-brightport_florencia7)
    - “I see, bye.” → *conversation ends*

    <span id="d-brightport_florencia7"></span>**`brightport_florencia7`** Florencia: “My father Forenza... I wish he would come visit us more often. What is he doing traveling alone at his age?” — **effects:** sets stage 254 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-254)

    - “I should get going.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 7 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportforenza1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportforenza1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportforenza1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportforenza1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `brightportforenza1` · Data from v0.8.18</small>
