# ![](../assets/icons/monsters/monsters_tometik1_86.png){ .sprite } Forenza

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

- [waytobrimhaven3](../maps/waytobrimhaven3.md)

## Quests

- [The odd coin collector](../quests/odd_coin_collector.md): stages 60, 110, 115
- [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md): stages 44, 45, 47, 48
- [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md): stages 255
- [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md): stages 106, 107, 108

??? quote "Dialogue (36 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-forenza_waytobrimhaven3_initial_phrase"></span>**`forenza_waytobrimhaven3_initial_phrase`** Forenza: “Hey, kid, nice to see you again.”

    - “It's nice to see you too. Can we talk about the Korhald coins?” *(if latest stage of [The odd coin collector](../quests/odd_coin_collector.md#stage-63) is 63; NOT reached stage 60 of [The odd coin collector](../quests/odd_coin_collector.md#stage-60))* → [forenza_brimhaven_5](#d-forenza_brimhaven_5)
    - “Hey. I found the Korhald tomb and it had two items that I think might interest you.” *(if latest stage of [The odd coin collector](../quests/odd_coin_collector.md#stage-65) is 65; carry 1× [Shield of the Brave](../items/shield_of_brave.md); carry 1× [Coin of Prestige](../items/hero_coin.md))* → [forenza_korhald_cop_0](#d-forenza_korhald_cop_0)
    - “Hey. I found the Korhald tomb and it had two items that I think might interest you.” *(if latest stage of [The odd coin collector](../quests/odd_coin_collector.md#stage-65) is 65; wearing [Shield of the Brave](../items/shield_of_brave.md); carry 1× [Coin of Prestige](../items/hero_coin.md))* → [forenza_korhald_cop_0](#d-forenza_korhald_cop_0)
    - “Inside the Korhald tomb, I found a locked chest. Do you know where I can find its key?” *(if reached stage 65 of [The odd coin collector](../quests/odd_coin_collector.md#stage-65); reached stage 50 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-50))* → [odd_coin_collector_ask_about_locked_chest](#d-odd_coin_collector_ask_about_locked_chest)
    - “I tried to get Gylew's key, but...” *(if latest stage of [The odd coin collector](../quests/odd_coin_collector.md#stage-62) is 62)* → [forenza_korhald_gylew_not_dead](#d-forenza_korhald_gylew_not_dead)
    - “I have not gone back to see Gylew since our last encounter. Why am I wasting time talking to you when the job is not…” *(if latest stage of [The odd coin collector](../quests/odd_coin_collector.md#stage-50) is 50)* → *conversation ends*
    - “Hey. I need to go now and follow this map.” *(if latest stage of [The odd coin collector](../quests/odd_coin_collector.md#stage-60) is 60)* → *conversation ends*
    - “I found these glowing coins in a pit beneath the well in Wexlow Village. They seem magical.” *(if reached stage 110 of [The odd coin collector](../quests/odd_coin_collector.md#stage-110); carry 3× [Mysterious coin](../items/mysterious_coin.md))* → [coin_collector_troll_coins](#d-coin_collector_troll_coins)
    - “I visited your daughter Florencia in Brightport. She wishes you would come home more often.” *(if reached stage 254 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-254); NOT reached stage 255 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-255))* → [brightport_forenza](#d-brightport_forenza)
    - “We have no more business to discuss. I'll see you later.” *(if reached stage 110 of [The odd coin collector](../quests/odd_coin_collector.md#stage-110))* → *conversation ends*
    - “I found these glowing coins in a pit beneath the well in Wexlow Village. They seem magical.” *(if reached stage 115 of [The odd coin collector](../quests/odd_coin_collector.md#stage-115); carry 3× [Mysterious coin](../items/mysterious_coin.md))* → [coin_collector_troll_coins](#d-coin_collector_troll_coins)
    - “I hope that these coins will enable you to make peace with your father. Take care.” *(if reached stage 115 of [The odd coin collector](../quests/odd_coin_collector.md#stage-115))* → *conversation ends*
    - “[Lie] I have these bronze and silver coins that I "acquired" in a game of chance. I would like to know if you are…” *(if reached stage 106 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-106); reached stage 80 of [Wanted men](../quests/wanted_men.md#stage-80); carry 60× [Silver coin](../items/silver_coin.md); carry 50× [Bronze coin](../items/bronze_coin.md); NOT reached stage 107 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-107))* → [coin_collector_thief_coins_10](#d-coin_collector_thief_coins_10)

    <span id="d-forenza_brimhaven_5"></span>**`forenza_brimhaven_5`** Forenza: “Do you have Gylew's key?”

    - “Yes, and I also have the chest. Here, take them. [You give both items to Forenza]” *(if hand over 1× [Gylew's key](../items/gylew_key.md); hand over 1× [Korhald coin chest](../items/korhald_coins.md))* → [forenza_brimhaven_10](#d-forenza_brimhaven_10)
    - “Yes, but I don't have the chest.” *(if carry 1× [Gylew's key](../items/gylew_key.md); NOT carry 1× [Korhald coin chest](../items/korhald_coins.md))* → [forenza_brimhaven_15](#d-forenza_brimhaven_15)
    - “What are you talking about? I already gave it to you along with the chest I found on the island.” *(if reached stage 108 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-108); NOT reached stage 60 of [The odd coin collector](../quests/odd_coin_collector.md#stage-60))* → [forenza_brimhaven_11](#d-forenza_brimhaven_11)
    - “No” *(if NOT carry 1× [Gylew's key](../items/gylew_key.md))* → [forenza_brimhaven_15](#d-forenza_brimhaven_15)

    <span id="d-forenza_korhald_cop_0"></span>**`forenza_korhald_cop_0`** Forenza: “Oh, really?! Let me see them and we can talk more.”

    - “[You show Forenza the Coin of Prestige and the Shield of the brave]” → [forenza_korhald_cop_10](#d-forenza_korhald_cop_10)

    <span id="d-odd_coin_collector_ask_about_locked_chest"></span>**`odd_coin_collector_ask_about_locked_chest`** Forenza: “A locked chest you say? Well, I'm not really sure, but logic tells me to look back in the Laeroth Manor.”

    - “Oh, yeah. That makes sense.” → *conversation ends*
    - “Oh, come on! I don't want to go back there again.” → *conversation ends*

    <span id="d-forenza_korhald_gylew_not_dead"></span>**`forenza_korhald_gylew_not_dead`** Forenza: “You wimp! Get me my brother's key now.”


    <span id="d-coin_collector_troll_coins"></span>**`coin_collector_troll_coins`** Forenza: “Ah, these are Enchanted Coins, crafted by ancient wizards who once drew magic from the well's waters. The runes on these coins change patterns, a sign of their magical origin. Such artifacts are rare indeed.”

    - “What can you tell me about their enchantment?” → [coin_collector_troll_coins_2](#d-coin_collector_troll_coins_2)
    - “Boring.” → *conversation ends*

    <span id="d-brightport_forenza"></span>**`brightport_forenza`** Forenza: “Yes... maybe I should do that sometime. Take care, $playername.” — **effects:** sets stage 255 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-255)


    <span id="d-coin_collector_thief_coins_10"></span>**`coin_collector_thief_coins_10`** Forenza: “Sure. Let's see what you have.”

    - “[Show the coins]” → [coin_collector_thief_coins_20](#d-coin_collector_thief_coins_20)

    <span id="d-forenza_brimhaven_10"></span>**`forenza_brimhaven_10`** [Dummy NPC](../monsters/none.md): “With an ever growing smile upon his face, Forenza inserts the first key and then the second. He then proceeds to slowly open the chest.” — **effects:** sets stage 108 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-108)

    - Next → [korhald_chest_examine_10](#d-korhald_chest_examine_10)

    <span id="d-forenza_brimhaven_15"></span>**`forenza_brimhaven_15`** Forenza: “Well, go get it and bring me back both the key and the chest.”

    - “Yes sir!” → *conversation ends*

    <span id="d-forenza_brimhaven_11"></span>**`forenza_brimhaven_11`** Forenza: “Oh, yeah. Let's look in that chest now.”

    - Next → [korhald_chest_examine_10](#d-korhald_chest_examine_10)

    <span id="d-forenza_korhald_cop_10"></span>**`forenza_korhald_cop_10`** Forenza: “Hmm...these are indeed interesting. Very interesting in fact.”

    - “[While trying to hold back the giant smile that you can feel growing upon your face, you ask:] 'Why is that'?” → [forenza_korhald_cop_20](#d-forenza_korhald_cop_20)

    <span id="d-coin_collector_troll_coins_2"></span>**`coin_collector_troll_coins_2`** Forenza: “The coins hold a faint echo of the well's enchantment. Though their magic is subtle, they carry the essence of the well's power. As a token of my gratitude for bringing these to me, I offer you this rare artifact in exchange for three of…”

    - “Without knowing more about this "rare artifact", I'm afraid that I will have to pass on your offer.” → [coin_collector_troll_coins_3a](#d-coin_collector_troll_coins_3a)
    - “Umm, I guess I can trust you now.” *(if hand over 3× [Mysterious coin](../items/mysterious_coin.md))* → [coin_collector_troll_coins_3b](#d-coin_collector_troll_coins_3b)

    <span id="d-coin_collector_thief_coins_20"></span>**`coin_collector_thief_coins_20`** Forenza: “[The coin collector eagerly examines the pilfered coins, eyes gleaming with fascination.]...”

    - Next → [coin_collector_thief_coins_30](#d-coin_collector_thief_coins_30)

    <span id="d-korhald_chest_examine_10"></span>**`korhald_chest_examine_10`** Forenza: “He then begins to feverlessly sift through the coins, transferring each one to his bag. When to his surpirse, he finds something...”

    - Next → [korhald_chest_examine_20](#d-korhald_chest_examine_20)

    <span id="d-forenza_korhald_cop_20"></span>**`forenza_korhald_cop_20`** Forenza: “Well, for obvious reasons. Didn't you notice that the shield has the Korhald family crest engraved on its front side? This clearly belonged to Korhald himself. You should keep this item as it could aid you in your adventures.”

    - Next → [forenza_korhald_cop_30](#d-forenza_korhald_cop_30)

    <span id="d-coin_collector_troll_coins_3a"></span>**`coin_collector_troll_coins_3a`** Forenza: “Well, if you change your mind, I will be here.”


    <span id="d-coin_collector_troll_coins_3b"></span>**`coin_collector_troll_coins_3b`** Forenza: “For your effort in retrieving these valuable coins, take this rare artifact. It is a relic from the same era as the coins, crafted with similar enchantments. It will serve you well in your journeys, offering protection and a touch of…” — **effects:** gives 1× [Circlet of clarity](../items/circlet_clarity.md)


    <span id="d-coin_collector_thief_coins_30"></span>**`coin_collector_thief_coins_30`** Forenza: “Ah, these coins tell a tale of clandestine dealings and shadowy alliances.”

    - Next → [coin_collector_thief_coins_35](#d-coin_collector_thief_coins_35)

    <span id="d-korhald_chest_examine_20"></span>**`korhald_chest_examine_20`** [Forenza](../monsters/forenza_waytobrimhaven3.md): “Look at what I found at the bottom of the chest. A pendant and a map. [Shows item to you]”

    - “A map? Really? Where does it point to?” → [korhald_chest_examine_30](#d-korhald_chest_examine_30)

    <span id="d-forenza_korhald_cop_30"></span>**`forenza_korhald_cop_30`** Forenza: “But this coin you have here really gives my pause, as I never believed the stories about its existence were true. I don't know much about it, but I do know that it has great value. Can I have it? I will reward you for it of course.”

    - “Reward?! I always love the sound of that. What are we talking here? 10,000 gold? 20,000 gold?” → [forenza_korhald_cop_40](#d-forenza_korhald_cop_40)
    - “Here, take it. I have enough coins.” *(if hand over 1× [Coin of Prestige](../items/hero_coin.md))* → [forenza_korhald_cop_35](#d-forenza_korhald_cop_35)

    <span id="d-coin_collector_thief_coins_35"></span>**`coin_collector_thief_coins_35`** Forenza: “These bronze pieces bear the mark of the Lunar Whisper, an infamous thieves' guild that once ruled the underground markets. Legend has it, these coins were minted in secret, their alloy infused with fragments of moonstone to enhance the…”

    - Next → [coin_collector_thief_coins_40](#d-coin_collector_thief_coins_40)

    <span id="d-korhald_chest_examine_30"></span>**`korhald_chest_examine_30`** Forenza: “Well, that is really hard to say. You see [he shows you the map], it is really old and a lot of the landmarks no longer exist in Dhayavar.”

    - “Yeah, I can see what you mean.” → [korhald_chest_examine_40](#d-korhald_chest_examine_40)

    <span id="d-forenza_korhald_cop_40"></span>**`forenza_korhald_cop_40`** Forenza: “[While laughing] Now, now, who do you think I am, Gylew? I don't have that kind of gold. How about 7,000 gold?”

    - “Sounds like a great deal. I'll take it.” *(if hand over 1× [Coin of Prestige](../items/hero_coin.md))* → [forenza_korhald_cop_50](#d-forenza_korhald_cop_50)
    - “Let me think about it. I will be back shortly.” → [forenza_korhald_41](#d-forenza_korhald_41)

    <span id="d-forenza_korhald_cop_35"></span>**`forenza_korhald_cop_35`** Forenza: “Oh, how very generous of you to just hand it over for free. I'll tell you what, once you find your way to Brightport, seek out my family. They will reward you for all of your generosity and hard work.” — **effects:** sets stage 115 of [The odd coin collector](../quests/odd_coin_collector.md#stage-115), clears stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47), sets stage 106 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-106)


    <span id="d-coin_collector_thief_coins_40"></span>**`coin_collector_thief_coins_40`** Forenza: “These silver coins hold the captivating history of a nomadic people, a seafaring tribe whose exploits were as boundless as the horizon. Born from the hands of skilled minters among the maritime wanderers, these coins tell the tale of the…”

    - Next → [coin_collector_thief_coins_45](#d-coin_collector_thief_coins_45)

    <span id="d-korhald_chest_examine_40"></span>**`korhald_chest_examine_40`** Forenza: “But not all hope is lost. You see this map shows the great river that is just right over there [points northeast] behind those trees. Anyone who follows the map going east, should have no problem reaching wherever this map is leading to.”

    - Next → [korhald_chest_examine_50](#d-korhald_chest_examine_50)

    <span id="d-forenza_korhald_cop_50"></span>**`forenza_korhald_cop_50`** Forenza: “Excellent. Come see me if you ever find any more interesting coins.” — **effects:** gives [Gold coins](../items/gold.md), sets stage 110 of [The odd coin collector](../quests/odd_coin_collector.md#stage-110), clears stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47), sets stage 106 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-106)


    <span id="d-forenza_korhald_41"></span>**`forenza_korhald_41`** Forenza: “OK, but don't keep this coin collector waiting too long. I want that coin.” — **effects:** sets stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47)


    <span id="d-coin_collector_thief_coins_45"></span>**`coin_collector_thief_coins_45`** Forenza: “The silver pieces depict a mighty ship sailing under the moonlit sky, capturing the essence of the Ocean Nomads' freedom and unity. Legends speak of these coins being crafted during the tribe's grand gatherings, where sailors from various…”

    - “So they are priceless?” → [coin_collector_thief_coins_50](#d-coin_collector_thief_coins_50)

    <span id="d-korhald_chest_examine_50"></span>**`korhald_chest_examine_50`** Forenza: “Here, take the map and the pendant. If you need me, I'll be here for a little bit longer.” — **effects:** gives 1× [Mysterious Korhald map](../items/korhald_map.md), sets stage 60 of [The odd coin collector](../quests/odd_coin_collector.md#stage-60), gives 1× [Mysterious Korhald pendant](../items/korhald_chamber_key.md), sets stage 44 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-44), sets stage 45 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-45), sets stage 48 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-48)


    <span id="d-coin_collector_thief_coins_50"></span>**`coin_collector_thief_coins_50`** Forenza: “[The collector pauses, his gaze lingering on the coins.] These pieces are not merely currency; they are artifacts of a hidden past, a glimpse into the underground world where alliances were forged in secrecy. I'd be willing to make you an…”

    - “So you want to buy them all?” → [coin_collector_thief_coins_55](#d-coin_collector_thief_coins_55)

    <span id="d-coin_collector_thief_coins_55"></span>**`coin_collector_thief_coins_55`** Forenza: “Well, yes. But not all of them. Afterall, who needs 110 of these?”

    - “OK, so what do you want to buy?” → [coin_collector_thief_coins_60](#d-coin_collector_thief_coins_60)

    <span id="d-coin_collector_thief_coins_60"></span>**`coin_collector_thief_coins_60`** Forenza: “Well, let's talk price first. You see, the silver coin is worth 11 gold in weight and the bronze is worth 5 gold in weight. But, to a collector they are worth more. Let's make this simple. I will pay you double those values for each coin…”

    - “So how much total than?” → [coin_collector_thief_coins_65](#d-coin_collector_thief_coins_65)

    <span id="d-coin_collector_thief_coins_65"></span>**`coin_collector_thief_coins_65`** Forenza: “110 gold for the silver and 50 for the bronze coins.”

    - “That little? No, thanks” → *conversation ends*
    - “Well, something is better than nothing.” *(if hand over 5× [Silver coin](../items/silver_coin.md); hand over 5× [Bronze coin](../items/bronze_coin.md))* → [coin_collector_thief_coins_70](#d-coin_collector_thief_coins_70)

    <span id="d-coin_collector_thief_coins_70"></span>**`coin_collector_thief_coins_70`** Forenza: “Thank you so much.” — **effects:** gives 160× [Gold coins](../items/gold.md), sets stage 107 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-107)




## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 31 lines added |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 4 lines added, 4 lines changed<br>· text: “[The collector pauses, his gaze lingering on the coins.] These pieces…” → “[The collector pauses, his gaze lingering on the coins.] These pieces…”<br>· text: “Well, for obvious reasons. Didn't you notice that the shield has the …” → “Well, for obvious reasons. Didn't you notice that the shield has the …” |
| [v0.8.13](../versions/0.8.13.md) | Dialogue: 1 line changed<br>· text: “These bronze pieces bear the mark of the Lunar Whispe, an infamous th…” → “These bronze pieces bear the mark of the Lunar Whisper, an infamous t…” |
| [v0.8.16.1](../versions/0.8.16.1.md) | Dialogue: 1 line added, 1 line changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 4 lines changed<br>· text: “[While laughing] Now, now, who do you think I am, Gylew? I don't have…” → “[While laughing] Now, now, who do you think I am, Gylew? I don't have…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forenza_waytobrimhaven3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forenza_waytobrimhaven3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forenza_waytobrimhaven3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forenza_waytobrimhaven3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `forenza_waytobrimhaven3` · Data from v0.8.18</small>
