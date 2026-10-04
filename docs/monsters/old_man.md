# ![](../assets/icons/monsters/monsters_men_5.png){ .sprite } Old man

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

- [fallhaven_nw](../maps/fallhaven_nw.md)

## Quests

- [Calomyran secrets](../quests/calomyran.md): stages 10, 100
- [Darkness in the Daylight](../quests/darkness_in_daylight.md): stages 130, 140

??? quote "Dialogue (19 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-fallhaven_oldman"></span>**`fallhaven_oldman`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 110 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-110); NOT reached stage 140 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-140))* → [dds_oldman_10](#d-dds_oldman_10)
    - branch 2 *(if reached stage 100 of [Calomyran secrets](../quests/calomyran.md#stage-100))* → [fallhaven_oldman_complete_2](#d-fallhaven_oldman_complete_2)
    - branch 3 *(if reached stage 10 of [Calomyran secrets](../quests/calomyran.md#stage-10))* → [fallhaven_oldman_continue](#d-fallhaven_oldman_continue)
    - branch 4 → [fallhaven_oldman_1](#d-fallhaven_oldman_1)

    <span id="d-dds_oldman_10"></span>**`dds_oldman_10`** Old man: “Who are you? Not here to steal my books, are you?”

    - “I once helped to find your book. Don't be rude!” → [dds_oldman_20](#d-dds_oldman_20)

    <span id="d-fallhaven_oldman_complete_2"></span>**`fallhaven_oldman_complete_2`** Old man: “Thank you so much for finding my book!”


    <span id="d-fallhaven_oldman_continue"></span>**`fallhaven_oldman_continue`** Old man: “How is the search for my book going? It's called 'Calomyran Secrets'. Have you found my book?”

    - “Yes, I found it.” *(if hand over 1× [Calomyran secrets](../items/calomyran_secrets.md))* → [fallhaven_oldman_complete](#d-fallhaven_oldman_complete)
    - “No, I have not found it yet.” → [fallhaven_oldman_6](#d-fallhaven_oldman_6)
    - “Could you tell me your story again please?” → [fallhaven_oldman_2](#d-fallhaven_oldman_2)

    <span id="d-fallhaven_oldman_1"></span>**`fallhaven_oldman_1`** Old man: “Would you help an old man please?”

    - “Sure, what do you need help with?” → [fallhaven_oldman_2](#d-fallhaven_oldman_2)
    - “I might. Are we talking about some kind of reward?” → [fallhaven_oldman_2](#d-fallhaven_oldman_2)
    - “No, I won't help an old timer like you. Bye.” → *conversation ends*

    <span id="d-dds_oldman_20"></span>**`dds_oldman_20`** Old man: “Sorry, there seem to be folks who want to take my books and not return them.”

    - “In fact, I'd like to borrow your copy of Calomyran Secrets.” → [dds_oldman_30](#d-dds_oldman_30)

    <span id="d-fallhaven_oldman_complete"></span>**`fallhaven_oldman_complete`** Old man: “My book! Thank you, thank you! Where was it? No, don't tell me. Here, take these coins for your trouble.” — **effects:** sets stage 100 of [Calomyran secrets](../quests/calomyran.md#stage-100), gives [Gold coins](../items/gold.md)

    - “Thank you. Goodbye.” → *conversation ends*
    - “At last, some gold. Bye.” → *conversation ends*

    <span id="d-fallhaven_oldman_6"></span>**`fallhaven_oldman_6`** Old man: “I have no idea where it might be. You could go ask Arcir, he seems very fond of his books. [Points at the house to the south]” — **effects:** sets stage 10 of [Calomyran secrets](../quests/calomyran.md#stage-10)

    - “OK, I'll go ask Arcir. Goodbye.” → *conversation ends*

    <span id="d-fallhaven_oldman_2"></span>**`fallhaven_oldman_2`** Old man: “I recently lost a very valuable book of mine.”

    - Next → [fallhaven_oldman_3](#d-fallhaven_oldman_3)

    <span id="d-dds_oldman_30"></span>**`dds_oldman_30`** Old man: “No can do. It's too rare and precious.”

    - “But Dhayavar is at stake!” → [dds_oldman_40](#d-dds_oldman_40)

    <span id="d-fallhaven_oldman_3"></span>**`fallhaven_oldman_3`** Old man: “I know I had it with me yesterday. Now I can't seem to find it.”

    - Next → [fallhaven_oldman_4](#d-fallhaven_oldman_4)

    <span id="d-dds_oldman_40"></span>**`dds_oldman_40`** Old man: “Sounds serious. But, what's the book got to do with that?”

    - “I need a chant from it to break a Kazaul spell.” → [dds_oldman_50](#d-dds_oldman_50)

    <span id="d-fallhaven_oldman_4"></span>**`fallhaven_oldman_4`** Old man: “I never lose things! Someone must have stolen it, that's my guess.”

    - Next → [fallhaven_oldman_5](#d-fallhaven_oldman_5)

    <span id="d-dds_oldman_50"></span>**`dds_oldman_50`** Old man: “Copy it then.” — **effects:** sets stage 130 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-130)

    - “OK ... just a second ...” → [dds_oldman_60](#d-dds_oldman_60)

    <span id="d-fallhaven_oldman_5"></span>**`fallhaven_oldman_5`** Old man: “Would you please go look for my book? It's called 'Calomyran Secrets'.”

    - Next → [fallhaven_oldman_6](#d-fallhaven_oldman_6)

    <span id="d-dds_oldman_60"></span>**`dds_oldman_60`** Old man: “Have you finished yet?”

    - “[Talking to self, while reading] So, this is the chant. Wait, this is half a chant! The books says the rest of the…” → [dds_oldman_62](#d-dds_oldman_62)

    <span id="d-dds_oldman_62"></span>**`dds_oldman_62`** Old man: “And stop babbling to yourself!”

    - “Done. Here's your book back, thank you.” → [dds_oldman_64](#d-dds_oldman_64)

    <span id="d-dds_oldman_64"></span>**`dds_oldman_64`** Old man: “Do I see greasy fingerprints there?”

    - “However, it is not complete. Do you also have the book Azimyran Secrets?” → [dds_oldman_70](#d-dds_oldman_70)

    <span id="d-dds_oldman_70"></span>**`dds_oldman_70`** Old man: “No, sorry. Do let me know if you come across a copy.” — **effects:** sets stage 140 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-140)




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines changed<br>· text: “I have no idea where it might be. You could go ask Arcir, he seems ve…” → “I have no idea where it might be. You could go ask Arcir, he seems ve…” |
| [v0.8.14](../versions/0.8.14.md) | Dialogue: 9 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=old_man.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=old_man.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=old_man.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=old_man.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `old_man` · Data from v0.8.18</small>
