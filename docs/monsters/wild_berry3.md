---
description: "Especially sweet berries is a non-player character (NPC) in Andor's Trail, found in Deebo's Orchard."
---

# ![](../assets/icons/monsters/items_japozero_484.png){ .sprite } Especially sweet berries

**Where to find Especially sweet berries:** Deebo's Orchard: [way_to_sullengard_east7](../maps/way_to_sullengard_east7.md#pin-npc-wild_berry3), [lodar19](../maps/lodar19.md#pin-npc-wild_berry3), [lodar21](../maps/lodar21.md#pin-npc-wild_berry3), [mountainlake7](../maps/mountainlake7.md#pin-npc-wild_berry3) (+3 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/items_japozero_484.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Deebo's Orchard |
| **Entry ID** | `wild_berry3` |
| **Introduced** | [v0.7.13](../versions/0.7.13.md) |

</div>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [lodar19](../maps/lodar19.md) | – | 5 | Appears later, during a quest |
| [lodar21](../maps/lodar21.md) | – | 4 | Appears later, during a quest |
| [mountainlake7](../maps/mountainlake7.md) | – | 4 | Appears later, during a quest |
| [mountainlake8](../maps/mountainlake8.md) | – | 3 | Appears later, during a quest |
| [way_to_sullengard_east7](../maps/way_to_sullengard_east7.md) | Deebo's Orchard | 2 | Appears later, during a quest |
| [waytolake10](../maps/waytolake10.md) | – | 5 | Appears later, during a quest |
| [waytolake11](../maps/waytolake11.md) | – | 4 | Appears later, during a quest |

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Especially sweet berries. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/chk_wild_berry3.json" data-npc="Especially sweet berries" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-chk_wild_berry3"></span>**`chk_wild_berry3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT wearing [Gardener's gloves](../items/gardener_gloves.md); reached stage 110 of [Fungi Panic - non displayed (hidden flag)](../quests/fungi_panic_nondisplayed.md#stage-110))* → [chk_wild_berry_50](#d-chk_wild_berry_50)
    - branch 2 *(if random chance (5%))* → [chk_wild_berry3_20](#d-chk_wild_berry3_20)
    - branch 3 → [chk_wild_berry3_10](#d-chk_wild_berry3_10)

    <span id="d-chk_wild_berry_50"></span>**`chk_wild_berry_50`** Especially sweet berries: “I should wear my gloves again.”


    <span id="d-chk_wild_berry3_20"></span>**`chk_wild_berry3_20`** *(silent check: the first matching branch below is taken)* — **effects:** gives 1× [Especially sweet red berries](../items/wild_berry3a.md)

    - branch 1 → *NPC leaves*

    <span id="d-chk_wild_berry3_10"></span>**`chk_wild_berry3_10`** *(silent check: the first matching branch below is taken)* — **effects:** gives 1× [Wild red berries](../items/wild_berry3.md)

    - branch 1 → *NPC leaves*



## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 4 lines added |
| [v0.7.17](../versions/0.7.17.md) | Dialogue: 1 line changed<br>· text: “I should better wear my gloves again.” → “I should wear my gloves again.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `wild_berry3` |
    | Spawn group | `wild_berry3` |
    | Loot table | – |
    | Conversation | `chk_wild_berry3` |
    | Faction | – |
    | Movement | – |
    | Icon | `items_japozero:484` |
    | Defined in | `res/raw/monsterlist_fungi_panic.json` |

    Raw data:

    ```json
    {
     "id": "wild_berry3",
     "name": "Especially sweet berries",
     "iconID": "items_japozero:484",
     "moveCost": 999,
     "monsterClass": "animal",
     "spawnGroup": "wild_berry3",
     "phraseID": "chk_wild_berry3"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wild_berry3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wild_berry3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wild_berry3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wild_berry3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
