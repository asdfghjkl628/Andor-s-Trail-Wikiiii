---
description: "Mayor Ale is a non-player character (NPC) in Andor's Trail, found in Sullengard."
---

# ![](../assets/icons/monsters/monsters_mage_0.png){ .sprite } Mayor Ale

**Where to find Mayor Ale:** Sullengard: [sullengard1_townhall](../maps/sullengard1_townhall.md#pin-npc-sullengard_mayor)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_mage_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Sullengard |
| **Entry ID** | `sullengard_mayor` |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Quests

- [Another ruthless Crackshot](../quests/Thieves04.md): stage 75
- [Beer Bootlegging](../quests/beer_bootlegging.md): stages 60, 80
- [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md): stages 25, 30

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Mayor Ale. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/sullengard_mayor.json" data-npc="Mayor Ale" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (35 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-sullengard_mayor"></span>**`sullengard_mayor`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 25 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-25); latest stage of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-30) is 30)* → [sullengard_mayor_10](#d-sullengard_mayor_10)
    - branch 2 *(if latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-50) is 50)* → [sullengard_mayor_beer_0](#d-sullengard_mayor_beer_0)
    - branch 3 *(if latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-70) is 70)* → [sullengard_mayor_letter_delivered](#d-sullengard_mayor_letter_delivered)
    - branch 4 *(if latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-60) is 60)* → [sullengard_mayor_no_letter_delivered](#d-sullengard_mayor_no_letter_delivered)
    - branch 5 *(if faction “gold_contribute” ≥ 50000)* → [sullengard_mayor_5](#d-sullengard_mayor_5)
    - branch 6 → [sullengard_mayor_1](#d-sullengard_mayor_1)

    <span id="d-sullengard_mayor_10"></span>**`sullengard_mayor_10`** Mayor Ale: “What's on your mind? I can see it in your eyes. You have questions.”

    - “I'm looking into the break-in and robbery at Zaccheria's shop and I am wondering if you saw or know anything about it?” → [sullengard_mayor_20](#d-sullengard_mayor_20)

    <span id="d-sullengard_mayor_beer_0"></span>**`sullengard_mayor_beer_0`** Mayor Ale: “How can I be of service to you my friend?”

    - “Can you tell me about your 'business agreement' with your beer 'distributors'?” → [sullengard_mayor_beer](#d-sullengard_mayor_beer)
    - “We want to contribute gold coins for your financial loss.” *(if NOT faction “gold_contribute” ≥ 50000; reached stage 70 of [Another ruthless Crackshot](../quests/Thieves04.md#stage-70))* → [sullengard_mayor_4](#d-sullengard_mayor_4)

    <span id="d-sullengard_mayor_letter_delivered"></span>**`sullengard_mayor_letter_delivered`** Mayor Ale: “Thank you for delivering my letter to Kealwea.”

    - “How did you know?” → [sullengard_mayor_beer_50](#d-sullengard_mayor_beer_50)
    - “We want to contribute gold coins for your financial loss.” *(if NOT faction “gold_contribute” ≥ 50000; reached stage 70 of [Another ruthless Crackshot](../quests/Thieves04.md#stage-70))* → [sullengard_mayor_4](#d-sullengard_mayor_4)

    <span id="d-sullengard_mayor_no_letter_delivered"></span>**`sullengard_mayor_no_letter_delivered`** Mayor Ale: “Why have you not delivered my letter to Kealwea yet?”

    - “How did you know that?” → [sullengard_mayor_beer_letter_not_delivered_10](#d-sullengard_mayor_beer_letter_not_delivered_10)
    - “We want to contribute gold coins for your financial loss.” *(if NOT faction “gold_contribute” ≥ 50000; reached stage 70 of [Another ruthless Crackshot](../quests/Thieves04.md#stage-70))* → [sullengard_mayor_4](#d-sullengard_mayor_4)

    <span id="d-sullengard_mayor_5"></span>**`sullengard_mayor_5`** Mayor Ale: “Thank you so much again, kid. You are just like your brother Andor. After we are done speaking, you really should speak with my assistant, Maddalena.” — **effects:** sets stage 30 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-30), sets stage 75 of [Another ruthless Crackshot](../quests/Thieves04.md#stage-75)

    - “Of course, he is my brother.” → [sullengard_mayor_6](#d-sullengard_mayor_6)
    - “How did you know?” → [sullengard_mayor_6](#d-sullengard_mayor_6)

    <span id="d-sullengard_mayor_1"></span>**`sullengard_mayor_1`** Mayor Ale: “Welcome to Sullengard, kid. Happy 20th beer celebration!”

    - “Cheers!” → *conversation ends*
    - “Do you know where Defy is?” *(if reached stage 40 of [Another ruthless Crackshot](../quests/Thieves04.md#stage-40))* → [sullengard_mayor_2](#d-sullengard_mayor_2)
    - “We want to contribute gold coins for your financial loss.” *(if NOT faction “gold_contribute” ≥ 50000; reached stage 70 of [Another ruthless Crackshot](../quests/Thieves04.md#stage-70))* → [sullengard_mayor_4](#d-sullengard_mayor_4)

    <span id="d-sullengard_mayor_20"></span>**`sullengard_mayor_20`** Mayor Ale: “I heard you are helping Zaccheria in tracking down who stole his inventory.”

    - “Yes. Hence my reason for asking you about it.” → [sullengard_mayor_30](#d-sullengard_mayor_30)

    <span id="d-sullengard_mayor_beer"></span>**`sullengard_mayor_beer`** Mayor Ale: “What? I am afraid that I have no idea what you are asking.”

    - “Oh, but I am sure you do. [You lean in closer to the mayor] Just between us, we both know that you do know.” → [sullengard_mayor_beer_10](#d-sullengard_mayor_beer_10)
    - “Sorry. I'll leave you now” → *conversation ends*

    <span id="d-sullengard_mayor_4"></span>**`sullengard_mayor_4`** Mayor Ale: “Finally, at least we can survive for a day with a beer and some bread.”

    - “Here's 50,000 gold coins.” *(if NOT faction “gold_contribute” ≥ 50000; pay 50,000 gold)* → [sullengard_mayor_4a](#d-sullengard_mayor_4a)
    - “Here's 20,000 gold coins.” *(if NOT faction “gold_contribute” ≥ 50000; pay 20,000 gold)* → [sullengard_mayor_4b](#d-sullengard_mayor_4b)
    - “Here's 10,000 gold coins.” *(if NOT faction “gold_contribute” ≥ 50000; pay 10,000 gold)* → [sullengard_mayor_4c](#d-sullengard_mayor_4c)
    - “Here's 5,000 gold coins.” *(if NOT faction “gold_contribute” ≥ 50000; pay 5,000 gold)* → [sullengard_mayor_4d](#d-sullengard_mayor_4d)
    - “I noticed that I'm running out of money. I'll be back.” → *conversation ends*

    <span id="d-sullengard_mayor_beer_50"></span>**`sullengard_mayor_beer_50`** Mayor Ale: “I had one of my people follow you. After all, I wasn't sure that you could be trusted.”

    - “Oh, I see. Now do you trust me?” → [sullengard_mayor_beer_60](#d-sullengard_mayor_beer_60)
    - “Now can you trust me to let me know more about the 'business agreement'” → [sullengard_mayor_beer_60](#d-sullengard_mayor_beer_60)

    <span id="d-sullengard_mayor_beer_letter_not_delivered_10"></span>**`sullengard_mayor_beer_letter_not_delivered_10`** Mayor Ale: “I have my ways of knowing. After all, I am the mayor.”

    - “I guess you do.” → *conversation ends*

    <span id="d-sullengard_mayor_6"></span>**`sullengard_mayor_6`** Mayor Ale: “He is taller than you, of course, but you guys have a very similiar looking face. He is one of the most active members in your guild.”

    - “Oh, is he?” → [sullengard_mayor_7](#d-sullengard_mayor_7)

    <span id="d-sullengard_mayor_2"></span>**`sullengard_mayor_2`** Mayor Ale: “No. We still don't know where that traitor is. How can we ever sleep peacefully and live sufficiently with this tragic situation?”

    - Next → [sullengard_mayor_3](#d-sullengard_mayor_3)

    <span id="d-sullengard_mayor_30"></span>**`sullengard_mayor_30`** Mayor Ale: “I wish I knew more, but I don't. Maybe ask around near the tavern?” — **effects:** sets stage 25 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-25)


    <span id="d-sullengard_mayor_beer_10"></span>**`sullengard_mayor_beer_10`** Mayor Ale: “What do you know?”

    - “Farrik told me a little bit about your operation.” → [sullengard_mayor_beer_15](#d-sullengard_mayor_beer_15)
    - “Well, I know that the Thieves guild is your 'distributor'.” → [sullengard_mayor_beer_20](#d-sullengard_mayor_beer_20)

    <span id="d-sullengard_mayor_4a"></span>**`sullengard_mayor_4a`** Mayor Ale: “I have no words to express my gratitude.” — **effects:** faction “gold_contribute” +50000

    - “Oh wait. There's more.” *(if NOT faction “gold_contribute” ≥ 50000)* → [sullengard_mayor_4](#d-sullengard_mayor_4)
    - “That's all of the coins we owe you and your people, Mayor Ale.” *(if faction “gold_contribute” ≥ 50000)* → [sullengard_mayor_5](#d-sullengard_mayor_5)

    <span id="d-sullengard_mayor_4b"></span>**`sullengard_mayor_4b`** Mayor Ale: “Oh my, thank you kid.” — **effects:** faction “gold_contribute” +20000

    - “Oh wait. There's more.” *(if NOT faction “gold_contribute” ≥ 50000)* → [sullengard_mayor_4](#d-sullengard_mayor_4)
    - “That's all, mayor Ale.” *(if faction “gold_contribute” ≥ 50000)* → [sullengard_mayor_5](#d-sullengard_mayor_5)

    <span id="d-sullengard_mayor_4c"></span>**`sullengard_mayor_4c`** Mayor Ale: “We appreciate it. Thank you, kid.” — **effects:** faction “gold_contribute” +10000

    - “Oh wait. There's more.” *(if NOT faction “gold_contribute” ≥ 50000)* → [sullengard_mayor_4](#d-sullengard_mayor_4)
    - “That's all, mayor Ale.” *(if faction “gold_contribute” ≥ 50000)* → [sullengard_mayor_5](#d-sullengard_mayor_5)

    <span id="d-sullengard_mayor_4d"></span>**`sullengard_mayor_4d`** Mayor Ale: “Small successes cometh before big ones.” — **effects:** faction “gold_contribute” +5000

    - “Oh wait. There's more.” *(if NOT faction “gold_contribute” ≥ 50000)* → [sullengard_mayor_4](#d-sullengard_mayor_4)
    - “That's all, mayor Ale.” *(if faction “gold_contribute” ≥ 50000)* → [sullengard_mayor_5](#d-sullengard_mayor_5)

    <span id="d-sullengard_mayor_beer_60"></span>**`sullengard_mayor_beer_60`** Mayor Ale: “Yes. You have proven yourself to me.”

    - “Finally! Now start talking. I'm getting annoyed.” → [sullengard_mayor_beer_70](#d-sullengard_mayor_beer_70)
    - “Great. Let's hear it.” → [sullengard_mayor_beer_70](#d-sullengard_mayor_beer_70)

    <span id="d-sullengard_mayor_7"></span>**`sullengard_mayor_7`** Mayor Ale: “He was considered as the helping hand of Sullengard during rough days. Not unlike this scenario.”

    - “I'm glad to help.” → *conversation ends*
    - “That's our job.” → *conversation ends*

    <span id="d-sullengard_mayor_3"></span>**`sullengard_mayor_3`** Mayor Ale: “But please talk to my fellow bootleg brewers. Maybe they know something.”

    - “I will. Stay strong.” → *conversation ends*
    - “Bah! Useless mayor.” → *conversation ends*

    <span id="d-sullengard_mayor_beer_15"></span>**`sullengard_mayor_beer_15`** Mayor Ale: “I don't know any 'Farrik'.”


    <span id="d-sullengard_mayor_beer_20"></span>**`sullengard_mayor_beer_20`** Mayor Ale: “Then that must mean that you are someone that they trust?”

    - “I guess you could say that.” → [sullengard_mayor_beer_30](#d-sullengard_mayor_beer_30)

    <span id="d-sullengard_mayor_beer_70"></span>**`sullengard_mayor_beer_70`** Mayor Ale: “Pull-up a chair kid and listen to the facts.”

    - “Oh, no! Another long-winded story. OK, let's get this over with.” → [sullengard_mayor_beer_80](#d-sullengard_mayor_beer_80)

    <span id="d-sullengard_mayor_beer_30"></span>**`sullengard_mayor_beer_30`** Mayor Ale: “Maybe, just maybe.”

    - Next → [sullengard_mayor_beer_35](#d-sullengard_mayor_beer_35)

    <span id="d-sullengard_mayor_beer_80"></span>**`sullengard_mayor_beer_80`** Mayor Ale: “You see, this all started many years ago before Lord Geomyr grew into power. The Sullengard brewers have been perfecting their beer brewing for many years and selling it outside of town for almost as long.”

    - “Sounds like they are experts.” → [sullengard_mayor_beer_90](#d-sullengard_mayor_beer_90)

    <span id="d-sullengard_mayor_beer_35"></span>**`sullengard_mayor_beer_35`** Mayor Ale: “But how can you prove it to me?...Uh, I know. You can deliver this letter for me. Here, take it to Kealwea and return to me afterwards.” — **effects:** sets stage 60 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-60), gives 1× [Mayor Ale's letter](../items/sullengard_mayor_letter.md)

    - “Um, OK, I guess.” → *conversation ends*

    <span id="d-sullengard_mayor_beer_90"></span>**`sullengard_mayor_beer_90`** Mayor Ale: “Well, yes they are when it comes to brewing the beer, but not so much when it comes to selling it. Even before Lord Geomyr grew into power, the citizens of Sullengard always had a hard time selling their beer.”

    - “Please go on.” → [sullengard_mayor_beer_100](#d-sullengard_mayor_beer_100)

    <span id="d-sullengard_mayor_beer_100"></span>**`sullengard_mayor_beer_100`** Mayor Ale: “Not so much selling it because that was easy. After all, we have the best product in Dhayavar. But the problem was getting to the other towns safely and with a fresh batch.”

    - Next → [sullengard_mayor_beer_105](#d-sullengard_mayor_beer_105)

    <span id="d-sullengard_mayor_beer_105"></span>**`sullengard_mayor_beer_105`** Mayor Ale: “Then after Lord Geomyr came to power and more specifically, after he decided to lay down such an unjust tax upon our beer sales, we desperately needed a 'distributor'.”

    - “Oh, that makes sense to me. But why the Thieves guild?” → [sullengard_mayor_beer_110](#d-sullengard_mayor_beer_110)

    <span id="d-sullengard_mayor_beer_110"></span>**`sullengard_mayor_beer_110`** Mayor Ale: “The decision was easy. We had done plenty of business with them in the past and they never did us wrong. Plus, they have the skills and resources to discreetly distribute our beer without Feygard interference.”

    - “I can't argue with that logic.” → [sullengard_mayor_beer_115](#d-sullengard_mayor_beer_115)
    - “But you are breaking the laws of Feygard. Aren't you afraid you will get caught?” → [sullengard_mayor_beer_120](#d-sullengard_mayor_beer_120)

    <span id="d-sullengard_mayor_beer_115"></span>**`sullengard_mayor_beer_115`** Mayor Ale: “Please keep this information to yourself.” — **effects:** sets stage 80 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-80)


    <span id="d-sullengard_mayor_beer_120"></span>**`sullengard_mayor_beer_120`** Mayor Ale: “Not as much as we fear not being able to make a living selling our beer. Plus, we have the support of the people of Nor City” — **effects:** sets stage 80 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-80)




## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 35 lines added |
| [v0.8.4](../versions/0.8.4.md) | Dialogue: 1 line changed |
| [v0.8.8](../versions/0.8.8.md) | Dialogue: 1 line changed<br>· text: “Thank you so much again, kid. You are just like your brother Andor.” → “Thank you so much again, kid. You are just like your brother Andor. A…” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `sullengard_mayor` |
    | Spawn group | `sullengard_mayor` |
    | Loot table | – |
    | Conversation | `sullengard_mayor` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_mage:0` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "sullengard_mayor",
     "name": "Mayor Ale",
     "iconID": "monsters_mage:0",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "sullengard_mayor",
     "phraseID": "sullengard_mayor"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_mayor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_mayor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_mayor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_mayor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
