# ![](../assets/icons/monsters/monsters_ld1_162.png){ .sprite } Waitress

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
| [Cooked meat](../items/meat_cooked.md) | 100% | 10 |
| [Cooked chicken leg](../items/chkn_leg.md) | 100% | 8 |
| [Brimhaven brew](../items/brv_brew.md) | 100% | 10 |
| [Mead](../items/mead.md) | 100% | 5 |
| [Duck eggs](../items/eggs_duck.md) | 100% | 1 to 3 |
| [Boiled tripe](../items/tripe_boiled.md) | 100% | 1 to 5 |

## Found on

- [brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)

??? quote "Dialogue (6 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brv_tavern_west_waitress_select"></span>**`brv_tavern_west_waitress_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50))* → [brv_tavern_west_waitress_100](#d-brv_tavern_west_waitress_100)
    - branch 2 → [brv_tavern_west_waitress_10](#d-brv_tavern_west_waitress_10)

    <span id="d-brv_tavern_west_waitress_100"></span>**`brv_tavern_west_waitress_100`** Waitress: “Please go away. I don't want you here in my tavern anymore.”


    <span id="d-brv_tavern_west_waitress_10"></span>**`brv_tavern_west_waitress_10`** Waitress: “Welcome to my tavern. How can I help you?”

    - “Do you know something about the back room?” *(if reached stage 10 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-10))* → [brv_tavern_west_waitress_20](#d-brv_tavern_west_waitress_20)
    - “What do you offer for trade?” → *shop opens*
    - “I am looking for my brother, Andor. He looks a bit like me.” → [brv_tavern_west_waitress_11](#d-brv_tavern_west_waitress_11)

    <span id="d-brv_tavern_west_waitress_20"></span>**`brv_tavern_west_waitress_20`** Waitress: “Keep your fingers out of things that are none of your business.”


    <span id="d-brv_tavern_west_waitress_11"></span>**`brv_tavern_west_waitress_11`** Waitress: “Let me think...”

    - Next → [brv_tavern_west_waitress_11b](#d-brv_tavern_west_waitress_11b)

    <span id="d-brv_tavern_west_waitress_11b"></span>**`brv_tavern_west_waitress_11b`** Waitress: “No, I am sorry.”

    - Next → [brv_tavern_west_waitress_10](#d-brv_tavern_west_waitress_10)



## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 6 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_tavern_west_waitress.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_tavern_west_waitress.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_tavern_west_waitress.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_tavern_west_waitress.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `brv_tavern_west_waitress` · Data from v0.8.18</small>
