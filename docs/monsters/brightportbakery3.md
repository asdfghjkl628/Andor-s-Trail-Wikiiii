# ![](../assets/icons/monsters/monsters_ld_edit_1.png){ .sprite } Gunther

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld_edit_1.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `brightportbakery3` |
| **Type** | Shopkeeper |
| **Class** | ? |
| **HP** | 1 |
| **Found in** | Brightport |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

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


## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Brightport bread](../items/brightport_bakery.md) | 100% | 5 |
| [Berry pie](../items/brightport_bakery1.md) | 100% | 2 |
| [Bread](../items/bread.md) | 100% | 10 |
| [Cake](../items/cake.md) | 100% | 1 |
| [Apple pie](../items/brightport_bakery2.md) | 100% | 3 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [brightport_bakery](../maps/brightport_bakery.md) | Brightport | 1 | – |


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Gunther. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_bakery3_selector.json" data-npc="Gunther" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightport_bakery3_selector"></span>**`brightport_bakery3_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 246 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-246))* → [brightport_bakery3](#d-brightport_bakery3)
    - Next *(if reached stage 246 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-246))* → [brightport_bakery3_behindcounter](#d-brightport_bakery3_behindcounter)

    <span id="d-brightport_bakery3"></span>**`brightport_bakery3`** [Gunther](../monsters/brightportbakery3.md): “Hello, and welcome to the world famous bakery of Brightport, how may I help you?”

    - “Please show me the menu.” → *shop opens*

    <span id="d-brightport_bakery3_behindcounter"></span>**`brightport_bakery3_behindcounter`** [Gunther](../monsters/brightportbakery3.md): “We don't serve people from behind the counter, please stand in front.”




## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportbakery3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportbakery3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportbakery3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportbakery3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `brightportbakery3` |
    | Spawn group | `brightportbakery3` |
    | Loot table | `brightport_bakery` |
    | Conversation | `brightport_bakery3_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld_edit:1` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportbakery3",
     "name": "Gunther",
     "iconID": "monsters_ld_edit:1",
     "unique": 1,
     "phraseID": "brightport_bakery3_selector",
     "droplistID": "brightport_bakery"
    }
    ```


<small>Data from v0.8.18</small>
