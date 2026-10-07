---
description: "Vilegard woman is a non-player character (NPC) in Andor's Trail, found in Vilegard. Starts Trusting an outsider."
---

# ![](../assets/icons/monsters/monsters_men_6.png){ .sprite } Vilegard woman

**Where to find Vilegard woman:** Vilegard: [vilegard_s](../maps/vilegard_s.md#pin-npc-vilegard_woman)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_6.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Starts [Trusting an outsider](../quests/vilegard.md) |
| **Found in** | Vilegard |
| **Entry ID** | `vilegard_woman` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [Trusting an outsider](../quests/vilegard.md): stage 10

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Vilegard woman. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/vilegard_villager_5.json" data-npc="Vilegard woman" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-vilegard_villager_5"></span>**`vilegard_villager_5`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 30 of [Trusting an outsider](../quests/vilegard.md#stage-30))* → [vilegard_villager_friend](#d-vilegard_villager_friend)
    - branch 2 → [vilegard_villager_5_0](#d-vilegard_villager_5_0)

    <span id="d-vilegard_villager_friend"></span>**`vilegard_villager_friend`** Vilegard woman: “Hello there. I heard you helped us common folk here in Vilegard. Please stay for as long as you like friend.”

    - “Thank you. Have you seen my brother Andor around here?” → [vilegard_villager_friend_1](#d-vilegard_villager_friend_1)
    - “Thank you. See you.” → *conversation ends*

    <span id="d-vilegard_villager_5_0"></span>**`vilegard_villager_5_0`** Vilegard woman: “Hello there outsider. You look lost, that's good. Now leave Vilegard while you can.”

    - “Why is everyone in Vilegard so afraid of outsiders?” → [vilegard_villager_5_1](#d-vilegard_villager_5_1)

    <span id="d-vilegard_villager_friend_1"></span>**`vilegard_villager_friend_1`** Vilegard woman: “Your brother? No, I haven't seen anyone that looks like you. But then again, I never take much notice to outsiders.”

    - “Thanks, bye.” → *conversation ends*

    <span id="d-vilegard_villager_5_1"></span>**`vilegard_villager_5_1`** Vilegard woman: “I don't trust you. You should go see Jolnor in the chapel if you want some sympathy.” — **effects:** sets stage 10 of [Trusting an outsider](../quests/vilegard.md#stage-10)




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `vilegard_woman` |
    | Spawn group | `vilegard_villager_5` |
    | Loot table | – |
    | Conversation | `vilegard_villager_5` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:6` |
    | Defined in | `res/raw/monsterlist_v068_npcs.json` |

    Raw data:

    ```json
    {
     "id": "vilegard_woman",
     "name": "Vilegard woman",
     "iconID": "monsters_men:6",
     "monsterClass": "humanoid",
     "spawnGroup": "vilegard_villager_5",
     "phraseID": "vilegard_villager_5"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vilegard_woman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vilegard_woman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vilegard_woman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vilegard_woman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
