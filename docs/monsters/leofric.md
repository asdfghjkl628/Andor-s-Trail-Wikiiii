# ![](../assets/icons/monsters/monsters_tometik1_85.png){ .sprite } Leofric

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik1_85.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `leofric` |
| **Type** | Shopkeeper |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Foaming Flask Tavern |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

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
| [Honey](../items/honey.md) | 100% | 5 to 9 |
| [Mead](../items/mead.md) | 100% | 3 to 5 |
| [Honeycomb](../items/honeycomb.md) | 2% | 1 |
| [Bees wax](../items/beeswax.md) | 100% | 5 to 9 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [beekeeper1](../maps/beekeeper1.md) | Foaming Flask Tavern | 1 | – |


## Quests

- [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md): stages 10

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Leofric. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/leofric_welcome.json" data-npc="Leofric" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-leofric_welcome"></span>**`leofric_welcome`** Leofric: “Ah, greetings, traveler! What brings you to my humble apiary?”

    - “Hello. Who might you be?” → [leofric_intro](#d-leofric_intro)

    <span id="d-leofric_intro"></span>**`leofric_intro`** Leofric: “I be Leofric, master of bees and their keeper. I tend the hives and harvest their golden treasures”

    - “What exactly do you do here, Leofric?” → [leofric_job](#d-leofric_job)
    - “If you're a master of bees, why do you wear a helmet and mask?” → [leofric_explain](#d-leofric_explain)

    <span id="d-leofric_job"></span>**`leofric_job`** Leofric: “I care for the bees, gather their honey and wax, and craft fine goods from their toil. Bees be wondrous creatures, providing both sweet sustenance and warm light.”

    - “Do you have anything for sale?” → [leofric_sell](#d-leofric_sell)

    <span id="d-leofric_explain"></span>**`leofric_explain`** Leofric: “Ah, a keen eye you have! The helmet and mask protect me from more than just bee stings. The forest holds dangers aplenty, and it's wise to be prepared. You never know what you might encounter when tending to the hives deep in the woods.”

    - “What exactly do you do here, Leofric?” → [leofric_job](#d-leofric_job)

    <span id="d-leofric_sell"></span>**`leofric_sell`** Leofric: “Aye, I have many wares to offer. Jars of honey, beeswax and some fine mead. But that's it for now as my supply is lower than normal. Take a look, and see what catches your fancy.” — **effects:** sets stage 10 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-10)

    - “Sounds great.” → *shop opens*



## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=leofric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=leofric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=leofric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=leofric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `leofric` |
    | Spawn group | `leofric` |
    | Loot table | `leofric_dl` |
    | Conversation | `leofric_welcome` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik1:85` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "leofric",
     "name": "Leofric",
     "iconID": "monsters_tometik1:85",
     "monsterClass": "humanoid",
     "phraseID": "leofric_welcome",
     "droplistID": "leofric_dl"
    }
    ```


<small>Data from v0.8.18</small>
