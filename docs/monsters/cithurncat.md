---
description: "Cithurn's cat is a non-player character (NPC) in Andor's Trail, found in Waterwaybhouse."
---

# ![](../assets/icons/monsters/monsters_ld2_103.png){ .sprite } Cithurn's cat

**Where to find Cithurn's cat:** [Waterwaybhouse](../maps/waterwaybhouse.md#pin-npc-cithurncat)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld2_103.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Waterwaybhouse |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Quests

- [General story flags 2 (hidden flag)](../quests/nondisplay_2.md): stage 100

## Dialogue simulator

Talk to Cithurn's cat as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/cithurncatmeow.json" data-npc="Cithurn&#x27;s cat" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-cithurncatmeow"></span>**`cithurncatmeow`** Cithurn's cat: “Meow ... Meow.”

    - “[You scratch the cat behind the ear]” *(if NOT reached stage 100 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-100))* → [cithurncatmeow_1](#d-cithurncatmeow_1)
    - “[You stroke the cat]” *(if NOT reached stage 100 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-100))* → [cithurncatmeow_2](#d-cithurncatmeow_2)

    <span id="d-cithurncatmeow_1"></span>**`cithurncatmeow_1`** Cithurn's cat: “Purr ... Purr.” — **effects:** sets stage 100 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-100)


    <span id="d-cithurncatmeow_2"></span>**`cithurncatmeow_2`** Cithurn's cat: “Purr ... Purr.” — **effects:** sets stage 100 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-100)




## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `cithurncat` |
    | Type (wiki) | NPC |
    | Spawn group | `cithurncat` |
    | Loot table | – |
    | Conversation | `cithurncatmeow` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:103` |
    | Defined in | `res/raw/monsterlist_graveyard1.json` |

    Raw data:

    ```json
    {
     "id": "cithurncat",
     "name": "Cithurn's cat",
     "iconID": "monsters_ld2:103",
     "unique": 1,
     "monsterClass": "animal",
     "spawnGroup": "cithurncat",
     "phraseID": "cithurncatmeow"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cithurncat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cithurncat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cithurncat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cithurncat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
