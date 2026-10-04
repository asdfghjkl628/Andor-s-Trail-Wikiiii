# ![](../assets/icons/monsters/monsters_ld1_3.png){ .sprite } Tahalendor

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

- [stoutford_church](../maps/stoutford_church.md)

## Quests

- [Rumblings](../quests/rumblings.md): stages 10, 90, 100, 103, 106
- [Stoutford's old castle](../quests/stoutford_castle.md): stages 14
- [The thorns of vengeance](../quests/thorns_vengeance.md): stages 65
- [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md): stages 23

??? quote "Dialogue (25 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-tahalendor_0"></span>**`tahalendor_0`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 106 of [Rumblings](../quests/rumblings.md#stage-106))* → [tahalendor_rumblings10x_0](#d-tahalendor_rumblings10x_0)
    - Next *(if reached stage 103 of [Rumblings](../quests/rumblings.md#stage-103))* → [tahalendor_rumblings10x_0](#d-tahalendor_rumblings10x_0)
    - Next *(if reached stage 100 of [Rumblings](../quests/rumblings.md#stage-100))* → [tahalendor_rumblings10x_0](#d-tahalendor_rumblings10x_0)
    - Next *(if reached stage 90 of [Rumblings](../quests/rumblings.md#stage-90))* → [tahalendor_rumblings90_0](#d-tahalendor_rumblings90_0)
    - Next *(if reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80))* → [tahalendor_rumblings80_0](#d-tahalendor_rumblings80_0)
    - Next → [tahalendor_initial_0](#d-tahalendor_initial_0)

    <span id="d-tahalendor_rumblings10x_0"></span>**`tahalendor_rumblings10x_0`** Tahalendor: “Go with the shadow child.”

    - “Shadow be with you.” → *conversation ends*
    - “Whatever.” → *conversation ends*
    - “Would you come with me to talk to Blornvale? He wants to confess something important.” *(if reached stage 50 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-50); NOT reached stage 65 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-65); NOT reached stage 74 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-74))* → [tahalendor_thorns50](#d-tahalendor_thorns50)
    - “Yolgen told me that you could provide me with an artifact that could be used against powerful undead.” *(if reached stage 12 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-12); NOT reached stage 14 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-14))* → [tahalendor_erwyn_1](#d-tahalendor_erwyn_1)
    - “Do you have anything to trade?” → [tahalendor_rumblings10x_1](#d-tahalendor_rumblings10x_1)
    - “I need some help finding out who is responsible for casting a Shadow spell that causes a person to become noticeable.” *(if reached stage 50 of [Troubling times](../quests/troubling_times.md#stage-50); NOT reached stage 70 of [Troubling times](../quests/troubling_times.md#stage-70))* → [tt_tahalendor_10](#d-tt_tahalendor_10)

    <span id="d-tahalendor_rumblings90_0"></span>**`tahalendor_rumblings90_0`** Tahalendor: “Thank you for your help. Do you have any idea who might be responsible for all this?”

    - “Not really.” → [tahalendor_rumblings100_0](#d-tahalendor_rumblings100_0)
    - “It was all Glasforn's doing. The tavern owner.” *(if reached stage 70 of [Rumblings](../quests/rumblings.md#stage-70))* → [tahalendor_rumblings103_0](#d-tahalendor_rumblings103_0)
    - “It was my brother Andor. I need to find him.” *(if reached stage 70 of [Rumblings](../quests/rumblings.md#stage-70))* → [tahalendor_rumblings106_0](#d-tahalendor_rumblings106_0)

    <span id="d-tahalendor_rumblings80_0"></span>**`tahalendor_rumblings80_0`** Tahalendor: “You! You saved us!”

    - “No thanks to you...” → [tahalendor_rumblings80_1](#d-tahalendor_rumblings80_1)
    - “Indeed.” → [tahalendor_rumblings80_1](#d-tahalendor_rumblings80_1)
    - “That was the right thing to do.” → [tahalendor_rumblings80_1](#d-tahalendor_rumblings80_1)
    - “Would you come with me to talk to Blornvale? He wants to confess something important.” *(if reached stage 50 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-50); NOT reached stage 65 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-65); NOT reached stage 74 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-74))* → [tahalendor_thorns50](#d-tahalendor_thorns50)

    <span id="d-tahalendor_initial_0"></span>**`tahalendor_initial_0`** Tahalendor: “How dare you come back here after all you've done?”

    - “What?” → [tahalendor_initial_1](#d-tahalendor_initial_1)
    - “Actually, it's the first time we have met.” → [tahalendor_initial_2](#d-tahalendor_initial_2)
    - “I need you as a witness for...” *(if reached stage 50 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-50); NOT reached stage 65 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-65); NOT reached stage 74 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-74))* → [tahalendor_initial_1](#d-tahalendor_initial_1)

    <span id="d-tahalendor_thorns50"></span>**`tahalendor_thorns50`** Tahalendor: “If I must. Well, go ahead, I'll be there when you get there.” — **effects:** sets stage 65 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-65)


    <span id="d-tahalendor_erwyn_1"></span>**`tahalendor_erwyn_1`** Tahalendor: “What are you talking about?”

    - “I met an undead lord in the castle, but every time it seems that I have destroyed him, he rises again. Do you have any…” *(if killed 1× [Lord Erwyn](../monsters/erwyn.md))* → [tahalendor_erwyn_2](#d-tahalendor_erwyn_2)
    - “I want to help you clean the castle of the undead. Yolgen seems to be worried, perhaps because he believes the undead…” *(if NOT killed 1× [Lord Erwyn](../monsters/erwyn.md))* → [tahalendor_erwyn_2](#d-tahalendor_erwyn_2)

    <span id="d-tahalendor_rumblings10x_1"></span>**`tahalendor_rumblings10x_1`** Tahalendor: “Talk to Yolgen. He handles such things for me.” — **effects:** sets stage 23 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-23)

    - “OK. Thanks.” → *conversation ends*

    <span id="d-tt_tahalendor_10"></span>**`tt_tahalendor_10`** Tahalendor: “Eh, what? Better ask Yolgen.”


    <span id="d-tahalendor_rumblings100_0"></span>**`tahalendor_rumblings100_0`** Tahalendor: “It's a shame we cannot punish the culprits. Thank you for your help kid.” — **effects:** sets stage 100 of [Rumblings](../quests/rumblings.md#stage-100)


    <span id="d-tahalendor_rumblings103_0"></span>**`tahalendor_rumblings103_0`** Tahalendor: “That fool! We'll make him pay. Thank you for your help kid.” — **effects:** sets stage 103 of [Rumblings](../quests/rumblings.md#stage-103), removes monsters from stoutford_tavern


    <span id="d-tahalendor_rumblings106_0"></span>**`tahalendor_rumblings106_0`** Tahalendor: “That is troublesome. I have no idea where he went when he left Stoutford, but Kazaul has always been linked to the Undertell, south of here. Thank you for your help kid.” — **effects:** sets stage 106 of [Rumblings](../quests/rumblings.md#stage-106)

    - Next → [tahalendor_rumblings10x_0](#d-tahalendor_rumblings10x_0)

    <span id="d-tahalendor_rumblings80_1"></span>**`tahalendor_rumblings80_1`** Tahalendor: “My sincerest apologies for earlier. I took you for someone else. Do you know what was causing the rumbles?”

    - “[Show Demon heart] Some monster. Here's what it left when I killed it.” *(if carry 1× [Demon heart](../items/eliszylae_heart.md))* → [tahalendor_rumblings80_2](#d-tahalendor_rumblings80_2)
    - “Not really...” → [tahalendor_rumblings80_2bis](#d-tahalendor_rumblings80_2bis)

    <span id="d-tahalendor_initial_1"></span>**`tahalendor_initial_1`** Tahalendor: “Go away! You're not welcome here!” — **effects:** sets stage 10 of [Rumblings](../quests/rumblings.md#stage-10)

    - “OK...” → *conversation ends*

    <span id="d-tahalendor_initial_2"></span>**`tahalendor_initial_2`** Tahalendor: “Nonsense! Go away!” — **effects:** sets stage 10 of [Rumblings](../quests/rumblings.md#stage-10)

    - “OK...” → *conversation ends*

    <span id="d-tahalendor_erwyn_2"></span>**`tahalendor_erwyn_2`** Tahalendor: “Most undead can be destroyed quite easily, but there is a rare and powerful kind that are much more difficult to permanently destroy.”

    - Next → [tahalendor_erwyn_3](#d-tahalendor_erwyn_3)

    <span id="d-tahalendor_rumblings80_2"></span>**`tahalendor_rumblings80_2`** Tahalendor: “Oh my. It's the heart of a lich! These are nasty creatures.”

    - “These? You mean there are others?” → [tahalendor_rumblings80_3](#d-tahalendor_rumblings80_3)

    <span id="d-tahalendor_rumblings80_2bis"></span>**`tahalendor_rumblings80_2bis`** Tahalendor: “Too bad. Come back when you know more.”


    <span id="d-tahalendor_erwyn_3"></span>**`tahalendor_erwyn_3`** Tahalendor: “I think I have a solution though.”

    - Next → [tahalendor_erwyn_4](#d-tahalendor_erwyn_4)

    <span id="d-tahalendor_rumblings80_3"></span>**`tahalendor_rumblings80_3`** Tahalendor: “They aren't common, but I have heard stories. They are powerful and live underground. They seem to be related to Kazaul somehow.”

    - Next → [tahalendor_rumblings80_4](#d-tahalendor_rumblings80_4)

    <span id="d-tahalendor_erwyn_4"></span>**`tahalendor_erwyn_4`** Tahalendor: “First, I need two coins. Please give me 2 gold coins.”

    - “OK.” *(if pay 2 gold)* → [tahalendor_erwyn_5](#d-tahalendor_erwyn_5)
    - “No, I won't.” → *conversation ends*

    <span id="d-tahalendor_rumblings80_4"></span>**`tahalendor_rumblings80_4`** Tahalendor: “I'm surprised such a young kid as you managed to survive encountering one, let alone actually kill it.”

    - Next → [tahalendor_rumblings80_5](#d-tahalendor_rumblings80_5)

    <span id="d-tahalendor_erwyn_5"></span>**`tahalendor_erwyn_5`** Tahalendor: “Now I will bless them with a special enchantment... [Tahalendor holds the coins over the altar and mutters something you can't hear]”

    - Next → [tahalendor_erwyn_6](#d-tahalendor_erwyn_6)

    <span id="d-tahalendor_rumblings80_5"></span>**`tahalendor_rumblings80_5`** Tahalendor: “You know, since those monsters' attacks, we don't have much to offer, but take these. By the way, do you have any idea who might be responsible for all this?” — **effects:** sets stage 90 of [Rumblings](../quests/rumblings.md#stage-90), gives [Green apple](../items/apple_green.md), [Bread](../items/bread.md), [Major potion of health](../items/health_major2.md)

    - “Not really.” → [tahalendor_rumblings100_0](#d-tahalendor_rumblings100_0)
    - “It was all Glasforn's doing. The tavern owner.” *(if reached stage 70 of [Rumblings](../quests/rumblings.md#stage-70))* → [tahalendor_rumblings103_0](#d-tahalendor_rumblings103_0)
    - “It was my brother Andor. I need to find him.” *(if reached stage 70 of [Rumblings](../quests/rumblings.md#stage-70))* → [tahalendor_rumblings106_0](#d-tahalendor_rumblings106_0)

    <span id="d-tahalendor_erwyn_6"></span>**`tahalendor_erwyn_6`** Tahalendor: “Here you go. As soon as the undead lord appears to be destroyed, place one coin on each eye. This will prevent him from rising again, and soon after you have placed the coins his remains should disintegrate, as he returns to his natural…” — **effects:** sets stage 14 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-14), gives 2× [Gold coins](../items/erwyn_coin.md)

    - “Thank you.” → *conversation ends*



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tahalendor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tahalendor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tahalendor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tahalendor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `tahalendor` · Data from v0.8.18</small>
