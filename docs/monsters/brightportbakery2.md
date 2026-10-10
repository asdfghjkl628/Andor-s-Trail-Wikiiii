---
description: "Effa is a non-player character (NPC) in Andor's Trail, found in Brightport. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_ld1_144.png){ .sprite } Effa

**Where to find Effa:** Brightport: [Brightport bakery](../maps/brightport_bakery.md#pin-npc-brightportbakery2)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld1_144.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Shopkeeper |
| **Found in** | Brightport |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Brightport bread](../items/brightport_bakery.md) | 100% | 5 |
| [Berry pie](../items/brightport_bakery1.md) | 100% | 2 |
| [Bread](../items/bread.md) | 100% | 10 |
| [Cake](../items/cake.md) | 100% | 1 |
| [Apple pie](../items/brightport_bakery2.md) | 100% | 3 |

## Dialogue simulator

Talk to Effa as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_bakery_selector.json" data-npc="Effa" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightport_bakery_selector"></span>**`brightport_bakery_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 246 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-246))* → [brightport_bakery](#d-brightport_bakery)
    - Next *(if reached stage 246 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-246))* → [brightport_bakery_behindcounter](#d-brightport_bakery_behindcounter)

    <span id="d-brightport_bakery"></span>**`brightport_bakery`** [Effa](../monsters/brightportbakery2.md): “Hello, and welcome to the world famous bakery of Brightport, how may I help you?”

    - “Please show me the menu.” → *shop opens*

    <span id="d-brightport_bakery_behindcounter"></span>**`brightport_bakery_behindcounter`** [Effa](../monsters/brightportbakery2.md): “We don't serve people from behind the counter, please stand in front.”




## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightportbakery2` |
    | Type (wiki) | NPC |
    | Spawn group | `brightportbakery2` |
    | Loot table | `brightport_bakery` |
    | Conversation | `brightport_bakery_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:144` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportbakery2",
     "name": "Effa",
     "iconID": "monsters_ld1:144",
     "unique": 1,
     "phraseID": "brightport_bakery_selector",
     "droplistID": "brightport_bakery"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportbakery2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportbakery2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportbakery2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportbakery2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
