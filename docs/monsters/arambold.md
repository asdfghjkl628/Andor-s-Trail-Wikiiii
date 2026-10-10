---
description: "Arambold is a non-player character (NPC) in Andor's Trail. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_men_3.png){ .sprite } Arambold

**Where to find Arambold:** appears during a quest or scripted event.

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_3.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Shopkeeper |
| **Introduced** | v0.7.0 or earlier |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Green hat](../items/hat1.md) | 100% | 1 |
| [Fine green hat](../items/hat2.md) | 100% | 1 |
| [Cloth shirt](../items/shirt1.md) | 100% | 1 |
| [Torn shirt](../items/shirt_torn.md) | 100% | 1 |
| [Gloves of fumbling](../items/gloves_fumbling.md) | 100% | 1 |
| [Fancy gloves](../items/gloves_fancy.md) | 100% | 1 |
| [Crude cloth gloves](../items/gloves_crude_cloth.md) | 100% | 1 |
| [Ring of damage +1](../items/ring_dmg1.md) | 100% | 1 |
| [Ring of damage +2](../items/ring_dmg2.md) | 100% | 1 |
| [Challenger's ring](../items/ring_challenger.md) | 100% | 1 |

## Dialogue simulator

Set your quest stages and items, then talk to Arambold. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/arambold1.json" data-npc="Arambold" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-arambold1"></span>**`arambold1`** Arambold: “Oh my, will I ever get any sleep with those drunkards singing like that? Someone should do something about them.”

    - “Can I rest here?” → [arambold2](#d-arambold2)
    - “Do you have anything to trade?” → *shop opens*

    <span id="d-arambold2"></span>**`arambold2`** Arambold: “Sure kid, you may rest here. Pick any bed you want.”

    - “Thanks, bye.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `arambold` |
    | Type (wiki) | NPC |
    | Spawn group | `arambold` |
    | Loot table | `shop_arambold` |
    | Conversation | `arambold1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:3` |
    | Defined in | `res/raw/monsterlist_crossglen_npcs.json` |

    Raw data:

    ```json
    {
     "id": "arambold",
     "name": "Arambold",
     "iconID": "monsters_men:3",
     "monsterClass": "humanoid",
     "spawnGroup": "arambold",
     "phraseID": "arambold1",
     "droplistID": "shop_arambold"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arambold.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arambold.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arambold.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arambold.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
