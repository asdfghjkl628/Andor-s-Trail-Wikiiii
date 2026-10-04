# ![](../assets/icons/monsters/monsters_tometik8_26.png){ .sprite } Shiny Foggerlump

| Stat | Value |
|---|---|
| Class | demon |
| HP | 220 |
| Max AP | 10 |
| Attack cost | 6 |
| Move cost | 5 |
| Damage | 8 to 20 |
| Attack chance | 140 |
| Block chance | 150 |
| Damage resistance | 10 |
| Critical skill | 0 |
| Critical multiplier | 0 |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons can't be critically hit. Your crit build will have to sit this one out.

## On hit

- **Heal HP:** 2 to 5
- **On target:** Mind fog (magnitude 2, 3 rounds, 50% chance)

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Fog in a bottle](../items/fogbottle.md) | 100% | 1 to 2 |

## Found on

- [swamp3](../maps/swamp3.md)

## Quests

- [Fog in the woods](../quests/fogmonster.md): stages 20

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-feygard_fogmonster9"></span>**`feygard_fogmonster9`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 1 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-1); reached stage 2 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-2); reached stage 3 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-3); reached stage 4 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-4); reached stage 5 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-5))* → [feygard_fogmonster9_5](#d-feygard_fogmonster9_5)
    - Next *(if reached stage 1 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-1))* → [feygard_fogmonster9_1](#d-feygard_fogmonster9_1)
    - Next *(if reached stage 2 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-2))* → [feygard_fogmonster9_1](#d-feygard_fogmonster9_1)
    - Next *(if reached stage 3 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-3))* → [feygard_fogmonster9_1](#d-feygard_fogmonster9_1)
    - Next *(if reached stage 4 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-4))* → [feygard_fogmonster9_1](#d-feygard_fogmonster9_1)
    - Next *(if reached stage 5 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-5))* → [feygard_fogmonster9_1](#d-feygard_fogmonster9_1)
    - Next → [feygard_fogmonster9_10](#d-feygard_fogmonster9_10)

    <span id="d-feygard_fogmonster9_5"></span>**`feygard_fogmonster9_5`** Shiny Foggerlump: “Me and my brothers watch over the ruler of the swamp.”

    - “Your brothers have all left the area already. Now to you ...” → *fight starts*
    - “So I'm going to talk to your brothers.” → *conversation ends*

    <span id="d-feygard_fogmonster9_1"></span>**`feygard_fogmonster9_1`** Shiny Foggerlump: “Me and my brothers watch over the ruler of the swamp.”

    - “Not for long, some of your brothers have all left the area already. Attack!” → [feygard_fogmonster9_20](#d-feygard_fogmonster9_20)
    - “So I'm going to talk to your remaining brothers.” → *conversation ends*

    <span id="d-feygard_fogmonster9_10"></span>**`feygard_fogmonster9_10`** Shiny Foggerlump: “Me and my brothers watch over the ruler of the swamp.”

    - “Not for long. Attack!” → [feygard_fogmonster9_20](#d-feygard_fogmonster9_20)
    - “So I'm going to talk to your brothers.” → *conversation ends*

    <span id="d-feygard_fogmonster9_20"></span>**`feygard_fogmonster9_20`** Shiny Foggerlump: “You can't defeat me as long as my brothers stand their ground.” — **effects:** sets stage 20 of [Fog in the woods](../quests/fogmonster.md#stage-20)

    - “Well, in that case stay here. I'll be back in a minute.” → *conversation ends*



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_fogmonster9.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_fogmonster9.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_fogmonster9.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_fogmonster9.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `feygard_fogmonster9` · Data from v0.8.18</small>
