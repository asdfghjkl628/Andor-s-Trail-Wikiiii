# ![](../assets/icons/monsters/monsters_men_0.png){ .sprite } Thieves guild cook

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_0.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `thieves_guild_cook` |
| **Type** | Shopkeeper |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Fallhaven |
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
| [Bread](../items/bread.md) | 100% | 5 |
| [Mushroom](../items/mushroom.md) | 100% | 5 |
| [Eggs](../items/eggs.md) | 100% | 5 |
| [Mead](../items/mead.md) | 100% | 5 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [fallhaven_derelict2](../maps/fallhaven_derelict2.md) | Fallhaven | 1 | – |
| [fallhaven_derelict2_t](../maps/fallhaven_derelict2_t.md) | Fallhaven | 1 | – |


## Quests

- [Night visit](../quests/farrik.md): stages 25

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Thieves guild cook. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/thievesguild_cook_1.json" data-npc="Thieves guild cook" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (11 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-thievesguild_cook_1"></span>**`thievesguild_cook_1`** Thieves guild cook: “Hello, did you want something?”

    - “You look like the cook around here.” → [thievesguild_cook_2](#d-thievesguild_cook_2)
    - “Can I see what food you have for sale?” → *shop opens*
    - “Farrik said you can prepare me a round of special mead.” *(if reached stage 20 of [Night visit](../quests/farrik.md#stage-20))* → [thievesguild_select_1](#d-thievesguild_select_1)

    <span id="d-thievesguild_cook_2"></span>**`thievesguild_cook_2`** Thieves guild cook: “That's right. Someone has to keep these ruffians fed.”

    - “That sure smells good.” → [thievesguild_cook_3](#d-thievesguild_cook_3)
    - “That stew looks disgusting.” → [thievesguild_cook_4](#d-thievesguild_cook_4)
    - “Never mind, bye.” → *conversation ends*

    <span id="d-thievesguild_select_1"></span>**`thievesguild_select_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 25 of [Night visit](../quests/farrik.md#stage-25))* → [thievesguild_cook_10](#d-thievesguild_cook_10)
    - branch 2 → [thievesguild_cook_5](#d-thievesguild_cook_5)

    <span id="d-thievesguild_cook_3"></span>**`thievesguild_cook_3`** Thieves guild cook: “Thanks. This stew is coming along nicely.”

    - “I'm interested in buying some of that.” → *shop opens*

    <span id="d-thievesguild_cook_4"></span>**`thievesguild_cook_4`** Thieves guild cook: “Yeah, I know. With ingredients this bad, what can you do? Anyway, it keeps us fed.”

    - “Can I see what food you have for sale?” → *shop opens*

    <span id="d-thievesguild_cook_10"></span>**`thievesguild_cook_10`** Thieves guild cook: “Yes, I gave you the special brew earlier.”

    - Next → [thievesguild_cook_9](#d-thievesguild_cook_9)

    <span id="d-thievesguild_cook_5"></span>**`thievesguild_cook_5`** Thieves guild cook: “Oh sure. Planning to get someone a bit sleepy eh?”

    - Next → [thievesguild_cook_6](#d-thievesguild_cook_6)

    <span id="d-thievesguild_cook_9"></span>**`thievesguild_cook_9`** Thieves guild cook: “Be careful not to get any of that stuff on your fingers, it is really potent.”

    - “Thank you.” → *conversation ends*

    <span id="d-thievesguild_cook_6"></span>**`thievesguild_cook_6`** Thieves guild cook: “Don't worry, I won't tell anyone. Making sleepy food is one of my specialties.”

    - Next → [thievesguild_cook_7](#d-thievesguild_cook_7)

    <span id="d-thievesguild_cook_7"></span>**`thievesguild_cook_7`** Thieves guild cook: “Give me a minute to mix it up for you.”

    - Next → [thievesguild_cook_8](#d-thievesguild_cook_8)

    <span id="d-thievesguild_cook_8"></span>**`thievesguild_cook_8`** Thieves guild cook: “There. This should do it. Here you go.” — **effects:** sets stage 25 of [Night visit](../quests/farrik.md#stage-25), gives [Prepared sleepy mead](../items/sleepingmead.md)

    - Next → [thievesguild_cook_9](#d-thievesguild_cook_9)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 3 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=thieves_guild_cook.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=thieves_guild_cook.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=thieves_guild_cook.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=thieves_guild_cook.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `thieves_guild_cook` |
    | Spawn group | `tg_cook` |
    | Loot table | `shop_thieves_guild_cook` |
    | Conversation | `thievesguild_cook_1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:0` |
    | Defined in | `res/raw/monsterlist_v068_npcs.json` |

    Raw data:

    ```json
    {
     "id": "thieves_guild_cook",
     "name": "Thieves guild cook",
     "iconID": "monsters_men:0",
     "monsterClass": "humanoid",
     "spawnGroup": "tg_cook",
     "phraseID": "thievesguild_cook_1",
     "droplistID": "shop_thieves_guild_cook"
    }
    ```


<small>Data from v0.8.18</small>
