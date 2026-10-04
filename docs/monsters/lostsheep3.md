# ![](../assets/icons/monsters/monsters_karvis2_8.png){ .sprite } Sheep

| Stat | Value |
|---|---|
| Class | animal |
| HP | 5 |
| Max AP | 10 |
| Attack cost | 5 |
| Move cost | 5 |
| Damage | 0 to 1 |
| Attack chance | 10 |
| Block chance | 5 |
| Damage resistance | 0 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Meat](../items/meat.md) | 70% | 0 to 3 |
| [Meat from Tinlyn's sheep](../items/tinlyn_sheep_meat.md) | 100% | 1 |

## Found on

- [fields3](../maps/fields3.md)

## Quests

- [Cheap cuts](../quests/benbyr.md): stages 21
- [Lost sheep](../quests/tinlyn.md): stages 22, 25, 60

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Sheep. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/tinlyn_lostsheep3.json" data-npc="Sheep" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (13 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-tinlyn_lostsheep3"></span>**`tinlyn_lostsheep3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 22 of [Lost sheep](../quests/tinlyn.md#stage-22))* → [tinlyn_lostsheep_y](#d-tinlyn_lostsheep_y)
    - branch 2 → [tinlyn_lostsheep3_n](#d-tinlyn_lostsheep3_n)

    <span id="d-tinlyn_lostsheep_y"></span>**`tinlyn_lostsheep_y`** Sheep: “Baah!”

    - “[Attack]” *(if reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20))* → [tinlyn_lostsheep_atk](#d-tinlyn_lostsheep_atk)

    <span id="d-tinlyn_lostsheep3_n"></span>**`tinlyn_lostsheep3_n`** Sheep: “Baah!”

    - “[Place Tinlyn's bell around the neck of the sheep]” *(if hand over 1× [Tinlyn's sheep bell](../items/tinlyn_bells.md))* → [tinlyn_lostsheep3_place](#d-tinlyn_lostsheep3_place)
    - “[Attack]” *(if reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20))* → [tinlyn_lostsheep_atk](#d-tinlyn_lostsheep_atk)

    <span id="d-tinlyn_lostsheep_atk"></span>**`tinlyn_lostsheep_atk`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 10 of [Lost sheep](../quests/tinlyn.md#stage-10))* → [tinlyn_lostsheep_atk1](#d-tinlyn_lostsheep_atk1)
    - branch 2 → [tinlyn_sheep_atk](#d-tinlyn_sheep_atk)

    <span id="d-tinlyn_lostsheep3_place"></span>**`tinlyn_lostsheep3_place`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 22 of [Lost sheep](../quests/tinlyn.md#stage-22)

    - branch 1 → [tinlyn_lostsheep_check_1](#d-tinlyn_lostsheep_check_1)

    <span id="d-tinlyn_lostsheep_atk1"></span>**`tinlyn_lostsheep_atk1`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 60 of [Lost sheep](../quests/tinlyn.md#stage-60)

    - branch 1 → [tinlyn_sheep_atk](#d-tinlyn_sheep_atk)

    <span id="d-tinlyn_sheep_atk"></span>**`tinlyn_sheep_atk`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 21 of [Cheap cuts](../quests/benbyr.md#stage-21)

    - branch 1 → *fight starts*

    <span id="d-tinlyn_lostsheep_check_1"></span>**`tinlyn_lostsheep_check_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 20 of [Lost sheep](../quests/tinlyn.md#stage-20))* → [tinlyn_lostsheep_check_2](#d-tinlyn_lostsheep_check_2)
    - branch 2 → [tinlyn_lostsheep_placed_2](#d-tinlyn_lostsheep_placed_2)

    <span id="d-tinlyn_lostsheep_check_2"></span>**`tinlyn_lostsheep_check_2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 21 of [Lost sheep](../quests/tinlyn.md#stage-21))* → [tinlyn_lostsheep_check_3](#d-tinlyn_lostsheep_check_3)
    - branch 2 → [tinlyn_lostsheep_placed_2](#d-tinlyn_lostsheep_placed_2)

    <span id="d-tinlyn_lostsheep_placed_2"></span>**`tinlyn_lostsheep_placed_2`** Sheep: “[You place one of the bells around the neck of the sheep]”


    <span id="d-tinlyn_lostsheep_check_3"></span>**`tinlyn_lostsheep_check_3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 22 of [Lost sheep](../quests/tinlyn.md#stage-22))* → [tinlyn_lostsheep_check_4](#d-tinlyn_lostsheep_check_4)
    - branch 2 → [tinlyn_lostsheep_placed_2](#d-tinlyn_lostsheep_placed_2)

    <span id="d-tinlyn_lostsheep_check_4"></span>**`tinlyn_lostsheep_check_4`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 23 of [Lost sheep](../quests/tinlyn.md#stage-23))* → [tinlyn_lostsheep_placed_1](#d-tinlyn_lostsheep_placed_1)
    - branch 2 → [tinlyn_lostsheep_placed_2](#d-tinlyn_lostsheep_placed_2)

    <span id="d-tinlyn_lostsheep_placed_1"></span>**`tinlyn_lostsheep_placed_1`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 25 of [Lost sheep](../quests/tinlyn.md#stage-25)

    - branch 1 → [tinlyn_lostsheep_placed_2](#d-tinlyn_lostsheep_placed_2)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 9 lines changed<br>· text: “(You place one of the bells around the neck of the sheep.)” → “[You place one of the bells around the neck of the sheep]” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lostsheep3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lostsheep3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lostsheep3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lostsheep3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `lostsheep3` · Data from v0.8.18</small>
