# ![](../assets/icons/monsters/monsters_gisons_15.png){ .sprite } Shannal

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

- [mt_galmore_railhouse](../maps/mt_galmore_railhouse.md)

## Quests

- [You shall pass](../quests/undertell_barricades.md): stages 20, 40, 80, 90, 160

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Shannal. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/shannal_selector.json" data-npc="Shannal" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (27 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-shannal_selector"></span>**`shannal_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if wearing [#heartsteel_filter](../items/#heartsteel_filter.md))* → [shannal_undertell_hs_11](#d-shannal_undertell_hs_11)
    - branch 2 *(if latest stage of [You shall pass](../quests/undertell_barricades.md#stage-10) is 10)* → [shannal_welcome_10](#d-shannal_welcome_10)
    - branch 3 *(if latest stage of [You shall pass](../quests/undertell_barricades.md#stage-20) is 20)* → [shannal_welcome_30](#d-shannal_welcome_30)
    - branch 4 *(if latest stage of [You shall pass](../quests/undertell_barricades.md#stage-40) is 40)* → [shannal_step_40](#d-shannal_step_40)
    - branch 5 *(if reached stage 70 of [You shall pass](../quests/undertell_barricades.md#stage-70); NOT reached stage 100 of [You shall pass](../quests/undertell_barricades.md#stage-100))* → [shannal_benbyr_30](#d-shannal_benbyr_30)
    - branch 6 *(if latest stage of [You shall pass](../quests/undertell_barricades.md#stage-150) is 150)* → [shannal_removes_barricades_10](#d-shannal_removes_barricades_10)
    - branch 7 *(if reached stage 160 of [You shall pass](../quests/undertell_barricades.md#stage-160))* → [shannal_undertell_10](#d-shannal_undertell_10)
    - branch 8 → [shannal_unfinished_business_10](#d-shannal_unfinished_business_10)

    <span id="d-shannal_undertell_hs_11"></span>**`shannal_undertell_hs_11`** Shannal: “How dare you come to me while wielding that weapon.”

    - “What?” → [shannal_undertell_hs_15](#d-shannal_undertell_hs_15)

    <span id="d-shannal_welcome_10"></span>**`shannal_welcome_10`** Shannal: “Who are you? Why have you come?”

    - “I am $playername. I have been seeking my brother Andor, who might have entered Undertell. Please let me pass.” → [shannal_welcome_20](#d-shannal_welcome_20)

    <span id="d-shannal_welcome_30"></span>**`shannal_welcome_30`** Shannal: “If you want to get into Undertell, you shall have to prove your capability to go inside. There are plenty of ghosts here. I don't want you to join their ranks.” — **effects:** sets stage 20 of [You shall pass](../quests/undertell_barricades.md#stage-20)

    - “But look at me, I am a powerful and skilled fighter.” → [shannal_welcome_40](#d-shannal_welcome_40)

    <span id="d-shannal_step_40"></span>**`shannal_step_40`** Shannal: “Now bring that coin that I just gave you to Benbyr.”


    <span id="d-shannal_benbyr_30"></span>**`shannal_benbyr_30`** Shannal: “So, what did you learn?”

    - “A very scared apple which didn't fall far from the tree. An ancestor who forced people to come to work here.” → [shannal_benbyr_40](#d-shannal_benbyr_40)

    <span id="d-shannal_removes_barricades_10"></span>**`shannal_removes_barricades_10`** Shannal: “Quite well done! Thank you for helping Rain.”

    - Next → [shannal_removes_barricades_20](#d-shannal_removes_barricades_20)

    <span id="d-shannal_undertell_10"></span>**`shannal_undertell_10`** Shannal: “You wanted to get into Undertell so much, then why are you still here? Go.”


    <span id="d-shannal_unfinished_business_10"></span>**`shannal_unfinished_business_10`** Shannal: “Has the assignment I gave you been completed?”

    - “No.” → [shannal_unfinished_business_20](#d-shannal_unfinished_business_20)

    <span id="d-shannal_undertell_hs_15"></span>**`shannal_undertell_hs_15`** Shannal: “Put it away!”

    - “If you say so.” → *conversation ends*

    <span id="d-shannal_welcome_20"></span>**`shannal_welcome_20`** Shannal: “Impossible! I control those barricades and I can assure you that nobody passed through them any time recently.”

    - “Regardless, I still want to pass through them.” → [shannal_welcome_30](#d-shannal_welcome_30)

    <span id="d-shannal_welcome_40"></span>**`shannal_welcome_40`** Shannal: “I know you are. Else I would not even consider asking you.”

    - “So, what do you want from me?” → [shannal_benbyr_10](#d-shannal_benbyr_10)

    <span id="d-shannal_benbyr_40"></span>**`shannal_benbyr_40`** Shannal: “I know. I was one of those people forcibly abducted by him. I lost my family. I lost my life here.”

    - “Do you intend to kill him?” → [shannal_benbyr_50](#d-shannal_benbyr_50)

    <span id="d-shannal_removes_barricades_20"></span>**`shannal_removes_barricades_20`** Shannal: “Remember, Undertell is a deep, fiery and confusing place...be alert, always.”

    - Next → [shannal_removes_barricades_30](#d-shannal_removes_barricades_30)

    <span id="d-shannal_unfinished_business_20"></span>**`shannal_unfinished_business_20`** Shannal: “Then go complete it.”

    - “Yes, ma'am.” → *conversation ends*

    <span id="d-shannal_benbyr_10"></span>**`shannal_benbyr_10`** Shannal: “Here, take this bronze coin. It is a 'Traders' Guild Bronze coin' and the only one I have left, so don't lose it. Now, go show it to Benbyr. He generally can be found north of Fallhaven, keeping out of the sight of Feygard guards. He's a…” — **effects:** sets stage 40 of [You shall pass](../quests/undertell_barricades.md#stage-40), gives 1× [Trader's Guild bronze coin](../items/trader_guild-coins.md)

    - “Why do I need to show this coin to Benbyr of all people?” → [shannal_benbyr_20](#d-shannal_benbyr_20)

    <span id="d-shannal_benbyr_50"></span>**`shannal_benbyr_50`** Shannal: “Benbyr? No, if I wanted, I could have harmed his predecessors. But I seek your help. Benbyr has to make restitution.” — **effects:** sets stage 80 of [You shall pass](../quests/undertell_barricades.md#stage-80)

    - Next → [shannal_benbyr_55](#d-shannal_benbyr_55)

    <span id="d-shannal_removes_barricades_30"></span>**`shannal_removes_barricades_30`** Shannal: “You may now pass. The path to Undertell is open. Fare the well, wanderer.” — **effects:** sets stage 160 of [You shall pass](../quests/undertell_barricades.md#stage-160)


    <span id="d-shannal_benbyr_20"></span>**`shannal_benbyr_20`** Shannal: “First step in restitution. Now go!”


    <span id="d-shannal_benbyr_55"></span>**`shannal_benbyr_55`** Shannal: “Remember the drunk man outside the Fallhaven tavern?”

    - “Sure...he's the one always begging me for some mead.” → [shannal_benbyr_60](#d-shannal_benbyr_60)

    <span id="d-shannal_benbyr_60"></span>**`shannal_benbyr_60`** Shannal: “Yes, that sounds like him alright. His name is Rain. He came to Undertell seeking his ancestor, me, to find out where I disappeared to.”

    - Next → [shannal_benbyr_65](#d-shannal_benbyr_65)

    <span id="d-shannal_benbyr_65"></span>**`shannal_benbyr_65`** Shannal: “The sights and sounds here broke his mind.”

    - “I know. He keeps babbling about treasure and dungeons and of course, getting more mead.” → [shannal_benbyr_70](#d-shannal_benbyr_70)

    <span id="d-shannal_benbyr_70"></span>**`shannal_benbyr_70`** Shannal: “Unnmir was with him when his mind broke on seeing Undertell. I feared Unnmir would abandon him. But he took him to Fallhaven, and tried to get the priest to heal him. To no avail. He fell into drinking and camping outside the tavern, when…”

    - “Poor guy.” → [shannal_benbyr_80](#d-shannal_benbyr_80)

    <span id="d-shannal_benbyr_80"></span>**`shannal_benbyr_80`** Shannal: “First shake down Benbyr for how much he can give you.”

    - Next → [shannal_benbyr_85](#d-shannal_benbyr_85)

    <span id="d-shannal_benbyr_85"></span>**`shannal_benbyr_85`** Shannal: “Then please give my descendant one of Lodar's Potion of heightened senses and tell Rain that I am at peace. Unnmir didn't know it, but that potion helps heal the mind as well.”

    - Next → [shannal_benbyr_90](#d-shannal_benbyr_90)

    <span id="d-shannal_benbyr_90"></span>**`shannal_benbyr_90`** Shannal: “Then give him what you got from Benbyr, to start his new life.”

    - Next → [shannal_benbyr_95](#d-shannal_benbyr_95)

    <span id="d-shannal_benbyr_95"></span>**`shannal_benbyr_95`** Shannal: “[sternly] And don't keep any gold from Benbyr for yourself, else you'll not get into Undertell!” — **effects:** sets stage 90 of [You shall pass](../quests/undertell_barricades.md#stage-90)

    - “Wow! That's a lot, but I think I've got it all. Don't worry.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 27 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shannal.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shannal.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shannal.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shannal.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `shannal` · Data from v0.8.18</small>
