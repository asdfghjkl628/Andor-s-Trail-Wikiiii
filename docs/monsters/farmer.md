---
description: "Farmer is a non-player character (NPC) in Andor's Trail, found in Crossglen, Crossroads Guardhouse, Remgard, Stoutford. Starts Flows through the veins."
---

# ![](../assets/icons/monsters/monsters_man1_0.png){ .sprite } Farmer

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_man1_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Starts [Flows through the veins](../quests/loneford.md) |
| **Found in** | Crossglen, Crossroads Guardhouse, Remgard, Stoutford |
| **Entries in game data** | 5 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "5 entries in the game data"
    The game data defines 5 separate characters named Farmer. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation, location, appearance. Each entry has its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`farmer`](#v-farmer) | NPC | Crossglen: [Crossglen](../maps/crossglen.md#pin-npc-farmer) | – |
| [`loneford_farmer0`](#v-loneford_farmer0) | NPC | Crossroads Guardhouse: [Loneford 1](../maps/loneford1.md#pin-npc-loneford_farmer0) | starts [Flows through the veins](../quests/loneford.md) |
| [`remgard_farmer1`](#v-remgard_farmer1) | NPC | Remgard: [Remgard 1](../maps/remgard1.md#pin-npc-remgard_farmer1) | – |
| [`remgard_farmer2`](#v-remgard_farmer2) | NPC | Remgard: [Remgard 4](../maps/remgard4.md#pin-npc-remgard_farmer2) | – |
| [`stouford_farmer2`](#v-stouford_farmer2) | NPC | Stoutford: [Stoutford north-west](../maps/stoutford_nw.md#pin-npc-stouford_farmer2) | – |

## Crossglen, Crossglen (farmer) { #v-farmer }

**Entry ID:** `farmer` · **Type:** NPC

**Location:** Crossglen: [Crossglen](../maps/crossglen.md#pin-npc-farmer)

### Dialogue simulator

Set your quest stages and items, then talk to Farmer. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/farm1.json" data-npc="Farmer" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-farmer-farm1"></span>**`farm1`** Farmer: “Please do not disturb me, I have work to do.”

    - “Have you seen my brother Andor?” → [farm_andor](#d-farmer-farm_andor)

    <span id="d-farmer-farm_andor"></span>**`farm_andor`** Farmer: “Andor? No, I haven't seen him around lately.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (farmer)"

    | | |
    |---|---|
    | Entry ID | `farmer` |
    | Spawn group | `crossglen_farmer1` |
    | Loot table | – |
    | Conversation | `farm1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_man1:0` |
    | Defined in | `res/raw/monsterlist_crossglen_npcs.json` |

    Raw data:

    ```json
    {
     "id": "farmer",
     "name": "Farmer",
     "iconID": "monsters_man1:0",
     "monsterClass": "humanoid",
     "spawnGroup": "crossglen_farmer1",
     "phraseID": "farm1"
    }
    ```


## Crossroads Guardhouse, Loneford 1 (loneford_farmer0) { #v-loneford_farmer0 }

**Entry ID:** `loneford_farmer0` · **Type:** NPC · **Role:** Starts [Flows through the veins](../quests/loneford.md)

**Location:** Crossroads Guardhouse: [Loneford 1](../maps/loneford1.md#pin-npc-loneford_farmer0)

### Quests

- [Flows through the veins](../quests/loneford.md): stages 10, 11

### Dialogue simulator

Set your quest stages and items, then talk to Farmer. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/loneford_farmer0.json" data-npc="Farmer" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (9 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-loneford_farmer0-loneford_farmer0"></span>**`loneford_farmer0`** Farmer: “What have we done to deserve this?”

    - “What's wrong?” → [loneford_farmer0_1](#d-loneford_farmer0-loneford_farmer0_1)

    <span id="d-loneford_farmer0-loneford_farmer0_1"></span>**`loneford_farmer0_1`** Farmer: “Didn't you hear about the illness?”

    - “What illness?” → [loneford_farmer_il_1](#d-loneford_farmer0-loneford_farmer_il_1)

    <span id="d-loneford_farmer0-loneford_farmer_il_1"></span>**`loneford_farmer_il_1`** Farmer: “It all started a few days ago. Selgan found Hesor passed out on his old crop field, completely white faced and shivering.”

    - Next → [loneford_farmer_il_2](#d-loneford_farmer0-loneford_farmer_il_2)

    <span id="d-loneford_farmer0-loneford_farmer_il_2"></span>**`loneford_farmer_il_2`** Farmer: “A few days later, Selgan started showing the same symptoms as Hesor, with stomach aches. I also started feeling the pains and got the shivers.”

    - Next → [loneford_farmer_il_3](#d-loneford_farmer0-loneford_farmer_il_3)

    <span id="d-loneford_farmer0-loneford_farmer_il_3"></span>**`loneford_farmer_il_3`** Farmer: “Then, all people showed the symptoms in one way or another.”

    - Next → [loneford_farmer_il_4](#d-loneford_farmer0-loneford_farmer_il_4)

    <span id="d-loneford_farmer0-loneford_farmer_il_4"></span>**`loneford_farmer_il_4`** Farmer: “Poor old Selgan and Hesor apparently got the worst of it, and both died the day before yesterday.”

    - Next → [loneford_farmer_il_5](#d-loneford_farmer0-loneford_farmer_il_5)

    <span id="d-loneford_farmer0-loneford_farmer_il_5"></span>**`loneford_farmer_il_5`** Farmer: “Cursed illness, why did it have to be Selgan and Hesor? I wonder who is next.”

    - Next → [loneford_farmer_il_6](#d-loneford_farmer0-loneford_farmer_il_6)

    <span id="d-loneford_farmer0-loneford_farmer_il_6"></span>**`loneford_farmer_il_6`** Farmer: “We all started to investigate what could be the cause. We still aren't certain what the cause is, but we have our suspicions.” — **effects:** sets stage 10 of [Flows through the veins](../quests/loneford.md#stage-10)

    - Next → [loneford_farmer_il_7](#d-loneford_farmer0-loneford_farmer_il_7)

    <span id="d-loneford_farmer0-loneford_farmer_il_7"></span>**`loneford_farmer_il_7`** Farmer: “Luckily, now Feygard has sent patrols up here to help guard the village at least. We are still suffering though, and we fear who will be taken by the illness next.” — **effects:** sets stage 11 of [Flows through the veins](../quests/loneford.md#stage-11)




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (loneford_farmer0)"

    | | |
    |---|---|
    | Entry ID | `loneford_farmer0` |
    | Spawn group | `loneford_farmer0` |
    | Loot table | – |
    | Conversation | `loneford_farmer0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:1` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "loneford_farmer0",
     "name": "Farmer",
     "iconID": "monsters_karvis2:1",
     "monsterClass": "humanoid",
     "spawnGroup": "loneford_farmer0",
     "phraseID": "loneford_farmer0"
    }
    ```


## Remgard, Remgard 1 (remgard_farmer1) { #v-remgard_farmer1 }

**Entry ID:** `remgard_farmer1` · **Type:** NPC

**Location:** Remgard: [Remgard 1](../maps/remgard1.md#pin-npc-remgard_farmer1)

### Dialogue simulator

Set your quest stages and items, then talk to Farmer. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/remgard_farmer1.json" data-npc="Farmer" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-remgard_farmer1-remgard_farmer1"></span>**`remgard_farmer1`** Farmer: “Oh, hello. I can't talk right now, must finish planting these crops.”

    - “Do you know where I can find some damerilias?” *(if reached stage 10 of [The roots of love](../quests/roots_love.md#stage-10); NOT reached stage 20 of [The roots of love](../quests/roots_love.md#stage-20))* → [remgard_farmer1_root10_0](#d-remgard_farmer1-remgard_farmer1_root10_0)

    <span id="d-remgard_farmer1-remgard_farmer1_root10_0"></span>**`remgard_farmer1_root10_0`** Farmer: “No. Excuse me, I have work to do.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (remgard_farmer1)"

    | | |
    |---|---|
    | Entry ID | `remgard_farmer1` |
    | Spawn group | `remgard_farmer1` |
    | Loot table | – |
    | Conversation | `remgard_farmer1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:26` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "remgard_farmer1",
     "name": "Farmer",
     "iconID": "monsters_ld1:26",
     "monsterClass": "humanoid",
     "spawnGroup": "remgard_farmer1",
     "phraseID": "remgard_farmer1"
    }
    ```


## Remgard, Remgard 4 (remgard_farmer2) { #v-remgard_farmer2 }

**Entry ID:** `remgard_farmer2` · **Type:** NPC

**Location:** Remgard: [Remgard 4](../maps/remgard4.md#pin-npc-remgard_farmer2)

### Dialogue simulator

Set your quest stages and items, then talk to Farmer. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/remgard_farmer2.json" data-npc="Farmer" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-remgard_farmer2-remgard_farmer2"></span>**`remgard_farmer2`** Farmer: “I hope the lands will be good to us this season.”

    - “Do you know where I can find some damerilias?” *(if reached stage 10 of [The roots of love](../quests/roots_love.md#stage-10); NOT reached stage 20 of [The roots of love](../quests/roots_love.md#stage-20))* → [remgard_farmer2_roots10_0](#d-remgard_farmer2-remgard_farmer2_roots10_0)

    <span id="d-remgard_farmer2-remgard_farmer2_roots10_0"></span>**`remgard_farmer2_roots10_0`** Farmer: “Damerilias. I haven't seen one in a long time. Try with Caeda, she used to give us a damerilia sometimes.”

    - “Thank you.” → *conversation ends*
    - “Caeda?” → [remgard_farmer2_roots10_1](#d-remgard_farmer2-remgard_farmer2_roots10_1)

    <span id="d-remgard_farmer2-remgard_farmer2_roots10_1"></span>**`remgard_farmer2_roots10_1`** Farmer: “I don't know where she might be at the moment. And I have work to do now, so excuse me.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (remgard_farmer2)"

    | | |
    |---|---|
    | Entry ID | `remgard_farmer2` |
    | Spawn group | `remgard_farmer2` |
    | Loot table | – |
    | Conversation | `remgard_farmer2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:220` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "remgard_farmer2",
     "name": "Farmer",
     "iconID": "monsters_ld1:220",
     "monsterClass": "humanoid",
     "spawnGroup": "remgard_farmer2",
     "phraseID": "remgard_farmer2"
    }
    ```


## Stoutford, Stoutford north-west (stouford_farmer2) { #v-stouford_farmer2 }

**Entry ID:** `stouford_farmer2` · **Type:** NPC

**Location:** Stoutford: [Stoutford north-west](../maps/stoutford_nw.md#pin-npc-stouford_farmer2)

### Dialogue simulator

Set your quest stages and items, then talk to Farmer. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stoutford_builder_0.json" data-npc="Farmer" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-stouford_farmer2-stoutford_builder_0"></span>**`stoutford_builder_0`** Farmer: “Sorry. I have work to do.”




### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (stouford_farmer2)"

    | | |
    |---|---|
    | Entry ID | `stouford_farmer2` |
    | Spawn group | `stouford_farmer2` |
    | Loot table | – |
    | Conversation | `stoutford_builder_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:27` |
    | Defined in | `res/raw/monsterlist_stoutford.json` |

    Raw data:

    ```json
    {
     "id": "stouford_farmer2",
     "name": "Farmer",
     "iconID": "monsters_ld1:27",
     "phraseID": "stoutford_builder_0"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=farmer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=farmer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=farmer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=farmer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
