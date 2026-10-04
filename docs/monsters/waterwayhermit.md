# ![](../assets/icons/monsters/monsters_ld1_30.png){ .sprite } Cithurn

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

- [waterwaybhouse](../maps/waterwaybhouse.md)

## Quests

- [Just the beginning](../quests/waterwayacave.md): stages 10, 12, 15, 20, 25, 30, 35, 60, 70
- [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md): stages 10, 90, 120

??? quote "Dialogue (28 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-cithurn_begin"></span>**`cithurn_begin`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 50 of [Trial by fire](../quests/charwood2.md#stage-50); reached stage 10 of [Just the beginning](../quests/waterwayacave.md#stage-10); NOT reached stage 35 of [Just the beginning](../quests/waterwayacave.md#stage-35))* → [cithurn_10](#d-cithurn_10)
    - Next *(if NOT reached stage 10 of [Just the beginning](../quests/waterwayacave.md#stage-10); NOT reached stage 90 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-90))* → [cithurn_00](#d-cithurn_00)
    - Next *(if reached stage 10 of [Just the beginning](../quests/waterwayacave.md#stage-10); NOT reached stage 12 of [Just the beginning](../quests/waterwayacave.md#stage-12); NOT reached stage 50 of [Trial by fire](../quests/charwood2.md#stage-50))* → [cithurn_64](#d-cithurn_64)
    - Next *(if reached stage 70 of [Just the beginning](../quests/waterwayacave.md#stage-70); NOT reached stage 120 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-120))* → [cithurn_110](#d-cithurn_110)
    - Next *(if NOT reached stage 90 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-90); NOT reached stage 70 of [Just the beginning](../quests/waterwayacave.md#stage-70))* → [cithurn_90](#d-cithurn_90)
    - Next *(if reached stage 90 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-90); NOT reached stage 10 of [Just the beginning](../quests/waterwayacave.md#stage-10))* → [cithurn_120](#d-cithurn_120)
    - Next *(if reached stage 10 of [Just the beginning](../quests/waterwayacave.md#stage-10); NOT reached stage 70 of [Just the beginning](../quests/waterwayacave.md#stage-70))* → [cithurn_90](#d-cithurn_90)
    - Next *(if reached stage 120 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-120))* → [cithurn_130](#d-cithurn_130)

    <span id="d-cithurn_10"></span>**`cithurn_10`** Cithurn: “The surrounding forest is usually quiet, but for some time now it has been under a monster invasion. I am surprised you managed to reach my home.” — **effects:** sets stage 15 of [Just the beginning](../quests/waterwayacave.md#stage-15)

    - Next → [cithurn_20](#d-cithurn_20)

    <span id="d-cithurn_00"></span>**`cithurn_00`** Cithurn: “You must not be from around here. If you were, you would know that it is impolite to barge into homes without invitation.”

    - “Sorry. I didn't mean to be rude. I'm $playername. I come from a small village where people tend to leave their doors…” → [cithurn_62](#d-cithurn_62)
    - “I'm looking for someone.” → [cithurn_80](#d-cithurn_80)

    <span id="d-cithurn_64"></span>**`cithurn_64`** Cithurn: “What's a kid like you doing around here? It's a dangerous place to be.”

    - “I'm looking for my brother, Andor. He looks a bit like me.” → [cithurn_65](#d-cithurn_65)
    - “Dangerous? Perhaps I can help?” *(if NOT reached stage 50 of [Trial by fire](../quests/charwood2.md#stage-50))* → [cithurn_66](#d-cithurn_66)
    - “Dangerous? Perhaps I can help?” *(if reached stage 50 of [Trial by fire](../quests/charwood2.md#stage-50); NOT reached stage 35 of [Just the beginning](../quests/waterwayacave.md#stage-35))* → [cithurn_10](#d-cithurn_10)

    <span id="d-cithurn_110"></span>**`cithurn_110`** Cithurn: “Have you come to return my talisman?”

    - “Yes. I changed my mind about keeping it.” *(if hand over 1× [Cithurn's talisman](../items/cithurn_talisman.md))* → [cithurn_111](#d-cithurn_111)
    - “No. I already told you that I am keeping it as payment for my work.” → [cithurn_112](#d-cithurn_112)

    <span id="d-cithurn_90"></span>**`cithurn_90`** Cithurn: “It is good to see you again $playername.”

    - “I explored the cave. You were correct. I found a monster called Tesrekan, which was similar to the one I found in the…” *(if reached stage 55 of [Just the beginning](../quests/waterwayacave.md#stage-55); carry 1× [Tesrekan's bone](../items/tesrekanbone.md))* → [cithurn_60](#d-cithurn_60)
    - “I think I need more help to be able to complete my mission.” *(if reached stage 50 of [Trial by fire](../quests/charwood2.md#stage-50); reached stage 35 of [Just the beginning](../quests/waterwayacave.md#stage-35); NOT reached stage 10 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-10))* → [cithurn_51](#d-cithurn_51)
    - “I haven't found out what is happening yet, but I wanted to let you know I'm still working on it.” *(if reached stage 50 of [Trial by fire](../quests/charwood2.md#stage-50); reached stage 10 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-10); NOT reached stage 55 of [Just the beginning](../quests/waterwayacave.md#stage-55))* → [cithurn_91](#d-cithurn_91)

    <span id="d-cithurn_120"></span>**`cithurn_120`** Cithurn: “You again? What do you want this time?”

    - “I wish to apologize. I'm $playername. I come from a small village where people tend to leave their doors open. I…” → [cithurn_62](#d-cithurn_62)
    - “Nothing. I'll leave now.” → *conversation ends*

    <span id="d-cithurn_130"></span>**`cithurn_130`** Cithurn: “Thanks for your help, but I don't think we have anything else to discuss.”


    <span id="d-cithurn_20"></span>**`cithurn_20`** Cithurn: “I heard something similar was occurring in Charwood until a young adventurer killed a vile beast in the mine beneath the city.” — **effects:** sets stage 20 of [Just the beginning](../quests/waterwayacave.md#stage-20)

    - “I was in Charwood recently and what you heard was true. [You describe your experiences in Charwood and the battle with…” → [cithurn_30](#d-cithurn_30)
    - “That is interesting, but I am supposed to be looking for my brother. I should leave.” → *conversation ends*

    <span id="d-cithurn_62"></span>**`cithurn_62`** Cithurn: “Well $playername, you are young, and you apologized, so perhaps I will be a little forgiving. Just remember that not everywhere is like your small village. My name is Cithurn.” — **effects:** sets stage 10 of [Just the beginning](../quests/waterwayacave.md#stage-10)

    - Next → [cithurn_63](#d-cithurn_63)

    <span id="d-cithurn_80"></span>**`cithurn_80`** Cithurn: “Well I'm the only one here. Perhaps you should leave. Come back when you have learned some manners.” — **effects:** sets stage 90 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-90)


    <span id="d-cithurn_65"></span>**`cithurn_65`** Cithurn: “Sorry. I haven't seen anyone like that.”

    - “Thanks. Maybe I can help you with whatever is dangerous around here?” *(if NOT reached stage 50 of [Trial by fire](../quests/charwood2.md#stage-50))* → [cithurn_66](#d-cithurn_66)
    - “Thanks. I need to get going.” → *conversation ends*
    - “Thanks. Maybe I can help you with whatever is dangerous around here?” *(if reached stage 50 of [Trial by fire](../quests/charwood2.md#stage-50); NOT reached stage 35 of [Just the beginning](../quests/waterwayacave.md#stage-35))* → [cithurn_10](#d-cithurn_10)

    <span id="d-cithurn_66"></span>**`cithurn_66`** Cithurn: “I don't think so. It would need an experienced fighter to help with this problem.” — **effects:** sets stage 12 of [Just the beginning](../quests/waterwayacave.md#stage-12)

    - “I have experience fighting.” → [cithurn_67](#d-cithurn_67)
    - “Fine. If I'm back around here sometime in the future maybe I'll offer my help again. Or maybe I won't.” → *conversation ends*

    <span id="d-cithurn_111"></span>**`cithurn_111`** Cithurn: “Thank you. It seems you do have more honor than I thought.” — **effects:** sets stage 120 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-120)


    <span id="d-cithurn_112"></span>**`cithurn_112`** Cithurn: “Then I have nothing to say to you.”


    <span id="d-cithurn_60"></span>**`cithurn_60`** Cithurn: “Was?”

    - “I killed the monster. I brought one of its bones as proof.” → [cithurn_61](#d-cithurn_61)

    <span id="d-cithurn_51"></span>**`cithurn_51`** Cithurn: “Here. Take this talisman. It does much to dispel evil forces. I acquired it long ago, and it has kept me safe over the years. Since you have agreed to help me I think your need is now greater than mine. My only request is that if you are…” — **effects:** gives 1× [Cithurn's talisman](../items/cithurn_talisman.md), sets stage 10 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-10)

    - Next → [cithurn_52](#d-cithurn_52)

    <span id="d-cithurn_91"></span>**`cithurn_91`** Cithurn: “OK. Thanks for keeping me updated. Please come back when you have more information.”


    <span id="d-cithurn_30"></span>**`cithurn_30`** Cithurn: “I do not know if it began happening here before the events in Charwood or after. However, from what you tell me, maybe there is a connection between the two.” — **effects:** sets stage 25 of [Just the beginning](../quests/waterwayacave.md#stage-25)

    - Next → [cithurn_40](#d-cithurn_40)

    <span id="d-cithurn_63"></span>**`cithurn_63`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 50 of [Trial by fire](../quests/charwood2.md#stage-50); NOT reached stage 35 of [Just the beginning](../quests/waterwayacave.md#stage-35); reached stage 10 of [Just the beginning](../quests/waterwayacave.md#stage-10))* → [cithurn_10](#d-cithurn_10)
    - branch 2 → [cithurn_64](#d-cithurn_64)

    <span id="d-cithurn_67"></span>**`cithurn_67`** Cithurn: “I will clarify. A more experienced fighter than you.”

    - “OK. I can take a hint.” → *conversation ends*

    <span id="d-cithurn_61"></span>**`cithurn_61`** Cithurn: “Well done! A thousand thanks young adventurer. I am in your debt. However, I would still like my talisman back. I need it to keep me safe.”

    - “Certainly. Here you are.” *(if hand over 1× [Cithurn's talisman](../items/cithurn_talisman.md); hand over 1× [Tesrekan's bone](../items/tesrekanbone.md))* → [cithurn_100](#d-cithurn_100)
    - “You are right about that debt. I think I'll keep the talisman as payment.” *(if hand over 1× [Tesrekan's bone](../items/tesrekanbone.md))* → [cithurn_101](#d-cithurn_101)

    <span id="d-cithurn_52"></span>**`cithurn_52`** Cithurn: “Good luck young adventurer. I await your return.”


    <span id="d-cithurn_40"></span>**`cithurn_40`** Cithurn: “There is a cave system that runs underneath the forest. If something sinister is afoot, it could be emanating from the ground below. Please, you must help me investigate the source of the monster invasion in this forest.” — **effects:** sets stage 30 of [Just the beginning](../quests/waterwayacave.md#stage-30)

    - “OK, I will help you.” → [cithurn_50](#d-cithurn_50)
    - “Sorry, I cannot help you right now.” → *conversation ends*
    - “How much "investigating" will you be doing in this proposed partnership?” → [cithurn_70](#d-cithurn_70)

    <span id="d-cithurn_100"></span>**`cithurn_100`** Cithurn: “Thank you. I see you are not just a great fighter, but also an adventurer that keeps his word.” — **effects:** sets stage 60 of [Just the beginning](../quests/waterwayacave.md#stage-60)


    <span id="d-cithurn_101"></span>**`cithurn_101`** Cithurn: “I see. You are apparently a great fighter, but not a very honorable one.” — **effects:** sets stage 70 of [Just the beginning](../quests/waterwayacave.md#stage-70)


    <span id="d-cithurn_50"></span>**`cithurn_50`** Cithurn: “Thank you. You will have to pass through the forest to reach an opening to the cave where you can enter. The opening is roughly east of my home.” — **effects:** sets stage 35 of [Just the beginning](../quests/waterwayacave.md#stage-35)

    - Next → [cithurn_51](#d-cithurn_51)

    <span id="d-cithurn_70"></span>**`cithurn_70`** Cithurn: “Hmm ... I'll work on the parts that aren't dangerous. A brave and expert fighter like yourself is better suited to the dangerous parts.”

    - “Danger is my middle name! I'll help you.” → [cithurn_50](#d-cithurn_50)
    - “Sorry. Flattery will not persuade me to risk my life for some piece of forest with one old man living in it.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 28 lines added |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=waterwayhermit.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=waterwayhermit.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=waterwayhermit.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=waterwayhermit.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `waterwayhermit` · Data from v0.8.18</small>
