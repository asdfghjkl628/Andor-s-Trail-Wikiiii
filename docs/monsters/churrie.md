---
description: "Churrie is a non-player character (NPC) in Andor's Trail, found in Loneford."
---

# ![](../assets/icons/monsters/monsters_ld1_184.png){ .sprite } Churrie

**Where to find Churrie:** Loneford: [Waytobrimhaven 2](../maps/waytobrimhaven2.md#pin-npc-churrie)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_184.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Loneford |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

## Quests

- [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md): stage 87

## Dialogue simulator

Set your quest stages and items, then talk to Churrie. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/churrie.json" data-npc="Churrie" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-churrie"></span>**`churrie`** Churrie: “Attention, kid! This is a dangerous place.”

    - “Why? It looks lovely here.” → [churrie_10](#d-churrie_10)

    <span id="d-churrie_10"></span>**`churrie_10`** Churrie: “There are dangerous creatures in the hole down there. I fear that they'll come out again.”

    - “Then I wish the dry lake was full of water again. It would keep the monsters from coming out.” → [churrie_20](#d-churrie_20)

    <span id="d-churrie_20"></span>**`churrie_20`** Churrie: “Indeed. I would see to it, if I had enough money.”

    - “What has money to do with it? I better go.” → *conversation ends*
    - “It should not fail because of a lack of money. Here you have 2,500 gold.” *(if pay 2,500 gold)* → [churrie_30](#d-churrie_30)

    <span id="d-churrie_30"></span>**`churrie_30`** Churrie: “Oh, wow! I will take care of it. So much money! Probably tonight ...” — **effects:** sets stage 87 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-87)




## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 4 lines added |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `churrie` |
    | Type (wiki) | NPC |
    | Spawn group | `churrie` |
    | Loot table | – |
    | Conversation | `churrie` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:184` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "churrie",
     "name": "Churrie",
     "iconID": "monsters_ld1:184",
     "moveCost": 5,
     "monsterClass": "humanoid",
     "spawnGroup": "churrie",
     "phraseID": "churrie"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=churrie.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=churrie.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=churrie.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=churrie.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
