# ![](../assets/icons/monsters/monsters_ld1_228.png){ .sprite } Ervelyn

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
| [Weathered shirt](../items/shirt_weathered.md) | 100% | 1 |
| [Patched cloth shirt](../items/shirt_patched_cloth.md) | 100% | 1 |
| [Fine shirt](../items/shirt2.md) | 100% | 1 |
| [Combat vest](../items/armour_cvest1.md) | 100% | 1 |
| [Remgard combat vest](../items/armour_cvest2.md) | 100% | 1 |
| [Hardened leather gloves](../items/gloves_leather1.md) | 100% | 1 |
| [Arulir skin gloves](../items/gloves_arulir.md) | 100% | 1 |

## Found on

- [remgard_clothes](../maps/remgard_clothes.md)

## Quests

- [What is that stench?](../quests/remgard2.md): stages 46

??? quote "Dialogue (7 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ervelyn"></span>**`ervelyn`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 46 of [What is that stench?](../quests/remgard2.md#stage-46))* → [ervelyn_gave1](#d-ervelyn_gave1)
    - branch 2 *(if reached stage 45 of [What is that stench?](../quests/remgard2.md#stage-45))* → [ervelyn_give1](#d-ervelyn_give1)
    - branch 3 → [ervelyn_1](#d-ervelyn_1)

    <span id="d-ervelyn_gave1"></span>**`ervelyn_gave1`** Ervelyn: “Hello again, my friend. You are always welcome here.”

    - Next → [ervelyn_d](#d-ervelyn_d)

    <span id="d-ervelyn_give1"></span>**`ervelyn_give1`** Ervelyn: “It is you! I heard what you did, helping us with that witch Algangror. You have my thanks, friend!”

    - Next → [ervelyn_give2](#d-ervelyn_give2)

    <span id="d-ervelyn_1"></span>**`ervelyn_1`** Ervelyn: “Hello there. Welcome to my shop.”

    - Next → [ervelyn_d](#d-ervelyn_d)

    <span id="d-ervelyn_d"></span>**`ervelyn_d`** Ervelyn: “How may I be of service?”

    - “Let me see what you have to trade.” → [ervelyn_shop](#d-ervelyn_shop)
    - “Never mind. Goodbye.” → *conversation ends*

    <span id="d-ervelyn_give2"></span>**`ervelyn_give2`** Ervelyn: “As a token of my appreciation, please accept this hat that I made. May it guide you through the blinding light.” — **effects:** gives [Woodcutter's feathered hat](../items/hat_crit.md), sets stage 46 of [What is that stench?](../quests/remgard2.md#stage-46)

    - “Thank you.” → *conversation ends*

    <span id="d-ervelyn_shop"></span>**`ervelyn_shop`** Ervelyn: “Certainly.”

    - Next → *shop opens*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ervelyn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ervelyn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ervelyn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ervelyn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `ervelyn` · Data from v0.8.18</small>
