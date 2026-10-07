---
description: "Horse is a non-player character (NPC) in Andor's Trail, found in Flagstone Prison, Guynmart Castle."
---

# ![](../assets/icons/monsters/monsters_ld2_66.png){ .sprite } Horse

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld2_66.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Flagstone Prison, Guynmart Castle |
| **Entries in game data** | 2 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

!!! info "2 entries in the game data"
    The game data defines 2 separate characters named Horse. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation, location. Each entry has its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`stn_horse`](#v-stn_horse) | NPC | Flagstone Prison: [Stoutford castle stable](../maps/stoutford_castle_stable.md#pin-npc-stn_horse) | – |
| [`guynmart_horse`](#v-guynmart_horse) | NPC | Guynmart Castle: [Guynmart](../maps/guynmart.md#pin-npc-guynmart_horse), Guynmart Castle: [Guynmart wood 4](../maps/guynmart_wood_4.md#pin-npc-guynmart_horse) (+1 more) | – |

## Flagstone Prison, Stoutford castle stable (stn_horse) { #v-stn_horse }

**Entry ID:** `stn_horse` · **Type:** NPC

**Location:** Flagstone Prison: [Stoutford castle stable](../maps/stoutford_castle_stable.md#pin-npc-stn_horse)

### Quests

- [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md): stage 6

### Dialogue simulator

Set your quest stages and items, then talk to Horse. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stn_horse.json" data-npc="Horse" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (6 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-stn_horse-stn_horse"></span>**`stn_horse`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 6 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-6))* → [stn_horse_90](#d-stn_horse-stn_horse_90)
    - branch 2 → [stn_horse_10](#d-stn_horse-stn_horse_10)

    <span id="d-stn_horse-stn_horse_90"></span>**`stn_horse_90`** Horse: “Neigh.”


    <span id="d-stn_horse-stn_horse_10"></span>**`stn_horse_10`** Horse: “Neigh!”

    - “Oh, nice to meet you.” → [stn_horse_12](#d-stn_horse-stn_horse_12)

    <span id="d-stn_horse-stn_horse_12"></span>**`stn_horse_12`** Horse: “Neigh!!!”

    - “One might think that you want something from me.” → [stn_horse_20](#d-stn_horse-stn_horse_20)
    - “Haha, I think I'm going crazy. Horses can't talk.” → *conversation ends*
    - “Neigh.” → [stn_horse_12](#d-stn_horse-stn_horse_12)

    <span id="d-stn_horse-stn_horse_20"></span>**`stn_horse_20`** Horse: “Neigh! Neigh!!! neigh.”

    - “Oh I see now. They left you here without anything to drink. Wait, Here is a bucket of water.” → [stn_horse_30](#d-stn_horse-stn_horse_30)
    - “You are becoming gradually more annoying. I'm leaving now.” → *conversation ends*

    <span id="d-stn_horse-stn_horse_30"></span>**`stn_horse_30`** Horse: “[After drinking greedily] Neiiieieiiigh!!” — **effects:** sets stage 6 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-6)

    - “There, now you feel better! I have to leave now.” → [stn_horse_90](#d-stn_horse-stn_horse_90)



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 6 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (stn_horse)"

    | | |
    |---|---|
    | Entry ID | `stn_horse` |
    | Spawn group | `stn_horse` |
    | Loot table | – |
    | Conversation | `stn_horse` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:66` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_horse",
     "name": "Horse",
     "iconID": "monsters_ld2:66",
     "monsterClass": "animal",
     "phraseID": "stn_horse"
    }
    ```


## Guynmart Castle, Guynmart and 2 more (guynmart_horse) { #v-guynmart_horse }

**Entry ID:** `guynmart_horse` · **Type:** NPC

**Location:** Guynmart Castle: [Guynmart](../maps/guynmart.md#pin-npc-guynmart_horse), Guynmart Castle: [Guynmart wood 4](../maps/guynmart_wood_4.md#pin-npc-guynmart_horse), [Waytolake 11](../maps/waytolake11.md#pin-npc-guynmart_horse)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Guynmart](../maps/guynmart.md) | Guynmart Castle | 2 | – |
| [Guynmart wood 4](../maps/guynmart_wood_4.md) | Guynmart Castle | 4 | – |
| [Waytolake 11](../maps/waytolake11.md) | – | 1 | – |

### Dialogue simulator

Set your quest stages and items, then talk to Horse. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_horse_10.json" data-npc="Horse" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_horse-guynmart_horse_10"></span>**`guynmart_horse_10`** Horse: “Neigh.”




### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_horse)"

    | | |
    |---|---|
    | Entry ID | `guynmart_horse` |
    | Spawn group | `guynmart_horse` |
    | Loot table | – |
    | Conversation | `guynmart_horse_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:66` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_horse",
     "name": "Horse",
     "iconID": "monsters_ld2:66",
     "monsterClass": "animal",
     "phraseID": "guynmart_horse_10"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_horse.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_horse.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_horse.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_horse.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
