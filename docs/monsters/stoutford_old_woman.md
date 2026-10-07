# ![](../assets/icons/monsters/monsters_men_2.png){ .sprite } Croaklear

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_2.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `stoutford_old_woman` |
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
| [stoutford_tavern](../maps/stoutford_tavern.md) | Stoutford | 1 | – |


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Croaklear. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/stoutford_old_woman.json" data-npc="Croaklear" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (7 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-stoutford_old_woman"></span>**`stoutford_old_woman`** Croaklear: “So young and already hanging around in taverns?”

    - “No, I am looking for my brother Andor. Maybe you have seen him?” → [stoutford_old_woman_10](#d-stoutford_old_woman_10)
    - “At least I am not drinking whole bottles on my own, like that guy at the next table.” → [stoutford_old_woman_20](#d-stoutford_old_woman_20)

    <span id="d-stoutford_old_woman_10"></span>**`stoutford_old_woman_10`** Croaklear: “Yes, I have seen a boy that looks a bit like you. Not too long ago. But he is gone and I can not say where he was bound to.”

    - “What a pity. At least someone has seen him. Better than nothing.” → *conversation ends*

    <span id="d-stoutford_old_woman_20"></span>**`stoutford_old_woman_20`** Croaklear: “Well said. I hope for your sake that you will choose other amusements.”

    - “He looks rather well off. Who is he?” → [stoutford_old_woman_22](#d-stoutford_old_woman_22)

    <span id="d-stoutford_old_woman_22"></span>**`stoutford_old_woman_22`** Croaklear: “That is Lord Bourbon ... - I mean Lord Berbane of Stoutford. His name invites a nasty pun, but honestly, he does not do much to show a different character.”

    - Next → [stoutford_old_woman_30](#d-stoutford_old_woman_30)

    <span id="d-stoutford_old_woman_30"></span>**`stoutford_old_woman_30`** Croaklear: “Lord Bourbon sits there every evening, drinking or telling fairy tales. Or he plays his lute and sings to it. I must admit he has a reasonable voice.”

    - “He is the heir to Stoutford Castle?” → [stoutford_old_woman_40](#d-stoutford_old_woman_40)

    <span id="d-stoutford_old_woman_40"></span>**`stoutford_old_woman_40`** Croaklear: “Correct, although there is not much in the way of heirlooms left. And the castle is almost in ruins now, after the raid.”

    - Next → [stoutford_old_woman_50](#d-stoutford_old_woman_50)

    <span id="d-stoutford_old_woman_50"></span>**`stoutford_old_woman_50`** Croaklear: “And now you should run home and go to bed. Your parents should take better care of you and your brothers.”

    - “Phew.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 7 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_old_woman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_old_woman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_old_woman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_old_woman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `stoutford_old_woman` |
    | Spawn group | `stoutford_old_woman` |
    | Loot table | – |
    | Conversation | `stoutford_old_woman` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:2` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stoutford_old_woman",
     "name": "Croaklear",
     "iconID": "monsters_men:2",
     "spawnGroup": "stoutford_old_woman",
     "phraseID": "stoutford_old_woman"
    }
    ```


<small>Data from v0.8.18</small>
