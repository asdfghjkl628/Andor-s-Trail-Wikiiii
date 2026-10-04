# ![](../assets/icons/monsters/monsters_rltiles1_63.png){ .sprite } Rogorn

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 145 |
| Max AP | 10 |
| Attack cost | 3 |
| Move cost | 5 |
| Damage | 5 to 9 |
| Attack chance | 90 |
| Block chance | 120 |
| Damage resistance | 5 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 0 to 50 |
| [Piece of painting](../items/rogorn_qitem.md) | 100% | 1 |
| [Hardened iron longsword](../items/longsword_hard_iron.md) | 100% | 1 |
| [Minor vial of health](../items/health_minor.md) | 100% | 1 to 2 |

## Found on

- [roadtocarntower2](../maps/roadtocarntower2.md)

## Quests

- [The path is clear to me](../quests/rogorn.md): stages 30, 35, 40, 45

??? quote "Dialogue (33 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-rogorn"></span>**`rogorn`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 60 of [The path is clear to me](../quests/rogorn.md#stage-60))* → [rogorn_completed_1](#d-rogorn_completed_1)
    - branch 2 *(if reached stage 40 of [The path is clear to me](../quests/rogorn.md#stage-40))* → [rogorn_attack_1](#d-rogorn_attack_1)
    - branch 3 *(if reached stage 45 of [The path is clear to me](../quests/rogorn.md#stage-45))* → [rogorn_story_r_9](#d-rogorn_story_r_9)
    - branch 4 *(if reached stage 35 of [The path is clear to me](../quests/rogorn.md#stage-35))* → [rogorn_toldstory_1](#d-rogorn_toldstory_1)
    - branch 5 → [rogorn_first_1](#d-rogorn_first_1)

    <span id="d-rogorn_completed_1"></span>**`rogorn_completed_1`** Rogorn: “Thank you for listening to our side of the story.”


    <span id="d-rogorn_attack_1"></span>**`rogorn_attack_1`** Rogorn: “I had hoped it would not come to this. For the Shadow!” — **effects:** sets stage 40 of [The path is clear to me](../quests/rogorn.md#stage-40)

    - “Let's fight!” → *fight starts*

    <span id="d-rogorn_story_r_9"></span>**`rogorn_story_r_9`** Rogorn: “Thank you for listening to our side of the story.”

    - “What now? I was sent here to find you by some guards in the Crossroads guardhouse.” → [rogorn_story_r_10](#d-rogorn_story_r_10)

    <span id="d-rogorn_toldstory_1"></span>**`rogorn_toldstory_1`** Rogorn: “You are back.”

    - “Can you tell me your side of the story again?” → [rogorn_story_r_1](#d-rogorn_story_r_1)
    - “I will not listen to your lies! You must be held accountable for your crimes against Feygard!” → [rogorn_story_r_8](#d-rogorn_story_r_8)
    - “I believe your story. How can I help you?” → [rogorn_story_r_9](#d-rogorn_story_r_9)

    <span id="d-rogorn_first_1"></span>**`rogorn_first_1`** Rogorn: “Look fellas, a kid! Out strolling here in the wilderness!”

    - Next → [rogorn_first_2](#d-rogorn_first_2)

    <span id="d-rogorn_story_r_10"></span>**`rogorn_story_r_10`** Rogorn: “You tell those guards that you searched for us, but did not find anyone.” — **effects:** sets stage 45 of [The path is clear to me](../quests/rogorn.md#stage-45)

    - “Will do. Goodbye.” → *conversation ends*

    <span id="d-rogorn_story_r_1"></span>**`rogorn_story_r_1`** Rogorn: “Me and my boys here travelled from our home in Nor City to these northern lands a few days ago.”

    - Next → [rogorn_story_r_2](#d-rogorn_story_r_2)

    <span id="d-rogorn_story_r_8"></span>**`rogorn_story_r_8`** Rogorn: “What are you, a spy for Feygard? I told you, the accusations against us are false.”

    - Next → [rogorn_attack_1](#d-rogorn_attack_1)

    <span id="d-rogorn_first_2"></span>**`rogorn_first_2`** Rogorn: “Should you really be out here kid? These areas are dangerous.”

    - “I can handle myself.” → [rogorn_first_3](#d-rogorn_first_3)
    - “Why? What is out here?” → [rogorn_first_4](#d-rogorn_first_4)
    - “You are right, I better leave.” → *conversation ends*

    <span id="d-rogorn_story_r_2"></span>**`rogorn_story_r_2`** Rogorn: “We had never been here ourselves. We had only heard stories about how tough the guards from Feygard were, and how they held their precious law above all.”

    - Next → [rogorn_story_r_3](#d-rogorn_story_r_3)

    <span id="d-rogorn_first_3"></span>**`rogorn_first_3`** Rogorn: “I bet you can.”

    - Next → [rogorn_first_6](#d-rogorn_first_6)

    <span id="d-rogorn_first_4"></span>**`rogorn_first_4`** Rogorn: “Well, west of here is not much. No towns for quite a while, only the harsh and dangerous wilderness.”

    - Next → [rogorn_first_5](#d-rogorn_first_5)

    <span id="d-rogorn_story_r_3"></span>**`rogorn_story_r_3`** Rogorn: “Anyway, we got wind of a certain business opportunity here up north. One where we would be on the receiving end of a very profitable deal.”

    - Next → [rogorn_story_r_4](#d-rogorn_story_r_4)

    <span id="d-rogorn_first_6"></span>**`rogorn_first_6`** Rogorn: “So, what brings you to these parts of the land?”

    - “I am looking for a group of men led by someone by the name of Rogorn. Are you him?” *(if reached stage 20 of [The path is clear to me](../quests/rogorn.md#stage-20))* → [rogorn_story_1](#d-rogorn_story_1)
    - “Just looking for any treasure that might reveal itself here.” → [rogorn_first_7](#d-rogorn_first_7)
    - “I am just exploring.” → [rogorn_first_7](#d-rogorn_first_7)

    <span id="d-rogorn_first_5"></span>**`rogorn_first_5`** Rogorn: “Of course, there is Carn Tower if you travel really far west, but you really do not want to head there.”

    - Next → [rogorn_first_6](#d-rogorn_first_6)

    <span id="d-rogorn_story_r_4"></span>**`rogorn_story_r_4`** Rogorn: “So we went here to conduct our business. Shortly thereafter, I guess the guards from Feygard must have been tipped off about us, since we noticed that we were being followed by the guards after a while.”

    - Next → [rogorn_story_r_5](#d-rogorn_story_r_5)

    <span id="d-rogorn_story_1"></span>**`rogorn_story_1`** Rogorn: “That depends, why do you want to know?” — **effects:** sets stage 30 of [The path is clear to me](../quests/rogorn.md#stage-30)

    - “You are wanted by the Feygard patrol for the crimes you have committed.” → [rogorn_story_2](#d-rogorn_story_2)
    - “I am seeking to deal justice wherever I can, and I heard that you are in need of being shown some justice.” → [rogorn_story_3](#d-rogorn_story_3)
    - “I am sent by some guards over at the Crossroads guardhouse to look for you.” → [rogorn_story_6](#d-rogorn_story_6)
    - “The guards from Feygard are looking for you, and I came to warn you.” → [rogorn_story_12](#d-rogorn_story_12)

    <span id="d-rogorn_first_7"></span>**`rogorn_first_7`** Rogorn: “Well, keep on looking then.”


    <span id="d-rogorn_story_r_5"></span>**`rogorn_story_r_5`** Rogorn: “Not willing to risk anything, considering the rumors we had heard about the guards from there, we did the only reasonable thing we could do - we abandoned the plan right away and left, before we could conduct the business we had planned.”

    - Next → [rogorn_story_r_6](#d-rogorn_story_r_6)

    <span id="d-rogorn_story_2"></span>**`rogorn_story_2`** Rogorn: “Hah! We? Crimes?”

    - Next → [rogorn_story_4](#d-rogorn_story_4)

    <span id="d-rogorn_story_3"></span>**`rogorn_story_3`** Rogorn: “Justice? What would you know of justice, kid?”

    - Next → [rogorn_story_4](#d-rogorn_story_4)

    <span id="d-rogorn_story_6"></span>**`rogorn_story_6`** Rogorn: “Talked to those guards from Feygard eh? Tell me, what is your opinion of Feygard?”

    - “They seem to have honorable ideals of law and order, and I respect that.” → [rogorn_story_10](#d-rogorn_story_10)
    - “Their ideals seem to be a bit oppressive of the people, which I do not like.” → [rogorn_story_9](#d-rogorn_story_9)
    - “I have no opinion, I try not to get involved in their business.” → [rogorn_story_7](#d-rogorn_story_7)
    - “I have no idea.” → [rogorn_story_8](#d-rogorn_story_8)

    <span id="d-rogorn_story_12"></span>**`rogorn_story_12`** Rogorn: “Good to hear that there still are some people willing to make a stand against Feygard. Let me tell you my side of the story.”

    - Next → [rogorn_story_r_1](#d-rogorn_story_r_1)

    <span id="d-rogorn_story_r_6"></span>**`rogorn_story_r_6`** Rogorn: “However, something must have upset the guards there anyway. Now we hear that we are accused of murder and theft in Feygard, without even being there ourselves.” — **effects:** sets stage 35 of [The path is clear to me](../quests/rogorn.md#stage-35)

    - “What was your business there?” → [rogorn_story_r_7](#d-rogorn_story_r_7)
    - “I will not listen to your lies! For Feygard!” → [rogorn_attack_1](#d-rogorn_attack_1)
    - “Your story does not add up.” → [rogorn_story_r_8](#d-rogorn_story_r_8)
    - “I believe your story. How can I help you?” → [rogorn_story_r_9](#d-rogorn_story_r_9)

    <span id="d-rogorn_story_4"></span>**`rogorn_story_4`** Rogorn: “If there is someone that deserves punishment, it surely isn't us. By the Shadow, it's those snobs from Feygard that should be taught a lesson.”

    - “I will not listen to your lies! For Feygard!” → [rogorn_attack_1](#d-rogorn_attack_1)
    - “Talk all you want, I happen to know that you have stolen from Feygard, which is not acceptable.” → [rogorn_story_5](#d-rogorn_story_5)
    - “What's your side of the story then?” → [rogorn_story_r_1](#d-rogorn_story_r_1)

    <span id="d-rogorn_story_10"></span>**`rogorn_story_10`** Rogorn: “Law and order? What use do we have of that if we are always persecuted by them and do not even have the freedom to live our lives the way we want?”

    - Next → [rogorn_story_11](#d-rogorn_story_11)

    <span id="d-rogorn_story_9"></span>**`rogorn_story_9`** Rogorn: “You have got that right. They are always trying to make life hard for us little people. Let me tell you my side of the story.”

    - Next → [rogorn_story_r_1](#d-rogorn_story_r_1)

    <span id="d-rogorn_story_7"></span>**`rogorn_story_7`** Rogorn: “Interesting. But now that you are part of their business by coming here to look for me on their behalf, how does that fit into your unwillingness to take sides?”

    - “I will not listen to your lies! For Feygard!” → [rogorn_attack_1](#d-rogorn_attack_1)
    - “I was told that you have stolen from Feygard, which is not acceptable.” → [rogorn_story_5](#d-rogorn_story_5)
    - “I want to hear your side of the story.” → [rogorn_story_r_1](#d-rogorn_story_r_1)
    - “I am just looking to see if there is some treasure to be gained from this.” → [rogorn_story_8](#d-rogorn_story_8)
    - “I have no idea.” → [rogorn_story_8](#d-rogorn_story_8)

    <span id="d-rogorn_story_8"></span>**`rogorn_story_8`** Rogorn: “You should make up your mind about what your priorities are. Tell your Feygard friends that we will not be oppressed by them. Shadow be with you, child.”


    <span id="d-rogorn_story_r_7"></span>**`rogorn_story_r_7`** Rogorn: “I can't really say. We do our business on behalf of Nor City, and our business is our own.”

    - “I will not listen to your lies! For Feygard!” → [rogorn_attack_1](#d-rogorn_attack_1)
    - “Your story does not add up.” → [rogorn_story_r_8](#d-rogorn_story_r_8)
    - “I believe your story. How can I help you?” → [rogorn_story_r_9](#d-rogorn_story_r_9)

    <span id="d-rogorn_story_5"></span>**`rogorn_story_5`** Rogorn: “I tell you, we did not steal anything from those snobs.”

    - “You are still wanted dead by the Feygard patrol. For Feygard!” → [rogorn_attack_1](#d-rogorn_attack_1)
    - “Why are they looking for you then?” → [rogorn_story_r_1](#d-rogorn_story_r_1)

    <span id="d-rogorn_story_11"></span>**`rogorn_story_11`** Rogorn: “They are always looking for us, trying to oppress us in some way. Always trying to make our lives a little bit harder.”

    - Next → [rogorn_story_4](#d-rogorn_story_4)



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rogorn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rogorn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rogorn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rogorn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `rogorn` · Data from v0.8.18</small>
