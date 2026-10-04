# ![](../assets/icons/monsters/monsters_rltiles2_37.png){ .sprite } Colonel Lutarc

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

- [waytogalmore0](../maps/waytogalmore0.md)

## Quests

- [Colonel Lutarc](../quests/stn_colonel.md): stages 10, 20, 170, 171, 172, 190
- [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md): stages 50, 110

??? quote "Dialogue (34 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-stn_colonel_30"></span>**`stn_colonel_30`** *(silent check: the first matching branch below is taken)*

    - branch 1 → [stn_colonel_30b](#d-stn_colonel_30b)

    <span id="d-stn_colonel_30b"></span>**`stn_colonel_30b`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 190 of [Colonel Lutarc](../quests/stn_colonel.md#stage-190))* → [stn_colonel_300](#d-stn_colonel_300)
    - branch 2 *(if reached stage 160 of [Colonel Lutarc](../quests/stn_colonel.md#stage-160))* → [stn_colonel_200](#d-stn_colonel_200)
    - branch 3 *(if reached stage 10 of [Colonel Lutarc](../quests/stn_colonel.md#stage-10); NOT reached stage 20 of [Colonel Lutarc](../quests/stn_colonel.md#stage-20))* → [stn_colonel_40](#d-stn_colonel_40)
    - branch 4 *(if NOT reached stage 110 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-110))* → [stn_colonel_32](#d-stn_colonel_32)
    - branch 5 → [stn_colonel_38](#d-stn_colonel_38)

    <span id="d-stn_colonel_300"></span>**`stn_colonel_300`** [Colonel Lutarc](../monsters/stn_colonel.md): “Greetings, $playername.”


    <span id="d-stn_colonel_200"></span>**`stn_colonel_200`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 113 of [Colonel Lutarc](../quests/stn_colonel.md#stage-113); reached stage 123 of [Colonel Lutarc](../quests/stn_colonel.md#stage-123); reached stage 133 of [Colonel Lutarc](../quests/stn_colonel.md#stage-133); reached stage 143 of [Colonel Lutarc](../quests/stn_colonel.md#stage-143); reached stage 153 of [Colonel Lutarc](../quests/stn_colonel.md#stage-153))* → [stn_colonel_210](#d-stn_colonel_210)
    - branch 2 *(if reached stage 112 of [Colonel Lutarc](../quests/stn_colonel.md#stage-112); reached stage 122 of [Colonel Lutarc](../quests/stn_colonel.md#stage-122); reached stage 132 of [Colonel Lutarc](../quests/stn_colonel.md#stage-132); reached stage 142 of [Colonel Lutarc](../quests/stn_colonel.md#stage-142); reached stage 152 of [Colonel Lutarc](../quests/stn_colonel.md#stage-152))* → [stn_colonel_220](#d-stn_colonel_220)
    - branch 3 → [stn_colonel_230](#d-stn_colonel_230)

    <span id="d-stn_colonel_40"></span>**`stn_colonel_40`** [Colonel Lutarc](../monsters/stn_colonel.md): “Oh, I know many things. A good leader has to keep his eyes and ears open.”

    - “You command the undead soldiers down there?” → [stn_colonel_42](#d-stn_colonel_42)
    - “You didn't answer my question. Who are you?” → [stn_colonel_44](#d-stn_colonel_44)

    <span id="d-stn_colonel_32"></span>**`stn_colonel_32`** [Colonel Lutarc](../monsters/stn_colonel.md): “Would you like a cup of good southern blend?” — **effects:** sets stage 10 of [Colonel Lutarc](../quests/stn_colonel.md#stage-10)

    - “With pleasure.” → [stn_colonel_34](#d-stn_colonel_34)
    - “No, thank you.” → [stn_colonel_36](#d-stn_colonel_36)

    <span id="d-stn_colonel_38"></span>**`stn_colonel_38`** [Colonel Lutarc](../monsters/stn_colonel.md): “You have not finished all the fights. So what are you doing here?”


    <span id="d-stn_colonel_210"></span>**`stn_colonel_210`** [Colonel Lutarc](../monsters/stn_colonel.md): “You lost every fight. I really did not expect such a poor performance from you.” — **effects:** sets stage 170 of [Colonel Lutarc](../quests/stn_colonel.md#stage-170)

    - “They were far too strong, and they all fought in an unfair way.” → [stn_colonel_250](#d-stn_colonel_250)

    <span id="d-stn_colonel_220"></span>**`stn_colonel_220`** [Colonel Lutarc](../monsters/stn_colonel.md): “You won every fight! Very good! I have not enjoyed myself so much for a long time.” — **effects:** sets stage 171 of [Colonel Lutarc](../quests/stn_colonel.md#stage-171)

    - “Me too.” → [stn_colonel_250](#d-stn_colonel_250)

    <span id="d-stn_colonel_230"></span>**`stn_colonel_230`** [Colonel Lutarc](../monsters/stn_colonel.md): “I did not expect you to win against all of my fighters, but it's good to know that for sure. Thanks for trying it out.” — **effects:** sets stage 172 of [Colonel Lutarc](../quests/stn_colonel.md#stage-172)

    - “If you have more for me, just call.” → [stn_colonel_250](#d-stn_colonel_250)

    <span id="d-stn_colonel_42"></span>**`stn_colonel_42`** Colonel Lutarc: “No, do not worry. I have nothing to do with the undead here in the castle. I just find them interesting.”

    - “Interesting indeed.” → [stn_colonel_44](#d-stn_colonel_44)
    - “Do you have any idea what the undead are doing here?” → [stn_colonel_43](#d-stn_colonel_43)

    <span id="d-stn_colonel_44"></span>**`stn_colonel_44`** Colonel Lutarc: “I am Colonel Lutarc, maybe you have already heard of me? No? Whatever.”

    - “May I ask what you are doing here?” → [stn_colonel_50](#d-stn_colonel_50)

    <span id="d-stn_colonel_34"></span>**`stn_colonel_34`** Colonel Lutarc: “Here you are.” — **effects:** sets stage 50 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-50)

    - “Who are you and how do you know my name?” → [stn_colonel_40](#d-stn_colonel_40)

    <span id="d-stn_colonel_36"></span>**`stn_colonel_36`** Colonel Lutarc: “*chuckles* Very clever. You should not trust strangers nowadays.”

    - “Who are you and how do you know my name?” → [stn_colonel_40](#d-stn_colonel_40)
    - “Right. That's why I'm leaving now.” → *conversation ends*

    <span id="d-stn_colonel_250"></span>**`stn_colonel_250`** Colonel Lutarc: “Take this medallion as a token of my thanks.” — **effects:** gives 1× [Lutarc's medallion](../items/lutarc_medallion.md), sets stage 190 of [Colonel Lutarc](../quests/stn_colonel.md#stage-190)

    - “Very kind of you. Oh, how nice! There is a tiny little lizard on it. It looks completely real, just like the lizard I…” → [stn_colonel_260](#d-stn_colonel_260)

    <span id="d-stn_colonel_43"></span>**`stn_colonel_43`** Colonel Lutarc: “No. I expected Lord Berbane's men to be here. But these undead are a nice change.”

    - Next → [stn_colonel_44](#d-stn_colonel_44)

    <span id="d-stn_colonel_50"></span>**`stn_colonel_50`** [Colonel Lutarc](../monsters/stn_colonel.md): “Isn't that obvious? I am enjoying my tea here. It is a splendid place. I really like it here.”

    - “You do have a nice view from here.” → [stn_colonel_52](#d-stn_colonel_52)
    - “You drink tea while fighting is going on down there?” → [stn_colonel_52](#d-stn_colonel_52)

    <span id="d-stn_colonel_260"></span>**`stn_colonel_260`** Colonel Lutarc: “Go now. I have to think.”


    <span id="d-stn_colonel_52"></span>**`stn_colonel_52`** [Colonel Lutarc](../monsters/stn_colonel.md): “Indeed. I come often to watch my warriors down there as they fight.”

    - Next → [stn_colonel_60](#d-stn_colonel_60)

    <span id="d-stn_colonel_60"></span>**`stn_colonel_60`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if killed 1× [Erwyn's knight](../monsters/erwyn_knight.md))* → [stn_colonel_62](#d-stn_colonel_62)
    - branch 2 *(if killed 1× [Erwyn's soldier](../monsters/erwyn_soldier.md))* → [stn_colonel_63](#d-stn_colonel_63)
    - branch 3 → [stn_colonel_70](#d-stn_colonel_70)

    <span id="d-stn_colonel_62"></span>**`stn_colonel_62`** Colonel Lutarc: “It was nice to see how easily you killed the undead knight.”

    - “Oh that - a small thing for me...” → [stn_colonel_64](#d-stn_colonel_64)

    <span id="d-stn_colonel_63"></span>**`stn_colonel_63`** Colonel Lutarc: “It was nice to see how easily you killed the undead soldier.”

    - “Oh that - a small thing for me...” → [stn_colonel_64](#d-stn_colonel_64)

    <span id="d-stn_colonel_70"></span>**`stn_colonel_70`** Colonel Lutarc: “Now I am curious about how well you could handle a number of my better warriors. Would you like to try?”

    - “Sure. After I have finished my tea of course.” *(if reached stage 50 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-50))* → [stn_colonel_72](#d-stn_colonel_72)
    - “Why not? A little challenge is always good.” → [stn_colonel_80](#d-stn_colonel_80)
    - “Maybe some other time. I have to leave now.” → *conversation ends*

    <span id="d-stn_colonel_64"></span>**`stn_colonel_64`** Colonel Lutarc: “I'm always impressed when I see a good fighter at work.”

    - “Thank you.” → [stn_colonel_70](#d-stn_colonel_70)
    - “Just tell me what you want from me.” → [stn_colonel_70](#d-stn_colonel_70)

    <span id="d-stn_colonel_72"></span>**`stn_colonel_72`** Colonel Lutarc: “Take your time.”

    - “[Drinking]” → [stn_colonel_74](#d-stn_colonel_74)
    - “OK, now to business.” → [stn_colonel_80](#d-stn_colonel_80)

    <span id="d-stn_colonel_80"></span>**`stn_colonel_80`** [Colonel Lutarc](../monsters/stn_colonel.md): “Good. Please go to the foot of this hill, right down there, by the gate.” — **effects:** sets stage 20 of [Colonel Lutarc](../quests/stn_colonel.md#stage-20), sets stage 110 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-110)

    - Next → [stn_colonel_82](#d-stn_colonel_82)

    <span id="d-stn_colonel_74"></span>**`stn_colonel_74`** Colonel Lutarc: “This is really an excellent tea, right?”

    - “[Drinking]” → [stn_colonel_75](#d-stn_colonel_75)
    - “OK, now to business.” → [stn_colonel_80](#d-stn_colonel_80)

    <span id="d-stn_colonel_82"></span>**`stn_colonel_82`** Colonel Lutarc: “There I will have five of my more interesting fighters compete against you.”

    - “Five?” → [stn_colonel_84](#d-stn_colonel_84)
    - “Well, it will be interesting.” → [stn_colonel_86](#d-stn_colonel_86)

    <span id="d-stn_colonel_75"></span>**`stn_colonel_75`** Colonel Lutarc: “I had not noticed that the cups are so big.”

    - “[Drinking]” → [stn_colonel_76](#d-stn_colonel_76)
    - “OK, now to business.” → [stn_colonel_80](#d-stn_colonel_80)

    <span id="d-stn_colonel_84"></span>**`stn_colonel_84`** Colonel Lutarc: “One after the other of course...”

    - “Oh, right.” → [stn_colonel_86](#d-stn_colonel_86)

    <span id="d-stn_colonel_86"></span>**`stn_colonel_86`** Colonel Lutarc: “Go now. Show me what you can do.”

    - “You will be surprised.” → *conversation ends*

    <span id="d-stn_colonel_76"></span>**`stn_colonel_76`** Colonel Lutarc: “You are really a connoisseur.”

    - “[Drinking]” → [stn_colonel_77](#d-stn_colonel_77)
    - “OK, now to business.” → [stn_colonel_80](#d-stn_colonel_80)

    <span id="d-stn_colonel_77"></span>**`stn_colonel_77`** Colonel Lutarc: “We have all the time in the world. Do not hurry.”

    - “[Drinking]” → [stn_colonel_79](#d-stn_colonel_79)
    - “OK, now to business.” → [stn_colonel_80](#d-stn_colonel_80)

    <span id="d-stn_colonel_79"></span>**`stn_colonel_79`** [Dummy NPC](../monsters/none.md): “The Colonel looks at you silently now.”

    - “[Drinking]” → [stn_colonel_79](#d-stn_colonel_79)
    - “OK, now to business.” → [stn_colonel_80](#d-stn_colonel_80)



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_colonel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_colonel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_colonel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_colonel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `stn_colonel` · Data from v0.8.18</small>
