# ![](../assets/icons/monsters/monsters_men_7.png){ .sprite } Kaori

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

- [vilegard_kaori](../maps/vilegard_kaori.md)

## Quests

- [Kaori's errands](../quests/kaori.md): stages 10, 20
- [Trusting an outsider](../quests/vilegard.md): stages 10

??? quote "Dialogue (21 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-kaori_start"></span>**`kaori_start`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 20 of [Kaori's errands](../quests/kaori.md#stage-20))* → [kaori_default_1](#d-kaori_default_1)
    - branch 2 *(if reached stage 10 of [Kaori's errands](../quests/kaori.md#stage-10))* → [kaori_return_1](#d-kaori_return_1)
    - branch 3 → [kaori_1](#d-kaori_1)

    <span id="d-kaori_default_1"></span>**`kaori_default_1`** Kaori: “Was there something you wanted to talk about?”

    - “What can you tell me about Vilegard?” → [kaori_vilegard_1](#d-kaori_vilegard_1)
    - “Why is everyone in Vilegard so afraid of outsiders?” → [kaori_vilegard_2](#d-kaori_vilegard_2)

    <span id="d-kaori_return_1"></span>**`kaori_return_1`** Kaori: “Hello again. Have you found those 10 bonemeal potions I asked for?”

    - “No, I am still looking for them.” → [kaori_14](#d-kaori_14)
    - “Yes, I brought your potions.” *(if hand over 10× [Bonemeal potion](../items/bonemeal_potion.md))* → [kaori_20](#d-kaori_20)
    - “No. If they are banned, there is most likely a good reason behind it. You shouldn't use them.” → [kaori_15](#d-kaori_15)

    <span id="d-kaori_1"></span>**`kaori_1`** Kaori: “You are not welcome here. Please leave now.”

    - “Why is everyone in Vilegard so afraid of outsiders?” → [kaori_2](#d-kaori_2)
    - “Jolnor asked me to talk to you.” *(if reached stage 5 of [Kaori's errands](../quests/kaori.md#stage-5))* → [kaori_3](#d-kaori_3)

    <span id="d-kaori_vilegard_1"></span>**`kaori_vilegard_1`** Kaori: “You should go talk to Erttu if you want the background story about Vilegard. She has been around here far longer than me.”

    - “OK, I will do that.” → [kaori_default_1](#d-kaori_default_1)

    <span id="d-kaori_vilegard_2"></span>**`kaori_vilegard_2`** Kaori: “We have a history of people coming here and causing mischief. Over time, we have learned that keeping to ourselves works best.”

    - “That sounds like a good idea.” → [kaori_vilegard_3](#d-kaori_vilegard_3)
    - “That sounds wrong.” → [kaori_vilegard_3](#d-kaori_vilegard_3)

    <span id="d-kaori_14"></span>**`kaori_14`** Kaori: “Well, hurry up. I really need them soon.”


    <span id="d-kaori_20"></span>**`kaori_20`** Kaori: “Good. Give them to me.” — **effects:** sets stage 20 of [Kaori's errands](../quests/kaori.md#stage-20)

    - Next → [kaori_21](#d-kaori_21)

    <span id="d-kaori_15"></span>**`kaori_15`** Kaori: “Fine. Now please leave me.”


    <span id="d-kaori_2"></span>**`kaori_2`** Kaori: “I don't want to talk to you. Go talk to Jolnor in the chapel if you want to help us.” — **effects:** sets stage 10 of [Trusting an outsider](../quests/vilegard.md#stage-10)

    - “OK, bye.” → *conversation ends*
    - “Fine. Don't tell me.” → *conversation ends*

    <span id="d-kaori_3"></span>**`kaori_3`** Kaori: “He did? I guess you are not as bad as I first thought.”

    - Next → [kaori_4](#d-kaori_4)

    <span id="d-kaori_vilegard_3"></span>**`kaori_vilegard_3`** Kaori: “Anyway, that's why we are so suspicious of outsiders.”

    - “I see.” → [kaori_default_1](#d-kaori_default_1)

    <span id="d-kaori_21"></span>**`kaori_21`** Kaori: “Yes, these will do fine. Thank you a lot kid. Maybe you are OK after all. May the Shadow watch over you.”

    - Next → [kaori_default_1](#d-kaori_default_1)

    <span id="d-kaori_4"></span>**`kaori_4`** Kaori: “I am still not convinced that you are not a spy from Feygard sent to cause mischief.”

    - “What can you tell me about Vilegard?” → [kaori_trust_1](#d-kaori_trust_1)
    - “I can assure you that I am not a spy.” → [kaori_5](#d-kaori_5)
    - “Feygard, where or what is that?” → [kaori_trust_1](#d-kaori_trust_1)

    <span id="d-kaori_trust_1"></span>**`kaori_trust_1`** Kaori: “I still don't fully trust you enough to talk about that.”

    - “Is there anything I can do to gain your trust?” → [kaori_10](#d-kaori_10)
    - “[Bribe] How would 100 gold sound? Could that help you to trust me?” → [kaori_bribe](#d-kaori_bribe)

    <span id="d-kaori_5"></span>**`kaori_5`** Kaori: “Hmm. Maybe not. But then again, maybe you are. I am still not sure.”

    - “Is there anything I can do to gain your trust?” → [kaori_10](#d-kaori_10)
    - “[Bribe] How would 100 gold sound? Could that help you to trust me?” → [kaori_bribe](#d-kaori_bribe)

    <span id="d-kaori_10"></span>**`kaori_10`** Kaori: “If you really want to prove to me that you are not a spy from Feygard, there actually is something that you can do for me.”

    - Next → [kaori_11](#d-kaori_11)

    <span id="d-kaori_bribe"></span>**`kaori_bribe`** Kaori: “Are you trying to bribe me, kid? That won't work on me. What use would I have for gold if you actually were a spy?”

    - “Is there anything I can do to gain your trust?” → [kaori_10](#d-kaori_10)

    <span id="d-kaori_11"></span>**`kaori_11`** Kaori: “Up until recently, we have been using special potions made of ground bones for healing. These were very potent healing potions, and were used for several purposes.”

    - Next → [kaori_12](#d-kaori_12)

    <span id="d-kaori_12"></span>**`kaori_12`** Kaori: “But now, they have been banned by Lord Geomyr, and most use of them has stopped.”

    - Next → [kaori_13](#d-kaori_13)

    <span id="d-kaori_13"></span>**`kaori_13`** Kaori: “I would really like to have a few more of those. If you can bring me 10 bonemeal potions, I might consider trusting you a bit more.” — **effects:** sets stage 10 of [Kaori's errands](../quests/kaori.md#stage-10)

    - “OK. I will get some potions for you.” → [kaori_14](#d-kaori_14)
    - “No. If they are banned, there is most likely a good reason behind it. You shouldn't use them.” → [kaori_15](#d-kaori_15)
    - “I already have some of those potions with me that you can have.” *(if hand over 10× [Bonemeal potion](../items/bonemeal_potion.md))* → [kaori_20](#d-kaori_20)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 10 lines changed<br>· text: “Up until recently, we have been using special potions made of ground …” → “Up until recently, we have been using special potions made of ground …”<br>· text: “Hello again. Have you found those 10 Bonemeal potions I asked for?” → “Hello again. Have you found those 10 bonemeal potions I asked for?” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kaori.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kaori.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kaori.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kaori.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `kaori` · Data from v0.8.18</small>
