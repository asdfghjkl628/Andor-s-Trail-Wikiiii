# ![](../assets/icons/monsters/monsters_rltiles1_76.png){ .sprite } Guard

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_76.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `crossroads_sleepguard` |
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


## Quests

- [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md): stages 17

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Guard. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/crossroads_sleepguard.json" data-npc="Guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (7 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-crossroads_sleepguard"></span>**`crossroads_sleepguard`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 17 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-17))* → [crossroads_sleepguard_2](#d-crossroads_sleepguard_2)
    - branch 2 → [crossroads_sleepguard_1](#d-crossroads_sleepguard_1)

    <span id="d-crossroads_sleepguard_2"></span>**`crossroads_sleepguard_2`** Guard: “Hello again. I hope the bed is comfortable enough. Use it as much as you like.”


    <span id="d-crossroads_sleepguard_1"></span>**`crossroads_sleepguard_1`** Guard: “Hello there. Can I help you?”

    - “No. Goodbye.” → *conversation ends*
    - “Mind if I use one of the beds over there?” → [crossroads_sleepguard_3](#d-crossroads_sleepguard_3)

    <span id="d-crossroads_sleepguard_3"></span>**`crossroads_sleepguard_3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 90 of [Night visit](../quests/farrik.md#stage-90))* → [crossroads_sleepguard_5](#d-crossroads_sleepguard_5)
    - branch 2 → [crossroads_sleepguard_4](#d-crossroads_sleepguard_4)

    <span id="d-crossroads_sleepguard_5"></span>**`crossroads_sleepguard_5`** Guard: “Say, aren't you that kid that helped the guards down in Fallhaven? With the thieves that were planning an escape?”

    - “Yes, I helped the guards in the prison find out about some plans that the thieves had.” → [crossroads_sleepguard_6](#d-crossroads_sleepguard_6)

    <span id="d-crossroads_sleepguard_4"></span>**`crossroads_sleepguard_4`** Guard: “No, sorry. These beds are for guards and allies of Feygard only.”


    <span id="d-crossroads_sleepguard_6"></span>**`crossroads_sleepguard_6`** Guard: “I knew I had heard about you somewhere. You are always welcome by us guards. You can use that second bed over there to the left if you need to rest.” — **effects:** sets stage 17 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-17)




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=crossroads_sleepguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=crossroads_sleepguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=crossroads_sleepguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=crossroads_sleepguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `crossroads_sleepguard` |
    | Spawn group | `crossroads_sleepguard` |
    | Loot table | – |
    | Conversation | `crossroads_sleepguard` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:76` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "crossroads_sleepguard",
     "name": "Guard",
     "iconID": "monsters_rltiles1:76",
     "monsterClass": "humanoid",
     "spawnGroup": "crossroads_sleepguard",
     "phraseID": "crossroads_sleepguard"
    }
    ```


<small>Data from v0.8.18</small>
