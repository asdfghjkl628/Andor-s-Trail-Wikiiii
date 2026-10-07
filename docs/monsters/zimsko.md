---
description: "Zimsko is a non-player character (NPC) in Andor's Trail, found in Brimhaven."
---

# ![](../assets/icons/monsters/monsters_men2_9.png){ .sprite } Zimsko

**Where to find Zimsko:** Brimhaven: [brimhaven_tavern_west](../maps/brimhaven_tavern_west.md#pin-npc-zimsko)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men2_9.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Brimhaven |
| **Entry ID** | `zimsko` |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

## Quests

- [Fair play?](../quests/brv_blackjack.md): stages 20, 30, 31, 70, 80
- [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md): stages 110, 120, 130

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Zimsko. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_zimsko_select.json" data-npc="Zimsko" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (17 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brv_zimsko_select"></span>**`brv_zimsko_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 110 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-110))* → [brv_zimsko_5](#d-brv_zimsko_5)
    - branch 2 → [brv_zimsko_10](#d-brv_zimsko_10)

    <span id="d-brv_zimsko_5"></span>**`brv_zimsko_5`** Zimsko: “You again?”

    - Next → [brv_zimsko_6](#d-brv_zimsko_6)

    <span id="d-brv_zimsko_10"></span>**`brv_zimsko_10`** Zimsko: “What do you want from me?” — **effects:** sets stage 110 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-110)

    - “I just want to talk a little bit.” → [brv_zimsko_10_1](#d-brv_zimsko_10_1)
    - “I want to join you for a beer.” → [brv_zimsko_10_2](#d-brv_zimsko_10_2)
    - “Do you know something about the back room?” *(if reached stage 10 of [Fair play?](../quests/brv_blackjack.md#stage-10))* → [brv_zimsko_10_1](#d-brv_zimsko_10_1)

    <span id="d-brv_zimsko_6"></span>**`brv_zimsko_6`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 70 of [Fair play?](../quests/brv_blackjack.md#stage-70))* → [brv_zimsko_80](#d-brv_zimsko_80)
    - branch 2 *(if reached stage 80 of [Fair play?](../quests/brv_blackjack.md#stage-80))* → [brv_zimsko_80](#d-brv_zimsko_80)
    - branch 3 *(if reached stage 30 of [Fair play?](../quests/brv_blackjack.md#stage-30))* → [brv_zimsko_40](#d-brv_zimsko_40)
    - branch 4 *(if reached stage 120 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-120))* → [brv_zimsko_20_2](#d-brv_zimsko_20_2)
    - branch 5 → [brv_zimsko_10](#d-brv_zimsko_10)

    <span id="d-brv_zimsko_10_1"></span>**`brv_zimsko_10_1`** Zimsko: “I am very thirsty...”

    - “Why don't you buy something for yourself?” → [brv_zimsko_10_2](#d-brv_zimsko_10_2)
    - “Let's drink a beer together. I will pay. [Pay 2 gold]” *(if pay 2 gold)* → [brv_zimsko_20](#d-brv_zimsko_20)

    <span id="d-brv_zimsko_10_2"></span>**`brv_zimsko_10_2`** Zimsko: “I lost all my money gambling and can't afford a beer.” — **effects:** sets stage 130 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-130)

    - “Bad luck.” → *conversation ends*
    - “I am out of money.” *(if NOT have 2 gold)* → *conversation ends*
    - “I will buy you a beer. [Pay 2 gold]” *(if pay 2 gold)* → [brv_zimsko_20](#d-brv_zimsko_20)

    <span id="d-brv_zimsko_80"></span>**`brv_zimsko_80`** Zimsko: “Thank you for your help with the gamblers.”

    - Next → [brv_zimsko_20_1](#d-brv_zimsko_20_1)

    <span id="d-brv_zimsko_40"></span>**`brv_zimsko_40`** Zimsko: “Did you already find out if they are cheating? You have to win and lose a few times until they trust you and play for higher amounts. Then they start cheating.”

    - “I did not find anything out yet.” → [brv_zimsko_20_1](#d-brv_zimsko_20_1)
    - “I gambled with them and it seems they are cheating.” *(if reached stage 140 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-140); NOT reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50))* → [brv_zimsko_40_2](#d-brv_zimsko_40_2)
    - “I gambled with them and it seems they are cheating. I even had a fight with them.” *(if reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50))* → [brv_zimsko_40_3](#d-brv_zimsko_40_3)
    - “I gambled with them and I think they are playing fair.” *(if reached stage 140 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-140); NOT reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50))* → [brv_zimsko_40_1](#d-brv_zimsko_40_1)

    <span id="d-brv_zimsko_20_2"></span>**`brv_zimsko_20_2`** Zimsko: “Thank you for the beer.”

    - Next → [brv_zimsko_20_1](#d-brv_zimsko_20_1)

    <span id="d-brv_zimsko_20"></span>**`brv_zimsko_20`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 120 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-120)

    - branch 1 → [brv_zimsko_20_2](#d-brv_zimsko_20_2)

    <span id="d-brv_zimsko_20_1"></span>**`brv_zimsko_20_1`** Zimsko: “Can I have one more beer?”

    - “Here is one more beer. [Pay 2 gold]” *(if pay 2 gold)* → [brv_zimsko_20_2](#d-brv_zimsko_20_2)
    - “I am out of money.” *(if NOT have 2 gold)* → [brv_zimsko_20_1](#d-brv_zimsko_20_1)
    - “[Lie] I am out of money.” *(if have 2 gold)* → [brv_zimsko_20_1](#d-brv_zimsko_20_1)
    - “No, you have had enough.” → [brv_zimsko_20_1](#d-brv_zimsko_20_1)
    - “Do you know something about the back room?” *(if reached stage 10 of [Fair play?](../quests/brv_blackjack.md#stage-10); NOT reached stage 20 of [Fair play?](../quests/brv_blackjack.md#stage-20))* → [brv_zimsko_30](#d-brv_zimsko_30)
    - “Where did you lose your money?” *(if NOT reached stage 20 of [Fair play?](../quests/brv_blackjack.md#stage-20); reached stage 130 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-130))* → [brv_zimsko_30](#d-brv_zimsko_30)
    - “I want to find out what's happening in the back room, but they want a password.” *(if reached stage 20 of [Fair play?](../quests/brv_blackjack.md#stage-20); reached stage 10 of [Fair play?](../quests/brv_blackjack.md#stage-10); NOT reached stage 30 of [Fair play?](../quests/brv_blackjack.md#stage-30))* → [brv_zimsko_30_2](#d-brv_zimsko_30_2)
    - “I want to find out what's happening in the back room.” *(if reached stage 20 of [Fair play?](../quests/brv_blackjack.md#stage-20); NOT reached stage 10 of [Fair play?](../quests/brv_blackjack.md#stage-10); NOT reached stage 30 of [Fair play?](../quests/brv_blackjack.md#stage-30))* → [brv_zimsko_30_1](#d-brv_zimsko_30_1)
    - “I want to talk to you about the gamblers.” *(if reached stage 30 of [Fair play?](../quests/brv_blackjack.md#stage-30); NOT reached stage 70 of [Fair play?](../quests/brv_blackjack.md#stage-70); NOT reached stage 80 of [Fair play?](../quests/brv_blackjack.md#stage-80))* → [brv_zimsko_40](#d-brv_zimsko_40)

    <span id="d-brv_zimsko_40_2"></span>**`brv_zimsko_40_2`** Zimsko: “Thats what I thought. Thank you for your help.” — **effects:** sets stage 70 of [Fair play?](../quests/brv_blackjack.md#stage-70)

    - Next → [brv_zimsko_20_1](#d-brv_zimsko_20_1)

    <span id="d-brv_zimsko_40_3"></span>**`brv_zimsko_40_3`** Zimsko: “That's what I thought. Thank you for your help and the fight. Someone had to do it.” — **effects:** sets stage 70 of [Fair play?](../quests/brv_blackjack.md#stage-70)


    <span id="d-brv_zimsko_40_1"></span>**`brv_zimsko_40_1`** Zimsko: “I still believe they are cheating. Thanks anyway.” — **effects:** sets stage 80 of [Fair play?](../quests/brv_blackjack.md#stage-80)

    - Next → [brv_zimsko_20_1](#d-brv_zimsko_20_1)

    <span id="d-brv_zimsko_30"></span>**`brv_zimsko_30`** Zimsko: “I lost all my money gambling in the backroom. I think they are cheating.” — **effects:** sets stage 20 of [Fair play?](../quests/brv_blackjack.md#stage-20)

    - “Oh, bad luck.” → [brv_zimsko_20_1](#d-brv_zimsko_20_1)
    - “I will go and play with them to find out if they are cheating.” *(if NOT reached stage 10 of [Fair play?](../quests/brv_blackjack.md#stage-10))* → [brv_zimsko_30_1](#d-brv_zimsko_30_1)
    - “I want to find out what's happening in the back room, but they want a password.” *(if reached stage 10 of [Fair play?](../quests/brv_blackjack.md#stage-10))* → [brv_zimsko_30_2](#d-brv_zimsko_30_2)

    <span id="d-brv_zimsko_30_2"></span>**`brv_zimsko_30_2`** Zimsko: “Thanks for trying to find out more. The password for entering the back room is... [he whispers the password in your ear.] You have to win and lose a few times until they trust you and play for higher amounts. Then they start cheating.” — **effects:** sets stage 30 of [Fair play?](../quests/brv_blackjack.md#stage-30), sets stage 31 of [Fair play?](../quests/brv_blackjack.md#stage-31)

    - Next → [brv_zimsko_20_1](#d-brv_zimsko_20_1)

    <span id="d-brv_zimsko_30_1"></span>**`brv_zimsko_30_1`** Zimsko: “Thanks for trying to find out more. But you will need a password for entering the back room. [He whispers the password in your ear.] You have to win and lose a few times until they trust you and play for higher amounts. Then they start…” — **effects:** sets stage 30 of [Fair play?](../quests/brv_blackjack.md#stage-30), sets stage 31 of [Fair play?](../quests/brv_blackjack.md#stage-31)

    - Next → [brv_zimsko_20_1](#d-brv_zimsko_20_1)



## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 17 lines added |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 5 lines changed<br>· text: “You again” → “You again?” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `zimsko` |
    | Spawn group | `zimsko` |
    | Loot table | – |
    | Conversation | `brv_zimsko_select` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men2:9` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "zimsko",
     "name": "Zimsko",
     "iconID": "monsters_men2:9",
     "unique": 1,
     "spawnGroup": "zimsko",
     "phraseID": "brv_zimsko_select"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=zimsko.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=zimsko.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=zimsko.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=zimsko.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
