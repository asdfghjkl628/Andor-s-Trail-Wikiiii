# ![](../assets/icons/monsters/monsters_karvis2_0.png){ .sprite } Aryfora

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
| [Potion of alertness](../items/pot_alertness.md) | 100% | 6 to 8 |
| [Potion of heroism](../items/pot_heroism.md) | 100% | 7 |
| [Potion of awareness](../items/pot_awareness.md) | 100% | 6 to 9 |
| [Potion of dexterity](../items/pot_dexterity.md) | 100% | 5 to 9 |
| [Potion of sound mind](../items/pot_sound_mind.md) | 100% | 4 to 6 |
| [Restore fatigue](../items/pot_fatigue_restore.md) | 100% | 6 to 7 |
| [Major potion of health](../items/health_major2.md) | 100% | 10 |
| [Ointment of bleeding wounds](../items/pot_bleeding_ointment.md) | 100% | 10 |

## Found on

- [stoutford_potion](../maps/stoutford_potion.md)

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Aryfora. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/stoutford_widow2_0.json" data-npc="Aryfora" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-stoutford_widow2_0"></span>**`stoutford_widow2_0`** Aryfora: “Welcome! I already created some good potions - better than Blornvale's stuff. Want to have a look?”

    - “Of course! Please show me what you have.” → *shop opens*
    - “Can I get your masterpiece, the potion of deftness?” → [stoutford_widow2_1](#d-stoutford_widow2_1)
    - “It's good to see you happy again.” → *conversation ends*

    <span id="d-stoutford_widow2_1"></span>**`stoutford_widow2_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 207 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-207))* → [stoutford_widow2_2](#d-stoutford_widow2_2)
    - branch 2 → [stoutford_widow2_3](#d-stoutford_widow2_3)

    <span id="d-stoutford_widow2_2"></span>**`stoutford_widow2_2`** Aryfora: “Well, no. Somehow I have the feeling that you did not always tell the truth about the damerilias. I don't think that you are old enough to get such a potent potion.”

    - “Then let me see your other potions, please.” → *shop opens*
    - “I have to leave now - bye.” → *conversation ends*

    <span id="d-stoutford_widow2_3"></span>**`stoutford_widow2_3`** Aryfora: “I won't sell this potion for money. You can pay me in flowers - damerilias of course. I will give you one potion of deftness for three damerilias.”

    - “OK, I have some damerilias with me.” *(if hand over 3× [Damerilias](../items/damerilias.md))* → [stoutford_widow2_4](#d-stoutford_widow2_4)
    - “I will think about it.” → *conversation ends*

    <span id="d-stoutford_widow2_4"></span>**`stoutford_widow2_4`** Aryfora: “Here, I have one potion for you.” — **effects:** gives 1× [Potion of deftness](../items/potion_deftness.md)

    - “And another one, please.” *(if hand over 3× [Damerilias](../items/damerilias.md))* → [stoutford_widow2_4](#d-stoutford_widow2_4)
    - “Thank you, that is enough for today.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_widow2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_widow2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_widow2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_widow2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `stoutford_widow2` · Data from v0.8.18</small>
