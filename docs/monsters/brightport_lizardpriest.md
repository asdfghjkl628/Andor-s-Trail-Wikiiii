# ![](../assets/icons/monsters/monsters_johny_4.png){ .sprite } Long-tail-dominio

| Stat | Value |
|---|---|
| Class | reptile |
| HP | 160 |
| Max AP | 12 |
| Attack cost | 6 |
| Move cost | 4 |
| Damage | 8 to 15 |
| Attack chance | 180 |
| Block chance | 160 |
| Damage resistance | 4 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Lizardman bone](../items/brightport_bone.md) | 35% | 1 to 2 |
| [Gold coins](../items/gold.md) | 100% | 30 to 45 |
| [Lizard skin](../items/lizard_skin.md) | 100% | 1 |

## Found on

- [brightport_lizardtemple](../maps/brightport_lizardtemple.md)

## Quests

- [The balance of scales](../quests/brightport_lizard.md): stages 65, 70
- [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md): stages 127

??? quote "Dialogue (32 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightport_dominio"></span>**`brightport_dominio`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 127 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-127))* → [brightport_dominio15](#d-brightport_dominio15)
    - Next *(if reached stage 70 of [The balance of scales](../quests/brightport_lizard.md#stage-70); NOT reached stage 127 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-127); NOT reached stage 90 of [The balance of scales](../quests/brightport_lizard.md#stage-90))* → [brightport_dominio11](#d-brightport_dominio11)
    - Next *(if reached stage 60 of [The balance of scales](../quests/brightport_lizard.md#stage-60))* → [brightport_dominio0](#d-brightport_dominio0)
    - Next *(if NOT reached stage 60 of [The balance of scales](../quests/brightport_lizard.md#stage-60))* → [brightport_dominio3](#d-brightport_dominio3)

    <span id="d-brightport_dominio15"></span>**`brightport_dominio15`** Long-tail-dominio: “The Shadow welcomes you, friend.”

    - “How did the Shadow end up in a place like this?” → [brightport_dominio16](#d-brightport_dominio16)
    - “Can you tell more about the lizard people?” → [brightport_dominio18](#d-brightport_dominio18)

    <span id="d-brightport_dominio11"></span>**`brightport_dominio11`** Long-tail-dominio: “The Shadow welcomes you, outsider. How is the task?”

    - “I found those crystals and shattered them.” *(if reached stage 80 of [The balance of scales](../quests/brightport_lizard.md#stage-80); reached stage 75 of [The balance of scales](../quests/brightport_lizard.md#stage-75))* → [brightport_dominio13](#d-brightport_dominio13)
    - “What am I supposed to do again?” → [brightport_dominio12](#d-brightport_dominio12)
    - “It might be too tough for me now, I'll attempt it again later.” → *conversation ends*

    <span id="d-brightport_dominio0"></span>**`brightport_dominio0`** Long-tail-dominio: “You returned the bones of our people back to us. Shadow be with you, human.”

    - “The chieftain told me, you have a task for me.” → [brightport_dominio4](#d-brightport_dominio4)
    - “Why is a Shadow priest in this place?” → [Brightport_dominio1](#d-Brightport_dominio1)

    <span id="d-brightport_dominio3"></span>**`brightport_dominio3`** Long-tail-dominio: “I don't trust you. outsider. Leave.”


    <span id="d-brightport_dominio16"></span>**`brightport_dominio16`** Long-tail-dominio: “When the honorable people of Nor City arrived here and requested our assistance in battle, we obliged under the condition that they cleanse the ruins of the beasts. While the warriors were away, I was taught of the Shadow by the priests…”

    - Next → [brightport_dominio17](#d-brightport_dominio17)

    <span id="d-brightport_dominio18"></span>**`brightport_dominio18`** Long-tail-dominio: “We posses a long oral tradition dating back to the last lizardman empire, but it does not tell us of our origins before that. Of the arrival.”

    - Next → [brightport_dominio19](#d-brightport_dominio19)

    <span id="d-brightport_dominio13"></span>**`brightport_dominio13`** Long-tail-dominio: “Great, and what about the beasts?”

    - “Once the crystals were shattered, they dissipated.” → [brightport_dominio14](#d-brightport_dominio14)

    <span id="d-brightport_dominio12"></span>**`brightport_dominio12`** Long-tail-dominio: “Remember, find the two crystals inside the ruins to the west, and try to break them.”


    <span id="d-brightport_dominio4"></span>**`brightport_dominio4`** Long-tail-dominio: “Yes. But outsider, this is no mere task. Every man who has sought to prove themselves to our tribe has been tasked with this challenge, but none have succeeded.”

    - Next → [brightport_dominio5](#d-brightport_dominio5)

    <span id="d-Brightport_dominio1"></span>**`Brightport_dominio1`** Long-tail-dominio: “Our tribe was taught the ways many years ago by the honorable paladins of Nor City. We were given the Holy Book of Rites, which I relentlessly study to enlighten my people.”

    - “Finally someone who can speak properly, can you tell me more?” → [brightport_dominio2](#d-brightport_dominio2)

    <span id="d-brightport_dominio17"></span>**`brightport_dominio17`** [Dummy NPC](../monsters/none.md): “The expression on the lizardman's face is indecipherable, but you can tell its eyes dazed off into space.”


    <span id="d-brightport_dominio19"></span>**`brightport_dominio19`** Long-tail-dominio: “Our earliest history begins with the Silverscales. Before the tribes split, we were one, with scales that glimmered silver, some shining as bright as light.”

    - Next → [brightport_dominio20](#d-brightport_dominio20)

    <span id="d-brightport_dominio14"></span>**`brightport_dominio14`** Long-tail-dominio: “That is wonderful news! Please tell the chief about your deeds. I shall pray the Shadow guide one as brave as you.” — **effects:** sets stage 127 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-127)


    <span id="d-brightport_dominio5"></span>**`brightport_dominio5`** Long-tail-dominio: “In the caves close to here lies the entrance to a ruin from which at times beasts of darkness emerge to attack our village.” — **effects:** sets stage 65 of [The balance of scales](../quests/brightport_lizard.md#stage-65)

    - Next → [brightport_dominio6](#d-brightport_dominio6)

    <span id="d-brightport_dominio2"></span>**`brightport_dominio2`** Long-tail-dominio: “I see you are longing for the wisdom of the Shadow, but you have been sent to me with a purpose, is that not the case?”

    - “The chieftain told me you have a task for me.” → [brightport_dominio4](#d-brightport_dominio4)

    <span id="d-brightport_dominio20"></span>**`brightport_dominio20`** Long-tail-dominio: “We did not live in swamps or damp caves, our homes were in the lakes. The Silverscales were advanced in culture and architecture. Before long, they called themselves an empire, one that lasted hundreds of years, but it was not eternal.”

    - Next → [brightport_dominio21](#d-brightport_dominio21)

    <span id="d-brightport_dominio6"></span>**`brightport_dominio6`** Long-tail-dominio: “We have driven them back numerous times, but past the entrance no lizardman can pass; a force holds us back. The only ones able to pass are humans.”

    - Next → [brightport_dominio7](#d-brightport_dominio7)

    <span id="d-brightport_dominio21"></span>**`brightport_dominio21`** Long-tail-dominio: “A calamity brought them down. The stories tell of demons. Proficient in dark arts and lustful for blood. We fought but the enemy was not one we could defeat. Here our records vanish, yet any lizardman can tell, we endured, and came back.…”

    - “And what after?” → [brightport_dominio23](#d-brightport_dominio23)
    - “If the knowledge was lost how come you still know of the silverscales?” → [brightport_dominio22](#d-brightport_dominio22)

    <span id="d-brightport_dominio7"></span>**`brightport_dominio7`** Long-tail-dominio: “Over hundreds of years, adventurers have failed to slay the beast, or claimed to have done so but the attacks continued, leaving us to distrust your brethren.”

    - Next → [brightport_dominio8](#d-brightport_dominio8)

    <span id="d-brightport_dominio23"></span>**`brightport_dominio23`** Long-tail-dominio: “From here on, history is better known, we lived in other places, and across the land different tribes thrived. But none more so than the tribes of the bright lake, here it was where the legacy of the forefathers remained. Yet we did not…”

    - Next → [brightport_dominio24](#d-brightport_dominio24)

    <span id="d-brightport_dominio22"></span>**`brightport_dominio22`** Long-tail-dominio: “The Silverscales history is carved on murals deep within the last city, in which the yellow scales make their home. We often make pilgrimages to the spire of our forebears to commune with the elders, and each tribe possesses artifacts…”

    - “What kind of artifacts?” → [brightport_dominio26_selector](#d-brightport_dominio26_selector)

    <span id="d-brightport_dominio8"></span>**`brightport_dominio8`** Long-tail-dominio: “The last human to challenge the ruin was a man named Lutarc. He slayed the beasts and brought back two stone tablets, which shone light on the origin of those creatures. They are not mere monsters, but guardians that will manifest as long…”

    - Next → [brightport_dominio9](#d-brightport_dominio9)

    <span id="d-brightport_dominio24"></span>**`brightport_dominio24`** Long-tail-dominio: “Men without scales; humans. They came and built. The more proud and warlike tribes fought them, and the humans retaliated. Where one tribe wars, the others come to aid. And we were shattered and dispersed, our claws could not match the…”

    - “Is that why you're a different color than the lizardmen outside?” → [brightport_dominio25](#d-brightport_dominio25)

    <span id="d-brightport_dominio26_selector"></span>**`brightport_dominio26_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 90 of [The balance of scales](../quests/brightport_lizard.md#stage-90))* → [brightport_dominio26](#d-brightport_dominio26)
    - Next *(if NOT reached stage 90 of [The balance of scales](../quests/brightport_lizard.md#stage-90))* → [brightport_dominio26_alt](#d-brightport_dominio26_alt)

    <span id="d-brightport_dominio9"></span>**`brightport_dominio9`** Long-tail-dominio: “The source of that lies in two crystals within the ruins. From the two tablets I discovered that the key is chanting a specific phrase before them. We need a human like you to undertake the last step to secure our sanctuary.”

    - “Sounds easy. I'll do it.” → [brightport_dominio10](#d-brightport_dominio10)

    <span id="d-brightport_dominio25"></span>**`brightport_dominio25`** Long-tail-dominio: “The wisdom of the elders says that the scales are a reflection of one's spirit, the warlike turned red and the wise green. That the redscales have come back to the lake is no surprise, I've witnessed the conflict between humans, it left…”

    - “I see, thanks for telling me this story.” → *conversation ends*

    <span id="d-brightport_dominio26"></span>**`brightport_dominio26`** Long-tail-dominio: “The diadem you received from our chieftain is one of them. Long gone, only the pinnacle of their craftsmanship remains, a worthy reward indeed.”

    - Next *(if carry 0× [Lutarc's medallion](../items/lutarc_medallion.md))* → [brightport_dominio27](#d-brightport_dominio27)

    <span id="d-brightport_dominio26_alt"></span>**`brightport_dominio26_alt`** Long-tail-dominio: “We can speak about it later. Chief Elyzard might have one for you once you inform him of your success.”

    - “Right, I'll go inform him.” → *conversation ends*

    <span id="d-brightport_dominio10"></span>**`brightport_dominio10`** Long-tail-dominio: “Good, the specific phrase you must chant is "Kazaul thu'um kha'zan". After that deliver a solid blow to these crystals, then report back to me if this truly works. May the Shadow watch over you.” — **effects:** sets stage 70 of [The balance of scales](../quests/brightport_lizard.md#stage-70)


    <span id="d-brightport_dominio27"></span>**`brightport_dominio27`** Long-tail-dominio: “I sense another on you, a necklace we gifted to the leader of the Nor City warriors who had been here. The man, named Lutarc, asked for our help in battle against his enemies, and that day he fell on the battlefield.”

    - “He seemed to be doing alright, can't help but think compared to the diadem this necklace is on the weaker side.” → [brightport_dominio28](#d-brightport_dominio28)

    <span id="d-brightport_dominio28"></span>**`brightport_dominio28`** Long-tail-dominio: “What constitutes an artifact is its immunity to decay. Created thousands of years ago, only the magical remain. The necklace's properties seem to attract scaled creatures lesser in nature, but that is all I can tell.”

    - “I see, thanks for telling me this story.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 32 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_lizardpriest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_lizardpriest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_lizardpriest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_lizardpriest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `brightport_lizardpriest` · Data from v0.8.18</small>
