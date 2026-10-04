# ![](../assets/icons/monsters/monsters_karvis2_2.png){ .sprite } Kizzo

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

- [loneford6](../maps/loneford6.md)

## Quests

- [A strange looking dagger](../quests/brv_dagger.md): stages 150, 170

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Kizzo. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/loneford_tavern_patron.json" data-npc="Kizzo" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (8 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-loneford_tavern_patron"></span>**`loneford_tavern_patron`** Kizzo: “This is no place for a kid like you. I think you had better leave now.”

    - “I met a man named Forlin who recommended that I speak with you in regards to a possible murder investigation that I am…” *(if reached stage 140 of [A strange looking dagger](../quests/brv_dagger.md#stage-140); NOT reached stage 150 of [A strange looking dagger](../quests/brv_dagger.md#stage-150))* → [kizzo_asd_10](#d-kizzo_asd_10)
    - “I did as you suggested and found the scene of a murder and I found this glove.” *(if carry 1× [Suspect's glove](../items/ogea_glove.md); NOT reached stage 190 of [A strange looking dagger](../quests/brv_dagger.md#stage-190); NOT reached stage 210 of [A strange looking dagger](../quests/brv_dagger.md#stage-210))* → [kizzo_asd_40](#d-kizzo_asd_40)

    <span id="d-kizzo_asd_10"></span>**`kizzo_asd_10`** Kizzo: “Oh, yes. A couple of years ago, a customer that I've never seen before nor have I seen since, sits down at the bar with a terrified look on his face.”

    - Next → [kizzo_asd_20](#d-kizzo_asd_20)

    <span id="d-kizzo_asd_40"></span>**`kizzo_asd_40`** Kizzo: “Wow! This glove looks like it's been through a lot.”

    - Next → [kizzo_asd_50](#d-kizzo_asd_50)

    <span id="d-kizzo_asd_20"></span>**`kizzo_asd_20`** Kizzo: “He begins to tell me that he just witnessed two men in the woods between here and Brimhaven embroiled in a violent altercation and fears that one killed the other.”

    - Next → [kizzo_asd_30](#d-kizzo_asd_30)

    <span id="d-kizzo_asd_50"></span>**`kizzo_asd_50`** Kizzo: “This does however look like it used to be a high quality item.”

    - “Really?” → [kizzo_asd_60](#d-kizzo_asd_60)

    <span id="d-kizzo_asd_30"></span>**`kizzo_asd_30`** Kizzo: “That's all I know. Maybe you could find out more if you can find the scene of the murder?” — **effects:** sets stage 150 of [A strange looking dagger](../quests/brv_dagger.md#stage-150)


    <span id="d-kizzo_asd_60"></span>**`kizzo_asd_60`** Kizzo: “Yes. If that was my glove, I would have tried to get a new one made instead of buying a new set as it would be cheaper.”

    - “Where would someone get just one glove?” → [kizzo_asd_70](#d-kizzo_asd_70)

    <span id="d-kizzo_asd_70"></span>**`kizzo_asd_70`** Kizzo: “Well, I know Venanra in Brimhaven does some great work with cloth and leather items.” — **effects:** sets stage 170 of [A strange looking dagger](../quests/brv_dagger.md#stage-170)




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.12](../versions/0.7.12.md) | name: Tavern owner → Kizzo<br>Dialogue: 7 lines added, 1 line changed<br>· text: “This is no place for a kid like you. I think you better leave now.” → “This is no place for a kid like you. I think you had better leave now.” |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=loneford_tavern_patron.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=loneford_tavern_patron.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=loneford_tavern_patron.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=loneford_tavern_patron.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `loneford_tavern_patron` · Data from v0.8.18</small>
