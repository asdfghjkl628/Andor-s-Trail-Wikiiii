# ![](../assets/icons/monsters/monsters_ld1_81.png){ .sprite } Defy

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_81.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `g04_defy` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Sullengard |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

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
| [sullengard_tavern_basement](../maps/sullengard_tavern_basement.md) | Sullengard | 1 | – |


## Quests

- [Another ruthless Crackshot](../quests/Thieves04.md): stages 20

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Defy. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/guild04_defy.json" data-npc="Defy" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (6 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guild04_defy"></span>**`guild04_defy`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if latest stage of [Another ruthless Crackshot](../quests/Thieves04.md#stage-10) is 10)* → [guild04_defy_1](#d-guild04_defy_1)
    - branch 2 → [guild04_defy_5](#d-guild04_defy_5)

    <span id="d-guild04_defy_1"></span>**`guild04_defy_1`** Defy: “Andor, is that you? You grew weak and small. How was your visit to Nor City?”

    - “I'm $playername. Andor is my brother and I'm not weak.” → [guild04_defy_2](#d-guild04_defy_2)

    <span id="d-guild04_defy_5"></span>**`guild04_defy_5`** Defy: “Just mind your own business, kid. Now, get out of here or I'll kick you out.”

    - “You will be the one who's kicked out of here.” → *conversation ends*
    - “You will be the one to blame here.” *(if latest stage of [Another ruthless Crackshot](../quests/Thieves04.md#stage-20) is 20)* → *conversation ends*

    <span id="d-guild04_defy_2"></span>**`guild04_defy_2`** Defy: “Oh, yeah, but you do look a lot like him. I'm Defy.”

    - “So you know my brother as well?” → [guild04_defy_3](#d-guild04_defy_3)

    <span id="d-guild04_defy_3"></span>**`guild04_defy_3`** Defy: “Indeed. He always asks questions like a curious kid does. Tell me, what brings you here, $playername?”

    - “Umar told me that it is time to give their share to the bootleg brewers.” → [guild04_defy_4](#d-guild04_defy_4)
    - “Umar sent me for our business.” → [guild04_defy_4](#d-guild04_defy_4)

    <span id="d-guild04_defy_4"></span>**`guild04_defy_4`** Defy: “The time of sharing? If that's so, then tell him that there will be a delay.” — **effects:** sets stage 20 of [Another ruthless Crackshot](../quests/Thieves04.md#stage-20)

    - “Really?” → [guild04_defy_5](#d-guild04_defy_5)
    - “A delay of what?” → [guild04_defy_5](#d-guild04_defy_5)



## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 6 lines added |
| [v0.8.8](../versions/0.8.8.md) | attackChance removed; attackCost removed; attackDamage removed; blockChance removed; criticalMultiplier removed; criticalSkill removed (+7 more) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g04_defy.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g04_defy.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g04_defy.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g04_defy.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `g04_defy` |
    | Spawn group | `g04_defy` |
    | Loot table | – |
    | Conversation | `guild04_defy` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:81` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "g04_defy",
     "name": "Defy",
     "iconID": "monsters_ld1:81",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "g04_defy",
     "phraseID": "guild04_defy",
     "hitEffect": {},
     "hitReceivedEffect": {}
    }
    ```


<small>Data from v0.8.18</small>
