# ![](../assets/icons/monsters/monsters_tometik1_2.png){ .sprite } Shop Owner

| Stat | Value |
|---|---|
| Class | ? |
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
| [Ring of damage +7](../items/ring_dmg7.md) | 100% | 1 |
| [Ring of poison immunity](../items/ring_antipoison.md) | 100% | 1 |
| [Diamond Ring](../items/diamond_ring.md) | 100% | 4 |
| [Diamond Necklace](../items/expensive_necklace.md) | 100% | 1 |
| [Enhanced Shielding necklace](../items/necklace_shield3.md) | 100% | 1 |
| [Ring of venom](../items/ring_venom.md) | 100% | 1 |
| [Mundane ring](../items/ring1.md) | 100% | 10 |
| [Polished necklace](../items/junk_necklace1.md) | 100% | 2 |
| [Impressive Diamond Necklace](../items/very_expensive_necklace.md) | 100% | 1 |

## Found on

- [brimhaven_shop](../maps/brimhaven_shop.md)

## Quests

- [Honor your parents](../quests/brv_present.md): stages 10, 20
- [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md): stages 130

??? quote "Dialogue (11 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brv_shop_owner_select"></span>**`brv_shop_owner_select`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 130 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-130))* → [brv_shop_owner_20](#d-brv_shop_owner_20)
    - Next → [brv_shop_owner_1](#d-brv_shop_owner_1)

    <span id="d-brv_shop_owner_20"></span>**`brv_shop_owner_20`** Shop Owner: “How can I serve you, traveler?” — **effects:** sets stage 10 of [Honor your parents](../quests/brv_present.md#stage-10)

    - “Show me your wares.” → *shop opens*
    - “I am looking for a necklace in our family colors of red, green and white, that I would like to give as a present to my…” → [brv_shop_owner_30](#d-brv_shop_owner_30)

    <span id="d-brv_shop_owner_1"></span>**`brv_shop_owner_1`** Shop Owner: “May I help you? [He looks down on you.]”

    - “I am just checking things out.” → [brv_shop_owner_2](#d-brv_shop_owner_2)

    <span id="d-brv_shop_owner_30"></span>**`brv_shop_owner_30`** Shop Owner: “No problem. I can arrange one for you. Just tell me how much you want to spend.”

    - “I have to think about it.” → *conversation ends*
    - “Give me a necklace for 5 gold coins.” *(if pay 5 gold)* → [brv_shop_owner_40_1](#d-brv_shop_owner_40_1)
    - “Give me a necklace for 500 gold coins.” *(if pay 500 gold)* → [brv_shop_owner_40_2](#d-brv_shop_owner_40_2)
    - “Give me a necklace for 50,000 gold coins.” *(if pay 50,000 gold)* → [brv_shop_owner_40_3](#d-brv_shop_owner_40_3)

    <span id="d-brv_shop_owner_2"></span>**`brv_shop_owner_2`** Shop Owner: “Are you looking for something in particular?”

    - “[You point to a very expensive looking necklace] How much is this?” → [brv_shop_owner_3](#d-brv_shop_owner_3)

    <span id="d-brv_shop_owner_40_1"></span>**`brv_shop_owner_40_1`** Shop Owner: “Take this... valuable necklace. Your father will be proud to wear it.” — **effects:** gives 1× [Necklace for father (cheap)](../items/necklace_for_father1.md), sets stage 20 of [Honor your parents](../quests/brv_present.md#stage-20)


    <span id="d-brv_shop_owner_40_2"></span>**`brv_shop_owner_40_2`** Shop Owner: “Here is the necklace.” — **effects:** gives 1× [Necklace for father](../items/necklace_for_father2.md), sets stage 20 of [Honor your parents](../quests/brv_present.md#stage-20)


    <span id="d-brv_shop_owner_40_3"></span>**`brv_shop_owner_40_3`** Shop Owner: “Take this wonderful necklace. Your father will be very happy.” — **effects:** gives 1× [Necklace for father (expensive)](../items/necklace_for_father3.md), sets stage 20 of [Honor your parents](../quests/brv_present.md#stage-20)


    <span id="d-brv_shop_owner_3"></span>**`brv_shop_owner_3`** Shop Owner: “I don't think this would fit you.”

    - “Well, I didn't ask if it would fit. I asked how much it was.” → [brv_shop_owner_4](#d-brv_shop_owner_4)

    <span id="d-brv_shop_owner_4"></span>**`brv_shop_owner_4`** Shop Owner: “It is very expensive. I don't think we have anything for you. You are obviously in the wrong place. Please leave.”

    - “[You slowly pull out your coin bag and show him your gold.]” *(if have 1,000 gold)* → [brv_shop_owner_10](#d-brv_shop_owner_10)

    <span id="d-brv_shop_owner_10"></span>**`brv_shop_owner_10`** Shop Owner: “[His eyes widen.] Oh I was just kidding, child... I mean... honored customer!” — **effects:** sets stage 130 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-130)

    - “Show me your wares, you worm.” → *shop opens*



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_shop_owner.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_shop_owner.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_shop_owner.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_shop_owner.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `brv_shop_owner` · Data from v0.8.18</small>
