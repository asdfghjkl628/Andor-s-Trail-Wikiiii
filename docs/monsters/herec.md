---
description: "Herec is a non-player character (NPC) in Andor's Trail, found in Blackwater mountain 44. Shopkeeper; starts No weakness."
---

# ![](../assets/icons/monsters/monsters_men2_9.png){ .sprite } Herec

**Where to find Herec:** [Blackwater mountain 44](../maps/blackwater_mountain44.md#pin-npc-herec)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men2_9.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Shopkeeper; starts [No weakness](../quests/bwm_wyrms.md) |
| **Found in** | Blackwater mountain 44 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Restore fatigue](../items/pot_fatigue_restore.md) | 100% | 10 |

## Quests

- [No weakness](../quests/bwm_wyrms.md): stages 10, 20, 30

## Dialogue simulator

Set your quest stages and items, then talk to Herec. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/herec_start.json" data-npc="Herec" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (18 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-herec_start"></span>**`herec_start`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 30 of [No weakness](../quests/bwm_wyrms.md#stage-30))* → [herec_q5](#d-herec_q5)
    - branch 2 *(if reached stage 20 of [No weakness](../quests/bwm_wyrms.md#stage-20))* → [herec_q3](#d-herec_q3)
    - branch 3 *(if reached stage 10 of [No weakness](../quests/bwm_wyrms.md#stage-10))* → [herec_q1](#d-herec_q1)
    - branch 4 → [herec_1](#d-herec_1)

    <span id="d-herec_q5"></span>**`herec_q5`** Herec: “Would you like to trade for some potions?”

    - “Sure. Let's see what you have.” → *shop opens*

    <span id="d-herec_q3"></span>**`herec_q3`** Herec: “Welcome back my friend! Good news. I have successfully distilled the fragments of the claws you brought earlier.”

    - Next → [herec_q4](#d-herec_q4)

    <span id="d-herec_q1"></span>**`herec_q1`** Herec: “Welcome back. How is the search going?”

    - “What was I supposed to do again?” → [herec_4](#d-herec_4)
    - “I haven't found everything yet. But I am working on it.” → [herec_10](#d-herec_10)
    - “I have found what you asked for.” *(if hand over 5× [White wyrm claw](../items/bwm_claws.md))* → [herec_q2](#d-herec_q2)

    <span id="d-herec_1"></span>**`herec_1`** Herec: “Welcome, traveller. You must be the one I heard about, that travelled up the mountain.”

    - Next → [herec_2](#d-herec_2)

    <span id="d-herec_q4"></span>**`herec_q4`** Herec: “Now I am able to create effective potions that contain some essence of the white wyrms. These potions will be very useful in future dealings with these monsters.” — **effects:** sets stage 30 of [No weakness](../quests/bwm_wyrms.md#stage-30)

    - Next → [herec_q5](#d-herec_q5)

    <span id="d-herec_4"></span>**`herec_4`** Herec: “It is simple really. I am studying these wyrm creatures that lurk outside our settlement. I am trying to find what their strengths are, so that I can use it for myself.”

    - Next → [herec_5](#d-herec_5)

    <span id="d-herec_10"></span>**`herec_10`** Herec: “Good. Thank you. Please hurry back so I can continue my research on these beasts.” — **effects:** sets stage 10 of [No weakness](../quests/bwm_wyrms.md#stage-10)


    <span id="d-herec_q2"></span>**`herec_q2`** Herec: “Very well done my friend! These will be very valuable in my research.” — **effects:** sets stage 20 of [No weakness](../quests/bwm_wyrms.md#stage-20)

    - Next → [herec_q2_2](#d-herec_q2_2)

    <span id="d-herec_2"></span>**`herec_2`** Herec: “Would you be willing to help me with a task?”

    - “Depends. What task?” → [herec_4](#d-herec_4)
    - “Why would I want to help you?” → [herec_3](#d-herec_3)

    <span id="d-herec_5"></span>**`herec_5`** Herec: “But my expertise is in the studies of them, and not in actually going head to head with those things.”

    - Next → [herec_6](#d-herec_6)

    <span id="d-herec_q2_2"></span>**`herec_q2_2`** Herec: “Come back in just a minute and I will have something ready for you.”


    <span id="d-herec_3"></span>**`herec_3`** Herec: “Ah, a negotiator. I like that. If you help me, I will offer to trade the fruits of my labour with you. It should be most valuable to you.”

    - “Fine. What task are we talking about here?” → [herec_4](#d-herec_4)
    - “No, how can I agree to something when I don't know what it is? I'm out.” → [herec_11](#d-herec_11)

    <span id="d-herec_6"></span>**`herec_6`** Herec: “That's where you come in.”

    - Next → [herec_7](#d-herec_7)

    <span id="d-herec_11"></span>**`herec_11`** Herec: “I assure you that my research is important. But it's your decision, and your loss.”


    <span id="d-herec_7"></span>**`herec_7`** Herec: “I need you to gather some samples from them for me. I hear that some of the white wyrm beasts have sharper claws that can be extracted at the time of death.”

    - Next → [herec_8](#d-herec_8)

    <span id="d-herec_8"></span>**`herec_8`** Herec: “If you were to bring me some samples of those claws from the white wyrms, that would really speed up my research further.”

    - Next → [herec_9](#d-herec_9)

    <span id="d-herec_9"></span>**`herec_9`** Herec: “Let's say, five of those claws should be enough.”

    - “OK, sounds easy enough. I'll get you your 5 white wyrm claws.” → [herec_10](#d-herec_10)
    - “Sure. Those things are no match for me.” → [herec_10](#d-herec_10)
    - “No way I am going near those beasts again.” → [herec_11](#d-herec_11)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `herec` |
    | Type (wiki) | NPC |
    | Spawn group | `herec` |
    | Loot table | `shop_herec` |
    | Conversation | `herec_start` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men2:9` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "herec",
     "name": "Herec",
     "iconID": "monsters_men2:9",
     "monsterClass": "humanoid",
     "spawnGroup": "herec",
     "phraseID": "herec_start",
     "droplistID": "shop_herec"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=herec.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=herec.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=herec.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=herec.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
