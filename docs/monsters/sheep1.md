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

- [fields6](../maps/fields6.md)

## Quests

- [Cheap cuts](../quests/benbyr.md): stages 21
- [Lost sheep](../quests/tinlyn.md): stages 60

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-tinlyn_sheep"></span>**`tinlyn_sheep`** Sheep: “Baah!”

    - “[Attack]” *(if reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20))* → [tinlyn_lostsheep_atk](#d-tinlyn_lostsheep_atk)

    <span id="d-tinlyn_lostsheep_atk"></span>**`tinlyn_lostsheep_atk`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 10 of [Lost sheep](../quests/tinlyn.md#stage-10))* → [tinlyn_lostsheep_atk1](#d-tinlyn_lostsheep_atk1)
    - branch 2 → [tinlyn_sheep_atk](#d-tinlyn_sheep_atk)

    <span id="d-tinlyn_lostsheep_atk1"></span>**`tinlyn_lostsheep_atk1`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 60 of [Lost sheep](../quests/tinlyn.md#stage-60)

    - branch 1 → [tinlyn_sheep_atk](#d-tinlyn_sheep_atk)

    <span id="d-tinlyn_sheep_atk"></span>**`tinlyn_sheep_atk`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 21 of [Cheap cuts](../quests/benbyr.md#stage-21)

    - branch 1 → *fight starts*



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sheep1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sheep1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sheep1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sheep1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `sheep1` · Data from v0.8.18</small>
