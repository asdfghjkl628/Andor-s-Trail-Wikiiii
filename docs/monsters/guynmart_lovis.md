# ![](../assets/icons/monsters/monsters_karvis2_2.png){ .sprite } Lovis

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

- [guynmart_tower_0](../maps/guynmart_tower_0.md)

## Quests

- [Roses](../quests/guynmart.md): stages 132, 134
- [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md): stages 6

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Lovis. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_lovis_10.json" data-npc="Lovis" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (13 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guynmart_lovis_10"></span>**`guynmart_lovis_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 132 of [Roses](../quests/guynmart.md#stage-132))* → [guynmart_lovis_100](#d-guynmart_lovis_100)
    - branch 2 → [guynmart_lovis_20](#d-guynmart_lovis_20)

    <span id="d-guynmart_lovis_100"></span>**`guynmart_lovis_100`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 134 of [Roses](../quests/guynmart.md#stage-134))* → [guynmart_lovis_200](#d-guynmart_lovis_200)
    - branch 2 *(if 5 rounds passed since timer “guynmart_flute”)* → [guynmart_lovis_104](#d-guynmart_lovis_104)
    - branch 3 → [guynmart_lovis_102](#d-guynmart_lovis_102)

    <span id="d-guynmart_lovis_20"></span>**`guynmart_lovis_20`** Lovis: “What are you - a spy? Or just another prisoner?”

    - “I'm a prisoner too. What is your name?” → [guynmart_lovis_22](#d-guynmart_lovis_22)
    - “I'm $playername. Lady Hannah asked me to look for someone called Lovis.” → [guynmart_lovis_30](#d-guynmart_lovis_30)

    <span id="d-guynmart_lovis_200"></span>**`guynmart_lovis_200`** Lovis: “Oh no! Look! The torturer! I will run around him and look for Guynmart's personal guards outside in the wood. They will help us. I hope Guynmart himself is also with them.” — **effects:** sets stage 134 of [Roses](../quests/guynmart.md#stage-134), spawns monsters on guynmart_tower_0, removes monsters from guynmart_tower_0

    - “OK, we will see each other later.” → *NPC leaves*
    - “I will try to still be alive then.” → *NPC leaves*

    <span id="d-guynmart_lovis_104"></span>**`guynmart_lovis_104`** Lovis: “I will play something on my flute. Maybe this will give us some hope.”

    - “Please do. Maybe a tune you used to play for Lady Hannah?” → [guynmart_lovis_110](#d-guynmart_lovis_110)
    - “Is that a good idea? We might disturb someone.” → *conversation ends*

    <span id="d-guynmart_lovis_102"></span>**`guynmart_lovis_102`** Lovis: “What a dreadful place. Time seems endless here.”

    - “Yes, but we must not give up hope.” → *conversation ends*

    <span id="d-guynmart_lovis_22"></span>**`guynmart_lovis_22`** Lovis: “No, you must tell me your name first.”

    - “No, first you will tell me your name.” → [guynmart_lovis_22](#d-guynmart_lovis_22)
    - “If you are going to be so rude, I have nothing to say.” → *conversation ends*
    - “I am $playername. Lady Hannah asked me to look for someone called Lovis.” → [guynmart_lovis_30](#d-guynmart_lovis_30)

    <span id="d-guynmart_lovis_30"></span>**`guynmart_lovis_30`** Lovis: “You come from Hannah? I must be sure. Prove it!”

    - “Here, I should give you this.” *(if hand over 1× [Lovis' Flute](../items/guynmart_flute.md))* → [guynmart_lovis_40](#d-guynmart_lovis_40)
    - “Oh dear - I forgot to bring your flute!” *(if NOT carry 1× [Lovis' Flute](../items/guynmart_flute.md))* → *conversation ends*

    <span id="d-guynmart_lovis_110"></span>**`guynmart_lovis_110`** Lovis: “[Fluting]”

    - “What a lovely tune! I almost seem to understand the meaning.” → [guynmart_lovis_120](#d-guynmart_lovis_120)
    - “Eh, nice, thank you for trying.” → *conversation ends*

    <span id="d-guynmart_lovis_40"></span>**`guynmart_lovis_40`** Lovis: “My flute! How I have missed it! I believe you now.” — **effects:** sets stage 132 of [Roses](../quests/guynmart.md#stage-132), sets stage 6 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-6), starts timer “guynmart_flute”

    - “This is settled then. Let us now look for an exit.” → *conversation ends*

    <span id="d-guynmart_lovis_120"></span>**`guynmart_lovis_120`** Lovis: “[Fluting]”

    - “...do me wrong...” → [guynmart_lovis_130](#d-guynmart_lovis_130)

    <span id="d-guynmart_lovis_130"></span>**`guynmart_lovis_130`** Lovis: “[Fluting]”

    - “...all my joy ... my delight...” → [guynmart_lovis_190](#d-guynmart_lovis_190)

    <span id="d-guynmart_lovis_190"></span>**`guynmart_lovis_190`** Lovis: “Hush - I hear footsteps.”

    - “Maybe some friendly soul will let us out? After all, we are completely innocent.” → [guynmart_lovis_200](#d-guynmart_lovis_200)



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 13 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_lovis.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_lovis.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_lovis.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_lovis.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `guynmart_lovis` · Data from v0.8.18</small>
