# ![](../assets/icons/monsters/monsters_rltiles2_106.png){ .sprite } Hungry pig

| Stat | Value |
|---|---|
| Class | animal |
| HP | 303 |
| Max AP | 10 |
| Attack cost | 10 |
| Move cost | 5 |
| Damage | 2 to 3 |
| Attack chance | 80 |
| Block chance | 90 |
| Damage resistance | 9 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Found on

- [gapfillerhole](../maps/gapfillerhole.md)

## Quests

- [Unusual experiences and achievements](../quests/achievements.md): stages 135
- [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md): stages 51

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Hungry pig. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/hungry_pig_selector.json" data-npc="Hungry pig" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (9 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-hungry_pig_selector"></span>**`hungry_pig_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if faction “pig_faction” = 15)* → [hungry_pig_sick](#d-hungry_pig_sick)
    - branch 2 *(if faction “pig_faction” ≥ 10)* → [hungry_pig_upset_stomach](#d-hungry_pig_upset_stomach)
    - branch 3 *(if carry 1× [Rotten meat](../items/meat2.md))* → [hungry_pig_feed](#d-hungry_pig_feed)
    - branch 4 *(if NOT hand over 1× [Rotten meat](../items/meat2.md))* → [hungry_pig_grunt](#d-hungry_pig_grunt)

    <span id="d-hungry_pig_sick"></span>**`hungry_pig_sick`** Hungry pig: “[Squeal]” — **effects:** faction “pig_faction” set to 0

    - “Are you OK?” → [hungry_pig_dies](#d-hungry_pig_dies)

    <span id="d-hungry_pig_upset_stomach"></span>**`hungry_pig_upset_stomach`** Hungry pig: “[Squeal] Please, stop feeding these to me. They're making my stomach hurt.”

    - “What? You can talk?” *(if NOT reached stage 51 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-51))* → [hungry_pig_upset_stomach_2](#d-hungry_pig_upset_stomach_2)
    - “More eating and less talking.” *(if reached stage 51 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-51))* → [hungry_pig_upset_stomach_2](#d-hungry_pig_upset_stomach_2)

    <span id="d-hungry_pig_feed"></span>**`hungry_pig_feed`** Hungry pig: “[Grunt]”

    - “Hungry? Here, have a piece of rotten meat.” *(if hand over 1× [Rotten meat](../items/meat2.md))* → [hungry_pig_feed_2](#d-hungry_pig_feed_2)

    <span id="d-hungry_pig_grunt"></span>**`hungry_pig_grunt`** Hungry pig: “[Grunt]”


    <span id="d-hungry_pig_dies"></span>**`hungry_pig_dies`** [Dummy NPC](../monsters/none.md): “The hungry pig dies due to the rotten meat.” — **effects:** removes monsters from gapfillerhole, sets stage 135 of [Unusual experiences and achievements](../quests/achievements.md#stage-135)


    <span id="d-hungry_pig_upset_stomach_2"></span>**`hungry_pig_upset_stomach_2`** Hungry pig: “[Grunt]” — **effects:** sets stage 51 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-51)

    - “Here. Have another piece of rotten meat. It's good for you.” *(if hand over 1× [Rotten meat](../items/meat2.md))* → [hungry_pig_upset_stomach_3](#d-hungry_pig_upset_stomach_3)

    <span id="d-hungry_pig_feed_2"></span>**`hungry_pig_feed_2`** Hungry pig: “[Grunt]” — **effects:** faction “pig_faction” +1


    <span id="d-hungry_pig_upset_stomach_3"></span>**`hungry_pig_upset_stomach_3`** Hungry pig: “[Squeal]” — **effects:** faction “pig_faction” +1




## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 9 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hungry_pig.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hungry_pig.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hungry_pig.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hungry_pig.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `hungry_pig` · Data from v0.8.18</small>
