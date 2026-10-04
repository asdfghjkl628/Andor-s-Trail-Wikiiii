# ![](../assets/icons/monsters/monsters_johny_1.png){ .sprite } Mysterious lizard creature

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

- [brightport_cave1](../maps/brightport_cave1.md)
- [brightport_cave10](../maps/brightport_cave10.md)

## Quests

- [The balance of scales](../quests/brightport_lizard.md): stages 1, 20, 25, 30
- [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md): stages 113, 116

??? quote "Dialogue (10 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightport_mlizard_selector"></span>**`brightport_mlizard_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 113 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-113))* → [brightport_lizard1](#d-brightport_lizard1)
    - Next *(if reached stage 113 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-113))* → [brightport_emyro_0](#d-brightport_emyro_0)

    <span id="d-brightport_lizard1"></span>**`brightport_lizard1`** [Dummy NPC](../monsters/none.md): “The mysterious creature leaps over the rubble to the other side of the cave.” — **effects:** removes monsters from brightport_cave1, sets stage 113 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-113), sets stage 1 of [The balance of scales](../quests/brightport_lizard.md#stage-1)


    <span id="d-brightport_emyro_0"></span>**`brightport_emyro_0`** [Dummy NPC](../monsters/none.md): “The creature steps back cautiously, its claws scraping the stone floor.”

    - Next → [brightport_emyro](#d-brightport_emyro)

    <span id="d-brightport_emyro"></span>**`brightport_emyro`** [Mysterious lizard creature](../monsters/brightport_emyro.md): “Human again? Why come here, not welcome. Leave.”

    - “I mean no harm. Bryma said your kind's been troubling her, so I came to find out why.” → [brightport_emyrocave2](#d-brightport_emyrocave2)
    - “I was just out for a stroll, and you bolted like your tail was on fire. Thought I'd see what all the fuss was about” → [brightport_emyrocave4](#d-brightport_emyrocave4)

    <span id="d-brightport_emyrocave2"></span>**`brightport_emyrocave2`** [Mysterious lizard creature](../monsters/brightport_emyro.md): “Bryma, that name stinks of lies! You call us trouble, but never ask why? Always blaming, never listen.”

    - Next → [brightport_emyrocave3](#d-brightport_emyrocave3)

    <span id="d-brightport_emyrocave4"></span>**`brightport_emyrocave4`** [Mysterious lizard creature](../monsters/brightport_emyro.md): “You! You smell of the witch. The witch who brought trouble!”

    - Next → [brightport_emyrocave3](#d-brightport_emyrocave3)

    <span id="d-brightport_emyrocave3"></span>**`brightport_emyrocave3`** [Mysterious lizard creature](../monsters/brightport_emyro.md): “She took what's not hers. Bones of our elders, sacred to us! We try to recover them, but she sends beasts. You call us trouble? She's the trouble!” — **effects:** sets stage 20 of [The balance of scales](../quests/brightport_lizard.md#stage-20), sets stage 116 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-116)

    - “I didn't know that. Maybe I could help you?” → [brightport_emyrocave5](#d-brightport_emyrocave5)
    - “I've had enough of your rambling. [Attack the creature.]” → [brightport_emyrofight](#d-brightport_emyrofight)

    <span id="d-brightport_emyrocave5"></span>**`brightport_emyrocave5`** [Green-claw-emyro](../monsters/brightport_lizard.md): “No! But I am only Emyro, the scout. Our leader must decide. Find our home, and leader Elyzard will tell...” — **effects:** sets stage 116 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-116), sets stage 30 of [The balance of scales](../quests/brightport_lizard.md#stage-30), removes monsters from brightport_cave10

    - Next → [brightport_emyrocave6](#d-brightport_emyrocave6)

    <span id="d-brightport_emyrofight"></span>**`brightport_emyrofight`** [Dummy NPC](../monsters/none.md): “As you attempt to attack the creature it swiftly tries to evade your blow, but your combat experience allows you to land a grazing strike. However, the spot it moved to to avoid your attack puts it close to the entrance, allowing it to…” — **effects:** sets stage 25 of [The balance of scales](../quests/brightport_lizard.md#stage-25), sets stage 116 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-116), removes monsters from brightport_cave10


    <span id="d-brightport_emyrocave6"></span>**`brightport_emyrocave6`** [Dummy NPC](../monsters/none.md): “The lizard cautiously steps back, then leaps out the entrance of the burial cave.”




## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_emyro.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_emyro.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_emyro.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_emyro.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `brightport_emyro` · Data from v0.8.18</small>
