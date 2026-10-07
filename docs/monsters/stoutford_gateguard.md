# ![](../assets/icons/monsters/monsters_tometik2_43.png){ .sprite } Stoutford guard

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik2_43.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `stoutford_gateguard` |
| **Type** | NPC |
| **Class** | ? |
| **HP** | 1 |
| **Found in** | Stoutford |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [wild20](../maps/wild20.md) | Stoutford | 2 | – |


## Quests

- [Search for Andor](../quests/andor.md): stages 85

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Stoutford guard. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/stoutford_gateguard_0.json" data-npc="Stoutford guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (10 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-stoutford_gateguard_0"></span>**`stoutford_gateguard_0`** Stoutford guard: “What do you want kid?”

    - “What is this place?” → [soutford_gateguard_what_0](#d-soutford_gateguard_what_0)
    - “What are you doing here?” → [soutford_gateguard_who_0](#d-soutford_gateguard_who_0)
    - “Have you seen my brother Andor?” → [stoutford_gateguard_andor_0](#d-stoutford_gateguard_andor_0)

    <span id="d-soutford_gateguard_what_0"></span>**`soutford_gateguard_what_0`** Stoutford guard: “This is Stoutford. Our small town was the resting place of choice for many merchants on their way between Fallhaven and the Blackwater mountain.”

    - “Was?” → [soutford_gateguard_what_1](#d-soutford_gateguard_what_1)

    <span id="d-soutford_gateguard_who_0"></span>**`soutford_gateguard_who_0`** Stoutford guard: “I'm guarding the town's gate.”

    - “Guarding against what?” → [soutford_gateguard_who_1](#d-soutford_gateguard_who_1)

    <span id="d-stoutford_gateguard_andor_0"></span>**`stoutford_gateguard_andor_0`** Stoutford guard: “I do recall some kid that looked a bit like you a while ago. He stayed here a couple of days, and never came back as far as I can tell.” — **effects:** sets stage 85 of [Search for Andor](../quests/andor.md#stage-85)

    - “What did he do here?” → [stoutford_gateguard_andor_1](#d-stoutford_gateguard_andor_1)
    - “Do you know where he was going?” → [stoutford_gateguard_andor_2](#d-stoutford_gateguard_andor_2)

    <span id="d-soutford_gateguard_what_1"></span>**`soutford_gateguard_what_1`** Stoutford guard: “Yes. It seems the road is closed for some reason. Maybe this is related to the monster attacks we have been suffering from recently.”

    - “Is there anything I can do to help?” → [soutford_gateguard_what_2](#d-soutford_gateguard_what_2)
    - “Whatever...” → *conversation ends*

    <span id="d-soutford_gateguard_who_1"></span>**`soutford_gateguard_who_1`** Stoutford guard: “In the past, troublemakers that bothered the citizens or merchants. Nowadays, it's mainly the monsters, when I can handle them.”

    - “What monsters?” → [soutford_gateguard_who_2](#d-soutford_gateguard_who_2)
    - “Pathetic...” → *conversation ends*

    <span id="d-stoutford_gateguard_andor_1"></span>**`stoutford_gateguard_andor_1`** Stoutford guard: “I can't really tell. No known trouble at least. He headed straight to the tavern, and I didn't see him again before he left.”

    - “Do you know where he was going?” → [stoutford_gateguard_andor_2](#d-stoutford_gateguard_andor_2)
    - “I have other questions...” → [stoutford_gateguard_0](#d-stoutford_gateguard_0)
    - “Thank you.” → *conversation ends*

    <span id="d-stoutford_gateguard_andor_2"></span>**`stoutford_gateguard_andor_2`** Stoutford guard: “No.”

    - “What did he do here?” → [stoutford_gateguard_andor_1](#d-stoutford_gateguard_andor_1)
    - “I have other questions...” → [stoutford_gateguard_0](#d-stoutford_gateguard_0)
    - “Thank you.” → *conversation ends*

    <span id="d-soutford_gateguard_what_2"></span>**`soutford_gateguard_what_2`** Stoutford guard: “I don't know. You look very young. Try talking to our priest.”

    - “I have other questions...” → [stoutford_gateguard_0](#d-stoutford_gateguard_0)
    - “Thank you.” → *conversation ends*

    <span id="d-soutford_gateguard_who_2"></span>**`soutford_gateguard_who_2`** Stoutford guard: “You should talk to our priest about that.”

    - “I have other questions...” → [stoutford_gateguard_0](#d-stoutford_gateguard_0)
    - “Thank you.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 10 lines added |
| [v0.7.4](../versions/0.7.4.md) | Dialogue: 1 line changed<br>· text: “This is Stoutford. Our small town was the resting place of choice for…” → “This is Stoutford. Our small town was the resting place of choice for…” |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_gateguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_gateguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_gateguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_gateguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `stoutford_gateguard` |
    | Spawn group | `stoutford_gateguard` |
    | Loot table | – |
    | Conversation | `stoutford_gateguard_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik2:43` |
    | Defined in | `res/raw/monsterlist_stoutford.json` |

    Raw data:

    ```json
    {
     "id": "stoutford_gateguard",
     "name": "Stoutford guard",
     "iconID": "monsters_tometik2:43",
     "phraseID": "stoutford_gateguard_0"
    }
    ```


<small>Data from v0.8.18</small>
