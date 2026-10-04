# ![](../assets/icons/monsters/monsters_ld1_22.png){ .sprite } Edrin

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

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Fancy letter opener](../items/letter_opener.md) | 100% | 1 |
| [Polished necklace](../items/junk_necklace1.md) | 100% | 1 |
| [Superior steel dagger](../items/dagger_steel_superior.md) | 100% | 1 |
| [Ring of damage +3](../items/ring_dmg_3.md) | 100% | 1 |
| [Jeweled dagger](../items/dagger_jeweled.md) | 100% | 1 |
| [Inlaid scepter](../items/scepter_inlaid.md) | 100% | 1 |

## Found on

- [brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)

## Quests

- [A strange looking dagger](../quests/brv_dagger.md): stages 10, 20, 25, 50, 60, 70, 80, 90, 100
- [Delivery - nondisplay (hidden flag)](../quests/brv_wh_delivery_nondisplay.md): stages 20

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Edrin. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/edrin_0_0.json" data-npc="Edrin" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (26 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-edrin_0_0"></span>**`edrin_0_0`** Edrin: “Hello.”

    - “Have you repaired the dagger?” *(if reached stage 80 of [A strange looking dagger](../quests/brv_dagger.md#stage-80); NOT reached stage 70 of [A strange looking dagger](../quests/brv_dagger.md#stage-70); NOT reached stage 90 of [A strange looking dagger](../quests/brv_dagger.md#stage-90); NOT reached stage 100 of [A strange looking dagger](../quests/brv_dagger.md#stage-100))* → [edrin_7_0](#d-edrin_7_0)
    - “I have a gem. I think it's the right one for the dagger we discussed.” *(if reached stage 10 of [A strange looking dagger](../quests/brv_dagger.md#stage-10); NOT reached stage 25 of [A strange looking dagger](../quests/brv_dagger.md#stage-25); NOT reached stage 70 of [A strange looking dagger](../quests/brv_dagger.md#stage-70); NOT reached stage 80 of [A strange looking dagger](../quests/brv_dagger.md#stage-80); NOT reached stage 90 of [A strange looking dagger](../quests/brv_dagger.md#stage-90); NOT reached stage 100 of [A strange looking dagger](../quests/brv_dagger.md#stage-100); carry 1× [A strange-looking gem](../items/strange_gem.md); carry 1× [A strange looking dagger](../items/strange_dagger.md))* → [edrin_5_0](#d-edrin_5_0)
    - “I have a dagger. I think it's the one that matches the gem we discussed.” *(if reached stage 20 of [A strange looking dagger](../quests/brv_dagger.md#stage-20); NOT reached stage 25 of [A strange looking dagger](../quests/brv_dagger.md#stage-25); NOT reached stage 70 of [A strange looking dagger](../quests/brv_dagger.md#stage-70); NOT reached stage 80 of [A strange looking dagger](../quests/brv_dagger.md#stage-80); NOT reached stage 90 of [A strange looking dagger](../quests/brv_dagger.md#stage-90); NOT reached stage 100 of [A strange looking dagger](../quests/brv_dagger.md#stage-100); carry 1× [A strange looking dagger](../items/strange_dagger.md); carry 1× [A strange-looking gem](../items/strange_gem.md))* → [edrin_6_0](#d-edrin_6_0)
    - “Who are you?” → [edrin_0](#d-edrin_0)
    - “I'm looking for my brother, Andor. Have you seen anyone around town that looks a bit like me?” → [edrin_1a](#d-edrin_1a)
    - “Do you have anything to trade?” → *shop opens*
    - “Hello, did you order a 'Striped Hammer'?” *(if hand over 1× [Striped hammer](../items/brv_wh_item_08.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 30 of [Delivery](../quests/brv_wh_delivery.md#stage-30))* → [brv_wh_delivery_edrin](#d-brv_wh_delivery_edrin)

    <span id="d-edrin_7_0"></span>**`edrin_7_0`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if 30 rounds passed since timer “Dagger_repair”; NOT reached stage 30 of [brv_dagger_nondisplay (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-30); NOT reached stage 40 of [brv_dagger_nondisplay (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-40))* → [edrin_7_1a](#d-edrin_7_1a)
    - branch 2 *(if 30 rounds passed since timer “Dagger_repair”)* → [edrin_7_1b](#d-edrin_7_1b)
    - branch 3 → [edrin_7_1c](#d-edrin_7_1c)

    <span id="d-edrin_5_0"></span>**`edrin_5_0`** Edrin: “Yes, that's the one that matches the dagger! Now that I have both pieces, I can repair the dagger for you if you wish.” — **effects:** sets stage 50 of [A strange looking dagger](../quests/brv_dagger.md#stage-50)

    - “How much will that cost?” → [edrin_5_1](#d-edrin_5_1)
    - “I'll think about it.” → *conversation ends*

    <span id="d-edrin_6_0"></span>**`edrin_6_0`** Edrin: “Yes, that's the one that matches the gem! Now that I have both pieces, I can repair the dagger for you if you wish.” — **effects:** sets stage 50 of [A strange looking dagger](../quests/brv_dagger.md#stage-50)

    - “How much will that cost?” → [edrin_6_1](#d-edrin_6_1)
    - “I'll think about it” → *conversation ends*

    <span id="d-edrin_0"></span>**`edrin_0`** Edrin: “I'm Edrin, the Brimhaven metalsmith.”

    - “What does a metalsmith do? Is that the same as a blacksmith?” → [edrin_1](#d-edrin_1)
    - “I don't think that's what I'm looking for. Thanks anyway.” → *conversation ends*
    - “Please show me what you have to trade.” → *shop opens*

    <span id="d-edrin_1a"></span>**`edrin_1a`** Edrin: “Well, yes, there was someone. He came to me to get a sword sharpened. I can't tell you any more than that though.”

    - “OK. Thanks. What type of services and products do you supply?” → [edrin_1](#d-edrin_1)

    <span id="d-brv_wh_delivery_edrin"></span>**`brv_wh_delivery_edrin`** Edrin: “Ah, yes, a striped hammer. Don't look so impatient. Here's my delivery charge, and now you can leave!” — **effects:** clears stage 30 of [Delivery](../quests/brv_wh_delivery.md#stage-30), sets stage 20 of [Delivery - nondisplay (hidden flag)](../quests/brv_wh_delivery_nondisplay.md#stage-20), gives 10× [Gold coins](../items/gold.md)

    - “Thank you.” → *conversation ends*

    <span id="d-edrin_7_1a"></span>**`edrin_7_1a`** Edrin: “Yes, it is done. Here is the repaired dagger. It's nice to see Lawellyn's dagger brought back to its original glory. There is some mystery about his death. I don't know anything about it though. Maybe someone else in town can tell you more.” — **effects:** gives 1× [Assassin's blade](../items/dagger_assassin.md), sets stage 90 of [A strange looking dagger](../quests/brv_dagger.md#stage-90)


    <span id="d-edrin_7_1b"></span>**`edrin_7_1b`** Edrin: “Yes, it is done. Here is the repaired dagger. It's nice to see Lawellyn's dagger brought back to its original glory. There is some mystery about his death. I don't know anything about it though. Maybe someone else in town can tell you more.” — **effects:** gives 1× [Assassin's blade](../items/dagger_assassin.md), sets stage 100 of [A strange looking dagger](../quests/brv_dagger.md#stage-100)


    <span id="d-edrin_7_1c"></span>**`edrin_7_1c`** Edrin: “No, not yet. You must have patience. I told you this is a difficult repair.”


    <span id="d-edrin_5_1"></span>**`edrin_5_1`** Edrin: “The best I can offer is 800 gold. The repair is quite delicate, and if done incorrectly it will just be a dagger with a gem in the pommel, and no more.”

    - “That's expensive. I'll think about it.” → [edrin_5_2c](#d-edrin_5_2c)
    - “That's too expensive. I'll keep the dagger and the gem I have.” → [edrin_5_2a](#d-edrin_5_2a)
    - “OK. I agree. Here are the dagger and the gem.” *(if pay 800 gold; hand over 1× [A strange looking dagger](../items/strange_dagger.md); hand over 1× [A strange-looking gem](../items/strange_gem.md))* → [edrin_5_2b](#d-edrin_5_2b)

    <span id="d-edrin_6_1"></span>**`edrin_6_1`** Edrin: “The best I can offer is 800 gold. The repair is quite delicate, and if done incorrectly it will just be a dagger with a gem in the pommel, and no more.”

    - “That's expensive. I'll think about it.” → [edrin_6_2c](#d-edrin_6_2c)
    - “That's too expensive. I'll keep the dagger and the gem I have.” → [edrin_6_2a](#d-edrin_6_2a)
    - “OK. I agree. Here are the dagger and the gem.” *(if pay 800 gold; hand over 1× [A strange looking dagger](../items/strange_dagger.md); hand over 1× [A strange-looking gem](../items/strange_gem.md))* → [edrin_6_2b](#d-edrin_6_2b)

    <span id="d-edrin_1"></span>**`edrin_1`** Edrin: “As a metalsmith I'm sort of like a blacksmith, but there is a difference. A blacksmith works with iron and steel, but a metalsmith works with many metals. I do work with iron and steel, but only for smaller, high quality objects. I also…”

    - “If you have those skills I would like you to look at two items I purchased locally. A strange-looking dagger and a…” *(if carry 1× [A strange looking dagger](../items/strange_dagger.md); carry 1× [A strange-looking gem](../items/strange_gem.md); NOT reached stage 10 of [A strange looking dagger](../quests/brv_dagger.md#stage-10); NOT reached stage 20 of [A strange looking dagger](../quests/brv_dagger.md#stage-20); NOT reached stage 80 of [A strange looking dagger](../quests/brv_dagger.md#stage-80); NOT reached stage 70 of [A strange looking dagger](../quests/brv_dagger.md#stage-70))* → [edrin_4_1](#d-edrin_4_1)
    - “If you have those skills I would like you to look at something I purchased locally. A strange-looking dagger.” *(if carry 1× [A strange looking dagger](../items/strange_dagger.md); NOT reached stage 70 of [A strange looking dagger](../quests/brv_dagger.md#stage-70); NOT reached stage 50 of [A strange looking dagger](../quests/brv_dagger.md#stage-50); NOT reached stage 25 of [A strange looking dagger](../quests/brv_dagger.md#stage-25); NOT reached stage 80 of [A strange looking dagger](../quests/brv_dagger.md#stage-80); NOT reached stage 20 of [A strange looking dagger](../quests/brv_dagger.md#stage-20); NOT carry 1× [A strange-looking gem](../items/strange_gem.md))* → [edrin_2_1](#d-edrin_2_1)
    - “If you have those skills I would like you to look at something I purchased locally. A strange-looking gem.” *(if carry 1× [A strange-looking gem](../items/strange_gem.md); NOT reached stage 70 of [A strange looking dagger](../quests/brv_dagger.md#stage-70); NOT reached stage 50 of [A strange looking dagger](../quests/brv_dagger.md#stage-50); NOT reached stage 25 of [A strange looking dagger](../quests/brv_dagger.md#stage-25); NOT reached stage 80 of [A strange looking dagger](../quests/brv_dagger.md#stage-80); NOT reached stage 10 of [A strange looking dagger](../quests/brv_dagger.md#stage-10); NOT carry 1× [A strange looking dagger](../items/strange_dagger.md))* → [edrin_3_1](#d-edrin_3_1)
    - “That's Interesting, but let's talk about something else.” → [edrin_0_0](#d-edrin_0_0)
    - “I don't think I need the services of a metalsmith right now.” → *conversation ends*

    <span id="d-edrin_5_2c"></span>**`edrin_5_2c`** Edrin: “Feel free to come back when you decide.” — **effects:** sets stage 60 of [A strange looking dagger](../quests/brv_dagger.md#stage-60)


    <span id="d-edrin_5_2a"></span>**`edrin_5_2a`** Edrin: “That is up to you, although I think you have made a mistake.” — **effects:** sets stage 70 of [A strange looking dagger](../quests/brv_dagger.md#stage-70)


    <span id="d-edrin_5_2b"></span>**`edrin_5_2b`** Edrin: “This will take me some time. Please come back later to collect the repaired dagger.” — **effects:** sets stage 80 of [A strange looking dagger](../quests/brv_dagger.md#stage-80), starts timer “Dagger_repair”


    <span id="d-edrin_6_2c"></span>**`edrin_6_2c`** Edrin: “Feel free to come back when you decide.” — **effects:** sets stage 60 of [A strange looking dagger](../quests/brv_dagger.md#stage-60)


    <span id="d-edrin_6_2a"></span>**`edrin_6_2a`** Edrin: “That is up to you, although I think you have made a mistake.” — **effects:** sets stage 70 of [A strange looking dagger](../quests/brv_dagger.md#stage-70)


    <span id="d-edrin_6_2b"></span>**`edrin_6_2b`** Edrin: “This will take me some time. Please come back later to collect the repaired dagger.” — **effects:** sets stage 80 of [A strange looking dagger](../quests/brv_dagger.md#stage-80), starts timer “Dagger_repair”


    <span id="d-edrin_4_1"></span>**`edrin_4_1`** Edrin: “I recognize these. I made the dagger, many years ago, for a man called Lawellyn. Alas, I hear he is now dead. See this recess in the pommel? The gem you have fits in that. It gave the dagger some special properties. If you wish, I can…” — **effects:** sets stage 25 of [A strange looking dagger](../quests/brv_dagger.md#stage-25)

    - “How much will that cost?” → [edrin_4_2](#d-edrin_4_2)
    - “I'll think about it.” → *conversation ends*

    <span id="d-edrin_2_1"></span>**`edrin_2_1`** Edrin: “I recognize this. I made it, many years ago, for a man called Lawellyn. Alas, I hear he is now dead. See this recess in the pommel? There used to be an unusual gem in that. It gave the dagger some special properties. If you can find the…” — **effects:** sets stage 10 of [A strange looking dagger](../quests/brv_dagger.md#stage-10)

    - “I think I know where to find that. I'll go and get it.” → *conversation ends*
    - “OK. Thanks for the information.” → *conversation ends*
    - “Let's talk about something else.” → [edrin_0_0](#d-edrin_0_0)

    <span id="d-edrin_3_1"></span>**`edrin_3_1`** Edrin: “I recognize this. It was used in something I made, many years ago. It was set into the pommel of a dagger I made for a man called Lawellyn. Alas, I hear he is now dead. It gave the dagger some special properties. If you can find the…” — **effects:** sets stage 20 of [A strange looking dagger](../quests/brv_dagger.md#stage-20)

    - “I think I know where to find that. I'll be right back.” → *conversation ends*
    - “Maybe if I find the time I'll look for it. Let's talk about something else.” → [edrin_0_0](#d-edrin_0_0)
    - “OK. Thanks for the information.” → *conversation ends*

    <span id="d-edrin_4_2"></span>**`edrin_4_2`** Edrin: “The best I can offer is 800 gold. The repair is quite delicate, and if done incorrectly it will just be a dagger with a gem in the pommel, and no more.”

    - “That's expensive. I'll think about it.” → [edrin_4_3c](#d-edrin_4_3c)
    - “That's too expensive. I'll keep the dagger and the gem I have.” → [edrin_4_3a](#d-edrin_4_3a)
    - “OK. I agree. Here are the dagger and the gem.” *(if pay 800 gold; hand over 1× [A strange looking dagger](../items/strange_dagger.md); hand over 1× [A strange-looking gem](../items/strange_gem.md))* → [edrin_4_3b](#d-edrin_4_3b)

    <span id="d-edrin_4_3c"></span>**`edrin_4_3c`** Edrin: “Feel free to come back when you decide.” — **effects:** sets stage 60 of [A strange looking dagger](../quests/brv_dagger.md#stage-60)


    <span id="d-edrin_4_3a"></span>**`edrin_4_3a`** Edrin: “That is up to you, although I think you have made a mistake.” — **effects:** sets stage 70 of [A strange looking dagger](../quests/brv_dagger.md#stage-70)


    <span id="d-edrin_4_3b"></span>**`edrin_4_3b`** Edrin: “This will take me some time. Please come back later to collect the repaired dagger.” — **effects:** sets stage 80 of [A strange looking dagger](../quests/brv_dagger.md#stage-80), starts timer “Dagger_repair”




## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 25 lines added |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 8 lines changed<br>· text: “Yes, it is done. Here is the repaired dagger.” → “Yes, it is done. Here is the repaired dagger. It's nice to see Lawell…”<br>· text: “I recognize this. I made it, many years ago. See this recess in the p…” → “I recognize this. I made it, many years ago, for a man called Lawelly…” |
| [v0.7.17](../versions/0.7.17.md) | Dialogue: 1 line added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_metalsmith.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_metalsmith.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_metalsmith.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_metalsmith.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `brv_metalsmith` · Data from v0.8.18</small>
