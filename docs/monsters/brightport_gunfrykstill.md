# ![](../assets/icons/monsters/monsters_ld1_74.png){ .sprite } Gunfryk

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

- [brightport_bakery](../maps/brightport_bakery.md)

## Quests

- [Boxed in](../quests/brightport_thieves.md): stages 60
- [Priceful vengeance](../quests/brightport_goons.md): stages 50, 60, 80, 120, 135, 140, 150
- [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md): stages 136, 139, 150, 156, 211, 212, 234, 240

??? quote "Dialogue (33 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightport_gunfryk_selector0"></span>**`brightport_gunfryk_selector0`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139); NOT reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60))* → [brightport_gunfryk_selector](#d-brightport_gunfryk_selector)
    - Next *(if reached stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139))* → [brightport_gunfryk_selectorafter](#d-brightport_gunfryk_selectorafter)
    - Next *(if reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60))* → [brightport_gunfryk_selectorafter](#d-brightport_gunfryk_selectorafter)

    <span id="d-brightport_gunfryk_selector"></span>**`brightport_gunfryk_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 80 of [Priceful vengeance](../quests/brightport_goons.md#stage-80); NOT reached stage 120 of [Priceful vengeance](../quests/brightport_goons.md#stage-120); NOT reached stage 240 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-240); NOT reached stage 211 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-211); NOT reached stage 135 of [Priceful vengeance](../quests/brightport_goons.md#stage-135))* → [brightport_gunfryk9](#d-brightport_gunfryk9)
    - Next *(if reached stage 240 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-240); NOT reached stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139))* → [brightport_gunfryk17](#d-brightport_gunfryk17)
    - Next *(if reached stage 211 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-211); NOT reached stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139))* → [brightport_gunfryk11](#d-brightport_gunfryk11)
    - Next *(if reached stage 50 of [Priceful vengeance](../quests/brightport_goons.md#stage-50); reached stage 135 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-135); NOT reached stage 136 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-136))* → [brightport_gunfryk_killfail0](#d-brightport_gunfryk_killfail0)
    - Next *(if reached stage 50 of [Priceful vengeance](../quests/brightport_goons.md#stage-50); NOT reached stage 135 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-135))* → [brightport_gunfryk2](#d-brightport_gunfryk2)
    - Next → [brightport_gunfryk](#d-brightport_gunfryk)

    <span id="d-brightport_gunfryk_selectorafter"></span>**`brightport_gunfryk_selectorafter`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 120 of [Priceful vengeance](../quests/brightport_goons.md#stage-120))* → [brightport_gunfryk_help](#d-brightport_gunfryk_help)
    - Next *(if reached stage 150 of [Priceful vengeance](../quests/brightport_goons.md#stage-150))* → [brightport_gunfryk_help](#d-brightport_gunfryk_help)
    - Next *(if reached stage 140 of [Priceful vengeance](../quests/brightport_goons.md#stage-140))* → [brightport_gunfryk_help](#d-brightport_gunfryk_help)
    - Next *(if reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60))* → [brightport_gunfryk_selector_after](#d-brightport_gunfryk_selector_after)

    <span id="d-brightport_gunfryk9"></span>**`brightport_gunfryk9`** Gunfryk: “Any progress on that investigation of yours?”

    - “I found their hideout and inside was this blade.” *(if hand over 1× [Nor city made blade](../items/brightport_sword0.md); reached stage 130 of [Priceful vengeance](../quests/brightport_goons.md#stage-130); reached stage 110 of [Priceful vengeance](../quests/brightport_goons.md#stage-110))* → [brightport_gunfryk16](#d-brightport_gunfryk16)
    - “I found a bunch of goods hidden in a cave east, here's a blade I took.” *(if hand over 1× [Nor city made blade](../items/brightport_sword0.md); NOT reached stage 130 of [Priceful vengeance](../quests/brightport_goons.md#stage-130); reached stage 110 of [Priceful vengeance](../quests/brightport_goons.md#stage-110))* → [brightport_gunfryk11](#d-brightport_gunfryk11)
    - “Sorry, I couldn't find anything.” *(if reached stage 130 of [Priceful vengeance](../quests/brightport_goons.md#stage-130))* → [brightport_gunfryk14](#d-brightport_gunfryk14)
    - “Sorry, I couldn't find anything.” *(if reached stage 110 of [Priceful vengeance](../quests/brightport_goons.md#stage-110); NOT reached stage 130 of [Priceful vengeance](../quests/brightport_goons.md#stage-130); NOT carry 1× [Nor city made blade](../items/brightport_sword0.md))* → [brightport_gunfryk21](#d-brightport_gunfryk21)
    - “Not yet. But I'll find something substantial soon.” → [brightport_gunfryk10](#d-brightport_gunfryk10)

    <span id="d-brightport_gunfryk17"></span>**`brightport_gunfryk17`** [Gunfryk](../monsters/brightport_gunfrykstill.md): “Most interesting, Nor City made? Nothing of that sort passes through our checkpoints without permission. Yes, that warrants an investigation. What are the name of these criminals?”

    - “Barthold and Dynes sir.” → [brightport_gunfryk18](#d-brightport_gunfryk18)

    <span id="d-brightport_gunfryk11"></span>**`brightport_gunfryk11`** Gunfryk: “Most interesting, Nor City made? Nothing of that sort passes through our checkpoints without permission. Yes, that warrants an investigation. What are the name of these criminals?” — **effects:** sets stage 211 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-211)

    - “Barthold and Dynes sir.” → [brightport_gunfryk12](#d-brightport_gunfryk12)

    <span id="d-brightport_gunfryk_killfail0"></span>**`brightport_gunfryk_killfail0`** [Dummy NPC](../monsters/none.md): “The commander extends his arm to grab your shoulder.”

    - Next → [brightport_gunfryk_killfail](#d-brightport_gunfryk_killfail)

    <span id="d-brightport_gunfryk2"></span>**`brightport_gunfryk2`** Gunfryk: “Lizardman you say? That is extremely serious. I will call my men and we will hurry to save him!” — **effects:** sets stage 50 of [Priceful vengeance](../quests/brightport_goons.md#stage-50), removes monsters from brightport_bakery, sets stage 234 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-234)


    <span id="d-brightport_gunfryk"></span>**`brightport_gunfryk`** Gunfryk: “I'm the guard commander. Inform me or my men if you spot any trouble.” — **effects:** sets stage 156 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-156)

    - “[Lie] My friend was chased by a lizardman and he went inside the derelict house east of town. Please save him!” *(if NOT reached stage 80 of [Priceful vengeance](../quests/brightport_goons.md#stage-80); NOT reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60); reached stage 30 of [Priceful vengeance](../quests/brightport_goons.md#stage-30); NOT reached stage 150 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-150); NOT reached stage 136 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-136); NOT reached stage 50 of [Priceful vengeance](../quests/brightport_goons.md#stage-50))* → [brightport_gunfryk2](#d-brightport_gunfryk2)
    - “I heard you really love orchids, Sir Gunfryk. [Blackmail him with the records.]” *(if reached stage 40 of [Priceful vengeance](../quests/brightport_goons.md#stage-40); NOT reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60); NOT reached stage 135 of [Priceful vengeance](../quests/brightport_goons.md#stage-135))* → [brightport_gunfryk3](#d-brightport_gunfryk3)
    - “Sir, I have some information on two troublemakers in town who wish to see you gone.” *(if reached stage 30 of [Priceful vengeance](../quests/brightport_goons.md#stage-30); NOT reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60); NOT reached stage 50 of [Priceful vengeance](../quests/brightport_goons.md#stage-50); NOT reached stage 135 of [Priceful vengeance](../quests/brightport_goons.md#stage-135))* → [brightport_gunfryk1](#d-brightport_gunfryk1)
    - “Can you tell me more about your job?” → [brightport_gunfryk0](#d-brightport_gunfryk0)

    <span id="d-brightport_gunfryk_help"></span>**`brightport_gunfryk_help`** Gunfryk: “It's good to see you around, glory to Feygard.”

    - “Can you tell me more about your job?” → [brightport_gunfryk0](#d-brightport_gunfryk0)

    <span id="d-brightport_gunfryk_selector_after"></span>**`brightport_gunfryk_selector_after`** Gunfryk: “It sours my day to see a treacherous criminal rat. You and your friends will regret this one day.”


    <span id="d-brightport_gunfryk16"></span>**`brightport_gunfryk16`** [Dummy NPC](../monsters/none.md): “You remember the deal you made with Barthold and Dynes, even though they gave you the money you still handed the evidence over to the guards.” — **effects:** sets stage 240 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-240)

    - Next → [brightport_gunfryk17](#d-brightport_gunfryk17)

    <span id="d-brightport_gunfryk14"></span>**`brightport_gunfryk14`** Gunfryk: “That is understandable. I was a bit hopeful, we've long needed a reason to nail down the coffin of the remaining criminals in town.”

    - Next → [brightport_gunfryk15](#d-brightport_gunfryk15)

    <span id="d-brightport_gunfryk21"></span>**`brightport_gunfryk21`** Gunfryk: “That is understandable. I was a bit hopeful, we've long needed a reason to nail down the coffin of the remaining criminals in town.”

    - Next → [brightport_gunfryk22](#d-brightport_gunfryk22)

    <span id="d-brightport_gunfryk10"></span>**`brightport_gunfryk10`** Gunfryk: “I see, good luck with that.”


    <span id="d-brightport_gunfryk18"></span>**`brightport_gunfryk18`** [Dummy NPC](../monsters/none.md): “You're not sure if what you're feeling right now is guilt, or the feeling of breaking a promise.”

    - “[I do feel a little bad.]” → [brightport_gunfryk19](#d-brightport_gunfryk19)
    - “[They deserved it.]” → [brightport_gunfryk19](#d-brightport_gunfryk19)

    <span id="d-brightport_gunfryk12"></span>**`brightport_gunfryk12`** Gunfryk: “Well done, $playername. They will be apprehended as soon as I give my men the order. As for you, a reward is most deserving, here is some gold.”

    - Next → [brightport_gunfryk13](#d-brightport_gunfryk13)

    <span id="d-brightport_gunfryk_killfail"></span>**`brightport_gunfryk_killfail`** [Gunfryk](../monsters/brightport_gunfrykstill.md): “Is your friend safe?! I sent my men to the derelict manor and they caught a Nor city spy, but no trace of any lizardmen or your friend!” — **effects:** spawns monsters on brightport_jail

    - “Umm. Ermm. He is alright sir.” → [brightport_gunfryk_killfail2](#d-brightport_gunfryk_killfail2)

    <span id="d-brightport_gunfryk3"></span>**`brightport_gunfryk3`** Gunfryk: “What? [The commander gulps dryly.] Who told you that? And anyway, my favorites are orchids!” — **effects:** sets stage 150 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-150)

    - “I also heard you love rolling in the flower fields and smelling the roses. I think the others would love hearing that…” → [brightport_gunfryk4](#d-brightport_gunfryk4)

    <span id="d-brightport_gunfryk1"></span>**`brightport_gunfryk1`** Gunfryk: “Those Nor City agitators are a dime a dozen; however, we can only act under Feygard law. The first thing we need is evidence.”

    - “What could serve as evidence?” → [brightport_gunfryk6](#d-brightport_gunfryk6)

    <span id="d-brightport_gunfryk0"></span>**`brightport_gunfryk0`** Gunfryk: “We protect Brightport from the critters of the wilderness and barbaric monsters such as those lizardmen. All by decree of our king, Lord Geomyr.”

    - Next → [Brightport_gunfryk1](#d-Brightport_gunfryk1)

    <span id="d-brightport_gunfryk15"></span>**`brightport_gunfryk15`** Gunfryk: “This time was a miss, but we sure need more brave youngsters like you who are not afraid to speak up. Glory to Feygard!” — **effects:** sets stage 140 of [Priceful vengeance](../quests/brightport_goons.md#stage-140), sets stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139)


    <span id="d-brightport_gunfryk22"></span>**`brightport_gunfryk22`** Gunfryk: “This time was a miss, but we sure need more brave youngsters like you who are not afraid to speak up. Glory to Feygard!” — **effects:** sets stage 135 of [Priceful vengeance](../quests/brightport_goons.md#stage-135)


    <span id="d-brightport_gunfryk19"></span>**`brightport_gunfryk19`** [Gunfryk](../monsters/brightport_gunfrykstill.md): “We sure need more brave, law-upholding youngsters like you around! I'll make sure to write to my superiors about it. After graduating from the academy here, be sure to give the military academy a try. Glory to Feygard!” — **effects:** sets stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139), sets stage 150 of [Priceful vengeance](../quests/brightport_goons.md#stage-150), spawns monsters on brightport_benbyr, starts timer “brightport_arrest”, sets stage 120 of [Priceful vengeance](../quests/brightport_goons.md#stage-120), sets stage 212 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-212)

    - Next → [brightport_gunfryk20](#d-brightport_gunfryk20)

    <span id="d-brightport_gunfryk13"></span>**`brightport_gunfryk13`** [Gunfryk](../monsters/brightport_gunfrykstill.md): “We sure need more brave, law-upholding youngsters like you around! I'll make sure to write to my superiors about it. After graduating from the academy here, be sure to give the military academy a try. Glory to Feygard!” — **effects:** gives 700× [Gold coins](../items/gold.md), spawns monsters on brightport_benbyr, sets stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139), sets stage 120 of [Priceful vengeance](../quests/brightport_goons.md#stage-120), sets stage 212 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-212), starts timer “brightport_arrest”


    <span id="d-brightport_gunfryk_killfail2"></span>**`brightport_gunfryk_killfail2`** Gunfryk: “Then that is good, and if not for you we wouldn't have gone there and found that spy. You can have his cloak, well done.” — **effects:** sets stage 60 of [Boxed in](../quests/brightport_thieves.md#stage-60), sets stage 136 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-136), gives 1× [Agent's cloak](../items/brightport_cloak.md)

    - “[Elysa will be mad at me...]” → *conversation ends*

    <span id="d-brightport_gunfryk4"></span>**`brightport_gunfryk4`** Gunfryk: “Grr... This is blackmail. I get it. What is it? What do you want?”

    - “You've put my two acquaintances, Dynes and Barthold, in a tough spot with your rules. I'd appreciate it if you gave…” → [brightport_gunfryk5](#d-brightport_gunfryk5)

    <span id="d-brightport_gunfryk6"></span>**`brightport_gunfryk6`** Gunfryk: “Reputable eyewitnesses. Records. In case of swindling or smuggling, illegal merchandise. Word of mouth means nothing.”

    - “I think I heard them mention a smuggling cave of sorts, that they use to evade the law.” → [brightport_gunfryk7](#d-brightport_gunfryk7)

    <span id="d-Brightport_gunfryk1"></span>**`Brightport_gunfryk1`** Gunfryk: “With us around all those Nor City thugs are shaking in their boots, Brightport has never been safer.”


    <span id="d-brightport_gunfryk20"></span>**`brightport_gunfryk20`** [Dummy NPC](../monsters/none.md): “What is certain, however, is that if there's any honor among Nor City's thieves, they'll surely have none to spare for you.”


    <span id="d-brightport_gunfryk5"></span>**`brightport_gunfryk5`** Gunfryk: “Have it your way, and keep those papers away from my subordinates. If word got out, my reputation would be ruined! But don't think this will last for long...” — **effects:** sets stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60)


    <span id="d-brightport_gunfryk7"></span>**`brightport_gunfryk7`** Gunfryk: “As if they could ever evade the watchful eyes of my men! Although...”

    - Next → [brightport_gunfryk8](#d-brightport_gunfryk8)

    <span id="d-brightport_gunfryk8"></span>**`brightport_gunfryk8`** Gunfryk: “If you came here to tell me, there may be some truth to your words, kid. If you want to do the right thing for the glory of Feygard, then see if you can find anything I could order my men to act on. But don't stick your neck out too much,…” — **effects:** sets stage 80 of [Priceful vengeance](../quests/brightport_goons.md#stage-80)

    - “I'll do my best, Glory to Feygard!” → *conversation ends*
    - “Sure, but I'm doing this because I want to, not because of your silly laws.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 33 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_gunfrykstill.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_gunfrykstill.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_gunfrykstill.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_gunfrykstill.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `brightport_gunfrykstill` · Data from v0.8.18</small>
