# ![](../assets/icons/monsters/monsters_tometik5_10.png){ .sprite } Morvath

| Stat | Value |
|---|---|
| Class | undead |
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

- [undertell_00](../maps/undertell_00.md)

## Quests

- [The fifth master](../quests/fifth_master.md): stages 10, 20, 78
- [hidden_undertell (hidden flag)](../quests/undertell_hidden.md): stages 5, 7

??? quote "Dialogue (15 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-morvath_initial_selector"></span>**`morvath_initial_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 5 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-5))* → [kazaul_masters_not_met_10](#d-kazaul_masters_not_met_10)
    - branch 2 *(if reached stage 5 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-5); NOT reached stage 10 of [The fifth master](../quests/fifth_master.md#stage-10))* → [kazaul_masters_met_but_no_quest_started_10](#d-kazaul_masters_met_but_no_quest_started_10)
    - branch 3 *(if reached stage 10 of [The fifth master](../quests/fifth_master.md#stage-10); NOT reached stage 20 of [The fifth master](../quests/fifth_master.md#stage-20))* → [the_fifth_master_10](#d-the_fifth_master_10)
    - branch 4 *(if carry 1× [The Ritual of Five Aspects](../items/ancient_kazaul_ritual.md))* → [masters_send_to_thalen_10](#d-masters_send_to_thalen_10)
    - branch 5 *(if reached stage 90 of [The fifth master](../quests/fifth_master.md#stage-90))* → [morvath_after_fifth_master_narrator](#d-morvath_after_fifth_master_narrator)
    - branch 6 → [morvath_intro_narrator](#d-morvath_intro_narrator)

    <span id="d-kazaul_masters_not_met_10"></span>**`kazaul_masters_not_met_10`** Morvath: “[While pointing its finger in your direction.] You! How did you get past our army?”

    - “"Our"? There's more of you bosses?” → [kazaul_masters_not_met_20](#d-kazaul_masters_not_met_20)

    <span id="d-kazaul_masters_met_but_no_quest_started_10"></span>**`kazaul_masters_met_but_no_quest_started_10`** Morvath: “If you ever leave while I am talking to you again, I will end your life. Understood?”

    - “[Terrified] Yes.” → [kazaul_masters_not_met_30](#d-kazaul_masters_not_met_30)

    <span id="d-the_fifth_master_10"></span>**`the_fifth_master_10`** Morvath: “[The air grows heavy as the master studies you.] You are bold to walk here. Perhaps bold enough to be of use. One of our own is missing. The fifth master, Anavrin, lies silent. The Ritual of Five Aspects was taken from us long ago.…” — **effects:** sets stage 10 of [The fifth master](../quests/fifth_master.md#stage-10)

    - “You want me to find this ritual?” → [the_fifth_master_20](#d-the_fifth_master_20)

    <span id="d-masters_send_to_thalen_10"></span>**`masters_send_to_thalen_10`** Morvath: “[The Master's hollow eyes flare briefly with dim blue fire.] You hold the Ritual of Five Aspects, mortal. But its meaning lies beyond your grasp. Only Thalen, our brother of Knowledge, can speak the words. Seek him where the thoughts of…”

    - “Thalen? What will he do with it?” → [masters_send_to_thalen_20](#d-masters_send_to_thalen_20)

    <span id="d-morvath_after_fifth_master_narrator"></span>**`morvath_after_fifth_master_narrator`** [Dummy NPC](../monsters/none.md): “A slow rumble of laughter escapes the Master's skeletal chest.”

    - Next → [morvath_after_fifth_master](#d-morvath_after_fifth_master)

    <span id="d-morvath_intro_narrator"></span>**`morvath_intro_narrator`** [Dummy NPC](../monsters/none.md): “The cavern trembles with wrath. A heavy voice fills your mind.”

    - Next → [morvath_intro](#d-morvath_intro)

    <span id="d-kazaul_masters_not_met_20"></span>**`kazaul_masters_not_met_20`** Morvath: “We are "masters", not "bosses". And yes, there are five of us.” — **effects:** sets stage 5 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-5)

    - Next → [kazaul_masters_not_met_30](#d-kazaul_masters_not_met_30)

    <span id="d-kazaul_masters_not_met_30"></span>**`kazaul_masters_not_met_30`** Morvath: “Well, currently there are only four of us masters. We are not complete.”

    - “"Complete"? What is that supposed to mean?” → [the_fifth_master_10](#d-the_fifth_master_10)

    <span id="d-the_fifth_master_20"></span>**`the_fifth_master_20`** Morvath: “Yes. The Ritual of Five Aspects lies lost among your kind. Long ago, a mortal scribe named Varnel served the Kazaul, writing our words into form. But when fear took him, he fled with the ritual and hid among your people. Bring it back to…” — **effects:** sets stage 20 of [The fifth master](../quests/fifth_master.md#stage-20)

    - “Then I will find it.” → [the_fifth_master_accept](#d-the_fifth_master_accept)
    - “I do not trust you, but I will look.” → [the_fifth_master_accept](#d-the_fifth_master_accept)

    <span id="d-masters_send_to_thalen_20"></span>**`masters_send_to_thalen_20`** Morvath: “He will guide your unlearned hands. He alone can draw the pattern that binds the Five. Without him, the ritual is only ink on lost parchment.” — **effects:** sets stage 78 of [The fifth master](../quests/fifth_master.md#stage-78), sets stage 7 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-7)

    - “I will find him.” → *conversation ends*

    <span id="d-morvath_after_fifth_master"></span>**`morvath_after_fifth_master`** [Morvath](../monsters/morvath.md): “The Fifth breathes again. The world will tremble...as it once did.”

    - “[Leave.]” → *conversation ends*

    <span id="d-morvath_intro"></span>**`morvath_intro`** [Morvath](../monsters/morvath.md): “You reek of intrusion, mortal. The stench of the living offends this place.”

    - “I mean no harm. Who...what are you?” → [morvath_intro_20](#d-morvath_intro_20)

    <span id="d-the_fifth_master_accept"></span>**`the_fifth_master_accept`** Morvath: “[The master's eyes flare with dim light.] Then go, mortal. Seek the lost ritual. In the ruins of your kind lies our key to completion. Return only when it is found.”

    - “I understand.” → *conversation ends*

    <span id="d-morvath_intro_20"></span>**`morvath_intro_20`** Morvath: “I am Morvath, the Kazaul master of wrath.”




## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=morvath.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=morvath.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=morvath.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=morvath.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `morvath` · Data from v0.8.18</small>
