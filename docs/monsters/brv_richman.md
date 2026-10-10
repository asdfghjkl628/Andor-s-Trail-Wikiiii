---
description: "Alkapoan is a non-player character (NPC) in Andor's Trail, found in Brimhaven house 1."
---

# ![](../assets/icons/monsters/monsters_tometik1_2.png){ .sprite } Alkapoan

**Where to find Alkapoan:** [Brimhaven house 1](../maps/brimhaven_house1.md#pin-npc-brv_richman)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_tometik1_2.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Brimhaven house 1 |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

## Quests

- [A place to forge](../quests/place_to_forge.md): stages 30, 35, 40, 50
- [Much water](../quests/brv_flood.md): stages 130, 150
- [Search for Andor](../quests/andor.md): stages 65, 912
- [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md): stages 110, 120
- [Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md): stage 22
- [Undertell story flags (hidden flag)](../quests/undertell_hidden.md): stage 15

## Dialogue simulator

Talk to Alkapoan as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_richman.json" data-npc="Alkapoan" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (38 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_richman"></span>**`brv_richman`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 21 of [Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md#stage-21); NOT reached stage 22 of [Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md#stage-22); faction “andor_ending” ≥ 1)* → [mg2_richman_10](#d-mg2_richman_10)
    - branch 2 *(if reached stage 22 of [Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md#stage-22); reached stage 23 of [Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md#stage-23); faction “andor_ending” ≥ 1)* → [mg2_richman_20](#d-mg2_richman_20)
    - branch 3 *(if reached stage 200 of [Much water](../quests/brv_flood.md#stage-200))* → [brv_guard_captain_and_rich_man](#d-brv_guard_captain_and_rich_man)
    - branch 4 *(if reached stage 150 of [Much water](../quests/brv_flood.md#stage-150))* → [brv_richman_25](#d-brv_richman_25)
    - branch 5 *(if reached stage 130 of [Much water](../quests/brv_flood.md#stage-130))* → [brv_richman_15](#d-brv_richman_15)
    - branch 6 → [brv_richman_01](#d-brv_richman_01)

    <span id="d-mg2_richman_10"></span>**`mg2_richman_10`** Alkapoan: “Oh, I know that look on their faces. Someone here wants to order something discreet.”

    - “Indeed. I want to expand a basement.” → [mg2_richman_12](#d-mg2_richman_12)

    <span id="d-mg2_richman_20"></span>**`mg2_richman_20`** Alkapoan: “Ah, my new homeowner. Do you like the renovation?”

    - “It's just perfect.” → *ends*

    <span id="d-brv_guard_captain_and_rich_man"></span>**`brv_guard_captain_and_rich_man`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 15 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-15); NOT reached stage 50 of [A place to forge](../quests/place_to_forge.md#stage-50))* → [talk_about_white_house_20](#d-talk_about_white_house_20)
    - branch 2 *(if reached stage 120 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-120))* → [brv_guard_captain_and_rich_man_50](#d-brv_guard_captain_and_rich_man_50)
    - branch 3 *(if reached stage 110 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-110))* → [brv_guard_captain_and_rich_man_40](#d-brv_guard_captain_and_rich_man_40)
    - branch 4 → [brv_guard_captain_and_rich_man_10](#d-brv_guard_captain_and_rich_man_10)

    <span id="d-brv_richman_25"></span>**`brv_richman_25`** Alkapoan: “Leave me alone. I will wait here for the guards to arrest me.”


    <span id="d-brv_richman_15"></span>**`brv_richman_15`** Alkapoan: “You again. I already told you that I know nothing about the destruction of the dam.”

    - “I don't believe a word you say. [Half-lie] The two brothers told me that you paid them for destroying the dam.” *(if reached stage 120 of [Much water](../quests/brv_flood.md#stage-120))* → [brv_richman_20](#d-brv_richman_20)
    - “Maybe you are right, sorry.” → *conversation ends*
    - “I found your coin bags, and you paid the brothers for destroying the dam. [Hand him the coin bags]” *(if hand over 1× [Coin bag (with the name "Alkapoan" on it)](../items/brv_richmans_coin_bag.md))* → [brv_richman_20](#d-brv_richman_20)

    <span id="d-brv_richman_01"></span>**`brv_richman_01`** Alkapoan: “I do not remember inviting you to my house.”

    - “What do you know about the destruction of the dam?” *(if reached stage 110 of [Much water](../quests/brv_flood.md#stage-110); NOT reached stage 150 of [Much water](../quests/brv_flood.md#stage-150))* → [brv_richman_05](#d-brv_richman_05)
    - “I am sorry and will leave.” → *conversation ends*

    <span id="d-mg2_richman_12"></span>**`mg2_richman_12`** Alkapoan: “Hmm, I don't run a construction company, but you seem to have something unusual in mind. Well, I'm sure I can help you. For a reasonable amount of gold, of course.”

    - “Of course. It's about an abandoned property far in the southeast.” → [mg2_richman_12b](#d-mg2_richman_12b)

    <span id="d-talk_about_white_house_20"></span>**`talk_about_white_house_20`** [Alkapoan](../monsters/brv_richman.md): “What do you want, foolish child?” — **effects:** sets stage 15 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-15)

    - “I've collected your 'operation tax' from the dealer. Now let's finish our deal.” *(if latest stage of [A place to forge](../quests/place_to_forge.md#stage-45) is 45)* → [alkapoan_lie_wh_50](#d-alkapoan_lie_wh_50)
    - “[lie] I want the glowing white house. I need a place to hide from my parents.” *(if NOT reached stage 30 of [A place to forge](../quests/place_to_forge.md#stage-30); NOT reached stage 45 of [A place to forge](../quests/place_to_forge.md#stage-45))* → [alkapoan_lie_wh_10](#d-alkapoan_lie_wh_10)
    - “Nocmar has sent me to get back what was once his.” *(if NOT reached stage 35 of [A place to forge](../quests/place_to_forge.md#stage-35))* → [alkapoan_nocmar_wh_10](#d-alkapoan_nocmar_wh_10)

    <span id="d-brv_guard_captain_and_rich_man_50"></span>**`brv_guard_captain_and_rich_man_50`** [Mustura](../monsters/brv_guard_captain.md): “You better disappear soon, or I might find some evidence that you are the evil spy from Loneford.”

    - “We are all reasonable people here. Let us settle this, shall we?” → [talk_about_white_house_10](#d-talk_about_white_house_10)

    <span id="d-brv_guard_captain_and_rich_man_40"></span>**`brv_guard_captain_and_rich_man_40`** [Mustura](../monsters/brv_guard_captain.md): “It seems Alkapoan's letters accidentally fell into a fire and I am sure some unknown evil spies from Loneford destroyed the dam. You better disappear soon, or I might find some evidence that you are the evil spy from Loneford.” — **effects:** sets stage 120 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-120)


    <span id="d-brv_guard_captain_and_rich_man_10"></span>**`brv_guard_captain_and_rich_man_10`** [Alkapoan](../monsters/brv_richman.md): “[Laughs] You again. Welcome back, foolish child.”

    - “Laugh while you can. The captain is here and now you will get your deserved punishment!” → [brv_guard_captain_and_rich_man_20](#d-brv_guard_captain_and_rich_man_20)

    <span id="d-brv_richman_20"></span>**`brv_richman_20`** Alkapoan: “[Breaks down] I was bribed by the people of Loneford to sabotage the dam. Here are some letters I exchanged with them, that prove what I did. [The handwriting looks like that of my brother.]” — **effects:** sets stage 150 of [Much water](../quests/brv_flood.md#stage-150), gives 1× [Alkapoans's letters](../items/alkapoans_letters.md), sets stage 65 of [Search for Andor](../quests/andor.md#stage-65)

    - “You were honest to me so I will not kill you, but I will tell the guard captain. (And you can't escape from Brimhaven…” *(if NOT reached stage 80 of [Much water](../quests/brv_flood.md#stage-80))* → [brv_richman_25](#d-brv_richman_25)
    - “I stopped the two brothers from destroying the dam. Who else could have done it?” *(if reached stage 80 of [Much water](../quests/brv_flood.md#stage-80))* → [brv_richman_21](#d-brv_richman_21)

    <span id="d-brv_richman_05"></span>**`brv_richman_05`** Alkapoan: “It is very sad that the dam was destroyed. But I don't know anything.”

    - “OK, thank you.” → *conversation ends*
    - “Are you sure?” *(if reached stage 120 of [Much water](../quests/brv_flood.md#stage-120))* → [brv_richman_10](#d-brv_richman_10)
    - “Are you sure?” *(if carry 1× [Coin bag (with the name "Alkapoan" on it)](../items/brv_richmans_coin_bag.md))* → [brv_richman_10](#d-brv_richman_10)

    <span id="d-mg2_richman_12b"></span>**`mg2_richman_12b`** Alkapoan: “No problem.”

    - “Up on a mountain.” → [mg2_richman_12c](#d-mg2_richman_12c)

    <span id="d-alkapoan_lie_wh_50"></span>**`alkapoan_lie_wh_50`** Alkapoan: “Sure thing! As soon as I see forty-five thousand gold, you will see the deed to the house. Remember, you have my 'operation tax' gold too.”

    - “Forty-five thousand?! I don't have that kind of gold.” *(if NOT have 45,000 gold)* → [alkapoan_not_enough_gold](#d-alkapoan_not_enough_gold)
    - “Here, take the fourty-five thousand and give me the deed and the key.” *(if pay 45,000 gold)* → [alkapoan_nocmar_wh_give_deed](#d-alkapoan_nocmar_wh_give_deed)

    <span id="d-alkapoan_lie_wh_10"></span>**`alkapoan_lie_wh_10`** Alkapoan: “You want the house for yourself? Now that is interesting. Most people shy away from that cursed glow, but I can see ambition in your eyes. Hm. I could let it go for forty thousand gold...but gold alone won't earn my trust. If I sell it to…” — **effects:** sets stage 35 of [A place to forge](../quests/place_to_forge.md#stage-35)

    - “Proof, how?” → [alkapoan_lie_wh_20](#d-alkapoan_lie_wh_20)

    <span id="d-alkapoan_nocmar_wh_10"></span>**`alkapoan_nocmar_wh_10`** Alkapoan: “Ah...so this is for Nocmar? The man who couldn't pay his debt and lost everything. And now you want me to just hand it back? Hah! If he wants redemption, let him pay double what he owed. Fifty thousand gold, no less. You bring me that…” — **effects:** sets stage 30 of [A place to forge](../quests/place_to_forge.md#stage-30)

    - “Fifty thousand gold?! Are you nuts? How about twenty-five housand?” → [alkapoan_bargin](#d-alkapoan_bargin)
    - “Fifty thousand gold? I don't have it.” *(if NOT have 50,000 gold)* → [alkapoan_not_enough_gold](#d-alkapoan_not_enough_gold)
    - “Here, take the fifty thousand and give me the deed and the key.” *(if pay 50,000 gold)* → [alkapoan_nocmar_wh_give_deed](#d-alkapoan_nocmar_wh_give_deed)

    <span id="d-talk_about_white_house_10"></span>**`talk_about_white_house_10`** Alkapoan: “You are reasonable?”

    - “Whatever!” *(if NOT reached stage 10 of [A place to forge](../quests/place_to_forge.md#stage-10))* → *conversation ends*
    - “Oh, for the purposes of this conversation? Yeah, yeah I am. I want to talk to Alkapoan, not you!” *(if latest stage of [A place to forge](../quests/place_to_forge.md#stage-20) is 20)* → [talk_about_white_house_20](#d-talk_about_white_house_20)

    <span id="d-brv_guard_captain_and_rich_man_20"></span>**`brv_guard_captain_and_rich_man_20`** [Mustura](../monsters/brv_guard_captain.md): “Well...”

    - Next → [brv_guard_captain_and_rich_man_30](#d-brv_guard_captain_and_rich_man_30)

    <span id="d-brv_richman_21"></span>**`brv_richman_21`** Alkapoan: “I don't know. Maybe it was the deliverer of the letters. [Oh no, it could have been Andor who destroyed the dam!]”

    - Next → [brv_richman_25](#d-brv_richman_25)

    <span id="d-brv_richman_10"></span>**`brv_richman_10`** Alkapoan: “I... I.... know nothing. Really, it is the truth!” — **effects:** sets stage 130 of [Much water](../quests/brv_flood.md#stage-130)

    - “I don't believe a word you say. [Half-lie] The two brothers told me that you paid them for destroying the dam.” *(if reached stage 120 of [Much water](../quests/brv_flood.md#stage-120))* → [brv_richman_20](#d-brv_richman_20)
    - “Maybe you are right, sorry.” → *conversation ends*
    - “I found your coin bags, and you paid the brothers to destroy the dam. [Show the coin bags]” *(if carry 1× [Coin bag (with the name "Alkapoan" on it)](../items/brv_richmans_coin_bag.md))* → [brv_richman_20](#d-brv_richman_20)

    <span id="d-mg2_richman_12c"></span>**`mg2_richman_12c`** Alkapoan: “No problem.”

    - “In the ice, on the summit.” → [mg2_richman_12d](#d-mg2_richman_12d)

    <span id="d-alkapoan_not_enough_gold"></span>**`alkapoan_not_enough_gold`** Alkapoan: “Well, then you better go find it.”


    <span id="d-alkapoan_nocmar_wh_give_deed"></span>**`alkapoan_nocmar_wh_give_deed`** Alkapoan: “A pleasure doing business with you.” — **effects:** sets stage 50 of [A place to forge](../quests/place_to_forge.md#stage-50), gives 1× [White house deed](../items/white_house_deed.md), gives 1× [White house key](../items/white_house_key.md)


    <span id="d-alkapoan_lie_wh_20"></span>**`alkapoan_lie_wh_20`** Alkapoan: “There's a small matter I want handled. Do this, and the price will stay at forty thousand. Refuse, and I'll reconsider whether you're worth the trouble.”

    - “What do you want from me?” → [alkapoan_lie_wh_30](#d-alkapoan_lie_wh_30)

    <span id="d-alkapoan_bargin"></span>**`alkapoan_bargin`** Alkapoan: “Yeah, sure, twenty-five thousand and I take a couple of your fingers too?”


    <span id="d-brv_guard_captain_and_rich_man_30"></span>**`brv_guard_captain_and_rich_man_30`** [Alkapoan](../monsters/brv_richman.md): “Let's see who is laughing in the end. The captain came to talk, not arrest me. Now she owns a new horse and I will be earning a lot of money with the necessary repairing of the dam and later the food harvesting. I call this a win-win.” — **effects:** sets stage 110 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-110)

    - Next → [brv_guard_captain_and_rich_man_40](#d-brv_guard_captain_and_rich_man_40)

    <span id="d-mg2_richman_12d"></span>**`mg2_richman_12d`** Alkapoan: “No problem.”

    - “Of Mt.Galmore.” → [mg2_richman_12e](#d-mg2_richman_12e)

    <span id="d-alkapoan_lie_wh_30"></span>**`alkapoan_lie_wh_30`** Alkapoan: “If you want the house, I'll need proof that you can handle business my way. There's a card dealer who runs games in the back of the tavern here in Brimhaven. He operates because I allow it. That means he owes me a regular fee, call it an…”

    - “Okay?” → [alkapoan_lie_wh_40](#d-alkapoan_lie_wh_40)

    <span id="d-mg2_richman_12e"></span>**`mg2_richman_12e`** Alkapoan: “No ... WHAT?!!”

    - “Of Mt.Galmore. Well, if you don't want to do it...” → [mg2_richman_14](#d-mg2_richman_14)

    <span id="d-alkapoan_lie_wh_40"></span>**`alkapoan_lie_wh_40`** Alkapoan: “He's late. Bring me what he owes, and don't let him wiggle out of it. I want every bit of the five thousand gold. When you return with the gold, I'll know you're serious, and the deed will be yours for forty thousand more.” — **effects:** sets stage 40 of [A place to forge](../quests/place_to_forge.md#stage-40)

    - “I'll be right back. Keep that deed handy.” → *conversation ends*

    <span id="d-mg2_richman_14"></span>**`mg2_richman_14`** Alkapoan: “Not so fast. Of course I can help you. I'm just a little ... surprised.”

    - Next → [mg2_richman_14b](#d-mg2_richman_14b)

    <span id="d-mg2_richman_14b"></span>**`mg2_richman_14b`** Alkapoan: “And it won't be ... cheap.”

    - Next → [mg2_richman_14c](#d-mg2_richman_14c)

    <span id="d-mg2_richman_14c"></span>**`mg2_richman_14c`** Alkapoan: “What exactly do you have in mind?”

    - “Well, finally you're talking sensibly. Look, I want the following ...” → [mg2_richman_16](#d-mg2_richman_16)

    <span id="d-mg2_richman_16"></span>**`mg2_richman_16`** [Dummy NPC](../monsters/none.md): “You give him a piece of paper with your ideas and instructions on how to build it.”

    - “Now?” → [mg2_richman_16b](#d-mg2_richman_16b)

    <span id="d-mg2_richman_16b"></span>**`mg2_richman_16b`** [Alkapoan](../monsters/brv_richman.md): “Well, that's something different for a change. It will cost you 50,000 gold pieces.”

    - “Good. Of course I don't have the money with me. But I'll be back.” → *conversation ends*
    - “OK, here you get 50,000. Make something good out of it.” *(if pay 50,000 gold)* → [mg2_richman_18](#d-mg2_richman_18)
    - “You get 25,000. Be happy, that's plenty.” *(if pay 25,000 gold; NOT pay 50,000 gold)* → [mg2_richman_18](#d-mg2_richman_18)

    <span id="d-mg2_richman_18"></span>**`mg2_richman_18`** Alkapoan: “So be it. You will be amazed how quickly we work.” — **effects:** sets stage 22 of [Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md#stage-22), faction “cavea_down” set to 2, clears stage 999 of [Search for Andor](../quests/andor.md#stage-999), sets stage 912 of [Search for Andor](../quests/andor.md#stage-912), removes monsters from galmore_cavea, removes monsters from galmore_cavea, removes monsters from galmore_cavea_1, removes monsters from galmore_cavea_1, removes monsters from galmore_cavea_2




## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 13 lines added |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 1 line added, 4 lines changed<br>· text: “[Laughs] You again” → “[Laughs] You again. Welcome back, foolish child.”<br>· text: “Better you disapear soon or I might find some evidence that you are t…” → “You better disappear soon, or I might find some evidence that you are…” |
| [v0.8.14](../versions/0.8.14.md) | Dialogue: 13 lines added, 1 line changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 11 lines added, 2 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brv_richman` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_richman` |
    | Loot table | `brv_richman` |
    | Conversation | `brv_richman` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik1:2` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_richman",
     "name": "Alkapoan",
     "iconID": "monsters_tometik1:2",
     "phraseID": "brv_richman",
     "droplistID": "brv_richman"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_richman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_richman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_richman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_richman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
