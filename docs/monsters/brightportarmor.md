---
description: "Freya is a non-player character (NPC) in Andor's Trail, found in Brightport. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_ld1_148.png){ .sprite } Freya

**Where to find Freya:** Brightport: [Brightport armorer](../maps/brightport_armorer.md#pin-npc-brightportarmor)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_148.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Shopkeeper |
| **Found in** | Brightport |
| **Entry ID** | `brightportarmor` |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Worn chainmail](../items/chmail2.md) | 100% | 1 |
| [Worn splint mail](../items/spmail2.md) | 100% | 1 |
| [Copper shield](../items/brightport_bronzeshield.md) | 100% | 1 |
| [Steel barbute](../items/brightport_helmet.md) | 100% | 1 |

## Quests

- [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md): stages 33, 235, 236

## Dialogue simulator

Set your quest stages and items, then talk to Freya. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_armor.json" data-npc="Freya" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (7 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightport_armor"></span>**`brightport_armor`** Freya: “Welcome to Brightport's armor smithy, how can I assist you?” — **effects:** sets stage 33 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-33)

    - “Please show me your wares.” → [brightport_armor0](#d-brightport_armor0)
    - “Everything seems pretty worn out, don't you have anything better to offer?” *(if reached stage 235 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-235))* → [brightport_armor4](#d-brightport_armor4)

    <span id="d-brightport_armor0"></span>**`brightport_armor0`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 235 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-235), sets stage 33 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-33)

    - branch 1 → *shop opens*

    <span id="d-brightport_armor4"></span>**`brightport_armor4`** Freya: “My husband and I maintain the guards' equipment, and we have pieces of great quality. But the Doughe set strict rules, so with Feygard soldiers stationed here we can't sell anything without approval.” — **effects:** sets stage 236 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-236)

    - “Doughe?” → [brightport_armor5](#d-brightport_armor5)
    - “How can I receive approval then?” → [brightport_armor7](#d-brightport_armor7)

    <span id="d-brightport_armor5"></span>**`brightport_armor5`** Freya: “The Doughe is the title of the ruler of Brightport. Those of us whose families have lived here for generations hold the Doughe in great respect.”

    - “Where can I find the Doughe?” → [brightport_armor6](#d-brightport_armor6)

    <span id="d-brightport_armor7"></span>**`brightport_armor7`** Freya: “You would have to ask for permission directly, the Doughe is on the second floor of the bakery, in the eastern part of town.”

    - Next → [brightport_armor8](#d-brightport_armor8)

    <span id="d-brightport_armor6"></span>**`brightport_armor6`** Freya: “That is simple, just follow the scent! Sorry I couldn't help myself, He is on the second floor of the bakery, just go to the eastern part of the town.”

    - “Thanks, I'll go see him.” → *conversation ends*
    - “That joke didn't smell good. Bye.” → *conversation ends*

    <span id="d-brightport_armor8"></span>**`brightport_armor8`** Freya: “But I wouldn't go and bother him if I were you, it is unlikely he would make an exception.”

    - “It is worth trying.” → *conversation ends*
    - “He'll make an exception for this purse.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 7 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightportarmor` |
    | Spawn group | `brightportarmor` |
    | Loot table | `freyja_shoplist` |
    | Conversation | `brightport_armor` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:148` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportarmor",
     "name": "Freya",
     "iconID": "monsters_ld1:148",
     "phraseID": "brightport_armor",
     "droplistID": "freyja_shoplist"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportarmor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportarmor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportarmor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportarmor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
