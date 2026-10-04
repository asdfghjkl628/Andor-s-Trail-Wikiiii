# ![](../assets/icons/monsters/monsters_gisons_13.png){ .sprite } Myrelis

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 0 |
| Max AP | 10 |
| Attack cost | 10 |
| Move cost | 3 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Found on

- [galmore_58](../maps/galmore_58.md)

## Quests

- [Lost treasures](../quests/nocmar.md): stages 35
- [You shall pass](../quests/undertell_barricades.md): stages 10
- [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md): stages 10

??? quote "Dialogue (15 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-mg_myrelis_selector"></span>**`mg_myrelis_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 9 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-9))* → [mg_myrelis_illusion_10](#d-mg_myrelis_illusion_10)

    <span id="d-mg_myrelis_illusion_10"></span>**`mg_myrelis_illusion_10`** Myrelis: “So, what did you think of my work?”

    - “What was that back there?” → [mg_myrelis_illusion_what_was_that_20](#d-mg_myrelis_illusion_what_was_that_20)
    - “You did that? How?” → [mg_myrelis_illusion_you_did_that_10](#d-mg_myrelis_illusion_you_did_that_10)
    - “Why did you build that here?” → [mg_myrelis_illusion_why_build_that_10](#d-mg_myrelis_illusion_why_build_that_10)
    - “We've already discussed it. Don't you remember?” *(if reached stage 10 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-10))* → [mg_myrelis_vaelric_5](#d-mg_myrelis_vaelric_5)
    - “I was wondering, why are those barricades there? [pointing southwest]” *(if latest stage of [Lost treasures](../quests/nocmar.md#stage-20) is 20; reached stage 3 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-3))* → [mg_myrelis_barricades_10](#d-mg_myrelis_barricades_10)
    - “How do I get past those barricades?” *(if latest stage of [Lost treasures](../quests/nocmar.md#stage-35) is 35; NOT reached stage 20 of [You shall pass](../quests/undertell_barricades.md#stage-20))* → [mg_myrelis_shannal_10](#d-mg_myrelis_shannal_10)
    - “I am wondering if you could help me, I am looking for something.” *(if latest stage of [Lost treasures](../quests/nocmar.md#stage-30) is 30)* → [mg_myrelis_undertell_10](#d-mg_myrelis_undertell_10)

    <span id="d-mg_myrelis_illusion_what_was_that_20"></span>**`mg_myrelis_illusion_what_was_that_20`** Myrelis: “Ah, my finest creation! A scene to dazzle the senses, to remind even the most weary traveler of life's beauty. I call it "Tropical Bliss." But enough about what it is. What did it make you feel? Awe? Peace? Perhaps a longing for adventure?”

    - “I liked it!” → *conversation ends*
    - “You did that? How?” → [mg_myrelis_illusion_you_did_that_10](#d-mg_myrelis_illusion_you_did_that_10)

    <span id="d-mg_myrelis_illusion_you_did_that_10"></span>**`mg_myrelis_illusion_you_did_that_10`** Myrelis: “No, no, no. An artist never reveals the "how." The methods are nothing compared to the grandeur of the art itself. Let's not tarnish the magic by pulling back the curtain, shall we?”

    - “Why did you build that here?” → [mg_myrelis_illusion_why_build_that_10](#d-mg_myrelis_illusion_why_build_that_10)

    <span id="d-mg_myrelis_illusion_why_build_that_10"></span>**`mg_myrelis_illusion_why_build_that_10`** Myrelis: “Let me tell you a little story. Long ago, I was an indentured servant, toiling away as a miner here in Galmore. This place was a prison to my spirit, a bleak and joyless pit. When I was freed, I swore I would transform it. I wanted to…”

    - “I see. Thank you for telling me your story.” → *conversation ends*
    - “Interesting! Very, but I have another question.” *(if reached stage 10 of [The swamp healer](../quests/swamp_healer.md#stage-10))* → [mg_myrelis_vaelric_10](#d-mg_myrelis_vaelric_10)

    <span id="d-mg_myrelis_vaelric_5"></span>**`mg_myrelis_vaelric_5`** Myrelis: “Sorry. You see, ghosts sometimes have bad memories. Or is it just me? Anyway, if we already talked, then why are you back here?”

    - “Do you know of Vaelric, the healer?” → [mg_myrelis_vaelric_20](#d-mg_myrelis_vaelric_20)
    - “I'm wondering if you could help me? I'm looking for something.” *(if latest stage of [Lost treasures](../quests/nocmar.md#stage-30) is 30)* → [mg_myrelis_undertell_10](#d-mg_myrelis_undertell_10)

    <span id="d-mg_myrelis_barricades_10"></span>**`mg_myrelis_barricades_10`** Myrelis: “[With a terrified expression on his face] Oh those? Yeah, you don't want to go past those. Past them is the entrance to Undertell.” — **effects:** sets stage 35 of [Lost treasures](../quests/nocmar.md#stage-35)

    - “Oh, that's how to get to Undertell?! How do I get past those barricades?” → [mg_myrelis_shannal_10](#d-mg_myrelis_shannal_10)

    <span id="d-mg_myrelis_shannal_10"></span>**`mg_myrelis_shannal_10`** Myrelis: “To enter Undertell, you need to talk to my friend Shannal, she has just come to spend a day at the beach. Shannal is the guardian ghost who controls passage to Undertell. Only she can remove (and put back) the barriers you see now.” — **effects:** sets stage 10 of [You shall pass](../quests/undertell_barricades.md#stage-10), spawns monsters on mt_galmore_railhouse

    - “You, Shannal, maybe other ghosts, you all sure can affect the world of the living. Why does Shannal control the…” → [mg_myrelis_shannal_20](#d-mg_myrelis_shannal_20)

    <span id="d-mg_myrelis_undertell_10"></span>**`mg_myrelis_undertell_10`** Myrelis: “What is it?”

    - “I'm looking for some place called "Undertell", do you know where it is?” → [mg_myrelis_undertell_20](#d-mg_myrelis_undertell_20)
    - “I'm looking for my brother. His name is Andor and he looks a lot like me.” → [mg_myrelis_andor](#d-mg_myrelis_andor)

    <span id="d-mg_myrelis_vaelric_10"></span>**`mg_myrelis_vaelric_10`** Myrelis: “Sure, ask away.” — **effects:** sets stage 10 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-10)

    - “Do you know of Vaelric, the healer?” → [mg_myrelis_vaelric_20](#d-mg_myrelis_vaelric_20)

    <span id="d-mg_myrelis_vaelric_20"></span>**`mg_myrelis_vaelric_20`** Myrelis: “Vaelric... Hmm, the name does tickle a memory, but I can't place it. I've heard whispers, perhaps, or seen his name scrawled in some dusty tome. Why do you ask? Is he another artist, or just someone you are curious about?”

    - “Oh, never mind. I was just wondering.” → *conversation ends*

    <span id="d-mg_myrelis_shannal_20"></span>**`mg_myrelis_shannal_20`** Myrelis: “She has seen horrors, as have the rest of us. It moved something inside her. When she came back as a ghost, that change gave her the ability to barricade the entrance, which she has. Go see her.”

    - “Sounds good. Thank you.” → *conversation ends*

    <span id="d-mg_myrelis_undertell_20"></span>**`mg_myrelis_undertell_20`** [Dummy NPC](../monsters/none.md): “With a terrified expression on his face, Myrelis slowly raises his arm and points you to the southwest.”

    - Next → [mg_myrelis_undertell_30](#d-mg_myrelis_undertell_30)

    <span id="d-mg_myrelis_andor"></span>**`mg_myrelis_andor`** Myrelis: “No, I'm sorry, but you are the first human that I've seen in...geez, I can't even remember how long.”


    <span id="d-mg_myrelis_undertell_30"></span>**`mg_myrelis_undertell_30`** [Myrelis](../monsters/mg_myrelis.md): “Over there, but it looks like it's blocked.” — **effects:** sets stage 35 of [Lost treasures](../quests/nocmar.md#stage-35)

    - “How do I get past those barricades?” → [mg_myrelis_shannal_10](#d-mg_myrelis_shannal_10)



## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 12 lines added |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 3 lines added, 3 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg_myrelis.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg_myrelis.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg_myrelis.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg_myrelis.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `mg_myrelis` · Data from v0.8.18</small>
