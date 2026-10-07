# ![](../assets/icons/monsters/monsters_ld1_148.png){ .sprite } Melona

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_148.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `melona` |
| **Type** | Shopkeeper |
| **Class** | ? |
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
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Hard biscuits](../items/biscuit_hard.md) | 100% | 1 to 5 |
| [Pork pie](../items/pie_pork.md) | 100% | 1 to 3 |
| [Cooked meat](../items/meat_cooked.md) | 100% | 1 to 4 |
| [Red apple](../items/apple_red.md) | 100% | 1 to 2 |
| [Carrots](../items/carrots.md) | 100% | 1 to 6 |
| [Cheese](../items/cheese.md) | 100% | 1 to 2 |
| [Corn](../items/corn.md) | 100% | 1 to 2 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [brimhaven_inn_east](../maps/brimhaven_inn_east.md) | Brimhaven | 1 | – |


## Quests

- [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md): stages 230

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Melona. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/melona_0.json" data-npc="Melona" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (6 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-melona_0"></span>**`melona_0`** Melona: “Hello. I'm Melona, and I run this fine establishment.”

    - Next → [melona_0a](#d-melona_0a)

    <span id="d-melona_0a"></span>**`melona_0a`** Melona: “What can I help you with?”

    - “I'm hungry. Do you have any food to sell?” → [melona_1](#d-melona_1)
    - “I need somewhere to sleep. Do you have a bed available?” *(if NOT reached stage 230 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-230))* → [melona_2](#d-melona_2)
    - “I'm looking for my brother, Andor. He looks a bit like me.” → [melona_3](#d-melona_3)

    <span id="d-melona_1"></span>**`melona_1`** Melona: “Certainly. Please take a look at what I can offer.”

    - “Thanks.” → *shop opens*

    <span id="d-melona_2"></span>**`melona_2`** Melona: “Yes. It's 90 gold. That may seem like a lot, but it's a one-time payment. As long as a bed is free, in the future you can use it any time you want.”

    - “That's too expensive. Let's talk about something else.” → [melona_0a](#d-melona_0a)
    - “I'll take it.” *(if pay 90 gold)* → [melona_2a](#d-melona_2a)

    <span id="d-melona_3"></span>**`melona_3`** Melona: “Sorry, I haven't seen anyone that looks like you.”

    - “OK. Let's talk about something else.” → [melona_0a](#d-melona_0a)

    <span id="d-melona_2a"></span>**`melona_2a`** Melona: “Thank you for your patronage. You can use any available bed.” — **effects:** sets stage 230 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-230)




## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 6 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=melona.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=melona.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=melona.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=melona.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `melona` |
    | Spawn group | `melona` |
    | Loot table | `melona` |
    | Conversation | `melona_0` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_ld1:148` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "melona",
     "name": "Melona",
     "iconID": "monsters_ld1:148",
     "unique": 1,
     "movementAggressionType": "none",
     "phraseID": "melona_0",
     "droplistID": "melona"
    }
    ```


<small>Data from v0.8.18</small>
