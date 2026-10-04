# ![](../assets/icons/monsters/monsters_rltiles2_82.png){ .sprite } Ewmondold

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

- [wild2](../maps/wild2.md)

## Quests

- [Perception is not reality](../quests/new_snake_master.md): stages 5, 10, 20

??? quote "Dialogue (10 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-inspiring_snake_master_10"></span>**`inspiring_snake_master_10`** Ewmondold: “Hello, young adventurer. I am Ewmondold, a world famous traveler.”

    - Next → [inspiring_snake_master_select](#d-inspiring_snake_master_select)

    <span id="d-inspiring_snake_master_select"></span>**`inspiring_snake_master_select`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT killed 1× [Snake master](../monsters/snake_master.md); NOT reached stage 5 of [Perception is not reality](../quests/new_snake_master.md#stage-5))* → [inspiring_snake_master_30](#d-inspiring_snake_master_30)
    - Next *(if reached stage 5 of [Perception is not reality](../quests/new_snake_master.md#stage-5); NOT killed 1× [Snake master](../monsters/snake_master.md))* → [inspiring_snake_master_25](#d-inspiring_snake_master_25)
    - Next *(if killed 1× [Snake master](../monsters/snake_master.md); NOT reached stage 5 of [Perception is not reality](../quests/new_snake_master.md#stage-5))* → [inspiring_snake_master_20](#d-inspiring_snake_master_20)
    - Next *(if reached stage 20 of [Perception is not reality](../quests/new_snake_master.md#stage-20); NOT reached stage 25 of [Perception is not reality](../quests/new_snake_master.md#stage-25))* → [inspiring_snake_master_20](#d-inspiring_snake_master_20)
    - Next *(if reached stage 5 of [Perception is not reality](../quests/new_snake_master.md#stage-5); NOT carry 1× [Ewmondold's map](../items/inspiring_snake_master_map.md))* → [inspiring_snake_master_25](#d-inspiring_snake_master_25)
    - Next *(if reached stage 5 of [Perception is not reality](../quests/new_snake_master.md#stage-5); killed 1× [Snake master](../monsters/snake_master.md); hand over 1× [Ewmondold's map](../items/inspiring_snake_master_map.md))* → [inspiring_snake_master_80](#d-inspiring_snake_master_80)

    <span id="d-inspiring_snake_master_30"></span>**`inspiring_snake_master_30`** Ewmondold: “Are you looking to help a man in need?”

    - “Not right now. Bye.” → *conversation ends*
    - “Yes, of course I am. What can I do for you?” → [inspiring_snake_master_40](#d-inspiring_snake_master_40)

    <span id="d-inspiring_snake_master_25"></span>**`inspiring_snake_master_25`** Ewmondold: “Have you found my map yet?”

    - “No, not yet.” → *conversation ends*

    <span id="d-inspiring_snake_master_20"></span>**`inspiring_snake_master_20`** Ewmondold: “Thanks for killing the Snake master, sucker - the way for me to rule is now free...” — **effects:** removes monsters from wild2, sets stage 10 of [Perception is not reality](../quests/new_snake_master.md#stage-10), spawns monsters on snakecave3


    <span id="d-inspiring_snake_master_80"></span>**`inspiring_snake_master_80`** Ewmondold: “Ah, my 'map'. Good!” — **effects:** sets stage 20 of [Perception is not reality](../quests/new_snake_master.md#stage-20)

    - Next → [inspiring_snake_master_20](#d-inspiring_snake_master_20)

    <span id="d-inspiring_snake_master_40"></span>**`inspiring_snake_master_40`** Ewmondold: “I too am an adventurer. I recently attempted to make my way through this here cave.”

    - Next → [inspiring_snake_master_50](#d-inspiring_snake_master_50)

    <span id="d-inspiring_snake_master_50"></span>**`inspiring_snake_master_50`** Ewmondold: “In the beginning it was relatively easy. It wasn't until I ran into the Snake master's minions.”

    - Next → [inspiring_snake_master_60](#d-inspiring_snake_master_60)

    <span id="d-inspiring_snake_master_60"></span>**`inspiring_snake_master_60`** Ewmondold: “I was quickly ambushed and was forced to flee in order to save my life. But of course, during my attempt to flee, I dropped my map.”

    - “I could retrieve the map for you.” → [inspiring_snake_master_70](#d-inspiring_snake_master_70)

    <span id="d-inspiring_snake_master_70"></span>**`inspiring_snake_master_70`** Ewmondold: “Please do and hurry back to me.” — **effects:** sets stage 5 of [Perception is not reality](../quests/new_snake_master.md#stage-5)




## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=inspiring_snake_master.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=inspiring_snake_master.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=inspiring_snake_master.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=inspiring_snake_master.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `inspiring_snake_master` · Data from v0.8.18</small>
