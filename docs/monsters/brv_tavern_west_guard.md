# ![](../assets/icons/monsters/monsters_rltiles1_69.png){ .sprite } Guard

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

- [brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)

## Quests

- [Fair play?](../quests/brv_blackjack.md): stages 10, 40, 60
- [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md): stages 150

??? quote "Dialogue (8 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brv_tavern_west_guard_select"></span>**`brv_tavern_west_guard_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 60 of [Fair play?](../quests/brv_blackjack.md#stage-60))* → [brv_tavern_west_guard_100](#d-brv_tavern_west_guard_100)
    - branch 2 *(if reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50); killed 1× [Dealer](../monsters/brv_blackjack_dealer_evil.md); killed 1× [Gambler](../monsters/brv_blackjack_gambler1_evil.md); killed 1× [Gambler](../monsters/brv_blackjack_gambler1_evil.md))* → [brv_tavern_west_guard_90](#d-brv_tavern_west_guard_90)
    - branch 3 *(if reached stage 40 of [Fair play?](../quests/brv_blackjack.md#stage-40))* → [brv_tavern_west_guard_20](#d-brv_tavern_west_guard_20)
    - branch 4 → [brv_tavern_west_backroom_5](#d-brv_tavern_west_backroom_5)

    <span id="d-brv_tavern_west_guard_100"></span>**`brv_tavern_west_guard_100`** [Guard](../monsters/brv_tavern_west_guard.md): “You are not welcome anymore.”

    - “Sure I am. I'm on official Alkapoan business.” *(if latest stage of [A place to forge](../quests/place_to_forge.md#stage-40) is 40)* → [brv_tavern_west_guard_alkapaon_business_10](#d-brv_tavern_west_guard_alkapaon_business_10)
    - “Ah, right. I forgot.” → *conversation ends*

    <span id="d-brv_tavern_west_guard_90"></span>**`brv_tavern_west_guard_90`** [Guard](../monsters/brv_tavern_west_guard.md): “I heard you fighting in there. Lucky for you that no one got killed. You are not welcome anymore.” — **effects:** sets stage 60 of [Fair play?](../quests/brv_blackjack.md#stage-60), clears stage 150 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-150)

    - “Sure I am. I'm on official Alkapoan business.” *(if latest stage of [A place to forge](../quests/place_to_forge.md#stage-40) is 40)* → [brv_tavern_west_guard_alkapaon_business_10](#d-brv_tavern_west_guard_alkapaon_business_10)
    - “Calm down! I'm leaving right now.” → *conversation ends*

    <span id="d-brv_tavern_west_guard_20"></span>**`brv_tavern_west_guard_20`** Guard: “I wish you good luck. [Laughs]” — **effects:** sets stage 150 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-150), sets stage 40 of [Fair play?](../quests/brv_blackjack.md#stage-40)


    <span id="d-brv_tavern_west_backroom_5"></span>**`brv_tavern_west_backroom_5`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 20 of [Fair play?](../quests/brv_blackjack.md#stage-20))* → [brv_tavern_west_guard_10](#d-brv_tavern_west_guard_10)
    - branch 2 → [brv_tavern_west_backroom_6](#d-brv_tavern_west_backroom_6)

    <span id="d-brv_tavern_west_guard_alkapaon_business_10"></span>**`brv_tavern_west_guard_alkapaon_business_10`** Guard: “Oh, sorry. Please don't tell Alkapoan that I hassled you.” — **effects:** sets stage 150 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-150), spawns monsters on brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back

    - “Now that's the attitude I like to see.” → *conversation ends*

    <span id="d-brv_tavern_west_guard_10"></span>**`brv_tavern_west_guard_10`** [Guard](../monsters/brv_tavern_west_guard.md): “[You hear noises from the back room...] Stop! Tell me the password, if you want to enter.” — **effects:** sets stage 10 of [Fair play?](../quests/brv_blackjack.md#stage-10)

    - “I don't know the password.” → *conversation ends*
    - “[Tell him the password]” *(if reached stage 30 of [Fair play?](../quests/brv_blackjack.md#stage-30))* → [brv_tavern_west_guard_20](#d-brv_tavern_west_guard_20)

    <span id="d-brv_tavern_west_backroom_6"></span>**`brv_tavern_west_backroom_6`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 10 of [Fair play?](../quests/brv_blackjack.md#stage-10)

    - branch 1 → [brv_tavern_west_guard_10](#d-brv_tavern_west_guard_10)



## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 7 lines added |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line added, 2 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_tavern_west_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_tavern_west_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_tavern_west_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_tavern_west_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `brv_tavern_west_guard` · Data from v0.8.18</small>
