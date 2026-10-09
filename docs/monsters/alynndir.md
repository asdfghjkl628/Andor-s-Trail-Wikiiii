---
description: "Alynndir is a non-player character (NPC) in Andor's Trail, found in Road 5 house. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_mage2_0.png){ .sprite } Alynndir

**Where to find Alynndir:** [Road 5 house](../maps/road5_house.md#pin-npc-alynndir)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_mage2_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Shopkeeper |
| **Found in** | Road 5 house |
| **Introduced** | v0.7.0 or earlier |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Small empty vial](../items/vial_empty1.md) | 100% | 10 |
| [Regular potion of health](../items/health.md) | 100% | 10 |
| [Rat tail](../items/rat_tail.md) | 100% | 5 |
| [Ruby gem](../items/gem2.md) | 5% | 3 |
| [Meat](../items/meat.md) | 30% | 20 |
| [Animal hair](../items/hair.md) | 30% | 5 |
| [Fine leather cap](../items/hat_fine_leather.md) | 100% | 1 |
| [Leather cap of reduced vision](../items/hat_leather_vision.md) | 100% | 1 |
| [Crude leather armor](../items/armour_crude_leather.md) | 100% | 1 |
| [Rigid leather armor](../items/armour_rigid_leather.md) | 100% | 1 |
| [Crude leather gloves](../items/gloves_crude_leather.md) | 100% | 1 |
| [Hardened leather boots](../items/boots_hard_leather.md) | 100% | 1 |
| [Jinxed ring of damage resistance](../items/ring_jinxed1.md) | 100% | 1 |

## Dialogue simulator

Set your quest stages and items, then talk to Alynndir. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/alynndir_1.json" data-npc="Alynndir" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (8 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-alynndir_1"></span>**`alynndir_1`** Alynndir: “Hello there. Welcome to my cabin.”

    - “What do you do around here?” → [alynndir_2](#d-alynndir_2)
    - “What can you tell me about the surroundings here?” → [alynndir_3](#d-alynndir_3)

    <span id="d-alynndir_2"></span>**`alynndir_2`** Alynndir: “Mostly, I trade with travelers on the main road on the way to Nor City.”

    - “Do you have anything to trade?” → *shop opens*
    - “What can you tell me about the surroundings here?” → [alynndir_3](#d-alynndir_3)

    <span id="d-alynndir_3"></span>**`alynndir_3`** Alynndir: “Oh, there is not much around here. Vilegard to the west, Brightport to the east and Sullengard to the south.”

    - Next → [alynndir_4](#d-alynndir_4)

    <span id="d-alynndir_4"></span>**`alynndir_4`** Alynndir: “Up north is just forest. But there are some strange things happening there.”

    - Next → [alynndir_5](#d-alynndir_5)

    <span id="d-alynndir_5"></span>**`alynndir_5`** Alynndir: “I have heard terrible screams coming from the forest to the northwest.”

    - Next → [alynndir_6](#d-alynndir_6)

    <span id="d-alynndir_6"></span>**`alynndir_6`** Alynndir: “I really wonder what is up there.”

    - “Goodbye.” → *conversation ends*
    - “You mentioned Sullengard. What can you tell me about it?” *(if NOT reached stage 19 of [Sullengard story flags (hidden flag)](../quests/sullengard_hidden.md#stage-19))* → [alynndir_10](#d-alynndir_10)

    <span id="d-alynndir_10"></span>**`alynndir_10`** Alynndir: “It is home of the best beer in all of Dhayavar! Every year they hold a beer festival. Matter of fact, that event is coming very soon.”

    - “I think I would like to go there now.” → [alynndir_16](#d-alynndir_16)

    <span id="d-alynndir_16"></span>**`alynndir_16`** Alynndir: “Well, I would too, but it is a very dangerous route to Sullengard. I'd think twice if I were you before making that trip.”

    - “I sure will. Thanks for the warning.” → *conversation ends*
    - “I can handle myself.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.8.2](../versions/0.8.2.md) | Dialogue: 2 lines added, 2 lines changed<br>· text: “Oh, there is not much around here. Vilegard to the west and Brightpor…” → “Oh, there is not much around here. Vilegard to the west, Brightport t…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `alynndir` |
    | Type (wiki) | NPC |
    | Spawn group | `alynndir` |
    | Loot table | `shop_alynndir` |
    | Conversation | `alynndir_1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_mage2:0` |
    | Defined in | `res/raw/monsterlist_v068_npcs.json` |

    Raw data:

    ```json
    {
     "id": "alynndir",
     "name": "Alynndir",
     "iconID": "monsters_mage2:0",
     "monsterClass": "humanoid",
     "spawnGroup": "alynndir",
     "phraseID": "alynndir_1",
     "droplistID": "shop_alynndir"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=alynndir.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=alynndir.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=alynndir.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=alynndir.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
