# ![](../assets/icons/monsters/monsters_men_8.png){ .sprite } Highwayman

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_8.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `sullengard_highwayman` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 200 |
| **XP when killed** | 621 |
| **Found in** | way_to_sullengard_east9 |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 200 |
| Damage | 10 to 20 |
| Attack chance | 200 |
| Block chance | 150 |
| Damage resistance | 3 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 50 |
| Critical multiplier | 2.0 |
| Crit chance | 26% |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Bandit's Brew](../items/sullengrad_bandit_brew.md) | 10% | 1 |
| [Gold coins](../items/gold.md) | 70% | 51 to 106 |
| [Ring of damage +5](../items/ring_dmg5.md) | 5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [way_to_sullengard_east9](../maps/way_to_sullengard_east9.md) | – | 1 | – |


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Highwayman. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/sullengard_highwayman.json" data-npc="Highwayman" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (7 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-sullengard_highwayman"></span>**`sullengard_highwayman`** Highwayman: “I've been looking for someone who fits your description.” — **effects:** faction “fct_highwayman2” set to -10

    - “You have? Why?” → [sullengard_highwayman_2](#d-sullengard_highwayman_2)

    <span id="d-sullengard_highwayman_2"></span>**`sullengard_highwayman_2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if killed 0× [Highwayman](../monsters/highwayman1.md))* → [sullengard_highwayman_2a](#d-sullengard_highwayman_2a)
    - branch 2 *(if killed 0× [Highwayman](../monsters/highwayman.md))* → [sullengard_highwayman_2b](#d-sullengard_highwayman_2b)
    - branch 3 → [sullengard_highwayman_3](#d-sullengard_highwayman_3)

    <span id="d-sullengard_highwayman_2a"></span>**`sullengard_highwayman_2a`** Highwayman: “Yes! You are the one that has killed my fellow "road travellers" and now you must pay!”

    - “Bring it on!” → *fight starts*

    <span id="d-sullengard_highwayman_2b"></span>**`sullengard_highwayman_2b`** Highwayman: “Yes! You are the one that has killed my fellow "road travellers" and now you must pay!”

    - “Bring it on!” → *fight starts*

    <span id="d-sullengard_highwayman_3"></span>**`sullengard_highwayman_3`** Highwayman: “Yes, you do look like him. He is the one who helped Sullengard financially on many occasions.”

    - “Hey, it must be my brother Andor! Tell me more about him.” → [sullengard_highwayman_4](#d-sullengard_highwayman_4)

    <span id="d-sullengard_highwayman_4"></span>**`sullengard_highwayman_4`** Highwayman: “Pay me 750 gold coins first or I'll rob you and then the Sullengard for my living!”

    - “Fine. Here's 750 gold coins. Now, tell me about him.” *(if pay 750 gold)* → [sullengard_highwayman_5](#d-sullengard_highwayman_5)
    - “Bring it on!” → *fight starts*

    <span id="d-sullengard_highwayman_5"></span>**`sullengard_highwayman_5`** Highwayman: “He is taller and stronger than you. Have a good time!” — **effects:** faction “fct_highwayman2” set to 11

    - branch 1 → *NPC leaves*



## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 7 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_highwayman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_highwayman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_highwayman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_highwayman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `sullengard_highwayman` |
    | Spawn group | `sullengard_highwayman` |
    | Loot table | `sullengard_highwayman_drop` |
    | Conversation | `sullengard_highwayman` |
    | Faction | `fct_highwayman2` |
    | Movement | – |
    | Icon | `monsters_men:8` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "sullengard_highwayman",
     "name": "Highwayman",
     "iconID": "monsters_men:8",
     "maxHP": 200,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 10,
      "max": 20
     },
     "spawnGroup": "sullengard_highwayman",
     "faction": "fct_highwayman2",
     "phraseID": "sullengard_highwayman",
     "droplistID": "sullengard_highwayman_drop",
     "attackCost": 5,
     "attackChance": 200,
     "criticalSkill": 50,
     "criticalMultiplier": 2.0,
     "blockChance": 150,
     "damageResistance": 3
    }
    ```


<small>Data from v0.8.18</small>
