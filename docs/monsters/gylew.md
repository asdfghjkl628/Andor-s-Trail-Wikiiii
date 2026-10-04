# ![](../assets/icons/monsters/monsters_mage2_0.png){ .sprite } Gylew

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 180 |
| Max AP | 10 |
| Attack cost | 5 |
| Move cost | 5 |
| Damage | 10 to 22 |
| Attack chance | 60 |
| Block chance | 40 |
| Damage resistance | 0 |
| Critical skill | 20 |
| Critical multiplier | 2.0 |

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Liquid courage](../items/pot_courage.md) | 10% | 1 |
| [Gold coins](../items/gold.md) | 100% | 20 to 50 |
| [Regular potion of health](../items/health.md) | 100% | 2 to 3 |
| [Gylew's key](../items/gylew_key.md) | 100% | 1 |

## Found on

- [waterway5](../maps/waterway5.md)

## Quests

- [The odd coin collector](../quests/odd_coin_collector.md): stages 10, 11, 12, 13, 20, 60, 62, 100, 105
- [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md): stages 44, 45, 47, 48
- [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md): stages 105, 106, 107

??? quote "Dialogue (71 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-gylew"></span>**`gylew`** Gylew: “Hey kid.”

    - “I'm not a kid anymore. Let's talk about the Korhald coins.” *(if reached stage 40 of [The odd coin collector](../quests/odd_coin_collector.md#stage-40); NOT reached stage 100 of [The odd coin collector](../quests/odd_coin_collector.md#stage-100); NOT reached stage 105 of [The odd coin collector](../quests/odd_coin_collector.md#stage-105))* → [gylew_korhald_10](#d-gylew_korhald_10)
    - “Hey old man.” *(if NOT reached stage 100 of [The odd coin collector](../quests/odd_coin_collector.md#stage-100); NOT reached stage 105 of [The odd coin collector](../quests/odd_coin_collector.md#stage-105))* → [gylew_old_man](#d-gylew_old_man)
    - “Hey. I found the Korhald tomb and it had two items that I think might interest you.” *(if latest stage of [The odd coin collector](../quests/odd_coin_collector.md#stage-66) is 66; carry 1× [Shield of the Brave](../items/shield_of_brave.md); carry 1× [Coin of Prestige](../items/hero_coin.md))* → [gylew_korhald_cop_0](#d-gylew_korhald_cop_0)
    - “Hey. I found the Korhald tomb and it had two items that I think might interest you.” *(if latest stage of [The odd coin collector](../quests/odd_coin_collector.md#stage-66) is 66; wearing [Shield of the Brave](../items/shield_of_brave.md); carry 1× [Coin of Prestige](../items/hero_coin.md))* → [gylew_korhald_cop_0](#d-gylew_korhald_cop_0)
    - “Inside the Korhald tomb, I found a locked chest. Do you know where I can find its key?” *(if reached stage 66 of [The odd coin collector](../quests/odd_coin_collector.md#stage-66); reached stage 50 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-50))* → [odd_coin_collector_ask_about_locked_chest](#d-odd_coin_collector_ask_about_locked_chest)
    - “About that "Coin of Prestige"...” *(if reached stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47))* → [gylew_korhald_cop_30a](#d-gylew_korhald_cop_30a)
    - “Hey. I need to go now and find this map.” *(if latest stage of [The odd coin collector](../quests/odd_coin_collector.md#stage-60) is 60)* → *conversation ends*
    - “I found these glowing coins in a pit beneath the well in Wexlow Village. They seem magical.” *(if reached stage 100 of [The odd coin collector](../quests/odd_coin_collector.md#stage-100); carry 3× [Mysterious coin](../items/mysterious_coin.md))* → [coin_collector_troll_coins](#d-coin_collector_troll_coins)
    - “We have no more business to discuss. I'll see you later.” *(if latest stage of [The odd coin collector](../quests/odd_coin_collector.md#stage-100) is 100)* → *conversation ends*
    - “I found these glowing coins in a pit beneath the well in Wexlow Village. They seem magical.” *(if reached stage 105 of [The odd coin collector](../quests/odd_coin_collector.md#stage-105); carry 3× [Mysterious coin](../items/mysterious_coin.md))* → [coin_collector_troll_coins](#d-coin_collector_troll_coins)
    - “I was glad to help fulfill you and your father's dream, but I need to go now.” *(if reached stage 105 of [The odd coin collector](../quests/odd_coin_collector.md#stage-105))* → *conversation ends*
    - “[Lie]I have these bronze and silver coins that I "acquired" in a game of chance. I would like to know if you are…” *(if reached stage 106 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-106); reached stage 80 of [Wanted men](../quests/wanted_men.md#stage-80); carry 50× [Bronze coin](../items/bronze_coin.md); carry 60× [Silver coin](../items/silver_coin.md); NOT reached stage 107 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-107))* → [coin_collector_thief_coins_10](#d-coin_collector_thief_coins_10)

    <span id="d-gylew_korhald_10"></span>**`gylew_korhald_10`** Gylew: “Did you find them?”

    - “Yes.” *(if carry 1× [Korhald coin chest](../items/korhald_coins.md); carry 1× [Forenza's key](../items/forenza_key.md); NOT reached stage 62 of [The odd coin collector](../quests/odd_coin_collector.md#stage-62))* → [gylew_korhald_20](#d-gylew_korhald_20)
    - “Yes and I already gave them to you.” *(if reached stage 105 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-105))* → [gylew_korhald_25](#d-gylew_korhald_25)
    - “Yes, I found the Korhald coins, but you are not getting them...[Attack]” *(if reached stage 50 of [The odd coin collector](../quests/odd_coin_collector.md#stage-50))* → [gylew_attack](#d-gylew_attack)
    - “Yes, but I don't have them on me. I will go get them.” *(if NOT carry 1× [Korhald coin chest](../items/korhald_coins.md); NOT reached stage 62 of [The odd coin collector](../quests/odd_coin_collector.md#stage-62))* → *conversation ends*

    <span id="d-gylew_old_man"></span>**`gylew_old_man`** Gylew: “Oh, you think you are a funny kid? I see.”

    - “Let's talk about the Korhald coins.” *(if reached stage 40 of [The odd coin collector](../quests/odd_coin_collector.md#stage-40))* → [gylew_korhald_10](#d-gylew_korhald_10)
    - “Yeah, actually, I do think so.” *(if NOT reached stage 20 of [The odd coin collector](../quests/odd_coin_collector.md#stage-20))* → [gylew_old_man_10a](#d-gylew_old_man_10a)
    - “Umm...” *(if reached stage 20 of [The odd coin collector](../quests/odd_coin_collector.md#stage-20))* → [gylew_old_man_10b](#d-gylew_old_man_10b)

    <span id="d-gylew_korhald_cop_0"></span>**`gylew_korhald_cop_0`** Gylew: “Oh, really?! Let me see them and we can talk more.”

    - “[You show Gylew the Coin of Prestige and the Shield of the brave]” → [gylew_korhald_cop_10](#d-gylew_korhald_cop_10)

    <span id="d-odd_coin_collector_ask_about_locked_chest"></span>**`odd_coin_collector_ask_about_locked_chest`** Gylew: “A locked chest you say? Well, I'm not really sure, but logic tells me to look back in the Laeroth Manor.”

    - “Oh, yeah. That makes sense.” → *conversation ends*
    - “Oh, come on! I don't want to go back there again.” → *conversation ends*

    <span id="d-gylew_korhald_cop_30a"></span>**`gylew_korhald_cop_30a`** Gylew: “I don't know anything about it. Which makes me want it even more. Can I have it? I will reward you handsomely for it.”

    - “Reward?! I always love the sound of that. What are we talking here? 10,000 gold? 20,000 gold?” → [gylew_korhald_cop_40](#d-gylew_korhald_cop_40)
    - “Here, take it. I have enough coins.” *(if hand over 1× [Coin of Prestige](../items/hero_coin.md))* → [gylew_korhald_cop_35](#d-gylew_korhald_cop_35)

    <span id="d-coin_collector_troll_coins"></span>**`coin_collector_troll_coins`** Gylew: “Ah, these are Enchanted Coins, crafted by ancient wizards who once drew magic from the well's waters. The runes on these coins change patterns, a sign of their magical origin. Such artifacts are rare indeed.”

    - “What can you tell me about their enchantment?” → [coin_collector_troll_coins_2](#d-coin_collector_troll_coins_2)
    - “Boring.” → *conversation ends*

    <span id="d-coin_collector_thief_coins_10"></span>**`coin_collector_thief_coins_10`** Gylew: “Sure. Let's see what you have.”

    - “[Show the coins]” → [coin_collector_thief_coins_20](#d-coin_collector_thief_coins_20)

    <span id="d-gylew_korhald_20"></span>**`gylew_korhald_20`** Gylew: “Great! Let me have them.”

    - “Here you go.” *(if hand over 1× [Korhald coin chest](../items/korhald_coins.md))* → [gylew_korhald_30](#d-gylew_korhald_30)

    <span id="d-gylew_korhald_25"></span>**`gylew_korhald_25`** Gylew: “You did? Oh, yes, I remember now.”

    - “You're a crazy old man.” → [gylew_korhald_27](#d-gylew_korhald_27)

    <span id="d-gylew_attack"></span>**`gylew_attack`** Gylew: “What? Why?” — **effects:** sets stage 62 of [The odd coin collector](../quests/odd_coin_collector.md#stage-62)

    - “You are not rightful.” → [gylew_attack_2](#d-gylew_attack_2)

    <span id="d-gylew_old_man_10a"></span>**`gylew_old_man_10a`** Gylew: “Show me your gold.”

    - “No way. I'm out of here.” → *conversation ends*
    - “Um...sure, I guess.” → [gylew2](#d-gylew2)

    <span id="d-gylew_old_man_10b"></span>**`gylew_old_man_10b`** Gylew: “What are you waiting for? Go find those Korhald coins!”


    <span id="d-gylew_korhald_cop_10"></span>**`gylew_korhald_cop_10`** Gylew: “Hmm...these are indeed interesting. Very interesting in fact.”

    - “[While trying to hold back the giant smile that you can feel growing upon your face, you ask 'why is that?']” → [gylew_korhald_cop_20](#d-gylew_korhald_cop_20)

    <span id="d-gylew_korhald_cop_40"></span>**`gylew_korhald_cop_40`** Gylew: “[While laughing] Now, now, don't get greedy on me. How about 7,000 gold and I will tell people we are friends?”

    - “Sounds like a great deal. I'll take it.” *(if hand over 1× [Coin of Prestige](../items/hero_coin.md))* → [gylew_korhald_cop_50](#d-gylew_korhald_cop_50)
    - “Let me think about it. I will be back shortly.” → [gylew_korhald_cop_45](#d-gylew_korhald_cop_45)

    <span id="d-gylew_korhald_cop_35"></span>**`gylew_korhald_cop_35`** Gylew: “Oh, you are so kind. I'll tell you what. Once you find your way to Feygard, seek out my family. They will help you make that shield a little bit better.” — **effects:** sets stage 105 of [The odd coin collector](../quests/odd_coin_collector.md#stage-105), clears stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47), sets stage 106 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-106)


    <span id="d-coin_collector_troll_coins_2"></span>**`coin_collector_troll_coins_2`** Gylew: “The coins hold a faint echo of the well's enchantment. Though their magic is subtle, they carry the essence of the well's power. As a token of my gratitude for bringing these to me, I offer you this rare artifact in exchange for three of…”

    - “Without knowing more about this "rare artifact", I'm afraid that I will have to pass on your offer.” → [coin_collector_troll_coins_3a](#d-coin_collector_troll_coins_3a)
    - “Umm, I guess I can trust you now.” *(if hand over 3× [Mysterious coin](../items/mysterious_coin.md))* → [coin_collector_troll_coins_3b](#d-coin_collector_troll_coins_3b)

    <span id="d-coin_collector_thief_coins_20"></span>**`coin_collector_thief_coins_20`** Gylew: “[The coin collector eagerly examines the pilfered coins, eyes gleaming with fascination.]...”

    - Next → [coin_collector_thief_coins_30](#d-coin_collector_thief_coins_30)

    <span id="d-gylew_korhald_30"></span>**`gylew_korhald_30`** Gylew: “[Gylew examines the chest] What?! There are two locks! How can this be? Do you know anything about a second key?” — **effects:** sets stage 105 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-105)

    - “Yes. In fact, I met a 'friend' of yours who told me all about it.” → [gylew_korhald_40](#d-gylew_korhald_40)

    <span id="d-gylew_korhald_27"></span>**`gylew_korhald_27`** Gylew: “There are two locks! How can this be? Do you know anything about a second key?”

    - “Yes. In fact, I met a 'friend' of yours who told me all about it.” → [gylew_korhald_40](#d-gylew_korhald_40)

    <span id="d-gylew_attack_2"></span>**`gylew_attack_2`** Gylew: “My trusty henchman will take care of you.” — **effects:** removes monsters from waterway5, spawns monsters on waterway5

    - “Oh, you need someone to help you?” → *fight starts*

    <span id="d-gylew2"></span>**`gylew2`** Gylew: “Great! Let me see.”

    - Next → [gylew3](#d-gylew3)

    <span id="d-gylew_korhald_cop_20"></span>**`gylew_korhald_cop_20`** Gylew: “Well, for starters, this shield has the Korhald family crest engraved on its front side and clearly belonged to Korhald himself, but I have no use for such an item. Here take it.”

    - Next → [gylew_korhald_cop_30](#d-gylew_korhald_cop_30)

    <span id="d-gylew_korhald_cop_50"></span>**`gylew_korhald_cop_50`** Gylew: “Excellent. Come see me if you ever find any more interesting coins.” — **effects:** gives [Gold coins](../items/gold.md), sets stage 100 of [The odd coin collector](../quests/odd_coin_collector.md#stage-100), clears stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47), sets stage 106 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-106)


    <span id="d-gylew_korhald_cop_45"></span>**`gylew_korhald_cop_45`** Gylew: “OK, but don't keep an old man waiting too long. I want that coin.” — **effects:** sets stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47)


    <span id="d-coin_collector_troll_coins_3a"></span>**`coin_collector_troll_coins_3a`** Gylew: “Well, if you change your mind, I will be here.”


    <span id="d-coin_collector_troll_coins_3b"></span>**`coin_collector_troll_coins_3b`** Gylew: “For your effort in retrieving these valuable coins, take this rare artifact. It is a relic from the same era as the coins, crafted with similar enchantments. It will serve you well in your journeys, offering protection and a touch of…” — **effects:** gives 1× [Circlet of clarity](../items/circlet_clarity.md)


    <span id="d-coin_collector_thief_coins_30"></span>**`coin_collector_thief_coins_30`** Gylew: “Ah, these coins tell a tale of clandestine dealings and shadowy alliances.”

    - Next → [coin_collector_thief_coins_35](#d-coin_collector_thief_coins_35)

    <span id="d-gylew_korhald_40"></span>**`gylew_korhald_40`** Gylew: “And whom may that be?”

    - “Your half-brother, Forenza. What a story he had to tell.” → [gylew_korhald_50](#d-gylew_korhald_50)

    <span id="d-gylew3"></span>**`gylew3`** Gylew: “I am a rare coin collector. Have you ever noticed how some of your gold is more unique or older looking than others?”

    - “Yes, I have.” → [gylew4](#d-gylew4)
    - “[Lie] Yes, yes I have.” → [gylew4](#d-gylew4)
    - “Honestly, I just use it to buy bonemeal.” *(if carry 20× [Bonemeal potion](../items/bonemeal_potion.md))* → [gylew4a](#d-gylew4a)
    - “No and I don't care.” → *conversation ends*

    <span id="d-gylew_korhald_cop_30"></span>**`gylew_korhald_cop_30`** Gylew: “But this coin you have here is a completely different story. I don't know anything about it. Which makes me want it even more. Can I have it? I will reward you handsomely for it.”

    - “Reward?! I always love the sound of that. What are we talking here? 10,000 gold? 20,000 gold?” → [gylew_korhald_cop_40](#d-gylew_korhald_cop_40)
    - “Here, take it. I have enough coins.” *(if hand over 1× [Coin of Prestige](../items/hero_coin.md))* → [gylew_korhald_cop_35](#d-gylew_korhald_cop_35)

    <span id="d-coin_collector_thief_coins_35"></span>**`coin_collector_thief_coins_35`** Gylew: “These bronze pieces bear the mark of the Lunar Whisper, an infamous thieves' guild that once ruled the underground markets. Legend has it, these coins were minted in secret, their alloy infused with fragments of moonstone to enhance the…”

    - Next → [coin_collector_thief_coins_40](#d-coin_collector_thief_coins_40)

    <span id="d-gylew_korhald_50"></span>**`gylew_korhald_50`** Gylew: “But I see that you did not listen to those 'stories' as you would not be here if you had. What did he tell you about the second key?”

    - “Well, for starters, he told me that he had it and he would not give it to me without a fight. Which of course, we did…” → [gylew_korhald_60](#d-gylew_korhald_60)

    <span id="d-gylew4"></span>**`gylew4`** Gylew: “Great. Please let me see...agh, interesting.”

    - “What? What do you see?” → [gylew5](#d-gylew5)

    <span id="d-gylew4a"></span>**`gylew4a`** Gylew: “You know that stuff is illegal and that you can get in serious trouble just for possessing it?”

    - “What can I say? I like to go rogue.” → *conversation ends*

    <span id="d-coin_collector_thief_coins_40"></span>**`coin_collector_thief_coins_40`** Gylew: “These silver coins hold the captivating history of a nomadic people, a seafaring tribe whose exploits were as boundless as the horizon. Born from the hands of skilled minters among the maritime wanderers, these coins tell the tale of the…”

    - Next → [coin_collector_thief_coins_45](#d-coin_collector_thief_coins_45)

    <span id="d-gylew_korhald_60"></span>**`gylew_korhald_60`** Gylew: “You killed my brother?”

    - “YES, and I loved doing so. Pathetic creature he was.” → [gylew_korhald_70](#d-gylew_korhald_70)
    - “I was forced to. He gave me no choice.” → [gylew_korhald_70](#d-gylew_korhald_70)
    - “[Lie] No, but I beat him up good and took his key.” → [gylew_korhald_70](#d-gylew_korhald_70)

    <span id="d-gylew5"></span>**`gylew5`** Gylew: “This one here was cut during the rise of Elythara and is quite rare and valuable. But this other one here is a more common coin as it was cut during Geomyr's rule. While this one here is from a far off land and is a part of a larger…”

    - “Oh, I see.” *(if reached stage 220 of [The silver scale](../quests/mermaid_scale.md#stage-220); have 5 gold; NOT reached stage 10 of [The odd coin collector](../quests/odd_coin_collector.md#stage-10); NOT reached stage 11 of [The odd coin collector](../quests/odd_coin_collector.md#stage-11))* → [gylew6](#d-gylew6)
    - “[While pointing at a few of the coins in Gylew's hand, you ask:] What about those?” *(if reached stage 250 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-250); NOT reached stage 12 of [The odd coin collector](../quests/odd_coin_collector.md#stage-12); have 10 gold; NOT reached stage 13 of [The odd coin collector](../quests/odd_coin_collector.md#stage-13))* → [gylew8](#d-gylew8)
    - “Yes, I know this already.” *(if reached stage 10 of [The odd coin collector](../quests/odd_coin_collector.md#stage-10))* → [gylew7](#d-gylew7)
    - “Yes, I know this already.” *(if reached stage 11 of [The odd coin collector](../quests/odd_coin_collector.md#stage-11))* → [gylew7](#d-gylew7)
    - “I am so not interested.” *(if NOT reached stage 220 of [The silver scale](../quests/mermaid_scale.md#stage-220))* → [gylew7](#d-gylew7)

    <span id="d-coin_collector_thief_coins_45"></span>**`coin_collector_thief_coins_45`** Gylew: “The silver pieces depict a mighty ship sailing under the moonlit sky, capturing the essence of the Ocean Nomads' freedom and unity. Legends speak of these coins being crafted during the tribe's grand gatherings, where sailors from various…”

    - “So they are priceless?” → [coin_collector_thief_coins_50](#d-coin_collector_thief_coins_50)

    <span id="d-gylew_korhald_70"></span>**`gylew_korhald_70`** Gylew: “I guess I should be saddened, but I am not. Can I have my brother's key now? I've waited a long time for these coins.”

    - “Of course.” *(if hand over 1× [Forenza's key](../items/forenza_key.md))* → [gylew_korhald_80](#d-gylew_korhald_80)

    <span id="d-gylew6"></span>**`gylew6`** Gylew: “Where did you get these coins?! [Gylew shows you a set of identical coins]”

    - “None of your business. Now get to the point.” → [gylew7](#d-gylew7)
    - “It was a gift from a friend. Can we get right to what you want?” → [gylew7](#d-gylew7)
    - “With all of my coins, do you actually think I can remember?” → [gylew7](#d-gylew7)
    - “It was a reward for helping a mermaid.” → [gylew7a](#d-gylew7a)

    <span id="d-gylew8"></span>**`gylew8`** Gylew: “Where did you get these coins?! [Gylew shows you a collection of identical coins]”

    - “I took them off of a dead guy.” → [gylew8a_1](#d-gylew8a_1)
    - “I got them from a friend” → [gylew8a_2](#d-gylew8a_2)
    - “That's none of your business.” → [gylew7](#d-gylew7)
    - “I don't know. After all, I have looted many a gold coin in my travels.” → [gylew8a_2](#d-gylew8a_2)

    <span id="d-gylew7"></span>**`gylew7`** Gylew: “OK, I will get back to my ask of you now.”

    - “Um, is this going to take long? I have to find my brother.” → [gylew9](#d-gylew9)
    - “Interesting, it really is, but I'm leaving.” → *conversation ends*
    - “Interesting. Please enlighten me some more.” → [gylew9](#d-gylew9)

    <span id="d-coin_collector_thief_coins_50"></span>**`coin_collector_thief_coins_50`** Gylew: “[The collector pauses, his gaze lingering on the coins.] These pieces are not merely currency; they are artifacts of a hidden past, a glimpse into the underground world where alliances were forged in secrecy. I'd be willing to make you an…”

    - “So you want to buy them all?” → [coin_collector_thief_coins_55](#d-coin_collector_thief_coins_55)

    <span id="d-gylew_korhald_80"></span>**`gylew_korhald_80`** Gylew: “Thank you! It is so nice to finally be this close to my life's dream.”

    - Next → [korhald_chest_examine_10_gylew](#d-korhald_chest_examine_10_gylew)

    <span id="d-gylew7a"></span>**`gylew7a`** Gylew: “What?! Seriously?”

    - “Yes.” → [gylew7a_1](#d-gylew7a_1)
    - “No.” → [gylew7](#d-gylew7)

    <span id="d-gylew8a_1"></span>**`gylew8a_1`** Gylew: “What?! You went digging through his corpse?”

    - “Don't judge me. I was desperate at the time.” → [gylew8a_2](#d-gylew8a_2)

    <span id="d-gylew8a_2"></span>**`gylew8a_2`** Gylew: “I must have them. All 10 of them!”

    - “OK. What do you have of value?” *(if pay 10 gold)* → [gylew8a_3](#d-gylew8a_3)
    - “Here, take it.” → [gylew8a_4](#d-gylew8a_4)
    - “Nope. You can not have them.” → [gylew7](#d-gylew7)

    <span id="d-gylew9"></span>**`gylew9`** Gylew: “You see, I was raised in Feygard by my father who was commissioned to create gold coins. All he ever talked about was coins and we shared this common love.”

    - Next → [gylew10](#d-gylew10)

    <span id="d-coin_collector_thief_coins_55"></span>**`coin_collector_thief_coins_55`** Gylew: “Well, yes. But not all of them. Afterall, who needs 110 of these?”

    - “OK, so what do you want to buy?” → [coin_collector_thief_coins_60](#d-coin_collector_thief_coins_60)

    <span id="d-korhald_chest_examine_10_gylew"></span>**`korhald_chest_examine_10_gylew`** [Dummy NPC](../monsters/none.md): “He opens the chest and begins to feverlessly sift through the coins, transferring each one to his bag. When to his surpirse, he finds something...”

    - Next → [korhald_chest_examine_20_gylew](#d-korhald_chest_examine_20_gylew)

    <span id="d-gylew7a_1"></span>**`gylew7a_1`** Gylew: “I must have one.”

    - “OK. What do you have of value?” *(if pay 5 gold)* → [gylew7a_2](#d-gylew7a_2)
    - “Here, take it.” *(if pay 5 gold)* → [gylew7a_3](#d-gylew7a_3)
    - “Nope, they are mine.” → [gylew7](#d-gylew7)

    <span id="d-gylew8a_3"></span>**`gylew8a_3`** Gylew: “Here is 550 gold” — **effects:** gives 550× [Gold coins](../items/gold.md), sets stage 12 of [The odd coin collector](../quests/odd_coin_collector.md#stage-12)

    - “Wow! I get 550 gold for the 10 I gave you?” → [gylew7](#d-gylew7)

    <span id="d-gylew8a_4"></span>**`gylew8a_4`** Gylew: “Much appreciated. Thank you.” — **effects:** sets stage 13 of [The odd coin collector](../quests/odd_coin_collector.md#stage-13), gives -10× [Gold coins](../items/gold.md), gives 1× [Feygard plated gloves](../items/feygard_plated_gloves.md)

    - Next → [gylew7](#d-gylew7)

    <span id="d-gylew10"></span>**`gylew10`** Gylew: “He once told me this story when I was very young about this magnificent coin collection called the 'Korhald coins'. So from a very young age I was fascinated.”

    - “You mentioned 'Korhald coins'. Who or what is 'Korhald'?” → [gylew10_1](#d-gylew10_1)

    <span id="d-coin_collector_thief_coins_60"></span>**`coin_collector_thief_coins_60`** Gylew: “Well, let's talk price first. You see, the silver coin is worth 11 gold in weight and the bronze is worth 5 gold in weight. But, to a collector they are worth more. Let's make this simple. I will pay you double those values for each coin…”

    - “So how much total than?” → [coin_collector_thief_coins_65](#d-coin_collector_thief_coins_65)

    <span id="d-korhald_chest_examine_20_gylew"></span>**`korhald_chest_examine_20_gylew`** [Gylew](../monsters/gylew.md): “Look at what I found at the bottom of the chest. A pendant and a map. [Shows item to you]”

    - “A map? Really? Where does it point to?” → [korhald_chest_examine_30](#d-korhald_chest_examine_30)

    <span id="d-gylew7a_2"></span>**`gylew7a_2`** Gylew: “Here is 500 gold.” — **effects:** gives 500× [Gold coins](../items/gold.md), sets stage 10 of [The odd coin collector](../quests/odd_coin_collector.md#stage-10)

    - “Now that's funny. A coin collector traded me his gold coins for my coins.” *(if reached stage 250 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-250); NOT reached stage 12 of [The odd coin collector](../quests/odd_coin_collector.md#stage-12); have 10 gold; NOT reached stage 13 of [The odd coin collector](../quests/odd_coin_collector.md#stage-13))* → [gylew8](#d-gylew8)
    - “Now that's funny. A coin collector traded me his gold coins for my coins.” *(if NOT reached stage 250 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-250))* → [gylew7](#d-gylew7)

    <span id="d-gylew7a_3"></span>**`gylew7a_3`** Gylew: “That was foolish of you. This is very valuable and you just gave it to me.” — **effects:** sets stage 11 of [The odd coin collector](../quests/odd_coin_collector.md#stage-11)

    - “Well, what can I say? You caught me me wanting to be charitable.” *(if reached stage 250 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-250); NOT reached stage 12 of [The odd coin collector](../quests/odd_coin_collector.md#stage-12); have 10 gold; NOT reached stage 13 of [The odd coin collector](../quests/odd_coin_collector.md#stage-13))* → [gylew8](#d-gylew8)
    - “Well, I just gave it to you because I was hoping for something special in return.” *(if NOT reached stage 250 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-250))* → [gylew7](#d-gylew7)

    <span id="d-gylew10_1"></span>**`gylew10_1`** Gylew: “You never heard of Korhald? He was the founder of Remgard. Anyways, back to my story...”

    - Next → [gylew10_2](#d-gylew10_2)

    <span id="d-coin_collector_thief_coins_65"></span>**`coin_collector_thief_coins_65`** Gylew: “110 gold for the silver and 50 for the bronze coins.”

    - “That little? No, thanks” → *conversation ends*
    - “Well, something is better than nothing.” *(if hand over 5× [Silver coin](../items/silver_coin.md); hand over 5× [Bronze coin](../items/bronze_coin.md))* → [coin_collector_thief_coins_70](#d-coin_collector_thief_coins_70)

    <span id="d-korhald_chest_examine_30"></span>**`korhald_chest_examine_30`** Gylew: “Well, that is really hard to say. You see [he shows you the map], it is really old and a lot of the landmarks no longer exist in Dhayavar.”

    - “Yeah, I can see what you mean.” → [korhald_chest_examine_40](#d-korhald_chest_examine_40)

    <span id="d-gylew10_2"></span>**`gylew10_2`** Gylew: “My father never mentioned the exact location to me, but from my efforts, I've ascertained a location near Remgard.”

    - “Remgard? Where's that?” *(if NOT reached stage 170 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-170))* → [gylew10_2_1](#d-gylew10_2_1)
    - “Great, I see where this is going. I need to go back to Remgard.” *(if reached stage 170 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-170))* → [gylew11](#d-gylew11)

    <span id="d-coin_collector_thief_coins_70"></span>**`coin_collector_thief_coins_70`** Gylew: “Thank you so much.” — **effects:** gives 160× [Gold coins](../items/gold.md), sets stage 107 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-107)


    <span id="d-korhald_chest_examine_40"></span>**`korhald_chest_examine_40`** Gylew: “But not all hope is lost. You see this map shows the great river that is just right over there [points northeast] behind those trees. Anyone who follows the map going east, should have no problem reaching wherever this map is leading to.”

    - Next → [korhald_chest_examine_50](#d-korhald_chest_examine_50)

    <span id="d-gylew10_2_1"></span>**`gylew10_2_1`** Gylew: “It is far east of here near a place called Laeroth Manor.”

    - Next → [gylew12](#d-gylew12)

    <span id="d-gylew11"></span>**`gylew11`** Gylew: “Yes, a place called Laeroth Manor.”

    - Next → [gylew12](#d-gylew12)

    <span id="d-korhald_chest_examine_50"></span>**`korhald_chest_examine_50`** Gylew: “Here, take the map and the pendant. If you need me, I'll be here for a little bit longer.” — **effects:** gives 1× [Mysterious Korhald map](../items/korhald_map.md), sets stage 60 of [The odd coin collector](../quests/odd_coin_collector.md#stage-60), gives 1× [Mysterious Korhald pendant](../items/korhald_chamber_key.md), sets stage 44 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-44), sets stage 45 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-45), sets stage 48 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-48)


    <span id="d-gylew12"></span>**`gylew12`** Gylew: “We have failed to retrieve it as the monsters are too strong. That's where you come in. What do you say? Will you help me?”

    - “Yes, of course, you need my help.” → [gylew13](#d-gylew13)
    - “Pathetic creatures you two are. Needing the help of a child. I will do it.” → [gylew13](#d-gylew13)
    - “Depends. What is the reward?” → [gylew14](#d-gylew14)
    - “No” → *conversation ends*

    <span id="d-gylew13"></span>**`gylew13`** Gylew: “Then please head to the east and return to me when you find the Korhald coins.” — **effects:** sets stage 20 of [The odd coin collector](../quests/odd_coin_collector.md#stage-20)


    <span id="d-gylew14"></span>**`gylew14`** Gylew: “We will discuss this after you have completed the job. But remember, I am from Feygard and can reward you handsomly.”

    - “Sounds good.” → [gylew13](#d-gylew13)
    - “OK, but I have high expectations. Please be prepared to pay up.” → [gylew13](#d-gylew13)



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gylew.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gylew.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gylew.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gylew.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `gylew` · Data from v0.8.18</small>
