# ![](../assets/icons/monsters/monsters_rltiles1_76.png){ .sprite } Guard

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_76.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `crossroads_backguard` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Crossroads Guardhouse |
| **Introduced** | v0.7.0 or earlier |

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
| [houseatcrossroads1](../maps/houseatcrossroads1.md) | Crossroads Guardhouse | 1 | – |


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Guard. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/crossroads_backguard.json" data-npc="Guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (11 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-crossroads_backguard"></span>**`crossroads_backguard`** Guard: “Uh, hello.”

    - “Hello. What's back there?” → [crossroads_backguard_1](#d-crossroads_backguard_1)

    <span id="d-crossroads_backguard_1"></span>**`crossroads_backguard_1`** Guard: “Back there? Oh, nothing.”

    - “OK, never mind then.” → *conversation ends*
    - “But there's a hole in the wall there. Where does it lead?” → [crossroads_backguard_2](#d-crossroads_backguard_2)

    <span id="d-crossroads_backguard_2"></span>**`crossroads_backguard_2`** Guard: “Lead? Oh nowhere. Nothing back there at all.”

    - “OK, never mind then.” → *conversation ends*
    - “There's something you are not telling me.” → [crossroads_backguard_3](#d-crossroads_backguard_3)

    <span id="d-crossroads_backguard_3"></span>**`crossroads_backguard_3`** Guard: “Oh no, no. Nothing interesting here. Move along now.”

    - “OK, never mind then.” → *conversation ends*
    - “How about I pay you 100 gold to move out of the way?” → [crossroads_backguard_4](#d-crossroads_backguard_4)

    <span id="d-crossroads_backguard_4"></span>**`crossroads_backguard_4`** Guard: “You would do that? Hmm, let me think.”

    - Next → [crossroads_backguard_5](#d-crossroads_backguard_5)

    <span id="d-crossroads_backguard_5"></span>**`crossroads_backguard_5`** Guard: “No.”

    - “OK, never mind then.” → *conversation ends*
    - “200 gold then?” → [crossroads_backguard_6](#d-crossroads_backguard_6)

    <span id="d-crossroads_backguard_6"></span>**`crossroads_backguard_6`** Guard: “No.”

    - “OK, never mind then.” → *conversation ends*
    - “400 gold then?” → [crossroads_backguard_7](#d-crossroads_backguard_7)

    <span id="d-crossroads_backguard_7"></span>**`crossroads_backguard_7`** Guard: “Look, you are not getting back there, and there is nothing to see back there.”

    - “OK, never mind then.” → *conversation ends*
    - “OK, final offer, 800 gold? That's a fortune.” → [crossroads_backguard_8](#d-crossroads_backguard_8)

    <span id="d-crossroads_backguard_8"></span>**`crossroads_backguard_8`** Guard: “Hmm, 800 gold you say? Well, why didn't you say so from the start? Sure, that could work.”

    - Next → [crossroads_backguard_9](#d-crossroads_backguard_9)

    <span id="d-crossroads_backguard_9"></span>**`crossroads_backguard_9`** Guard: “I should tell you however, that there is something in there that we won't dare go near. I just guard here to make sure it doesn't get out, and that no one goes in.”

    - Next → [crossroads_backguard_10](#d-crossroads_backguard_10)

    <span id="d-crossroads_backguard_10"></span>**`crossroads_backguard_10`** Guard: “Some other guards went in there earlier, and came back screaming. Enter at your own risk, but don't say I didn't warn you.”

    - “Never mind, I was just kidding.” → *conversation ends*
    - “Here is the gold, now get out of the way.” *(if pay 800 gold)* → *NPC leaves*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 8 lines changed<br>· text: “Hm, 800 gold you say? Well, why didn't you say so from the start? Sur…” → “Hmm, 800 gold you say? Well, why didn't you say so from the start? Su…”<br>· text: “You would do that? Hm, let me think.” → “You would do that? Hmm, let me think.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=crossroads_backguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=crossroads_backguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=crossroads_backguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=crossroads_backguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `crossroads_backguard` |
    | Spawn group | `crossroads_backguard` |
    | Loot table | – |
    | Conversation | `crossroads_backguard` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:76` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "crossroads_backguard",
     "name": "Guard",
     "iconID": "monsters_rltiles1:76",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "crossroads_backguard",
     "phraseID": "crossroads_backguard"
    }
    ```


<small>Data from v0.8.18</small>
