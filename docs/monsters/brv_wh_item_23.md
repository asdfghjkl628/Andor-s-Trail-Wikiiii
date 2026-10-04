# ![](../assets/icons/monsters/monsters_guynmart_8.png){ .sprite } brv_wh_item_23

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 0 |
| Max AP | 10 |
| Attack cost | 10 |
| Move cost | 99 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Found on

- [brimhaven_warehouse](../maps/brimhaven_warehouse.md)

## Quests

- [Inventory](../quests/brv_wh.md): stages 103

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to brv_wh_item_23. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_wh_item_23.json" data-npc="brv_wh_item_23" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brv_wh_item_23"></span>**`brv_wh_item_23`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if faction “brv_wh_aln” = 103)* → [brv_wh_item_03_1](#d-brv_wh_item_03_1)
    - branch 2 *(if faction “brv_wh_aln” = 123)* → [brv_wh_item_xx_2](#d-brv_wh_item_xx_2)
    - branch 3 *(if faction “brv_wh_aln” ≥ 1)* → [brv_wh_item_xx_3](#d-brv_wh_item_xx_3)
    - branch 4 → [brv_wh_item_23_4](#d-brv_wh_item_23_4)

    <span id="d-brv_wh_item_03_1"></span>**`brv_wh_item_03_1`** brv_wh_item_23: “You have found the yellow boot!” — **effects:** sets stage 103 of [Inventory](../quests/brv_wh.md#stage-103), gives 2× [Yellow boot](../items/brv_wh_item_03.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse


    <span id="d-brv_wh_item_xx_2"></span>**`brv_wh_item_xx_2`** brv_wh_item_23: “You put it back to its former place.” — **effects:** faction “brv_wh_aln” set to 0


    <span id="d-brv_wh_item_xx_3"></span>**`brv_wh_item_xx_3`** brv_wh_item_23: “No, this is not what you're looking for. You put both items back to their bin.” — **effects:** faction “brv_wh_aln” set to 0


    <span id="d-brv_wh_item_23_4"></span>**`brv_wh_item_23_4`** brv_wh_item_23: “You take the item.” — **effects:** faction “brv_wh_aln” set to 123




## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_wh_item_23.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_wh_item_23.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_wh_item_23.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_wh_item_23.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `brv_wh_item_23` · Data from v0.8.18</small>
