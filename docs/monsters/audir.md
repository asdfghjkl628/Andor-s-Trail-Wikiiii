---
description: "Audir is a non-player character (NPC) in Andor's Trail. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_men_0.png){ .sprite } Audir

**Where to find Audir:** appears during a quest or scripted event.

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Shopkeeper |
| **Introduced** | v0.7.0 or earlier |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Iron axe](../items/axe2.md) | 100% | 1 |
| [Black axe](../items/axe_black1.md) | 100% | 1 |
| [Wooden club](../items/club1.md) | 100% | 1 |
| [Crude iron sword](../items/ironsword0.md) | 100% | 1 |
| [Iron hammer](../items/hammer0.md) | 100% | 1 |
| [Iron club](../items/club3.md) | 100% | 1 |
| [Quarterstaff](../items/qtrstaff.md) | 100% | 1 |
| [Rusted iron sword](../items/rusted_iron_sword.md) | 100% | 1 |
| [Iron sword](../items/ironsword1.md) | 100% | 1 |
| [Iron broadsword](../items/broadsword1.md) | 100% | 1 |
| [Iron longsword](../items/ironsword2.md) | 100% | 1 |
| [Iron shortsword](../items/shortsword1.md) | 100% | 1 |
| [Hardened iron longsword](../items/longsword_hard_iron.md) | 100% | 1 |
| [Rusty claymore](../items/clmr_rst.md) | 100% | 1 |
| [Two-handed iron sword](../items/clmr_irn1.md) | 100% | 1 |
| [Broken wooden buckler](../items/broken_buckler.md) | 100% | 1 |
| [Crude wooden buckler](../items/shield_crude_wooden.md) | 100% | 1 |
| [Cracked wooden buckler](../items/shield_cracked_wooden.md) | 100% | 1 |
| [Second-hand wooden buckler](../items/shield_wooden_buckler.md) | 100% | 1 |
| [Reinforced wooden buckler](../items/shield3.md) | 100% | 1 |
| [Crude leather boots](../items/boots_crude_leather.md) | 100% | 1 |
| [Iron spear](../items/spear_iron.md) | 100% | 1 |
| [Rusty iron spear](../items/spear_rusty.md) | 100% | 1 |

## Quests

- [Yellow is it](../quests/ratdom_quest.md): stage 82

## Dialogue simulator

Set your quest stages and items, then talk to Audir. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/audir1.json" data-npc="Audir" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-audir1"></span>**`audir1`** Audir: “Welcome to my shop! Please browse my selection of fine wares.”

    - “Please show me your wares.” → *shop opens*
    - “Do you have a pickaxe by chance?” *(if reached stage 80 of [Yellow is it](../quests/ratdom_quest.md#stage-80); NOT reached stage 82 of [Yellow is it](../quests/ratdom_quest.md#stage-82))* → [ratdom_audir](#d-ratdom_audir)

    <span id="d-ratdom_audir"></span>**`ratdom_audir`** Audir: “Now that you mention it - yes. Long ago I made a good, sturdy pickaxe. But nobody wanted it for years, so I almost forgot it.”

    - Next → [ratdom_audir_1](#d-ratdom_audir_1)

    <span id="d-ratdom_audir_1"></span>**`ratdom_audir_1`** Audir: “You could have it for 80 pieces of gold.”

    - “Great, I'll take it.” *(if pay 80 gold)* → [ratdom_audir_2](#d-ratdom_audir_2)
    - “Hmm, I will think about it.” → *conversation ends*

    <span id="d-ratdom_audir_2"></span>**`ratdom_audir_2`** Audir: “Here you are.” — **effects:** sets stage 82 of [Yellow is it](../quests/ratdom_quest.md#stage-82), gives 1× [Pickhatchet](../items/ratdom_pickaxe.md)

    - “Thank you, bye.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.8.5](../versions/0.8.5.md) | Dialogue: 3 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `audir` |
    | Type (wiki) | NPC |
    | Spawn group | `audir` |
    | Loot table | `shop_audir` |
    | Conversation | `audir1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:0` |
    | Defined in | `res/raw/monsterlist_crossglen_npcs.json` |

    Raw data:

    ```json
    {
     "id": "audir",
     "name": "Audir",
     "iconID": "monsters_men:0",
     "monsterClass": "humanoid",
     "spawnGroup": "audir",
     "phraseID": "audir1",
     "droplistID": "shop_audir"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=audir.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=audir.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=audir.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=audir.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
