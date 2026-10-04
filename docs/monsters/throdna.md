# ![](../assets/icons/monsters/monsters_men2_4.png){ .sprite } Throdna

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

- [blackwater_mountain50](../maps/blackwater_mountain50.md)

## Quests

- [Darkness in the Daylight](../quests/darkness_in_daylight.md): stages 100, 110
- [Lights in the dark](../quests/kazaul.md): stages 8, 9, 10, 11, 30, 40, 41, 100

??? quote "Dialogue (71 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-throdna_start"></span>**`throdna_start`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 90 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-90); NOT reached stage 100 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-100))* → [dds_throdna_10](#d-dds_throdna_10)
    - branch 2 *(if reached stage 100 of [Lights in the dark](../quests/kazaul.md#stage-100))* → [throdna_purify_4](#d-throdna_purify_4)
    - branch 3 *(if reached stage 41 of [Lights in the dark](../quests/kazaul.md#stage-41))* → [throdna_purify_1](#d-throdna_purify_1)
    - branch 4 *(if reached stage 30 of [Lights in the dark](../quests/kazaul.md#stage-30))* → [throdna_return_3](#d-throdna_return_3)
    - branch 5 *(if reached stage 10 of [Lights in the dark](../quests/kazaul.md#stage-10))* → [throdna_return_1](#d-throdna_return_1)
    - branch 6 → [throdna_1](#d-throdna_1)

    <span id="d-dds_throdna_10"></span>**`dds_throdna_10`** Throdna: “You keep on disturbing us?”

    - “How did you manage to lose this? [Gives Throdna the second piece of the Kazaul ritual]” → [dds_throdna_20](#d-dds_throdna_20)

    <span id="d-throdna_purify_4"></span>**`throdna_purify_4`** Throdna: “You should get out of here to allow us to concentrate on our work.”

    - Next → [throdna_purify_5](#d-throdna_purify_5)

    <span id="d-throdna_purify_1"></span>**`throdna_purify_1`** Throdna: “Hello again. I hope you are here to tell me you have purified the shrine of Kazaul?”

    - “Yes, it is done.” *(if reached stage 60 of [Lights in the dark](../quests/kazaul.md#stage-60))* → [throdna_purify_3](#d-throdna_purify_3)
    - “No, not yet.” → [throdna_purify_2](#d-throdna_purify_2)
    - “What was I supposed to do again?” → [throdna_return_8](#d-throdna_return_8)

    <span id="d-throdna_return_3"></span>**`throdna_return_3`** Throdna: “You actually found all five pieces? I suppose I should thank you. Well then. Thank you.” — **effects:** sets stage 30 of [Lights in the dark](../quests/kazaul.md#stage-30)

    - Next → [throdna_return_4](#d-throdna_return_4)

    <span id="d-throdna_return_1"></span>**`throdna_return_1`** Throdna: “Hello again. I hope you come here to tell me you have the five parts of the ritual.”

    - “I am still looking for them.” → [throdna_return_2](#d-throdna_return_2)
    - “How many parts was I supposed to find?” → [throdna_15](#d-throdna_15)
    - “What was I supposed to do again?” → [throdna_12](#d-throdna_12)
    - “Yes, I think I have found them all.” *(if reached stage 21 of [Lights in the dark](../quests/kazaul.md#stage-21))* → [throdna_check_1](#d-throdna_check_1)

    <span id="d-throdna_1"></span>**`throdna_1`** Throdna: “Kazaul ... Shadow ... what was it again?”

    - Next → [throdna_2](#d-throdna_2)

    <span id="d-dds_throdna_20"></span>**`dds_throdna_20`** Throdna: “Why did you steal this? You must be part of that terrible cult of the Kazaul.”

    - Next → [dds_throdna_22](#d-dds_throdna_22)

    <span id="d-throdna_purify_5"></span>**`throdna_purify_5`** Throdna: “...Kazaul, destroyer of bright dreams...”

    - Next → [throdna_purify_6](#d-throdna_purify_6)

    <span id="d-throdna_purify_3"></span>**`throdna_purify_3`** Throdna: “Good. We must hurry to continue our research on Kazaul.” — **effects:** sets stage 100 of [Lights in the dark](../quests/kazaul.md#stage-100)

    - Next → [throdna_purify_4](#d-throdna_purify_4)

    <span id="d-throdna_purify_2"></span>**`throdna_purify_2`** Throdna: “Then hurry and go take the vial to the shrine! What are you standing around here for?”


    <span id="d-throdna_return_8"></span>**`throdna_return_8`** Throdna: “We need you to do two things. First, you must find the shrine of Kazaul. Our scouts tell us that the shrine should be located somewhere near the base of Blackwater mountain.”

    - Next → [throdna_return_9](#d-throdna_return_9)

    <span id="d-throdna_return_4"></span>**`throdna_return_4`** Throdna: “We have more pressing matters to focus on. As I briefly mentioned before, we believe that Kazaul will manifest in our presence soon.”

    - Next → [throdna_return_5](#d-throdna_return_5)

    <span id="d-throdna_return_2"></span>**`throdna_return_2`** Throdna: “Then hurry and go find them! What are you standing around here for then?”


    <span id="d-throdna_15"></span>**`throdna_15`** Throdna: “According to our sources, there should be five parts of the ritual scattered across the mountain. Three of them describing the ritual itself, and two describing the Kazaul chant used to summon the guardian.”

    - Next → [throdna_15_1](#d-throdna_15_1)

    <span id="d-throdna_12"></span>**`throdna_12`** Throdna: “As I said, we want to learn more about the ritual itself.” — **effects:** sets stage 9 of [Lights in the dark](../quests/kazaul.md#stage-9)

    - Next → [throdna_13](#d-throdna_13)

    <span id="d-throdna_check_1"></span>**`throdna_check_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 22 of [Lights in the dark](../quests/kazaul.md#stage-22))* → [throdna_check_2](#d-throdna_check_2)
    - branch 2 → [throdna_check_fail](#d-throdna_check_fail)

    <span id="d-throdna_2"></span>**`throdna_2`** Throdna: “Oh, a visitor. Hello there. I have not seen you around here before. Did they let you in here?”

    - Next → [throdna_3](#d-throdna_3)

    <span id="d-dds_throdna_22"></span>**`dds_throdna_22`** Throdna: “Where was I? Ah, yes ...”

    - Next → [dds_throdna_22a](#d-dds_throdna_22a)

    <span id="d-throdna_purify_6"></span>**`throdna_purify_6`** Throdna: “...Kazaul ... Shadow...”

    - Next → [throdna_purify_7](#d-throdna_purify_7)

    <span id="d-throdna_return_9"></span>**`throdna_return_9`** Throdna: “However, all passageways to the shrine are 'clouded in Shadow' according to our scouts. I'm not sure what that means.”

    - Next → [throdna_return_10](#d-throdna_return_10)

    <span id="d-throdna_return_5"></span>**`throdna_return_5`** Throdna: “If that were to happen, we could not complete our research about the ritual or Kazaul itself, all our efforts would be lost.”

    - Next → [throdna_return_6](#d-throdna_return_6)

    <span id="d-throdna_15_1"></span>**`throdna_15_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 10 of [Lights in the dark](../quests/kazaul.md#stage-10))* → *conversation ends*
    - branch 2 → [throdna_16](#d-throdna_16)

    <span id="d-throdna_13"></span>**`throdna_13`** Throdna: “A while ago, we were on the verge of getting our hands on the whole ritual itself, but the messenger was killed under most interesting circumstances while traveling up here.”

    - Next → [throdna_14](#d-throdna_14)

    <span id="d-throdna_check_2"></span>**`throdna_check_2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 25 of [Lights in the dark](../quests/kazaul.md#stage-25))* → [throdna_check_3](#d-throdna_check_3)
    - branch 2 → [throdna_check_fail](#d-throdna_check_fail)

    <span id="d-throdna_check_fail"></span>**`throdna_check_fail`** Throdna: “It seems you have not found all five pieces yet.”

    - Next → [throdna_15](#d-throdna_15)

    <span id="d-throdna_3"></span>**`throdna_3`** Throdna: “Of course they did. What am I rambling on about. Harlenn and his gang always keep their worldly duties under control.”

    - Next → [throdna_4](#d-throdna_4)

    <span id="d-dds_throdna_22a"></span>**`dds_throdna_22a`** Throdna: “O Kazaul, venerabilis deus, where art thou in the shadows of tempus ...”

    - Next → [dds_throdna_22b](#d-dds_throdna_22b)

    <span id="d-throdna_purify_7"></span>**`throdna_purify_7`** Throdna: “[Throdna continues to mumble on about Kazaul, but you cannot make out any other words]”


    <span id="d-throdna_return_10"></span>**`throdna_return_10`** Throdna: “Second, we need you to take a vial of purifying spirit and apply it to the shrine.” — **effects:** sets stage 40 of [Lights in the dark](../quests/kazaul.md#stage-40)

    - Next → [throdna_return_11_select](#d-throdna_return_11_select)

    <span id="d-throdna_return_6"></span>**`throdna_return_6`** Throdna: “Therefore, we intend to delay the process as much as we can, until we have learned of its powers.”

    - Next → [throdna_return_7](#d-throdna_return_7)

    <span id="d-throdna_16"></span>**`throdna_16`** Throdna: “Hmm, maybe you could be of use here...”

    - “I would be glad to help.” → [throdna_18](#d-throdna_18)
    - “Sounds dangerous, but I'll do it.” → [throdna_18](#d-throdna_18)
    - “Keep your ritual of the Shadow to yourself. I am not getting involved in this.” → [throdna_17](#d-throdna_17)

    <span id="d-throdna_14"></span>**`throdna_14`** Throdna: “We knew he had the parts of the complete ritual on him, but since he was killed and we could not get to him because of the monsters - his notes were lost to us.”

    - Next → [throdna_15](#d-throdna_15)

    <span id="d-throdna_check_3"></span>**`throdna_check_3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 26 of [Lights in the dark](../quests/kazaul.md#stage-26))* → [throdna_check_4](#d-throdna_check_4)
    - branch 2 → [throdna_check_fail](#d-throdna_check_fail)

    <span id="d-throdna_4"></span>**`throdna_4`** Throdna: “So, who might you be then, eh? Probably here to bother me with some worldly complaint about the settlement needing more resources or someone complaining about the cold drag from the outside again?”

    - Next → [throdna_loop_1](#d-throdna_loop_1)

    <span id="d-dds_throdna_22b"></span>**`dds_throdna_22b`** Throdna: “... Sacra ritus, anciente, must be reawakened, sed obscure ...”

    - Next → [dds_throdna_22c](#d-dds_throdna_22c)

    <span id="d-throdna_return_11_select"></span>**`throdna_return_11_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 41 of [Lights in the dark](../quests/kazaul.md#stage-41))* → [throdna_return_13](#d-throdna_return_13)
    - branch 2 → [throdna_return_11](#d-throdna_return_11)

    <span id="d-throdna_return_7"></span>**`throdna_return_7`** Throdna: “You might be useful to us here again.”

    - “I'm ready for anything.” → [throdna_return_8](#d-throdna_return_8)
    - “What do you need of me?” → [throdna_return_8](#d-throdna_return_8)
    - “I sure hope it involves more killing and looting.” → [throdna_return_8](#d-throdna_return_8)

    <span id="d-throdna_18"></span>**`throdna_18`** Throdna: “Yes, you might be able to help. Not that you really have any choice though.”

    - Next → [throdna_19](#d-throdna_19)

    <span id="d-throdna_17"></span>**`throdna_17`** Throdna: “Fine, we will just have to find someone else then.”


    <span id="d-throdna_check_4"></span>**`throdna_check_4`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 27 of [Lights in the dark](../quests/kazaul.md#stage-27))* → [throdna_return_3](#d-throdna_return_3)
    - branch 2 → [throdna_check_fail](#d-throdna_check_fail)

    <span id="d-throdna_loop_1"></span>**`throdna_loop_1`** Throdna: “What do you want?”

    - “What is this place?” → [throdna_6](#d-throdna_6)
    - “Who are you?” → [throdna_7](#d-throdna_7)
    - “What was that you talked about when I arrived, Kazaul?” → [throdna_8](#d-throdna_8)
    - “Are you aware that there is a bitter rivalry going on between this settlement and Prim?” → [throdna_5](#d-throdna_5)

    <span id="d-dds_throdna_22c"></span>**`dds_throdna_22c`** Throdna: “... Lumen in tenebris, the sigil of Kazaul, lost in the mists of memoria ...”

    - Next → [dds_throdna_24](#d-dds_throdna_24)

    <span id="d-throdna_return_13"></span>**`throdna_return_13`** Throdna: “Return to me as soon as you have completed your task.”


    <span id="d-throdna_return_11"></span>**`throdna_return_11`** Throdna: “This vial is a vial of purifying spirit. It should delay the process well enough for us to be able to continue our research.”

    - “Sounds easy. I'll do it.” → [throdna_return_12](#d-throdna_return_12)
    - “Sounds dangerous, but I will do it.” → [throdna_return_12](#d-throdna_return_12)
    - “This sounds like a trap. I won't agree to do your dirty work.” → [throdna_17](#d-throdna_17)

    <span id="d-throdna_19"></span>**`throdna_19`** Throdna: “OK. Find me the pieces of the ritual that the former messenger carried on him. They should be found somewhere on the path up to Blackwater mountain.” — **effects:** sets stage 10 of [Lights in the dark](../quests/kazaul.md#stage-10)

    - “I will return with your parts of the ritual.” → [throdna_20](#d-throdna_20)

    <span id="d-throdna_6"></span>**`throdna_6`** Throdna: “This is the mages' chamber in Blackwater mountain. We devote our time to the studies of the Shadow and its descendants.”

    - “Descendants?” → [throdna_8](#d-throdna_8)
    - “Let's go back to my other questions.” → [throdna_loop_1](#d-throdna_loop_1)

    <span id="d-throdna_7"></span>**`throdna_7`** Throdna: “I am Throdna. One of the most learned persons around, if you ask me.”

    - Next → [throdna_loop_1](#d-throdna_loop_1)

    <span id="d-throdna_8"></span>**`throdna_8`** Throdna: “Kazaul, the Shadow spawn of red marrow.” — **effects:** sets stage 8 of [Lights in the dark](../quests/kazaul.md#stage-8)

    - Next → [throdna_9](#d-throdna_9)

    <span id="d-throdna_5"></span>**`throdna_5`** Throdna: “And there you go with your mundane problems. I tell you, your worldly troubles do not interest me the least bit.”

    - Next → [throdna_6](#d-throdna_6)

    <span id="d-dds_throdna_24"></span>**`dds_throdna_24`** Throdna: “... Perhaps the incantatio of the ancients holds the key, sed forgotten ...”

    - “What was the word again? Ah, I remember. [Loud voice] Kazaul Est!” → [dds_throdna_30](#d-dds_throdna_30)

    <span id="d-throdna_return_12"></span>**`throdna_return_12`** Throdna: “Good, here is the vial. Now hurry.” — **effects:** sets stage 41 of [Lights in the dark](../quests/kazaul.md#stage-41), gives [Vial of purifying spirit](../items/q_kazaul_vial.md)

    - Next → [throdna_return_13](#d-throdna_return_13)

    <span id="d-throdna_20"></span>**`throdna_20`** Throdna: “Yes, you will.” — **effects:** sets stage 11 of [Lights in the dark](../quests/kazaul.md#stage-11)


    <span id="d-throdna_9"></span>**`throdna_9`** Throdna: “We have been trying to read all we can on Kazaul, and the ritual. It seems we might be too late.”

    - “What do you mean?” → [throdna_10](#d-throdna_10)

    <span id="d-dds_throdna_30"></span>**`dds_throdna_30`** Throdna: “You are still here? Well ...”

    - Next → [dds_throdna_32](#d-dds_throdna_32)

    <span id="d-throdna_10"></span>**`throdna_10`** Throdna: “The ritual. We believe that Kazaul will manifest in our presence soon.”

    - Next → [throdna_11](#d-throdna_11)

    <span id="d-dds_throdna_32"></span>**`dds_throdna_32`** Throdna: “So, you're not the one who stole my notes?”

    - “No, in fact I helped purify the shrine.” → [dds_throdna_40](#d-dds_throdna_40)

    <span id="d-throdna_11"></span>**`throdna_11`** Throdna: “We must learn more about the Kazaul ritual, to gain its power and learn to use it for our purposes.”

    - “Can I help in some way?” → [throdna_12](#d-throdna_12)
    - “What were you planning to do?” → [throdna_12](#d-throdna_12)

    <span id="d-dds_throdna_40"></span>**`dds_throdna_40`** Throdna: “That is right. So, what do you want?”

    - “I need to know what all this chant can do.” → [dds_throdna_50](#d-dds_throdna_50)

    <span id="d-dds_throdna_50"></span>**`dds_throdna_50`** Throdna: “It's a powerful chant for many dangerous things. I'm not sure I should tell. Followers of Kazaul want to get a foothold in Dhayavar.”

    - Next → [dds_throdna_52](#d-dds_throdna_52)

    <span id="d-dds_throdna_52"></span>**`dds_throdna_52`** Throdna: “The ritual of the nocturnus, should it be performed under Luna's watchful eye ...”

    - Next → [dds_throdna_54](#d-dds_throdna_54)

    <span id="d-dds_throdna_54"></span>**`dds_throdna_54`** Throdna: “... Ego dubito, whether the offerings still hold power, or are but relics of a bygone era ...”

    - “Not again - Kazaul Est!” → [dds_throdna_60](#d-dds_throdna_60)

    <span id="d-dds_throdna_60"></span>**`dds_throdna_60`** Throdna: “Yes. This piece of the ritual is of Kazaul. Along with the first part, one can raise Kazaul monsters, use in sacrifices, make defensive walls, impenetrable barriers ... dangerous rites.” — **effects:** sets stage 100 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-100)

    - “I just came from such an impenetrable barrier in the south of Stoutford.” → [dds_throdna_70](#d-dds_throdna_70)

    <span id="d-dds_throdna_70"></span>**`dds_throdna_70`** Throdna: “An impenetrable barrier? That's no good. If Kazaul gains a foothold in Dhayavar, strong monsters will roam in Dhayavar.”

    - Next → [dds_throdna_72](#d-dds_throdna_72)

    <span id="d-dds_throdna_72"></span>**`dds_throdna_72`** Throdna: “... Is the tempus ripe for the reawakening of Kazaul, or is it but an illusion ...”

    - Next → [dds_throdna_74](#d-dds_throdna_74)

    <span id="d-dds_throdna_74"></span>**`dds_throdna_74`** Throdna: “... Must find the correct verba, the sacred words that summon the divine ...”

    - Next → [dds_throdna_78](#d-dds_throdna_78)

    <span id="d-dds_throdna_78"></span>**`dds_throdna_78`** Throdna: “... Kazaul's essence, hidden within the arcana of the old scrolls, waiting to be uncovered ...”

    - “Kazaul Est!!” → [dds_throdna_80](#d-dds_throdna_80)

    <span id="d-dds_throdna_80"></span>**`dds_throdna_80`** Throdna: “Eh, yes. The barrier. One has to use the two pieces of the ritual and a chant of passage to go through the barrier.”

    - “What is the chant of passage?” → [dds_throdna_90](#d-dds_throdna_90)

    <span id="d-dds_throdna_90"></span>**`dds_throdna_90`** Throdna: “That is something I do not know.”

    - “So, nothing to be done?” → [dds_throdna_100](#d-dds_throdna_100)

    <span id="d-dds_throdna_100"></span>**`dds_throdna_100`** Throdna: “I didn't say that! There was a traveler a long time back - he wrote a book Calomyran Secrets. It has the chant of passage, among other things to counter Kazaul dangers. Find it, if you can.” — **effects:** sets stage 110 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-110)

    - “Calomyran Secrets? That rings a bell. Thanks!” → [dds_throdna_102](#d-dds_throdna_102)

    <span id="d-dds_throdna_102"></span>**`dds_throdna_102`** Throdna: “... Ah, the anciente scriptura, perhaps it reveals the secret to rekindling the divine ...”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 17 lines changed<br>· text: “.. Kazaul .. Shadow ..” → “...Kazaul ... Shadow...”<br>· text: “Hm, maybe you could be of use here..” → “Hmm, maybe you could be of use here...” |
| [v0.8.14](../versions/0.8.14.md) | Dialogue: 22 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=throdna.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=throdna.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=throdna.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=throdna.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `throdna` · Data from v0.8.18</small>
