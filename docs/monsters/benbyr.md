# ![](../assets/icons/monsters/monsters_rltiles1_74.png){ .sprite } Benbyr

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_74.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `benbyr` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Crossroads Guardhouse |
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


## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [crossroads](../maps/crossroads.md) | Crossroads Guardhouse | 1 | – |


## Quests

- [Cheap cuts](../quests/benbyr.md): stages 10, 20, 30, 60
- [The ruthless Crackshot](../quests/Thieves03.md): stages 11
- [You shall pass](../quests/undertell_barricades.md): stages 60, 70, 100, 110, 120

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Benbyr. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/benbyr.json" data-npc="Benbyr" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (46 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-benbyr"></span>**`benbyr`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 10 of [The ruthless Crackshot](../quests/Thieves03.md#stage-10); NOT reached stage 11 of [The ruthless Crackshot](../quests/Thieves03.md#stage-11))* → [benbyr_guild03_1](#d-benbyr_guild03_1)
    - branch 2 *(if reached stage 40 of [You shall pass](../quests/undertell_barricades.md#stage-40); carry 1× [Trader's Guild bronze coin](../items/trader_guild-coins.md); NOT reached stage 70 of [You shall pass](../quests/undertell_barricades.md#stage-70))* → [benbyr_shannal_10](#d-benbyr_shannal_10)
    - branch 3 *(if latest stage of [You shall pass](../quests/undertell_barricades.md#stage-70) is 70)* → [benbyr_step_70](#d-benbyr_step_70)
    - branch 4 *(if reached stage 90 of [You shall pass](../quests/undertell_barricades.md#stage-90); NOT reached stage 120 of [You shall pass](../quests/undertell_barricades.md#stage-120))* → [benbyr_restitution_10](#d-benbyr_restitution_10)
    - branch 5 *(if reached stage 60 of [Cheap cuts](../quests/benbyr.md#stage-60))* → [benbyr_declined](#d-benbyr_declined)
    - branch 6 *(if reached stage 30 of [Cheap cuts](../quests/benbyr.md#stage-30))* → [benbyr_complete_1](#d-benbyr_complete_1)
    - branch 7 *(if reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20))* → [benbyr_mission_1](#d-benbyr_mission_1)
    - branch 8 → [benbyr_story_1](#d-benbyr_story_1)

    <span id="d-benbyr_guild03_1"></span>**`benbyr_guild03_1`** Benbyr: “(This man seems to be immersed in his thoughts)”

    - “Hi. Have you heard about the murder not far from here?” → [benbyr_guild03_2](#d-benbyr_guild03_2)

    <span id="d-benbyr_shannal_10"></span>**`benbyr_shannal_10`** Benbyr: “What do you want?”

    - “To show you this traders' coin.” → [benbyr_shannal_20](#d-benbyr_shannal_20)

    <span id="d-benbyr_step_70"></span>**`benbyr_step_70`** Benbyr: “Have you t-t-talked to the ghost y-y-yet? P-p-please hurry.”

    - “I will go now.” → *conversation ends*

    <span id="d-benbyr_restitution_10"></span>**`benbyr_restitution_10`** Benbyr: “W-w-w-well?”

    - “You have to make restitution.” → [benbyr_restitution_20](#d-benbyr_restitution_20)

    <span id="d-benbyr_declined"></span>**`benbyr_declined`** Benbyr: “I have nothing more to say to you. Leave me.”


    <span id="d-benbyr_complete_1"></span>**`benbyr_complete_1`** Benbyr: “Hello again. We sure showed that bastard Tinlyn. That should teach him not to mess with me again.”


    <span id="d-benbyr_mission_1"></span>**`benbyr_mission_1`** Benbyr: “Ah, my walking accident returns. He he.”

    - “Can you tell me your story again?” → [benbyr_story_4](#d-benbyr_story_4)
    - “I am still looking for those sheep.” → [benbyr_accept_3](#d-benbyr_accept_3)
    - “I have slain all eight of Tinlyn's sheep for you.” *(if hand over 8× [Meat from Tinlyn's sheep](../items/tinlyn_sheep_meat.md))* → [benbyr_mission_2](#d-benbyr_mission_2)

    <span id="d-benbyr_story_1"></span>**`benbyr_story_1`** Benbyr: “Psst, hey. Over here.”

    - Next → [benbyr_story_2](#d-benbyr_story_2)

    <span id="d-benbyr_guild03_2"></span>**`benbyr_guild03_2`** Benbyr: “What? A murder? I don't know what you're talking about, sorry.” — **effects:** sets stage 11 of [The ruthless Crackshot](../quests/Thieves03.md#stage-11)

    - “Civilians! You never see anything. Bye.” → *conversation ends*
    - “OK, thank you anyway!” → *conversation ends*

    <span id="d-benbyr_shannal_20"></span>**`benbyr_shannal_20`** Benbyr: “W-w-w-where did you get t-t-t-that?”

    - “A ghost near Galmore Mountain asked me to show it to you.” → [benbyr_shannal_30](#d-benbyr_shannal_30)

    <span id="d-benbyr_restitution_20"></span>**`benbyr_restitution_20`** Benbyr: “W-w-whatever y-y-you say.”

    - “You need to pay Shannal's descendant.” → [benbyr_restitution_30](#d-benbyr_restitution_30)

    <span id="d-benbyr_story_4"></span>**`benbyr_story_4`** Benbyr: “A while ago, I did some business with a certain man called Tinlyn, over here at this Crossroads guardhouse.”

    - Next → [benbyr_story_5](#d-benbyr_story_5)

    <span id="d-benbyr_accept_3"></span>**`benbyr_accept_3`** Benbyr: “Return to me with proof that you have slain all eight of them.”


    <span id="d-benbyr_mission_2"></span>**`benbyr_mission_2`** Benbyr: “Ha ha! That fool Tinlyn must be in tears. The Shadow surely walks with you my friend.” — **effects:** sets stage 30 of [Cheap cuts](../quests/benbyr.md#stage-30)

    - Next → [benbyr_complete_2](#d-benbyr_complete_2)

    <span id="d-benbyr_story_2"></span>**`benbyr_story_2`** Benbyr: “You look like an aspiring adventurer. Are you willing to do some ... [Benbyr pauses] ... adventuring? He he.”

    - “What are we talking about here?” → [benbyr_story_3_1](#d-benbyr_story_3_1)
    - “Depends on what I get in return.” → [benbyr_story_3_2](#d-benbyr_story_3_2)
    - “I try to help people wherever they might need help.” → [benbyr_story_3_3](#d-benbyr_story_3_3)

    <span id="d-benbyr_shannal_30"></span>**`benbyr_shannal_30`** Benbyr: “G-g-g-g-almore! I am dead.”

    - “Why is that?” → [benbyr_shannal_40](#d-benbyr_shannal_40)

    <span id="d-benbyr_restitution_30"></span>**`benbyr_restitution_30`** Benbyr: “I have to pay this person? How can you be serious? Look at me, I just recently got of that Feygard prison. I don't have any gold.”

    - “Well, that's not my problem.” → [benbyr_restitution_40](#d-benbyr_restitution_40)

    <span id="d-benbyr_story_5"></span>**`benbyr_story_5`** Benbyr: “As to the nature of our business, I can't really tell you. Let's just say that our business was of the kind that was mutually beneficial and the guards did not know about it.”

    - Next → [benbyr_story_6](#d-benbyr_story_6)

    <span id="d-benbyr_complete_2"></span>**`benbyr_complete_2`** Benbyr: “This is a glorious day indeed! Tinlyn should have known not to mess with me!”

    - Next → [benbyr_complete_3](#d-benbyr_complete_3)

    <span id="d-benbyr_story_3_1"></span>**`benbyr_story_3_1`** Benbyr: “Straight to the point eh? I like that.”

    - Next → [benbyr_story_4](#d-benbyr_story_4)

    <span id="d-benbyr_story_3_2"></span>**`benbyr_story_3_2`** Benbyr: “Ah, the adventurer seeks compensation. Tell me, is the thrill of an adventure not reward enough?”

    - “Yes, you are right.” → [benbyr_story_4](#d-benbyr_story_4)
    - “No.” → [benbyr_story_3_4](#d-benbyr_story_3_4)

    <span id="d-benbyr_story_3_3"></span>**`benbyr_story_3_3`** Benbyr: “The noble adventurer. He he, I like that. Yes, you will do fine.”

    - Next → [benbyr_story_4](#d-benbyr_story_4)

    <span id="d-benbyr_shannal_40"></span>**`benbyr_shannal_40`** Benbyr: “Oh well, we're not proud of it. My ancestor was one of those who would force or capture people to work in the mines of Undertell. He would be paid in these coins to get these people.” — **effects:** sets stage 60 of [You shall pass](../quests/undertell_barricades.md#stage-60)

    - “What is that coin? What does it mean?” → [benbyr_shannal_50](#d-benbyr_shannal_50)

    <span id="d-benbyr_restitution_40"></span>**`benbyr_restitution_40`** Benbyr: “All I have is fifty gold, I swear of it.” — **effects:** sets stage 100 of [You shall pass](../quests/undertell_barricades.md#stage-100)

    - “Are you kidding me? Let me call the ghost - she must be nearby...” → [benbyr_restitution_50](#d-benbyr_restitution_50)

    <span id="d-benbyr_story_6"></span>**`benbyr_story_6`** Benbyr: “We were ready to finish the big deal, me and Tinlyn. That's when he decided to turn on me.”

    - Next → [benbyr_story_7](#d-benbyr_story_7)

    <span id="d-benbyr_complete_3"></span>**`benbyr_complete_3`** Benbyr: “As for you my friend, seek out my friends in Brightport. I am sure they would extend their hospitality to you.”


    <span id="d-benbyr_story_3_4"></span>**`benbyr_story_3_4`** Benbyr: “Then I will surely disappoint you. Return to me once you are ready for my task.”


    <span id="d-benbyr_shannal_50"></span>**`benbyr_shannal_50`** Benbyr: “Can't really say. We're not happy about it. He was the black sheep of the family.”

    - “Like you're any better. The apple doesn't fall far from the tree.” → [benbyr_shannal_60](#d-benbyr_shannal_60)

    <span id="d-benbyr_restitution_50"></span>**`benbyr_restitution_50`** Benbyr: “N-n-no, I found some more in my other pocket. I have 500 gold.” — **effects:** sets stage 110 of [You shall pass](../quests/undertell_barricades.md#stage-110)

    - “A pittance.” → [benbyr_restitution_60](#d-benbyr_restitution_60)

    <span id="d-benbyr_story_7"></span>**`benbyr_story_7`** Benbyr: “He reported me to the guards, and made me take the whole blame for our business.”

    - Next → [benbyr_story_8](#d-benbyr_story_8)

    <span id="d-benbyr_shannal_60"></span>**`benbyr_shannal_60`** Benbyr: “A ghost asked you to show m-m-me? I'm dead. Since the ghost is here after all these years, it could be looking for revenge. My life for her suffering.”

    - “Old sins cast long shadows. However, perhaps I could talk to her, ask her to spare you?” → [benbyr_shannal_70](#d-benbyr_shannal_70)

    <span id="d-benbyr_restitution_60"></span>**`benbyr_restitution_60`** Benbyr: “H-h-how about a 1,000?”

    - “Old sins cast long shadows. Try harder.” → [benbyr_restitution_70](#d-benbyr_restitution_70)

    <span id="d-benbyr_story_8"></span>**`benbyr_story_8`** Benbyr: “I was sent to Feygard prison, while he himself was set free for reporting me.”

    - Next → [benbyr_story_8_1](#d-benbyr_story_8_1)

    <span id="d-benbyr_shannal_70"></span>**`benbyr_shannal_70`** Benbyr: “W-w-will you? T-t-t-thank you! P-p-p-please help me.” — **effects:** sets stage 70 of [You shall pass](../quests/undertell_barricades.md#stage-70)


    <span id="d-benbyr_restitution_70"></span>**`benbyr_restitution_70`** Benbyr: “You'll bankrupt me! Well, here's 5000. It's all my savings I secreted away before I was arrested and put in a Feygard prison.” — **effects:** sets stage 120 of [You shall pass](../quests/undertell_barricades.md#stage-120), gives 5000× [Gold coins](../items/gold.md)

    - “That should be enough. Stay out of trouble. You're safe for now.” → *conversation ends*

    <span id="d-benbyr_story_8_1"></span>**`benbyr_story_8_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20))* → [benbyr_story_10](#d-benbyr_story_10)
    - branch 2 → [benbyr_story_9](#d-benbyr_story_9)

    <span id="d-benbyr_story_10"></span>**`benbyr_story_10`** Benbyr: “I want to get revenge on that fool Tinlyn of course. Now, my plan is the following:”

    - Next → [benbyr_story_11](#d-benbyr_story_11)

    <span id="d-benbyr_story_9"></span>**`benbyr_story_9`** Benbyr: “Argh, that fool Tinlyn. I hope the Shadow never shows him any mercy.”

    - “Get to the point already.” → [benbyr_story_10](#d-benbyr_story_10)
    - “What do you need me to do?” → [benbyr_story_10](#d-benbyr_story_10)

    <span id="d-benbyr_story_11"></span>**`benbyr_story_11`** Benbyr: “I have heard that he is herding sheep these days. This is an excellent opportunity for ... shall we say ... an accident to happen to his sheep. He he.”

    - Next → [benbyr_story_12](#d-benbyr_story_12)

    <span id="d-benbyr_story_12"></span>**`benbyr_story_12`** Benbyr: “You, my friend, would be the perfect walking accident. I want you to find all of Tinlyn's sheep and make sure they are forever united with the Shadow.”

    - Next → [benbyr_story_12_1](#d-benbyr_story_12_1)

    <span id="d-benbyr_story_12_1"></span>**`benbyr_story_12_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20))* → [benbyr_accept_2](#d-benbyr_accept_2)
    - branch 2 → [benbyr_story_13](#d-benbyr_story_13)

    <span id="d-benbyr_accept_2"></span>**`benbyr_accept_2`** Benbyr: “I happen to know that there are eight of his sheep in total, and they should all be to the northwest of here.”

    - Next → [benbyr_accept_3](#d-benbyr_accept_3)

    <span id="d-benbyr_story_13"></span>**`benbyr_story_13`** Benbyr: “Do this, and I will have avenged that fool Tinlyn.” — **effects:** sets stage 10 of [Cheap cuts](../quests/benbyr.md#stage-10)

    - “Sounds like just my type of thing. I'll do it!” → [benbyr_accept_1](#d-benbyr_accept_1)
    - “This sounds a bit shady, but I'll do it anyway.” → [benbyr_accept_1](#d-benbyr_accept_1)
    - “No way, killing innocent sheep is beneath me. I will never do your task.” → [benbyr_decline_1](#d-benbyr_decline_1)

    <span id="d-benbyr_accept_1"></span>**`benbyr_accept_1`** Benbyr: “Splendid!” — **effects:** sets stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20)

    - Next → [benbyr_accept_2](#d-benbyr_accept_2)

    <span id="d-benbyr_decline_1"></span>**`benbyr_decline_1`** Benbyr: “Very well, but remember that I have my eyes on you ... adventurer.” — **effects:** sets stage 60 of [Cheap cuts](../quests/benbyr.md#stage-60)

    - Next → [benbyr_declined](#d-benbyr_declined)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 7 lines changed<br>· text: “I have heard that he is herding sheep these days. This is an excellen…” → “I have heard that he is herding sheep these days. This is an excellen…”<br>· text: “Very well, but remember that I have my eyes on you.. adventurer.” → “Very well, but remember that I have my eyes on you ... adventurer.” |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 2 lines added, 1 line changed |
| [v0.7.9](../versions/0.7.9.md) | Dialogue: 1 line changed<br>· text: “(This man seems to be inmersed in his thoughts)” → “(This man seems to be immersed in his thoughts)” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 15 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=benbyr.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=benbyr.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=benbyr.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=benbyr.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `benbyr` |
    | Spawn group | `benbyr` |
    | Loot table | – |
    | Conversation | `benbyr` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:74` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "benbyr",
     "name": "Benbyr",
     "iconID": "monsters_rltiles1:74",
     "monsterClass": "humanoid",
     "spawnGroup": "benbyr",
     "phraseID": "benbyr"
    }
    ```


<small>Data from v0.8.18</small>
