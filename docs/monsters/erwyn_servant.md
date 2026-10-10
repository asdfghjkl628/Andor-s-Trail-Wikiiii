---
description: "Servant is an NPC you can also fight in Andor's Trail, found in Stoutford castle 1, Stoutford castle 2, Guynmart Castle."
---

# ![](../assets/icons/monsters/monsters_tometik8_28.png){ .sprite } Servant

**Where to find Servant:** [Stoutford castle 1 and 1 more](#v-erwyn_servant), [Guynmart Castle, Guynmart main 3](#v-guynmart_servant)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_tometik8_28.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Stoutford castle 1, Stoutford castle 2, Guynmart Castle |
| **Class** | Undead |
| **HP** | 30 |
| **XP when defeated** | 30 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Stoutford castle 1 and 1 more { #v-erwyn_servant }

**Where:** [Stoutford castle 1](../maps/stoutford_castle1.md), [Stoutford castle 2](../maps/stoutford_castle2.md)

### Combat

| | |
|---|---|
| Class | Undead |
| HP | 30 |
| XP when defeated | 30 |
| Damage | 1 to 3 |
| AC | 50 |
| BC | 20 |
| DR | 0 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

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


## Guynmart Castle, Guynmart main 3 { #v-guynmart_servant }

**Where:** Guynmart Castle: [Guynmart main 3](../maps/guynmart_main_3.md#pin-npc-guynmart_servant)

### Quests

- [Brimhaven warehouse delivery (hidden flag)](../quests/brv_wh_delivery_nondisplay.md): stage 60

### Dialogue simulator

Talk to Servant as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_servant_10.json" data-npc="Servant" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

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



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Servant. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location, combat statistics, appearance, movement.

| Entry | Type | Section |
|---|---|---|
| `erwyn_servant` | Enemy | [Stoutford castle 1 and 1 more](#v-erwyn_servant) |
| `guynmart_servant` | NPC | [Guynmart Castle, Guynmart main 3](#v-guynmart_servant) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: erwyn_servant"

    | | |
    |---|---|
    | Entry ID | `erwyn_servant` |
    | Type (wiki) | Enemy |
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

??? info "Technical information: guynmart_servant"

    | | |
    |---|---|
    | Entry ID | `guynmart_servant` |
    | Type (wiki) | NPC |
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
