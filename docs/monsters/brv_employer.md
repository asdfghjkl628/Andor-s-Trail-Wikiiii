# ![](../assets/icons/monsters/monsters_ld1_10.png){ .sprite } Gnossath

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_10.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `brv_employer` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Brimhaven |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

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
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [brimhaven1](../maps/brimhaven1.md) | Brimhaven | 1 | appears later in a quest |


## Quests

- [Work for debts](../quests/brv_employee.md): stages 30
- [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md): stages 11

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Gnossath. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_employer.json" data-npc="Gnossath" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (14 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brv_employer"></span>**`brv_employer`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 90 of [Work for debts](../quests/brv_employee.md#stage-90))* → [brv_employer_90](#d-brv_employer_90)
    - branch 2 *(if reached stage 40 of [Work for debts](../quests/brv_employee.md#stage-40))* → [brv_employer_40](#d-brv_employer_40)
    - branch 3 *(if reached stage 30 of [Work for debts](../quests/brv_employee.md#stage-30))* → [brv_employer_30](#d-brv_employer_30)
    - branch 4 *(if reached stage 10 of [Work for debts](../quests/brv_employee.md#stage-10))* → [brv_employer_10](#d-brv_employer_10)
    - branch 5 *(if reached stage 1 of [Work for debts](../quests/brv_employee.md#stage-1))* → [brv_employer_01](#d-brv_employer_01)
    - branch 6 → [brv_employer_0](#d-brv_employer_0)

    <span id="d-brv_employer_90"></span>**`brv_employer_90`** Gnossath: “Thanks again for your good work. Are you sure you don't want a job?”

    - “Certainly not. I am on a mission for Mikhail.” → *conversation ends*

    <span id="d-brv_employer_40"></span>**`brv_employer_40`** Gnossath: “You have carried some boulders already - good. Just do the rest too.”

    - “OK.” → *conversation ends*

    <span id="d-brv_employer_30"></span>**`brv_employer_30`** Gnossath: “Where are the boulders? I knew they would be too heavy for you.”

    - “Just you wait.” → *conversation ends*

    <span id="d-brv_employer_10"></span>**`brv_employer_10`** Gnossath: “Have you seen the lazybones, Stebbarik?”

    - “Stebbarik is ill at home. He is very anxious that you might get angry.” → [brv_employer_10_10](#d-brv_employer_10_10)

    <span id="d-brv_employer_01"></span>**`brv_employer_01`** Gnossath: “I am waiting for Stebbarik. Have you seen him?” — **effects:** sets stage 11 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-11), removes monsters from brimhaven_tavern1, removes monsters from brimhaven_employee, spawns monsters on brimhaven_employee, spawns monsters on brimhaven_tavern1

    - “No. What do you want of him?” → [brv_employer_02](#d-brv_employer_02)

    <span id="d-brv_employer_0"></span>**`brv_employer_0`** Gnossath: “Ahoy kid! I am Gnossath, warden of the great dam.”

    - Next → [brv_employer_01](#d-brv_employer_01)

    <span id="d-brv_employer_10_10"></span>**`brv_employer_10_10`** Gnossath: “Ill? Rats! Who will repair the dam now? It must be done soon.”

    - “If it is so important, maybe I can help?” → [brv_employer_10_20](#d-brv_employer_10_20)

    <span id="d-brv_employer_02"></span>**`brv_employer_02`** Gnossath: “He has to work for me. I hope for his sake that he will appear soon.”

    - Next → [brv_employer_04](#d-brv_employer_04)

    <span id="d-brv_employer_10_20"></span>**`brv_employer_10_20`** Gnossath: “You? This work requires a lot of heavy lifting. You being a kid and all, I'm not sure you are up to it.”

    - Next → [brv_employer_10_22](#d-brv_employer_10_22)

    <span id="d-brv_employer_04"></span>**`brv_employer_04`** Gnossath: “You could do me a favor, if you'd find him for me.”


    <span id="d-brv_employer_10_22"></span>**`brv_employer_10_22`** Gnossath: “We need 25 big boulders carried from the stock to the dam here.”

    - “Sounds easy. Let me try it.” → [brv_employer_10_30](#d-brv_employer_10_30)
    - “You are right. This is no work for me.” → *conversation ends*

    <span id="d-brv_employer_10_30"></span>**`brv_employer_10_30`** Gnossath: “OK. Try, if you want. The pile of boulders is just next to the wooden logs over there.” — **effects:** sets stage 30 of [Work for debts](../quests/brv_employee.md#stage-30), changes map brimhaven1

    - “OK.” → [brv_employer_10_40](#d-brv_employer_10_40)

    <span id="d-brv_employer_10_40"></span>**`brv_employer_10_40`** Gnossath: “But beware, they are really heavy.”




## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 14 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_employer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_employer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_employer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_employer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `brv_employer` |
    | Spawn group | `brv_employer` |
    | Loot table | – |
    | Conversation | `brv_employer` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:10` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_employer",
     "name": "Gnossath",
     "iconID": "monsters_ld1:10",
     "moveCost": 5,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_employer",
     "phraseID": "brv_employer"
    }
    ```


<small>Data from v0.8.18</small>
