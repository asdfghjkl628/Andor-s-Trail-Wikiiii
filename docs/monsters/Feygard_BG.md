---
description: "Feygard barricade guard is a non-player character (NPC) in Andor's Trail, found in Foaming Flask Tavern."
---

# ![](../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite } Feygard barricade guard

**Where to find Feygard barricade guard:** Foaming Flask Tavern: [road1](../maps/road1.md#pin-npc-Feygard_BG)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Foaming Flask Tavern |
| **Entry ID** | `Feygard_BG` |
| **Introduced** | [v0.7.8](../versions/0.7.8.md) |

</div>

## Quests

- [The ruthless Crackshot](../quests/Thieves03.md): stage 20

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Feygard barricade guard. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/Feygard_BG_selector.json" data-npc="Feygard barricade guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (9 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-Feygard_BG_selector"></span>**`Feygard_BG_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 15 of [The ruthless Crackshot](../quests/Thieves03.md#stage-15))* → [Feygard_BG_guild03_0](#d-Feygard_BG_guild03_0)
    - branch 2 → [Feygard_BG_guild02_1](#d-Feygard_BG_guild02_1)

    <span id="d-Feygard_BG_guild03_0"></span>**`Feygard_BG_guild03_0`** Feygard barricade guard: “Halt! The road to Fallhaven is closed due to a murder committed three days ago.”

    - “Hey! I live in Crossglen. How do you expect me to get there?” → [Feygard_BG_guild03_1](#d-Feygard_BG_guild03_1)

    <span id="d-Feygard_BG_guild02_1"></span>**`Feygard_BG_guild02_1`** Feygard barricade guard: “Halt! The road to Fallhaven is closed due to recent information about a dangerous criminal who has been seen not far from here. That criminal committed a murder only hours ago.”

    - “But I really need to pass!” → [Feygard_BG_guild02_2a](#d-Feygard_BG_guild02_2a)

    <span id="d-Feygard_BG_guild03_1"></span>**`Feygard_BG_guild03_1`** Feygard barricade guard: “Sorry, kid! I'm unable to let you pass. Orders from above!”

    - “Any news about the murderer?” *(if NOT reached stage 20 of [The ruthless Crackshot](../quests/Thieves03.md#stage-20))* → [Feygard_BG_guild03_2](#d-Feygard_BG_guild03_2)
    - “Tsch, Bye!” → *conversation ends*

    <span id="d-Feygard_BG_guild02_2a"></span>**`Feygard_BG_guild02_2a`** Feygard barricade guard: “Sorry, I'm not able to decide who passes. This barricade will be here until we catch or kill the criminal. (You take a look into your map. There seems to be another way to reach Fallhaven, heading up to the North)”

    - “OK, thank you anyway.” → *conversation ends*

    <span id="d-Feygard_BG_guild03_2"></span>**`Feygard_BG_guild03_2`** Feygard barricade guard: “Yes. He's not alone!”

    - “Anything more?” → [Feygard_BG_guild03_3](#d-Feygard_BG_guild03_3)

    <span id="d-Feygard_BG_guild03_3"></span>**`Feygard_BG_guild03_3`** Feygard barricade guard: “Yes! We have sent patrols to the north. There's a place infested by larval burrowers.”

    - Next → [Feygard_BG_guild03_4](#d-Feygard_BG_guild03_4)

    <span id="d-Feygard_BG_guild03_4"></span>**`Feygard_BG_guild03_4`** Feygard barricade guard: “He and the other criminals are probably hiding there!”

    - “Anything else?” → [Feygard_BG_guild03_5](#d-Feygard_BG_guild03_5)

    <span id="d-Feygard_BG_guild03_5"></span>**`Feygard_BG_guild03_5`** Feygard barricade guard: “Yes! Those crimin ... Wait, you don't have to know this information! Forget everything I've said!” — **effects:** sets stage 20 of [The ruthless Crackshot](../quests/Thieves03.md#stage-20), changes map woodcave0

    - “I will, bye!” → *conversation ends*
    - “[Lie]I will!” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added<br>Dialogue: 9 lines added |
| [v0.7.9](../versions/0.7.9.md) | Dialogue: 2 lines changed<br>· text: “Halt! The road to Fallhaven is closed due to recent information about…” → “Halt! The road to Fallhaven is closed due to recent information about…”<br>· text: “Halt! The road to Fallhaven is closed due to a murder commited three …” → “Halt! The road to Fallhaven is closed due to a murder committed three…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `Feygard_BG` |
    | Spawn group | `Feygard_BG` |
    | Loot table | – |
    | Conversation | `Feygard_BG_selector` |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_rltiles3:14` |
    | Defined in | `res/raw/monsterlist_omicronrg9.json` |

    Raw data:

    ```json
    {
     "id": "Feygard_BG",
     "name": "Feygard barricade guard",
     "iconID": "monsters_rltiles3:14",
     "monsterClass": "humanoid",
     "movementAggressionType": "protectSpawn",
     "spawnGroup": "Feygard_BG",
     "phraseID": "Feygard_BG_selector"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=Feygard_BG.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=Feygard_BG.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=Feygard_BG.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=Feygard_BG.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
