# ![](../assets/icons/monsters/monsters_rogue1_0.png){ .sprite } Gruil

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

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Iron dagger](../items/dagger0.md) | 100% | 1 |
| [Weathered shirt](../items/shirt_weathered.md) | 100% | 1 |
| [Crude combat ring](../items/ring_crude_combat.md) | 100% | 1 |
| [Bar brawler's ring](../items/ring_barbrawler.md) | 100% | 1 |
| [Glass gem](../items/gem1.md) | 100% | 5 |
| [Ruby gem](../items/gem2.md) | 100% | 5 |
| [Polished gem](../items/gem3.md) | 100% | 5 |

## Quests

- [Search for Andor](../quests/andor.md): stages 20, 30

??? quote "Dialogue (8 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-gruil1"></span>**`gruil1`** Gruil: “Psst, hey. Wanna trade?”

    - “Sure, let's trade.” → *shop opens*
    - “I heard that you talked to my brother a while ago.” *(if reached stage 10 of [Search for Andor](../quests/andor.md#stage-10))* → [gruil_select](#d-gruil_select)

    <span id="d-gruil_select"></span>**`gruil_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 30 of [Search for Andor](../quests/andor.md#stage-30))* → [gruil_return](#d-gruil_return)
    - branch 2 → [gruil2](#d-gruil2)

    <span id="d-gruil_return"></span>**`gruil_return`** Gruil: “Look kid, I already told you.”

    - Next → [gruil_andor1](#d-gruil_andor1)

    <span id="d-gruil2"></span>**`gruil2`** Gruil: “Your brother? Oh you mean Andor? I might know something, but that information will cost you. Bring me a poison gland from one of those poisonous snakes and maybe I'll tell you.” — **effects:** sets stage 20 of [Search for Andor](../quests/andor.md#stage-20)

    - “Here, I have a poison gland for you.” *(if hand over 1× [Poison gland](../items/gland.md))* → [gruil_complete](#d-gruil_complete)
    - “OK, I'll bring one.” → *conversation ends*

    <span id="d-gruil_andor1"></span>**`gruil_andor1`** Gruil: “I talked to him yesterday. He asked if I knew someone called Umar or something like that. I have no idea who he was talking about.”

    - Next → [gruil_andor2](#d-gruil_andor2)

    <span id="d-gruil_complete"></span>**`gruil_complete`** Gruil: “Thanks a lot kid. This will do just fine.” — **effects:** sets stage 30 of [Search for Andor](../quests/andor.md#stage-30)

    - Next → [gruil_andor1](#d-gruil_andor1)

    <span id="d-gruil_andor2"></span>**`gruil_andor2`** Gruil: “He seemed really upset about something and left in a hurry. Something about the Thieves' Guild in Fallhaven.”

    - Next → [gruil_andor3](#d-gruil_andor3)

    <span id="d-gruil_andor3"></span>**`gruil_andor3`** Gruil: “That's all I know. Maybe you should ask around in Fallhaven. Look for my friend Gaela, he probably knows more.”

    - “Thanks, bye.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 3 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gruil.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gruil.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gruil.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gruil.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `gruil` · Data from v0.8.18</small>
