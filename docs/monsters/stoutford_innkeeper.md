# ![](../assets/icons/monsters/monsters_ld1_33.png){ .sprite } Glasforn

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

- [stoutford_tavern](../maps/stoutford_tavern.md)

## Quests

- [Rumblings](../quests/rumblings.md): stages 30, 60, 70

??? quote "Dialogue (30 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-glasforn_0"></span>**`glasforn_0`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 103 of [Rumblings](../quests/rumblings.md#stage-103))* → [glasforn_rumblings103_0](#d-glasforn_rumblings103_0)
    - Next *(if reached stage 70 of [Rumblings](../quests/rumblings.md#stage-70))* → [glasforn_rumblings70_0](#d-glasforn_rumblings70_0)
    - Next *(if reached stage 60 of [Rumblings](../quests/rumblings.md#stage-60))* → [glasforn_rumblings60_0](#d-glasforn_rumblings60_0)
    - Next *(if reached stage 50 of [Rumblings](../quests/rumblings.md#stage-50))* → [glasforn_rumblings50_0](#d-glasforn_rumblings50_0)
    - Next *(if reached stage 30 of [Rumblings](../quests/rumblings.md#stage-30))* → [glasforn_rumblings30_0](#d-glasforn_rumblings30_0)
    - Next → [glasforn_initial_0](#d-glasforn_initial_0)

    <span id="d-glasforn_rumblings103_0"></span>**`glasforn_rumblings103_0`** Glasforn: “Boohoohoo ... the whole town hates me now. Even my dear customers left. Just the old hag who only drinks water stayed, and Lord Bourbon who never pays.”

    - “You deserved it.” → [glasforn_rumblings103_1](#d-glasforn_rumblings103_1)
    - “Well done.” → [glasforn_rumblings103_1](#d-glasforn_rumblings103_1)
    - “Whatever.” → *conversation ends*

    <span id="d-glasforn_rumblings70_0"></span>**`glasforn_rumblings70_0`** Glasforn: “That's all I know, I swear. Please spare me. You can use the bed safely now.” — **effects:** changes map stoutford_tavern

    - “I'll spare you. For now. But no more tricks. Or else...” → [glasforn_rumblings70_1](#d-glasforn_rumblings70_1)
    - “I guess this was all necessary.” → [glasforn_rumblings70_1](#d-glasforn_rumblings70_1)

    <span id="d-glasforn_rumblings60_0"></span>**`glasforn_rumblings60_0`** Glasforn: “Wait. OK. I stand no chance against you. I'll tell you all I know.” — **effects:** sets stage 60 of [Rumblings](../quests/rumblings.md#stage-60)

    - “It'd better be worth it.” → [glasforn_rumblings60_1](#d-glasforn_rumblings60_1)
    - “Go ahead.” → [glasforn_rumblings60_1](#d-glasforn_rumblings60_1)
    - “I'm all ears.” → [glasforn_rumblings60_1](#d-glasforn_rumblings60_1)

    <span id="d-glasforn_rumblings50_0"></span>**`glasforn_rumblings50_0`** Glasforn: “Wha... Impossible...! How did you...?”

    - “I should kill you right now!” → [glasforn_rumblings50_1](#d-glasforn_rumblings50_1)
    - “What was that beast?” → [glasforn_rumblings50_1](#d-glasforn_rumblings50_1)
    - “What did you do to me?” → [glasforn_rumblings50_1](#d-glasforn_rumblings50_1)

    <span id="d-glasforn_rumblings30_0"></span>**`glasforn_rumblings30_0`** Glasforn: “So kid, have you tried that bed? Our beds are the best!”

    - “About Andor...” → [glasforn_rumblings30_1](#d-glasforn_rumblings30_1)
    - “About those noises...” → [glasforn_rumblings30_1](#d-glasforn_rumblings30_1)
    - “Not yet.” → [glasforn_rumblings30_1](#d-glasforn_rumblings30_1)

    <span id="d-glasforn_initial_0"></span>**`glasforn_initial_0`** Glasforn: “Hello.”

    - “Who are you?” → [glasforn_initial_who_0](#d-glasforn_initial_who_0)
    - “Can I use one of your beds?” → [glasforn_initial_bed_0](#d-glasforn_initial_bed_0)
    - “What can you tell me about the strange noises in the church?” *(if reached stage 20 of [Rumblings](../quests/rumblings.md#stage-20))* → [glasforn_rumblings20_0](#d-glasforn_rumblings20_0)

    <span id="d-glasforn_rumblings103_1"></span>**`glasforn_rumblings103_1`** Glasforn: “Boohoohoo...”


    <span id="d-glasforn_rumblings70_1"></span>**`glasforn_rumblings70_1`** Glasforn: “I swear. You'll be my honored guest for life.”


    <span id="d-glasforn_rumblings60_1"></span>**`glasforn_rumblings60_1`** Glasforn: “It was Andor. He made us do it, and promised to rid us of the Shadow church if we helped.”

    - Next → [glasforn_rumblings60_2](#d-glasforn_rumblings60_2)

    <span id="d-glasforn_rumblings50_1"></span>**`glasforn_rumblings50_1`** Glasforn: “You ... you should be dead!”

    - “And so should you.” → [glasforn_rumblings60_0](#d-glasforn_rumblings60_0)
    - “Stop. Talk. Tell me everything.” → [glasforn_rumblings60_0](#d-glasforn_rumblings60_0)

    <span id="d-glasforn_rumblings30_1"></span>**`glasforn_rumblings30_1`** Glasforn: “You really should try that bed. You'll thank me afterwards.”


    <span id="d-glasforn_initial_who_0"></span>**`glasforn_initial_who_0`** Glasforn: “I'm Glasforn, proud owner of this fine establishment.”

    - “Can I use one of your beds?” → [glasforn_initial_bed_0](#d-glasforn_initial_bed_0)
    - “What can you tell me about the strange noises in the church?” *(if reached stage 20 of [Rumblings](../quests/rumblings.md#stage-20))* → [glasforn_rumblings20_0](#d-glasforn_rumblings20_0)

    <span id="d-glasforn_initial_bed_0"></span>**`glasforn_initial_bed_0`** Glasforn: “Sorry, none are available today.”

    - “Who are you?” → [glasforn_initial_who_0](#d-glasforn_initial_who_0)
    - “What can you tell me about the strange noises in the church?” *(if reached stage 20 of [Rumblings](../quests/rumblings.md#stage-20))* → [glasforn_rumblings20_0](#d-glasforn_rumblings20_0)

    <span id="d-glasforn_rumblings20_0"></span>**`glasforn_rumblings20_0`** Glasforn: “What about them?”

    - “Well, I heard they may be related to my brother Andor. I'm looking for him.” → [glasforn_rumblings20_1](#d-glasforn_rumblings20_1)

    <span id="d-glasforn_rumblings60_2"></span>**`glasforn_rumblings60_2`** Glasforn: “When he came, he asked me for a "private" place where he could do his weird stuff undisturbed. It had to be underground, and it had to be in the city. I have no idea why.” — **effects:** sets stage 86 of [andor (hidden flag)](../quests/andor.md#stage-86)

    - Next → [glasforn_rumblings60_3](#d-glasforn_rumblings60_3)

    <span id="d-glasforn_rumblings20_1"></span>**`glasforn_rumblings20_1`** Glasforn: “You indeed look a lot like him...”

    - Next → [glasforn_rumblings20_2](#d-glasforn_rumblings20_2)

    <span id="d-glasforn_rumblings60_3"></span>**`glasforn_rumblings60_3`** Glasforn: “I showed him the cellar under the old derelict house.”

    - Next → [glasforn_rumblings60_4](#d-glasforn_rumblings60_4)

    <span id="d-glasforn_rumblings20_2"></span>**`glasforn_rumblings20_2`** Glasforn: “OK, I can believe that you are Andor's sibling. You should have told me earlier!”

    - “Why?” → [glasforn_rumblings20_3](#d-glasforn_rumblings20_3)

    <span id="d-glasforn_rumblings60_4"></span>**`glasforn_rumblings60_4`** Glasforn: “I think he spent several days in there, as we didn't see him. Around that time, the rumbles in the church began and we knew he would be keeping his promise.”

    - Next → [glasforn_rumblings60_5](#d-glasforn_rumblings60_5)

    <span id="d-glasforn_rumblings20_3"></span>**`glasforn_rumblings20_3`** Glasforn: “Well, you see, I keep some beds for occasions like this one. You can use the one in the corner, near the painting, if you wish to rest.” — **effects:** sets stage 30 of [Rumblings](../quests/rumblings.md#stage-30)

    - “For free?” → [glasforn_rumblings20_4](#d-glasforn_rumblings20_4)
    - “Thanks.” → *conversation ends*
    - “About those noises...” → [glasforn_rumblings20_5](#d-glasforn_rumblings20_5)

    <span id="d-glasforn_rumblings60_5"></span>**`glasforn_rumblings60_5`** Glasforn: “When he returned he put this horrible necklace on me. He told me that thing in the cellar needed lives to grow stronger, and either I could give it those lives or the necklace would take mine.”

    - Next → [glasforn_rumblings60_5_1](#d-glasforn_rumblings60_5_1)

    <span id="d-glasforn_rumblings20_4"></span>**`glasforn_rumblings20_4`** Glasforn: “Sure.”

    - “Thank you.” → *conversation ends*

    <span id="d-glasforn_rumblings20_5"></span>**`glasforn_rumblings20_5`** Glasforn: “Oh, you'll definitely enjoy our beds. I'm very proud of them.”

    - “...yes but...” → [glasforn_rumblings20_6](#d-glasforn_rumblings20_6)

    <span id="d-glasforn_rumblings60_5_1"></span>**`glasforn_rumblings60_5_1`** Glasforn: “It was terrible! I could feel the necklace draining the life out of me, and the only thing that made me feel better was giving it another victim.”

    - “Why didn't you just take it off?” → [glasforn_rumblings60_5_2](#d-glasforn_rumblings60_5_2)

    <span id="d-glasforn_rumblings20_6"></span>**`glasforn_rumblings20_6`** Glasforn: “Our food isn't bad either. Go see our cook. He's weird, but does great work.”

    - “...” → *conversation ends*

    <span id="d-glasforn_rumblings60_5_2"></span>**`glasforn_rumblings60_5_2`** Glasforn: “I couldn't. When I tried, and failed, he laughed. He told me it was bound to that thing in the basement, which needed me to be its servant.”

    - Next → [glasforn_rumblings60_5_3](#d-glasforn_rumblings60_5_3)

    <span id="d-glasforn_rumblings60_5_3"></span>**`glasforn_rumblings60_5_3`** Glasforn: “Then he laughed some more, and told me that all I had to do was kill that thing, and I would be able to remove the necklace. I'm no fighter though. I was too scared to even go near it.”

    - “I guess you are lucky I visited, although just asking me to kill it would have been easier. And nicer.” → [glasforn_rumblings60_5_4](#d-glasforn_rumblings60_5_4)

    <span id="d-glasforn_rumblings60_5_4"></span>**`glasforn_rumblings60_5_4`** Glasforn: “I didn't dare. The evening after Andor left his companion returned briefly. He warned me you might come here, and that if you found out what I had done you would kill me. He told me that my only hope was to make you the next victim.”

    - Next → [glasforn_rumblings60_6](#d-glasforn_rumblings60_6)

    <span id="d-glasforn_rumblings60_6"></span>**`glasforn_rumblings60_6`** Glasforn: “I'm sorry! How was I to know you could actually kill it? You're just a kid! Anyway, now I can remove the necklace. Please take it. I never want to see it again.” — **effects:** gives 1× [Necklace of the Undead](../items/necklace_undead.md), sets stage 70 of [Rumblings](../quests/rumblings.md#stage-70)

    - Next → [glasforn_rumblings70_0](#d-glasforn_rumblings70_0)



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_innkeeper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_innkeeper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_innkeeper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_innkeeper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `stoutford_innkeeper` · Data from v0.8.18</small>
