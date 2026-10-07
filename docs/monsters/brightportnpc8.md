---
description: "Janwick is a non-player character (NPC) in Andor's Trail, found in Brightport."
---

# ![](../assets/icons/monsters/monsters_karvis2_5.png){ .sprite } Janwick

**Where to find Janwick:** Brightport: [Brightport stanwick](../maps/brightport_stanwick.md#pin-npc-brightportnpc8)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_karvis2_5.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Brightport |
| **Entry ID** | `brightportnpc8` |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Quests

- [No rest for the wicked](../quests/Stanwickquest.md): stage 10
- [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md): stage 248

## Dialogue simulator

Set your quest stages and items, then talk to Janwick. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_janwick_selector.json" data-npc="Janwick" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (6 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightport_janwick_selector"></span>**`brightport_janwick_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 10 of [No rest for the wicked](../quests/Stanwickquest.md#stage-10))* → [brightport_janwick](#d-brightport_janwick)
    - Next *(if reached stage 10 of [No rest for the wicked](../quests/Stanwickquest.md#stage-10))* → [brightport_janwick4](#d-brightport_janwick4)

    <span id="d-brightport_janwick"></span>**`brightport_janwick`** [Janwick](../monsters/brightportnpc8.md): “Where did I put my glasses? Was it here... or maybe over there?”

    - Next *(if reached stage 110 of [Search for Andor](../quests/andor.md#stage-110))* → [brightport_janwick1](#d-brightport_janwick1)

    <span id="d-brightport_janwick4"></span>**`brightport_janwick4`** Janwick: “My eyesight's not what it was...”

    - “Do you know anyone by the name of Bryma?” *(if reached stage 55 of [No rest for the wicked](../quests/Stanwickquest.md#stage-55); NOT reached stage 60 of [No rest for the wicked](../quests/Stanwickquest.md#stage-60))* → [brightport_janwick3](#d-brightport_janwick3)

    <span id="d-brightport_janwick1"></span>**`brightport_janwick1`** Janwick: “Oh, it's you, Andor! Even without my glasses, I can tell you haven't changed a bit. Here to visit Stanwick, I see.”

    - Next → [brightport_janwick2](#d-brightport_janwick2)

    <span id="d-brightport_janwick3"></span>**`brightport_janwick3`** Janwick: “It sounds familiar, but I struggle a bit with my memory. Go and ask my good friend Richimor, his house is right next to ours.” — **effects:** sets stage 248 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-248)


    <span id="d-brightport_janwick2"></span>**`brightport_janwick2`** Janwick: “He's at the academy, as always. Here, take these fruits with you and give them to him for me, would you?” — **effects:** sets stage 10 of [No rest for the wicked](../quests/Stanwickquest.md#stage-10), gives 1× [Fresh fruit for Stanwick](../items/brightport_fruit.md)




## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 6 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightportnpc8` |
    | Spawn group | `brightportnpc8` |
    | Loot table | – |
    | Conversation | `brightport_janwick_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:5` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportnpc8",
     "name": "Janwick",
     "iconID": "monsters_karvis2:5",
     "phraseID": "brightport_janwick_selector"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc8.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc8.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc8.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc8.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
