# ![](../assets/icons/monsters/monsters_ld1_12.png){ .sprite } Golin

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 80 |
| Max AP | 10 |
| Attack cost | 4 |
| Move cost | 5 |
| Damage | 1 to 4 |
| Attack chance | 40 |
| Block chance | 120 |
| Damage resistance | 5 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Found on

- [brimhaven_school](../maps/brimhaven_school.md)

## Quests

- [Lessons learned](../quests/brv_school2.md): stages 20, 30, 40, 50, 60, 100, 104, 240
- [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md): stages 20, 21

??? quote "Dialogue (75 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-golin"></span>**`golin`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 220 of [Lessons learned](../quests/brv_school2.md#stage-220))* → [golin_220](#d-golin_220)
    - branch 2 *(if reached stage 210 of [Lessons learned](../quests/brv_school2.md#stage-210))* → [golin_210](#d-golin_210)
    - branch 3 *(if reached stage 200 of [Lessons learned](../quests/brv_school2.md#stage-200))* → [golin_200](#d-golin_200)
    - branch 4 *(if reached stage 152 of [Lessons learned](../quests/brv_school2.md#stage-152))* → [golin_152](#d-golin_152)
    - branch 5 *(if reached stage 150 of [Lessons learned](../quests/brv_school2.md#stage-150))* → [golin_150](#d-golin_150)
    - branch 6 *(if reached stage 124 of [Lessons learned](../quests/brv_school2.md#stage-124))* → [golin_124](#d-golin_124)
    - branch 7 *(if reached stage 122 of [Lessons learned](../quests/brv_school2.md#stage-122))* → [golin_122](#d-golin_122)
    - branch 8 *(if reached stage 120 of [Lessons learned](../quests/brv_school2.md#stage-120))* → [golin_120](#d-golin_120)
    - branch 9 *(if reached stage 104 of [Lessons learned](../quests/brv_school2.md#stage-104))* → [golin_104](#d-golin_104)
    - branch 10 *(if reached stage 100 of [Lessons learned](../quests/brv_school2.md#stage-100))* → [golin_100](#d-golin_100)
    - branch 11 *(if reached stage 60 of [Lessons learned](../quests/brv_school2.md#stage-60))* → [golin_60](#d-golin_60)
    - branch 12 *(if reached stage 50 of [Lessons learned](../quests/brv_school2.md#stage-50))* → [golin_50](#d-golin_50)
    - branch 13 *(if reached stage 40 of [Lessons learned](../quests/brv_school2.md#stage-40))* → [golin_40](#d-golin_40)
    - branch 14 *(if reached stage 30 of [Lessons learned](../quests/brv_school2.md#stage-30))* → [brv_school_seated_22](#d-brv_school_seated_22)
    - branch 15 → [brv_school_seated_12](#d-brv_school_seated_12)

    <span id="d-golin_220"></span>**`golin_220`** Golin: “Pity you are leaving. It was a nice break from the boring lessons.”


    <span id="d-golin_210"></span>**`golin_210`** Golin: “What a pity you have to go.”


    <span id="d-golin_200"></span>**`golin_200`** Golin: “Wow, that was exciting!”

    - Next → [golin_200_10](#d-golin_200_10)

    <span id="d-golin_152"></span>**`golin_152`** Golin: “Wow, what is that beast? You were splendid!”

    - “Thank you.” → [golin_152_10](#d-golin_152_10)
    - “Oh, that was nothing special.” → [golin_152_10](#d-golin_152_10)

    <span id="d-golin_150"></span>**`golin_150`** Golin: “Wow, what is that beast? What did you do?”

    - “I don't know either, but it looks like it wants to kill me.” → *conversation ends*

    <span id="d-golin_124"></span>**`golin_124`** Golin: “Wow - you dared to fight the teacher. Awesome!”


    <span id="d-golin_122"></span>**`golin_122`** Golin: “You killed the teacher! She was not very good, but she did not deserve such a death.”

    - Next → [golin_122_10](#d-golin_122_10)

    <span id="d-golin_120"></span>**`golin_120`** Golin: “Hey, do not run away! Finish your fight with the teacher.”


    <span id="d-golin_104"></span>**`golin_104`** Golin: “Practice session is over now. We won't duel anymore.”


    <span id="d-golin_100"></span>**`golin_100`** [Golin](../monsters/golin.md): “Hey, you are not bad! We should stop here indeed. Otherwise you might get hurt.” — **effects:** sets stage 104 of [Lessons learned](../quests/brv_school2.md#stage-104), clears stage 100 of [Lessons learned](../quests/brv_school2.md#stage-100), spawns monsters on brimhaven_school

    - “Sure.” → *conversation ends*
    - “Me? You will get hurt!” → [golin_100_10](#d-golin_100_10)

    <span id="d-golin_60"></span>**`golin_60`** Golin: “You want to fight me?! Hahaha!”

    - “What's so funny about it?” → [golin_60_10](#d-golin_60_10)

    <span id="d-golin_50"></span>**`golin_50`** Golin: “I already have my exercise equipment.”

    - “Hush, the teacher is talking again.” → [brv_school_seated](#d-brv_school_seated)

    <span id="d-golin_40"></span>**`golin_40`** Golin: “It's about time. This is my favorite class.”

    - “What will happen now?” → [golin_40_10](#d-golin_40_10)

    <span id="d-brv_school_seated_22"></span>**`brv_school_seated_22`** [Teacher](../monsters/brv_teacher.md): “No talking, please.”

    - “But...” → [brv_school_seated_22](#d-brv_school_seated_22)
    - “[nod silently]” → [brv_school_seated_30](#d-brv_school_seated_30)

    <span id="d-brv_school_seated_12"></span>**`brv_school_seated_12`** [Golin](../monsters/golin.md): “Hi kid. I am Golin.” — **effects:** sets stage 20 of [Lessons learned](../quests/brv_school2.md#stage-20)

    - “Thanks, it's a pleasure.” → [brv_school_seated_14](#d-brv_school_seated_14)
    - “[nod silently]” → [brv_school_seated_20](#d-brv_school_seated_20)

    <span id="d-golin_200_10"></span>**`golin_200_10`** Golin: “I never liked this statue, but I never thought that it would be so evil.”


    <span id="d-golin_152_10"></span>**`golin_152_10`** Golin: “Now that the statue is gone, I feel like a great burden has fallen from my soul.”

    - “I found the statue in the corner awful right from the beginning.” → *conversation ends*

    <span id="d-golin_122_10"></span>**`golin_122_10`** Golin: “I will avenge her. Prepare to die!” — **effects:** faction “brv_fct_school_duel” -10, sets stage 240 of [Lessons learned](../quests/brv_school2.md#stage-240)

    - Next → *fight starts*

    <span id="d-golin_100_10"></span>**`golin_100_10`** Golin: “Haha! Yes, me of course. Do not always be offended.”


    <span id="d-golin_60_10"></span>**`golin_60_10`** Golin: “Hahaha! Hahaha! Sorry * snort * Pooh! You are really funny!”

    - “Do you think?” → [golin_60_20](#d-golin_60_20)

    <span id="d-brv_school_seated"></span>**`brv_school_seated`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 60 of [Lessons learned](../quests/brv_school2.md#stage-60))* → *conversation ends*
    - branch 2 *(if carry 1× [Wooden sword](../items/brv_school_sword.md); carry 1× [Paper shield](../items/brv_school_shield.md))* → [brv_school_practice_20](#d-brv_school_practice_20)
    - branch 3 *(if carry 1× [Wooden sword](../items/brv_school_sword.md); wearing [Paper shield](../items/brv_school_shield.md))* → [brv_school_practice_20](#d-brv_school_practice_20)
    - branch 4 *(if wearing [Wooden sword](../items/brv_school_sword.md); carry 1× [Paper shield](../items/brv_school_shield.md))* → [brv_school_practice_20](#d-brv_school_practice_20)
    - branch 5 *(if wearing [Wooden sword](../items/brv_school_sword.md); wearing [Paper shield](../items/brv_school_shield.md))* → [brv_school_practice_20](#d-brv_school_practice_20)
    - branch 6 *(if reached stage 40 of [Lessons learned](../quests/brv_school2.md#stage-40))* → [brv_school_practice_10](#d-brv_school_practice_10)
    - branch 7 *(if reached stage 30 of [Lessons learned](../quests/brv_school2.md#stage-30))* → [brv_school_seated_30](#d-brv_school_seated_30)
    - branch 8 *(if reached stage 20 of [Lessons learned](../quests/brv_school2.md#stage-20))* → [brv_school_seated_20](#d-brv_school_seated_20)
    - branch 9 → [brv_school_seated_10](#d-brv_school_seated_10)

    <span id="d-golin_40_10"></span>**`golin_40_10`** Golin: “Listen, she is going to explain.”

    - Next → [brv_school_practice_10](#d-brv_school_practice_10)

    <span id="d-brv_school_seated_30"></span>**`brv_school_seated_30`** [Teacher](../monsters/brv_teacher.md): “I will start from the beginning again, because it is so important. You can't listen to it often enough.”

    - Next → [brv_school_history_10](#d-brv_school_history_10)

    <span id="d-brv_school_seated_14"></span>**`brv_school_seated_14`** [Teacher](../monsters/brv_teacher.md): “No talking, please.”

    - “But...” → [brv_school_seated_14](#d-brv_school_seated_14)
    - “[keep silent]” → [brv_school_seated_20](#d-brv_school_seated_20)

    <span id="d-brv_school_seated_20"></span>**`brv_school_seated_20`** [Teacher](../monsters/brv_teacher.md): “Very well, you have found a place after all. Now let us proceed with our history lesson.”

    - “Please do.” → [brv_school_seated_22](#d-brv_school_seated_22)
    - “[nod silently]” → [brv_school_seated_30](#d-brv_school_seated_30)

    <span id="d-golin_60_20"></span>**`golin_60_20`** Golin: “[still giggling] If you insist - en garde!”

    - “Yes, en Garde!” → [golin_60_30](#d-golin_60_30)

    <span id="d-brv_school_practice_20"></span>**`brv_school_practice_20`** [Teacher](../monsters/brv_teacher.md): “You all have your gear? OK.”

    - Next → [brv_school_practice_22](#d-brv_school_practice_22)

    <span id="d-brv_school_practice_10"></span>**`brv_school_practice_10`** [Teacher](../monsters/brv_teacher.md): “Everybody get your practice gear out of the chest over there. Each of you take one wooden sword and one paper shield, please. Then sit down again.” — **effects:** sets stage 50 of [Lessons learned](../quests/brv_school2.md#stage-50)

    - “OK” → *conversation ends*
    - “Wooden weapons? Honestly?” → [brv_school_practice_12](#d-brv_school_practice_12)
    - “May I use my own weapons?” → [brv_school_practice_14](#d-brv_school_practice_14)

    <span id="d-brv_school_seated_10"></span>**`brv_school_seated_10`** Golin: “[You sit next to a smug-looking child that is about your age.]”

    - Next → [brv_school_seated_12](#d-brv_school_seated_12)

    <span id="d-brv_school_history_10"></span>**`brv_school_history_10`** Golin: “In the glorious days of year 2177, the enslavement of men ended.” — **effects:** sets stage 30 of [Lessons learned](../quests/brv_school2.md#stage-30)

    - Next → [brv_school_history_12](#d-brv_school_history_12)

    <span id="d-golin_60_30"></span>**`golin_60_30`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 100 of [Lessons learned](../quests/brv_school2.md#stage-100)

    - branch 1 → *fight starts*

    <span id="d-brv_school_practice_22"></span>**`brv_school_practice_22`** [Teacher](../monsters/brv_teacher.md): “Listen everybody: Use the sword and shield of the school set. We duel in pairs, the new kid first.”

    - Next → [brv_school_practice_24](#d-brv_school_practice_24)

    <span id="d-brv_school_practice_12"></span>**`brv_school_practice_12`** Golin: “Of course. You mustn't hurt yourself.”

    - Next → [brv_school_practice_10](#d-brv_school_practice_10)

    <span id="d-brv_school_practice_14"></span>**`brv_school_practice_14`** Golin: “Of course not.”

    - Next → [brv_school_practice_10](#d-brv_school_practice_10)

    <span id="d-brv_school_history_12"></span>**`brv_school_history_12`** Golin: “The world was formed new.”

    - Next → [brv_school_history_20](#d-brv_school_history_20)

    <span id="d-brv_school_practice_24"></span>**`brv_school_practice_24`** Golin: “Run now, seek ye an opponent!”

    - “Anybody?” → [brv_school_practice_30](#d-brv_school_practice_30)

    <span id="d-brv_school_history_20"></span>**`brv_school_history_20`** Golin: “Our redeemers fought a bloody war to make the world worthy for us again. In exchange and out of deepest respect, men helped to build up vast cities and many underground places.”

    - Next → [brv_school_history_22](#d-brv_school_history_22)

    <span id="d-brv_school_practice_30"></span>**`brv_school_practice_30`** Golin: “Just go ahead. But don't forget: You must use the school weapon and shield.” — **effects:** sets stage 60 of [Lessons learned](../quests/brv_school2.md#stage-60), changes map brimhaven_school


    <span id="d-brv_school_history_22"></span>**`brv_school_history_22`** Golin: “Little has been preserved from this period. Nor City is the only large city that has survived from this period. Their bright and magnificent flags were visible from afar in the surrounding area.”

    - Next → [brv_school_history_30](#d-brv_school_history_30)

    <span id="d-brv_school_history_30"></span>**`brv_school_history_30`** Golin: “Just imagine all those mighty churches and splendid palaces! It was a merry time, down under Mt. Galmore, the highest mountain in whole of Dhayavar.”

    - “Sigh.” → [brv_school_history_32](#d-brv_school_history_32)
    - “[keep silent]” → [brv_school_history_40](#d-brv_school_history_40)

    <span id="d-brv_school_history_32"></span>**`brv_school_history_32`** Golin: “What...? Don't interrupt me. Now I don't know where I was. I have to start from the beginning.”

    - “Sorry.” → [brv_school_history_10](#d-brv_school_history_10)

    <span id="d-brv_school_history_40"></span>**`brv_school_history_40`** Golin: “People were living happily and all was well. There was plenty of food and music everywhere.”

    - Next → [brv_school_history_42](#d-brv_school_history_42)

    <span id="d-brv_school_history_42"></span>**`brv_school_history_42`** Golin: “I hope you will live to see it one day.”

    - Next → [brv_school_history_43](#d-brv_school_history_43)

    <span id="d-brv_school_history_43"></span>**`brv_school_history_43`** Golin: “But one dark day, this treacherous liar, Elythara, appeared. Many men were betrayed by her blinding light.”

    - Next → [brv_school_history_44](#d-brv_school_history_44)

    <span id="d-brv_school_history_44"></span>**`brv_school_history_44`** Golin: “They believed in her false promises and were misled.”

    - Next → [brv_school_history_45](#d-brv_school_history_45)

    <span id="d-brv_school_history_45"></span>**`brv_school_history_45`** Golin: “Then Elytharan cultists arrived on the shore of the northern sea, which is also known as the Sea of Tears.”

    - Next → [brv_school_history_46](#d-brv_school_history_46)

    <span id="d-brv_school_history_46"></span>**`brv_school_history_46`** Golin: “The cultists worshipped the blinding and cleansing light of Elythara. Clever and sneaky as they were, they gained people's trust.”

    - Next → [brv_school_history_47](#d-brv_school_history_47)

    <span id="d-brv_school_history_47"></span>**`brv_school_history_47`** Golin: “Partly with gold, partly with cunning and violence, they attracted more and more people to their side. Those who still wanted to walk the old ways often found their house burning.”

    - Next → [brv_school_history_48](#d-brv_school_history_48)

    <span id="d-brv_school_history_48"></span>**`brv_school_history_48`** Golin: “A general distrust began, and it didn't take long until weapons were drawn. Brothers fought each other - the horrible War of Dawn began!”

    - Next → [brv_school_history_50](#d-brv_school_history_50)

    <span id="d-brv_school_history_50"></span>**`brv_school_history_50`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 20 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-20))* → [brv_school_history_50_1](#d-brv_school_history_50_1)
    - branch 2 → [brv_school_history_60](#d-brv_school_history_60)

    <span id="d-brv_school_history_50_1"></span>**`brv_school_history_50_1`** [Golin](../monsters/golin.md): “Psst...”

    - “[keep silent]” → [brv_school_history_60](#d-brv_school_history_60)
    - “[whispering] What's up?” → [brv_school_history_52](#d-brv_school_history_52)

    <span id="d-brv_school_history_60"></span>**`brv_school_history_60`** [Teacher](../monsters/brv_teacher.md): “However Elythara and her cultists failed to completely annihilate the old ways. Many true men managed to hide in remote places in the total darkness, unknown to the Elytharans. Also, Elythara's power is diminished underground.”

    - “[whispering to Golin] What's up?” *(if NOT reached stage 20 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-20))* → [brv_school_history_52](#d-brv_school_history_52)
    - “[keep silent]” → [brv_school_history_70](#d-brv_school_history_70)

    <span id="d-brv_school_history_52"></span>**`brv_school_history_52`** [Teacher](../monsters/brv_teacher.md): “Be quiet, please. How can I concentrate if you are talking all the time? Where was I? I had better start anew.” — **effects:** sets stage 20 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-20)

    - “Yes, sorry.” → [brv_school_history_10](#d-brv_school_history_10)

    <span id="d-brv_school_history_70"></span>**`brv_school_history_70`** Golin: “Each city was ruled by one or two houses who closely collaborated with the Elytharan priests. People were mainly influenced by the Elytharan priests.”

    - Next → [brv_school_history_71](#d-brv_school_history_71)

    <span id="d-brv_school_history_71"></span>**`brv_school_history_71`** Golin: “The Elytharans built several towns and cities, dedicated to their goddess. Several aristocratic houses were formed at that time.”

    - Next → [brv_school_history_72](#d-brv_school_history_72)

    <span id="d-brv_school_history_72"></span>**`brv_school_history_72`** Golin: “First the Elytharans erected the city of Feygard on the shore of the Sea of Tears. It became a center of trade for the realm due to its access to the sea.”

    - Next → [brv_school_history_73](#d-brv_school_history_73)

    <span id="d-brv_school_history_73"></span>**`brv_school_history_73`** Golin: “The town of Loneford was founded and it soon became famous for its fertile fields and healthy vegetables which fed the northern parts of the Forgotten Kingdom.”

    - Next → [brv_school_history_74](#d-brv_school_history_74)

    <span id="d-brv_school_history_74"></span>**`brv_school_history_74`** Golin: “Blackwater Mountain was explored, and on its summit a large sanctuary for the Elytharan priests was erected.”

    - Next → [brv_school_history_75](#d-brv_school_history_75)

    <span id="d-brv_school_history_75"></span>**`brv_school_history_75`** Golin: “The mining colony of Prim was also founded after pioneers found rich sources of iron and coal under the mountain.”

    - Next → [brv_school_history_76](#d-brv_school_history_76)

    <span id="d-brv_school_history_76"></span>**`brv_school_history_76`** Golin: “The city of Fallhaven became a prospering center of trade due to its excellent location as a junction between the sanctuary of Blackwater Mountain, Stoutford, Nor City and Feygard.”

    - Next → [brv_school_history_77](#d-brv_school_history_77)

    <span id="d-brv_school_history_77"></span>**`brv_school_history_77`** Golin: “Big storehouses were built to safely store shipments.”

    - Next → [brv_school_history_80](#d-brv_school_history_80)

    <span id="d-brv_school_history_80"></span>**`brv_school_history_80`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 21 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-21))* → [brv_school_history_88](#d-brv_school_history_88)
    - branch 2 → [brv_school_history_82](#d-brv_school_history_82)

    <span id="d-brv_school_history_88"></span>**`brv_school_history_88`** Golin: “However, bands of thieves were soon attracted by the growing wealth and united under one big organization, the Thieves' Guild, whose guild halls were secretly placed in Fallhaven, Feygard, and Nor City, those being the richest cities at…”

    - Next → [brv_school_history_90](#d-brv_school_history_90)

    <span id="d-brv_school_history_82"></span>**`brv_school_history_82`** Golin: “However, bands of thieves ...”

    - “Thieves?!” → [brv_school_history_84](#d-brv_school_history_84)
    - “[keep silent]” → [brv_school_history_86](#d-brv_school_history_86)

    <span id="d-brv_school_history_90"></span>**`brv_school_history_90`** Golin: “At last many other towns, including our Brimhaven and Brightport were also founded around this time.”

    - “[Sigh] 'At last' sounds good.” → [brv_school_history_52](#d-brv_school_history_52)
    - “[keep silent]” → [brv_school_history_92](#d-brv_school_history_92)

    <span id="d-brv_school_history_84"></span>**`brv_school_history_84`** Golin: “Yes thieves. Dishonorable men who cut cheeky children's neck for a few pennies. But ... where was I?” — **effects:** sets stage 21 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-21)

    - “You said 'However, bands of thieves'” → [brv_school_history_52](#d-brv_school_history_52)
    - “[keep silent]” → [brv_school_history_85](#d-brv_school_history_85)

    <span id="d-brv_school_history_86"></span>**`brv_school_history_86`** Golin: “... were soon attracted by the growing wealth and united under one big organization, the Thieves' Guild, whose guild halls were secretly placed in Fallhaven, Feygard, and Nor City, those being the richest cities at that time.”

    - Next → [brv_school_history_90](#d-brv_school_history_90)

    <span id="d-brv_school_history_92"></span>**`brv_school_history_92`** Golin: “Brimhaven has become an emerging, thriving city. Our importance will increase - you have it in your hands!”

    - Next → [brv_school_history_94](#d-brv_school_history_94)

    <span id="d-brv_school_history_85"></span>**`brv_school_history_85`** Golin: “You don't know what I just said? Then I had better start anew.”

    - Next → [brv_school_history_10](#d-brv_school_history_10)

    <span id="d-brv_school_history_94"></span>**`brv_school_history_94`** Golin: “So study hard and beware of the lies of false leaders!”

    - Next → [brv_school_history_96](#d-brv_school_history_96)

    <span id="d-brv_school_history_96"></span>**`brv_school_history_96`** Golin: “[Waiting silently]”

    - Next → [brv_school_history_100](#d-brv_school_history_100)

    <span id="d-brv_school_history_100"></span>**`brv_school_history_100`** Golin: “OK now. Does anybody have a question?”

    - “Yes, please. Who was Elythara?” → [brv_school_history_110](#d-brv_school_history_110)
    - “[keep silent]” → [brv_school_history_200](#d-brv_school_history_200)

    <span id="d-brv_school_history_110"></span>**`brv_school_history_110`** Golin: “Oh dear. Didn't you listen? Well, because you are new, I will tell you again.”

    - Next → [brv_school_history_10](#d-brv_school_history_10)

    <span id="d-brv_school_history_200"></span>**`brv_school_history_200`** Golin: “And now we will do something completely different. Let's practice fighting, so that you learn how to defend yourselves.” — **effects:** sets stage 40 of [Lessons learned](../quests/brv_school2.md#stage-40)

    - “Finally. I thought her talking would never cease.” → [brv_school_practice_10](#d-brv_school_practice_10)



## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 75 lines added |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 6 lines changed<br>· text: “However Elythara and her cultists failed to completely annihilate the…” → “However Elythara and her cultists failed to completely annihilate the…”<br>· text: “The Elytharans built several towns and cities, dedicated to their god…” → “The Elytharans built several towns and cities, dedicated to their god…” |
| [v0.7.15](../versions/0.7.15.md) | Dialogue: 1 line changed<br>· text: “It's about time. This is my favourite class.” → “It's about time. This is my favorite class.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=golin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=golin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=golin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=golin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `golin` · Data from v0.8.18</small>
