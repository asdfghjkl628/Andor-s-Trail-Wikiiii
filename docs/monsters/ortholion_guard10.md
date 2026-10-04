# ![](../assets/icons/monsters/monsters_omi2_12.png){ .sprite } Drunken Feygard scout

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_omi2_12.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `ortholion_guard10` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | elm_mine1 |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

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
| [elm_mine1](../maps/elm_mine1.md) | – | 2 | appears later in a quest |


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Drunken Feygard scout. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/ortholion_guard10_s.json" data-npc="Drunken Feygard scout" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ortholion_guard10_s"></span>**`ortholion_guard10_s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (1/4%))* → [ortholion_guard10_1](#d-ortholion_guard10_1)
    - branch 2 *(if random chance (1/3%))* → [ortholion_guard10_2](#d-ortholion_guard10_2)
    - branch 3 *(if random chance (1/2%))* → [ortholion_guard10_3](#d-ortholion_guard10_3)
    - branch 4 → [ortholion_guard10_4](#d-ortholion_guard10_4)

    <span id="d-ortholion_guard10_1"></span>**`ortholion_guard10_1`** Drunken Feygard scout: “[hic] Drink! [hic] Drink for those who've fallen!”


    <span id="d-ortholion_guard10_2"></span>**`ortholion_guard10_2`** Drunken Feygard scout: “No! [looks at you] This is my beeeeeer, kid! [hic]”

    - “Uh... How did you get drunk that fast?” → *conversation ends*
    - “Mead isn't my cup of tea, goodbye.” → *conversation ends*
    - “Get out of my way, drunkard!” → *conversation ends*

    <span id="d-ortholion_guard10_3"></span>**`ortholion_guard10_3`** Drunken Feygard scout: “H..Halt! [hic] Kids not allowed!”

    - “I'll go where I please in this mine! Hmpf...” → *conversation ends*
    - “I'm here to see your general, now go sleep it off.” → *conversation ends*

    <span id="d-ortholion_guard10_4"></span>**`ortholion_guard10_4`** Drunken Feygard scout: “This guard drinks his jar of mead ceaselessly, ignoring your presence.”




## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added<br>Dialogue: 5 lines added |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 3 lines changed<br>· text: “H..Halt! *hic* Kids not allowed!” → “H..Halt! [hic] Kids not allowed!”<br>· text: “No! *looks at you* This is my beeeeeer, kid! *hic*” → “No! [looks at you] This is my beeeeeer, kid! [hic]” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard10.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard10.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard10.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard10.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `ortholion_guard10` |
    | Spawn group | `ortholion_guard10` |
    | Loot table | – |
    | Conversation | `ortholion_guard10_s` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_omi2:12` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "ortholion_guard10",
     "name": "Drunken Feygard scout",
     "iconID": "monsters_omi2:12",
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "phraseID": "ortholion_guard10_s"
    }
    ```


<small>Data from v0.8.18</small>
