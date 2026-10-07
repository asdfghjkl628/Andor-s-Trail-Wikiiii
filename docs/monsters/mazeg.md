# ![](../assets/icons/monsters/monsters_rltiles1_85.png){ .sprite } Mazeg

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_85.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `mazeg` |
| **Type** | Shopkeeper |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | blackwater_mountain43 |
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
| [Regular potion of health](../items/health.md) | 100% | 10 |
| [Major potion of health](../items/health_major2.md) | 100% | 10 |
| [Blackwater brew](../items/bwm_brew.md) | 100% | 10 |
| [Weak poison](../items/pot_poison_weak.md) | 100% | 10 |
| [Potion of blind rage](../items/pot_blind_rage.md) | 100% | 10 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [blackwater_mountain43](../maps/blackwater_mountain43.md) | – | 1 | – |


## Quests

- [A difference of opinion](../quests/sisterfight.md): stages 50, 51, 55

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Mazeg. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/mazeg.json" data-npc="Mazeg" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (18 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-mazeg"></span>**`mazeg`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 240 of [The agent and the beast](../quests/bwm_agent.md#stage-240))* → [mazeg_1](#d-mazeg_1)
    - branch 2 → [mazeg_2](#d-mazeg_2)

    <span id="d-mazeg_1"></span>**`mazeg_1`** Mazeg: “Welcome friend! Would you like to browse my selection of fine potions and ointments?”

    - “Sure. Show me what you have.” → *shop opens*
    - “I am looking for some Lyson marrow extract, for Hjaldar in Remgard.” *(if reached stage 45 of [A difference of opinion](../quests/sisterfight.md#stage-45))* → [mazeg_e_1](#d-mazeg_e_1)

    <span id="d-mazeg_2"></span>**`mazeg_2`** Mazeg: “Welcome traveller. Have you come to ask for help from me and my potions?”

    - “Yes. Please show me what you have.” → [blackwater_notrust](#d-blackwater_notrust)
    - “I am looking for some Lyson marrow extract, for Hjaldar in Remgard.” *(if reached stage 45 of [A difference of opinion](../quests/sisterfight.md#stage-45))* → [mazeg_e_1](#d-mazeg_e_1)

    <span id="d-mazeg_e_1"></span>**`mazeg_e_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 55 of [A difference of opinion](../quests/sisterfight.md#stage-55))* → [mazeg_d](#d-mazeg_d)
    - branch 2 *(if reached stage 51 of [A difference of opinion](../quests/sisterfight.md#stage-51))* → [mazeg_e_5b](#d-mazeg_e_5b)
    - branch 3 *(if reached stage 50 of [A difference of opinion](../quests/sisterfight.md#stage-50))* → [mazeg_e_5b](#d-mazeg_e_5b)
    - branch 4 → [mazeg_e_2](#d-mazeg_e_2)

    <span id="d-blackwater_notrust"></span>**`blackwater_notrust`** Mazeg: “Regardless, I cannot help you. My services are only for residents of Blackwater mountain, and I don't trust you enough yet.”


    <span id="d-mazeg_d"></span>**`mazeg_d`** Mazeg: “I already sold you some before. Did you lose it? Please tell my old friend Hjaldar that I said hello.”


    <span id="d-mazeg_e_5b"></span>**`mazeg_e_5b`** Mazeg: “Sure, I have it.”

    - Next → [mazeg_e_6](#d-mazeg_e_6)

    <span id="d-mazeg_e_2"></span>**`mazeg_e_2`** Mazeg: “Hjaldar, my old friend! Tell me, how is he these days?”

    - “He asked me to relay his greetings to you, and to tell you that he is well.” → [mazeg_e_3](#d-mazeg_e_3)
    - “He is sick, and getting worse every day.” → [mazeg_e_4](#d-mazeg_e_4)

    <span id="d-mazeg_e_6"></span>**`mazeg_e_6`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 240 of [The agent and the beast](../quests/bwm_agent.md#stage-240))* → [mazeg_e_7a](#d-mazeg_e_7a)
    - branch 2 → [mazeg_e_7b](#d-mazeg_e_7b)

    <span id="d-mazeg_e_3"></span>**`mazeg_e_3`** Mazeg: “Oh, I am so glad to hear that! We sure did have some nice times while working together.”

    - Next → [mazeg_e_5](#d-mazeg_e_5)

    <span id="d-mazeg_e_4"></span>**`mazeg_e_4`** Mazeg: “I'm sorry to hear that. He always seemed like a tough old boy to me.”

    - Next → [mazeg_e_5](#d-mazeg_e_5)

    <span id="d-mazeg_e_7a"></span>**`mazeg_e_7a`** Mazeg: “Since you helped us up here in the Blackwater mountain settlement earlier, I am willing to give you a discount on the price for some Lyson marrow extract. For 400 gold, I am willing to sell you some of it for my old friend Hjaldar.” — **effects:** sets stage 50 of [A difference of opinion](../quests/sisterfight.md#stage-50)

    - “Here is 400 gold.” *(if pay 400 gold)* → [mazeg_e_9](#d-mazeg_e_9)
    - “Ouch, that much?! Is there anything you can do to lower the price?” → [mazeg_e_8a](#d-mazeg_e_8a)
    - “I'll return when I have the gold for it.” → *conversation ends*

    <span id="d-mazeg_e_7b"></span>**`mazeg_e_7b`** Mazeg: “For 800 gold, I am willing to sell you some of it for my old friend Hjaldar.” — **effects:** sets stage 51 of [A difference of opinion](../quests/sisterfight.md#stage-51)

    - “Here is 800 gold.” *(if pay 800 gold)* → [mazeg_e_9](#d-mazeg_e_9)
    - “Ouch, that much?! Is there anything you can do to lower the price?” → [mazeg_e_8b](#d-mazeg_e_8b)
    - “I'll return when I have the gold for it.” → *conversation ends*

    <span id="d-mazeg_e_5"></span>**`mazeg_e_5`** Mazeg: “You asked for some Lyson marrow extract.”

    - Next → [mazeg_e_5b](#d-mazeg_e_5b)

    <span id="d-mazeg_e_9"></span>**`mazeg_e_9`** Mazeg: “Thanks. Here's some of the Lyson marrow extract.” — **effects:** sets stage 55 of [A difference of opinion](../quests/sisterfight.md#stage-55), gives [Vial of Lyson marrow extract](../items/lyson_marrow.md)

    - Next → [mazeg_e_10](#d-mazeg_e_10)

    <span id="d-mazeg_e_8a"></span>**`mazeg_e_8a`** Mazeg: “No, 400 gold it is. That's a really good price, considering how hard this stuff is to find. Besides, if it weren't for Hjaldar, I wouldn't even be selling this to you.”

    - “Here is 400 gold.” *(if pay 400 gold)* → [mazeg_e_9](#d-mazeg_e_9)
    - “I'll return when I have the gold for it.” → *conversation ends*

    <span id="d-mazeg_e_8b"></span>**`mazeg_e_8b`** Mazeg: “No, 800 gold it is. That's a really good price, considering how hard this stuff is to find. Besides, if it weren't for Hjaldar, I wouldn't even be selling this to you.”

    - “Here is 800 gold.” *(if pay 800 gold)* → [mazeg_e_9](#d-mazeg_e_9)
    - “I'll return when I have the gold for it.” → *conversation ends*

    <span id="d-mazeg_e_10"></span>**`mazeg_e_10`** Mazeg: “Please give my warmest greetings to my good friend Hjaldar. Tell him that I am well.”

    - “Will do. Thanks and goodbye.” → *conversation ends*
    - “Whatever. Goodbye.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 7 lines changed<br>· text: “Since you helped us up here in the Blackwater Mountain settlement ear…” → “Since you helped us up here in the Blackwater mountain settlement ear…”<br>· text: “Regardless, I cannot help you. My services are only for residents of …” → “Regardless, I cannot help you. My services are only for residents of …” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mazeg.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mazeg.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mazeg.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mazeg.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `mazeg` |
    | Spawn group | `mazeg` |
    | Loot table | `shop_mazeg` |
    | Conversation | `mazeg` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:85` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "mazeg",
     "name": "Mazeg",
     "iconID": "monsters_rltiles1:85",
     "monsterClass": "humanoid",
     "spawnGroup": "mazeg",
     "phraseID": "mazeg",
     "droplistID": "shop_mazeg"
    }
    ```


<small>Data from v0.8.18</small>
