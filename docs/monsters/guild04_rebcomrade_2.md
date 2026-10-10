---
description: "Grabby comrade is a non-player character (NPC) in Andor's Trail, found in Sullengard."
---

# ![](../assets/icons/monsters/monsters_ld1_65.png){ .sprite } Grabby comrade

**Where to find Grabby comrade:** Sullengard: [Sullengard tavern basement](../maps/sullengard_tavern_basement.md#pin-npc-guild04_rebcomrade_2)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_65.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Sullengard |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Dialogue simulator

Set your quest stages and items, then talk to Grabby comrade. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/smuggler6_1.json" data-npc="Grabby comrade" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-smuggler6_1"></span>**`smuggler6_1`** Grabby comrade: “Can you spare some gold?”

    - “Get away from me!” → *conversation ends*
    - “Here's 5 gold.” *(if pay 5 gold)* → [smuggler6_3](#d-smuggler6_3)
    - “Here's 50 gold.” *(if pay 50 gold)* → [smuggler6_3](#d-smuggler6_3)
    - “Here's 100 gold.” *(if pay 100 gold)* → [smuggler6_2](#d-smuggler6_2)

    <span id="d-smuggler6_3"></span>**`smuggler6_3`** Grabby comrade: “Is that all you have?”


    <span id="d-smuggler6_2"></span>**`smuggler6_2`** Grabby comrade: “Oh, oh! I haven't seen that much gold in my whole life. I'm finally rich!”




## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added |
| [v0.8.8](../versions/0.8.8.md) | Attack chance: removed (was 110)<br>Attack cost: removed (was 5)<br>Attack damage: removed (was 5–10)<br>Block chance: removed (was 100)<br>Critical multiplier: removed (was 2)<br>Critical skill: removed (was 10)<br>Damage resistance: removed (was 2)<br>Loot table removed<br>Max HP: removed (was 70)<br>Move cost: removed (was 5) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `guild04_rebcomrade_2` |
    | Type (wiki) | NPC |
    | Spawn group | `guild04_comrade_2` |
    | Loot table | – |
    | Conversation | `smuggler6_1` |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_ld1:65` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "guild04_rebcomrade_2",
     "name": "Grabby comrade",
     "iconID": "monsters_ld1:65",
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "helpOthers",
     "spawnGroup": "guild04_comrade_2",
     "phraseID": "smuggler6_1"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guild04_rebcomrade_2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guild04_rebcomrade_2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guild04_rebcomrade_2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guild04_rebcomrade_2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
