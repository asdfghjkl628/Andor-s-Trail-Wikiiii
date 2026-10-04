# ![](../assets/icons/monsters/monsters_rogue1_0.png){ .sprite } Quiet thief

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rogue1_0.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `stoutford_thief` |
| **Type** | Shopkeeper |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Stoutford |
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
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Stiletto](../items/stiletto.md) | 100% | 1 |
| [Ring of damage resistance](../items/ring_dr1.md) | 100% | 1 |
| [Necklace of lifesteal](../items/necklace_lifesteal.md) | 100% | 1 |
| [Polished ring of damage resistance](../items/ring_dr2.md) | 100% | 1 |
| [Cloth tunic](../items/tunic_cloth.md) | 100% | 1 |
| [Boots of flight](../items/boots_flight.md) | 100% | 1 |
| [Villain's ring](../items/ring_villain.md) | 100% | 1 |
| [Fine snakeskin gloves](../items/gloves4.md) | 100% | 1 |
| [Fine green hat](../items/hat2.md) | 100% | 1 |
| [Lesser ring of block](../items/ring_block1.md) | 100% | 1 |
| [Spiked buckler](../items/shield_spiked.md) | 100% | 1 |
| [Superior necklace of the protector](../items/necklace_protector2.md) | 100% | 1 |
| [Sharp steel dagger](../items/dagger_sharp_steel.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [stoutford_tavern](../maps/stoutford_tavern.md) | Stoutford | 1 | – |


## Quests

- [Rumblings](../quests/rumblings.md): stages 25

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Quiet thief. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/stoutford_thief_0.json" data-npc="Quiet thief" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (8 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-stoutford_thief_0"></span>**`stoutford_thief_0`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 20 of [Rumblings](../quests/rumblings.md#stage-20); reached stage 70 of [Night visit](../quests/farrik.md#stage-70))* → [stoutford_thief_rumblings20_0](#d-stoutford_thief_rumblings20_0)
    - Next → [stoutford_thief_initial_0](#d-stoutford_thief_initial_0)

    <span id="d-stoutford_thief_rumblings20_0"></span>**`stoutford_thief_rumblings20_0`** Quiet thief: “Hey kid. A "common friend" told me about you.”

    - “Who?” → [stoutford_thief_rumblings20_1](#d-stoutford_thief_rumblings20_1)

    <span id="d-stoutford_thief_initial_0"></span>**`stoutford_thief_initial_0`** Quiet thief: “Psst.”

    - Next → [stoutford_thief_initial_1](#d-stoutford_thief_initial_1)

    <span id="d-stoutford_thief_rumblings20_1"></span>**`stoutford_thief_rumblings20_1`** Quiet thief: “Shhh! Quiet here. You helped the guild, so I'll help you too.”

    - “Help me do what?” → [stoutford_thief_rumblings20_2](#d-stoutford_thief_rumblings20_2)
    - “Great!” → [stoutford_thief_rumblings20_2](#d-stoutford_thief_rumblings20_2)

    <span id="d-stoutford_thief_initial_1"></span>**`stoutford_thief_initial_1`** Quiet thief: “Wanna trade?”

    - “Sure.” → *shop opens*
    - “No.” → *conversation ends*

    <span id="d-stoutford_thief_rumblings20_2"></span>**`stoutford_thief_rumblings20_2`** Quiet thief: “A kid that looked like you was here. He apparently did some business with the owner and the regulars.” — **effects:** sets stage 25 of [Rumblings](../quests/rumblings.md#stage-25)

    - Next → [stoutford_thief_rumblings20_3](#d-stoutford_thief_rumblings20_3)

    <span id="d-stoutford_thief_rumblings20_3"></span>**`stoutford_thief_rumblings20_3`** Quiet thief: “They were very careful, and even I couldn't catch a glimpse of their deeds, but you should be cautious if you deal with them.”

    - “Thanks for the advice. I'll take care.” → [stoutford_thief_rumblings20_4](#d-stoutford_thief_rumblings20_4)
    - “I can handle myself! I don't fear them, or anyone else!” → [stoutford_thief_rumblings20_4](#d-stoutford_thief_rumblings20_4)

    <span id="d-stoutford_thief_rumblings20_4"></span>**`stoutford_thief_rumblings20_4`** Quiet thief: “Just sayin'. Do what you will.”

    - Next → [stoutford_thief_initial_1](#d-stoutford_thief_initial_1)



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 8 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_thief.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_thief.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_thief.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_thief.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `stoutford_thief` |
    | Spawn group | `stoutford_thief` |
    | Loot table | `stoutfordthief` |
    | Conversation | `stoutford_thief_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rogue1:0` |
    | Defined in | `res/raw/monsterlist_stoutford.json` |

    Raw data:

    ```json
    {
     "id": "stoutford_thief",
     "name": "Quiet thief",
     "iconID": "monsters_rogue1:0",
     "monsterClass": "humanoid",
     "spawnGroup": "stoutford_thief",
     "phraseID": "stoutford_thief_0",
     "droplistID": "stoutfordthief"
    }
    ```


<small>Data from v0.8.18</small>
