---
description: "Servant is an NPC who can also be fought in Andor's Trail, found in Stoutford castle 1, Stoutford castle 2, Guynmart Castle."
---

# ![](../assets/icons/monsters/monsters_tometik8_28.png){ .sprite } Servant

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik8_28.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Stoutford castle 1, Stoutford castle 2, Guynmart Castle |
| **Class** | Undead |
| **HP** | 30 |
| **XP when defeated** | 30 |
| **Entries in game data** | 2 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

!!! info "2 entries in the game data"
    The game data defines 2 separate characters named Servant. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation, location, combat statistics, appearance, movement. Each entry has its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`erwyn_servant`](#v-erwyn_servant) | Enemy | [Stoutford castle 1](../maps/stoutford_castle1.md), [Stoutford castle 2](../maps/stoutford_castle2.md) | – | 30 |
| [`guynmart_servant`](#v-guynmart_servant) | NPC | Guynmart Castle: [Guynmart main 3](../maps/guynmart_main_3.md#pin-npc-guynmart_servant) | – | – |

## Stoutford castle 1 and 1 more (erwyn_servant) { #v-erwyn_servant }

**Entry ID:** `erwyn_servant` · **Type:** Enemy

**Location:** [Stoutford castle 1](../maps/stoutford_castle1.md), [Stoutford castle 2](../maps/stoutford_castle2.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 30 |
| XP when defeated | 30 |
| Damage | 1 to 3 |
| Attack chance | 50 |
| Block chance | 20 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Stoutford castle 1](../maps/stoutford_castle1.md) | – | 2 | – |
| [Stoutford castle 2](../maps/stoutford_castle2.md) | – | 2 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (erwyn_servant)"

    | | |
    |---|---|
    | Entry ID | `erwyn_servant` |
    | Spawn group | `erwyn_servant` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_tometik8:28` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "erwyn_servant",
     "name": "Servant",
     "iconID": "monsters_tometik8:28",
     "maxHP": 30,
     "unique": 1,
     "monsterClass": "undead",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 1,
      "max": 3
     },
     "spawnGroup": "erwyn_servant",
     "attackCost": 5,
     "attackChance": 50,
     "blockChance": 20
    }
    ```


## Guynmart Castle, Guynmart main 3 (guynmart_servant) { #v-guynmart_servant }

**Entry ID:** `guynmart_servant` · **Type:** NPC

**Location:** Guynmart Castle: [Guynmart main 3](../maps/guynmart_main_3.md#pin-npc-guynmart_servant)

### Quests

- [Brimhaven warehouse delivery (hidden flag)](../quests/brv_wh_delivery_nondisplay.md): stage 60

### Dialogue simulator

Set your quest stages and items, then talk to Servant. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_servant_10.json" data-npc="Servant" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_servant-guynmart_servant_10"></span>**`guynmart_servant_10`** Servant: “What are you doing in my lords rooms?”

    - “You are lying around in bed in broad daylight?” → [guynmart_servant_20](#d-guynmart_servant-guynmart_servant_20)
    - “I'm here to give you your ordered item. You don't want it?” *(if hand over 1× [Chandelier](../items/brv_wh_item_04.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 70 of [Delivery](../quests/brv_wh_delivery.md#stage-70))* → [brv_wh_delivery_servant](#d-guynmart_servant-brv_wh_delivery_servant)

    <span id="d-guynmart_servant-guynmart_servant_20"></span>**`guynmart_servant_20`** Servant: “I am checking that the bed of young Robalyrius is still in order.”


    <span id="d-guynmart_servant-brv_wh_delivery_servant"></span>**`brv_wh_delivery_servant`** Servant: “Finally, I'm no longer afraid of that room every time my lord turns off the lights to scare me. Here's my delivery fee.” — **effects:** clears stage 70 of [Delivery](../quests/brv_wh_delivery.md#stage-70), sets stage 60 of [Brimhaven warehouse delivery (hidden flag)](../quests/brv_wh_delivery_nondisplay.md#stage-60), gives 40× [Gold coins](../items/gold.md)

    - “Thank you.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 2 lines added |
| [v0.7.17](../versions/0.7.17.md) | Dialogue: 1 line added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_servant)"

    | | |
    |---|---|
    | Entry ID | `guynmart_servant` |
    | Spawn group | `guynmart_servant` |
    | Loot table | – |
    | Conversation | `guynmart_servant_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:20` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_servant",
     "name": "Servant",
     "iconID": "monsters_ld1:20",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_servant_10"
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn_servant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn_servant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn_servant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn_servant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
