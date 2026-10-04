# ![](../assets/icons/monsters/monsters_newb_1_663.png){ .sprite } Forsaken shade

| Stat | Value |
|---|---|
| Class | ghost |
| HP | 431 |
| Max AP | 10 |
| Attack cost | 5 |
| Move cost | 10 |
| Damage | 5 to 7 |
| Attack chance | 230 |
| Block chance | 250 |
| Damage resistance | 9 |
| Critical skill | 0 |
| Critical multiplier | 0 |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons can't be critically hit. Your crit build will have to sit this one out.

## On hit

- **On target:** Deathtouch (magnitude 1, 3 rounds, 50% chance); Vulnerability (magnitude 6, 2 rounds, 75% chance)

## Found on

- [undertell_3_00](../maps/undertell_3_00.md)

## Quests

- [Devotion](../quests/devotion.md): stages 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420
- [hidden_devotion (hidden flag)](../quests/hidden_devotion.md): stages 20, 140, 170, 200, 230, 260, 290, 320, 350, 380, 410, 440

??? quote "Dialogue (38 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-shade7_selector"></span>**`shade7_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 320 of [hidden_devotion (hidden flag)](../quests/hidden_devotion.md#stage-320))* → [shade_fight](#d-shade_fight)
    - branch 2 *(if reached stage 110 of [Devotion](../quests/devotion.md#stage-110); wearing [Elythara's ring](../items/elythara_ring.md))* → [shade_return_wearing_ring_7](#d-shade_return_wearing_ring_7)
    - branch 3 *(if NOT reached stage 40 of [Devotion](../quests/devotion.md#stage-40))* → [shade7_initial](#d-shade7_initial)
    - branch 4 *(if reached stage 40 of [Devotion](../quests/devotion.md#stage-40); NOT reached stage 60 of [Devotion](../quests/devotion.md#stage-60))* → [shade_retry2](#d-shade_retry2)
    - branch 5 *(if reached stage 60 of [Devotion](../quests/devotion.md#stage-60); NOT reached stage 80 of [Devotion](../quests/devotion.md#stage-80))* → [shade_retry3](#d-shade_retry3)
    - branch 6 → [shade7_initial](#d-shade7_initial)

    <span id="d-shade_fight"></span>**`shade_fight`** Forsaken shade: “Your life ends now, mortal.”

    - “I don't think so!” → *fight starts*

    <span id="d-shade_return_wearing_ring_7"></span>**`shade_return_wearing_ring_7`** Forsaken shade: “You have returned to us.” — **effects:** faction “currentShade” set to 7

    - Next → [shade_dialog_template](#d-shade_dialog_template)

    <span id="d-shade7_initial"></span>**`shade7_initial`** Forsaken shade: “Go away!”

    - “But I want to...” → [shade7_dismiss_10](#d-shade7_dismiss_10)

    <span id="d-shade_retry2"></span>**`shade_retry2`** Forsaken shade: “Go away!”

    - “Wait...” → [shade_retry_dismiss](#d-shade_retry_dismiss)

    <span id="d-shade_retry3"></span>**`shade_retry3`** Forsaken shade: “Go away!”

    - “But...I just want to...” → [shade_retry3_dismiss](#d-shade_retry3_dismiss)

    <span id="d-shade_dialog_template"></span>**`shade_dialog_template`** Forsaken shade: “Ah! You have overcome our safeguards.”

    - “Your time has come to an end.” → [shade_offer_mercy](#d-shade_offer_mercy)

    <span id="d-shade7_dismiss_10"></span>**`shade7_dismiss_10`** [Dummy NPC](../monsters/none.md): “Frost forms midair around the shade. A shattering crack erupts, and you vanish with the falling ice. The next thing you know...”

    - Next → [undertell_shade_teleport_loc_selector](#d-undertell_shade_teleport_loc_selector)

    <span id="d-shade_retry_dismiss"></span>**`shade_retry_dismiss`** [Dummy NPC](../monsters/none.md): “The shade flickers with annoyance. A dull pulse of power washes over you, pushing you from this place once more.”

    - Next → [undertell_shade_teleport_loc_selector](#d-undertell_shade_teleport_loc_selector)

    <span id="d-shade_retry3_dismiss"></span>**`shade_retry3_dismiss`** [Dummy NPC](../monsters/none.md): “The shade shudders in irritation. A wave of cold force swells outward, hurling you from the cavern yet again.”

    - Next → [undertell_shade_teleport_loc_selector](#d-undertell_shade_teleport_loc_selector)

    <span id="d-shade_offer_mercy"></span>**`shade_offer_mercy`** Forsaken shade: “Spare us, and we shall reward you when you get out of here. Are we truly monsters or are those who rule and oppress us the true monsters?”

    - “[Let it go.] You deserve freedom.” *(if faction “currentShade” = 1)* → [shade_freed_1](#d-shade_freed_1)
    - “[Let it go.] You deserve freedom.” *(if faction “currentShade” = 2)* → [shade_freed_2](#d-shade_freed_2)
    - “[Let it go.] You deserve freedom.” *(if faction “currentShade” = 3)* → [shade_freed_3](#d-shade_freed_3)
    - “[Let it go.] You deserve freedom.” *(if faction “currentShade” = 4)* → [shade_freed_4](#d-shade_freed_4)
    - “[Let it go.] You deserve freedom.” *(if faction “currentShade” = 5)* → [shade_freed_5](#d-shade_freed_5)
    - “[Let it go.] You deserve freedom.” *(if faction “currentShade” = 6)* → [shade_freed_6](#d-shade_freed_6)
    - “[Let it go.] You deserve freedom.” *(if faction “currentShade” = 7)* → [shade_freed_7](#d-shade_freed_7)
    - “[Let it go.] You deserve freedom.” *(if faction “currentShade” = 8)* → [shade_freed_8](#d-shade_freed_8)
    - “[Let it go.] You deserve freedom.” *(if faction “currentShade” = 9)* → [shade_freed_9](#d-shade_freed_9)
    - “[Let it go.] You deserve freedom.” *(if faction “currentShade” = 10)* → [shade_freed_10](#d-shade_freed_10)
    - “[Let it go.] You deserve freedom.” *(if faction “currentShade” = 11)* → [shade_freed_11](#d-shade_freed_11)
    - “I know my history. You shall cease to exist.” *(if faction “currentShade” = 1)* → [shade_kill_1](#d-shade_kill_1)
    - “I know my history. You shall cease to exist.” *(if faction “currentShade” = 2)* → [shade_kill_2](#d-shade_kill_2)
    - “I know my history. You shall cease to exist.” *(if faction “currentShade” = 3)* → [shade_kill_3](#d-shade_kill_3)
    - “I know my history. You shall cease to exist.” *(if faction “currentShade” = 4)* → [shade_kill_4](#d-shade_kill_4)
    - “I know my history. You shall cease to exist.” *(if faction “currentShade” = 5)* → [shade_kill_5](#d-shade_kill_5)
    - “I know my history. You shall cease to exist.” *(if faction “currentShade” = 6)* → [shade_kill_6](#d-shade_kill_6)
    - “I know my history. You shall cease to exist.” *(if faction “currentShade” = 7)* → [shade_kill_7](#d-shade_kill_7)
    - “I know my history. You shall cease to exist.” *(if faction “currentShade” = 8)* → [shade_kill_8](#d-shade_kill_8)
    - “I know my history. You shall cease to exist.” *(if faction “currentShade” = 9)* → [shade_kill_9](#d-shade_kill_9)
    - “I know my history. You shall cease to exist.” *(if faction “currentShade” = 10)* → [shade_kill_10](#d-shade_kill_10)
    - “I know my history. You shall cease to exist.” *(if faction “currentShade” = 11)* → [shade_kill_11](#d-shade_kill_11)
    - “Let me think...” → *conversation ends*

    <span id="d-undertell_shade_teleport_loc_selector"></span>**`undertell_shade_teleport_loc_selector`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 20 of [hidden_devotion (hidden flag)](../quests/hidden_devotion.md#stage-20)

    - Next *(if random chance (1/4%))* → [mt_galmore1_h1](#d-mt_galmore1_h1)
    - Next *(if random chance (1/3%))* → [mt_galmore0_h2](#d-mt_galmore0_h2)
    - Next *(if random chance (1/2%))* → [mt_galmore1_h5](#d-mt_galmore1_h5)
    - Next *(if random chance (1/1%))* → [galmore_58](#d-galmore_58)

    <span id="d-shade_freed_1"></span>**`shade_freed_1`** Forsaken shade: “Thank you.” — **effects:** faction “shadeSetFreeCount” +1, sets stage 120 of [Devotion](../quests/devotion.md#stage-120), removes monsters from undertell_3_02


    <span id="d-shade_freed_2"></span>**`shade_freed_2`** Forsaken shade: “Thank you.” — **effects:** faction “shadeSetFreeCount” +1, sets stage 150 of [Devotion](../quests/devotion.md#stage-150), removes monsters from undertell_3_02


    <span id="d-shade_freed_3"></span>**`shade_freed_3`** Forsaken shade: “Thank you.” — **effects:** faction “shadeSetFreeCount” +1, sets stage 180 of [Devotion](../quests/devotion.md#stage-180), removes monsters from undertell_3_12


    <span id="d-shade_freed_4"></span>**`shade_freed_4`** Forsaken shade: “Thank you.” — **effects:** faction “shadeSetFreeCount” +1, sets stage 210 of [Devotion](../quests/devotion.md#stage-210), removes monsters from undertell_3_12


    <span id="d-shade_freed_5"></span>**`shade_freed_5`** Forsaken shade: “Thank you.” — **effects:** faction “shadeSetFreeCount” +1, sets stage 240 of [Devotion](../quests/devotion.md#stage-240), removes monsters from undertell_3_13


    <span id="d-shade_freed_6"></span>**`shade_freed_6`** Forsaken shade: “Thank you.” — **effects:** faction “shadeSetFreeCount” +1, sets stage 270 of [Devotion](../quests/devotion.md#stage-270), removes monsters from undertell_3_11


    <span id="d-shade_freed_7"></span>**`shade_freed_7`** Forsaken shade: “Thank you.” — **effects:** faction “shadeSetFreeCount” +1, sets stage 300 of [Devotion](../quests/devotion.md#stage-300), removes monsters from undertell_3_00


    <span id="d-shade_freed_8"></span>**`shade_freed_8`** Forsaken shade: “Thank you.” — **effects:** faction “shadeSetFreeCount” +1, sets stage 330 of [Devotion](../quests/devotion.md#stage-330), removes monsters from undertell_3_00


    <span id="d-shade_freed_9"></span>**`shade_freed_9`** Forsaken shade: “Thank you.” — **effects:** faction “shadeSetFreeCount” +1, sets stage 360 of [Devotion](../quests/devotion.md#stage-360), removes monsters from undertell_3_00


    <span id="d-shade_freed_10"></span>**`shade_freed_10`** Forsaken shade: “Thank you.” — **effects:** faction “shadeSetFreeCount” +1, sets stage 390 of [Devotion](../quests/devotion.md#stage-390), removes monsters from undertell_3_10


    <span id="d-shade_freed_11"></span>**`shade_freed_11`** Forsaken shade: “Thank you.” — **effects:** faction “shadeSetFreeCount” +1, sets stage 420 of [Devotion](../quests/devotion.md#stage-420), removes monsters from undertell_3_03


    <span id="d-shade_kill_1"></span>**`shade_kill_1`** Forsaken shade: “You shall not live.” — **effects:** sets stage 140 of [hidden_devotion (hidden flag)](../quests/hidden_devotion.md#stage-140)

    - “We will see!” → *fight starts*

    <span id="d-shade_kill_2"></span>**`shade_kill_2`** Forsaken shade: “You shall not live.” — **effects:** sets stage 170 of [hidden_devotion (hidden flag)](../quests/hidden_devotion.md#stage-170)

    - “We will see!” → *fight starts*

    <span id="d-shade_kill_3"></span>**`shade_kill_3`** Forsaken shade: “You shall not live.” — **effects:** sets stage 200 of [hidden_devotion (hidden flag)](../quests/hidden_devotion.md#stage-200)

    - “We will see!” → *fight starts*

    <span id="d-shade_kill_4"></span>**`shade_kill_4`** Forsaken shade: “You shall not live.” — **effects:** sets stage 230 of [hidden_devotion (hidden flag)](../quests/hidden_devotion.md#stage-230)

    - “We will see!” → *fight starts*

    <span id="d-shade_kill_5"></span>**`shade_kill_5`** Forsaken shade: “You shall not live.” — **effects:** sets stage 260 of [hidden_devotion (hidden flag)](../quests/hidden_devotion.md#stage-260)

    - “We will see!” → *fight starts*

    <span id="d-shade_kill_6"></span>**`shade_kill_6`** Forsaken shade: “You shall not live.” — **effects:** sets stage 290 of [hidden_devotion (hidden flag)](../quests/hidden_devotion.md#stage-290)

    - “We will see!” → *fight starts*

    <span id="d-shade_kill_7"></span>**`shade_kill_7`** Forsaken shade: “You shall not live.” — **effects:** sets stage 320 of [hidden_devotion (hidden flag)](../quests/hidden_devotion.md#stage-320)

    - “We will see!” → *fight starts*

    <span id="d-shade_kill_8"></span>**`shade_kill_8`** Forsaken shade: “You shall not live.” — **effects:** sets stage 350 of [hidden_devotion (hidden flag)](../quests/hidden_devotion.md#stage-350)

    - “We will see!” → *fight starts*

    <span id="d-shade_kill_9"></span>**`shade_kill_9`** Forsaken shade: “You shall not live.” — **effects:** sets stage 380 of [hidden_devotion (hidden flag)](../quests/hidden_devotion.md#stage-380)

    - “We will see!” → *fight starts*

    <span id="d-shade_kill_10"></span>**`shade_kill_10`** Forsaken shade: “You shall not live.” — **effects:** sets stage 410 of [hidden_devotion (hidden flag)](../quests/hidden_devotion.md#stage-410)

    - “We will see!” → *fight starts*

    <span id="d-shade_kill_11"></span>**`shade_kill_11`** Forsaken shade: “You shall not live.” — **effects:** sets stage 440 of [hidden_devotion (hidden flag)](../quests/hidden_devotion.md#stage-440)

    - “We will see!” → *fight starts*

    <span id="d-mt_galmore1_h1"></span>**`mt_galmore1_h1`** *(silent check: the first matching branch below is taken)* — **effects:** moves you to [mt_galmore1_h1](../maps/mt_galmore1_h1.md)


    <span id="d-mt_galmore0_h2"></span>**`mt_galmore0_h2`** *(silent check: the first matching branch below is taken)* — **effects:** moves you to [mt_galmore0_h2](../maps/mt_galmore0_h2.md)


    <span id="d-mt_galmore1_h5"></span>**`mt_galmore1_h5`** *(silent check: the first matching branch below is taken)* — **effects:** moves you to [mt_galmore1_h5](../maps/mt_galmore1_h5.md)


    <span id="d-galmore_58"></span>**`galmore_58`** *(silent check: the first matching branch below is taken)* — **effects:** moves you to [galmore_58](../maps/galmore_58.md)




## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 38 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shade7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shade7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shade7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shade7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `shade7` · Data from v0.8.18</small>
