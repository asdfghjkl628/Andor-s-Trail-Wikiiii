# ![](../assets/icons/monsters/monsters_ld1_219.png){ .sprite } Fiamma

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

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Fine steel broadsword](../items/broadsword_fine_steel.md) | 100% | 1 |
| [Two-handed iron claymore](../items/clmr_irn2.md) | 100% | 1 |
| [Defender's claymore](../items/clmr_def1.md) | 100% | 1 |
| [Massive two-handed sword](../items/clmr_msv.md) | 100% | 1 |
| [Iron halberd](../items/halberd_iron.md) | 100% | 1 |

## Found on

- [brightport_weapon](../maps/brightport_weapon.md)

## Quests

- [Too hot to handle](../quests/brightport_fiamma.md): stages 5, 10, 15, 20, 25, 30, 35, 40, 45, 50
- [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md): stages 87

??? quote "Dialogue (28 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightport_fiamma_selector2"></span>**`brightport_fiamma_selector2`** *(silent check: the first matching branch below is taken)*

    - Next *(if 6 rounds passed since timer “fiamma_forge”; NOT reached stage 50 of [Too hot to handle](../quests/brightport_fiamma.md#stage-50))* → [brightport_fiamma14](#d-brightport_fiamma14)
    - Next *(if NOT 6 rounds passed since timer “fiamma_forge”; reached stage 35 of [Too hot to handle](../quests/brightport_fiamma.md#stage-35))* → [brightport_fiamma15](#d-brightport_fiamma15)
    - Next *(if reached stage 25 of [Too hot to handle](../quests/brightport_fiamma.md#stage-25); reached stage 30 of [Too hot to handle](../quests/brightport_fiamma.md#stage-30); NOT reached stage 35 of [Too hot to handle](../quests/brightport_fiamma.md#stage-35))* → [brightport_fiamma11](#d-brightport_fiamma11)
    - Next → [brightport_smith](#d-brightport_smith)

    <span id="d-brightport_fiamma14"></span>**`brightport_fiamma14`** Fiamma: “It's done! but... There is a slight problem.”

    - Next → [brightport_fiamma16](#d-brightport_fiamma16)

    <span id="d-brightport_fiamma15"></span>**`brightport_fiamma15`** Fiamma: “The sword is not done yet. Have you no patience?”


    <span id="d-brightport_fiamma11"></span>**`brightport_fiamma11`** Fiamma: “With all these quality materials, I can forge you something magnificent enough to equal the legends. Come back to me later!” — **effects:** sets stage 35 of [Too hot to handle](../quests/brightport_fiamma.md#stage-35), starts timer “fiamma_forge”


    <span id="d-brightport_smith"></span>**`brightport_smith`** [Fiamma](../monsters/brightportsmith.md): “Greetings, my name is Fiamma. I forge my swords as finely as I bake my bread.”

    - “Could you show me what you have to sell?” → [brightport_fiamma_selector](#d-brightport_fiamma_selector)
    - “That makes it sound like you're not a very good baker either.” *(if reached stage 87 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-87); NOT reached stage 20 of [Too hot to handle](../quests/brightport_fiamma.md#stage-20))* → [brightport_fiamma0](#d-brightport_fiamma0)
    - “I have the cold lava rocks and arulir skin.” *(if hand over 15× [Cold Lava Rock](../items/lava_rock_cold.md); hand over 1× [Arulir skin](../items/arulir_skin.md); NOT reached stage 25 of [Too hot to handle](../quests/brightport_fiamma.md#stage-25); reached stage 15 of [Too hot to handle](../quests/brightport_fiamma.md#stage-15); reached stage 20 of [Too hot to handle](../quests/brightport_fiamma.md#stage-20))* → [brightport_fiamma9](#d-brightport_fiamma9)
    - “I have the cold lava rocks.” *(if carry 15× [Cold Lava Rock](../items/lava_rock_cold.md); reached stage 15 of [Too hot to handle](../quests/brightport_fiamma.md#stage-15); NOT reached stage 25 of [Too hot to handle](../quests/brightport_fiamma.md#stage-25); NOT carry 1× [Arulir skin](../items/arulir_skin.md))* → [brightport_fiamma_rocks](#d-brightport_fiamma_rocks)
    - “I have the red crystal here.” *(if hand over 1× [Red Crystals](../items/crystal_red.md); NOT reached stage 30 of [Too hot to handle](../quests/brightport_fiamma.md#stage-30); reached stage 20 of [Too hot to handle](../quests/brightport_fiamma.md#stage-20))* → [brightport_fiamma10](#d-brightport_fiamma10)

    <span id="d-brightport_fiamma16"></span>**`brightport_fiamma16`** Fiamma: “I've quenched it, but when I try to pull it out of the water, it reacts to the air and starts heating up. It quickly becomes unbearable to hold.”

    - Next → [brightport_fiamma17](#d-brightport_fiamma17)

    <span id="d-brightport_fiamma_selector"></span>**`brightport_fiamma_selector`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 87 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-87)

    - branch 1 → *shop opens*

    <span id="d-brightport_fiamma0"></span>**`brightport_fiamma0`** Fiamma: “Hey kid, you might be right about the swords, but don't ever insult my baking skills!”

    - Next → [brightport_fiamma1](#d-brightport_fiamma1)

    <span id="d-brightport_fiamma9"></span>**`brightport_fiamma9`** Fiamma: “Yes, those look good. Thanks!” — **effects:** sets stage 25 of [Too hot to handle](../quests/brightport_fiamma.md#stage-25)

    - Next → [brightport_fiamma_selector1](#d-brightport_fiamma_selector1)

    <span id="d-brightport_fiamma_rocks"></span>**`brightport_fiamma_rocks`** Fiamma: “That's good, $playername. But I still need a strip of arulir skin to go along with them.”


    <span id="d-brightport_fiamma10"></span>**`brightport_fiamma10`** Fiamma: “Wow. It looks magnificent!” — **effects:** sets stage 30 of [Too hot to handle](../quests/brightport_fiamma.md#stage-30)

    - Next → [brightport_fiamma_selector1](#d-brightport_fiamma_selector1)

    <span id="d-brightport_fiamma17"></span>**`brightport_fiamma17`** Fiamma: “I was hoping to keep the Arulir skin for a pair of forging gloves, but I ended up making these smaller, heat-resistant gloves, to wield this magnificent two-handed sword I crafted from the materials you brought me.” — **effects:** sets stage 40 of [Too hot to handle](../quests/brightport_fiamma.md#stage-40)

    - “Two-handed sword? I thought you would make me a regular sword.” → [brightport_fiamma18](#d-brightport_fiamma18)
    - “Sounds nice, I'll take it.” → [brightport_fiamma20](#d-brightport_fiamma20)

    <span id="d-brightport_fiamma1"></span>**`brightport_fiamma1`** Fiamma: “Unfortunately, it's not about my skill but the quality of the steel. If I had the materials, I could forge good swords all day.”

    - “If I brought you materials, could you forge me something with them?” → [brightport_fiamma](#d-brightport_fiamma)
    - “What's wrong with the steel?” → [brightport_fiamma2](#d-brightport_fiamma2)

    <span id="d-brightport_fiamma_selector1"></span>**`brightport_fiamma_selector1`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 30 of [Too hot to handle](../quests/brightport_fiamma.md#stage-30); reached stage 25 of [Too hot to handle](../quests/brightport_fiamma.md#stage-25))* → [brightport_fiamma11](#d-brightport_fiamma11)
    - Next *(if reached stage 30 of [Too hot to handle](../quests/brightport_fiamma.md#stage-30); NOT reached stage 25 of [Too hot to handle](../quests/brightport_fiamma.md#stage-25))* → [brightport_fiamma12](#d-brightport_fiamma12)
    - Next *(if NOT reached stage 30 of [Too hot to handle](../quests/brightport_fiamma.md#stage-30); reached stage 25 of [Too hot to handle](../quests/brightport_fiamma.md#stage-25))* → [brightport_fiamma13](#d-brightport_fiamma13)

    <span id="d-brightport_fiamma18"></span>**`brightport_fiamma18`** Fiamma: “Hey, you didn't specify, so I made what I know best.”

    - “Could you forge me something else with the same materials then?” → [brightport_fiamma19](#d-brightport_fiamma19)

    <span id="d-brightport_fiamma20"></span>**`brightport_fiamma20`** Fiamma: “Well, usually I would have my reservations about giving someone as young as you something this dangerous. But you're the one who fought those dangerous creatures, so my worries are unfounded. Take it, and use it well.” — **effects:** sets stage 50 of [Too hot to handle](../quests/brightport_fiamma.md#stage-50), gives 1× [Flaming greatsword](../items/brightportflamesword.md), gives 1× [Salamander gloves](../items/brightport_glove.md)

    - “Thanks, I will!” → *conversation ends*
    - “[I'll probably keep it as a trophy]” → *conversation ends*

    <span id="d-brightport_fiamma"></span>**`brightport_fiamma`** Fiamma: “I would gladly forge you something, but it would require much effort on your part. If that's alright with you.”

    - “There is no task beyond my skill.” → [brightport_fiamma3](#d-brightport_fiamma3)
    - “Ha! You're speaking with a seasoned adventurer, I can do it!” → [brightport_fiamma3](#d-brightport_fiamma3)

    <span id="d-brightport_fiamma2"></span>**`brightport_fiamma2`** Fiamma: “All the metal we're getting now is lower quality scraps. Feygard has been deliberately interfering with the trade, creating a shortage so that blacksmiths in towns like Vilegard and ours, which were affiliated with Nor City, can't forge…”

    - “What would you say if I brought you some quality materials?” → [brightport_fiamma](#d-brightport_fiamma)

    <span id="d-brightport_fiamma12"></span>**`brightport_fiamma12`** Fiamma: “What a clear crystal! But I still need the lava rocks for fuel, and the arulir skin. Bring them to me and I can start.”


    <span id="d-brightport_fiamma13"></span>**`brightport_fiamma13`** Fiamma: “Remember, I still need that red crystal to forge the blade. Bring it to me, and I can start.”


    <span id="d-brightport_fiamma19"></span>**`brightport_fiamma19`** Fiamma: “Frankly, I don't feel like forging another sword for you, but I can give you something else instead, and keep the sword for myself if you don't like it.”

    - “Yes, I would prefer that.” → [brightport_fiamma21](#d-brightport_fiamma21)
    - “Sorry, I'll keep the sword instead.” → [brightport_fiamma20](#d-brightport_fiamma20)

    <span id="d-brightport_fiamma3"></span>**`brightport_fiamma3`** Fiamma: “OK. First, we have to discuss the materials I have in mind. I presume you have heard of the town of Remgard?” — **effects:** sets stage 5 of [Too hot to handle](../quests/brightport_fiamma.md#stage-5)

    - “Yes I have heard of it.” → [brightport_fiamma5](#d-brightport_fiamma5)
    - “No, I have not.” → [brightport_fiamma4](#d-brightport_fiamma4)

    <span id="d-brightport_fiamma21"></span>**`brightport_fiamma21`** Fiamma: “Take this glaive, it was given to me by my old master from Nor City. It was originally forged for nobility but after lord Emeric's defeat in the noble wars. The Imeria branch of house Houdart fell from grace, and this was sold for cheap…” — **effects:** sets stage 45 of [Too hot to handle](../quests/brightport_fiamma.md#stage-45), gives 1× [Glaive of Imeria](../items/glaive_butcher.md), sets stage 50 of [Too hot to handle](../quests/brightport_fiamma.md#stage-50)

    - “That's really cool. Thanks!” → *conversation ends*
    - “[I don't use pole weapons either...]” → *conversation ends*

    <span id="d-brightport_fiamma5"></span>**`brightport_fiamma5`** Fiamma: “Many travelers pass through Brightport on their way to and back from Remgard. The town lies high in the mountains, and from those travelers I heard of beasts called arulirs, harassing travelers along a short stretch of the road.” — **effects:** sets stage 10 of [Too hot to handle](../quests/brightport_fiamma.md#stage-10)

    - Next → [brightport_fiamma6](#d-brightport_fiamma6)

    <span id="d-brightport_fiamma4"></span>**`brightport_fiamma4`** Fiamma: “If so, then listen closely, as you are about to hear of it.”

    - Next → [brightport_fiamma5](#d-brightport_fiamma5)

    <span id="d-brightport_fiamma6"></span>**`brightport_fiamma6`** Fiamma: “But what's most interesting is their origin. The area they now inhabit was a mining camp, which was abandoned after the caves became unstable. Out of the depths, gornauds clawed a tunnel, releasing arulirs from the fiery depths they…”

    - Next → [brightport_fiamma7](#d-brightport_fiamma7)

    <span id="d-brightport_fiamma7"></span>**`brightport_fiamma7`** Fiamma: “First, if you can travel there, I want a strip of the arulir's skin - rumored to be tougher than steel but as flexible as leather. Second, I want 15 cooled down lava rocks from inside the mountain cave. These will fuel my forge better…” — **effects:** sets stage 15 of [Too hot to handle](../quests/brightport_fiamma.md#stage-15)

    - Next → [brightport_fiamma8](#d-brightport_fiamma8)

    <span id="d-brightport_fiamma8"></span>**`brightport_fiamma8`** Fiamma: “And lastly, the material from which I will forge a blade, a red crystal from a gornaud. This material, which their teeth and claws are made of, can easily crush rock. Only in rare cases, the mineral gathers and forms crystal clusters on…” — **effects:** sets stage 20 of [Too hot to handle](../quests/brightport_fiamma.md#stage-20)

    - “I'm on my way.” → *conversation ends*
    - “I'll get there eventually.” → *conversation ends*



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportsmith.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportsmith.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportsmith.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportsmith.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `brightportsmith` · Data from v0.8.18</small>
