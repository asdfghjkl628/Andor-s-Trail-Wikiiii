---
description: "General's henchman is an NPC who can also be fought in Andor's Trail, found in Prim. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite } General's henchman

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Role** | Shopkeeper |
| **Found in** | Prim |
| **Class** | Humanoid |
| **HP** | 1 |
| **XP when defeated** | 1 |
| **Entries in game data** | 2 |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named General's henchman. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location, loot or shop stock, movement. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`ortholion_guard1`](#v-ortholion_guard1) | NPC | Prim: [blackwater_mountain11](../maps/blackwater_mountain11.md#pin-npc-ortholion_guard1), Prim: [blackwater_mountain29](../maps/blackwater_mountain29.md#pin-npc-ortholion_guard1) | shopkeeper | – |
| [`ortholion_guard_hidden`](#v-ortholion_guard_hidden) | Enemy | Prim: [blackwater_mountain11](../maps/blackwater_mountain11.md) | – | 1 |

## Prim, Blackwater mountain11 and 1 more (ortholion_guard1) { #v-ortholion_guard1 }

**Entry ID:** `ortholion_guard1` · **Type:** NPC · **Role:** Shopkeeper

**Location:** Prim: [blackwater_mountain11](../maps/blackwater_mountain11.md#pin-npc-ortholion_guard1), Prim: [blackwater_mountain29](../maps/blackwater_mountain29.md#pin-npc-ortholion_guard1)

### Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Minor potion of health](../items/health_minor2.md) | 100% | 1 to 5 |
| [Claws](../items/claws.md) | 100% | 1 to 12 |
| [Bottle of mountain water](../items/bwm_water1.md) | 33.3333% | 1 to 10 |
| [Reinforced wooden buckler](../items/shield3.md) | 33.3333% | 0 to 2 |
| [Khakin eye](../items/khakin.md) | 25% | 1 to 10 |
| [Thin amphibian skin](../items/bwm_olm_drop.md) | 25% | 1 to 5 |
| [Milk](../items/milk.md) | 25% | 1 to 10 |
| [Fine shirt](../items/shirt2.md) | 20% | 1 |
| [Snakeskin gloves](../items/gloves3.md) | 20% | 1 |
| [Battered amphibian gloves](../items/bwm_olm_drop3.md) | 20% | 1 |
| [Leather boots](../items/boots1.md) | 20% | 1 |
| [Large bottle of mountain water](../items/bwm_water2.md) | 10% | 1 to 5 |
| [Cooked chicken leg](../items/chkn_leg.md) | 5% | 1 to 5 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [blackwater_mountain11](../maps/blackwater_mountain11.md) | Prim | 2 | Appears later, during a quest |
| [blackwater_mountain29](../maps/blackwater_mountain29.md) | Prim | 1 | Appears later, during a quest |

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with General's henchman. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/ortholion_guard_selector.json" data-npc="General&#x27;s henchman" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (33 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ortholion_guard1-ortholion_guard_selector"></span>**`ortholion_guard_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if latest stage of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-46) is 46)* → [ortholion_guard_0e](#d-ortholion_guard1-ortholion_guard_0e)
    - branch 2 *(if random chance (1/4%))* → [ortholion_guard_0a](#d-ortholion_guard1-ortholion_guard_0a)
    - branch 3 *(if random chance (1/3%))* → [ortholion_guard_0b](#d-ortholion_guard1-ortholion_guard_0b)
    - branch 4 *(if random chance (1/2%))* → [ortholion_guard_0c](#d-ortholion_guard1-ortholion_guard_0c)
    - branch 5 → [ortholion_guard_0d](#d-ortholion_guard1-ortholion_guard_0d)

    <span id="d-ortholion_guard1-ortholion_guard_0e"></span>**`ortholion_guard_0e`** General's henchman: “No, kid, I don't have anything to trade right now. I am tired of this place. Mountains are not my thing, you know?”

    - “I have a very important message fr...” → [ortholion_guard_1e](#d-ortholion_guard1-ortholion_guard_1e)

    <span id="d-ortholion_guard1-ortholion_guard_0a"></span>**`ortholion_guard_0a`** General's henchman: “I'm on duty, youngster. Go play somewhere else.”

    - “Hah! Good one. Go buy a better sword, rookie.” *(if carry 1× [Flagstone's pride](../items/sword_flagstone.md))* → *conversation ends*
    - “Sorry, bye.” → *conversation ends*
    - “How does it feel that a kid killed more gornauds than you?” *(if killed 100× [Gornaud](../monsters/gornaud.md))* → [ortholion_guard_1a](#d-ortholion_guard1-ortholion_guard_1a)

    <span id="d-ortholion_guard1-ortholion_guard_0b"></span>**`ortholion_guard_0b`** General's henchman: “Beware kid, it's dangerous out there.”

    - “I'm well prepared, thanks.” → *conversation ends*
    - “Of course it is. I am sometimes out there.” → [ortholion_guard_1b](#d-ortholion_guard1-ortholion_guard_1b)

    <span id="d-ortholion_guard1-ortholion_guard_0c"></span>**`ortholion_guard_0c`** General's henchman: “Hey kid! Can you do me a favor?”

    - “Have you seen my brother Andor? He looks a bit like me.” → [ortholion_guard_1c](#d-ortholion_guard1-ortholion_guard_1c)
    - “No, sorry. Bye.” → *conversation ends*
    - “What is it?” → [ortholion_guard_2c](#d-ortholion_guard1-ortholion_guard_2c)

    <span id="d-ortholion_guard1-ortholion_guard_0d"></span>**`ortholion_guard_0d`** General's henchman: “It's good to see vigorous youngsters wandering around here and there. You could become a soldier of Feygard someday.”

    - “Thanks for the compliment, sir.” → [ortholion_guard_1d](#d-ortholion_guard1-ortholion_guard_1d)
    - “And end up like you, guarding the outskirts of a tiny village? Zero action jobs aren't my type.” → *conversation ends*
    - “Sorry, but I am a follower of the Shadow.” → [ortholion_guard_1d2](#d-ortholion_guard1-ortholion_guard_1d2)

    <span id="d-ortholion_guard1-ortholion_guard_1e"></span>**`ortholion_guard_1e`** General's henchman: “I prefer the great plains of calm, always calm Loneford ... Yes, always quiet and peaceful ...”

    - “But General Orth...” → [ortholion_guard_2e](#d-ortholion_guard1-ortholion_guard_2e)

    <span id="d-ortholion_guard1-ortholion_guard_1a"></span>**`ortholion_guard_1a`** General's henchman: “Bah! I said I AM ON DUTY!”

    - “OK, OK. How boring...” → *conversation ends*
    - “Sorry. Goodbye.” → *conversation ends*

    <span id="d-ortholion_guard1-ortholion_guard_1b"></span>**`ortholion_guard_1b`** General's henchman: “Ha ha! Hilarious, but seriously be careful out there.”

    - “No promises!” → *conversation ends*
    - “OK, sir. Thank you for the advice.” → *conversation ends*
    - “Shadow be with you.” → *conversation ends*

    <span id="d-ortholion_guard1-ortholion_guard_1c"></span>**`ortholion_guard_1c`** General's henchman: “Yes, can you... Eh? Your brother? No idea. Is he from this village?”

    - “Never mind, bye.” → *conversation ends*
    - “No, he is not. But thanks anyway.” → *conversation ends*
    - “No...But tell me about the favor you were asking before.” → [ortholion_guard_2c](#d-ortholion_guard1-ortholion_guard_2c)

    <span id="d-ortholion_guard1-ortholion_guard_2c"></span>**`ortholion_guard_2c`** General's henchman: “Well. Do you mind bringing me some food? I have not eaten anything decent since we arrived in this village.”

    - “Go buy your own food.” → *conversation ends*
    - “Here's a pork pie.” *(if hand over 1× [Pork pie](../items/pie_pork.md))* → [ortholion_guard_2c_pork](#d-ortholion_guard1-ortholion_guard_2c_pork)
    - “Here's some cheese.” *(if hand over 2× [Cheese](../items/cheese.md))* → [ortholion_guard_2c_cheese](#d-ortholion_guard1-ortholion_guard_2c_cheese)
    - “I don't have food, but here's 50 gold.” *(if pay 50 gold)* → [ortholion_guard_2c_gold](#d-ortholion_guard1-ortholion_guard_2c_gold)
    - “How about some cooked meat?” *(if hand over 1× [Cooked meat](../items/meat_cooked.md))* → [ortholion_guard_2c_meat](#d-ortholion_guard1-ortholion_guard_2c_meat)

    <span id="d-ortholion_guard1-ortholion_guard_1d"></span>**`ortholion_guard_1d`** General's henchman: “And good-mannered too! Keep going like this.”

    - “Thank you. Have a good day, sir.” → *conversation ends*
    - “I will. How is the patrol going?” → [ortholion_guard_2d2](#d-ortholion_guard1-ortholion_guard_2d2)

    <span id="d-ortholion_guard1-ortholion_guard_1d2"></span>**`ortholion_guard_1d2`** General's henchman: “The Shadow? Probably your parents inculcated those ideas in you. Let me tell you, they are wrong. Followers of the Shadow only promote chaos and anarchy.”

    - “Chaos and anarchy? Have you ever met a priest of the Shadow?” → [ortholion_guard_2d](#d-ortholion_guard1-ortholion_guard_2d)
    - “Hmmm, probably your parents inculcated those ideas in you. I won't try to change your mind. Bye.” → *conversation ends*

    <span id="d-ortholion_guard1-ortholion_guard_2e"></span>**`ortholion_guard_2e`** General's henchman: “Ah! The soft breeze of the coast, the vivid life of the port of Feygard ... [The soldier continues lamenting and completely ignores your presence]”

    - “Hey, pay attention!” → [ortholion_guard_0e](#d-ortholion_guard1-ortholion_guard_0e)
    - “Okay, I give up. Let's try with someone else.” → *conversation ends*

    <span id="d-ortholion_guard1-ortholion_guard_2c_pork"></span>**`ortholion_guard_2c_pork`** General's henchman: “Oh, looks good! Thank you, kid. Here's something shiny I've found.” — **effects:** gives 2× [Polished gem](../items/gem3.md)

    - “Gems...? Whatever, thanks anyway.” → *conversation ends*
    - “Oh! Thank you. Good luck in your duties.” → *conversation ends*

    <span id="d-ortholion_guard1-ortholion_guard_2c_cheese"></span>**`ortholion_guard_2c_cheese`** General's henchman: “Cheese! It is rare to taste cheese out of home. In exchange, take these strawberries I gathered near Stoutford. They are fresh, but I don't like the taste.” — **effects:** gives 3× [Strawberry](../items/strawberry.md)

    - “So you already had food? I traveled a long to get that cheese. Hmpf.” → *conversation ends*
    - “Thank you. Have a good day.” → *conversation ends*

    <span id="d-ortholion_guard1-ortholion_guard_2c_gold"></span>**`ortholion_guard_2c_gold`** General's henchman: “Well. It is said that money doesn't bring happiness but gets it closer. Thank you.”

    - “Anything for the glory of Feygard!” → *conversation ends*
    - “50 gold is a trifle to me. No worries.” → *conversation ends*
    - “Shadow be with you.” → *conversation ends*

    <span id="d-ortholion_guard1-ortholion_guard_2c_meat"></span>**`ortholion_guard_2c_meat`** General's henchman: “Hear, hear! I won't be in shape for much longer if you keep bringing me such feasts. Take a couple of these "Izthiel" claws. They might keep you alive in case of exterme neccessity.” — **effects:** gives 4× [Izthiel claw](../items/izthiel_claw.md)

    - “I am grateful, sir. Have a nice day.” → *conversation ends*
    - “Don't stand in the same place for the full beat if you want to get in shape. Bye.” → *conversation ends*
    - “I'll keep that in mind. Thank you.” → *conversation ends*

    <span id="d-ortholion_guard1-ortholion_guard_2d2"></span>**`ortholion_guard_2d2`** General's henchman: “About to end for me. The people of this village are exaggerating. There aren't so many monsters, they are just weak.”

    - Next → [ortholion_guard_3d4](#d-ortholion_guard1-ortholion_guard_3d4)

    <span id="d-ortholion_guard1-ortholion_guard_2d"></span>**`ortholion_guard_2d`** General's henchman: “Oh yes. Good speakers with poison in their tongues. They conspire with the savages of the South against our righteous lord, just for restoring order in the wake of the chaos left after the war.”

    - “Hmm, I never saw it that way.” → [ortholion_guard_3d](#d-ortholion_guard1-ortholion_guard_3d)
    - “Or maybe just good speakers who don't like their rituals to be banned nonsensically...” → [ortholion_guard_3d2](#d-ortholion_guard1-ortholion_guard_3d2)
    - “Every flock has their black sheep.” → [ortholion_guard_3d3](#d-ortholion_guard1-ortholion_guard_3d3)

    <span id="d-ortholion_guard1-ortholion_guard_3d4"></span>**`ortholion_guard_3d4`** General's henchman: “These gornauds are no match for us, soldiers of the great Feygard.”

    - “Said the heavily armored soldier...” → [ortholion_guard_4d2](#d-ortholion_guard1-ortholion_guard_4d2)
    - “Sure. How many have you killed?” → [ortholion_guard_4d3](#d-ortholion_guard1-ortholion_guard_4d3)

    <span id="d-ortholion_guard1-ortholion_guard_3d"></span>**`ortholion_guard_3d`** General's henchman: “Your friends of the Shadow are not trustworthy. This is the best advice I can give you.”

    - “May the Shadow not be with you, then.” → *conversation ends*
    - “I will remember it...Thanks.” → *conversation ends*
    - “It'd better be. My Shadow knows what I can do with unwanted ghosts.” *(if killed 10× [Hirathil ghost](../monsters/hirathil2.md))* → *conversation ends*

    <span id="d-ortholion_guard1-ortholion_guard_3d2"></span>**`ortholion_guard_3d2`** General's henchman: “Whatever, kid. My shift is ending and I don't like your tone. You will see that I am right when you get older.”

    - “I won't waste my time anymore with a closed-minded Feygard soldier. Bye.” → *conversation ends*
    - “I did not want to offend you... Sorry.” → *conversation ends*
    - “Maybe, but I certainly don't see myself becoming a Feygard soldier.” → *conversation ends*

    <span id="d-ortholion_guard1-ortholion_guard_3d3"></span>**`ortholion_guard_3d3`** General's henchman: “Maybe you are right...But it's the duty of the shepherd to rid the flock of those black sheep.”

    - “Is your general a good shepherd?” → [ortholion_guard_4d](#d-ortholion_guard1-ortholion_guard_4d)
    - “Maybe you are right too. How is the patrol going?” → [ortholion_guard_2d2](#d-ortholion_guard1-ortholion_guard_2d2)

    <span id="d-ortholion_guard1-ortholion_guard_4d2"></span>**`ortholion_guard_4d2`** General's henchman: “Heh, you have a point there, kid.”

    - “Have you seen anything out of the normal?” → [ortholion_guard_5d2](#d-ortholion_guard1-ortholion_guard_5d2)
    - “I guess. Well, see you.” → *conversation ends*
    - “Do you mind selling me some of your shiny armor? You know, I need protection.” → [ortholion_guard_5d3](#d-ortholion_guard1-ortholion_guard_5d3)

    <span id="d-ortholion_guard1-ortholion_guard_4d3"></span>**`ortholion_guard_4d3`** General's henchman: “Well...I...Actually, I should not be talking with you during my patrol. Leave me now.”


    <span id="d-ortholion_guard1-ortholion_guard_4d"></span>**`ortholion_guard_4d`** General's henchman: “Absolutely. He is the smartest and strongest man I ever had the honor to meet and serve.”

    - “I bet he won't survive the wyrms.” *(if killed 1× [Wyrm trainer](../monsters/wyrm_trainer.md))* → [ortholion_guard_5d](#d-ortholion_guard1-ortholion_guard_5d)
    - “I think I will leave you and your fanaticism.” → *conversation ends*

    <span id="d-ortholion_guard1-ortholion_guard_5d2"></span>**`ortholion_guard_5d2`** General's henchman: “I can't really. Guard patrolling tends to be boring work, but someone has to do it.”

    - “I see. Hope you finish it soon, sir.” → [ortholion_guard_6d](#d-ortholion_guard1-ortholion_guard_6d)
    - “Have you found anything...for me to play with?” → [ortholion_guard_6d2](#d-ortholion_guard1-ortholion_guard_6d2)

    <span id="d-ortholion_guard1-ortholion_guard_5d3"></span>**`ortholion_guard_5d3`** General's henchman: “Your protection inside the village is granted by us. A kid like you does not need armor, but some friends to play with.”

    - “Bah, I give up.” → *conversation ends*
    - “Tell me some interesting story to tell my friends then. Did something happen during your round?” → [ortholion_guard_5d2](#d-ortholion_guard1-ortholion_guard_5d2)

    <span id="d-ortholion_guard1-ortholion_guard_5d"></span>**`ortholion_guard_5d`** General's henchman: “HOW DARE YOU?!”

    - “I'd better leave.” → *conversation ends*
    - “Yes, pure fanaticism.” → *conversation ends*

    <span id="d-ortholion_guard1-ortholion_guard_6d"></span>**`ortholion_guard_6d`** General's henchman: “Thank you, kid.”


    <span id="d-ortholion_guard1-ortholion_guard_6d2"></span>**`ortholion_guard_6d2`** General's henchman: “Huh? No. But if you have some gold to spare, I could sell you some bargains I've found during my duties.”

    - “Never mind, bye.” → *conversation ends*
    - “Sure, let me have a look.” → *shop opens*
    - “I am not looking for bargains.” → [ortholion_guard_7d](#d-ortholion_guard1-ortholion_guard_7d)

    <span id="d-ortholion_guard1-ortholion_guard_7d"></span>**`ortholion_guard_7d`** General's henchman: “I might even have some shiny gems...”

    - “I have tons, sorry.” → *conversation ends*
    - “Hmm, ok. Let's trade.” → *shop opens*



### Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added<br>Dialogue: 30 lines added |
| [v0.8.8](../versions/0.8.8.md) | Dialogue: 3 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ortholion_guard1)"

    | | |
    |---|---|
    | Entry ID | `ortholion_guard1` |
    | Spawn group | `ortholion_guard1` |
    | Loot table | `ortholion_guard1` |
    | Conversation | `ortholion_guard_selector` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_rltiles3:14` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "ortholion_guard1",
     "name": "General's henchman",
     "iconID": "monsters_rltiles3:14",
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "spawnGroup": "ortholion_guard1",
     "phraseID": "ortholion_guard_selector",
     "droplistID": "ortholion_guard1"
    }
    ```


## Prim, Blackwater mountain11 (ortholion_guard_hidden) { #v-ortholion_guard_hidden }

**Entry ID:** `ortholion_guard_hidden` · **Type:** Enemy

**Location:** Prim: [blackwater_mountain11](../maps/blackwater_mountain11.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 1 |
| XP when defeated | 1 |
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
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [blackwater_mountain11](../maps/blackwater_mountain11.md) | Prim | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ortholion_guard_hidden)"

    | | |
    |---|---|
    | Entry ID | `ortholion_guard_hidden` |
    | Spawn group | `ortholion_guard_hidden` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles3:14` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "ortholion_guard_hidden",
     "name": "General's henchman",
     "iconID": "monsters_rltiles3:14",
     "monsterClass": "humanoid",
     "spawnGroup": "ortholion_guard_hidden"
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
