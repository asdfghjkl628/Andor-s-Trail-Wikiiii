# ![](../assets/icons/monsters/monsters_ld1_158.png){ .sprite } Gyra

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_158.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `stn_gyra4` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Flagstone Prison, Stoutford |
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
| Move cost | 2 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [stoutford_castle0](../maps/stoutford_castle0.md) | Flagstone Prison | 1 | appears later in a quest |
| [stoutford_castle_barrack0](../maps/stoutford_castle_barrack0.md) | Stoutford | 1 | appears later in a quest |
| [waytogalmore0](../maps/waytogalmore0.md) | Flagstone Prison | 1 | appears later in a quest |
| [waytogalmore1](../maps/waytogalmore1.md) | Flagstone Prison | 1 | appears later in a quest |
| [wild18](../maps/wild18.md) | Flagstone Prison | 1 | appears later in a quest |
| [wild22](../maps/wild22.md) | Stoutford | 1 | appears later in a quest |


## Quests

- [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md): stages 29

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Gyra. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/stn_gyra.json" data-npc="Gyra" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-stn_gyra"></span>**`stn_gyra`** Gyra: “Please go ahead. I will follow you, probably.”

    - “Probably?” → [stn_gyra_20](#d-stn_gyra_20)
    - “OK, just stay close to me.” → *conversation ends*
    - “Let me carry you for a while.” → [stn_gyra_10](#d-stn_gyra_10)

    <span id="d-stn_gyra_20"></span>**`stn_gyra_20`** Gyra: “I will follow you wherever you go. Only if I'm too scared, then I will stay where I am. For example, I will never go to Flagstone.”

    - Next → [stn_gyra_22](#d-stn_gyra_22)

    <span id="d-stn_gyra_10"></span>**`stn_gyra_10`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 29 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-29), applies condition fatigue_minor

    - branch 1 → *NPC leaves*

    <span id="d-stn_gyra_22"></span>**`stn_gyra_22`** Gyra: “You may have to carry me from time to time. I'll jump off your back again when I'm rested.”

    - “OK, let's go then.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_gyra4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_gyra4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_gyra4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_gyra4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `stn_gyra4` |
    | Spawn group | `stn_gyra4` |
    | Loot table | – |
    | Conversation | `stn_gyra` |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:158` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_gyra4",
     "name": "Gyra",
     "iconID": "monsters_ld1:158",
     "moveCost": 2,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "phraseID": "stn_gyra"
    }
    ```


<small>Data from v0.8.18</small>
