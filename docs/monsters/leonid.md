# ![](../assets/icons/monsters/monsters_men_3.png){ .sprite } Leonid

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

## Quests

- [Disallowed substance](../quests/bonemeal.md): stages 10
- [Search for Andor](../quests/andor.md): stages 10
- [TODO (hidden flag)](../quests/crossglen.md): stages 1

??? quote "Dialogue (15 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-leonid1"></span>**`leonid1`** Leonid: “Hello kid. You're Mikhail's youngest child aren't you? With that brother of yours. I'm Leonid, steward of Crossglen village.”

    - “Have you seen my brother Andor?” → [leonid_andor](#d-leonid_andor)
    - “What can you tell me about Crossglen?” → [leonid_crossglen](#d-leonid_crossglen)
    - “Never mind, see you later.” → [leonid_bye](#d-leonid_bye)

    <span id="d-leonid_andor"></span>**`leonid_andor`** Leonid: “Your brother? No, I haven't seen him here today. I think I saw him in here yesterday talking to Gruil. Maybe he knows more?” — **effects:** sets stage 10 of [Search for Andor](../quests/andor.md#stage-10)

    - “Thanks, I'll go talk to Gruil. There was something more I wanted to talk about.” → [leonid_continue](#d-leonid_continue)
    - “Thanks, I'll go talk to Gruil.” → [leonid_bye](#d-leonid_bye)

    <span id="d-leonid_crossglen"></span>**`leonid_crossglen`** Leonid: “As you know, this is Crossglen village. Mostly a farming community.”

    - Next → [leonid_crossglen1](#d-leonid_crossglen1)

    <span id="d-leonid_bye"></span>**`leonid_bye`** Leonid: “Shadow be with you.”

    - “Shadow be with you.” → *conversation ends*

    <span id="d-leonid_continue"></span>**`leonid_continue`** Leonid: “Anything else I can help you with?”

    - “Have you seen my brother Andor?” → [leonid_andor](#d-leonid_andor)
    - “What can you tell me about Crossglen?” → [leonid_crossglen](#d-leonid_crossglen)
    - “Never mind, see you later.” → [leonid_bye](#d-leonid_bye)

    <span id="d-leonid_crossglen1"></span>**`leonid_crossglen1`** Leonid: “We have Audir with his smithy to the southwest, Leta and her husband's cabin to the west, this town hall here and your father's cabin to the northwest.”

    - Next → [leonid_crossglen2](#d-leonid_crossglen2)

    <span id="d-leonid_crossglen2"></span>**`leonid_crossglen2`** Leonid: “That's pretty much it. We try to live a peaceful life.”

    - “Has there been any recent activity in the village?” → [leonid_crossglen3](#d-leonid_crossglen3)
    - “Let's go back to the other things we talked about.” → [leonid_continue](#d-leonid_continue)

    <span id="d-leonid_crossglen3"></span>**`leonid_crossglen3`** Leonid: “There were some recent disturbances some weeks ago that you may have noticed. Some villagers got into a fight over the new decree from Lord Geomyr.”

    - Next → [leonid_crossglen4](#d-leonid_crossglen4)

    <span id="d-leonid_crossglen4"></span>**`leonid_crossglen4`** Leonid: “Lord Geomyr issued a statement regarding the unlawful use of bonemeal as healing substance. Some villagers argued that we should oppose Lord Geomyr's word and still use it.” — **effects:** sets stage 10 of [Disallowed substance](../quests/bonemeal.md#stage-10)

    - Next → [leonid_crossglen4_1](#d-leonid_crossglen4_1)

    <span id="d-leonid_crossglen4_1"></span>**`leonid_crossglen4_1`** Leonid: “Tharal, our priest, was particularly upset and suggested we do something about Lord Geomyr.”

    - Next → [leonid_crossglen5](#d-leonid_crossglen5)

    <span id="d-leonid_crossglen5"></span>**`leonid_crossglen5`** Leonid: “Other villagers argued that we should follow Lord Geomyr's decree. Personally, I haven't decided what my thoughts are.”

    - Next → [leonid_crossglen6](#d-leonid_crossglen6)

    <span id="d-leonid_crossglen6"></span>**`leonid_crossglen6`** Leonid: “On one hand, Lord Geomyr supports Crossglen with a lot of protection. [Points to the soldiers in the hall]”

    - Next → [leonid_crossglen7](#d-leonid_crossglen7)

    <span id="d-leonid_crossglen7"></span>**`leonid_crossglen7`** Leonid: “But on the other hand, the tax and the recent changes of what's allowed are really taking a toll on Crossglen.”

    - Next → [leonid_crossglen8](#d-leonid_crossglen8)

    <span id="d-leonid_crossglen8"></span>**`leonid_crossglen8`** Leonid: “Someone should go to Castle Geomyr and talk to the steward about our situation here in Crossglen.” — **effects:** sets stage 1 of [TODO (hidden flag)](../quests/crossglen.md#stage-1)

    - Next → [leonid_crossglen9](#d-leonid_crossglen9)

    <span id="d-leonid_crossglen9"></span>**`leonid_crossglen9`** Leonid: “In the meantime, we've banned all use of bonemeal as a healing substance.”

    - “Thank you for the information. There was something more I wanted to ask you.” → [leonid_continue](#d-leonid_continue)
    - “Thank you for the information. Bye.” → [leonid_bye](#d-leonid_bye)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 3 lines changed<br>· text: “Lord Geomyr issued a statement regarding the unlawful use of Bonemeal…” → “Lord Geomyr issued a statement regarding the unlawful use of bonemeal…”<br>· text: “In the meantime, we've banned all use of Bonemeal as a healing substa…” → “In the meantime, we've banned all use of bonemeal as a healing substa…” |
| [v0.8.3](../versions/0.8.3.md) | Dialogue: 1 line changed<br>· text: “Hello kid. You're Mikhail's son aren't you? With that brother of your…” → “Hello kid. You're Mikhail's youngest child aren't you? With that brot…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=leonid.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=leonid.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=leonid.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=leonid.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `leonid` · Data from v0.8.18</small>
