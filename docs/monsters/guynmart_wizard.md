# ![](../assets/icons/monsters/monsters_ld1_30.png){ .sprite } Rorthron

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
| [Mundane ring](../items/ring1.md) | 100% | 1 |
| [Jinxed ring of damage resistance](../items/ring_jinxed1.md) | 100% | 1 |
| [Ring of damage +1](../items/ring_dmg1.md) | 100% | 1 |
| [Ring of damage +2](../items/ring_dmg2.md) | 100% | 1 |

## Found on

- [guynmart_tower_4](../maps/guynmart_tower_4.md)

## Quests

- [Ringmaker (hidden flag)](../quests/guynmart_quest_wizard.md): stages 1, 2, 100

??? quote "Dialogue (18 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guynmart_wizard_10"></span>**`guynmart_wizard_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 12 of [Ringmaker (hidden flag)](../quests/guynmart_quest_wizard.md#stage-12))* → [guynmart_wizard_20](#d-guynmart_wizard_20)
    - branch 2 → [guynmart_wizard_12](#d-guynmart_wizard_12)

    <span id="d-guynmart_wizard_20"></span>**`guynmart_wizard_20`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 190444 of [Roses](../quests/guynmart.md#stage-190444))* → [guynmart_wizard_24](#d-guynmart_wizard_24)
    - branch 2 *(if carry 1× [Ring of lesser Shadow](../items/ring_shadow0.md))* → [guynmart_wizard_40](#d-guynmart_wizard_40)
    - branch 3 *(if wearing [Ring of lesser Shadow](../items/ring_shadow0.md))* → [guynmart_wizard_30](#d-guynmart_wizard_30)
    - branch 4 → [guynmart_wizard_21](#d-guynmart_wizard_21)

    <span id="d-guynmart_wizard_12"></span>**`guynmart_wizard_12`** Rorthron: “It is dangerous here. Please stay outside, in front of the signs on the floor, and wait there. I will be with you in a minute.”


    <span id="d-guynmart_wizard_24"></span>**`guynmart_wizard_24`** Rorthron: “Maybe you want to look at my fine collection of rings? Unfortunately I have no ring of real power available just now. But I sell them for a good price.”

    - “Certainly. Show me your rings.” → *shop opens*
    - “Not right now, thanks.” → *conversation ends*

    <span id="d-guynmart_wizard_40"></span>**`guynmart_wizard_40`** Rorthron: “Be welcome, $playername. I am Rorthron, the world's most famous ringmaker. I know Andor, your brother. He sometimes consulted me about newly found rings.”

    - “You know me? And my brother?” → [guynmart_wizard_42](#d-guynmart_wizard_42)
    - “I never met a ringmaker.” → [guynmart_wizard_24](#d-guynmart_wizard_24)
    - “Andor! Do you know where he was bound?” → [guynmart_wizard_28](#d-guynmart_wizard_28)

    <span id="d-guynmart_wizard_30"></span>**`guynmart_wizard_30`** Rorthron: “Ah - just one thing: I know the power some rings can have, and I would prefer you took yours off in my presence.”

    - “OK, just a second.” → *conversation ends*

    <span id="d-guynmart_wizard_21"></span>**`guynmart_wizard_21`** Rorthron: “Welcome, $playername. I am Rorthron, the world's most famous ringmaker. I know Andor, your brother. He sometimes consulted me about newly found rings.”

    - “I have never met a ringmaker.” → [guynmart_wizard_24](#d-guynmart_wizard_24)
    - “Andor! Do you know where he was bound?” → [guynmart_wizard_28](#d-guynmart_wizard_28)

    <span id="d-guynmart_wizard_42"></span>**`guynmart_wizard_42`** Rorthron: “You and Andor are different. You will be legendary. Well do I know your deeds! And I even heard rumors that you gained the legends of legends, the mighty Ring of lesser Shadow!”

    - Next → [guynmart_wizard_50](#d-guynmart_wizard_50)

    <span id="d-guynmart_wizard_28"></span>**`guynmart_wizard_28`** Rorthron: “No, sorry. I tend not to ask about things that are personal.”

    - “That's a pity. I have been trailing my big brother for quite some time.” *(if carry 1× [Ring of lesser Shadow](../items/ring_shadow0.md))* → [guynmart_wizard_42](#d-guynmart_wizard_42)
    - “What do you know about magic rings?” → [guynmart_wizard_22](#d-guynmart_wizard_22)

    <span id="d-guynmart_wizard_50"></span>**`guynmart_wizard_50`** Rorthron: “With the help of some bonemeal potions I could improve it to be an even greater ring. The powers will be similar but greater. It will become the ** Ring of far lesser Shadow ** You are lucky indeed.”

    - “Really?” → [guynmart_wizard_54](#d-guynmart_wizard_54)

    <span id="d-guynmart_wizard_22"></span>**`guynmart_wizard_22`** Rorthron: “A lot. If ever you find one of the strong, old rings, come and show it to me. I might enhance it for you, as I already did for Andor. Don't forget to bring some bonemeal potions as a sign of friendship.”

    - “Thank you. I will remember.” → [guynmart_wizard_24](#d-guynmart_wizard_24)

    <span id="d-guynmart_wizard_54"></span>**`guynmart_wizard_54`** Rorthron: “Really. When my work is done, your ring will be stronger than ever.”

    - “Great! I didn't know that the ring lore has not been totally forgotten.” → [guynmart_wizard_56](#d-guynmart_wizard_56)
    - “Hmm, I like my ring the way it is.” → *conversation ends*
    - “Do you have any rings in stock?” → [guynmart_wizard_24](#d-guynmart_wizard_24)

    <span id="d-guynmart_wizard_56"></span>**`guynmart_wizard_56`** Rorthron: “Eleven should be OK.”

    - “Eleven what?” → [guynmart_wizard_58](#d-guynmart_wizard_58)

    <span id="d-guynmart_wizard_58"></span>**`guynmart_wizard_58`** Rorthron: “Eleven bonemeal potions of course. I need these potions for, eh, my work.”

    - Next → [guynmart_wizard_60](#d-guynmart_wizard_60)

    <span id="d-guynmart_wizard_60"></span>**`guynmart_wizard_60`** Rorthron: “Now to work - put the ring into the golden vessel here.”

    - “Thank you for your offer Rorthron. Here is the ring - be careful with it.” *(if hand over 1× [Ring of lesser Shadow](../items/ring_shadow0.md))* → [guynmart_wizard_70](#d-guynmart_wizard_70)
    - “No, I would never give you my ring.” → *conversation ends*

    <span id="d-guynmart_wizard_70"></span>**`guynmart_wizard_70`** Rorthron: “Oops!” — **effects:** gives [Ring of far lesser Shadow](../items/ring_shadow1.md), sets stage 1 of [Ringmaker (hidden flag)](../quests/guynmart_quest_wizard.md#stage-1), sets stage 2 of [Ringmaker (hidden flag)](../quests/guynmart_quest_wizard.md#stage-2), sets stage 100 of [Ringmaker (hidden flag)](../quests/guynmart_quest_wizard.md#stage-100)

    - “Oops? What does "oops" mean? Something went wrong?” → [guynmart_wizard_72](#d-guynmart_wizard_72)

    <span id="d-guynmart_wizard_72"></span>**`guynmart_wizard_72`** Rorthron: “Oh no, it is nothing. All is ... well, perfect. Yes. Now go, go and leave me, I have work to do. No need to thank me. Farewell.”

    - Next → [guynmart_wizard_74](#d-guynmart_wizard_74)

    <span id="d-guynmart_wizard_74"></span>**`guynmart_wizard_74`** Rorthron: “Forget the bonemeal potions. You owe me nothing. Farewell now.”




## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_wizard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_wizard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_wizard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_wizard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `guynmart_wizard` · Data from v0.8.18</small>
