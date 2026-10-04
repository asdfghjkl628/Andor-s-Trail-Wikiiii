# ![](../assets/icons/monsters/monsters_ld1_0.png){ .sprite } Guynmart guard

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

- [guynmart](../maps/guynmart.md)

## Quests

- [Roses](../quests/guynmart.md): stages 16, 18

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guynmart_guard_guide_10"></span>**`guynmart_guard_guide_10`** Guynmart guard: “Hi, kid. Wanna visit Guynmart Castle? Ancient walls, and sometimes a ghost at midnight?”

    - “No, thank you.” → *conversation ends*
    - “Might be interesting. And an easy way to get in...” → [guynmart_guard_guide_20](#d-guynmart_guard_guide_20)

    <span id="d-guynmart_guard_guide_20"></span>**`guynmart_guard_guide_20`** Guynmart guard: “Great choice, you won't regret it. Adults 20 gold, kids 12 gold. Bilingual guide would be 3 gold extra.”

    - “OK, one kid, without guide, please.” *(if pay 12 gold)* → [guynmart_guard_guide_30](#d-guynmart_guard_guide_30)
    - “One kid and a guide, please.” *(if pay 15 gold)* → [guynmart_guard_guide_32](#d-guynmart_guard_guide_32)
    - “I changed my mind. Bye.” → *conversation ends*

    <span id="d-guynmart_guard_guide_30"></span>**`guynmart_guard_guide_30`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 16 of [Roses](../quests/guynmart.md#stage-16), removes monsters from guynmart

    - branch 1 → [guynmart_guard_guide_40](#d-guynmart_guard_guide_40)

    <span id="d-guynmart_guard_guide_32"></span>**`guynmart_guard_guide_32`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 18 of [Roses](../quests/guynmart.md#stage-18), removes monsters from guynmart

    - branch 1 → [guynmart_guard_guide_40](#d-guynmart_guard_guide_40)

    <span id="d-guynmart_guard_guide_40"></span>**`guynmart_guard_guide_40`** Guynmart guard: “[Gold taken] HAHAHA! Once again some stupid person with more money than brains! HAHAHA!”

    - “Hey!” → *NPC leaves*



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_guard_guide.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_guard_guide.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_guard_guide.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_guard_guide.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `guynmart_guard_guide` · Data from v0.8.18</small>
