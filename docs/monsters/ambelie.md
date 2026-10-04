# ![](../assets/icons/monsters/monsters_men_6.png){ .sprite } Ambelie

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 0 |
| Max AP | 10 |
| Attack cost | 10 |
| Move cost | 10 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Found on

- [foaming_flask](../maps/foaming_flask.md)

## Quests

- [Immaculate kidnapping](../quests/Thieves02.md): stages 10, 20, 21, 24, 65
- [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md): stages 20

??? quote "Dialogue (31 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ambelie_selector"></span>**`ambelie_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 24 of [Immaculate kidnapping](../quests/Thieves02.md#stage-24))* → [ambelie_guild02_20](#d-ambelie_guild02_20)
    - Next *(if reached stage 60 of [Immaculate kidnapping](../quests/Thieves02.md#stage-60))* → [ambelie_guild02_10](#d-ambelie_guild02_10)
    - Next *(if reached stage 21 of [Immaculate kidnapping](../quests/Thieves02.md#stage-21))* → [ambelie_guild02_16b](#d-ambelie_guild02_16b)
    - Next *(if reached stage 15 of [Immaculate kidnapping](../quests/Thieves02.md#stage-15))* → [ambelie_guild02_3](#d-ambelie_guild02_3)
    - Next → [ambelie_1](#d-ambelie_1)

    <span id="d-ambelie_guild02_20"></span>**`ambelie_guild02_20`** Ambelie: “You already took my necklace. Leave me alone.”


    <span id="d-ambelie_guild02_10"></span>**`ambelie_guild02_10`** Ambelie: “Bread? That's not a worthy food for a noblewoman like me! Oh my, where am I?”

    - “If you prefer going without food in this ugly cell for a long while then I don't care.” → [ambelie_guild02_11](#d-ambelie_guild02_11)
    - “Do you prefer to eat the floor, bad mannered woman?” → [ambelie_guild02_11](#d-ambelie_guild02_11)

    <span id="d-ambelie_guild02_16b"></span>**`ambelie_guild02_16b`** Ambelie: “You! Don't go any further. Leave me!”

    - “I'm not going to hurt you.” → [ambelie_guild02_16a](#d-ambelie_guild02_16a)

    <span id="d-ambelie_guild02_3"></span>**`ambelie_guild02_3`** [Ambelie](../monsters/ambelie.md): “You again?!”

    - “[Lie] Sorry, but I have to take you back home!” → [ambelie_guild02_4a](#d-ambelie_guild02_4a)
    - “(Knock her out) Time to sleep!” → [ambelie_guild02_4b](#d-ambelie_guild02_4b)

    <span id="d-ambelie_1"></span>**`ambelie_1`** Ambelie: “Oh my, a commoner. Get away from me. I might catch something.”

    - “Who are you?” → [ambelie_2](#d-ambelie_2)
    - “What is a noble woman such as yourself doing in a place like this?” → [ambelie_5](#d-ambelie_5)
    - “I would be glad to get away from a snob like you.” → *conversation ends*

    <span id="d-ambelie_guild02_11"></span>**`ambelie_guild02_11`** Ambelie: “S..sorry, please ... Yes I'm hungry ... Will you give me that? *sniffs*”

    - “[Give the Bread]” *(if hand over 5× [Bread](../items/bread.md))* → [ambelie_guild02_12](#d-ambelie_guild02_12)

    <span id="d-ambelie_guild02_16a"></span>**`ambelie_guild02_16a`** Ambelie: “Then get out of my sight now!” — **effects:** sets stage 21 of [Immaculate kidnapping](../quests/Thieves02.md#stage-21)

    - “I can't.Things are not that easy! Other people will get you instead of me.” → [ambelie_guild02_17a](#d-ambelie_guild02_17a)
    - “They will probably kill me if I go back without you.” → [ambelie_guild02_17b](#d-ambelie_guild02_17b)

    <span id="d-ambelie_guild02_4a"></span>**`ambelie_guild02_4a`** Ambelie: “No! I won't go anywhere with you, commoner! Guards, guards!”

    - Next → [ff_captain_guild02_4](#d-ff_captain_guild02_4)

    <span id="d-ambelie_guild02_4b"></span>**`ambelie_guild02_4b`** Ambelie: “(You tap her on the back of the head with the handle of your weapon, and she falls unconscious)” — **effects:** sets stage 20 of [Immaculate kidnapping](../quests/Thieves02.md#stage-20), removes monsters from foaming_flask, spawns monsters on road1, applies condition carrying_ambelie, sets stage 20 of [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md#stage-20)

    - “Fine ...” → *NPC leaves*

    <span id="d-ambelie_2"></span>**`ambelie_2`** Ambelie: “I am Ambelie of the house of Laumwill in Feygard. I am sure you must have heard of me and my house.”

    - “Oh yes ... um ... House of Laumwill in Feygard. Of course.” → [ambelie_3](#d-ambelie_3)
    - “I have never heard of you or your house.” → [ambelie_4](#d-ambelie_4)
    - “Where is Feygard?” → [ambelie_3](#d-ambelie_3)

    <span id="d-ambelie_5"></span>**`ambelie_5`** Ambelie: “I, Ambelie, of the house of Laumwill in Feygard, am on an excursion to the southern Nor City.”

    - Next → [ambelie_6](#d-ambelie_6)

    <span id="d-ambelie_guild02_12"></span>**`ambelie_guild02_12`** Ambelie: “Th..thanks. Now, please tell me, where am I?” — **effects:** sets stage 65 of [Immaculate kidnapping](../quests/Thieves02.md#stage-65)

    - “Sorry, but I cannot reveal that to you right now. Bye.” → *conversation ends*
    - “That doesn't matter! If you behave well maybe you will be out of here sooner rather than later.” → [ambelie_guild02_13](#d-ambelie_guild02_13)

    <span id="d-ambelie_guild02_17a"></span>**`ambelie_guild02_17a`** Ambelie: “I am safe here!”

    - “You aren't, and my presence here is the proof!” → [ambelie_guild02_18](#d-ambelie_guild02_18)

    <span id="d-ambelie_guild02_17b"></span>**`ambelie_guild02_17b`** Ambelie: “I couldn't care less about you! Just ask the guards.”

    - “Those untrained men aren't able to defend themselves. Don't make me laugh.” → [ambelie_guild02_18](#d-ambelie_guild02_18)
    - “Other people will get you, and they won't be as kind as me.” → [ambelie_guild02_17a](#d-ambelie_guild02_17a)

    <span id="d-ff_captain_guild02_4"></span>**`ff_captain_guild02_4`** [Feygard patrol captain](../monsters/feygard_patrol_captain.md): “Haha! Sorry lady, but your father wants you back home. I also believe this dirty tavern is no place for a woman like you, haha!”

    - “Yes, you have to come with me.” → [ambelie_guild02_5](#d-ambelie_guild02_5)

    <span id="d-ambelie_3"></span>**`ambelie_3`** Ambelie: “Feygard, the great city of peace. Surely you must know of it. Northwest in our great land.”

    - “What is a noble woman such as yourself doing in a place like this?” → [ambelie_5](#d-ambelie_5)
    - “No, I have never heard of it.” → [ambelie_4](#d-ambelie_4)

    <span id="d-ambelie_4"></span>**`ambelie_4`** Ambelie: “Pfft. That just proves everything I have heard of you savages here in the southern land. So uneducated.”


    <span id="d-ambelie_6"></span>**`ambelie_6`** [Ambelie](../monsters/ambelie.md): “An excursion to see if Nor City really is all that I have heard about it. If it really can compare itself to the glamour of the great city of Feygard.”

    - “Nor City, where is that?” → [ambelie_7](#d-ambelie_7)
    - “If you like it so much in Feygard, why would you even leave?” → [ambelie_9](#d-ambelie_9)
    - “Ehh ... I'm here to ... escort you safely to Nor City.” *(if reached stage 4 of [Immaculate kidnapping](../quests/Thieves02.md#stage-4); NOT reached stage 10 of [Immaculate kidnapping](../quests/Thieves02.md#stage-10))* → [ambelie_guild02_1](#d-ambelie_guild02_1)

    <span id="d-ambelie_guild02_13"></span>**`ambelie_guild02_13`** Ambelie: “... Fine *sniffs*.”


    <span id="d-ambelie_guild02_18"></span>**`ambelie_guild02_18`** Ambelie: “Stop. Then tell me what I can do!”

    - “Give me something of value, and you won't see me again.” → [ambelie_guild02_19](#d-ambelie_guild02_19)
    - “[Lie]I have enough gold, so if you give me something valuable .... The ransom we were going to ask will be covered.” → [ambelie_guild02_19](#d-ambelie_guild02_19)

    <span id="d-ambelie_guild02_5"></span>**`ambelie_guild02_5`** [Ambelie](../monsters/ambelie.md): “NO! I've said no! Don't bother me. Get away from me!”

    - “Sorry about this (Knock her out).” → [ambelie_guild02_4b](#d-ambelie_guild02_4b)
    - “[Whispering] You fool! Be quiet. Listen to me if you want to save your life.” → [ambelie_guild02_4c](#d-ambelie_guild02_4c)

    <span id="d-ambelie_7"></span>**`ambelie_7`** Ambelie: “Don't you know of Nor City? I will take note that the savages here haven't even heard of the city.”

    - Next → [ambelie_8](#d-ambelie_8)

    <span id="d-ambelie_9"></span>**`ambelie_9`** Ambelie: “All the noblewomen in Feygard keep talking about the mysterious Shadow in Nor City. I just have to see it myself.”

    - “Nor City, where is that?” → [ambelie_7](#d-ambelie_7)
    - “Good luck on your excursion.” → [ambelie_10](#d-ambelie_10)

    <span id="d-ambelie_guild02_1"></span>**`ambelie_guild02_1`** Ambelie: “Why? I don't know you, commoner. Why would I be willing to trust a savage looking kid?”

    - “But I'm not a commoner! I'm a ... Feygard spy. These clothes are my disguise!” → [ambelie_guild02_2](#d-ambelie_guild02_2)
    - “I'm stronger than those smug guards.” → [ambelie_guild02_2](#d-ambelie_guild02_2)

    <span id="d-ambelie_guild02_19"></span>**`ambelie_guild02_19`** Ambelie: “Take this and leave me, please.” — **effects:** gives 1× [Sapphire Necklace](../items/g02_ambelie.md), sets stage 24 of [Immaculate kidnapping](../quests/Thieves02.md#stage-24), spawns monsters on road1, sets stage 20 of [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md#stage-20)

    - “It has been a pleasure, my lady.” → *conversation ends*
    - “Sure, thank you.” → *conversation ends*

    <span id="d-ambelie_guild02_4c"></span>**`ambelie_guild02_4c`** Ambelie: “Wha... what are you referring to?”

    - “Sorry. Time to sleep! (Knock her out)” → [ambelie_guild02_4b](#d-ambelie_guild02_4b)
    - “I'm here to detain you, and then ask for a ransom.” → [ambelie_guild02_15](#d-ambelie_guild02_15)

    <span id="d-ambelie_8"></span>**`ambelie_8`** Ambelie: “I am beginning to be even more certain that Nor City will never, even in my wildest dreams, be comparable to the great city of Feygard.”

    - “Good luck on your excursion.” → [ambelie_10](#d-ambelie_10)

    <span id="d-ambelie_10"></span>**`ambelie_10`** Ambelie: “Thank you. Now please leave before someone sees me talking to a commoner like you.”

    - “Commoner? Are you trying to insult me? Goodbye.” → *conversation ends*
    - “Whatever, you probably wouldn't even survive a forest wasp.” → *conversation ends*

    <span id="d-ambelie_guild02_2"></span>**`ambelie_guild02_2`** Ambelie: “Anyway, I prefer to stay in this place for now. Get away from me!” — **effects:** sets stage 10 of [Immaculate kidnapping](../quests/Thieves02.md#stage-10)

    - “Hmpf .... Goodbye” → *conversation ends*

    <span id="d-ambelie_guild02_15"></span>**`ambelie_guild02_15`** Ambelie: “No way! Guards!”

    - “... Yes, no way. (Knock her out)” → [ambelie_guild02_4b](#d-ambelie_guild02_4b)
    - “I'm not going to hurt you, I don't want to do this.” → [ambelie_guild02_16a](#d-ambelie_guild02_16a)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed |
| [v0.7.8](../versions/0.7.8.md) | phraseID: ambelie_1 → ambelie_selector<br>Dialogue: 21 lines added, 1 line changed |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 1 line changed<br>· text: “(You tap her on the back of the head with the handle of your weapon, …” → “(You tap her on the back of the head with the handle of your weapon, …” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ambelie.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ambelie.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ambelie.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ambelie.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `ambelie` · Data from v0.8.18</small>
