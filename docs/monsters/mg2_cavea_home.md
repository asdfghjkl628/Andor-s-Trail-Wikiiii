---
description: "Oegyth crystal is a non-player character (NPC) in Andor's Trail, found in Mt. Galmore."
---

# ![](../assets/icons/monsters/items_misc_35.png){ .sprite } Oegyth crystal

**Where to find Oegyth crystal:** [Mt. Galmore, Galmore cavea 2](#v-mg2_cavea_home), [Mt. Galmore, Galmore cavea 2](#v-mg2_cavea_throdna)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/items_misc_35.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Mt. Galmore |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Mt. Galmore, Galmore cavea 2 { #v-mg2_cavea_home }

**Where:** Mt. Galmore: [Galmore cavea 2](../maps/galmore_cavea_2.md#pin-npc-mg2_cavea_home)

### Dialogue simulator

Set your quest stages and items, then talk to Oegyth crystal. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/mg2_cavea_home.json" data-npc="Oegyth crystal" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-mg2_cavea_home-mg2_cavea_home"></span>**`mg2_cavea_home`** Oegyth crystal: “You are watching Mikhail at home.” — **effects:** moves you to [Home](../maps/home.md)




### Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Mt. Galmore, Galmore cavea 2 (2) { #v-mg2_cavea_throdna }

**Where:** Mt. Galmore: [Galmore cavea 2](../maps/galmore_cavea_2.md#pin-npc-mg2_cavea_throdna)

### Dialogue simulator

Set your quest stages and items, then talk to Oegyth crystal. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/mg2_cavea_throdna.json" data-npc="Oegyth crystal" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-mg2_cavea_throdna-mg2_cavea_throdna"></span>**`mg2_cavea_throdna`** Oegyth crystal: “You are watching Throdna and his followers.” — **effects:** moves you to [Blackwater mountain 50](../maps/blackwater_mountain50.md)




### Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Oegyth crystal. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation.

| Entry | Type | Section |
|---|---|---|
| `mg2_cavea_home` | NPC | [Mt. Galmore, Galmore cavea 2](#v-mg2_cavea_home) |
| `mg2_cavea_throdna` | NPC | [Mt. Galmore, Galmore cavea 2](#v-mg2_cavea_throdna) |

??? info "Technical information: mg2_cavea_home"

    | | |
    |---|---|
    | Entry ID | `mg2_cavea_home` |
    | Type (wiki) | NPC |
    | Spawn group | `mg2_cavea_home` |
    | Loot table | – |
    | Conversation | `mg2_cavea_home` |
    | Faction | – |
    | Movement | – |
    | Icon | `items_misc:35` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "mg2_cavea_home",
     "name": "Oegyth crystal",
     "iconID": "items_misc:35",
     "monsterClass": "construct",
     "spawnGroup": "mg2_cavea_home",
     "phraseID": "mg2_cavea_home"
    }
    ```

??? info "Technical information: mg2_cavea_throdna"

    | | |
    |---|---|
    | Entry ID | `mg2_cavea_throdna` |
    | Type (wiki) | NPC |
    | Spawn group | `mg2_cavea_throdna` |
    | Loot table | – |
    | Conversation | `mg2_cavea_throdna` |
    | Faction | – |
    | Movement | – |
    | Icon | `items_misc:35` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "mg2_cavea_throdna",
     "name": "Oegyth crystal",
     "iconID": "items_misc:35",
     "monsterClass": "construct",
     "spawnGroup": "mg2_cavea_throdna",
     "phraseID": "mg2_cavea_throdna"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_cavea_home.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_cavea_home.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_cavea_home.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_cavea_home.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
