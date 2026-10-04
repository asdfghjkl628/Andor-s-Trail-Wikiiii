# ![](../assets/icons/monsters/monsters_ld1_81.png){ .sprite } Defy

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_81.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `aidem_base_defy` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 359 |
| **XP when killed** | 851 |
| **Found in** | aidem_base_2 |
| **Introduced** | [v0.8.8](../versions/0.8.8.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 359 |
| Damage | 10 to 18 |
| Attack chance | 170 |
| Block chance | 170 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 3 AP |
| Critical skill | 5 |
| Critical multiplier | 3.0 |
| Crit chance | 5% |

**When hit:** On self: Concentration (magnitude 1, 2 rounds, 40% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Villain's ring](../items/ring_villain.md) | 100% | 1 |
| [Gold coins](../items/gold.md) | 100% | 3500 to 5000 |
| [Defy's ring](../items/defy_ring.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [aidem_base_2](../maps/aidem_base_2.md) | – | 1 | appears later in a quest |


## Quests that count kills

- [Wanted men](../quests/wanted_men.md#stage-76) with stepping on a trigger on [aidem_base_2](../maps/aidem_base_2.md) checks that you've killed at least 1


## Quests

- [Wanted men](../quests/wanted_men.md): stages 56, 60, 75

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Defy. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/aidem_base_defy_selector.json" data-npc="Defy" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (8 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-aidem_base_defy_selector"></span>**`aidem_base_defy_selector`** *(silent check: the first matching branch below is taken)*

    - “Come and get it!” *(if latest stage of [Wanted men](../quests/wanted_men.md#stage-75) is 75)* → [aidem_base_fight](#d-aidem_base_fight)
    - Next *(if reached stage 45 of [Wanted men](../quests/wanted_men.md#stage-45); NOT reached stage 60 of [Wanted men](../quests/wanted_men.md#stage-60))* → [aidem_base_defy_help_10](#d-aidem_base_defy_help_10)
    - Next *(if NOT reached stage 56 of [Wanted men](../quests/wanted_men.md#stage-56))* → [aidem_base_dont_help_defy_10](#d-aidem_base_dont_help_defy_10)
    - “What are you waiting for? Go take the fake key to Troublemaker.” *(if reached stage 60 of [Wanted men](../quests/wanted_men.md#stage-60))* → *conversation ends*

    <span id="d-aidem_base_fight"></span>**`aidem_base_fight`** Defy: “You will regret this, kid!” — **effects:** removes monsters from aidem_base_2, spawns monsters on aidem_base_2, spawns monsters on aidem_base_2, spawns monsters on aidem_base_2, spawns monsters on aidem_base_2

    - “I hope not.” → *fight starts*

    <span id="d-aidem_base_defy_help_10"></span>**`aidem_base_defy_help_10`** Defy: “Do you have the key? Hand it over.”

    - “Oops. I forgot to bring it with me. I'll be back soon.” *(if NOT carry 1× [Thieves' vault key](../items/thieves_vault_key.md))* → *conversation ends*
    - “Yes. Here it is.” *(if hand over 1× [Thieves' vault key](../items/thieves_vault_key.md))* → [aidem_base_defy_help_20](#d-aidem_base_defy_help_20)
    - “Yes, but you are not having it. I will loot the vault myself and keep everything I find.” *(if carry 1× [Thieves' vault key](../items/thieves_vault_key.md))* → [aidem_base_defy_dont_help_10](#d-aidem_base_defy_dont_help_10)

    <span id="d-aidem_base_dont_help_defy_10"></span>**`aidem_base_dont_help_defy_10`** Defy: “Do you have the key? Hand it over.”

    - “Yes, Here it is. [Handing over the fake key]” *(if hand over 1× [Fake Thieve's Guild vault key](../items/thieves_vault_key_fake.md))* → [aidem_base_defy_help_tg_10](#d-aidem_base_defy_help_tg_10)

    <span id="d-aidem_base_defy_help_20"></span>**`aidem_base_defy_help_20`** Defy: “Thank you so much. Now take this fake key that Zachlanny's has made and return it to Troublemaker before he suspects anything. Then meet us at the vault to collect your share of the loot.” — **effects:** gives [Aidem fake vault key](../items/aidem_fake_vault_key.md), sets stage 60 of [Wanted men](../quests/wanted_men.md#stage-60)


    <span id="d-aidem_base_defy_dont_help_10"></span>**`aidem_base_defy_dont_help_10`** Defy: “Come again?”

    - “I said, "here it is".” → [aidem_base_defy_help_20](#d-aidem_base_defy_help_20)
    - “You heard me the first time. I'm keeping the key and looting the vault myself.” → [aidem_base_defy_dont_help_20](#d-aidem_base_defy_dont_help_20)

    <span id="d-aidem_base_defy_help_tg_10"></span>**`aidem_base_defy_help_tg_10`** Defy: “Thank you so much. Now take this fake key that Zachlanny's has made and return it to Troublemaker before he suspects anything. Then meet us at the vault to collect your share of the loot.” — **effects:** gives [Aidem fake vault key](../items/aidem_fake_vault_key.md), sets stage 56 of [Wanted men](../quests/wanted_men.md#stage-56), removes monsters from aidem_base_2, spawns monsters on wild6_house, removes monsters from aidem_base_2


    <span id="d-aidem_base_defy_dont_help_20"></span>**`aidem_base_defy_dont_help_20`** Defy: “I will be taking that key now!” — **effects:** sets stage 75 of [Wanted men](../quests/wanted_men.md#stage-75)

    - “Come and try!” → [aidem_base_fight](#d-aidem_base_fight)



## Version history

| Version | Change |
|---|---|
| [v0.8.8](../versions/0.8.8.md) | Added<br>Dialogue: 8 lines added |
| [v0.8.10](../versions/0.8.10.md) | Dialogue: 1 line changed |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=aidem_base_defy.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=aidem_base_defy.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=aidem_base_defy.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=aidem_base_defy.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `aidem_base_defy` |
    | Spawn group | `help_defy` |
    | Loot table | `aidem_base_defy_dl` |
    | Conversation | `aidem_base_defy_selector` |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_ld1:81` |
    | Defined in | `res/raw/monsterlist_mt_galmore.json` |

    Raw data:

    ```json
    {
     "id": "aidem_base_defy",
     "name": "Defy",
     "iconID": "monsters_ld1:81",
     "maxHP": 359,
     "moveCost": 3,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 10,
      "max": 18
     },
     "spawnGroup": "help_defy",
     "phraseID": "aidem_base_defy_selector",
     "droplistID": "aidem_base_defy_dl",
     "attackCost": 3,
     "attackChance": 170,
     "criticalSkill": 5,
     "criticalMultiplier": 3.0,
     "blockChance": 170,
     "hitReceivedEffect": {
      "conditionsSource": [
       {
        "condition": "g03_concentration",
        "magnitude": 1,
        "duration": 2,
        "chance": "40"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
