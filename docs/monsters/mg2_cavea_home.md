---
description: "Oegyth crystal is a non-player character (NPC) in Andor's Trail, found in Mt. Galmore."
---

# ![](../assets/icons/monsters/items_misc_35.png){ .sprite } Oegyth crystal

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/items_misc_35.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Mt. Galmore |
| **Entries in game data** | 2 |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Oegyth crystal. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`mg2_cavea_home`](#v-mg2_cavea_home) | NPC | Mt. Galmore: [galmore_cavea_2](../maps/galmore_cavea_2.md#pin-npc-mg2_cavea_home) | – |
| [`mg2_cavea_throdna`](#v-mg2_cavea_throdna) | NPC | Mt. Galmore: [galmore_cavea_2](../maps/galmore_cavea_2.md#pin-npc-mg2_cavea_throdna) | – |

## Mt. Galmore, Galmore cavea 2 (mg2_cavea_home) { #v-mg2_cavea_home }

**Entry ID:** `mg2_cavea_home` · **Type:** NPC

**Location:** Mt. Galmore: [galmore_cavea_2](../maps/galmore_cavea_2.md#pin-npc-mg2_cavea_home)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Oegyth crystal. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/mg2_cavea_home.json" data-npc="Oegyth crystal" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-mg2_cavea_home-mg2_cavea_home"></span>**`mg2_cavea_home`** Oegyth crystal: “You are watching Mikhail at home.” — **effects:** moves you to [home](../maps/home.md)




### Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (mg2_cavea_home)"

    | | |
    |---|---|
    | Entry ID | `mg2_cavea_home` |
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


## Mt. Galmore, Galmore cavea 2 (mg2_cavea_throdna) { #v-mg2_cavea_throdna }

**Entry ID:** `mg2_cavea_throdna` · **Type:** NPC

**Location:** Mt. Galmore: [galmore_cavea_2](../maps/galmore_cavea_2.md#pin-npc-mg2_cavea_throdna)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Oegyth crystal. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/mg2_cavea_throdna.json" data-npc="Oegyth crystal" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-mg2_cavea_throdna-mg2_cavea_throdna"></span>**`mg2_cavea_throdna`** Oegyth crystal: “You are watching Throdna and his followers.” — **effects:** moves you to [blackwater_mountain50](../maps/blackwater_mountain50.md)




### Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (mg2_cavea_throdna)"

    | | |
    |---|---|
    | Entry ID | `mg2_cavea_throdna` |
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
