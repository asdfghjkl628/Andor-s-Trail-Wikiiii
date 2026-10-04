# ![](../assets/icons/monsters/monsters_mage2_0.png){ .sprite } Potion merchant

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_mage2_0.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `potion_merchant` |
| **Type** | Shopkeeper |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Fallhaven |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Small empty vial](../items/vial_empty1.md) | 100% | 10 |
| [Empty vial](../items/vial_empty2.md) | 100% | 10 |
| [Empty flask](../items/vial_empty3.md) | 100% | 10 |
| [Empty potion bottle](../items/vial_empty4.md) | 100% | 10 |
| [Minor potion of health](../items/health_minor2.md) | 100% | 10 |
| [Regular potion of health](../items/health.md) | 100% | 10 |
| [Major potion of health](../items/health_major2.md) | 100% | 10 |
| [Milk](../items/milk.md) | 100% | 10 |
| [Rat tail](../items/rat_tail.md) | 100% | 5 |
| [Radish](../items/radish.md) | 100% | 5 |
| [Strawberry](../items/strawberry.md) | 100% | 5 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [fallhaven_potions](../maps/fallhaven_potions.md) | Fallhaven | 1 | – |


## Quests

- [Fungi panic](../quests/fungi_panic.md): stages 20, 50
- [Lodar's potions](../quests/lodar_pots.md): stages 20
- [Taste is everything](../quests/antifoodp.md): stages 15, 20, 30, 35, 40

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Potion merchant. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/fallhaven_potions.json" data-npc="Potion merchant" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (48 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-fallhaven_potions"></span>**`fallhaven_potions`** Potion merchant: “Welcome to my shop. Please browse my fine selection of everyday potions.”

    - “Let me see what potions you have available.” → *shop opens*
    - “Do you have anything to help against food-poisoning?” → [fallhaven_pot_antifoodp1](#d-fallhaven_pot_antifoodp1)
    - “I was told that I can get some Spotted Hornbeam fungus from you.” *(if reached stage 10 of [Lodar's potions](../quests/lodar_pots.md#stage-10))* → [fallhaven_potions1](#d-fallhaven_potions1)
    - “Can you sell me a special crystal vial?” *(if reached stage 78 of [A quick glance](../quests/quick_glance.md#stage-78))* → [fallhaven_potions_offer_crystal_vial](#d-fallhaven_potions_offer_crystal_vial)
    - “Bogsten is sick after encountering a giant mushroom. He asked me to get a cure for him.” *(if reached stage 10 of [Fungi panic](../quests/fungi_panic.md#stage-10); NOT reached stage 20 of [Fungi panic](../quests/fungi_panic.md#stage-20))* → [fungi_panic_potioner_10](#d-fungi_panic_potioner_10)
    - “Here are four samples of mushroom spores. Can you help Bogsten now?” *(if carry 4× [Spores of the giant mushroom](../items/fungi_panic_spores.md); NOT reached stage 60 of [Fungi panic](../quests/fungi_panic.md#stage-60))* → [fungi_panic_potioner_50](#d-fungi_panic_potioner_50)
    - “Here's a sample of the mushroom spores. Can you help Bogsten now?” *(if carry 1× [Spores of the giant mushroom](../items/fungi_panic_spores.md); NOT reached stage 60 of [Fungi panic](../quests/fungi_panic.md#stage-60); NOT carry 4× [Spores of the giant mushroom](../items/fungi_panic_spores.md))* → [fungi_panic_potioner_50a](#d-fungi_panic_potioner_50a)
    - “Here are some of Bogsten's mushrooms.” *(if hand over 1× [Bag with mushrooms](../items/fungi_panic_bag.md))* → [fungi_panic_potioner_100](#d-fungi_panic_potioner_100)

    <span id="d-fallhaven_pot_antifoodp1"></span>**`fallhaven_pot_antifoodp1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 40 of [Taste is everything](../quests/antifoodp.md#stage-40))* → [fallhaven_pot_antifoodp5](#d-fallhaven_pot_antifoodp5)
    - branch 2 *(if reached stage 35 of [Taste is everything](../quests/antifoodp.md#stage-35))* → [fallhaven_pot_antifp_q4](#d-fallhaven_pot_antifp_q4)
    - branch 3 *(if reached stage 30 of [Taste is everything](../quests/antifoodp.md#stage-30))* → [fallhaven_pot_antifp_q2](#d-fallhaven_pot_antifp_q2)
    - branch 4 *(if reached stage 20 of [Taste is everything](../quests/antifoodp.md#stage-20))* → [fallhaven_pot_antifoodp5](#d-fallhaven_pot_antifoodp5)
    - branch 5 → [fallhaven_pot_antifoodp2](#d-fallhaven_pot_antifoodp2)

    <span id="d-fallhaven_potions1"></span>**`fallhaven_potions1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 20 of [Lodar's potions](../quests/lodar_pots.md#stage-20))* → [fallhaven_potions4](#d-fallhaven_potions4)
    - branch 2 → [fallhaven_potions2](#d-fallhaven_potions2)

    <span id="d-fallhaven_potions_offer_crystal_vial"></span>**`fallhaven_potions_offer_crystal_vial`** Potion merchant: “Yes, I have some crystal vials. I can sell you one for 50 gold pieces.”

    - “That is too expensive for me.” → [fallhaven_potions_offer_crystal_vial_too_expensive](#d-fallhaven_potions_offer_crystal_vial_too_expensive)
    - “I'll take one.” *(if pay 50 gold)* → [fallhaven_potions_buy_crystal_vial](#d-fallhaven_potions_buy_crystal_vial)

    <span id="d-fungi_panic_potioner_10"></span>**`fungi_panic_potioner_10`** Potion merchant: “Bogsten? I haven't heard from that old boy in a long time now. I was starting to wonder if he was still alive.”

    - “He is alive, but only barely. He didn't even make it to Fallhaven to ask for help.” → [fungi_panic_potioner_20](#d-fungi_panic_potioner_20)
    - “Stop talking. Just give me the cure.” → [fungi_panic_potioner_12](#d-fungi_panic_potioner_12)

    <span id="d-fungi_panic_potioner_50"></span>**`fungi_panic_potioner_50`** Potion merchant: “Let me see... Ah, yes. A fungus maximus, also known as 'Giant mushroom'. Its wounds are deadly if not cured properly.”

    - Next → [fungi_panic_potioner_52](#d-fungi_panic_potioner_52)

    <span id="d-fungi_panic_potioner_50a"></span>**`fungi_panic_potioner_50a`** Potion merchant: “A sample? This won't do. I'll need at least four samples for my work.”

    - “I see. I'll be back with more in just a moment.” → *conversation ends*

    <span id="d-fungi_panic_potioner_100"></span>**`fungi_panic_potioner_100`** Potion merchant: “Oh. Thank you.”

    - “Hey! Aren't you going to give me something interesting for it?” → [fungi_panic_potioner_110](#d-fungi_panic_potioner_110)

    <span id="d-fallhaven_pot_antifoodp5"></span>**`fallhaven_pot_antifoodp5`** Potion merchant: “To make the potion against food-poisoning, I would need one poison gland and two pieces of animal hair. I will also require 50 gold for the work required.” — **effects:** sets stage 20 of [Taste is everything](../quests/antifoodp.md#stage-20)

    - “I'll be right back with those ingredients.” → [fallhaven_pot_antifoodp6](#d-fallhaven_pot_antifoodp6)
    - “Any ideas where I can find those ingredients?” → [fallhaven_pot_antifoodp7](#d-fallhaven_pot_antifoodp7)
    - “I have those ingredients for you.” *(if hand over 1× [Poison gland](../items/gland.md); hand over 2× [Animal hair](../items/hair.md); pay 50 gold; NOT reached stage 35 of [Taste is everything](../quests/antifoodp.md#stage-35))* → [fallhaven_pot_antifp_q1](#d-fallhaven_pot_antifp_q1)
    - “I have those ingredients for you.” *(if hand over 1× [Poison gland](../items/gland.md); hand over 2× [Animal hair](../items/hair.md); pay 50 gold; reached stage 35 of [Taste is everything](../quests/antifoodp.md#stage-35))* → [fallhaven_pot_antifp_q3](#d-fallhaven_pot_antifp_q3)
    - “Here, I have enough of those ingredients for five potions.” *(if hand over 5× [Poison gland](../items/gland.md); hand over 10× [Animal hair](../items/hair.md); pay 250 gold; reached stage 35 of [Taste is everything](../quests/antifoodp.md#stage-35))* → [fallhaven_pot_antifp_q3x5](#d-fallhaven_pot_antifp_q3x5)
    - “Here, I have enough of those ingredients for ten potions.” *(if hand over 10× [Poison gland](../items/gland.md); hand over 20× [Animal hair](../items/hair.md); pay 500 gold; reached stage 35 of [Taste is everything](../quests/antifoodp.md#stage-35))* → [fallhaven_pot_antifp_q3x10](#d-fallhaven_pot_antifp_q3x10)

    <span id="d-fallhaven_pot_antifp_q4"></span>**`fallhaven_pot_antifp_q4`** Potion merchant: “I can create more of those potions if you want. You'll have to bring me more of those ingredients then.” — **effects:** sets stage 40 of [Taste is everything](../quests/antifoodp.md#stage-40)

    - “Thank you.” → *conversation ends*
    - “I sure hope this mixture of your works.” → *conversation ends*

    <span id="d-fallhaven_pot_antifp_q2"></span>**`fallhaven_pot_antifp_q2`** Potion merchant: “[Mixes the ingredients]”

    - Next → [fallhaven_pot_antifp_q3](#d-fallhaven_pot_antifp_q3)

    <span id="d-fallhaven_pot_antifoodp2"></span>**`fallhaven_pot_antifoodp2`** Potion merchant: “Oh yes, I have a recipe for a mixture that helps against food poisoning. If you want, I could create some of that for you.” — **effects:** sets stage 15 of [Taste is everything](../quests/antifoodp.md#stage-15)

    - “Sounds good, what do you need from me?” → [fallhaven_pot_antifoodp3](#d-fallhaven_pot_antifoodp3)

    <span id="d-fallhaven_potions4"></span>**`fallhaven_potions4`** Potion merchant: “I already gave you some, before. Don't tell me you lost it?”


    <span id="d-fallhaven_potions2"></span>**`fallhaven_potions2`** Potion merchant: “Oh yes. Really disgusting smell, they have. But good for making potions.”

    - Next → [fallhaven_potions3](#d-fallhaven_potions3)

    <span id="d-fallhaven_potions_offer_crystal_vial_too_expensive"></span>**`fallhaven_potions_offer_crystal_vial_too_expensive`** Potion merchant: “Well, that's the price.”

    - Next → [fallhaven_potions](#d-fallhaven_potions)

    <span id="d-fallhaven_potions_buy_crystal_vial"></span>**`fallhaven_potions_buy_crystal_vial`** Potion merchant: “Here is your crystal vial. Thanks for the 50 gold pieces.” — **effects:** gives 1× [Empty crystal vial](../items/empty_crystal_vial.md)

    - Next → [fallhaven_potions](#d-fallhaven_potions)

    <span id="d-fungi_panic_potioner_20"></span>**`fungi_panic_potioner_20`** Potion merchant: “And now I have to rescue him again. Well, what did he do to himself this time?”

    - “A giant mushroom attacked him.” → [fungi_panic_potioner_40](#d-fungi_panic_potioner_40)
    - “This time? Did he ask for help before?” → [fungi_panic_potioner_22](#d-fungi_panic_potioner_22)

    <span id="d-fungi_panic_potioner_12"></span>**`fungi_panic_potioner_12`** Potion merchant: “[muttering] ... grumble ... cheeky kids, grumble ...”

    - Next → [fungi_panic_potioner_40](#d-fungi_panic_potioner_40)

    <span id="d-fungi_panic_potioner_52"></span>**`fungi_panic_potioner_52`** Potion merchant: “I'm glad that I have the right potion for it. You can have it for only 150 gold coins.”

    - “That much!” → [fungi_panic_potioner_54](#d-fungi_panic_potioner_54)
    - “OK, here you are.” *(if pay 150 gold; hand over 4× [Spores of the giant mushroom](../items/fungi_panic_spores.md))* → [fungi_panic_potioner_60](#d-fungi_panic_potioner_60)

    <span id="d-fungi_panic_potioner_110"></span>**`fungi_panic_potioner_110`** Potion merchant: “I could, yes. But I won't.”

    - “That's robbery! I won't let you get away with it!” → [fungi_panic_potioner_111](#d-fungi_panic_potioner_111)

    <span id="d-fallhaven_pot_antifoodp6"></span>**`fallhaven_pot_antifoodp6`** Potion merchant: “Excellent.”


    <span id="d-fallhaven_pot_antifoodp7"></span>**`fallhaven_pot_antifoodp7`** Potion merchant: “Well, animal hair can probably be found on any beast here outside of Fallhaven. I heard some hunters found a pack of wolves a bit south of here.”

    - Next → [fallhaven_pot_antifoodp8](#d-fallhaven_pot_antifoodp8)

    <span id="d-fallhaven_pot_antifp_q1"></span>**`fallhaven_pot_antifp_q1`** Potion merchant: “Good. Give me a minute to prepare that antidote for you.” — **effects:** sets stage 30 of [Taste is everything](../quests/antifoodp.md#stage-30)

    - Next → [fallhaven_pot_antifp_q2](#d-fallhaven_pot_antifp_q2)

    <span id="d-fallhaven_pot_antifp_q3"></span>**`fallhaven_pot_antifp_q3`** Potion merchant: “There. One potion against food-poisoning for you.” — **effects:** sets stage 35 of [Taste is everything](../quests/antifoodp.md#stage-35), gives [Antidote](../items/antifoodp.md)

    - Next → [fallhaven_pot_antifp_q4](#d-fallhaven_pot_antifp_q4)

    <span id="d-fallhaven_pot_antifp_q3x5"></span>**`fallhaven_pot_antifp_q3x5`** Potion merchant: “There. Five potions against food-poisoning for you.” — **effects:** gives [Antidote](../items/antifoodp.md)

    - Next → [fallhaven_pot_antifp_q4](#d-fallhaven_pot_antifp_q4)

    <span id="d-fallhaven_pot_antifp_q3x10"></span>**`fallhaven_pot_antifp_q3x10`** Potion merchant: “There. Ten potions against food-poisoning for you.” — **effects:** gives [Antidote](../items/antifoodp.md)

    - Next → [fallhaven_pot_antifp_q4](#d-fallhaven_pot_antifp_q4)

    <span id="d-fallhaven_pot_antifoodp3"></span>**`fallhaven_pot_antifoodp3`** Potion merchant: “I am all out of the ingredients required for it. Maybe you could help me gather some of them?”

    - “No way, I'm not running your errands.” → [fallhaven_pot_antifoodp4](#d-fallhaven_pot_antifoodp4)
    - “What ingredients are needed?” → [fallhaven_pot_antifoodp5](#d-fallhaven_pot_antifoodp5)

    <span id="d-fallhaven_potions3"></span>**`fallhaven_potions3`** Potion merchant: “Here, have some. I don't have that much, so don't lose it!” — **effects:** sets stage 20 of [Lodar's potions](../quests/lodar_pots.md#stage-20), gives [Spotted Hornbeam fungus](../items/hornbeam.md)

    - “Thank you.” → *conversation ends*

    <span id="d-fungi_panic_potioner_40"></span>**`fungi_panic_potioner_40`** Potion merchant: “So you need a cure against giant mushrooms?”

    - “Yes.” → [fungi_panic_potioner_42](#d-fungi_panic_potioner_42)
    - “Yes. Here are some samples of the mushroom spores.” *(if reached stage 40 of [Fungi panic](../quests/fungi_panic.md#stage-40); carry 4× [Spores of the giant mushroom](../items/fungi_panic_spores.md))* → [fungi_panic_potioner_50](#d-fungi_panic_potioner_50)

    <span id="d-fungi_panic_potioner_22"></span>**`fungi_panic_potioner_22`** Potion merchant: “Several times, indeed. Let me think...”

    - Next → [fungi_panic_potioner_24](#d-fungi_panic_potioner_24)

    <span id="d-fungi_panic_potioner_54"></span>**`fungi_panic_potioner_54`** Potion merchant: “Take it or leave it. Poor Bogsten ...”

    - “Forget it.” → [fungi_panic_potioner_56](#d-fungi_panic_potioner_56)
    - “OK, here you are.” *(if pay 150 gold; hand over 4× [Spores of the giant mushroom](../items/fungi_panic_spores.md))* → [fungi_panic_potioner_60](#d-fungi_panic_potioner_60)

    <span id="d-fungi_panic_potioner_60"></span>**`fungi_panic_potioner_60`** Potion merchant: “And here's the cure.” — **effects:** gives 1× [Curative potion against mushroom wounding](../items/fungi_panic_cure.md), sets stage 50 of [Fungi panic](../quests/fungi_panic.md#stage-50)

    - “Thank you.” → *conversation ends*

    <span id="d-fungi_panic_potioner_111"></span>**`fungi_panic_potioner_111`** Potion merchant: “Well, what did you expect? I make potions, not mushroom stew. If that's what you're after, go look for that Gison fellow south of town.”

    - Next → [fungi_panic_potioner_112](#d-fungi_panic_potioner_112)

    <span id="d-fallhaven_pot_antifoodp8"></span>**`fallhaven_pot_antifoodp8`** Potion merchant: “Poison glands however, can be a bit trickier to find. I don't know really, but any poisonous creature might do. Maybe some snakes around here are poisonous?”

    - “I'll be right back with those ingredients.” → [fallhaven_pot_antifoodp6](#d-fallhaven_pot_antifoodp6)
    - “Phew, that sounds like a lot of work. I don't know if I'll do it.” → [fallhaven_pot_antifoodp4](#d-fallhaven_pot_antifoodp4)

    <span id="d-fallhaven_pot_antifoodp4"></span>**`fallhaven_pot_antifoodp4`** Potion merchant: “Fair enough. Welcome back if you change your mind.”


    <span id="d-fungi_panic_potioner_42"></span>**`fungi_panic_potioner_42`** Potion merchant: “There are lots of different mushrooms. A spore infection can be nasty, deadly even. Unfortunately the cure for one kind kills you, when you are afflicted by another kind.”

    - “Oh dear. So Bogsten can't be helped?” → [fungi_panic_potioner_44](#d-fungi_panic_potioner_44)

    <span id="d-fungi_panic_potioner_24"></span>**`fungi_panic_potioner_24`** Potion merchant: “He was my first customer. Needed an antidote against snake poison. His pet snake bit him.”

    - “Pet snake?!” → [fungi_panic_potioner_26](#d-fungi_panic_potioner_26)
    - “I heard enough. Just give me the cure, please.” → [fungi_panic_potioner_40](#d-fungi_panic_potioner_40)

    <span id="d-fungi_panic_potioner_56"></span>**`fungi_panic_potioner_56`** Potion merchant: “I had always liked him ...”

    - “No.” → [fungi_panic_potioner_58](#d-fungi_panic_potioner_58)
    - “OK, here you are.” *(if pay 150 gold; hand over 4× [Spores of the giant mushroom](../items/fungi_panic_spores.md))* → [fungi_panic_potioner_60](#d-fungi_panic_potioner_60)

    <span id="d-fungi_panic_potioner_112"></span>**`fungi_panic_potioner_112`** Potion merchant: “Now leave my shop, unless you have some other business. I have work to do.”

    - “Forget it, let's talk about something else.” → [fallhaven_potions](#d-fallhaven_potions)
    - “You can't do that to me! I'll get the guards!” → [fungi_panic_potioner_120](#d-fungi_panic_potioner_120)

    <span id="d-fungi_panic_potioner_44"></span>**`fungi_panic_potioner_44`** Potion merchant: “No need to despair. To make a cure, I will need a sample of these spores. Can you get some?”

    - “I could try.” → [fungi_panic_potioner_46](#d-fungi_panic_potioner_46)

    <span id="d-fungi_panic_potioner_26"></span>**`fungi_panic_potioner_26`** Potion merchant: “Next time he ate something interesting. I always had told him not to try all these red and white mushrooms.”

    - Next → [fungi_panic_potioner_28](#d-fungi_panic_potioner_28)

    <span id="d-fungi_panic_potioner_58"></span>**`fungi_panic_potioner_58`** Potion merchant: “Sigh.”

    - “I said no.” → *conversation ends*
    - “OK, here you are.” *(if pay 150 gold; hand over 4× [Spores of the giant mushroom](../items/fungi_panic_spores.md))* → [fungi_panic_potioner_60](#d-fungi_panic_potioner_60)

    <span id="d-fungi_panic_potioner_120"></span>**`fungi_panic_potioner_120`** Potion merchant: “Calm down. Shall I sell a sedative to you?”

    - “NO! I DON'T NEED ANY SEDATIVE!!” → *conversation ends*

    <span id="d-fungi_panic_potioner_46"></span>**`fungi_panic_potioner_46`** Potion merchant: “Good. Bring me four sample spores of the mushroom, then I will be able to choose the right antidote.” — **effects:** sets stage 20 of [Fungi panic](../quests/fungi_panic.md#stage-20)

    - “I will be back with the spores in an instant.” → *conversation ends*
    - “Here are four samples of the mushroom spores.” *(if reached stage 40 of [Fungi panic](../quests/fungi_panic.md#stage-40); carry 4× [Spores of the giant mushroom](../items/fungi_panic_spores.md))* → [fungi_panic_potioner_50](#d-fungi_panic_potioner_50)

    <span id="d-fungi_panic_potioner_28"></span>**`fungi_panic_potioner_28`** Potion merchant: “Then he wanted some drink for an annoying 'friend' who always came and disturbed him.”

    - “Nice.” → [fungi_panic_potioner_30](#d-fungi_panic_potioner_30)
    - “Enough. Just give me the cure, please.” → [fungi_panic_potioner_40](#d-fungi_panic_potioner_40)

    <span id="d-fungi_panic_potioner_30"></span>**`fungi_panic_potioner_30`** Potion merchant: “He came regularly for the snake antidote. Trying to tame snakes wasn't successful obviously...”

    - “I can imagine.” → [fungi_panic_potioner_32](#d-fungi_panic_potioner_32)

    <span id="d-fungi_panic_potioner_32"></span>**`fungi_panic_potioner_32`** Potion merchant: “He even tried to get my recipe for this antidote. But of course I couldn't reveal it to him.”

    - “Yes, such things should be done by learned potion makers.” → [fungi_panic_potioner_34](#d-fungi_panic_potioner_34)

    <span id="d-fungi_panic_potioner_34"></span>**`fungi_panic_potioner_34`** Potion merchant: “Nonsense. He was my best customer. I want to keep it like this.”

    - “Oh. Sure.” → [fungi_panic_potioner_40](#d-fungi_panic_potioner_40)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 5 lines changed<br>· text: “[mixes the ingredients]” → “[Mixes the ingredients]” |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 1 line changed |
| [v0.7.11](../versions/0.7.11.md) | Dialogue: 3 lines added, 1 line changed |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 26 lines added, 1 line changed |
| [v0.8.4](../versions/0.8.4.md) | Dialogue: 1 line changed<br>· text: “So you need a cure against giant mushrooms.” → “So you need a cure against giant mushrooms?” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=potion_merchant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=potion_merchant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=potion_merchant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=potion_merchant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `potion_merchant` |
    | Spawn group | `fallhaven_potions` |
    | Loot table | `shop_fallhaven_potions` |
    | Conversation | `fallhaven_potions` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_mage2:0` |
    | Defined in | `res/raw/monsterlist_fallhaven_npcs.json` |

    Raw data:

    ```json
    {
     "id": "potion_merchant",
     "name": "Potion merchant",
     "iconID": "monsters_mage2:0",
     "monsterClass": "humanoid",
     "spawnGroup": "fallhaven_potions",
     "phraseID": "fallhaven_potions",
     "droplistID": "shop_fallhaven_potions"
    }
    ```


<small>Data from v0.8.18</small>
