---
description: "Feygard scout is an NPC you can also fight in Andor's Trail, found in Crossroads Guardhouse, Prim. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_omi1_0.png){ .sprite } Feygard scout

**Where to find Feygard scout:** [Crossroads Guardhouse, Crossroads](#v-feygard_scout), [Prim, Blackwater mountain 29](#v-ortholion_guard2), [Prim, Blackwater mountain 10](#v-ortholion_guard6)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_omi1_0.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Role** | Shopkeeper |
| **Found in** | Crossroads Guardhouse, Prim |
| **Class** | Humanoid |
| **HP** | 83 |
| **XP when defeated** | 209 |
| **Introduced** | [v0.7.8](../versions/0.7.8.md) |

</div>

## Crossroads Guardhouse, Crossroads { #v-feygard_scout }

**Where:** Crossroads Guardhouse: [Crossroads](../maps/crossroads.md#pin-npc-feygard_scout)

!!! warning "You can fight Feygard scout"
    Any of your answers (“Not without a fight!”, “How dare you! Prepare to die, useless soldier!” or “For the shadow!”) while talking to [Fanamor](../monsters/fanamor.md) during [Thief apprentice](../quests/Thieves01.md#stage-40) starts a fight with Feygard scout.

    Any of your answers (“Not without a fight!”, “How dare you! Prepare to die, useless soldier!” or “For the shadow!”) during [Thief apprentice](../quests/Thieves01.md#stage-40) starts a fight with Feygard scout.

### Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 83 |
| XP when defeated | 209 |
| Damage | 6 to 11 |
| AC | 110 |
| BC | 95 |
| DR | 5 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | 17% (×2.5) |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Fanamor's Journal](../items/Fanamor_journal.md) | 100% | 1 |
| [Feygard iron dagger](../items/feygard_iron_dagger.md) | 100% | 1 |
| [Polished gem](../items/gem3.md) | 100% | 1 to 3 |

### Quests that count defeats

- A conversation with [Fanamor](../monsters/fanamor.md) ([Crossroads](../maps/crossroads.md)) checks that this enemy has been defeated.

### Quests

- [Thief apprentice](../quests/Thieves01.md): stage 40

### Dialogue simulator

Talk to Feygard scout as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/feygard_scout_3.json" data-npc="Feygard scout" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-feygard_scout-feygard_scout_3"></span>**`feygard_scout_3`** [Feygard scout](../monsters/feygard_scout.md): “(Grabs the book) What have we here? A lost kid trying to do business with this scum, hah? You are under arrest!” — **effects:** sets stage 40 of [Thief apprentice](../quests/Thieves01.md#stage-40)

    - “Not without a fight!” → *fight starts*
    - “How dare you! Prepare to die, useless soldier!” → *fight starts*
    - “For the shadow!” → *fight starts*



### Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Prim, Blackwater mountain 29 { #v-ortholion_guard2 }

**Where:** Prim: [Blackwater mountain 29](../maps/blackwater_mountain29.md#pin-npc-ortholion_guard2)

### Dialogue simulator

Talk to Feygard scout as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/ortholion_guard6_1.json" data-npc="Feygard scout" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (5 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-ortholion_guard2-ortholion_guard6_1"></span>**`ortholion_guard6_1`** Feygard scout: “*Looks nervous* Kid! Go back now, it's really dangerous past here.”

    - “Come with me, we'll cover each other's backs.” → [ortholion_guard6_2](#d-ortholion_guard2-ortholion_guard6_2)
    - “Can you clear the way for me then?” → [ortholion_guard6_2](#d-ortholion_guard2-ortholion_guard6_2)
    - “Where's the general?” → [ortholion_guard6_5](#d-ortholion_guard2-ortholion_guard6_5)

    <span id="d-ortholion_guard2-ortholion_guard6_2"></span>**`ortholion_guard6_2`** Feygard scout: “No way! I have a home to go back to you know? And you probably do too.”

    - “Step aside then, you're in my way.” → *conversation ends*
    - “What are you scared of?” → [ortholion_guard6_3](#d-ortholion_guard2-ortholion_guard6_3)

    <span id="d-ortholion_guard2-ortholion_guard6_5"></span>**`ortholion_guard6_5`** Feygard scout: “We...We haven't seen him. The other scout entered the tunnel... *looks back* Two men are guarding the rearback. Something's off with this place.”

    - “What's wrong with those passages?” → [ortholion_guard6_3](#d-ortholion_guard2-ortholion_guard6_3)
    - “I will look for him, bye.” → *conversation ends*

    <span id="d-ortholion_guard2-ortholion_guard6_3"></span>**`ortholion_guard6_3`** Feygard scout: “*stares at the tunnels* They're dark, stinky, and narrow. We were going to pass in line through them. But seconds after the other scout entered, a horrible scream came from inside there... It was him, I'm sure!”

    - Next → [ortholion_guard6_4](#d-ortholion_guard2-ortholion_guard6_4)

    <span id="d-ortholion_guard2-ortholion_guard6_4"></span>**`ortholion_guard6_4`** Feygard scout: “...I ran away. I am sure there's something dangerous inside there. Really dangerous! Dangerous enough to make a Feygard soldier scream that way.”

    - “I'll be careful. Thanks.” → *conversation ends*
    - “It was surely a cave rat. I will find out now.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Prim, Blackwater mountain 10 { #v-ortholion_guard6 }

**Where:** Prim: [Blackwater mountain 10](../maps/blackwater_mountain10.md#pin-npc-ortholion_guard6) · **Role:** Shopkeeper

### Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Minor potion of health](../items/health_minor2.md) | 100% | 1 to 10 |
| [Regular potion of health](../items/health.md) | 100% | 1 to 10 |
| [Animal hair](../items/hair.md) | 100% | 1 to 10 |
| [Rough ring of damage](../items/ring_rough_damage.md) | 100% | 0 to 3 |
| [Iqhan pendant](../items/iqhan_pendant.md) | 33.3333% | 0 to 2 |
| [Runed scepter](../items/scptr_runed.md) | 33.3333% | 0 to 2 |
| [Superior leather boots](../items/boots2.md) | 25% | 1 to 2 |
| [Black axe](../items/axe_black1.md) | 25% | 1 |
| [Redfoot beast hair](../items/redfthair.md) | 25% | 1 to 10 |
| [Bottle of mountain water](../items/bwm_water1.md) | 20% | 0 to 10 |
| [Large bottle of mountain water](../items/bwm_water2.md) | 20% | 1 to 10 |
| [Jinxed ring of damage resistance](../items/ring_jinxed1.md) | 20% | 1 to 3 |
| [Cold Lava Rock](../items/lava_rock_cold.md) | 10% | 1 to 10 |
| [Steel broadsword](../items/broadsword2.md) | 10% | 1 |
| [Blackwater brew](../items/bwm_brew.md) | 10% | 1 to 20 |
| [Sharp steel rapier](../items/rapier_steel.md) | 5% | 1 |
| [Venomfang dirk](../items/venomfang_dagger.md) | 100% | 1 |

### Dialogue simulator

Talk to Feygard scout as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/ortholion_guard_selector.json" data-npc="Feygard scout" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (33 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-ortholion_guard6-ortholion_guard_selector"></span>**`ortholion_guard_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if latest stage of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-46) is 46)* → [ortholion_guard_0e](#d-ortholion_guard6-ortholion_guard_0e)
    - branch 2 *(if random chance (1/4%))* → [ortholion_guard_0a](#d-ortholion_guard6-ortholion_guard_0a)
    - branch 3 *(if random chance (1/3%))* → [ortholion_guard_0b](#d-ortholion_guard6-ortholion_guard_0b)
    - branch 4 *(if random chance (1/2%))* → [ortholion_guard_0c](#d-ortholion_guard6-ortholion_guard_0c)
    - branch 5 → [ortholion_guard_0d](#d-ortholion_guard6-ortholion_guard_0d)

    <span id="d-ortholion_guard6-ortholion_guard_0e"></span>**`ortholion_guard_0e`** Feygard scout: “No, kid, I don't have anything to trade right now. I am tired of this place. Mountains are not my thing, you know?”

    - “I have a very important message fr...” → [ortholion_guard_1e](#d-ortholion_guard6-ortholion_guard_1e)

    <span id="d-ortholion_guard6-ortholion_guard_0a"></span>**`ortholion_guard_0a`** Feygard scout: “I'm on duty, youngster. Go play somewhere else.”

    - “Hah! Good one. Go buy a better sword, rookie.” *(if carry 1× [Flagstone's pride](../items/sword_flagstone.md))* → *conversation ends*
    - “Sorry, bye.” → *conversation ends*
    - “How does it feel that a kid killed more gornauds than you?” *(if killed 100× [Gornaud](../monsters/gornaud.md))* → [ortholion_guard_1a](#d-ortholion_guard6-ortholion_guard_1a)

    <span id="d-ortholion_guard6-ortholion_guard_0b"></span>**`ortholion_guard_0b`** Feygard scout: “Beware kid, it's dangerous out there.”

    - “I'm well prepared, thanks.” → *conversation ends*
    - “Of course it is. I am sometimes out there.” → [ortholion_guard_1b](#d-ortholion_guard6-ortholion_guard_1b)

    <span id="d-ortholion_guard6-ortholion_guard_0c"></span>**`ortholion_guard_0c`** Feygard scout: “Hey kid! Can you do me a favor?”

    - “Have you seen my brother Andor? He looks a bit like me.” → [ortholion_guard_1c](#d-ortholion_guard6-ortholion_guard_1c)
    - “No, sorry. Bye.” → *conversation ends*
    - “What is it?” → [ortholion_guard_2c](#d-ortholion_guard6-ortholion_guard_2c)

    <span id="d-ortholion_guard6-ortholion_guard_0d"></span>**`ortholion_guard_0d`** Feygard scout: “It's good to see vigorous youngsters wandering around here and there. You could become a soldier of Feygard someday.”

    - “Thanks for the compliment, sir.” → [ortholion_guard_1d](#d-ortholion_guard6-ortholion_guard_1d)
    - “And end up like you, guarding the outskirts of a tiny village? Zero action jobs aren't my type.” → *conversation ends*
    - “Sorry, but I am a follower of the Shadow.” → [ortholion_guard_1d2](#d-ortholion_guard6-ortholion_guard_1d2)

    <span id="d-ortholion_guard6-ortholion_guard_1e"></span>**`ortholion_guard_1e`** Feygard scout: “I prefer the great plains of calm, always calm Loneford ... Yes, always quiet and peaceful ...”

    - “But General Orth...” → [ortholion_guard_2e](#d-ortholion_guard6-ortholion_guard_2e)

    <span id="d-ortholion_guard6-ortholion_guard_1a"></span>**`ortholion_guard_1a`** Feygard scout: “Bah! I said I AM ON DUTY!”

    - “OK, OK. How boring...” → *conversation ends*
    - “Sorry. Goodbye.” → *conversation ends*

    <span id="d-ortholion_guard6-ortholion_guard_1b"></span>**`ortholion_guard_1b`** Feygard scout: “Ha ha! Hilarious, but seriously be careful out there.”

    - “No promises!” → *conversation ends*
    - “OK, sir. Thank you for the advice.” → *conversation ends*
    - “Shadow be with you.” → *conversation ends*

    <span id="d-ortholion_guard6-ortholion_guard_1c"></span>**`ortholion_guard_1c`** Feygard scout: “Yes, can you... Eh? Your brother? No idea. Is he from this village?”

    - “Never mind, bye.” → *conversation ends*
    - “No, he is not. But thanks anyway.” → *conversation ends*
    - “No...But tell me about the favor you were asking before.” → [ortholion_guard_2c](#d-ortholion_guard6-ortholion_guard_2c)

    <span id="d-ortholion_guard6-ortholion_guard_2c"></span>**`ortholion_guard_2c`** Feygard scout: “Well. Do you mind bringing me some food? I have not eaten anything decent since we arrived in this village.”

    - “Go buy your own food.” → *conversation ends*
    - “Here's a pork pie.” *(if hand over 1× [Pork pie](../items/pie_pork.md))* → [ortholion_guard_2c_pork](#d-ortholion_guard6-ortholion_guard_2c_pork)
    - “Here's some cheese.” *(if hand over 2× [Cheese](../items/cheese.md))* → [ortholion_guard_2c_cheese](#d-ortholion_guard6-ortholion_guard_2c_cheese)
    - “I don't have food, but here's 50 gold.” *(if pay 50 gold)* → [ortholion_guard_2c_gold](#d-ortholion_guard6-ortholion_guard_2c_gold)
    - “How about some cooked meat?” *(if hand over 1× [Cooked meat](../items/meat_cooked.md))* → [ortholion_guard_2c_meat](#d-ortholion_guard6-ortholion_guard_2c_meat)

    <span id="d-ortholion_guard6-ortholion_guard_1d"></span>**`ortholion_guard_1d`** Feygard scout: “And good-mannered too! Keep going like this.”

    - “Thank you. Have a good day, sir.” → *conversation ends*
    - “I will. How is the patrol going?” → [ortholion_guard_2d2](#d-ortholion_guard6-ortholion_guard_2d2)

    <span id="d-ortholion_guard6-ortholion_guard_1d2"></span>**`ortholion_guard_1d2`** Feygard scout: “The Shadow? Probably your parents inculcated those ideas in you. Let me tell you, they are wrong. Followers of the Shadow only promote chaos and anarchy.”

    - “Chaos and anarchy? Have you ever met a priest of the Shadow?” → [ortholion_guard_2d](#d-ortholion_guard6-ortholion_guard_2d)
    - “Hmmm, probably your parents inculcated those ideas in you. I won't try to change your mind. Bye.” → *conversation ends*

    <span id="d-ortholion_guard6-ortholion_guard_2e"></span>**`ortholion_guard_2e`** Feygard scout: “Ah! The soft breeze of the coast, the vivid life of the port of Feygard ... [The soldier continues lamenting and completely ignores your presence]”

    - “Hey, pay attention!” → [ortholion_guard_0e](#d-ortholion_guard6-ortholion_guard_0e)
    - “Okay, I give up. Let's try with someone else.” → *conversation ends*

    <span id="d-ortholion_guard6-ortholion_guard_2c_pork"></span>**`ortholion_guard_2c_pork`** Feygard scout: “Oh, looks good! Thank you, kid. Here's something shiny I've found.” — **effects:** gives 2× [Polished gem](../items/gem3.md)

    - “Gems...? Whatever, thanks anyway.” → *conversation ends*
    - “Oh! Thank you. Good luck in your duties.” → *conversation ends*

    <span id="d-ortholion_guard6-ortholion_guard_2c_cheese"></span>**`ortholion_guard_2c_cheese`** Feygard scout: “Cheese! It is rare to taste cheese out of home. In exchange, take these strawberries I gathered near Stoutford. They are fresh, but I don't like the taste.” — **effects:** gives 3× [Strawberry](../items/strawberry.md)

    - “So you already had food? I traveled a long to get that cheese. Hmpf.” → *conversation ends*
    - “Thank you. Have a good day.” → *conversation ends*

    <span id="d-ortholion_guard6-ortholion_guard_2c_gold"></span>**`ortholion_guard_2c_gold`** Feygard scout: “Well. It is said that money doesn't bring happiness but gets it closer. Thank you.”

    - “Anything for the glory of Feygard!” → *conversation ends*
    - “50 gold is a trifle to me. No worries.” → *conversation ends*
    - “Shadow be with you.” → *conversation ends*

    <span id="d-ortholion_guard6-ortholion_guard_2c_meat"></span>**`ortholion_guard_2c_meat`** Feygard scout: “Hear, hear! I won't be in shape for much longer if you keep bringing me such feasts. Take a couple of these "Izthiel" claws. They might keep you alive in case of exterme neccessity.” — **effects:** gives 4× [Izthiel claw](../items/izthiel_claw.md)

    - “I am grateful, sir. Have a nice day.” → *conversation ends*
    - “Don't stand in the same place for the full beat if you want to get in shape. Bye.” → *conversation ends*
    - “I'll keep that in mind. Thank you.” → *conversation ends*

    <span id="d-ortholion_guard6-ortholion_guard_2d2"></span>**`ortholion_guard_2d2`** Feygard scout: “About to end for me. The people of this village are exaggerating. There aren't so many monsters, they are just weak.”

    - Next → [ortholion_guard_3d4](#d-ortholion_guard6-ortholion_guard_3d4)

    <span id="d-ortholion_guard6-ortholion_guard_2d"></span>**`ortholion_guard_2d`** Feygard scout: “Oh yes. Good speakers with poison in their tongues. They conspire with the savages of the South against our righteous lord, just for restoring order in the wake of the chaos left after the war.”

    - “Hmm, I never saw it that way.” → [ortholion_guard_3d](#d-ortholion_guard6-ortholion_guard_3d)
    - “Or maybe just good speakers who don't like their rituals to be banned nonsensically...” → [ortholion_guard_3d2](#d-ortholion_guard6-ortholion_guard_3d2)
    - “Every flock has their black sheep.” → [ortholion_guard_3d3](#d-ortholion_guard6-ortholion_guard_3d3)

    <span id="d-ortholion_guard6-ortholion_guard_3d4"></span>**`ortholion_guard_3d4`** Feygard scout: “These gornauds are no match for us, soldiers of the great Feygard.”

    - “Said the heavily armored soldier...” → [ortholion_guard_4d2](#d-ortholion_guard6-ortholion_guard_4d2)
    - “Sure. How many have you killed?” → [ortholion_guard_4d3](#d-ortholion_guard6-ortholion_guard_4d3)

    <span id="d-ortholion_guard6-ortholion_guard_3d"></span>**`ortholion_guard_3d`** Feygard scout: “Your friends of the Shadow are not trustworthy. This is the best advice I can give you.”

    - “May the Shadow not be with you, then.” → *conversation ends*
    - “I will remember it...Thanks.” → *conversation ends*
    - “It'd better be. My Shadow knows what I can do with unwanted ghosts.” *(if killed 10× [Hirathil ghost](../monsters/hirathil2.md))* → *conversation ends*

    <span id="d-ortholion_guard6-ortholion_guard_3d2"></span>**`ortholion_guard_3d2`** Feygard scout: “Whatever, kid. My shift is ending and I don't like your tone. You will see that I am right when you get older.”

    - “I won't waste my time anymore with a closed-minded Feygard soldier. Bye.” → *conversation ends*
    - “I did not want to offend you... Sorry.” → *conversation ends*
    - “Maybe, but I certainly don't see myself becoming a Feygard soldier.” → *conversation ends*

    <span id="d-ortholion_guard6-ortholion_guard_3d3"></span>**`ortholion_guard_3d3`** Feygard scout: “Maybe you are right...But it's the duty of the shepherd to rid the flock of those black sheep.”

    - “Is your general a good shepherd?” → [ortholion_guard_4d](#d-ortholion_guard6-ortholion_guard_4d)
    - “Maybe you are right too. How is the patrol going?” → [ortholion_guard_2d2](#d-ortholion_guard6-ortholion_guard_2d2)

    <span id="d-ortholion_guard6-ortholion_guard_4d2"></span>**`ortholion_guard_4d2`** Feygard scout: “Heh, you have a point there, kid.”

    - “Have you seen anything out of the normal?” → [ortholion_guard_5d2](#d-ortholion_guard6-ortholion_guard_5d2)
    - “I guess. Well, see you.” → *conversation ends*
    - “Do you mind selling me some of your shiny armor? You know, I need protection.” → [ortholion_guard_5d3](#d-ortholion_guard6-ortholion_guard_5d3)

    <span id="d-ortholion_guard6-ortholion_guard_4d3"></span>**`ortholion_guard_4d3`** Feygard scout: “Well...I...Actually, I should not be talking with you during my patrol. Leave me now.”


    <span id="d-ortholion_guard6-ortholion_guard_4d"></span>**`ortholion_guard_4d`** Feygard scout: “Absolutely. He is the smartest and strongest man I ever had the honor to meet and serve.”

    - “I bet he won't survive the wyrms.” *(if killed 1× [Wyrm trainer](../monsters/wyrm_trainer.md))* → [ortholion_guard_5d](#d-ortholion_guard6-ortholion_guard_5d)
    - “I think I will leave you and your fanaticism.” → *conversation ends*

    <span id="d-ortholion_guard6-ortholion_guard_5d2"></span>**`ortholion_guard_5d2`** Feygard scout: “I can't really. Guard patrolling tends to be boring work, but someone has to do it.”

    - “I see. Hope you finish it soon, sir.” → [ortholion_guard_6d](#d-ortholion_guard6-ortholion_guard_6d)
    - “Have you found anything...for me to play with?” → [ortholion_guard_6d2](#d-ortholion_guard6-ortholion_guard_6d2)

    <span id="d-ortholion_guard6-ortholion_guard_5d3"></span>**`ortholion_guard_5d3`** Feygard scout: “Your protection inside the village is granted by us. A kid like you does not need armor, but some friends to play with.”

    - “Bah, I give up.” → *conversation ends*
    - “Tell me some interesting story to tell my friends then. Did something happen during your round?” → [ortholion_guard_5d2](#d-ortholion_guard6-ortholion_guard_5d2)

    <span id="d-ortholion_guard6-ortholion_guard_5d"></span>**`ortholion_guard_5d`** Feygard scout: “HOW DARE YOU?!”

    - “I'd better leave.” → *conversation ends*
    - “Yes, pure fanaticism.” → *conversation ends*

    <span id="d-ortholion_guard6-ortholion_guard_6d"></span>**`ortholion_guard_6d`** Feygard scout: “Thank you, kid.”


    <span id="d-ortholion_guard6-ortholion_guard_6d2"></span>**`ortholion_guard_6d2`** Feygard scout: “Huh? No. But if you have some gold to spare, I could sell you some bargains I've found during my duties.”

    - “Never mind, bye.” → *conversation ends*
    - “Sure, let me have a look.” → *shop opens*
    - “I am not looking for bargains.” → [ortholion_guard_7d](#d-ortholion_guard6-ortholion_guard_7d)

    <span id="d-ortholion_guard6-ortholion_guard_7d"></span>**`ortholion_guard_7d`** Feygard scout: “I might even have some shiny gems...”

    - “I have tons, sorry.” → *conversation ends*
    - “Hmm, ok. Let's trade.” → *shop opens*



### Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added<br>Dialogue: 30 lines added |
| [v0.8.8](../versions/0.8.8.md) | Dialogue: 3 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**3 entries.** The game data defines 3 separate characters named Feygard scout. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location, combat statistics, loot or shop stock, faction, appearance, movement.

| Entry | Type | Section |
|---|---|---|
| `feygard_scout` | NPC/Enemy | [Crossroads Guardhouse, Crossroads](#v-feygard_scout) |
| `ortholion_guard2` | NPC | [Prim, Blackwater mountain 29](#v-ortholion_guard2) |
| `ortholion_guard6` | NPC | [Prim, Blackwater mountain 10](#v-ortholion_guard6) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: feygard_scout"

    | | |
    |---|---|
    | Entry ID | `feygard_scout` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `feygard_scout` |
    | Loot table | `Feygard_scout` |
    | Conversation | `feygard_scout_3` |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_omi1:0` |
    | Defined in | `res/raw/monsterlist_omicronrg9.json` |

    Raw data:

    ```json
    {
     "id": "feygard_scout",
     "name": "Feygard scout",
     "iconID": "monsters_omi1:0",
     "maxHP": 83,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 6,
      "max": 11
     },
     "spawnGroup": "feygard_scout",
     "phraseID": "feygard_scout_3",
     "droplistID": "Feygard_scout",
     "attackCost": 5,
     "attackChance": 110,
     "criticalSkill": 25,
     "criticalMultiplier": 2.5,
     "blockChance": 95,
     "damageResistance": 5
    }
    ```

??? info "Technical information: ortholion_guard2"

    | | |
    |---|---|
    | Entry ID | `ortholion_guard2` |
    | Type (wiki) | NPC |
    | Spawn group | `ortholion_guard2` |
    | Loot table | `ortholion_guard2` |
    | Conversation | `ortholion_guard6_1` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_omi2:12` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "ortholion_guard2",
     "name": "Feygard scout",
     "iconID": "monsters_omi2:12",
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "spawnGroup": "ortholion_guard2",
     "faction": "",
     "phraseID": "ortholion_guard6_1",
     "droplistID": "ortholion_guard2"
    }
    ```

??? info "Technical information: ortholion_guard6"

    | | |
    |---|---|
    | Entry ID | `ortholion_guard6` |
    | Type (wiki) | NPC |
    | Spawn group | `ortholion_guard6` |
    | Loot table | `ortholion_guard2` |
    | Conversation | `ortholion_guard_selector` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_omi2:12` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "ortholion_guard6",
     "name": "Feygard scout",
     "iconID": "monsters_omi2:12",
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "phraseID": "ortholion_guard_selector",
     "droplistID": "ortholion_guard2"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_scout.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_scout.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_scout.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_scout.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
