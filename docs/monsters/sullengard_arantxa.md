# ![](../assets/icons/monsters/monsters_rogue1_0.png){ .sprite } Prowling Arantxa

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rogue1_0.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `sullengard_arantxa` |
| **Type** | Shopkeeper |
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


## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Spiked metal boots](../items/boots_spiked.md) | 100% | 1 |
| [Garnet whisper ring](../items/old_lady_ring.md) | 85% | 1 |
| [Polished sparkling gem](../items/gem5.md) | 100% | 5 to 10 |
| [Branch of twilight](../items/branch_of_twilight.md) | 70% | 1 |
| [Sharpened gem](../items/gem4.md) | 100% | 3 |
| [Soul rapier](../items/soul_rapier.md) | 100% | 1 |
| [Quickstrike dagger](../items/quickdagger1.md) | 200% | 1 to 2 |
| [Thieves' cloak of whispers](../items/thieve_clock_whispers.md) | 100% | 1 |
| [Treads of dark glory](../items/shoe_dark_glory.md) | 75% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [sullengard_tavern_basement](../maps/sullengard_tavern_basement.md) | Sullengard | 1 | – |


## Quests

- [Recovering stolen property](../quests/sullengard_recover_items.md): stages 40

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Prowling Arantxa. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/sullengard_arantxa_0.json" data-npc="Prowling Arantxa" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (9 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-sullengard_arantxa_0"></span>**`sullengard_arantxa_0`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if latest stage of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-30) is 30; reached stage 23 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-23); reached stage 24 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-24); reached stage 25 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-25))* → [sullengard_arantxa_10](#d-sullengard_arantxa_10)
    - branch 2 → [sullengard_arantxa_sell](#d-sullengard_arantxa_sell)

    <span id="d-sullengard_arantxa_10"></span>**`sullengard_arantxa_10`** Prowling Arantxa: “I saw you talking with Gaelian and many other people in town. May I ask about what?”

    - “None of your business.” → *conversation ends*
    - “I'm looking into the armory break-in and robbery.” → [sullengard_arantxa_20](#d-sullengard_arantxa_20)

    <span id="d-sullengard_arantxa_sell"></span>**`sullengard_arantxa_sell`** Prowling Arantxa: “Do you want to take a look at any of 'my stuff'? It's all for sale at the right price.”

    - “Yes. I could use some item upgrades.” → *shop opens*
    - “No, I'm good for now.” → *conversation ends*

    <span id="d-sullengard_arantxa_20"></span>**`sullengard_arantxa_20`** Prowling Arantxa: “Are you sure that you want to involve yourself in such affairs?”

    - “Why, what's this about?” → [sullengard_arantxa_30](#d-sullengard_arantxa_30)

    <span id="d-sullengard_arantxa_30"></span>**`sullengard_arantxa_30`** Prowling Arantxa: “Well I don't know much. All I know is 'the lost traveler', whom I've never seen before, approached me recently with a couple of items that he wanted me to buy.”

    - Next → [sullengard_arantxa_40](#d-sullengard_arantxa_40)

    <span id="d-sullengard_arantxa_40"></span>**`sullengard_arantxa_40`** Prowling Arantxa: “Since I recognized a couple of them as being Zaccheria's, I refused to buy them.”

    - “Really? That's honestly the only reason why you didn't buy them?” → [sullengard_arantxa_50](#d-sullengard_arantxa_50)

    <span id="d-sullengard_arantxa_50"></span>**`sullengard_arantxa_50`** Prowling Arantxa: “What is that supposed to mean?”

    - “Well, let's be honest. You are a thief after all.” → [sullengard_arantxa_60](#d-sullengard_arantxa_60)

    <span id="d-sullengard_arantxa_60"></span>**`sullengard_arantxa_60`** Prowling Arantxa: “You see kid, here in Sullengard, we have a working agreement with the townspeople. They pay us for our services and we do not steal from them.” — **effects:** sets stage 40 of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-40)

    - “That makes good business sense.” → [sullengard_arantxa_70](#d-sullengard_arantxa_70)

    <span id="d-sullengard_arantxa_70"></span>**`sullengard_arantxa_70`** Prowling Arantxa: “Now if I were you, I would approach 'the lost traveler' very carefully. He is desperate and desperate people have been known to be unpredictable.”

    - “Thank you, friend and I will be careful.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 9 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_arantxa.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_arantxa.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_arantxa.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_arantxa.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `sullengard_arantxa` |
    | Spawn group | `sullengard_arantxa` |
    | Loot table | `sullengard_arantxa_dl` |
    | Conversation | `sullengard_arantxa_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rogue1:0` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "sullengard_arantxa",
     "name": "Prowling Arantxa",
     "iconID": "monsters_rogue1:0",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "sullengard_arantxa",
     "phraseID": "sullengard_arantxa_0",
     "droplistID": "sullengard_arantxa_dl"
    }
    ```


<small>Data from v0.8.18</small>
