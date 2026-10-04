# ![](../assets/icons/monsters/items_japozero_387.png){ .sprite } Glade key

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/items_japozero_387.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `lakecave2_key` |
| **Type** | NPC |
| **Class** | ? |
| **HP** | 1 |
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


## Quests

- [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md): stages 210, 211

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Glade key. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/lakecave2_key_check2.json" data-npc="Glade key" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-lakecave2_key_check2"></span>**`lakecave2_key_check2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if 1 rounds passed since timer “lakecave2_timer_keycheck”)* → [lakecave2_key_check2_10](#d-lakecave2_key_check2_10)
    - branch 2 *(if NOT reached stage 210 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-210))* → [lakecave2_key_check2_20](#d-lakecave2_key_check2_20)
    - branch 3 → [lakecave2_key_check2_90](#d-lakecave2_key_check2_90)

    <span id="d-lakecave2_key_check2_10"></span>**`lakecave2_key_check2_10`** [Dummy NPC](../monsters/none.md): “You may be a great warrior, but you are not a tall one. Maybe a jump with a runup?” — **effects:** clears stage 210 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-210)


    <span id="d-lakecave2_key_check2_20"></span>**`lakecave2_key_check2_20`** [Dummy NPC](../monsters/none.md): “That was close - just half an inch short. Try again!” — **effects:** sets stage 210 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-210)


    <span id="d-lakecave2_key_check2_90"></span>**`lakecave2_key_check2_90`** [Dummy NPC](../monsters/none.md): “You got hold of the shelves and tore them down!” — **effects:** changes map lakecave2, sets stage 211 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-211)




## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lakecave2_key.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lakecave2_key.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lakecave2_key.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lakecave2_key.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `lakecave2_key` |
    | Spawn group | `lakecave2_key` |
    | Loot table | – |
    | Conversation | `lakecave2_key_check2` |
    | Faction | – |
    | Movement | – |
    | Icon | `items_japozero:387` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "lakecave2_key",
     "name": "Glade key",
     "iconID": "items_japozero:387",
     "unique": 1,
     "spawnGroup": "lakecave2_key",
     "phraseID": "lakecave2_key_check2"
    }
    ```


<small>Data from v0.8.18</small>
