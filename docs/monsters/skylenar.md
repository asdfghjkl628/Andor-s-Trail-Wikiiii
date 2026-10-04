# ![](../assets/icons/monsters/monsters_ld1_3.png){ .sprite } Skylenar

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
| [Minor potion of health](../items/health_minor2.md) | 100% | 10 |
| [Regular potion of health](../items/health.md) | 100% | 10 |
| [Major potion of health](../items/health_major2.md) | 100% | 10 |
| [Ring of damage +6](../items/ring_dmg6.md) | 100% | 1 |
| [Polished ring of the protector](../items/polished_ring_protector.md) | 100% | 1 |

## Found on

- [remgard_church](../maps/remgard_church.md)

## Quests

- [The fifth master](../quests/fifth_master.md): stages 60, 65

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Skylenar. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/skylenar.json" data-npc="Skylenar" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (8 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-skylenar"></span>**`skylenar`** Skylenar: “May you forever walk with the Shadow, my child.”

    - “Do you have anything to trade?” → *shop opens*
    - “What do you do around here?” → [skylenar_1](#d-skylenar_1)
    - “I found a strange locked box in the library basement. Can you tell me anything about it?” *(if reached stage 58 of [The fifth master](../quests/fifth_master.md#stage-58); carry 1× [Ancient locked box](../items/ancient_locked_box.md))* → [skylenar_kazaul_10](#d-skylenar_kazaul_10)

    <span id="d-skylenar_1"></span>**`skylenar_1`** Skylenar: “I provide ... guidance to those that seek it. The Shadow guides us. It keeps us safe and comforts us when we sleep.”

    - Next → [skylenar_2](#d-skylenar_2)

    <span id="d-skylenar_kazaul_10"></span>**`skylenar_kazaul_10`** Skylenar: “A locked box, you say? Hmm. May I see it? The etchings...these are older than the Church itself. I do not recognize the language, but I have heard of such seals.”

    - “What kind of seals?” → [skylenar_kazaul_20](#d-skylenar_kazaul_20)

    <span id="d-skylenar_2"></span>**`skylenar_2`** Skylenar: “Lately, it seems Remgard has been in dire need of the comfort that the Shadow provides.”

    - “I see. Goodbye.” → *conversation ends*
    - “Do you have anything to trade?” → *shop opens*

    <span id="d-skylenar_kazaul_20"></span>**`skylenar_kazaul_20`** Skylenar: “Relics from before the rise of the Shadow. Some were bound by the breath of dragonkind. Only a claw or fang from those creatures could undo their locks. At least, that is what the old sermons used to say.” — **effects:** sets stage 60 of [The fifth master](../quests/fifth_master.md#stage-60)

    - “Where would I find a dragon in this age?” *(if NOT reached stage 50 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-50))* → [skylenar_kazaul_30](#d-skylenar_kazaul_30)
    - “I've encountered a dragon.” *(if reached stage 50 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-50))* → [skylenar_kazaul_25](#d-skylenar_kazaul_25)

    <span id="d-skylenar_kazaul_30"></span>**`skylenar_kazaul_30`** Skylenar: “I have never seen one, and few alive have. I have heard the oldest priests whisper of strange remains found deep beneath the earth. They spoke of ash-covered scales in Undertell - relics of some creature that once breathed fire into the…” — **effects:** sets stage 65 of [The fifth master](../quests/fifth_master.md#stage-65)

    - “Thank you, Skylenar. I will seek it out.” → [skylenar_kazaul_40](#d-skylenar_kazaul_40)

    <span id="d-skylenar_kazaul_25"></span>**`skylenar_kazaul_25`** Skylenar: “Oh?...”

    - Next → [skylenar_kazaul_30](#d-skylenar_kazaul_30)

    <span id="d-skylenar_kazaul_40"></span>**`skylenar_kazaul_40`** Skylenar: “Go with caution, child. The Shadow hides many truths beneath its darkness.”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed<br>· text: “I provide .. guidance to those that seek it. The Shadow guides us. It…” → “I provide ... guidance to those that seek it. The Shadow guides us. I…” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 5 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=skylenar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=skylenar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=skylenar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=skylenar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `skylenar` · Data from v0.8.18</small>
