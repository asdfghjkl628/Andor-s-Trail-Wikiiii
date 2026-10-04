# Fungi panic

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `fungi_panic` |
| **In journal** | Yes |
| **Stages** | 30 (completes at 200) |
| **Started by** | [Bogsten](../monsters/bogsten.md) ([bogsten1](../maps/bogsten1.md)) |
| **NPCs involved** | [Black fog](../monsters/zuul_khan1_blocker.md), [Black fog](../monsters/zuul_khan9_blocker.md), [Black fog](../monsters/zuul_khan2_blocker.md), [Black fog](../monsters/zuul_khan4_blocker.md), [Black fog](../monsters/zuul_khan3_blocker.md), [Bogsten](../monsters/bogsten.md) +4 |
| **Locations** | [bogsten1](../maps/bogsten1.md), [bogsten4](../maps/bogsten4.md), [fallhaven_potions](../maps/fallhaven_potions.md), [mushroom_m2_3](../maps/mushroom_m2_3.md) |
| **Total XP** | 7,500 |

</div>

## Overview

> I met old man Bogsten in his cabin. He was sick after encountering a giant mushroom and wanted me to go see the potion merchant in Fallhaven to get a cure.

## Prerequisites to start

None: talk to [Bogsten](../monsters/bogsten.md) ([bogsten1](../maps/bogsten1.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

No links to other quests were found in the dialogue conditions.

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I met old man Bogsten in his cabin. He was sick after encountering a giant mushroom and wanted me to go see the potion merchant in Fallhaven to get a cure. | [Bogsten](../monsters/bogsten.md) ([bogsten1](../maps/bogsten1.md)) | – | – |
| <span id="stage-20"></span>20 | The potion merchant needed four spore samples to prepare the cure. I should go back to see Bogsten. | [Potion merchant](../monsters/potion_merchant.md) ([fallhaven_potions](../maps/fallhaven_potions.md)) | stage 10 | – |
| <span id="stage-30"></span>30 | Bogsten gave me the key to his backyard. I should go to the mushroom cave from there and collect the spore samples. | [Bogsten](../monsters/bogsten.md) ([bogsten1](../maps/bogsten1.md)) | stage 10, stage 20 | gives 1× [Bogsten's key](../items/bogsten_key.md) |
| <span id="stage-35"></span>35 | I opened Bogsten's backyard door. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-40"></span>40 | I showed Bogsten the spores. Now I should go back to see the potion merchant. | [Bogsten](../monsters/bogsten.md) ([bogsten1](../maps/bogsten1.md)) | carry 1× [Spores of the giant mushroom](../items/fungi_panic_spores.md), stage 30 | – |
| <span id="stage-50"></span>50 | The potion merchant gave me the cure. I should give it to Bogsten now. | [Potion merchant](../monsters/potion_merchant.md) ([fallhaven_potions](../maps/fallhaven_potions.md)) | carry 4× [Spores of the giant mushroom](../items/fungi_panic_spores.md), hand over 4× [Spores of the giant mushroom](../items/fungi_panic_spores.md), pay 150 gold | gives 1× [Curative potion against mushroom wounding](../items/fungi_panic_cure.md) |
| <span id="stage-52"></span>52 | Bogsten was cured. | [Bogsten](../monsters/bogsten.md) ([bogsten1](../maps/bogsten1.md)) | hand over 1× [Curative potion against mushroom wounding](../items/fungi_panic_cure.md), stage 50 | – |
| <span id="stage-60"></span>60 | Bogsten said evil forces in his cave were preventing him from working. He asked me to check his cave and gave me his necklace. | [Bogsten](../monsters/bogsten.md) ([bogsten1](../maps/bogsten1.md)) | – | gives 1× [Bogsten's necklace](../items/bogsten_necklace.md) |
| <span id="stage-70"></span>70 | I met an old sorcerer named Zuul'khan in the cave. He told me Bogsten's family imprisoned him using an ancient petrifying spell, but thanks to Bogsten's laxity, he was now free. | [Zuul'khan](../monsters/zuul_khan.md) ([bogsten4](../maps/bogsten4.md)) | – | – |
| <span id="stage-72"></span>72 | He wanted me to kill Bogsten and bring him Bogsten's staff. | [Zuul'khan](../monsters/zuul_khan.md) ([bogsten4](../maps/bogsten4.md)) | stage 70 | – |
| <span id="stage-80"></span>80 | I decided to slay Zuul'khan. | [Zuul'khan](../monsters/zuul_khan.md) ([bogsten4](../maps/bogsten4.md)) | stage 70 | – |
| <span id="stage-90"></span>90 | I defeated Zuul'khan, but he was not dead. He disappeared into the ground.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Bogsten4](../maps/bogsten4.md).</span> | stepping on a trigger on [bogsten4](../maps/bogsten4.md) | – | – |
| <span id="stage-92"></span>92 | I told Bogsten about what happened. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-100"></span>100 | Bogsten remembered the petrifying spell. This time he would make sure that Zuul'khan cannot come back. He gave me a bag of mushrooms and told me I should take them to the potion merchant. | [Bogsten](../monsters/bogsten.md) ([bogsten1](../maps/bogsten1.md)) | stage 70 | 2,000 XP<br>gives 1× [Bag with mushrooms](../items/fungi_panic_bag.md) |
| <span id="stage-102"></span>102 | Zuul'khan seems to have moved away from Bogsten's caves to another hiding place. | [Bogsten](../monsters/bogsten.md) ([bogsten1](../maps/bogsten1.md)) | stage 70 | – |
| <span id="stage-110"></span>110 | The potion merchant said that these were very rare mushrooms. He prepared two "Underground Fighter" potions for me. He would sell me some more if I came back. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-115"></span>115 | Zuul'khan's offer seemed interesting. I have to go kill Bogsten. | [Zuul'khan](../monsters/zuul_khan.md) ([bogsten4](../maps/bogsten4.md)) | stage 70 | – |
| <span id="stage-135"></span>135 | I decided to keep Bogsten's staff for myself, so I had to kill Zuul'khan. | [Zuul'khan](../monsters/zuul_khan.md) ([bogsten4](../maps/bogsten4.md)) | carry 1× [Bogsten's staff](../items/bogsten_staff.md) | – |
| <span id="stage-145"></span>145 | I defeated Zuul'khan, but he was not dead. He disappeared into the ground. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | 2,000 XP |
| <span id="stage-150"></span>150 | I gave Bogsten's staff to Zuul'khan. | [Zuul'khan](../monsters/zuul_khan.md) ([bogsten4](../maps/bogsten4.md)) | carry 1× [Bogsten's staff](../items/bogsten_staff.md), hand over 1× [Bogsten's staff](../items/bogsten_staff.md) | – |
| <span id="stage-155"></span>155 | He rewarded me with permanent immunity to Spore Infection. | [Zuul'khan](../monsters/zuul_khan.md) ([bogsten4](../maps/bogsten4.md)) | stage 150 | 2,000 XP<br>applies condition spore_poison<br>+1 [Spore poison immunity](../skills/sporeImmunity.md) |
| <span id="stage-161"></span>161 | I got through the black fog. | [Black fog](../monsters/zuul_khan1_blocker.md) ([bogsten4](../maps/bogsten4.md)) | – | removes monsters from bogsten4 |
| <span id="stage-162"></span>162 | I got through the black fog again after a fight with Zuul'khan. | [Black fog](../monsters/zuul_khan2_blocker.md) ([mushroom_m2_3](../maps/mushroom_m2_3.md)) | – | removes monsters from mushroom_m2_3 |
| <span id="stage-163"></span>163 | And a third time. | [Black fog](../monsters/zuul_khan3_blocker.md) ([mushroom_m2_6](../maps/mushroom_m2_6.md)) | – | removes monsters from mushroom_m2_6 |
| <span id="stage-164"></span>164 | After another fight with Zuul'khan I got through the black fog again. | [Black fog](../monsters/zuul_khan4_blocker.md) ([mushroom_m2_8](../maps/mushroom_m2_8.md)) | – | removes monsters from mushroom_m2_8 |
| <span id="stage-169"></span>169 | I overpowered Zuul'khan one more time, but this time the black fog wouldn't go away. Obviously I can't get past the fog that way. | [Black fog](../monsters/zuul_khan9_blocker.md) ([mushroom_m3_1](../maps/mushroom_m3_1.md)) | – | – |
| <span id="stage-170"></span>170 | I defeated Zuul'khan one last time and the black fog was gone for good. I must find and destroy the fungi leader. | [Black fog](../monsters/zuul_khan9_blocker.md) ([mushroom_m3_1](../maps/mushroom_m3_1.md)) | – | removes monsters from mywildcave4<br>removes monsters from mushroom_m3_1 |
| <span id="stage-200"></span>200 | I defeated the giant mushroom, Zuul'khan's fungi leader. **(completes quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mushroom m3 2](../maps/mushroom_m3_2.md).</span> | stepping on a trigger on [mushroom_m3_2](../maps/mushroom_m3_2.md) | – | 500 XP<br>spawns monsters on mushroom_m3_2 |
| <span id="stage-210"></span>210 | A young girl named Lediofa emerged after my battle with the mushroom. She told me how Zuul'khan captured her as food for the mushroom. She seemed to have been poisoned just like Bogsten, so I directed her to see the Fallhaven potioner. | [Lediofa](../monsters/fungi_rescued.md) ([mushroom_m3_2](../maps/mushroom_m3_2.md)) | – | spawns monsters on fallhaven_potions |
| <span id="stage-220"></span>220 | I met Lediofa at the potions shop in Fallhaven. She couldn't afford to pay the potioner for a mushroom poison cure, so I gave her the gold she needed. In return, she offered her family's hospitality if I ever come to visit in Nor City. | [Lediofa](../monsters/fungi_rescued2.md) ([fallhaven_potions](../maps/fallhaven_potions.md)) | – | 1,000 XP |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Bogsten](../monsters/bogsten.md) ([bogsten1](../maps/bogsten1.md)) → choose “Sure. I'll go there right now.” → **stage 10**. NPC: “Thank you! I'll be waiting for you. Be quick!”

???+ note "Stage 20: 1 route"

    1. Talk to [Potion merchant](../monsters/potion_merchant.md) ([fallhaven_potions](../maps/fallhaven_potions.md)) → choose “I could try.” — **conditions:** reached stage 10 of [Fungi panic](../quests/fungi_panic.md#stage-10); NOT reached stage 20 of [Fungi panic](../quests/fungi_panic.md#stage-20) → **stage 20**. NPC: “Good. Bring me four sample spores of the mushroom, then I will be able to choose the right antidote.”

???+ note "Stage 30: 1 route"

    1. Talk to [Bogsten](../monsters/bogsten.md) ([bogsten1](../maps/bogsten1.md)) → choose “Not yet. The potion merchant needs some spore sample to prepare it.” — **conditions:** reached stage 10 of [Fungi panic](../quests/fungi_panic.md#stage-10); reached stage 20 of [Fungi panic](../quests/fungi_panic.md#stage-20) → **stage 30**; also gives 1× [Bogsten's key](../items/bogsten_key.md). NPC: “I'm sorry to have dragged you into this, kid. Take this key. It will open the way to my mushroom cave. You will…”

???+ note "Stage 40: 1 route"

    1. Talk to [Bogsten](../monsters/bogsten.md) ([bogsten1](../maps/bogsten1.md)) → choose “Yes. I have them with me.” — **conditions:** reached stage 30 of [Fungi panic](../quests/fungi_panic.md#stage-30); carry 1× [Spores of the giant mushroom](../items/fungi_panic_spores.md) → **stage 40**. NPC: “These spores would do. Please go and give them to Fallhaven's potion merchant.”

???+ note "Stage 50: 1 route"

    1. Talk to [Potion merchant](../monsters/potion_merchant.md) ([fallhaven_potions](../maps/fallhaven_potions.md)) → choose “OK, here you are.” — **conditions:** carry 4× [Spores of the giant mushroom](../items/fungi_panic_spores.md); NOT reached stage 60 of [Fungi panic](../quests/fungi_panic.md#stage-60); pay 150 gold; hand over 4× [Spores of the giant mushroom](../items/fungi_panic_spores.md) → **stage 50**; also gives 1× [Curative potion against mushroom wounding](../items/fungi_panic_cure.md). NPC: “And here's the cure.”

???+ note "Stage 52: 1 route"

    1. Talk to [Bogsten](../monsters/bogsten.md) ([bogsten1](../maps/bogsten1.md)) → choose “Yes, I have got a potion for you.” — **conditions:** reached stage 50 of [Fungi panic](../quests/fungi_panic.md#stage-50); hand over 1× [Curative potion against mushroom wounding](../items/fungi_panic_cure.md) → **stage 52**. NPC: “Finally! [He pours down the liquid greedily]”

???+ note "Stage 60: 1 route"

    1. Talk to [Bogsten](../monsters/bogsten.md) ([bogsten1](../maps/bogsten1.md)) → choose “OK. Down again.” — **conditions:** reached stage 60 of [Fungi panic](../quests/fungi_panic.md#stage-60) → **stage 60**; also gives 1× [Bogsten's necklace](../items/bogsten_necklace.md). NPC: “There are hidden rooms. I'll give you my necklace so that you can find them. Wear it down in the caves. Never take it…”

???+ note "Stage 70: 1 route"

    1. Talk to [Zuul'khan](../monsters/zuul_khan.md) ([bogsten4](../maps/bogsten4.md)) → choose “He had children?” — **conditions:** reached stage 70 of [Fungi panic](../quests/fungi_panic.md#stage-70) → **stage 70**. NPC: “AHAHAHAHA!”

???+ note "Stage 72: 1 route"

    1. Talk to [Zuul'khan](../monsters/zuul_khan.md) ([bogsten4](../maps/bogsten4.md)) → choose “Hm, wait. Let me think again.” — **conditions:** reached stage 70 of [Fungi panic](../quests/fungi_panic.md#stage-70) → **stage 72**. NPC: “Kill Bogsten and bring me his staff as evidence.”

???+ note "Stage 80: 1 route"

    1. Talk to [Zuul'khan](../monsters/zuul_khan.md) ([bogsten4](../maps/bogsten4.md)) → choose “Attack!” — **conditions:** reached stage 70 of [Fungi panic](../quests/fungi_panic.md#stage-70) → **stage 80**

???+ note "Stage 90: 2 routes"

    1. stepping on a trigger on [bogsten4](../maps/bogsten4.md) → the conversation leads here automatically — **conditions:** killed 1× [Zuul'khan](../monsters/zuul_khan.md); killed 1× [Bogsten](../monsters/bogsten.md); NOT reached stage 90 of [Fungi panic](../quests/fungi_panic.md#stage-90) → **stage 90**. NPC: “You have the impression that Zuul'khan is not dead. He just disappeared into the ground.”
    2. stepping on a trigger on [bogsten4](../maps/bogsten4.md) → the conversation leads here automatically — **conditions:** killed 1× [Zuul'khan](../monsters/zuul_khan.md); NOT reached stage 90 of [Fungi panic](../quests/fungi_panic.md#stage-90) → **stage 90**. NPC: “You have the impression that Zuul'khan is not dead. He just disappeared into the ground. You should tell Bogsten about…”

???+ note "Stage 100: 1 route"

    1. Talk to [Bogsten](../monsters/bogsten.md) ([bogsten1](../maps/bogsten1.md)) → choose “I don't think so. He just disappeared into the ground.” — **conditions:** reached stage 70 of [Fungi panic](../quests/fungi_panic.md#stage-70); killed 1× [Zuul'khan](../monsters/zuul_khan.md) → **stage 100**; also gives 1× [Bag with mushrooms](../items/fungi_panic_bag.md). NPC: “Disappeared! I hope he doesn't appear here next. Well, as a reward for your efforts, please take this bag of mushrooms…”

???+ note "Stage 102: 1 route"

    1. Talk to [Bogsten](../monsters/bogsten.md) ([bogsten1](../maps/bogsten1.md)) → choose “What??” — **conditions:** reached stage 70 of [Fungi panic](../quests/fungi_panic.md#stage-70); killed 1× [Zuul'khan](../monsters/zuul_khan.md) → **stage 102**. NPC: “It has moved probably to another place. But that is someone else's problem.”

???+ note "Stage 115: 1 route"

    1. Talk to [Zuul'khan](../monsters/zuul_khan.md) ([bogsten4](../maps/bogsten4.md)) → choose “Agreed. I'll go upstairs and finish Bogsten.” — **conditions:** reached stage 70 of [Fungi panic](../quests/fungi_panic.md#stage-70) → **stage 115**. NPC: “Do so.”

???+ note "Stage 135: 1 route"

    1. Talk to [Zuul'khan](../monsters/zuul_khan.md) ([bogsten4](../maps/bogsten4.md)) → choose “Little in height - but strong! Attack!” — **conditions:** carry 1× [Bogsten's staff](../items/bogsten_staff.md) → **stage 135**

???+ note "Stage 150: 1 route"

    1. Talk to [Zuul'khan](../monsters/zuul_khan.md) ([bogsten4](../maps/bogsten4.md)) → choose “Here it is.” — **conditions:** carry 1× [Bogsten's staff](../items/bogsten_staff.md); hand over 1× [Bogsten's staff](../items/bogsten_staff.md) → **stage 150**. NPC: “Finally I got the staff back!”

???+ note "Stage 155: 1 route"

    1. Talk to [Zuul'khan](../monsters/zuul_khan.md) ([bogsten4](../maps/bogsten4.md)) → choose “I'm feeling dizzy...” — **conditions:** reached stage 150 of [Fungi panic](../quests/fungi_panic.md#stage-150) → **stage 155**; also applies condition spore_poison, +1 [Spore poison immunity](../skills/sporeImmunity.md). NPC: “Done. You will never fear any of these fungi spores anymore.”

???+ note "Stage 161: 1 route"

    1. Talk to [Black fog](../monsters/zuul_khan1_blocker.md) ([bogsten4](../maps/bogsten4.md)) → choose “Your foul master is gone.” — **conditions:** killed 1× [Zuul'khan](../monsters/zuul_khan.md) → **stage 161**; also removes monsters from bogsten4, removes monsters from bogsten4. NPC: “The black fog hisses and instantly vanishes.”

???+ note "Stage 162: 1 route"

    1. Talk to [Black fog](../monsters/zuul_khan2_blocker.md) ([mushroom_m2_3](../maps/mushroom_m2_3.md)) → choose “Your foul master is gone again...” — **conditions:** killed 1× [Zuul'khan](../monsters/zuul_khan2.md) → **stage 162**; also removes monsters from mushroom_m2_3. NPC: “The black fog hisses and instantly vanishes.”

???+ note "Stage 163: 1 route"

    1. Talk to [Black fog](../monsters/zuul_khan3_blocker.md) ([mushroom_m2_6](../maps/mushroom_m2_6.md)) → choose “Your foul master is once more gone...” — **conditions:** killed 1× [Zuul'khan](../monsters/zuul_khan3.md) → **stage 163**; also removes monsters from mushroom_m2_6. NPC: “The black fog hisses and instantly vanishes.”

???+ note "Stage 164: 1 route"

    1. Talk to [Black fog](../monsters/zuul_khan4_blocker.md) ([mushroom_m2_8](../maps/mushroom_m2_8.md)) → choose “Oh my. How often?” — **conditions:** killed 1× [Zuul'khan](../monsters/zuul_khan4.md) → **stage 164**; also removes monsters from mushroom_m2_8. NPC: “The black fog hisses and instantly vanishes.”

???+ note "Stage 169: 1 route"

    1. Talk to [Black fog](../monsters/zuul_khan9_blocker.md) ([mushroom_m3_1](../maps/mushroom_m3_1.md)) → choose “Your master is dead. Begone!” — **conditions:** killed 1× [Zuul'khan](../monsters/zuul_khan9.md); NOT killed 1× [Zuul'khan](../monsters/gison_thiefboss.md) → **stage 169**. NPC: “No. We were expecting you to say so. We were told not to leave.”

???+ note "Stage 170: 1 route"

    1. Talk to [Black fog](../monsters/zuul_khan9_blocker.md) ([mushroom_m3_1](../maps/mushroom_m3_1.md)) → choose “Your master is dead forever now. Begone!” — **conditions:** killed 1× [Zuul'khan](../monsters/gison_thiefboss.md) → **stage 170**; also removes monsters from mywildcave4, removes monsters from mushroom_m3_1. NPC: “The black fog hisses and instantly vanishes.”

???+ note "Stage 200: 1 route"

    1. stepping on a trigger on [mushroom_m3_2](../maps/mushroom_m3_2.md) → the conversation leads here automatically — **conditions:** killed 3× [Angry dangerous fungi](../monsters/dangerous_fungi_1.md); killed 4× [Angry fungi](../monsters/mid_fungi_1.md); killed 5× [Angry weak fungi](../monsters/weak_fungi_1.md); NOT reached stage 200 of [Fungi panic](../quests/fungi_panic.md#stage-200) → **stage 200**; also spawns monsters on mushroom_m3_2. NPC: “The giant mushroom is finally destroyed.”

???+ note "Stage 210: 1 route"

    1. Talk to [Lediofa](../monsters/fungi_rescued.md) ([mushroom_m3_2](../maps/mushroom_m3_2.md)) → choose “That might be the giant mushroom's poison. The potioner in Fallhaven knows the cure.” → **stage 210**; also spawns monsters on fallhaven_potions. NPC: “[Lediofa's eyes widen.] I've been poisoned...? Oh no! I'll seek the potioner right away. Thank you for telling me. I…”

???+ note "Stage 220: 1 route"

    1. Talk to [Lediofa](../monsters/fungi_rescued2.md) ([fallhaven_potions](../maps/fallhaven_potions.md)) → the conversation leads here automatically — **conditions:** reached stage 220 of [Fungi panic](../quests/fungi_panic.md#stage-220) → **stage 220**. NPC: “You've saved me again, $playername. You truly are a hero. If you ever find yourself in Nor City, I'm sure my family…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 27 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fungi_panic.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fungi_panic.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fungi_panic.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fungi_panic.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fungi_panic.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `fungi_panic` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 35, 40, 50, 52, 60, 70, 72, 80, 90, 92, 100, 102, 110, 115, 135, 145, 150, 155, 161, 162, 163, 164, 169, 170, 200, 210, 220 |
    | Dialogue nodes setting stages | 10: `bogsten_start_8`, 20: `fungi_panic_potioner_46`, 30: `bogsten_20_10`, 40: `bogsten_30_20`, 50: `fungi_panic_potioner_60`, 52: `bogsten_50_20`, 60: `bogsten_60_54`, 70: `zuul_khan_60_140`, 72: `zuul_khan_70_22`, 80: `zuul_khan_70_30`, 90: `bogsten_check_zuulkhan_10`, 90: `bogsten_check_zuulkhan_20`, 100: `bogsten_90_30`, 102: `bogsten_90_50`, 115: `zuul_khan_70_50`, 135: `zuul_khan_115_24`, 150: `zuul_khan_115_50`, 155: `zuul_khan_150_10`, 161: `zuul_khan1_blocker_10`, 162: `zuul_khan2_blocker_10`, 163: `zuul_khan3_blocker_10`, 164: `zuul_khan4_blocker_10`, 169: `zuul_khan9_blocker_20`, 170: `zuul_khan9_blocker_10`, 200: `boss_fungi_killed_22`, 210: `fungi_rescued_110`, 220: `fungi_rescued2_30` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
