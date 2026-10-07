---
description: "Ganos is a non-player character (NPC) in Andor's Trail. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_rogue1_0.png){ .sprite } Ganos

**Where to find Ganos:** not placed on any map; appears through a quest or scripted event.

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rogue1_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Shopkeeper |
| **Entry ID** | `ganos` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Iron dagger](../items/dagger0.md) | 100% | 1 |
| [Sharp iron dagger](../items/dagger1.md) | 100% | 1 |
| [Sharp steel dagger](../items/dagger_sharp_steel.md) | 100% | 1 |
| [Weathered shirt](../items/shirt_weathered.md) | 100% | 1 |
| [Patched cloth shirt](../items/shirt_patched_cloth.md) | 100% | 1 |
| [Gloves of swift attack](../items/gloves_attack1.md) | 100% | 1 |
| [Gloves of better grip](../items/gloves_grip.md) | 100% | 1 |
| [Superior leather boots](../items/boots2.md) | 100% | 1 |
| [Necklace of strike](../items/necklace_strike.md) | 100% | 1 |
| [Ring of strike](../items/ring_crit1.md) | 100% | 1 |
| [Ring of damage +2](../items/ring_dmg2.md) | 100% | 1 |
| [Tavern brawler's ring](../items/ring_taverbrawler.md) | 100% | 1 |
| [Ring of damage +4](../items/ring_dmg_4.md) | 100% | 1 |
| [Polished gem](../items/gem3.md) | 100% | 5 |
| [Assassin's gloves](../items/gloves_critical.md) | 100% | 1 |

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Ganos. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/ganos.json" data-npc="Ganos" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ganos"></span>**`ganos`** Ganos: “You seem familiar somehow.”

    - “Do you have anything to trade?” → *shop opens*
    - “Do you know anything about the Thieves' Guild?” *(if reached stage 30 of [Search for Andor](../quests/andor.md#stage-30))* → [ganos_1](#d-ganos_1)

    <span id="d-ganos_1"></span>**`ganos_1`** Ganos: “Thieves' Guild? How would I know? Do I look like a thief to you?! Hrmpf.”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `ganos` |
    | Spawn group | `ganos` |
    | Loot table | `shop_ganos` |
    | Conversation | `ganos` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rogue1:0` |
    | Defined in | `res/raw/monsterlist_fallhaven_npcs.json` |

    Raw data:

    ```json
    {
     "id": "ganos",
     "name": "Ganos",
     "iconID": "monsters_rogue1:0",
     "monsterClass": "humanoid",
     "spawnGroup": "ganos",
     "phraseID": "ganos",
     "droplistID": "shop_ganos"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ganos.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ganos.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ganos.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ganos.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
