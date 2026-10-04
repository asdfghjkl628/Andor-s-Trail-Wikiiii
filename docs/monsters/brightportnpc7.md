# ![](../assets/icons/monsters/monsters_rltiles1_94.png){ .sprite } Bryma

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

## Found on

- [brightport_forest](../maps/brightport_forest.md)

## Quests

- [No rest for the wicked](../quests/Stanwickquest.md): stages 86, 92, 95
- [The balance of scales](../quests/brightport_lizard.md): stages 5, 10, 36, 50, 55, 100, 110
- [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md): stages 104, 105, 106, 107, 110, 111, 112, 221, 233, 257

??? quote "Dialogue (67 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightport_bryma_selector"></span>**`brightport_bryma_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 10 of [The balance of scales](../quests/brightport_lizard.md#stage-10); NOT reached stage 112 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-112))* → [brightport_bryma38](#d-brightport_bryma38)
    - Next *(if reached stage 112 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-112))* → [brightport_bryma50](#d-brightport_bryma50)
    - Next *(if reached stage 104 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-104))* → [brightport_bryma6_alt](#d-brightport_bryma6_alt)
    - Next → [brightport_bryma](#d-brightport_bryma)

    <span id="d-brightport_bryma38"></span>**`brightport_bryma38`** Bryma: “Have you had any success with the creatures?”

    - “As long as you don't bother them again, things should be good now.” *(if reached stage 90 of [The balance of scales](../quests/brightport_lizard.md#stage-90))* → [brightport_bryma46](#d-brightport_bryma46)
    - “Yes, they are all dead.” *(if reached stage 32 of [The balance of scales](../quests/brightport_lizard.md#stage-32))* → [brightport_bryma_lizardselector](#d-brightport_bryma_lizardselector)
    - “I've met with the leader of the lizardman tribe, they demand I return the 13 stolen bones.” *(if NOT reached stage 55 of [The balance of scales](../quests/brightport_lizard.md#stage-55); reached stage 40 of [The balance of scales](../quests/brightport_lizard.md#stage-40); NOT reached stage 90 of [The balance of scales](../quests/brightport_lizard.md#stage-90))* → [brightport_bryma42_alt_alt](#d-brightport_bryma42_alt_alt)
    - “Not yet.” *(if NOT reached stage 55 of [The balance of scales](../quests/brightport_lizard.md#stage-55))* → [brightport_bryma45](#d-brightport_bryma45)
    - “I've yet to return the bones.” *(if reached stage 55 of [The balance of scales](../quests/brightport_lizard.md#stage-55); NOT reached stage 60 of [The balance of scales](../quests/brightport_lizard.md#stage-60))* → [brightport_bryma45](#d-brightport_bryma45)
    - “I returned the bones but I've got one more task to do.” *(if reached stage 60 of [The balance of scales](../quests/brightport_lizard.md#stage-60); NOT reached stage 90 of [The balance of scales](../quests/brightport_lizard.md#stage-90))* → [brightport_bryma45](#d-brightport_bryma45)
    - “Not yet, I wish to ask you about other things.” → [brightport_bryma14](#d-brightport_bryma14)

    <span id="d-brightport_bryma50"></span>**`brightport_bryma50`** Bryma: “It is good to see you $playername. what brings you around?”

    - “I wish to talk about something.” → [brightport_bryma14](#d-brightport_bryma14)

    <span id="d-brightport_bryma6_alt"></span>**`brightport_bryma6_alt`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 95 of [No rest for the wicked](../quests/Stanwickquest.md#stage-95))* → [brightport_bryma6](#d-brightport_bryma6)
    - Next *(if reached stage 92 of [No rest for the wicked](../quests/Stanwickquest.md#stage-92))* → [brightport_bryma_alternative_greeting](#d-brightport_bryma_alternative_greeting)

    <span id="d-brightport_bryma"></span>**`brightport_bryma`** Bryma: “A visitor, how unusual. I assume you haven't simply stumbled upon my cabin by accident?” — **effects:** sets stage 86 of [No rest for the wicked](../quests/Stanwickquest.md#stage-86)

    - “Are you the person named Bryma?” → [brightport_bryma0](#d-brightport_bryma0)
    - “Yuck, what is that thing inside your kitchen?” → [brightport_bryma7](#d-brightport_bryma7)

    <span id="d-brightport_bryma46"></span>**`brightport_bryma46`** Bryma: “That is no problem. But how am I supposed to get bones now...”

    - “I negotiated with the lizardmen, they agree to trade with you the bones of the animals they hunt.” *(if reached stage 95 of [The balance of scales](../quests/brightport_lizard.md#stage-95))* → [brightport_bryma47](#d-brightport_bryma47)
    - “I've solved the main problem. That should be the least of your issues now.” *(if NOT reached stage 95 of [The balance of scales](../quests/brightport_lizard.md#stage-95))* → [brightport_bryma53](#d-brightport_bryma53)

    <span id="d-brightport_bryma_lizardselector"></span>**`brightport_bryma_lizardselector`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 35 of [The balance of scales](../quests/brightport_lizard.md#stage-35))* → [brightport_bryma_lizardexist](#d-brightport_bryma_lizardexist)
    - Next *(if reached stage 35 of [The balance of scales](../quests/brightport_lizard.md#stage-35))* → [brightport_bryma_lizarddead](#d-brightport_bryma_lizarddead)

    <span id="d-brightport_bryma42_alt_alt"></span>**`brightport_bryma42_alt_alt`** [Dummy NPC](../monsters/none.md): “She begins quietly murmuring to herself.”

    - Next → [brightport_bryma42_alt](#d-brightport_bryma42_alt)

    <span id="d-brightport_bryma45"></span>**`brightport_bryma45`** Bryma: “I see, good luck with that.”


    <span id="d-brightport_bryma14"></span>**`brightport_bryma14`** Bryma: “Sure, what do you want to know?”

    - “Can you tell me about Andor again?” *(if reached stage 105 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-105); reached stage 132 of [andor (hidden flag)](../quests/andor.md#stage-132))* → [brightport_bryma13](#d-brightport_bryma13)
    - “Why do you live here in the forest?” → [brightport_bryma15](#d-brightport_bryma15)
    - “I'm curious, how did that scroll reach you?” *(if NOT reached stage 132 of [andor (hidden flag)](../quests/andor.md#stage-132))* → [brightport_bryma8](#d-brightport_bryma8)
    - “What's with that statue at the entrance of the forest?” → [brightport_bryma37](#d-brightport_bryma37)
    - “You mentioned your bonemeal research, what can you tell me about the potion?” *(if reached stage 106 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-106); NOT reached stage 111 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-111))* → [brightport_bryma22](#d-brightport_bryma22)
    - “Can you tell me about your bonemeal theory again?” *(if reached stage 111 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-111))* → [brightport_bryma31](#d-brightport_bryma31)

    <span id="d-brightport_bryma6"></span>**`brightport_bryma6`** Bryma: “You're back again? The forest isn't as quiet as it used to be.”

    - “I saw a strange creature in the cave under your house. It didn't stick around though.” *(if reached stage 1 of [The balance of scales](../quests/brightport_lizard.md#stage-1); NOT reached stage 10 of [The balance of scales](../quests/brightport_lizard.md#stage-10))* → [brightport_bryma39](#d-brightport_bryma39)
    - “Can you tell me more about what you know of my brother Andor?” *(if reached stage 132 of [andor (hidden flag)](../quests/andor.md#stage-132); NOT reached stage 105 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-105))* → [brightport_bryma13](#d-brightport_bryma13)
    - “Can you tell me about Andor again?” *(if reached stage 132 of [andor (hidden flag)](../quests/andor.md#stage-132); reached stage 105 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-105))* → [brightport_bryma13](#d-brightport_bryma13)
    - “I'm curious, how did that scroll reach you?” *(if NOT reached stage 132 of [andor (hidden flag)](../quests/andor.md#stage-132))* → [brightport_bryma8](#d-brightport_bryma8)
    - “What's with that statue at the entrance of the forest?” → [brightport_bryma37](#d-brightport_bryma37)
    - “Why do you live here in the forest?” → [brightport_bryma15](#d-brightport_bryma15)
    - “You mentioned your bonemeal research, what can you tell me about the potion?” *(if reached stage 107 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-107); NOT reached stage 111 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-111); reached stage 106 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-106))* → [brightport_bryma22](#d-brightport_bryma22)
    - “Can you tell me about your bonemeal theory again?” *(if reached stage 111 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-111))* → [brightport_bryma31](#d-brightport_bryma31)

    <span id="d-brightport_bryma_alternative_greeting"></span>**`brightport_bryma_alternative_greeting`** Bryma: “Hello, I am most happy to have someone to talk with.”

    - “I saw a strange creature in the cave under your house. It didn't stick around though.” *(if reached stage 1 of [The balance of scales](../quests/brightport_lizard.md#stage-1); NOT reached stage 10 of [The balance of scales](../quests/brightport_lizard.md#stage-10))* → [brightport_bryma39](#d-brightport_bryma39)
    - “Can you tell me more about what you know of my brother Andor?” *(if reached stage 132 of [andor (hidden flag)](../quests/andor.md#stage-132); NOT reached stage 105 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-105))* → [brightport_bryma13](#d-brightport_bryma13)
    - “Can you tell me about Andor again?” *(if reached stage 132 of [andor (hidden flag)](../quests/andor.md#stage-132); reached stage 105 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-105))* → [brightport_bryma13](#d-brightport_bryma13)
    - “I'm curious, how did that scroll get to you?” *(if NOT reached stage 132 of [andor (hidden flag)](../quests/andor.md#stage-132))* → [brightport_bryma8](#d-brightport_bryma8)
    - “What's with that statue at the entrance of the forest?” → [brightport_bryma37](#d-brightport_bryma37)
    - “Why do you live here in the forest?” → [brightport_bryma15](#d-brightport_bryma15)
    - “You mentioned your bonemeal research, what can you tell me about the potion?” *(if reached stage 106 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-106); NOT reached stage 111 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-111); reached stage 107 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-107))* → [brightport_bryma22](#d-brightport_bryma22)
    - “Can you tell me about your bonemeal theory again?” *(if reached stage 111 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-111))* → [brightport_bryma31](#d-brightport_bryma31)

    <span id="d-brightport_bryma0"></span>**`brightport_bryma0`** Bryma: “It's an odd coincidence that the only two visitors I have had in years are asking the same question. You two could almost be twins.”

    - “So you are Bryma. I'm looking for a document from the Brightport archive that was stolen.” → [brightport_bryma2](#d-brightport_bryma2)
    - “Could that possibly have been my brother, Andor?” → [brightport_bryma1](#d-brightport_bryma1)

    <span id="d-brightport_bryma7"></span>**`brightport_bryma7`** Bryma: “That is one of the bread golems I invented, after years of research and study with the great minds of Nor City.”

    - Next → [brightport_bryma0](#d-brightport_bryma0)

    <span id="d-brightport_bryma47"></span>**`brightport_bryma47`** Bryma: “You've done a great job, $playername. I have little of value to offer, just these two special potions. I possess very few, so I can't give you more. Use them well.” — **effects:** sets stage 100 of [The balance of scales](../quests/brightport_lizard.md#stage-100), gives 2× [Essence concentrate potion](../items/brightport_bonemeal.md), sets stage 112 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-112)

    - Next *(if reached stage 115 of [Destined for great things](../quests/charwood1.md#stage-115))* → [brightport_bryma48](#d-brightport_bryma48)

    <span id="d-brightport_bryma53"></span>**`brightport_bryma53`** Bryma: “You're right. I can figure the rest out, $playername. I don't have much to offer, except one of my special potions. I have very few, so use it wisely.” — **effects:** gives 1× [Essence concentrate potion](../items/brightport_bonemeal.md), sets stage 110 of [The balance of scales](../quests/brightport_lizard.md#stage-110), sets stage 112 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-112)

    - Next *(if reached stage 35 of [Destined for great things](../quests/charwood1.md#stage-35))* → [brightport_bryma48](#d-brightport_bryma48)

    <span id="d-brightport_bryma_lizardexist"></span>**`brightport_bryma_lizardexist`** Bryma: “Sigh, I'm fine with such a violent method. But please finish the work to the end, there are still lizardmen left.”

    - “Fine.” → *conversation ends*

    <span id="d-brightport_bryma_lizarddead"></span>**`brightport_bryma_lizarddead`** Bryma: “Good work $playername. Now I have access to as much bonemeal as I need. Please have these potions, including a special one.” — **effects:** sets stage 112 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-112), gives 1× [Essence concentrate potion](../items/brightport_bonemeal.md), gives 6× [Bonemeal potion](../items/bonemeal_potion.md), sets stage 36 of [The balance of scales](../quests/brightport_lizard.md#stage-36)

    - Next *(if reached stage 115 of [Destined for great things](../quests/charwood1.md#stage-115))* → [brightport_bryma48](#d-brightport_bryma48)

    <span id="d-brightport_bryma42_alt"></span>**`brightport_bryma42_alt`** [Bryma](../monsters/brightportnpc7.md): “Does this imply they're sentient? No. That can't be...”

    - Next → [brightport_bryma42](#d-brightport_bryma42)

    <span id="d-brightport_bryma13"></span>**`brightport_bryma13`** Bryma: “About half a year ago, I was carefully measuring the ingredients for my baking experiments when I heard the door. I went to look, and a boy who looked a little older than you introduced himself as Andor.”

    - Next → [brightport_bryma10](#d-brightport_bryma10)

    <span id="d-brightport_bryma15"></span>**`brightport_bryma15`** Bryma: “I discovered this place in my youth while researching Brightport's fauna. After Lord Geomyr's coronation, many alchemists like myself were at risk of being arrested under the new laws. So I returned here to continue my research.”

    - “What kind of research?” → [brightport_bryma18](#d-brightport_bryma18)

    <span id="d-brightport_bryma8"></span>**`brightport_bryma8`** Bryma: “It was brought to me by a boy who looked a lot like you.”

    - Next → [brightport_bryma9](#d-brightport_bryma9)

    <span id="d-brightport_bryma37"></span>**`brightport_bryma37`** Bryma: “Those statues are intriguing. The light one sees in their vicinity is similar to the descriptions of the blinding light of the false goddess Elythara.”

    - Next → [brightport_bryma54](#d-brightport_bryma54)

    <span id="d-brightport_bryma22"></span>**`brightport_bryma22`** Bryma: “It will be a long and difficult subject, so please keep that in mind and don't interrupt me.”

    - Next → [brightport_bryma23](#d-brightport_bryma23)

    <span id="d-brightport_bryma31"></span>**`brightport_bryma31`** Bryma: “In my baking research, I discovered that the potion does not merely heal but it facilitates growth. What we perceive as healing is, in fact, simply the acceleration of the body's natural regeneration condensed into a shorter time by the…”

    - Next → [brightport_bryma32](#d-brightport_bryma32)

    <span id="d-brightport_bryma39"></span>**`brightport_bryma39`** Bryma: “Lizardmen, again. They've been bothering me for months now. My bread golems can handle a few, but if they all come at once, I'll be in trouble.”

    - “Maybe I could help with that, what's the story here?” → [brightport_bryma40](#d-brightport_bryma40)

    <span id="d-brightport_bryma2"></span>**`brightport_bryma2`** Bryma: “You mean the secret scroll that I have right here? [Bryma takes out a rolled, tattered looking parchment]”

    - “You can give it to me, or I can take it by force.” → [brightport_bryma4](#d-brightport_bryma4)
    - “I need to take it back, could you kindly give it to me?” → [brightport_bryma5](#d-brightport_bryma5)

    <span id="d-brightport_bryma1"></span>**`brightport_bryma1`** Bryma: “Andor? Yes, I think that was his name.”

    - Next → [brightport_bryma3](#d-brightport_bryma3)

    <span id="d-brightport_bryma48"></span>**`brightport_bryma48`** Bryma: “One thing I wish to mention, between Brightport and Charwood, there was a path that travelers would use. When I fled from Feygard, I took that path, but I was stopped by the same phenomenon as in the forest, and had to circle back to the…”

    - Next → [brightport_bryma49](#d-brightport_bryma49)

    <span id="d-brightport_bryma42"></span>**`brightport_bryma42`** Bryma: “Suffice to say, those bones are no longer around, I ground them to dust for my bonemeal research and fertilizer experiments.” — **effects:** sets stage 50 of [The balance of scales](../quests/brightport_lizard.md#stage-50)

    - “Great, and what am I suppossed to return now?” → [brightport_bryma43](#d-brightport_bryma43)

    <span id="d-brightport_bryma10"></span>**`brightport_bryma10`** Bryma: “We sat down and he started asking me all sorts of questions. I was glad to have someone to talk to. But soon, he pulled out a list of ingredients and asked about how to acquire and use them. Most which were highly poisonous.”

    - Next → [brightport_bryma11](#d-brightport_bryma11)

    <span id="d-brightport_bryma18"></span>**`brightport_bryma18`** Bryma: “The application of potions in baking, but primarily bonemeal potions. Their healing potency and various properties puzzled me for many years. I studied them with the great minds of Feygard and Nor City alike.” — **effects:** sets stage 106 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-106)

    - “What do potions have to do with baking?” → [brightport_bryma21](#d-brightport_bryma21)

    <span id="d-brightport_bryma9"></span>**`brightport_bryma9`** Bryma: “About half a year ago, I was carefully measuring the ingredients for my baking experiments when I heard the door creak. I went to look, and a boy who looked a little older than you introduced himself. I think his name was Andor...”

    - “[My brother Andor, here too?]” → [brightport_bryma10](#d-brightport_bryma10)

    <span id="d-brightport_bryma54"></span>**`brightport_bryma54`** Bryma: “For all of it's shortcomings, the cult and her followers fought against necromancy, and many masters of the dark arts perished under their swords. The statues are likely a seal for some evil that dwelt here in ancient times.”

    - “Shortcomings?” → [brightport_bryma55](#d-brightport_bryma55)
    - “What's the meaning of that password?” → [brightport_bryma56](#d-brightport_bryma56)

    <span id="d-brightport_bryma23"></span>**`brightport_bryma23`** Bryma: “First, what do you think makes bonemeal so potent that people still seek it out despite it now being illegal?”

    - “It's cheap and effective.” → [brightport_bryma27](#d-brightport_bryma27)
    - “Personally I don't know, that evil concoction hasn't been anywhere near my mouth.” *(if NOT used 1× [Bonemeal potion](../items/bonemeal_potion.md))* → [brightport_bryma24](#d-brightport_bryma24)
    - “I'm not sure, but the main ingredient is easy to find anywhere.” → [brightport_bryma25](#d-brightport_bryma25)

    <span id="d-brightport_bryma32"></span>**`brightport_bryma32`** Bryma: “But my experiments revealed something more. The late Headmaster Dervin rewarded me with an advanced bonemeal potion that contained a mysterious ingredient called kazarite, which doubled the potency of a regular potion.”

    - Next → [brightport_bryma33](#d-brightport_bryma33)

    <span id="d-brightport_bryma40"></span>**`brightport_bryma40`** Bryma: “One day, I ventured into that decrepit basement to see what was there. Curious, I began exploring and carelessly ventured down into a cave. Days later, I began hearing the scratching of monstrous claws echoing through the tunnels. Like a…” — **effects:** sets stage 5 of [The balance of scales](../quests/brightport_lizard.md#stage-5)

    - “I'll see what I can do about those creatures.” → [brightport_bryma41](#d-brightport_bryma41)

    <span id="d-brightport_bryma4"></span>**`brightport_bryma4`** Bryma: “Is that any way to speak to someone you just met? So rude! Here - have it. I wasn't intending to keep it anyway. And if you return, leave that attitude outside my cabin.” — **effects:** sets stage 95 of [No rest for the wicked](../quests/Stanwickquest.md#stage-95), gives 1× [Secret scroll](../items/brightport_scroll.md), sets stage 104 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-104)


    <span id="d-brightport_bryma5"></span>**`brightport_bryma5`** Bryma: “It was never my intention to keep it, as it's not particularly useful to me. Here, take it.” — **effects:** sets stage 92 of [No rest for the wicked](../quests/Stanwickquest.md#stage-92), gives 1× [Secret scroll](../items/brightport_scroll.md), sets stage 104 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-104)

    - “Thanks! I will make sure it's returned to its place.” → *conversation ends*

    <span id="d-brightport_bryma3"></span>**`brightport_bryma3`** Bryma: “He brought me a scroll, and in exchange, he wanted me to mentor him in alchemy.” — **effects:** sets stage 132 of [andor (hidden flag)](../quests/andor.md#stage-132)

    - “I was looking for that scroll, can I have it?” → [brightport_bryma5](#d-brightport_bryma5)
    - “You can give that scroll to me, or I can take it by force.” → [brightport_bryma4](#d-brightport_bryma4)

    <span id="d-brightport_bryma49"></span>**`brightport_bryma49`** Bryma: “I later investigated and found another statue, the activation word for that specific one is "Elythara" I hope this information assists you well.” — **effects:** sets stage 233 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-233)


    <span id="d-brightport_bryma43"></span>**`brightport_bryma43`** Bryma: “No need to look at me like that, if those bones are gone just find more to replace them with.”

    - Next → [brightport_bryma44](#d-brightport_bryma44)

    <span id="d-brightport_bryma11"></span>**`brightport_bryma11`** Bryma: “I tried to refuse him, but that's when his tone shifted. The cheerful charisma he'd shown vanished. As he pulled out that scroll, I heard him mumbling, 'last resort...'” — **effects:** sets stage 132 of [andor (hidden flag)](../quests/andor.md#stage-132), sets stage 105 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-105)

    - Next → [brightport_bryma12](#d-brightport_bryma12)

    <span id="d-brightport_bryma21"></span>**`brightport_bryma21`** Bryma: “Don't underestimate baking, child. To master this art takes years of arduous training, including the study of advanced alchemy.”

    - Next → [brightport_bryma16](#d-brightport_bryma16)

    <span id="d-brightport_bryma55"></span>**`brightport_bryma55`** Bryma: “I lived in Feygard among the northerners for several years, and the few who do not follow the Shadow bow down to the goddess Elythara. They take great pride in their past. Yet the light they praise has blinded more than it has…”

    - “Can we talk about something else?” → [brightport_bryma14](#d-brightport_bryma14)
    - “This has left me with more questions than answers.” → *conversation ends*

    <span id="d-brightport_bryma56"></span>**`brightport_bryma56`** Bryma: “The "Lethgar" password refers to the Lethgar people who lived over two thousand years ago. Perhaps their name was used by those who constructed the statues in remembrance of something.”

    - “Can we talk about something else?” → [brightport_bryma14](#d-brightport_bryma14)
    - “Interesting, I'll be on my way.” → *conversation ends*

    <span id="d-brightport_bryma27"></span>**`brightport_bryma27`** Bryma: “That simple answer is the closest to the correct one. And I would have told you the same, had I not dedicated my life to it.”

    - Next → [brightport_bryma26](#d-brightport_bryma26)

    <span id="d-brightport_bryma24"></span>**`brightport_bryma24`** Bryma: “I don't know whether to applaud your commitment or waive it off as a form of childish ignorance, but either way...”

    - Next → [brightport_bryma26](#d-brightport_bryma26)

    <span id="d-brightport_bryma25"></span>**`brightport_bryma25`** Bryma: “That is true, any ordinary tomb will do for some bones. And monsters are not an uncommon appearance in our day and age.” — **effects:** sets stage 110 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-110)

    - Next → [brightport_bryma26](#d-brightport_bryma26)

    <span id="d-brightport_bryma33"></span>**`brightport_bryma33`** Bryma: “This completely changed my perspective. When I asked for the recipe to identify the ingredient responsible, I was denied. But it was no setback. I soon realized that bones are not unique in their properties. It's common alchemical…”

    - Next → [brightport_bryma34](#d-brightport_bryma34)

    <span id="d-brightport_bryma41"></span>**`brightport_bryma41`** Bryma: “I appreciate your enthusiasm. The passage down is blocked but if you go deeper into the forest you'll find another statue. The activation word is "Light". Use it, and then find a way to their lair.” — **effects:** sets stage 10 of [The balance of scales](../quests/brightport_lizard.md#stage-10)


    <span id="d-brightport_bryma44"></span>**`brightport_bryma44`** Bryma: “Red or green, their bones look the same. Just slay those red ones along the shore of the lake until you have enough. Here's a few of what I've got left for starters.” — **effects:** sets stage 55 of [The balance of scales](../quests/brightport_lizard.md#stage-55), gives 3× [Lizardman bone](../items/brightport_bone.md)

    - Next → [brightport_bryma52](#d-brightport_bryma52)

    <span id="d-brightport_bryma12"></span>**`brightport_bryma12`** Bryma: “I had no choice but to accept it. I told him everything he wanted to know, and he left me with the scroll before leaving. It might have been useful to me twenty years ago, but I've already researched and developed my baking methods…”

    - “Can we talk about something else?” → [brightport_bryma14](#d-brightport_bryma14)
    - “What are you researching?” → [brightport_bryma18](#d-brightport_bryma18)

    <span id="d-brightport_bryma16"></span>**`brightport_bryma16`** Bryma: “It started in my second year at the academy, at the beginning of my baking studies. I set out to develop a unique leavening method to stand out from other bakers and make a name for myself.”

    - “[Listen quietly.]” → [brightport_bryma17](#d-brightport_bryma17)
    - “Great, another long story.” → [brightport_bryma17_alt](#d-brightport_bryma17_alt)

    <span id="d-brightport_bryma26"></span>**`brightport_bryma26`** Bryma: “The answer would be all the correct reasons you could cite. It's cheap, it's effective, and it worked for hundreds of years.”

    - Next → [brightport_bryma28](#d-brightport_bryma28)

    <span id="d-brightport_bryma34"></span>**`brightport_bryma34`** Bryma: “I call this the Theory of Essence. We all know that when the Rift opened, immense magical energy entered our plane along with the monstrous creatures. Before that, what I refer to as the essence already existed, but it was greatly…”

    - Next → [brightport_bryma35](#d-brightport_bryma35)

    <span id="d-brightport_bryma52"></span>**`brightport_bryma52`** Bryma: “If you can pacify those creatures and they're truly capable of reason, see if you can come to an understanding. They could supply me with what I need.” — **effects:** sets stage 221 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-221)


    <span id="d-brightport_bryma17"></span>**`brightport_bryma17`** Bryma: “I tried using different yeasts, temperatures, and moisture levels, but none gave me the results I was hoping for. On a whim, I decided to mix a bonemeal potion into the process.”

    - Next → [brightport_bryma19](#d-brightport_bryma19)

    <span id="d-brightport_bryma17_alt"></span>**`brightport_bryma17_alt`** Bryma: “Shush.”

    - Next → [brightport_bryma17](#d-brightport_bryma17)

    <span id="d-brightport_bryma28"></span>**`brightport_bryma28`** Bryma: “But if you think I'm a blind supporter of its use, you're mistaken. In the first place, don't you think there's something off about it? It's easy to make and immensely effective.”

    - Next → [brightport_bryma29](#d-brightport_bryma29)

    <span id="d-brightport_bryma35"></span>**`brightport_bryma35`** Bryma: “This essence exists within every part of Dhayavar. The soil, the mountains, the creatures, and the people all hold it. The proof lies in the crystals that form inside monsters. These crystals are concentrated forms of essence. Bones are…” — **effects:** sets stage 111 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-111)

    - Next → [brightport_bryma36](#d-brightport_bryma36)

    <span id="d-brightport_bryma19"></span>**`brightport_bryma19`** Bryma: “To my amazement, the bread rose to nearly triple its size! That's when I brought it to the Headmaster's attention. It was very well received, and I was rewarded with a specially made bonemeal potion from his collection.” — **effects:** sets stage 257 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-257)

    - Next → [brightport_bryma20](#d-brightport_bryma20)

    <span id="d-brightport_bryma29"></span>**`brightport_bryma29`** Bryma: “Not to mention that the origin of those bones could have very well have been human. There have been stories of such things having been done, especially during plagues...”

    - “I thought we would be talking about your research?” → [brightport_bryma30](#d-brightport_bryma30)

    <span id="d-brightport_bryma36"></span>**`brightport_bryma36`** Bryma: “Not to say it's all the same. Some things, despite containing a high concentration of essence, can be harmful. Such as poisons or diseases that drain our lifeforce. Merely consuming more has no benefit, and indeed there have to be certain…”

    - Next → [brightport_bryma51](#d-brightport_bryma51)

    <span id="d-brightport_bryma20"></span>**`brightport_bryma20`** Bryma: “But the bread baked using that potion started mutating, much like what you can see in my kitchen. Soon afterward, my research was banned, and I had no choice but to leave if I wanted to continue my studies.” — **effects:** sets stage 107 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-107)

    - “Can I ask you something else?” → [brightport_bryma14](#d-brightport_bryma14)
    - “Thanks for telling me this story. I will be on my way.” → *conversation ends*

    <span id="d-brightport_bryma30"></span>**`brightport_bryma30`** Bryma: “Oh right, my apologies. I got a bit sidetracked. Yes, where do I begin.”

    - Next → [brightport_bryma31](#d-brightport_bryma31)

    <span id="d-brightport_bryma51"></span>**`brightport_bryma51`** Bryma: “That is the gist of my research, which is mostly a theory. I was preparing to publish and discuss it among the scholars of Feygard before I fled.”

    - “Can we talk about something else?” → [brightport_bryma14](#d-brightport_bryma14)
    - “That's a lot to digest, I think I'll leave now.” → *conversation ends*



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `brightportnpc7` · Data from v0.8.18</small>
