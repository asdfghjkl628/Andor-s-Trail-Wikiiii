---
description: "Shop Owner is a non-player character (NPC) in Andor's Trail, found in Brimhaven. Shopkeeper; starts Honor your parents."
---

# ![](../assets/icons/monsters/monsters_tometik1_2.png){ .sprite } Shop Owner

**Where to find Shop Owner:** Brimhaven: [Brimhaven shop](../maps/brimhaven_shop.md#pin-npc-brv_shop_owner)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_tometik1_2.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Shopkeeper; starts [Honor your parents](../quests/brv_present.md) |
| **Found in** | Brimhaven |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

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

## Quests

- [Honor your parents](../quests/brv_present.md): stages 10, 20
- [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md): stage 130

## Dialogue simulator

Talk to Shop Owner as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_shop_owner_select.json" data-npc="Shop Owner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (11 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_shop_owner_select"></span>**`brv_shop_owner_select`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 130 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-130))* → [brv_shop_owner_20](#d-brv_shop_owner_20)
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

    <span id="d-brv_shop_owner_10"></span>**`brv_shop_owner_10`** Shop Owner: “[His eyes widen.] Oh I was just kidding, child... I mean... honored customer!” — **effects:** sets stage 130 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-130)

    - “Show me your wares, you worm.” → *shop opens*



## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 11 lines added |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 1 line changed<br>· text: “Are you lookng for something in particular?” → “Are you looking for something in particular?” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 3 lines changed<br>· text: “How can I serve you, Sir?” → “How can I serve you, traveler?”<br>· text: “[His eyes widen.] Oh I was just kidding, child... I mean... Sir!” → “[His eyes widen.] Oh I was just kidding, child... I mean... honored c…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brv_shop_owner` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_shop_owner` |
    | Loot table | `brv_jewelery` |
    | Conversation | `brv_shop_owner_select` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik1:2` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_shop_owner",
     "name": "Shop Owner",
     "iconID": "monsters_tometik1:2",
     "unique": 1,
     "phraseID": "brv_shop_owner_select",
     "droplistID": "brv_jewelery"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_shop_owner.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_shop_owner.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_shop_owner.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_shop_owner.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
