# ![](../assets/icons/monsters/monsters_karvis2_0.png){ .sprite } Prim cook

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

- [blackwater_mountain21](../maps/blackwater_mountain21.md)

## Quests

- [Well rested](../quests/prim_innquest.md): stages 10, 50

??? quote "Dialogue (15 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-prim_cook_start"></span>**`prim_cook_start`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 50 of [Well rested](../quests/prim_innquest.md#stage-50))* → [prim_cook_return_1](#d-prim_cook_return_1)
    - branch 2 *(if reached stage 10 of [Well rested](../quests/prim_innquest.md#stage-10))* → [prim_cook_return_2](#d-prim_cook_return_2)
    - branch 3 → [prim_cook_1](#d-prim_cook_1)

    <span id="d-prim_cook_return_1"></span>**`prim_cook_return_1`** Prim cook: “Thank you for your help earlier. I hope the back room is comfortable enough.”

    - Next → [prim_cook_return_7](#d-prim_cook_return_7)

    <span id="d-prim_cook_return_2"></span>**`prim_cook_return_2`** Prim cook: “Did you talk to Arghest?”

    - “No, not yet.” → [prim_cook_return_3](#d-prim_cook_return_3)
    - “[Lie] Yes, he told me that I could rest in the back room if I want to.” → [prim_cook_return_4](#d-prim_cook_return_4)
    - “Yes, he gave me permission to use the back room whenever I wish.” *(if reached stage 40 of [Well rested](../quests/prim_innquest.md#stage-40))* → [prim_cook_return_6](#d-prim_cook_return_6)

    <span id="d-prim_cook_1"></span>**`prim_cook_1`** Prim cook: “Can I help you?”

    - “What food do you have available for trade?” → [prim_cook_2](#d-prim_cook_2)
    - “Is the back room available for rent?” → [prim_cook_3](#d-prim_cook_3)

    <span id="d-prim_cook_return_7"></span>**`prim_cook_return_7`** Prim cook: “You are welcome to rest in the back room any time you want. Please let me know if there is anything I can do to help.”


    <span id="d-prim_cook_return_3"></span>**`prim_cook_return_3`** Prim cook: “Return to me once you know if he is still interested in renting the back room or not.”

    - “Any idea where he might be?” → [prim_cook_6](#d-prim_cook_6)

    <span id="d-prim_cook_return_4"></span>**`prim_cook_return_4`** Prim cook: “Did he really say that? Somehow I doubt that. It doesn't sound like him.”

    - Next → [prim_cook_return_5](#d-prim_cook_return_5)

    <span id="d-prim_cook_return_6"></span>**`prim_cook_return_6`** Prim cook: “Really, he did? Well then, go ahead. I'm just glad the back room is being used.” — **effects:** sets stage 50 of [Well rested](../quests/prim_innquest.md#stage-50)

    - Next → [prim_cook_return_7](#d-prim_cook_return_7)

    <span id="d-prim_cook_2"></span>**`prim_cook_2`** Prim cook: “Food? No, sorry. I don't have anything to trade.”

    - Next → [prim_cook_1](#d-prim_cook_1)

    <span id="d-prim_cook_3"></span>**`prim_cook_3`** Prim cook: “Rent? Hmm. No, not at the moment.”

    - Next → [prim_cook_41](#d-prim_cook_41)

    <span id="d-prim_cook_6"></span>**`prim_cook_6`** Prim cook: “I don't know where he is now, but I do know that he used to be part of the mining effort in our mine to the southwest.” — **effects:** sets stage 10 of [Well rested](../quests/prim_innquest.md#stage-10)

    - “Thanks. I will go look for him.” → *conversation ends*
    - “I will go look for him right away.” → *conversation ends*

    <span id="d-prim_cook_return_5"></span>**`prim_cook_return_5`** Prim cook: “You will have to do something more to convince me.”


    <span id="d-prim_cook_41"></span>**`prim_cook_41`** Prim cook: “It is still rented out to Arghest. He would not be very happy if I rented it out to someone else when he expects to use it.”

    - Next → [prim_cook_5](#d-prim_cook_5)

    <span id="d-prim_cook_5"></span>**`prim_cook_5`** Prim cook: “Now that you mention it, he hasn't been around here for quite some time. Maybe you could go talk to him and see if he still wants to rent it?”

    - “OK, I will go talk to him.” → [prim_cook_7](#d-prim_cook_7)
    - “Sure. Any idea where he might be?” → [prim_cook_6](#d-prim_cook_6)

    <span id="d-prim_cook_7"></span>**`prim_cook_7`** Prim cook: “Thanks.”

    - Next → [prim_cook_6](#d-prim_cook_6)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 4 lines changed<br>· text: “Rent? Hm. No, not at the moment.” → “Rent? Hmm. No, not at the moment.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_cook.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_cook.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_cook.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_cook.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `prim_cook` · Data from v0.8.18</small>
