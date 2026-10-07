# ![](../assets/icons/monsters/monsters_men2_0.png){ .sprite } Jueth

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men2_0.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `jueth` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Prim |
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
| [blackwater_mountain24](../maps/blackwater_mountain24.md) | Prim | 1 | – |


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Jueth. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/prim_tailor.json" data-npc="Jueth" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-prim_tailor"></span>**`prim_tailor`** Jueth: “Welcome traveller, what can I do for you?”

    - “Let me see what you have available to sell.” → [prim_tailor_1](#d-prim_tailor_1)
    - “What do you know about Lorn's crew's accident?” *(if reached stage 20 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-20); NOT reached stage 21 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-21))* → [prim_tailor_2](#d-prim_tailor_2)

    <span id="d-prim_tailor_1"></span>**`prim_tailor_1`** Jueth: “Sell? I'm sorry, my supplies are all out. Now that the traders do not come here anymore, I don't get my regular shipments. So at the moment, I have nothing to trade with you unfortunately.”


    <span id="d-prim_tailor_2"></span>**`prim_tailor_2`** Jueth: “I have heard about an accident, yes, but I've been very busy lately.”

    - “Busy? You're out of stock!” → [prim_tailor_3](#d-prim_tailor_3)
    - “OK, thanks anyway.” → *conversation ends*

    <span id="d-prim_tailor_3"></span>**`prim_tailor_3`** Jueth: “*Staring at you comptemptuously* I also take various repair orders, kid. Now get out of my shop.”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.14](../versions/0.7.14.md) | Dialogue: 2 lines added, 2 lines changed<br>· text: “Sell? I'm sorry, my supply is all out. Now that the traders do not co…” → “Sell? I'm sorry, my supplies are all out. Now that the traders do not…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jueth.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jueth.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jueth.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jueth.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `jueth` |
    | Spawn group | `prim_tailor` |
    | Loot table | – |
    | Conversation | `prim_tailor` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men2:0` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "jueth",
     "name": "Jueth",
     "iconID": "monsters_men2:0",
     "monsterClass": "humanoid",
     "spawnGroup": "prim_tailor",
     "phraseID": "prim_tailor"
    }
    ```


<small>Data from v0.8.18</small>
