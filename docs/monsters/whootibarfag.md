# ![](../assets/icons/monsters/monsters_rltiles3_16.png){ .sprite } Whootibarfag

| Stat | Value |
|---|---|
| Class | ? |
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

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Blue rat necklace](../items/ratdom_compass_bwm.md) | 100% | 1 |
| [Ratcave Torch](../items/ratdom_torch.md) | 100% | 1 to 5 |
| [Hand carved snowball](../items/handcarved_snowball.md) | 100% | 100 to 150 |

## Found on

- [blackwater_mountain55](../maps/blackwater_mountain55.md)

## Quests

- [Yellow is it](../quests/ratdom_quest.md): stages 200, 210
- [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md): stages 191

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Whootibarfag. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/whootibarfag.json" data-npc="Whootibarfag" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (48 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-whootibarfag"></span>**`whootibarfag`** Whootibarfag: “Greetings, young being.” — **effects:** sets stage 200 of [Yellow is it](../quests/ratdom_quest.md#stage-200)

    - “Hello to you, old man.” → [whootibarfag_20](#d-whootibarfag_20)
    - “Do you have something to trade?” → [whootibarfag_10](#d-whootibarfag_10)

    <span id="d-whootibarfag_20"></span>**`whootibarfag_20`** Whootibarfag: “I am Whootibarfag, wise of the Blackwater mountains.”

    - “Nice to meet you. I am $playername from Crossglen, if you should know the village.” → [whootibarfag_24](#d-whootibarfag_24)
    - “Do you have anything to trade?” → [whootibarfag_22](#d-whootibarfag_22)

    <span id="d-whootibarfag_10"></span>**`whootibarfag_10`** Whootibarfag: “Young people are always in a hurry. In my time, you introduced yourself first.”

    - Next → [whootibarfag_12](#d-whootibarfag_12)

    <span id="d-whootibarfag_24"></span>**`whootibarfag_24`** Whootibarfag: “Now, what brings you to this lonely area?”

    - “I'm helping a cheeky little rat find an artifact.” *(if reached stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10); NOT reached stage 900 of [Yellow is it](../quests/ratdom_quest.md#stage-900))* → [whootibarfag_50](#d-whootibarfag_50)
    - “Do you have anything to trade?” → [whootibarfag_30](#d-whootibarfag_30)
    - “I recovered and brought back Rat King Rah's skeleton.” *(if reached stage 390 of [Yellow is it](../quests/ratdom_quest.md#stage-390); NOT reached stage 210 of [Yellow is it](../quests/ratdom_quest.md#stage-210))* → [whootibarfag_200](#d-whootibarfag_200)

    <span id="d-whootibarfag_22"></span>**`whootibarfag_22`** Whootibarfag: “Sigh. Always in a hurry. Again - who are you?”

    - Next → [whootibarfag_20](#d-whootibarfag_20)

    <span id="d-whootibarfag_12"></span>**`whootibarfag_12`** Whootibarfag: “We'll try again from the beginning.”

    - Next → [whootibarfag](#d-whootibarfag)

    <span id="d-whootibarfag_50"></span>**`whootibarfag_50`** Whootibarfag: “Ah, a sacred quest for a mystical object. Good luck on your way.”

    - “Thanks. Then we'll go looking further.” → *conversation ends*
    - “Maybe you can help us?” → [whootibarfag_52](#d-whootibarfag_52)

    <span id="d-whootibarfag_30"></span>**`whootibarfag_30`** Whootibarfag: “I should have known. No one comes up here to ask for wisdom.”

    - “Not now. Let us trade first.” → [whootibarfag_32](#d-whootibarfag_32)
    - “All right, let's get this over with. Enlighten us.” *(if reached stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10))* → [whootibarfag_100](#d-whootibarfag_100)

    <span id="d-whootibarfag_200"></span>**`whootibarfag_200`** Whootibarfag: “Oh, yes. Of course I know.”

    - Next → [whootibarfag_202](#d-whootibarfag_202)

    <span id="d-whootibarfag_52"></span>**`whootibarfag_52`** Whootibarfag: “Who knows? Tell me about your artifact.”

    - “Maybe another time. Let's just trade.” → [whootibarfag_40](#d-whootibarfag_40)
    - “It's big, round and yellow. Clevered, what else do you know about this?” *(if reached stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10))* → [whootibarfag_54](#d-whootibarfag_54)

    <span id="d-whootibarfag_32"></span>**`whootibarfag_32`** Whootibarfag: “I have great knowledge, you know?”

    - “Maybe another time. Let's just trade.” → [whootibarfag_40](#d-whootibarfag_40)
    - “Then finally say what you want to say. And after that show me your goods.” *(if reached stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10))* → [whootibarfag_100](#d-whootibarfag_100)

    <span id="d-whootibarfag_100"></span>**`whootibarfag_100`** Whootibarfag: “I know that I know nothing.”

    - Next → [whootibarfag_110](#d-whootibarfag_110)

    <span id="d-whootibarfag_202"></span>**`whootibarfag_202`** Whootibarfag: “Nothing remains hidden from me that is happening here in the mountain.”

    - “I really had to run around a lot.” *(if NOT Evasion level 4+)* → [whootibarfag_210](#d-whootibarfag_210)

    <span id="d-whootibarfag_40"></span>**`whootibarfag_40`** Whootibarfag: “Sigh. Well, I have interesting items to sell. However, no food, I need it for myself.”

    - “Then what do you have for sale?” → [whootibarfag_42](#d-whootibarfag_42)

    <span id="d-whootibarfag_54"></span>**`whootibarfag_54`** [Clevred](../monsters/ratdom_rat.md): “Oh, whoever possesses this artifact will be rich and never go hungry again.”

    - “Gold?” → [whootibarfag_56](#d-whootibarfag_56)

    <span id="d-whootibarfag_110"></span>**`whootibarfag_110`** Whootibarfag: “But at least I think, so I am. Then I left the cave.”

    - “From the shadows to the light.” → [whootibarfag_112](#d-whootibarfag_112)

    <span id="d-whootibarfag_210"></span>**`whootibarfag_210`** Whootibarfag: “Well, I see you've learned a lot by searching the rat kingdom. But you're still missing one thing ...”

    - “What do you mean?” → [whootibarfag_220](#d-whootibarfag_220)
    - “Do you mean wisdom?” → [whootibarfag_212](#d-whootibarfag_212)
    - “Yes, I lack patience. The patience to keep listening to your babble.” → *conversation ends*

    <span id="d-whootibarfag_42"></span>**`whootibarfag_42`** Whootibarfag: “Torches to light your way.”

    - “I already have one.” → [whootibarfag_44](#d-whootibarfag_44)

    <span id="d-whootibarfag_56"></span>**`whootibarfag_56`** Whootibarfag: “Who needs gold?! It is much better.”

    - Next → [whootibarfag_68](#d-whootibarfag_68)

    <span id="d-whootibarfag_112"></span>**`whootibarfag_112`** Whootibarfag: “Yes, yes! How did you know?”

    - “I just guessed.” → [whootibarfag_120](#d-whootibarfag_120)

    <span id="d-whootibarfag_220"></span>**`whootibarfag_220`** Whootibarfag: “You've seen enough rats skilfully flee and escape.”

    - “Oh yes, I actually have.” → [whootibarfag_222](#d-whootibarfag_222)

    <span id="d-whootibarfag_212"></span>**`whootibarfag_212`** Whootibarfag: “Wisdom? No, hahaha!”

    - Next → [whootibarfag_214](#d-whootibarfag_214)

    <span id="d-whootibarfag_44"></span>**`whootibarfag_44`** Whootibarfag: “Hand carved snowballs.”

    - Next → [whootibarfag_46](#d-whootibarfag_46)

    <span id="d-whootibarfag_68"></span>**`whootibarfag_68`** [Dummy NPC](../monsters/none.md): “Clevred tells and tells.”

    - Next → [whootibarfag_70](#d-whootibarfag_70)

    <span id="d-whootibarfag_120"></span>**`whootibarfag_120`** Whootibarfag: “Now I need to know what is louder: the noise of a lonely falling tree, or the sound of one hand clapping.”

    - “Eh ...” → [whootibarfag_122](#d-whootibarfag_122)

    <span id="d-whootibarfag_222"></span>**`whootibarfag_222`** Whootibarfag: “You just haven't understood that you can make this ability your own.”

    - Next → [whootibarfag_224](#d-whootibarfag_224)

    <span id="d-whootibarfag_214"></span>**`whootibarfag_214`** Whootibarfag: “Leave wisdom to the wise. So to me.”

    - “So what am I missing?” → [whootibarfag_220](#d-whootibarfag_220)
    - “I will. What do you have for sale?” → [whootibarfag_42](#d-whootibarfag_42)
    - “As you wish. I leave the wise now. Bye.” → *conversation ends*

    <span id="d-whootibarfag_46"></span>**`whootibarfag_46`** Whootibarfag: “And finally, a medallion that will help you find your way here if your memory fails you.”

    - “Now that sounds interesting. Show me your items, please.” → *shop opens*
    - “However, I am as poor as a church rat.” *(if NOT have 3,333 gold; NOT reached stage 191 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-191))* → [whootibarfag_48](#d-whootibarfag_48)

    <span id="d-whootibarfag_70"></span>**`whootibarfag_70`** [Whootibarfag](../monsters/whootibarfag.md): “Hold on!”

    - Next → [whootibarfag_71](#d-whootibarfag_71)

    <span id="d-whootibarfag_122"></span>**`whootibarfag_122`** Whootibarfag: “I didn't really expect you to know.”

    - “Yes. I know.” *(if reached stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10))* → [whootibarfag_130](#d-whootibarfag_130)
    - “Enough. It's getting late.” *(if NOT reached stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10))* → [whootibarfag_190](#d-whootibarfag_190)

    <span id="d-whootibarfag_224"></span>**`whootibarfag_224`** Whootibarfag: “Come closer.”

    - Next → [whootibarfag_226](#d-whootibarfag_226)

    <span id="d-whootibarfag_48"></span>**`whootibarfag_48`** Whootibarfag: “Well, I have too good a heart. Here, take the amulet for 100 gold pieces.”

    - “Oh thank you! Here is the gold.” *(if NOT pay 100 gold)* → [whootibarfag_48a](#d-whootibarfag_48a)
    - “I will think about it.” → [whootibarfag_48b](#d-whootibarfag_48b)

    <span id="d-whootibarfag_71"></span>**`whootibarfag_71`** Whootibarfag: “I'm afraid I can't help you much there. I'm more familiar with the events out here on the mountain.”

    - Next → [whootibarfag_72](#d-whootibarfag_72)

    <span id="d-whootibarfag_130"></span>**`whootibarfag_130`** [Clevred](../monsters/ratdom_rat.md): “There are many paths leading to happiness.”

    - Next → [whootibarfag_132](#d-whootibarfag_132)

    <span id="d-whootibarfag_190"></span>**`whootibarfag_190`** [Whootibarfag](../monsters/whootibarfag.md): “Seize the day.”

    - “Enough! What. do. you. have. for. sale?” → [whootibarfag_40](#d-whootibarfag_40)
    - “I give up. Come, Clevred, let us leave.” *(if reached stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10))* → *conversation ends*

    <span id="d-whootibarfag_226"></span>**`whootibarfag_226`** Whootibarfag: “Closer ...”

    - “[You hold your breath - from tension, and because of his bad breath.]” → [whootibarfag_230](#d-whootibarfag_230)

    <span id="d-whootibarfag_48a"></span>**`whootibarfag_48a`** *(silent check: the first matching branch below is taken)* — **effects:** gives 1× [Blue rat necklace](../items/ratdom_compass_bwm.md), sets stage 191 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-191)

    - Next → [whootibarfag_48b](#d-whootibarfag_48b)

    <span id="d-whootibarfag_48b"></span>**`whootibarfag_48b`** Whootibarfag: “Well, now some wisdom ...”

    - “It is getting late. Bye.” → *conversation ends*
    - “All right, let's get this over with. Enlighten us.” *(if reached stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10))* → [whootibarfag_100](#d-whootibarfag_100)

    <span id="d-whootibarfag_72"></span>**`whootibarfag_72`** Whootibarfag: “But you might ask an old friend of mine. He has a small but valuable collection of important items and I'm sure he'll be happy to show you around.”

    - “We'll look for him.” *(if NOT reached stage 310 of [Yellow is it](../quests/ratdom_quest.md#stage-310))* → [whootibarfag_74](#d-whootibarfag_74)
    - “You mean Wart? We have already met him.” *(if reached stage 310 of [Yellow is it](../quests/ratdom_quest.md#stage-310))* → [whootibarfag_76](#d-whootibarfag_76)

    <span id="d-whootibarfag_132"></span>**`whootibarfag_132`** Whootibarfag: “One of them is to stop whining.”

    - Next → [whootibarfag_140](#d-whootibarfag_140)

    <span id="d-whootibarfag_230"></span>**`whootibarfag_230`** [Dummy NPC](../monsters/none.md): “Whootibarfag let you in on the secret of the rat escape. This increases your ability to flee and escape.” — **effects:** sets stage 210 of [Yellow is it](../quests/ratdom_quest.md#stage-210), +1 [Evasion](../skills/evasion.md)

    - “Hey! Yes of course! That's how it works!” → [whootibarfag_240](#d-whootibarfag_240)

    <span id="d-whootibarfag_74"></span>**`whootibarfag_74`** Whootibarfag: “You may find him in the caves below, even deeper in the mountain.”

    - “Thank you.” → [whootibarfag_76](#d-whootibarfag_76)
    - “Do you have anything to trade?” → [whootibarfag_30](#d-whootibarfag_30)

    <span id="d-whootibarfag_76"></span>**`whootibarfag_76`** Whootibarfag: “Good, so that's settled. Now I could share a little of my wisdom with you?”

    - “Not now. Let us trade first.” → [whootibarfag_32](#d-whootibarfag_32)
    - “All right, let's get this over with. Enlighten me.” → [whootibarfag_100](#d-whootibarfag_100)

    <span id="d-whootibarfag_140"></span>**`whootibarfag_140`** [Whootibarfag](../monsters/whootibarfag.md): “Hey - I'm the one with the wisdom here!”

    - Next → [whootibarfag_142](#d-whootibarfag_142)

    <span id="d-whootibarfag_240"></span>**`whootibarfag_240`** [Whootibarfag](../monsters/whootibarfag.md): “Use this knowledge well. Go now, I need some rest.”

    - “Thanks for all your help. Good bye.” → *conversation ends*

    <span id="d-whootibarfag_142"></span>**`whootibarfag_142`** [Clevred](../monsters/ratdom_rat.md): “Arrogance is the surest path to failure.”

    - Next → [whootibarfag_150](#d-whootibarfag_150)

    <span id="d-whootibarfag_150"></span>**`whootibarfag_150`** [Whootibarfag](../monsters/whootibarfag.md): “From failure we learn.”

    - Next → [whootibarfag_152](#d-whootibarfag_152)

    <span id="d-whootibarfag_152"></span>**`whootibarfag_152`** [Clevred](../monsters/ratdom_rat.md): “Learn as if you were to live forever.”

    - Next → [whootibarfag_190](#d-whootibarfag_190)



## Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added<br>Dialogue: 48 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=whootibarfag.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=whootibarfag.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=whootibarfag.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=whootibarfag.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `whootibarfag` · Data from v0.8.18</small>
