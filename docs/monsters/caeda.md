# ![](../assets/icons/monsters/monsters_ld1_145.png){ .sprite } Caeda

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

- [lakecave2](../maps/lakecave2.md)
- [remgard0](../maps/remgard0.md)

## Quests

- [A secret garden](../quests/secret_garden.md): stages 10, 20, 40, 50, 60
- [The roots of love](../quests/roots_love.md): stages 20
- [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md): stages 205

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Caeda. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/caeda.json" data-npc="Caeda" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (33 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-caeda"></span>**`caeda`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 10 of [The roots of love](../quests/roots_love.md#stage-10))* → [caeda_1](#d-caeda_1)
    - branch 2 *(if reached stage 10 of [The roots of love](../quests/roots_love.md#stage-10); NOT reached stage 20 of [The roots of love](../quests/roots_love.md#stage-20); NOT reached stage 10 of [A secret garden](../quests/secret_garden.md#stage-10))* → [caeda_2](#d-caeda_2)
    - branch 3 *(if reached stage 20 of [The roots of love](../quests/roots_love.md#stage-20); NOT reached stage 10 of [A secret garden](../quests/secret_garden.md#stage-10))* → [caeda_3](#d-caeda_3)
    - branch 4 *(if reached stage 60 of [A secret garden](../quests/secret_garden.md#stage-60))* → [caeda_60](#d-caeda_60)
    - branch 5 *(if reached stage 50 of [A secret garden](../quests/secret_garden.md#stage-50))* → [caeda_50](#d-caeda_50)
    - branch 6 *(if reached stage 40 of [A secret garden](../quests/secret_garden.md#stage-40))* → [caeda_40](#d-caeda_40)
    - branch 7 *(if reached stage 30 of [A secret garden](../quests/secret_garden.md#stage-30))* → [caeda_30](#d-caeda_30)
    - branch 8 *(if reached stage 20 of [A secret garden](../quests/secret_garden.md#stage-20))* → [caeda_20](#d-caeda_20)
    - branch 9 *(if reached stage 10 of [A secret garden](../quests/secret_garden.md#stage-10))* → [caeda_10](#d-caeda_10)
    - branch 10 *(if reached stage 40 of [A secret garden](../quests/secret_garden.md#stage-40); NOT reached stage 50 of [A secret garden](../quests/secret_garden.md#stage-50))* → [caeda_root30_1](#d-caeda_root30_1)
    - “I killed most of the trolls in the cave.” *(if reached stage 60 of [A secret garden](../quests/secret_garden.md#stage-60))* → [caeda_root60_1](#d-caeda_root60_1)

    <span id="d-caeda_1"></span>**`caeda_1`** Caeda: “So much work to do. I sure hope we will have some rain soon.”


    <span id="d-caeda_2"></span>**`caeda_2`** Caeda: “So much work to do. I sure hope we will have some rain soon.”

    - “Do you know where I can find some damerilias?” → [caeda_root10_0](#d-caeda_root10_0)

    <span id="d-caeda_3"></span>**`caeda_3`** Caeda: “Oh, it is you again.”

    - “Thank you for the damerilias.” → [caeda_root10_5](#d-caeda_root10_5)

    <span id="d-caeda_60"></span>**`caeda_60`** Caeda: “Oh, it is you again. Thank you for all you have done.”

    - “Could you give me the key for the glade again?” *(if reached stage 30 of [The roots of love](../quests/roots_love.md#stage-30); NOT reached stage 205 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-205))* → [caeda_root60_1](#d-caeda_root60_1)
    - “No problem.” → *conversation ends*
    - “It was all for the Shadow.” → *conversation ends*

    <span id="d-caeda_50"></span>**`caeda_50`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 55 of [A secret garden](../quests/secret_garden.md#stage-55))* → [caeda_root50_3](#d-caeda_root50_3)
    - branch 2 → [caeda_root50_2](#d-caeda_root50_2)

    <span id="d-caeda_40"></span>**`caeda_40`** Caeda: “Oh, it is you again. Thank you again for bringing back my key.”

    - Next → [caeda_root40_1](#d-caeda_root40_1)

    <span id="d-caeda_30"></span>**`caeda_30`** Caeda: “Oh, it is you again. Did you find my key?”

    - “Yes. Here. Please take it.” *(if hand over 1× [Key to the glade](../items/glade_key.md))* → [caeda_root30_1](#d-caeda_root30_1)
    - “Yes. Eh, no. I seem to have lost it. Wait, I'll go and find it.” → *conversation ends*

    <span id="d-caeda_20"></span>**`caeda_20`** Caeda: “Oh, it is you. Nice to meet you again.”


    <span id="d-caeda_10"></span>**`caeda_10`** Caeda: “Oh, it is you again. Did you find my key?”

    - “No, not yet.” → *conversation ends*

    <span id="d-caeda_root30_1"></span>**`caeda_root30_1`** Caeda: “You really found my key! Thank you - I can't believe it!” — **effects:** sets stage 40 of [A secret garden](../quests/secret_garden.md#stage-40)

    - “A troll had taken the key, but he won't need it any more.” → [caeda_root40_1](#d-caeda_root40_1)

    <span id="d-caeda_root60_1"></span>**`caeda_root60_1`** Caeda: “Yes, of course. I will give you my father's key. Keep it. Then you can always pick damerilias for Noraed's grave.”

    - “That would be great, thank you.” → [caeda_root60_2](#d-caeda_root60_2)

    <span id="d-caeda_root10_0"></span>**`caeda_root10_0`** Caeda: “What a strange request!”

    - Next → [caeda_root10_1](#d-caeda_root10_1)

    <span id="d-caeda_root10_5"></span>**`caeda_root10_5`** Caeda: “These damerilias are not really good any more. You should get fresh ones from my family's glade north of Remgard.”

    - “How would I get to your glade?” → [caeda_root10_6](#d-caeda_root10_6)

    <span id="d-caeda_root50_3"></span>**`caeda_root50_3`** Caeda: “Is the passage to the glade safe again?”

    - “Yes, I have dealt with most of the trolls. They won't dare to bother you for a long time.” → [caeda_root50_4](#d-caeda_root50_4)

    <span id="d-caeda_root50_2"></span>**`caeda_root50_2`** Caeda: “Is the passage to the glade safe again?”

    - “No, not yet. I guess there are at least 30 trolls to kill. I will go after them again.” → [caeda_root50_2a](#d-caeda_root50_2a)

    <span id="d-caeda_root40_1"></span>**`caeda_root40_1`** Caeda: “With all these trolls around I don't feel safe to go through the cave and take care of the flowers in the glade.”

    - Next → [caeda_root40_1a](#d-caeda_root40_1a)

    <span id="d-caeda_root60_2"></span>**`caeda_root60_2`** Caeda: “Here is the key. I will move to the glade and retire there. It is the most beautiful place in the world.” — **effects:** sets stage 205 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-205), removes monsters from remgard0, spawns monsters on lakecave2, gives 1× [Key to the glade](../items/glade_key.md), removes monsters from lakecave2

    - “So I will meet you there. Bye.” → *NPC leaves*

    <span id="d-caeda_root10_1"></span>**`caeda_root10_1`** Caeda: “Yes I happen to have some. Why are you asking?”

    - “There is this woman in Stoutford, she wants some for the grave of her husband, Noraed.” → [caeda_root10_2](#d-caeda_root10_2)

    <span id="d-caeda_root10_6"></span>**`caeda_root10_6`** Caeda: “To find the glade you have to pass through a cave. There are trolls, but my father had put up a statue that the trolls don't like to pass. So I was able to pass through the cave fairly safely.”

    - Next → [caeda_root10_6a](#d-caeda_root10_6a)

    <span id="d-caeda_root50_4"></span>**`caeda_root50_4`** Caeda: “Thank you so much! I wish you safe travels back to Stoutford. If you want to go to the glade next time you are in Remgard, just ask me for the key.” — **effects:** sets stage 60 of [A secret garden](../quests/secret_garden.md#stage-60)

    - “Thank you. I will leave now.” → *conversation ends*

    <span id="d-caeda_root50_2a"></span>**`caeda_root50_2a`** Caeda: “Please do, and come to me when you are done with them.”


    <span id="d-caeda_root40_1a"></span>**`caeda_root40_1a`** Caeda: “The scorpions are bad enough, but the trolls are really dangerous. I know that they hate the statue, but I am scared they can reach past it.”

    - Next → [caeda_root40_2](#d-caeda_root40_2)

    <span id="d-caeda_root10_2"></span>**`caeda_root10_2`** Caeda: “Noraed is dead? Oh no ... my poor little brother. What happened?”

    - “He was killed saving the life of his wife, during a monster attack on Stoutford.” → [caeda_root10_3](#d-caeda_root10_3)

    <span id="d-caeda_root10_6a"></span>**`caeda_root10_6a`** Caeda: “The glade itself is barred by a solid door to keep the trolls out. I had a key for it of course.”

    - “Had?” → [caeda_root10_7](#d-caeda_root10_7)

    <span id="d-caeda_root40_2"></span>**`caeda_root40_2`** Caeda: “Would it be too much to ask if you could get rid of the trolls?” — **effects:** sets stage 50 of [A secret garden](../quests/secret_garden.md#stage-50), spawns monsters on lakecave0

    - “I can teach them to stay further away from the statue. No problem.” → *conversation ends*

    <span id="d-caeda_root10_3"></span>**`caeda_root10_3`** Caeda: “Yes, that would be him. He loved Aryfora so much. I never had the chance to meet her.”

    - Next → [caeda_root10_3a](#d-caeda_root10_3a)

    <span id="d-caeda_root10_7"></span>**`caeda_root10_7`** Caeda: “Yes. Unfortunately I did not pay enough attention to where I was going when I was there last time, and took a wrong turn.”

    - Next → [caeda_root10_8](#d-caeda_root10_8)

    <span id="d-caeda_root10_3a"></span>**`caeda_root10_3a`** Caeda: “Every year he came to pick the most beautiful damerilia to give it to her as a present.”

    - “Yes, Aryfora told me. She asked me to bring her some damerilias for Noraed's grave.” → [caeda_root10_4](#d-caeda_root10_4)

    <span id="d-caeda_root10_8"></span>**`caeda_root10_8`** Caeda: “Suddenly there were trolls everywhere. I barely escaped, but I must have lost the key to our glade there. If only I could have my key back!” — **effects:** sets stage 10 of [A secret garden](../quests/secret_garden.md#stage-10)

    - “Your damerilias do look a bit wilted. I will go to your glade.” → [caeda_root10_9](#d-caeda_root10_9)
    - “Eh, OK. This isn't worth the trouble. Fresh damerilias wouldn't look different after my travel back. Thank you, I will…” → [caeda_root10_8a](#d-caeda_root10_8a)

    <span id="d-caeda_root10_4"></span>**`caeda_root10_4`** Caeda: “I still have some. Here, take these to her, and send her my condolences.” — **effects:** gives 3× [Damerilias](../items/damerilias.md), sets stage 20 of [The roots of love](../quests/roots_love.md#stage-20)

    - “Thanks. I'll make sure she gets them.” → [caeda_root10_5](#d-caeda_root10_5)
    - “All this trouble for a bunch of smelly flowers...” → [caeda_root10_5](#d-caeda_root10_5)

    <span id="d-caeda_root10_9"></span>**`caeda_root10_9`** Caeda: “And you will bring back my key to the glade? Then I would be the happiest person!”

    - “A small thing for me.” → *conversation ends*

    <span id="d-caeda_root10_8a"></span>**`caeda_root10_8a`** Caeda: “Farewell then. Give my greetings to my sister-in-law.” — **effects:** sets stage 20 of [A secret garden](../quests/secret_garden.md#stage-20)




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 32 lines added, 1 line changed<br>· text: “So much work to do. I sure hope we will have some rain soon.” → “null” |
| [v0.7.9](../versions/0.7.9.md) | Dialogue: 1 line changed<br>· text: “I still have some. Here, take these to her, and send her my condolanc…” → “I still have some. Here, take these to her, and send her my condolenc…” |
| [v0.7.11](../versions/0.7.11.md) | Dialogue: 2 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=caeda.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=caeda.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=caeda.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=caeda.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `caeda` · Data from v0.8.18</small>
