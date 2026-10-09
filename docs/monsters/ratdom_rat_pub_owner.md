---
description: "Horfael is a non-player character (NPC) in Andor's Trail, found in Pub. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_ld1_9.png){ .sprite } Horfael

**Where to find Horfael:** Pub: [Ratdom maze 705](../maps/ratdom_maze_705.md#pin-npc-ratdom_rat_pub_owner)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_9.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Shopkeeper |
| **Found in** | Pub |
| **Entry ID** | `ratdom_rat_pub_owner` |
| **Introduced** | [v0.8.5](../versions/0.8.5.md) |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Cooked snake meat](../items/snake_meat_cooked.md) | 100% | 5 to 10 |
| [Wine](../items/guynmart_wine.md) | 100% | 5 |
| [Charwood cheddar](../items/charwood_cheddar.md) | 100% | 2 |
| [Fermented garlic](../items/ferm-garlic.md) | 80% | 1 to 3 |
| [Mead](../items/mead.md) | 100% | 5 |

## Dialogue simulator

Set your quest stages and items, then talk to Horfael. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/ratdom_rat_pub_owner.json" data-npc="Horfael" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-ratdom_rat_pub_owner"></span>**`ratdom_rat_pub_owner`** Horfael: “Hi, have a drink?”

    - “You are running a pub here?” → [ratdom_rat_pub_owner_10](#d-ratdom_rat_pub_owner_10)

    <span id="d-ratdom_rat_pub_owner_10"></span>**`ratdom_rat_pub_owner_10`** Horfael: “Yes, I've always wanted that. Only my customers are usually a bit special.”

    - “I see.” → [ratdom_rat_pub_owner_20](#d-ratdom_rat_pub_owner_20)

    <span id="d-ratdom_rat_pub_owner_20"></span>**`ratdom_rat_pub_owner_20`** Horfael: “They are very picky, especially when it comes to food. For example, nobody has ordered anything today.”

    - “What are you offering?” → *shop opens*



## Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `ratdom_rat_pub_owner` |
    | Spawn group | `ratdom_rat_pub_owner` |
    | Loot table | `ratdom_rat_pub_owner` |
    | Conversation | `ratdom_rat_pub_owner` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:9` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_rat_pub_owner",
     "name": "Horfael",
     "iconID": "monsters_ld1:9",
     "phraseID": "ratdom_rat_pub_owner",
     "droplistID": "ratdom_rat_pub_owner"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_rat_pub_owner.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_rat_pub_owner.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_rat_pub_owner.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_rat_pub_owner.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
