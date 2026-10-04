# ![](../assets/icons/monsters/monsters_ld1_0.png){ .sprite } Guynmart guard

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
| [Gold coins](../items/gold.md) | 100% | 12 |

## Found on

- [guynmart](../maps/guynmart.md)

## Quests

- [Roses](../quests/guynmart.md): stages 30, 32
- [gardenGuard blocks (hidden flag)](../quests/guynmart_quest_gguard.md): stages 1, 82

??? quote "Dialogue (43 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guynmart_gguard_10"></span>**`guynmart_gguard_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 1 of [gardenGuard blocks (hidden flag)](../quests/guynmart_quest_gguard.md#stage-1))* → [guynmart_gguard_919](#d-guynmart_gguard_919)
    - branch 2 *(if reached stage 170 of [Roses](../quests/guynmart.md#stage-170); reached stage 2 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-2))* → [guynmart_gguard_400](#d-guynmart_gguard_400)
    - branch 3 *(if reached stage 70 of [Roses](../quests/guynmart.md#stage-70))* → [guynmart_gguard_220](#d-guynmart_gguard_220)
    - branch 4 → [guynmart_gguard_20](#d-guynmart_gguard_20)

    <span id="d-guynmart_gguard_919"></span>**`guynmart_gguard_919`** Guynmart guard: “...nine...”

    - Next → [guynmart_gguard_919](#d-guynmart_gguard_919)

    <span id="d-guynmart_gguard_400"></span>**`guynmart_gguard_400`** Guynmart guard: “No trespassing! Especially for kids!”

    - “Tell me, did many people pass by today?” → [guynmart_gguard_410](#d-guynmart_gguard_410)

    <span id="d-guynmart_gguard_220"></span>**`guynmart_gguard_220`** Guynmart guard: “No trespassing! Especially for kids!”

    - “Here are 100 gold.” → [guynmart_gguard_248](#d-guynmart_gguard_248)
    - “Do you not know me anymore? I've already given you enough gold.” → [guynmart_gguard_242](#d-guynmart_gguard_242)
    - “I would like to pass through again.” → [guynmart_gguard_250](#d-guynmart_gguard_250)
    - “May I pick a rose?” *(if NOT carry 1× [Rose](../items/guynmart_rose.md); NOT reached stage 100 of [Roses](../quests/guynmart.md#stage-100))* → [guynmart_gguard_350](#d-guynmart_gguard_350)

    <span id="d-guynmart_gguard_20"></span>**`guynmart_gguard_20`** Guynmart guard: “No trespassing! Especially for kids!”

    - “Here is 100 gold.” *(if reached stage 30 of [Roses](../quests/guynmart.md#stage-30); pay 100 gold)* → [guynmart_gguard_900](#d-guynmart_gguard_900)
    - “Who are you?” → [guynmart_gguard_30](#d-guynmart_gguard_30)
    - “What are you doing here?” → [guynmart_gguard_40](#d-guynmart_gguard_40)
    - “I just want to pass through.” → [guynmart_gguard_22](#d-guynmart_gguard_22)
    - “May I pick a rose?” → [guynmart_gguard_50](#d-guynmart_gguard_50)

    <span id="d-guynmart_gguard_410"></span>**`guynmart_gguard_410`** Guynmart guard: “Now that you mention it - not a single one. Bad business today.”

    - “No wonder with the main gate open.” → [guynmart_gguard_420](#d-guynmart_gguard_420)

    <span id="d-guynmart_gguard_248"></span>**`guynmart_gguard_248`** Guynmart guard: “Well, everything is getting more expensive nowadays. So 200 pieces of gold, please.”

    - “Here is 200 gold.” *(if pay 200 gold)* → [guynmart_gguard_900](#d-guynmart_gguard_900)
    - “Forget it. This is outrageous.” → *conversation ends*

    <span id="d-guynmart_gguard_242"></span>**`guynmart_gguard_242`** Guynmart guard: “Gold can never be enough. So it is 200 pieces of gold now.”

    - Next → [guynmart_gguard_244](#d-guynmart_gguard_244)

    <span id="d-guynmart_gguard_250"></span>**`guynmart_gguard_250`** Guynmart guard: “I am not allowed to let anyone in or out. And I am incorruptable below 200 pieces of gold.”

    - “Here is 200 gold.” *(if pay 200 gold)* → [guynmart_gguard_900](#d-guynmart_gguard_900)
    - “Well, I will really look for another entrance now.” → *conversation ends*
    - “200 gold? Last time it was 100 gold.” → [guynmart_gguard_248](#d-guynmart_gguard_248)
    - “Sorry, I don't have that much gold with me.” → [guynmart_gguard_930](#d-guynmart_gguard_930)

    <span id="d-guynmart_gguard_350"></span>**`guynmart_gguard_350`** Guynmart guard: “Pick? A rose? You? No way! All flowers in this garden are the personal property of Lady Hannah.”

    - “Come on. With so many plants she will not miss a single flower.” → [guynmart_gguard_70](#d-guynmart_gguard_70)
    - “But Lady Hannah herself told me to get her one.” *(if NOT reached stage 132 of [Roses](../quests/guynmart.md#stage-132))* → [guynmart_gguard_360](#d-guynmart_gguard_360)

    <span id="d-guynmart_gguard_900"></span>**`guynmart_gguard_900`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 1 of [gardenGuard blocks (hidden flag)](../quests/guynmart_quest_gguard.md#stage-1), sets stage 30 of [Roses](../quests/guynmart.md#stage-30)

    - branch 1 *(if NOT reached stage 10 of [Roses](../quests/guynmart.md#stage-10); NOT reached stage 32 of [Roses](../quests/guynmart.md#stage-32))* → [guynmart_gguard_902](#d-guynmart_gguard_902)
    - branch 2 → [guynmart_gguard_910](#d-guynmart_gguard_910)

    <span id="d-guynmart_gguard_30"></span>**`guynmart_gguard_30`** Guynmart guard: “Mind your own business. I hate kids. Just disappear!”

    - “Wait!” → [guynmart_gguard_20](#d-guynmart_gguard_20)
    - “OK, I'll leave.” → *conversation ends*

    <span id="d-guynmart_gguard_40"></span>**`guynmart_gguard_40`** Guynmart guard: “I am standing around kicking my heels and answering stupid questions.”

    - “Here is 100 gold.” *(if reached stage 30 of [Roses](../quests/guynmart.md#stage-30); pay 100 gold)* → [guynmart_gguard_900](#d-guynmart_gguard_900)
    - “Who are you?” → [guynmart_gguard_30](#d-guynmart_gguard_30)
    - “What are you doing here?” → [guynmart_gguard_40](#d-guynmart_gguard_40)
    - “I want to pass through.” → [guynmart_gguard_22](#d-guynmart_gguard_22)
    - “May I pick a rose?” → [guynmart_gguard_50](#d-guynmart_gguard_50)

    <span id="d-guynmart_gguard_22"></span>**`guynmart_gguard_22`** Guynmart guard: “I am not allowed to let anyone in or out. And I am incorruptable below 100 pieces of gold.”

    - “Here is 100 gold.” *(if pay 100 gold)* → [guynmart_gguard_900](#d-guynmart_gguard_900)
    - “Well, I think I'll look for another entrance.” → *conversation ends*
    - “Sorry, I don't have that much gold with me.” → [guynmart_gguard_930](#d-guynmart_gguard_930)

    <span id="d-guynmart_gguard_50"></span>**`guynmart_gguard_50`** Guynmart guard: “Pick? A rose? You? No way! All flowers in this garden are the personal property of Lady Hannah.”

    - “Who is Lady Hannah?” → [guynmart_gguard_60](#d-guynmart_gguard_60)
    - “Come on. With so many plants she will not miss a single flower.” → [guynmart_gguard_70](#d-guynmart_gguard_70)

    <span id="d-guynmart_gguard_420"></span>**`guynmart_gguard_420`** Guynmart guard: “Ah, that is why. OK. I am not allowed to let anyone in or out. And I am incorruptable below 2 pieces of gold.”

    - “Here is 2 gold.” *(if pay 2 gold)* → [guynmart_gguard_900](#d-guynmart_gguard_900)
    - “You never give up, do you?” → *conversation ends*

    <span id="d-guynmart_gguard_244"></span>**`guynmart_gguard_244`** Guynmart guard: “So do you want to go through or not?”

    - “Outrageous! But OK, here is 200 gold.” *(if pay 200 gold)* → [guynmart_gguard_900](#d-guynmart_gguard_900)
    - “I have to think about it.” → *conversation ends*

    <span id="d-guynmart_gguard_930"></span>**`guynmart_gguard_930`** Guynmart guard: “Hmm, you may have not enough money, but you have some nice things with you. I might give you a good price.”

    - “We'll see. Let's have a look at my belongings.” → *shop opens*
    - “I would rather starve here on the spot than sell you a single thing.” → *conversation ends*

    <span id="d-guynmart_gguard_70"></span>**`guynmart_gguard_70`** Guynmart guard: “Hannah knows every single plant in her garden. Nobody but herself and old Nuik may touch the plants.”

    - “Who is Nuik again?” → [guynmart_gguard_80](#d-guynmart_gguard_80)

    <span id="d-guynmart_gguard_360"></span>**`guynmart_gguard_360`** Guynmart guard: “Anyone could say that. But maybe...”

    - “Yes?” → [guynmart_gguard_362](#d-guynmart_gguard_362)

    <span id="d-guynmart_gguard_902"></span>**`guynmart_gguard_902`** Guynmart guard: “[Gold taken] Very good. Before you enter maybe you should also know the family names: Lord Guynmart, his beautiful but complicated daughter Hannah and his annoying son Rob. Got it?” — **effects:** sets stage 32 of [Roses](../quests/guynmart.md#stage-32)

    - Next → [guynmart_gguard_904](#d-guynmart_gguard_904)

    <span id="d-guynmart_gguard_910"></span>**`guynmart_gguard_910`** Guynmart guard: “[Gold taken] Very good. I will close my eyes now and count to 10.”

    - Next → [guynmart_gguard_911](#d-guynmart_gguard_911)

    <span id="d-guynmart_gguard_60"></span>**`guynmart_gguard_60`** Guynmart guard: “Hannah is Guynmart's daughter.”

    - “May I pick a rose?” → [guynmart_gguard_50](#d-guynmart_gguard_50)
    - “And Guynmart is...?” → [guynmart_gguard_90](#d-guynmart_gguard_90)
    - “Guynmart has a daughter?” → [guynmart_gguard_100](#d-guynmart_gguard_100)

    <span id="d-guynmart_gguard_80"></span>**`guynmart_gguard_80`** Guynmart guard: “Nuik has been a gardener here for as long as I can remember. And now disappear!”

    - “I have another question.” → [guynmart_gguard_10](#d-guynmart_gguard_10)
    - “OK, OK, I'll leave.” → *conversation ends*

    <span id="d-guynmart_gguard_362"></span>**`guynmart_gguard_362`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if have 100 gold)* → [guynmart_gguard_370](#d-guynmart_gguard_370)
    - branch 2 → [guynmart_gguard_364](#d-guynmart_gguard_364)

    <span id="d-guynmart_gguard_904"></span>**`guynmart_gguard_904`** Guynmart guard: “Rob is always playing some stupid game, and Hannah is always having problems. See?”

    - “Ah.” → [guynmart_gguard_906](#d-guynmart_gguard_906)

    <span id="d-guynmart_gguard_911"></span>**`guynmart_gguard_911`** Guynmart guard: “...one...”

    - Next → [guynmart_gguard_912](#d-guynmart_gguard_912)

    <span id="d-guynmart_gguard_90"></span>**`guynmart_gguard_90`** Guynmart guard: “Don't you know anything? Guynmart has been Lord of Guynmart castle for as long as I remember. His wife died early, during the birth of their daughter.”

    - “Guynmart has a daughter?” → [guynmart_gguard_100](#d-guynmart_gguard_100)

    <span id="d-guynmart_gguard_100"></span>**`guynmart_gguard_100`** Guynmart guard: “Hannah's beauty is well known all over the country. Many young men asked to marry her. But she only has eyes for Lovis.”

    - “Ah.” → [guynmart_gguard_110](#d-guynmart_gguard_110)
    - “And who is Lovis?” → [guynmart_gguard_110](#d-guynmart_gguard_110)
    - “This is getting boring.” → [guynmart_gguard_110](#d-guynmart_gguard_110)

    <span id="d-guynmart_gguard_370"></span>**`guynmart_gguard_370`** Guynmart guard: “for 100 gold...”

    - “I understand. Here, 100 gold.” *(if pay 100 gold)* → [guynmart_gguard_380](#d-guynmart_gguard_380)
    - “Oh you greedy, filthy, ...” → *conversation ends*

    <span id="d-guynmart_gguard_364"></span>**`guynmart_gguard_364`** Guynmart guard: “Nothing. You don't seem to have enough money. Forget it.”

    - “Oh.” → *conversation ends*

    <span id="d-guynmart_gguard_906"></span>**`guynmart_gguard_906`** Guynmart guard: “Enough talk. No trespassing! I will close my eyes now and count to 10.”

    - Next → [guynmart_gguard_911](#d-guynmart_gguard_911)

    <span id="d-guynmart_gguard_912"></span>**`guynmart_gguard_912`** Guynmart guard: “...two...”

    - Next → [guynmart_gguard_913](#d-guynmart_gguard_913)

    <span id="d-guynmart_gguard_110"></span>**`guynmart_gguard_110`** Guynmart guard: “Lovis is a good boy. I have not seen him for a while.”

    - “Whatever.” → [guynmart_gguard_120](#d-guynmart_gguard_120)
    - “La la la ... I'm not listening anymore...” → [guynmart_gguard_120](#d-guynmart_gguard_120)

    <span id="d-guynmart_gguard_380"></span>**`guynmart_gguard_380`** Guynmart guard: “And here is the rose. Don't tell anybody that you got it from me.” — **effects:** gives [Rose](../items/guynmart_rose.md), sets stage 82 of [gardenGuard blocks (hidden flag)](../quests/guynmart_quest_gguard.md#stage-82)

    - “OK.” → *conversation ends*
    - “Hmm, we will see.” → *conversation ends*

    <span id="d-guynmart_gguard_913"></span>**`guynmart_gguard_913`** Guynmart guard: “...three...”

    - Next → [guynmart_gguard_914](#d-guynmart_gguard_914)

    <span id="d-guynmart_gguard_120"></span>**`guynmart_gguard_120`** Guynmart guard: “But when Lovis is back, I am sure he will marry Hannah immediately.”

    - “This is all very interesting. Are you letting me through now?” → [guynmart_gguard_130](#d-guynmart_gguard_130)

    <span id="d-guynmart_gguard_914"></span>**`guynmart_gguard_914`** Guynmart guard: “...four...”

    - Next → [guynmart_gguard_915](#d-guynmart_gguard_915)

    <span id="d-guynmart_gguard_130"></span>**`guynmart_gguard_130`** Guynmart guard: “What? No, of course not!”

    - Next → [guynmart_gguard_10](#d-guynmart_gguard_10)

    <span id="d-guynmart_gguard_915"></span>**`guynmart_gguard_915`** Guynmart guard: “...five...”

    - Next → [guynmart_gguard_916](#d-guynmart_gguard_916)

    <span id="d-guynmart_gguard_916"></span>**`guynmart_gguard_916`** Guynmart guard: “...six...”

    - Next → [guynmart_gguard_917](#d-guynmart_gguard_917)

    <span id="d-guynmart_gguard_917"></span>**`guynmart_gguard_917`** Guynmart guard: “...eh, now seven, I think...”

    - Next → [guynmart_gguard_918](#d-guynmart_gguard_918)

    <span id="d-guynmart_gguard_918"></span>**`guynmart_gguard_918`** Guynmart guard: “...eight...”

    - Next → [guynmart_gguard_919](#d-guynmart_gguard_919)



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 43 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_gguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_gguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_gguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_gguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `guynmart_gguard` · Data from v0.8.18</small>
