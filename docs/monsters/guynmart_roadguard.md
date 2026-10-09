---
description: "Feygard road guard is a non-player character (NPC) in Andor's Trail, found in Guynmart Castle."
---

# ![](../assets/icons/monsters/monsters_men2_4.png){ .sprite } Feygard road guard

**Where to find Feygard road guard:** Guynmart Castle: [Guynmart wood 13](../maps/guynmart_wood_13.md#pin-npc-guynmart_roadguard)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men2_4.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Guynmart Castle |
| **Entry ID** | `guynmart_roadguard` |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Dialogue simulator

Set your quest stages and items, then talk to Feygard road guard. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_roadguard_10.json" data-npc="Feygard road guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_roadguard_10"></span>**`guynmart_roadguard_10`** Feygard road guard: “Sorry, the road to Feygard is closed until further notice.”

    - “Oh? Is it the fog that is the problem?” → [guynmart_roadguard_20](#d-guynmart_roadguard_20)
    - “Why?” *(if reached stage 1 of [Feygard fog (hidden flag)](../quests/feygard_fog.md#stage-1))* → [guynmart_roadguard_12](#d-guynmart_roadguard_12)
    - “Why?” *(if reached stage 80 of [Fog in the woods](../quests/fogmonster.md#stage-80))* → [guynmart_roadguard_12](#d-guynmart_roadguard_12)

    <span id="d-guynmart_roadguard_20"></span>**`guynmart_roadguard_20`** Feygard road guard: “Yes. Several men already got lost and never reappeared. There is no way through.”

    - “But ... which fog?” *(if reached stage 1 of [Feygard fog (hidden flag)](../quests/feygard_fog.md#stage-1))* → [guynmart_roadguard_30](#d-guynmart_roadguard_30)

    <span id="d-guynmart_roadguard_12"></span>**`guynmart_roadguard_12`** Feygard road guard: “The fog over there is very dangerous.”

    - “Which fog? Do you ever look up?” → [guynmart_roadguard_30](#d-guynmart_roadguard_30)

    <span id="d-guynmart_roadguard_30"></span>**`guynmart_roadguard_30`** Feygard road guard: “Oh ... Forget it. I feel rather stupid now. Bye.” — **effects:** removes monsters from guynmart_wood_13




## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 2 lines added |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 2 lines added, 2 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `guynmart_roadguard` |
    | Spawn group | `guynmart_roadguard` |
    | Loot table | – |
    | Conversation | `guynmart_roadguard_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men2:4` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_roadguard",
     "name": "Feygard road guard",
     "iconID": "monsters_men2:4",
     "monsterClass": "humanoid",
     "phraseID": "guynmart_roadguard_10"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_roadguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_roadguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_roadguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_roadguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
