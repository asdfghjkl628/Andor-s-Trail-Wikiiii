# ![](../assets/icons/monsters/monsters_tometik8_26.png){ .sprite } Shiny Foggerlump

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik8_26.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `feygard_fogmonster9` |
| **Type** | NPC |
| **Class** | Demon |
| **HP** | 220 |
| **XP when killed** | 540 |
| **Found in** | Guynmart Castle |
| **Immune to crits** | Yes |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 220 |
| Damage | 8 to 20 |
| Attack chance | 140 |
| Block chance | 150 |
| Damage resistance | 10 |
| Max AP | 10 |
| Attack cost | 6 AP |
| Attacks per turn | 1 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons can't be critically hit. Your crit build will have to sit this one out.

**On hit:** Heal HP: 2 to 5; On target: Mind fog (magnitude 2, 3 rounds, 50% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Fog in a bottle](../items/fogbottle.md) | 100% | 1 to 2 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [swamp3](../maps/swamp3.md) | Guynmart Castle | 1 | – |


## Quests

- [Fog in the woods](../quests/fogmonster.md): stages 20

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Shiny Foggerlump. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/feygard_fogmonster9.json" data-npc="Shiny Foggerlump" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-feygard_fogmonster9"></span>**`feygard_fogmonster9`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 1 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-1); reached stage 2 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-2); reached stage 3 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-3); reached stage 4 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-4); reached stage 5 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-5))* → [feygard_fogmonster9_5](#d-feygard_fogmonster9_5)
    - Next *(if reached stage 1 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-1))* → [feygard_fogmonster9_1](#d-feygard_fogmonster9_1)
    - Next *(if reached stage 2 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-2))* → [feygard_fogmonster9_1](#d-feygard_fogmonster9_1)
    - Next *(if reached stage 3 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-3))* → [feygard_fogmonster9_1](#d-feygard_fogmonster9_1)
    - Next *(if reached stage 4 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-4))* → [feygard_fogmonster9_1](#d-feygard_fogmonster9_1)
    - Next *(if reached stage 5 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-5))* → [feygard_fogmonster9_1](#d-feygard_fogmonster9_1)
    - Next → [feygard_fogmonster9_10](#d-feygard_fogmonster9_10)

    <span id="d-feygard_fogmonster9_5"></span>**`feygard_fogmonster9_5`** Shiny Foggerlump: “Me and my brothers watch over the ruler of the swamp.”

    - “Your brothers have all left the area already. Now to you ...” → *fight starts*
    - “So I'm going to talk to your brothers.” → *conversation ends*

    <span id="d-feygard_fogmonster9_1"></span>**`feygard_fogmonster9_1`** Shiny Foggerlump: “Me and my brothers watch over the ruler of the swamp.”

    - “Not for long, some of your brothers have all left the area already. Attack!” → [feygard_fogmonster9_20](#d-feygard_fogmonster9_20)
    - “So I'm going to talk to your remaining brothers.” → *conversation ends*

    <span id="d-feygard_fogmonster9_10"></span>**`feygard_fogmonster9_10`** Shiny Foggerlump: “Me and my brothers watch over the ruler of the swamp.”

    - “Not for long. Attack!” → [feygard_fogmonster9_20](#d-feygard_fogmonster9_20)
    - “So I'm going to talk to your brothers.” → *conversation ends*

    <span id="d-feygard_fogmonster9_20"></span>**`feygard_fogmonster9_20`** Shiny Foggerlump: “You can't defeat me as long as my brothers stand their ground.” — **effects:** sets stage 20 of [Fog in the woods](../quests/fogmonster.md#stage-20)

    - “Well, in that case stay here. I'll be back in a minute.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_fogmonster9.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_fogmonster9.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_fogmonster9.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_fogmonster9.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `feygard_fogmonster9` |
    | Spawn group | `feygard_fogmonster9` |
    | Loot table | `feygard_fogmonster` |
    | Conversation | `feygard_fogmonster9` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik8:26` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "feygard_fogmonster9",
     "name": "Shiny Foggerlump",
     "iconID": "monsters_tometik8:26",
     "maxHP": 220,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "demon",
     "attackDamage": {
      "min": 8,
      "max": 20
     },
     "phraseID": "feygard_fogmonster9",
     "droplistID": "feygard_fogmonster",
     "attackCost": 6,
     "attackChance": 140,
     "blockChance": 150,
     "damageResistance": 10,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 2,
       "max": 5
      },
      "conditionsTarget": [
       {
        "condition": "mind_fog",
        "magnitude": 2,
        "duration": 3,
        "chance": "50"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
