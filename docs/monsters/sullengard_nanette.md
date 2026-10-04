# ![](../assets/icons/monsters/monsters_ld1_149.png){ .sprite } Nanette

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_149.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `sullengard_nanette` |
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
| [sullengard2_northwest_house](../maps/sullengard2_northwest_house.md) | Sullengard | 1 | – |


## Quests

- [Pond safety](../quests/sullengard_pond_safety.md): stages 10, 20, 30, 50

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Nanette. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/sullengard_nanette_selector_0.json" data-npc="Nanette" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (15 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-sullengard_nanette_selector_0"></span>**`sullengard_nanette_selector_0`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 50 of [Pond safety](../quests/sullengard_pond_safety.md#stage-50))* → [sullengard_nanette_12](#d-sullengard_nanette_12)
    - branch 2 *(if latest stage of [Pond safety](../quests/sullengard_pond_safety.md#stage-20) is 20)* → [sullengard_nanette_7](#d-sullengard_nanette_7)
    - branch 3 *(if latest stage of [Pond safety](../quests/sullengard_pond_safety.md#stage-10) is 10)* → [sullengard_nanette_4](#d-sullengard_nanette_4)
    - branch 4 *(if NOT reached stage 10 of [Pond safety](../quests/sullengard_pond_safety.md#stage-10))* → [sullengard_nanette_0](#d-sullengard_nanette_0)
    - branch 5 → [sullengard_nanette_9](#d-sullengard_nanette_9)

    <span id="d-sullengard_nanette_12"></span>**`sullengard_nanette_12`** Nanette: “Thank you so much again, kid. I can now enjoy my pond again. I'll never throw pebbles in the pond again, I promise.”

    - “You're welcome.” → *conversation ends*
    - “You promise? I won't clean up your mess again.” → [sullengard_nanette_13](#d-sullengard_nanette_13)

    <span id="d-sullengard_nanette_7"></span>**`sullengard_nanette_7`** Nanette: “[Sigh]. Oh hello there, kid. Is my pond safe again?”

    - “Not yet.” *(if NOT killed 26× [Sullengard snapper](../monsters/sullengard_snapper.md))* → *conversation ends*
    - “Yes, your pond is safe again. May I know the cause of it?” *(if killed 26× [Sullengard snapper](../monsters/sullengard_snapper.md))* → [sullengard_nanette_8](#d-sullengard_nanette_8)

    <span id="d-sullengard_nanette_4"></span>**`sullengard_nanette_4`** Nanette: “[Sigh]. Please help me. For I'm longing to enjoy my pond again.” — **effects:** sets stage 10 of [Pond safety](../quests/sullengard_pond_safety.md#stage-10)

    - “Fine. I'm going now.” → [sullengard_nanette_5](#d-sullengard_nanette_5)
    - “Where is your pond again?” → [sullengard_nanette_5](#d-sullengard_nanette_5)
    - “What's the cause of it?” → [sullengard_nanette_6](#d-sullengard_nanette_6)

    <span id="d-sullengard_nanette_0"></span>**`sullengard_nanette_0`** Nanette: “[Sigh]. Oh...hello there, kid.”

    - “Are you OK?” → [sullengard_nanette_1](#d-sullengard_nanette_1)
    - “Is everything all right?” → [sullengard_nanette_1](#d-sullengard_nanette_1)

    <span id="d-sullengard_nanette_9"></span>**`sullengard_nanette_9`** Nanette: “Oh hello there, kid. Have you talked to Kealwea the priest yet?”

    - “There must be a reason why it happened. But what is it?” *(if NOT reached stage 40 of [Pond safety](../quests/sullengard_pond_safety.md#stage-40))* → [sullengard_nanette_8](#d-sullengard_nanette_8)
    - “Not yet” *(if NOT reached stage 40 of [Pond safety](../quests/sullengard_pond_safety.md#stage-40))* → *conversation ends*
    - “Yes. He told me to tell you a story.” *(if reached stage 40 of [Pond safety](../quests/sullengard_pond_safety.md#stage-40))* → [sullengard_nanette_10](#d-sullengard_nanette_10)

    <span id="d-sullengard_nanette_13"></span>**`sullengard_nanette_13`** Nanette: “Promise.”


    <span id="d-sullengard_nanette_8"></span>**`sullengard_nanette_8`** Nanette: “I...I still don't know what's the cause of it. You should talk to Kealwea the priest about it.” — **effects:** sets stage 30 of [Pond safety](../quests/sullengard_pond_safety.md#stage-30)

    - “I'm going to visit him now.” → *conversation ends*
    - “What the? But it just happened yesterday.” → *conversation ends*

    <span id="d-sullengard_nanette_5"></span>**`sullengard_nanette_5`** Nanette: “Remember. It is just southeast from here.” — **effects:** sets stage 20 of [Pond safety](../quests/sullengard_pond_safety.md#stage-20)


    <span id="d-sullengard_nanette_6"></span>**`sullengard_nanette_6`** Nanette: “[Sigh] I will tell you once you help me enjoy my pond again.”

    - “Fine. I'll do it.” → [sullengard_nanette_5](#d-sullengard_nanette_5)
    - “If that's so, then I will not help you.” → *conversation ends*

    <span id="d-sullengard_nanette_1"></span>**`sullengard_nanette_1`** Nanette: “[Sigh]. I'm longing for my pond which I used to enjoy going to. But now it is dangerous to go near my pond, nevermind in it.”

    - “Why is that?” → [sullengard_nanette_2](#d-sullengard_nanette_2)
    - “And then?” → [sullengard_nanette_2](#d-sullengard_nanette_2)
    - “Well I used to enjoy playing hide-and-seek with my brother but not anymore. Bye.” → *conversation ends*

    <span id="d-sullengard_nanette_10"></span>**`sullengard_nanette_10`** Nanette: “[Sigh]. I'm too old for a story. Just tell me the moral of it.”

    - “Don't throw pebbles into the pond. You might disturb whatever lies beneath the surface.” → [sullengard_nanette_11](#d-sullengard_nanette_11)

    <span id="d-sullengard_nanette_2"></span>**`sullengard_nanette_2`** Nanette: “[Sigh]. It started yesterday as I sat on the bench enjoying the pond, I saw vicious creatures emerging from it.”

    - Next → [sullengard_nanette_3](#d-sullengard_nanette_3)

    <span id="d-sullengard_nanette_11"></span>**`sullengard_nanette_11`** Nanette: “Oh. I remember now. I kept throwing pebbles on the pond to relieve my anger issues caused by the unfair taxes of Feygard.” — **effects:** sets stage 50 of [Pond safety](../quests/sullengard_pond_safety.md#stage-50)

    - Next → [sullengard_nanette_12](#d-sullengard_nanette_12)

    <span id="d-sullengard_nanette_3"></span>**`sullengard_nanette_3`** Nanette: “Before I could get away, one of them bit my leg. So I ran home in tremendous pain.”

    - Next → [sullengard_nanette_4](#d-sullengard_nanette_4)



## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 15 lines added |
| [v0.8.8](../versions/0.8.8.md) | Dialogue: 1 line changed<br>· text: “[Sigh]. I'm to old for a story. Just tell me the moral of it.” → “[Sigh]. I'm too old for a story. Just tell me the moral of it.” |
| [v0.8.11](../versions/0.8.11.md) | Dialogue: 1 line changed<br>· text: “Oh hello there, kid. Have you talked to Kaelwea the priest yet?” → “Oh hello there, kid. Have you talked to Kealwea the priest yet?” |
| [v0.8.13](../versions/0.8.13.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_nanette.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_nanette.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_nanette.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_nanette.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `sullengard_nanette` |
    | Spawn group | `sullengard_nanette` |
    | Loot table | – |
    | Conversation | `sullengard_nanette_selector_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:149` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "sullengard_nanette",
     "name": "Nanette",
     "iconID": "monsters_ld1:149",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "sullengard_nanette",
     "phraseID": "sullengard_nanette_selector_0"
    }
    ```


<small>Data from v0.8.18</small>
