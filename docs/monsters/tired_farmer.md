# ![](../assets/icons/monsters/monsters_man1_0.png){ .sprite } Tired farmer

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_man1_0.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `tired_farmer` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Crossglen |
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
| [crossglen](../maps/crossglen.md) | Crossglen | 1 | – |


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Tired farmer. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/farm2.json" data-npc="Tired farmer" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-farm2"></span>**`farm2`** Tired farmer: “What?! Can't you see I'm busy? Go bother someone else.”

    - “Have you seen my brother Andor?” → [farm_andor](#d-farm_andor)
    - “What happened to Leta and Oromir?” *(if reached stage 70 of [A familiar shadow](../quests/familiar_shadow.md#stage-70))* → [farmer2_old_leta](#d-farmer2_old_leta)

    <span id="d-farm_andor"></span>**`farm_andor`** Tired farmer: “Andor? No, I haven't seen him around lately.”


    <span id="d-farmer2_old_leta"></span>**`farmer2_old_leta`** Tired farmer: “They weren't like that yesterday. I saw Leta in the fields, tending to her garden, just as spry as ever. Then this morning...well, you've seen it yourself.”

    - “Did either of them say anything to you? About what happened?” → [farmer2_old_leta_20](#d-farmer2_old_leta_20)

    <span id="d-farmer2_old_leta_20"></span>**`farmer2_old_leta_20`** Tired farmer: “[shaking his head, grim] Not a word. Just that vacant smile of hers, like everything's fine. Oromir, though...he's got this strange look in his eye. Like he knows something we don't.”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.8.14](../versions/0.8.14.md) | Dialogue: 2 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tired_farmer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tired_farmer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tired_farmer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tired_farmer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `tired_farmer` |
    | Spawn group | `crossglen_farmer2` |
    | Loot table | – |
    | Conversation | `farm2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_man1:0` |
    | Defined in | `res/raw/monsterlist_crossglen_npcs.json` |

    Raw data:

    ```json
    {
     "id": "tired_farmer",
     "name": "Tired farmer",
     "iconID": "monsters_man1:0",
     "monsterClass": "humanoid",
     "spawnGroup": "crossglen_farmer2",
     "phraseID": "farm2"
    }
    ```


<small>Data from v0.8.18</small>
