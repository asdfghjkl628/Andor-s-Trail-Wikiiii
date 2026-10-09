---
description: "Androni is a non-player character (NPC) in Andor's Trail, found in Brightport."
---

# ![](../assets/icons/monsters/monsters_ld1_23.png){ .sprite } Androni

**Where to find Androni:** Brightport: [Brightport bakery 1](../maps/brightport_bakery1.md#pin-npc-brightport_chef)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_23.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Brightport |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Quests

- [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md): stage 188

## Dialogue simulator

Set your quest stages and items, then talk to Androni. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_androni.json" data-npc="Androni" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightport_androni"></span>**`brightport_androni`** Androni: “Ah hello, like the smell?”

    - “Do you have butter or dough?” *(if reached stage 5 of [A Feygard delicacy](../quests/feygard_delicacy.md#stage-5))* → [brightport_androni1](#d-brightport_androni1)
    - “It's alright.” → *conversation ends*

    <span id="d-brightport_androni1"></span>**`brightport_androni1`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 188 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-188))* → [brightport_androni2](#d-brightport_androni2)
    - Next *(if NOT reached stage 188 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-188))* → [brightport_androni3](#d-brightport_androni3)

    <span id="d-brightport_androni2"></span>**`brightport_androni2`** Androni: “I already gave you some, don't be cheeky.”


    <span id="d-brightport_androni3"></span>**`brightport_androni3`** Androni: “You want some? Here, I have a bit left over after preparing a roulette cake. I wouldn't eat those raw if I were you.” — **effects:** sets stage 188 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-188), gives 1× [Raw dough](../items/dough.md), gives 1× [Butter](../items/butter.md)




## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightport_chef` |
    | Type (wiki) | NPC |
    | Spawn group | `brightport_chef` |
    | Loot table | – |
    | Conversation | `brightport_androni` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:23` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_chef",
     "name": "Androni",
     "iconID": "monsters_ld1:23",
     "phraseID": "brightport_androni"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_chef.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_chef.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_chef.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_chef.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
