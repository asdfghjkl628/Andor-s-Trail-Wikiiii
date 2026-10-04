# ![](../assets/icons/monsters/monsters_ld1_134.png){ .sprite } Godwin

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

- [wexlow_village](../maps/wexlow_village.md)

## Quests

- [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md): stages 7, 13, 14, 15

??? quote "Dialogue (12 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-village_godwin_selector"></span>**`village_godwin_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 7 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-7))* → [village_godwin_lost_ring_1](#d-village_godwin_lost_ring_1)
    - Next *(if reached stage 7 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-7))* → [village_godwin_has_ring](#d-village_godwin_has_ring)

    <span id="d-village_godwin_lost_ring_1"></span>**`village_godwin_lost_ring_1`** Godwin: “Have you by any chance seen my wedding ring? Oh my, Godelieve is going to kill me when she sees it's missing.”

    - “What does it look like?” → [village_godwin_lost_ring_2](#d-village_godwin_lost_ring_2)

    <span id="d-village_godwin_has_ring"></span>**`village_godwin_has_ring`** Godwin: “A crisis has been averted thanks to you.”

    - “You should do a better job protecting that ring.” → *conversation ends*

    <span id="d-village_godwin_lost_ring_2"></span>**`village_godwin_lost_ring_2`** Godwin: “Um, let me think. Oh, yeah, I remember. It's black, gold and covered in emeralds.”

    - “"Oh, yeah, I remember"? What? Don't you know what it looks like?” → [village_godwin_lost_ring_3](#d-village_godwin_lost_ring_3)
    - “Actually, this is your lucky day. I have it here.” *(if carry 1× [Godwin's ring](../items/godwin_ring.md))* → [village_godwin_lost_ring_4](#d-village_godwin_lost_ring_4)

    <span id="d-village_godwin_lost_ring_3"></span>**`village_godwin_lost_ring_3`** Godwin: “Leave me alone. I don't need you questioning me under this stressful situation.”


    <span id="d-village_godwin_lost_ring_4"></span>**`village_godwin_lost_ring_4`** Godwin: “Your messing with me, right? Give it to me, please.”

    - “Sure. Here, it's yours.” *(if hand over 1× [Godwin's ring](../items/godwin_ring.md))* → [village_godwin_lost_ring_give_ring_free](#d-village_godwin_lost_ring_give_ring_free)
    - “What do you want to give me in exchange for your wife not "killing you"?” → [village_godwin_lost_ring_5](#d-village_godwin_lost_ring_5)

    <span id="d-village_godwin_lost_ring_give_ring_free"></span>**`village_godwin_lost_ring_give_ring_free`** Godwin: “Thank you so much! I really appreciate you just giving it to me. Here are a few coins for your trouble.” — **effects:** sets stage 7 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-7), gives 100× [Gold coins](../items/gold.md), sets stage 13 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-13)


    <span id="d-village_godwin_lost_ring_5"></span>**`village_godwin_lost_ring_5`** Godwin: “Give you? How about 2,000 gold coins?”

    - “Sounds good.” *(if hand over 1× [Godwin's ring](../items/godwin_ring.md))* → [village_godwin_lost_ring_take_ring](#d-village_godwin_lost_ring_take_ring)
    - “Hey Godelieve, did you hear what happened to Godwin?” → [village_godwin_lost_ring_godelieve](#d-village_godwin_lost_ring_godelieve)

    <span id="d-village_godwin_lost_ring_take_ring"></span>**`village_godwin_lost_ring_take_ring`** Godwin: “Thank you so much! Here take these coins.” — **effects:** gives 2000× [Gold coins](../items/gold.md), sets stage 7 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-7), sets stage 14 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-14)


    <span id="d-village_godwin_lost_ring_godelieve"></span>**`village_godwin_lost_ring_godelieve`** [Godelieve](../monsters/village_godelieve_hidden.md): “No. What happened?”

    - “Well, he los...” → [village_godwin_lost_ring_godelieve_2](#d-village_godwin_lost_ring_godelieve_2)

    <span id="d-village_godwin_lost_ring_godelieve_2"></span>**`village_godwin_lost_ring_godelieve_2`** [Godwin](../monsters/village_godwin.md): “NEVER MIND! Godelieve, this kid is being silly. You can go back to whatever it is that you were doing.”

    - “3,000 gold or no ring.” *(if hand over 1× [Godwin's ring](../items/godwin_ring.md))* → [village_godwin_lost_ring_3k](#d-village_godwin_lost_ring_3k)

    <span id="d-village_godwin_lost_ring_3k"></span>**`village_godwin_lost_ring_3k`** Godwin: “Fine! Take the coins you thief.” — **effects:** gives 3000× [Gold coins](../items/gold.md), sets stage 7 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-7), sets stage 15 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-15)

    - “I will put them to good use.” → *conversation ends*



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_godwin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_godwin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_godwin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_godwin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `village_godwin` · Data from v0.8.18</small>
