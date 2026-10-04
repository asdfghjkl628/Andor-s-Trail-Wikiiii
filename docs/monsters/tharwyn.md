# ![](../assets/icons/monsters/monsters_men_7.png){ .sprite } Tharwyn

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_7.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `tharwyn` |
| **Type** | Shopkeeper |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Vilegard |
| **Introduced** | v0.7.0 or earlier |

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
| [Meat](../items/meat.md) | 100% | 5 |
| [Cooked meat](../items/meat_cooked.md) | 100% | 5 |
| [Carrot](../items/carrot.md) | 100% | 5 |
| [Mushroom](../items/mushroom.md) | 100% | 5 |
| [Mead](../items/mead.md) | 100% | 5 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [vilegard_tavern](../maps/vilegard_tavern.md) | Vilegard | 1 | – |


## Quests

- [Beer Bootlegging](../quests/beer_bootlegging.md): stages 30
- [Trusting an outsider](../quests/vilegard.md): stages 10
- [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md): stages 32

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Tharwyn. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/tharwyn_select.json" data-npc="Tharwyn" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (15 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-tharwyn_select"></span>**`tharwyn_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 30 of [Trusting an outsider](../quests/vilegard.md#stage-30))* → [tharwyn_1](#d-tharwyn_1)
    - branch 2 → [vilegard_shop_notrust](#d-vilegard_shop_notrust)

    <span id="d-tharwyn_1"></span>**`tharwyn_1`** Tharwyn: “Hello there. I heard you helped Jolnor in the chapel. You have my thanks, friend.”

    - Next → [tharwyn_2](#d-tharwyn_2)

    <span id="d-vilegard_shop_notrust"></span>**`vilegard_shop_notrust`** Tharwyn: “You are an outsider. We don't like outsiders here in Vilegard. Please leave.”

    - “Why is everyone in Vilegard so suspicious of outsiders?” → [vilegard_shop_notrust_2](#d-vilegard_shop_notrust_2)
    - “Can I see what items you have for sale?” → [vilegard_shop_notrust_2](#d-vilegard_shop_notrust_2)

    <span id="d-tharwyn_2"></span>**`tharwyn_2`** Tharwyn: “Have a seat anywhere. What can I get you?”

    - “Show me what food you have available.” → *shop opens*
    - “Torilo suggested that I ask other tavern owners such as yourself about a 'business agreement' that you may have with a…” *(if latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-20) is 20)* → [tharwyn_beer](#d-tharwyn_beer)
    - “Let's get back to discussing your 'business agreement' with the 'distributors'.” *(if reached stage 32 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-32); NOT reached stage 30 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-30))* → [tharwyn_beer_50](#d-tharwyn_beer_50)

    <span id="d-vilegard_shop_notrust_2"></span>**`vilegard_shop_notrust_2`** Tharwyn: “I don't trust you. You should go see Jolnor in the chapel if you want some sympathy.” — **effects:** sets stage 10 of [Trusting an outsider](../quests/vilegard.md#stage-10)


    <span id="d-tharwyn_beer"></span>**`tharwyn_beer`** Tharwyn: “What? I don't know anything about what you speak of.”

    - “I am sure you do. What do I have to do to hear what you know?” → [tharwyn_beer_10](#d-tharwyn_beer_10)

    <span id="d-tharwyn_beer_50"></span>**`tharwyn_beer_50`** Tharwyn: “I will not get into the 'business agreement' part of this deal, but I will tell you about the 'distributors'.” — **effects:** sets stage 32 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-32)

    - “Great. Start talking.” → [tharwyn_beer_60](#d-tharwyn_beer_60)

    <span id="d-tharwyn_beer_10"></span>**`tharwyn_beer_10`** Tharwyn: “Well, if I read you correctly, I feel like you are prepared to offer me a bribe?”

    - “Oh great, not another tavern owner hungry for more gold.” → [tharwyn_beer_20](#d-tharwyn_beer_20)

    <span id="d-tharwyn_beer_60"></span>**`tharwyn_beer_60`** Tharwyn: “Do you see that suspicious looking fellow over there in the corner?”

    - “The thief?” → [tharwyn_beer_70](#d-tharwyn_beer_70)

    <span id="d-tharwyn_beer_20"></span>**`tharwyn_beer_20`** Tharwyn: “Well, am I correct?”

    - “If that's what it it takes to get you to talk, then yes.” → [tharwyn_beer_30](#d-tharwyn_beer_30)

    <span id="d-tharwyn_beer_70"></span>**`tharwyn_beer_70`** Tharwyn: “That is Dunla. He gets me my beer. Go talk to him.” — **effects:** sets stage 30 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-30)


    <span id="d-tharwyn_beer_30"></span>**`tharwyn_beer_30`** Tharwyn: “Wow! This is my lucky day. I just found out today that my daughter needs 5,000 gold in order to enroll at this special school in Nor City and now here you are offering me a bribe.”

    - Next → [tharwyn_beer_31](#d-tharwyn_beer_31)

    <span id="d-tharwyn_beer_31"></span>**`tharwyn_beer_31`** Tharwyn: “That will be 5,000 gold please.”

    - “What? You guys are killing me.” → [tharwyn_beer_40](#d-tharwyn_beer_40)

    <span id="d-tharwyn_beer_40"></span>**`tharwyn_beer_40`** Tharwyn: “Is that a 'yes' or a 'no'?”

    - “That sounds ridiculous, but here, take it.” *(if pay 5,000 gold)* → [tharwyn_beer_50](#d-tharwyn_beer_50)
    - “That sounds ridiculous! I won't pay that much.” *(if have 5,000 gold)* → [tharwyn_beer_51](#d-tharwyn_beer_51)
    - “I can't afford that.” *(if have 5,000 gold)* → [tharwyn_beer_51](#d-tharwyn_beer_51)

    <span id="d-tharwyn_beer_51"></span>**`tharwyn_beer_51`** Tharwyn: “That's fine with me, but no information for you.”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines changed |
| [v0.8.2](../versions/0.8.2.md) | Dialogue: 10 lines added, 1 line changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 2 lines changed<br>· text: “Wow! This is my lucky day. I just found out today that my daughter ne…” → “Wow! This is my lucky day. I just found out today that my daughter ne…”<br>· text: “That will be 5000 gold please.” → “That will be {5000} gold please.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tharwyn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tharwyn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tharwyn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tharwyn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `tharwyn` |
    | Spawn group | `tharwyn` |
    | Loot table | `shop_tharwyn` |
    | Conversation | `tharwyn_select` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:7` |
    | Defined in | `res/raw/monsterlist_v068_npcs.json` |

    Raw data:

    ```json
    {
     "id": "tharwyn",
     "name": "Tharwyn",
     "iconID": "monsters_men:7",
     "monsterClass": "humanoid",
     "spawnGroup": "tharwyn",
     "phraseID": "tharwyn_select",
     "droplistID": "shop_tharwyn"
    }
    ```


<small>Data from v0.8.18</small>
