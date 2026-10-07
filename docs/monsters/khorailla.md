---
description: "Khorailla is an NPC who can also be fought in Andor's Trail, found in Prim. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_ld1_221.png){ .sprite } Khorailla

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_221.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Role** | Shopkeeper |
| **Found in** | Prim |
| **Class** | Humanoid |
| **HP** | 1 |
| **XP when defeated** | 1 |
| **Entries in game data** | 2 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "2 entries in the game data"
    The game data defines 2 separate characters named Khorailla. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation, loot or shop stock. Each entry has its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`khorailla`](#v-khorailla) | NPC | Prim: [Tradehouse 0](../maps/tradehouse0.md#pin-npc-khorailla) | shopkeeper | – |
| [`khorailla_cheddar`](#v-khorailla_cheddar) | Enemy | Prim: [Tradehouse 0](../maps/tradehouse0.md) | – | 1 |

## Prim, Tradehouse 0 (khorailla) { #v-khorailla }

**Entry ID:** `khorailla` · **Type:** NPC · **Role:** Shopkeeper

**Location:** Prim: [Tradehouse 0](../maps/tradehouse0.md#pin-npc-khorailla)

### Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Carrots](../items/carrots.md) | 100% | 5 to 12 |
| [Cheese](../items/cheese.md) | 100% | 5 to 12 |
| [Raw perch](../items/rawperch.md) | 100% | 5 to 12 |
| [Cooked perch](../items/cookperch.md) | 100% | 5 to 12 |
| [Cooked chicken leg](../items/chkn_leg.md) | 100% | 5 to 12 |
| [Sap of the charwood tree](../items/drink_charwood1.md) | 100% | 5 to 12 |
| [Concentrated charwood sap](../items/drink_charwood2.md) | 100% | 5 to 12 |

### Quests

- [Destined for great things](../quests/charwood1.md): stage 19

### Dialogue simulator

Set your quest stages and items, then talk to Khorailla. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/khorailla.json" data-npc="Khorailla" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (7 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-khorailla-khorailla"></span>**`khorailla`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 19 of [Destined for great things](../quests/charwood1.md#stage-19)

    - branch 1 *(if reached stage 50 of [Destined for great things](../quests/charwood1.md#stage-50))* → [khorailla1](#d-khorailla-khorailla1)
    - branch 2 → [khorailla3](#d-khorailla-khorailla3)

    <span id="d-khorailla-khorailla1"></span>**`khorailla1`** Khorailla: “Thank you so much for finding our missing people!”

    - “Do you have anything to trade?” → [khorailla2](#d-khorailla-khorailla2)
    - “Please sell me some of your famous Cheddar cheese.” *(if reached stage 30 of [Rare delicacies](../quests/guynmart_wise.md#stage-30))* → [khorailla_cheddar](#d-khorailla-khorailla_cheddar)
    - “You're welcome.” → *conversation ends*

    <span id="d-khorailla-khorailla3"></span>**`khorailla3`** Khorailla: “What ever will we do? Poor Ayell and Fayvara, I sure hope they're alright.”

    - “Do you have anything to trade?” → [khorailla5](#d-khorailla-khorailla5)
    - “What happened to them?” → [khorailla4](#d-khorailla-khorailla4)

    <span id="d-khorailla-khorailla2"></span>**`khorailla2`** Khorailla: “It's not much, but I have some food if you'd like.”

    - “Sure, let me see what you have.” → *shop opens*

    <span id="d-khorailla-khorailla_cheddar"></span>**`khorailla_cheddar`** [Khorailla](../monsters/khorailla.md#v-khorailla_cheddar): “Ah, you really know what's good.”

    - “I hope so. It was a long way to come.” → *shop opens*

    <span id="d-khorailla-khorailla5"></span>**`khorailla5`** Khorailla: “I'm sorry, I'm too distracted to help you right now.”

    - Next → [khorailla4](#d-khorailla-khorailla4)

    <span id="d-khorailla-khorailla4"></span>**`khorailla4`** Khorailla: “You should talk to Maevalia over there.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line added, 2 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (khorailla)"

    | | |
    |---|---|
    | Entry ID | `khorailla` |
    | Spawn group | `khorailla` |
    | Loot table | `shop_khorailla` |
    | Conversation | `khorailla` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:221` |
    | Defined in | `res/raw/monsterlist_v070_npcs.json` |

    Raw data:

    ```json
    {
     "id": "khorailla",
     "name": "Khorailla",
     "iconID": "monsters_ld1:221",
     "phraseID": "khorailla",
     "droplistID": "shop_khorailla"
    }
    ```


## Prim, Tradehouse 0 (khorailla_cheddar) { #v-khorailla_cheddar }

**Entry ID:** `khorailla_cheddar` · **Type:** Enemy

**Location:** Prim: [Tradehouse 0](../maps/tradehouse0.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 1 |
| XP when defeated | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Carrots](../items/carrots.md) | 100% | 5 to 12 |
| [Cheese](../items/cheese.md) | 100% | 5 to 12 |
| [Raw perch](../items/rawperch.md) | 100% | 5 to 12 |
| [Cooked perch](../items/cookperch.md) | 100% | 5 to 12 |
| [Cooked chicken leg](../items/chkn_leg.md) | 100% | 5 to 12 |
| [Sap of the charwood tree](../items/drink_charwood1.md) | 100% | 5 to 12 |
| [Concentrated charwood sap](../items/drink_charwood2.md) | 100% | 5 to 12 |
| [Charwood cheddar](../items/charwood_cheddar.md) | 100% | 5 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Tradehouse 0](../maps/tradehouse0.md) | Prim | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (khorailla_cheddar)"

    | | |
    |---|---|
    | Entry ID | `khorailla_cheddar` |
    | Spawn group | `khorailla_cheddar` |
    | Loot table | `shop_khorailla_cheddar` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:221` |
    | Defined in | `res/raw/monsterlist_v070_npcs.json` |

    Raw data:

    ```json
    {
     "id": "khorailla_cheddar",
     "name": "Khorailla",
     "iconID": "monsters_ld1:221",
     "droplistID": "shop_khorailla_cheddar"
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=khorailla.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=khorailla.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=khorailla.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=khorailla.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
