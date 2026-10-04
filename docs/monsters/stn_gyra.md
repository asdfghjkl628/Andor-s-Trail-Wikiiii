# ![](../assets/icons/monsters/monsters_ld1_158.png){ .sprite } Gyra

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

- [stoutford_castle1](../maps/stoutford_castle1.md)

## Quests

- [Lost girl looking for lost things](../quests/stn_quest_gyra.md): stages 20, 30
- [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md): stages 11

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Gyra. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/stn_gyra_init.json" data-npc="Gyra" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (6 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-stn_gyra_init"></span>**`stn_gyra_init`** Gyra: “Help! You must help me! Please!”

    - “What is your problem, my little one?” → [stn_gyra_init_10](#d-stn_gyra_init_10)

    <span id="d-stn_gyra_init_10"></span>**`stn_gyra_init_10`** Gyra: “I am Gyra, Odirath's daughter. My father is the armorer of Stoutford, a very important man.”

    - Next → [stn_gyra_init_12](#d-stn_gyra_init_12)

    <span id="d-stn_gyra_init_12"></span>**`stn_gyra_init_12`** Gyra: “I was looking for Lord Bourbon's helmet, when I was surprised by these monsters.” — **effects:** sets stage 20 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-20)

    - Next → [stn_gyra_init_20](#d-stn_gyra_init_20)

    <span id="d-stn_gyra_init_20"></span>**`stn_gyra_init_20`** Gyra: “So I hid here in the storeroom and didn't dare to leave the hiding place.”

    - “Eh, I will be back soon. Maybe. But ... probably not, no. I hate kids.” → *conversation ends*
    - “Of course I will help you. Just follow me.” → [stn_gyra_init_50](#d-stn_gyra_init_50)

    <span id="d-stn_gyra_init_50"></span>**`stn_gyra_init_50`** Gyra: “Great! It is so important that Lord Bourbon gets his helmet. Then he will drive out these monsters!”

    - Next → [stn_gyra_init_52](#d-stn_gyra_init_52)

    <span id="d-stn_gyra_init_52"></span>**`stn_gyra_init_52`** Gyra: “I started to look in the main house, but maybe we have to search the whole castle.” — **effects:** sets stage 30 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-30), sets stage 11 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-11), starts timer “stn_gyra_hint”, removes monsters from stoutford_castle1, spawns monsters on stoutford_castle1

    - “Let's go then.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 6 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_gyra.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_gyra.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_gyra.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_gyra.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `stn_gyra` · Data from v0.8.18</small>
