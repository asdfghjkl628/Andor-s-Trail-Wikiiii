# ![](../assets/icons/monsters/monsters_rltiles2_92.png){ .sprite } Kealwea

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

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Regular potion of health](../items/health.md) | 100% | 8 to 10 |
| [Minor vial of health](../items/health_minor.md) | 100% | 5 to 10 |
| [Major potion of health](../items/health_major2.md) | 100% | 3 to 6 |
| [Hat of the protector](../items/hat_of_protector.md) | 100% | 1 |

## Found on

- [sullengard_church](../maps/sullengard_church.md)

## Quests

- [Beer Bootlegging](../quests/beer_bootlegging.md): stages 70
- [Pond safety](../quests/sullengard_pond_safety.md): stages 40
- [The exploded star](../quests/mg2_exploded_star.md): stages 12, 17, 20, 32, 40, 47, 48, 52
- [The fifth master](../quests/fifth_master.md): stages 40
- [mg2_exploded_star_nd (hidden flag)](../quests/mg2_exploded_star_nd.md): stages 90, 91

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Kealwea. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/sullengard_kealwea_00.json" data-npc="Kealwea" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (48 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-sullengard_kealwea_00"></span>**`sullengard_kealwea_00`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 91 of [mg2_exploded_star_nd (hidden flag)](../quests/mg2_exploded_star_nd.md#stage-91))* → [sullengard_kealwea_0](#d-sullengard_kealwea_0)
    - branch 2 *(if NOT reached stage 12 of [The exploded star](../quests/mg2_exploded_star.md#stage-12); reached stage 80 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-80))* → [mg2_kealwea_2](#d-mg2_kealwea_2)
    - branch 3 *(if reached stage 17 of [The exploded star](../quests/mg2_exploded_star.md#stage-17); NOT reached stage 47 of [The exploded star](../quests/mg2_exploded_star.md#stage-47); NOT reached stage 48 of [The exploded star](../quests/mg2_exploded_star.md#stage-48); NOT reached stage 52 of [The exploded star](../quests/mg2_exploded_star.md#stage-52))* → [mg2_kealwea_20](#d-mg2_kealwea_20)
    - branch 4 *(if reached stage 12 of [The exploded star](../quests/mg2_exploded_star.md#stage-12); NOT reached stage 17 of [The exploded star](../quests/mg2_exploded_star.md#stage-17))* → [mg2_kealwea_3](#d-mg2_kealwea_3)
    - branch 5 → [sullengard_kealwea_0](#d-sullengard_kealwea_0)

    <span id="d-sullengard_kealwea_0"></span>**`sullengard_kealwea_0`** Kealwea: “Ah, young traveller. I am Kealwea. How can I help you, my child?”

    - “I am in need of supplies. Can you help?” → [sullengard_kealwea_sell](#d-sullengard_kealwea_sell)
    - “Nanette told me to see you about her pond.” *(if reached stage 30 of [Pond safety](../quests/sullengard_pond_safety.md#stage-30); NOT reached stage 40 of [Pond safety](../quests/sullengard_pond_safety.md#stage-40))* → [sullengard_kealwea_pond_safety_1](#d-sullengard_kealwea_pond_safety_1)
    - “Mayor Ale has asked me to give this letter to you.” *(if latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-60) is 60; hand over 1× [Mayor Ale's letter](../items/sullengard_mayor_letter.md))* → [sullengard_kealwea_letter](#d-sullengard_kealwea_letter)
    - “I am searching for something called "The Ritual of Five Aspects". I was told it may have passed through this town long…” *(if reached stage 30 of [The fifth master](../quests/fifth_master.md#stage-30); NOT reached stage 50 of [The fifth master](../quests/fifth_master.md#stage-50))* → [sullengard_kealwea_kazaul_1](#d-sullengard_kealwea_kazaul_1)

    <span id="d-mg2_kealwea_2"></span>**`mg2_kealwea_2`** Kealwea: “You saw it too, didn't you?”

    - “Sure.” → [mg2_kealwea_3](#d-mg2_kealwea_3)
    - “What do you mean?” → [mg2_kealwea_3](#d-mg2_kealwea_3)
    - “No, I haven't had any mead today.” → [mg2_kealwea_2a](#d-mg2_kealwea_2a)
    - “I am $playername.” → [mg2_kealwea_2a](#d-mg2_kealwea_2a)

    <span id="d-mg2_kealwea_20"></span>**`mg2_kealwea_20`** Kealwea: “Kid, anything new about those fallen lights over Mt.Galmore?”

    - “I haven't found any pieces yet.” *(if NOT faction “mg2_exploded_star” ≥ 1)* → [mg2_starwatcher_22](#d-mg2_starwatcher_22)
    - “Here I have some pieces already.” *(if carry 1× [Piece of bright shining crystal](../items/mg2_exploded_star.md); NOT carry 10× [Piece of bright shining crystal](../items/mg2_exploded_star.md))* → [mg2_starwatcher_24](#d-mg2_starwatcher_24)
    - “I might give you half of them - five pieces.” *(if carry 5× [Piece of bright shining crystal](../items/mg2_exploded_star.md); reached stage 15 of [The exploded star](../quests/mg2_exploded_star.md#stage-15); NOT reached stage 45 of [The exploded star](../quests/mg2_exploded_star.md#stage-45); NOT reached stage 47 of [The exploded star](../quests/mg2_exploded_star.md#stage-47))* → [mg2_kealwea_25](#d-mg2_kealwea_25)
    - “I might give you the rest of them - five pieces.” *(if hand over 5× [Piece of bright shining crystal](../items/mg2_exploded_star.md); reached stage 45 of [The exploded star](../quests/mg2_exploded_star.md#stage-45))* → [mg2_kealwea_28](#d-mg2_kealwea_28)
    - “I have found all of the ten pieces.” *(if reached stage 110 of [The exploded star](../quests/mg2_exploded_star.md#stage-110); NOT reached stage 20 of [The exploded star](../quests/mg2_exploded_star.md#stage-20); NOT reached stage 40 of [The exploded star](../quests/mg2_exploded_star.md#stage-40); NOT reached stage 47 of [The exploded star](../quests/mg2_exploded_star.md#stage-47); NOT reached stage 48 of [The exploded star](../quests/mg2_exploded_star.md#stage-48); NOT reached stage 50 of [The exploded star](../quests/mg2_exploded_star.md#stage-50))* → [mg2_kealwea_30](#d-mg2_kealwea_30)
    - “I have found all of the ten pieces, but I have already given them to Teccow in Stoutford.” *(if reached stage 50 of [The exploded star](../quests/mg2_exploded_star.md#stage-50))* → [mg2_starwatcher_32](#d-mg2_starwatcher_32)
    - “I need some help of the local priest.” → [sullengard_kealwea_0](#d-sullengard_kealwea_0)

    <span id="d-mg2_kealwea_3"></span>**`mg2_kealwea_3`** Kealwea: “There was a tear in the heavens. Not a star falling, but something cast down.”

    - Next → [mg2_kealwea_4](#d-mg2_kealwea_4)

    <span id="d-sullengard_kealwea_sell"></span>**`sullengard_kealwea_sell`** Kealwea: “Of course my child. Here, let's take a look at what I have.”

    - “Thank you!” → *shop opens*

    <span id="d-sullengard_kealwea_pond_safety_1"></span>**`sullengard_kealwea_pond_safety_1`** Kealwea: “[Sigh]. Yes, she told me about her pond as well, but she won't listen to my story.”

    - “I will listen to your story.” → [sullengard_kealwea_pond_safety_2](#d-sullengard_kealwea_pond_safety_2)
    - “That will be a long story.” → *conversation ends*

    <span id="d-sullengard_kealwea_letter"></span>**`sullengard_kealwea_letter`** Kealwea: “Oh, I've been expecting this. Thank you.” — **effects:** sets stage 70 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-70)


    <span id="d-sullengard_kealwea_kazaul_1"></span>**`sullengard_kealwea_kazaul_1`** Kealwea: “"The Ritual of Five Aspects"? That is not a name I hear often, my child. Some years back, when I first took stewardship of this church, I found mention of a strange relic - a bundle of parchment in an unknown tongue. It was sent north to…”

    - “Do you remember who sent it there?” → [sullengard_kealwea_kazaul_2](#d-sullengard_kealwea_kazaul_2)
    - “So it was once here in Sullengard?” → [sullengard_kealwea_kazaul_3](#d-sullengard_kealwea_kazaul_3)

    <span id="d-mg2_kealwea_2a"></span>**`mg2_kealwea_2a`** Kealwea: “Sorry, where are my manners?”

    - Next → [sullengard_kealwea_0](#d-sullengard_kealwea_0)

    <span id="d-mg2_starwatcher_22"></span>**`mg2_starwatcher_22`** Kealwea: “Don't waste time. Go again and find them. It is urgent!”


    <span id="d-mg2_starwatcher_24"></span>**`mg2_starwatcher_24`** Kealwea: “Good, good. But these are not all of them. It must be ten - where are the others?”


    <span id="d-mg2_kealwea_25"></span>**`mg2_kealwea_25`** Kealwea: “You must be out of your mind! They are deadly - let me destroy all of them.”

    - “OK, you are right. Here take them and do what you must.” *(if hand over 10× [Piece of bright shining crystal](../items/mg2_exploded_star.md))* → [mg2_kealwea_50](#d-mg2_kealwea_50)
    - “No, I will give you only half of them.” *(if hand over 5× [Piece of bright shining crystal](../items/mg2_exploded_star.md))* → [mg2_kealwea_26](#d-mg2_kealwea_26)

    <span id="d-mg2_kealwea_28"></span>**`mg2_kealwea_28`** Kealwea: “Good, good. I'll destroy these dangerous things.” — **effects:** sets stage 48 of [The exploded star](../quests/mg2_exploded_star.md#stage-48)

    - “Great to hear. And now I have to go and find my brother at last.” → *conversation ends*

    <span id="d-mg2_kealwea_30"></span>**`mg2_kealwea_30`** Kealwea: “Good, good. Give them to me. I'll destroy these dangerous things.” — **effects:** sets stage 32 of [The exploded star](../quests/mg2_exploded_star.md#stage-32)

    - “I seem to have lost them. Just a minute, I'll look for them ...” *(if NOT carry 10× [Piece of bright shining crystal](../items/mg2_exploded_star.md); NOT reached stage 50 of [The exploded star](../quests/mg2_exploded_star.md#stage-50))* → *conversation ends*
    - “But I have already given them to Teccow in Stoutford.” *(if reached stage 50 of [The exploded star](../quests/mg2_exploded_star.md#stage-50))* → [mg2_starwatcher_32](#d-mg2_starwatcher_32)
    - “Here you go. Take it and do what you have to do.” *(if hand over 10× [Piece of bright shining crystal](../items/mg2_exploded_star.md))* → [mg2_kealwea_50](#d-mg2_kealwea_50)
    - “I've changed my mind. These glittery things are too pretty to be destroyed.” *(if carry 10× [Piece of bright shining crystal](../items/mg2_exploded_star.md))* → [mg2_kealwea_40](#d-mg2_kealwea_40)
    - “Hmm, I still have to think about it. I'll be back...” → *conversation ends*

    <span id="d-mg2_starwatcher_32"></span>**`mg2_starwatcher_32`** Kealwea: “You fool!” — **effects:** sets stage 91 of [mg2_exploded_star_nd (hidden flag)](../quests/mg2_exploded_star_nd.md#stage-91)

    - “It was the right thing to do.” → [mg2_starwatcher_34](#d-mg2_starwatcher_34)

    <span id="d-mg2_kealwea_4"></span>**`mg2_kealwea_4`** Kealwea: “It wept fire. And the mountain answered with a shudder. Such things are not random.”

    - Next → [mg2_kealwea_5](#d-mg2_kealwea_5)

    <span id="d-sullengard_kealwea_pond_safety_2"></span>**`sullengard_kealwea_pond_safety_2`** Kealwea: “I used to go there when I was a young disciple.”

    - Next → [sullengard_kealwea_pond_safety_3](#d-sullengard_kealwea_pond_safety_3)

    <span id="d-sullengard_kealwea_kazaul_2"></span>**`sullengard_kealwea_kazaul_2`** Kealwea: “It was before my time, but the records say it came from one of my predecessors, the first priest to serve under the banner of the Shadow here. He noted that it was delivered to him by travelers claiming to have found it among the ruins to…”

    - “Ruins to the west, perhaps where Varnel perished.” → [sullengard_kealwea_kazaul_4](#d-sullengard_kealwea_kazaul_4)

    <span id="d-sullengard_kealwea_kazaul_3"></span>**`sullengard_kealwea_kazaul_3`** Kealwea: “So it seems. It rested in our archives for generations, though no one could read it. When the scholars from Remgard offered to take it, we gladly let them. It felt unsettling to keep something no one understood.”

    - “Then Remgard is where I must go next.” → [sullengard_kealwea_kazaul_4](#d-sullengard_kealwea_kazaul_4)

    <span id="d-mg2_kealwea_50"></span>**`mg2_kealwea_50`** Kealwea: “Wonderful. You have no idea what terrible things this crystal could have done.” — **effects:** sets stage 52 of [The exploded star](../quests/mg2_exploded_star.md#stage-52)

    - “Yes - whatever it was exactly.” → [mg2_kealwea_52](#d-mg2_kealwea_52)

    <span id="d-mg2_kealwea_26"></span>**`mg2_kealwea_26`** Kealwea: “Well, I am going to destroy these five. I hope you will be careful with the others and don't rue your decision.” — **effects:** sets stage 47 of [The exploded star](../quests/mg2_exploded_star.md#stage-47)

    - “I might throw the remaining ones at Andor. Hmm ...” *(if carry 1× [Piece of bright shining crystal](../items/mg2_exploded_star.md))* → [mg2_starwatcher_27](#d-mg2_starwatcher_27)

    <span id="d-mg2_kealwea_40"></span>**`mg2_kealwea_40`** Kealwea: “You must be out of your mind! Free yourself from them or you are lost!”

    - “No. I will keep them.” → [mg2_starwatcher_42](#d-mg2_starwatcher_42)
    - “You are certainly right. Take it and do what you have to do.” *(if hand over 10× [Piece of bright shining crystal](../items/mg2_exploded_star.md))* → [mg2_kealwea_50](#d-mg2_kealwea_50)

    <span id="d-mg2_starwatcher_34"></span>**`mg2_starwatcher_34`** Kealwea: “It is bad. But I won't talk about it anymore.”


    <span id="d-mg2_kealwea_5"></span>**`mg2_kealwea_5`** [Dummy NPC](../monsters/none.md): “He gestured to the dark Galmore montains in the distant west.”

    - Next → [mg2_kealwea_10](#d-mg2_kealwea_10)

    <span id="d-sullengard_kealwea_pond_safety_3"></span>**`sullengard_kealwea_pond_safety_3`** Kealwea: “One time, I was sitting on the bench thinking about how the Feygard soldiers can sleep at night with all of their unlawful taxes placed on the citizens of Sullengard causing all this financial trouble on the people.”

    - Next → [sullengard_kealwea_pond_safety_4](#d-sullengard_kealwea_pond_safety_4)

    <span id="d-sullengard_kealwea_kazaul_4"></span>**`sullengard_kealwea_kazaul_4`** Kealwea: “If you seek that ritual, Remgard's church library is where your path leads.” — **effects:** sets stage 40 of [The fifth master](../quests/fifth_master.md#stage-40)

    - “Thank you, Kealwea.” → *conversation ends*

    <span id="d-mg2_kealwea_52"></span>**`mg2_kealwea_52`** Kealwea: “You did the right thing. The whole world is grateful to you.”

    - “I do something like that every other day.” → *conversation ends*
    - “I can't buy anything with words of thanks.” → [mg2_kealwea_54](#d-mg2_kealwea_54)

    <span id="d-mg2_starwatcher_27"></span>**`mg2_starwatcher_27`** Kealwea: “What???”

    - “Nothing. Bye.” → *conversation ends*

    <span id="d-mg2_starwatcher_42"></span>**`mg2_starwatcher_42`** Kealwea: “NOOOOO!!” — **effects:** sets stage 40 of [The exploded star](../quests/mg2_exploded_star.md#stage-40), sets stage 91 of [mg2_exploded_star_nd (hidden flag)](../quests/mg2_exploded_star_nd.md#stage-91)

    - “Now you're exaggerating. I'll go then.” → *conversation ends*

    <span id="d-mg2_kealwea_10"></span>**`mg2_kealwea_10`** [Kealwea](../monsters/sullengard_priest.md): “Ten fragments of that burning star scattered along Galmore's bones. They are still warm. Still ... humming.” — **effects:** sets stage 12 of [The exploded star](../quests/mg2_exploded_star.md#stage-12)

    - “Can I help?” → [mg2_kealwea_14](#d-mg2_kealwea_14)
    - “How do you know there are ten pieces?” → [mg2_kealwea_12](#d-mg2_kealwea_12)
    - “Ten tongues of light, each flickering in defiance of the dark.” *(if reached stage 10 of [The exploded star](../quests/mg2_exploded_star.md#stage-10))* → [mg2_kealwea_11](#d-mg2_kealwea_11)

    <span id="d-sullengard_kealwea_pond_safety_4"></span>**`sullengard_kealwea_pond_safety_4`** Kealwea: “My anger arose to the point that I lifted up a large rock and threw it in the pond.”

    - Next → [sullengard_kealwea_pond_safety_5](#d-sullengard_kealwea_pond_safety_5)

    <span id="d-mg2_kealwea_54"></span>**`mg2_kealwea_54`** Kealwea: “Oh. I understand.”

    - Next → [mg2_kealwea_56](#d-mg2_kealwea_56)

    <span id="d-mg2_kealwea_14"></span>**`mg2_kealwea_14`** Kealwea: “[Ominous voice] In The Ash I Saw Them - Ten Tongues Of Light, Each Flickering In Defiance Of The Dark.”

    - Next → [mg2_kealwea_15](#d-mg2_kealwea_15)

    <span id="d-mg2_kealwea_12"></span>**`mg2_kealwea_12`** Kealwea: “I can feel it.”

    - “You can feel that there are ten? Wow.” → [mg2_kealwea_14](#d-mg2_kealwea_14)

    <span id="d-mg2_kealwea_11"></span>**`mg2_kealwea_11`** Kealwea: “How do you know?!”

    - “Teccow, a stargazer in Stoutford, told me so. Now go on.” → [mg2_kealwea_16](#d-mg2_kealwea_16)

    <span id="d-sullengard_kealwea_pond_safety_5"></span>**`sullengard_kealwea_pond_safety_5`** Kealwea: “After that, I saw some snappers emerge from the pond and attack me before I even realized what had happened. Good thing they are too slow to catch me as I quickly composed myself and limped home.”

    - Next → [sullengard_kealwea_pond_safety_6](#d-sullengard_kealwea_pond_safety_6)

    <span id="d-mg2_kealwea_56"></span>**`mg2_kealwea_56`** Kealwea: “I can't give you any gold. That belongs to the church.”

    - “Sure.” → [mg2_kealwea_60](#d-mg2_kealwea_60)

    <span id="d-mg2_kealwea_15"></span>**`mg2_kealwea_15`** Kealwea: “Their Number Is Ten. Not Nine. Not Eleven. Ten.”

    - “All right, all right. Ten.” → [mg2_kealwea_16](#d-mg2_kealwea_16)

    <span id="d-mg2_kealwea_16"></span>**`mg2_kealwea_16`** Kealwea: “So if you have no more questions ...”

    - “Well, why don't you go and collect them?” → [mg2_kealwea_17](#d-mg2_kealwea_17)

    <span id="d-sullengard_kealwea_pond_safety_6"></span>**`sullengard_kealwea_pond_safety_6`** Kealwea: “The moral of my story is to never again to throw rocks there, be it small or large. Thank you for listening. Please talk to Nanette about this.” — **effects:** sets stage 40 of [Pond safety](../quests/sullengard_pond_safety.md#stage-40)

    - “Oh, I understand now. I have to tell her about this one. Bye” → *conversation ends*
    - “Oh, good thing it's not a long story. I'm about to start snoring here. Bye.” → *conversation ends*

    <span id="d-mg2_kealwea_60"></span>**`mg2_kealwea_60`** Kealwea: “But this little book might bring you joy. Wait, I'll write you a dedication inside.” — **effects:** gives 1× [Booklet from Kealwea](../items/mg2_rewarded_book.md)

    - “Thank you.” → *conversation ends*

    <span id="d-mg2_kealwea_17"></span>**`mg2_kealwea_17`** Kealwea: “Only little children could ask such a stupid question. Of course I can't go. Sullengard needs me here.”

    - Next → [mg2_kealwea_17b](#d-mg2_kealwea_17b)

    <span id="d-mg2_kealwea_17b"></span>**`mg2_kealwea_17b`** Kealwea: “Hmm, but you could go.”

    - “Me?” → [mg2_kealwea_18](#d-mg2_kealwea_18)

    <span id="d-mg2_kealwea_18"></span>**`mg2_kealwea_18`** Kealwea: “'Yes. Bring these shards to me. Before the mountain's curse draws worse than beasts to them!” — **effects:** sets stage 17 of [The exploded star](../quests/mg2_exploded_star.md#stage-17)

    - “But ...” *(if NOT faction “mg2_exploded_star” ≥ 1)* → [mg2_starwatcher_19](#d-mg2_starwatcher_19)
    - “In fact I was already there.” *(if faction “mg2_exploded_star” ≥ 1)* → [mg2_kealwea_20](#d-mg2_kealwea_20)

    <span id="d-mg2_starwatcher_19"></span>**`mg2_starwatcher_19`** Kealwea: “[Ominous voice] Bring The Ten Pieces ...”

    - “Enough, please! I can't think when you are talking like this.” → *conversation ends*
    - “Forget it, do it yourself.” → [mg2_starwatcher_19a](#d-mg2_starwatcher_19a)

    <span id="d-mg2_starwatcher_19a"></span>**`mg2_starwatcher_19a`** Kealwea: “So you really don't want to help? And save the world from this disaster?”

    - “Maybe later. I have to go now.” → *conversation ends*
    - “No, I have enough other things to do.” → [mg2_starwatcher_19b](#d-mg2_starwatcher_19b)

    <span id="d-mg2_starwatcher_19b"></span>**`mg2_starwatcher_19b`** Kealwea: “Woe, woe! Then leave me. I hope you can live with the guilt.” — **effects:** sets stage 20 of [The exploded star](../quests/mg2_exploded_star.md#stage-20), sets stage 90 of [mg2_exploded_star_nd (hidden flag)](../quests/mg2_exploded_star_nd.md#stage-90), sets stage 91 of [mg2_exploded_star_nd (hidden flag)](../quests/mg2_exploded_star_nd.md#stage-91)




## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 9 lines added |
| [v0.8.14](../versions/0.8.14.md) | phraseID: sullengard_kealwea_0 → sullengard_kealwea_00<br>Dialogue: 35 lines added |
| [v0.8.15](../versions/0.8.15.md) | Dialogue: 1 line changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 4 lines added, 1 line changed<br>· text: “Hey, young fellow. I am Kealwea. How can I help you my child?” → “Ah, young traveller. I am Kealwea. How can I help you, my child?” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_priest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_priest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_priest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_priest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `sullengard_priest` · Data from v0.8.18</small>
