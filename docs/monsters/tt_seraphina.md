---
description: "Sly Seraphina is a non-player character (NPC) in Andor's Trail, found in Prim, Vilegard, Brimhaven, Lake shore road 9, Crackshot hideout 3, Crackshot hideout 4. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_tometik7_38.png){ .sprite } Sly Seraphina

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik7_38.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Shopkeeper |
| **Found in** | Prim, Vilegard, Brimhaven, Lake shore road 9, Crackshot hideout 3, Crackshot hideout 4 |
| **Entries in game data** | 7 |
| **Introduced** | [v0.8.13](../versions/0.8.13.md) |

</div>

!!! info "7 entries in the game data"
    The game data defines 7 separate characters named Sly Seraphina. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation, location, loot or shop stock, movement. Each entry has its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`tt_seraphina`](#v-tt_seraphina) | NPC | Brimhaven: [Waterway 6](../maps/waterway6.md#pin-npc-tt_seraphina), Brimhaven: [Waytobrimhaven 3](../maps/waytobrimhaven3.md#pin-npc-tt_seraphina) (+5 more) | – |
| [`thief_seraphina`](#v-thief_seraphina) | NPC | [Lake shore road 9](../maps/lake_shore_road_9.md#pin-npc-thief_seraphina) | shopkeeper |
| [`tt_seraphina2`](#v-tt_seraphina2) | NPC | [Crackshot hideout 3](../maps/crackshot_hideout3.md#pin-npc-tt_seraphina2) | – |
| [`tt_seraphina3`](#v-tt_seraphina3) | NPC | [Crackshot hideout 4](../maps/crackshot_hideout4.md#pin-npc-tt_seraphina3) | – |
| [`tt_seraphina3b`](#v-tt_seraphina3b) | NPC | [Crackshot hideout 4](../maps/crackshot_hideout4.md#pin-npc-tt_seraphina3b) | – |
| [`tt_seraphina4`](#v-tt_seraphina4) | NPC | [Crackshot hideout 4](../maps/crackshot_hideout4.md#pin-npc-tt_seraphina4) | – |
| [`tt_seraphina5`](#v-tt_seraphina5) | NPC | [Crackshot hideout 4](../maps/crackshot_hideout4.md#pin-npc-tt_seraphina5) | – |

## Brimhaven, Waterway 6 and 6 more (tt_seraphina) { #v-tt_seraphina }

**Entry ID:** `tt_seraphina` · **Type:** NPC

**Location:** Brimhaven: [Waterway 6](../maps/waterway6.md#pin-npc-tt_seraphina), Brimhaven: [Waytobrimhaven 3](../maps/waytobrimhaven3.md#pin-npc-tt_seraphina), Loneford: [Waytobrimhaven 1](../maps/waytobrimhaven1.md#pin-npc-tt_seraphina), Prim: [Blackwater mountain 12](../maps/blackwater_mountain12.md#pin-npc-tt_seraphina), Stoutford: [Wild 21](../maps/wild21.md#pin-npc-tt_seraphina), Vilegard: [Vilegard south](../maps/vilegard_s.md#pin-npc-tt_seraphina) (+1 more)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Blackwater mountain 12](../maps/blackwater_mountain12.md) | Prim | 1 | Appears later, during a quest |
| [Sullengard 3](../maps/sullengard3.md) | – | 1 | Appears later, during a quest |
| [Vilegard south](../maps/vilegard_s.md) | Vilegard | 1 | Appears later, during a quest |
| [Waterway 6](../maps/waterway6.md) | Brimhaven | 1 | Appears later, during a quest |
| [Waytobrimhaven 1](../maps/waytobrimhaven1.md) | Loneford | 1 | Appears later, during a quest |
| [Waytobrimhaven 3](../maps/waytobrimhaven3.md) | Brimhaven | 1 | Appears later, during a quest |
| [Wild 21](../maps/wild21.md) | Stoutford | 1 | Appears later, during a quest |

### Quests

- [Search for Andor](../quests/andor.md): stages 130, 999
- [Troubling times](../quests/troubling_times.md): stages 180, 190, 192, 195

### Dialogue simulator

Set your quest stages and items, then talk to Sly Seraphina. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/tt_sly_200.json" data-npc="Sly Seraphina" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (15 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-tt_seraphina-tt_sly_200"></span>**`tt_sly_200`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT killed 5× [Seraphina's bodyguard](../monsters/tt_guys.md))* → [tt_sly_202](#d-tt_seraphina-tt_sly_202)
    - branch 2 → [tt_sly_210](#d-tt_seraphina-tt_sly_210)

    <span id="d-tt_seraphina-tt_sly_202"></span>**`tt_sly_202`** Sly Seraphina: “Watch out, kid. Behind you!”


    <span id="d-tt_seraphina-tt_sly_210"></span>**`tt_sly_210`** Sly Seraphina: “OK, you're tough, even if not smart, kid.” — **effects:** sets stage 180 of [Troubling times](../quests/troubling_times.md#stage-180), removes monsters from sullengard3, removes monsters from wild21, removes monsters from waytobrimhaven1, removes monsters from blackwater_mountain12, removes monsters from waterway6, removes monsters from vilegard_s

    - “Thank you?” → [tt_sly_211](#d-tt_seraphina-tt_sly_211)

    <span id="d-tt_seraphina-tt_sly_211"></span>**`tt_sly_211`** Sly Seraphina: “Smart enough to find me, and tough enough to beat my friends. You convinced me that we can do it.”

    - Next → [tt_sly_212](#d-tt_seraphina-tt_sly_212)

    <span id="d-tt_seraphina-tt_sly_212"></span>**`tt_sly_212`** Sly Seraphina: “As we discussed, Luthor's Ring can be found in the secret room which Crackshot tried to open with Luthor's key from Umar.”

    - Next → [tt_sly_213](#d-tt_seraphina-tt_sly_213)

    <span id="d-tt_seraphina-tt_sly_213"></span>**`tt_sly_213`** Sly Seraphina: “So you have to go and ask Umar for Luthor's key.” — **effects:** sets stage 192 of [Troubling times](../quests/troubling_times.md#stage-192)

    - “No problem.” → [tt_sly_214](#d-tt_seraphina-tt_sly_214)

    <span id="d-tt_seraphina-tt_sly_214"></span>**`tt_sly_214`** Sly Seraphina: “However, that door can only be opened if you also wear Luthor's gloves, which breaks the spell on it.”

    - “And the evil you mentioned are monsters, nothing more?” → [tt_sly_216](#d-tt_seraphina-tt_sly_216)

    <span id="d-tt_seraphina-tt_sly_216"></span>**`tt_sly_216`** Sly Seraphina: “In fact, I didn't take the time to look at them more closely. But they seemed terrible and deadly to me.”

    - Next → [tt_sly_220](#d-tt_seraphina-tt_sly_220)

    <span id="d-tt_seraphina-tt_sly_220"></span>**`tt_sly_220`** Sly Seraphina: “When the door opens, and these strong monsters escape into the open, they will attack Dhayavar, which we must avoid at all costs.”

    - Next → [tt_sly_222](#d-tt_seraphina-tt_sly_222)

    <span id="d-tt_seraphina-tt_sly_222"></span>**`tt_sly_222`** Sly Seraphina: “Which reminds me: Another kid was looking for information to open it.”

    - “That kid, did he look just like me, but older?” → [tt_sly_230](#d-tt_seraphina-tt_sly_230)

    <span id="d-tt_seraphina-tt_sly_230"></span>**`tt_sly_230`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 999 of [Search for Andor](../quests/andor.md#stage-999)

    - branch 1 → [tt_sly_240](#d-tt_seraphina-tt_sly_240)

    <span id="d-tt_seraphina-tt_sly_240"></span>**`tt_sly_240`** Sly Seraphina: “Come to think of it, he did.” — **effects:** sets stage 130 of [Search for Andor](../quests/andor.md#stage-130), sets stage 999 of [Search for Andor](../quests/andor.md#stage-999)

    - “[to self] What was Andor trying to do now?” → [tt_sly_250](#d-tt_seraphina-tt_sly_250)

    <span id="d-tt_seraphina-tt_sly_250"></span>**`tt_sly_250`** Sly Seraphina: “Looking at your strength, kid, you may just be able to beat those monsters. We might give it a try.”

    - “Thanks again.” *(if reached stage 38 of [Sullengard story flags (hidden flag)](../quests/sullengard_hidden.md#stage-38); NOT reached stage 190 of [Troubling times](../quests/troubling_times.md#stage-190))* → [tt_sly_252](#d-tt_seraphina-tt_sly_252)
    - “Thanks again.” *(if NOT reached stage 38 of [Sullengard story flags (hidden flag)](../quests/sullengard_hidden.md#stage-38))* → [tt_sly_254](#d-tt_seraphina-tt_sly_254)

    <span id="d-tt_seraphina-tt_sly_252"></span>**`tt_sly_252`** Sly Seraphina: “By the way, here's your money back. 1,000 gold.” — **effects:** sets stage 190 of [Troubling times](../quests/troubling_times.md#stage-190), gives 1000× [Gold coins](../items/gold.md)

    - “Hmm, OK.” → [tt_sly_254](#d-tt_seraphina-tt_sly_254)

    <span id="d-tt_seraphina-tt_sly_254"></span>**`tt_sly_254`** Sly Seraphina: “Meet me at the door to the secret room, and bring Luthor's key. Together with Luthor's gloves the door will open.” — **effects:** sets stage 195 of [Troubling times](../quests/troubling_times.md#stage-195), spawns monsters on crackshot_hideout3, removes monsters from sullengard3, removes monsters from sullengard3, removes monsters from wild21, removes monsters from wild21, removes monsters from waytobrimhaven1, removes monsters from waytobrimhaven1, removes monsters from blackwater_mountain12, removes monsters from blackwater_mountain12, removes monsters from waterway6, removes monsters from waterway6, removes monsters from vilegard_s, removes monsters from vilegard_s

    - “OK.” → *NPC leaves*



### Version history

| Version | Change |
|---|---|
| [v0.8.13](../versions/0.8.13.md) | Added<br>Dialogue: 15 lines added |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed<br>· text: “By the way, here's your money back. 1000 gold.” → “By the way, here's your money back. {1000} gold.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (tt_seraphina)"

    | | |
    |---|---|
    | Entry ID | `tt_seraphina` |
    | Spawn group | `tt_seraphina` |
    | Loot table | – |
    | Conversation | `tt_sly_200` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik7:38` |
    | Defined in | `res/raw/monsterlist_troubling_times.json` |

    Raw data:

    ```json
    {
     "id": "tt_seraphina",
     "name": "Sly Seraphina",
     "iconID": "monsters_tometik7:38",
     "monsterClass": "humanoid",
     "spawnGroup": "tt_seraphina",
     "phraseID": "tt_sly_200"
    }
    ```


## Lake shore road 9 (thief_seraphina) { #v-thief_seraphina }

**Entry ID:** `thief_seraphina` · **Type:** NPC · **Role:** Shopkeeper

**Location:** [Lake shore road 9](../maps/lake_shore_road_9.md#pin-npc-thief_seraphina)

### Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Armored helmet](../items/armored_helmet.md) | 100% | 1 |

### Quests

- [Troubling times](../quests/troubling_times.md): stages 110, 130, 140, 320
- [Sullengard story flags (hidden flag)](../quests/sullengard_hidden.md): stage 38

### Dialogue simulator

Set your quest stages and items, then talk to Sly Seraphina. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/thief_seraphina_selector.json" data-npc="Sly Seraphina" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (59 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-thief_seraphina-thief_seraphina_selector"></span>**`thief_seraphina_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 36 of [Sullengard story flags (hidden flag)](../quests/sullengard_hidden.md#stage-36); NOT reached stage 75 of [Another ruthless Crackshot](../quests/Thieves04.md#stage-75))* → [thief_seraphina_script_10](#d-thief_seraphina-thief_seraphina_script_10)
    - Next *(if NOT reached stage 75 of [Another ruthless Crackshot](../quests/Thieves04.md#stage-75); NOT reached stage 38 of [Sullengard story flags (hidden flag)](../quests/sullengard_hidden.md#stage-38))* → [thief_seraphina_10](#d-thief_seraphina-thief_seraphina_10)
    - Next *(if reached stage 75 of [Another ruthless Crackshot](../quests/Thieves04.md#stage-75))* → [thief_seraphina_bridge_fixed](#d-thief_seraphina-thief_seraphina_bridge_fixed)
    - Next *(if reached stage 38 of [Sullengard story flags (hidden flag)](../quests/sullengard_hidden.md#stage-38))* → [thief_seraphina_80](#d-thief_seraphina-thief_seraphina_80)

    <span id="d-thief_seraphina-thief_seraphina_script_10"></span>**`thief_seraphina_script_10`** [Sly Seraphina](../monsters/tt_seraphina.md#v-thief_seraphina): “Hey, kid! Just where do you think you're going?”

    - “Across the bridge, of course. After all, I can't swim.” → [thief_seraphina_script_20](#d-thief_seraphina-thief_seraphina_script_20)
    - “Nowhere...I guess.” → *conversation ends*

    <span id="d-thief_seraphina-thief_seraphina_10"></span>**`thief_seraphina_10`** [Sly Seraphina](../monsters/tt_seraphina.md#v-thief_seraphina): “Let me guess, you're wondering if I know how to cross the river?”

    - “Well, do you?” → [thief_seraphina_20](#d-thief_seraphina-thief_seraphina_20)

    <span id="d-thief_seraphina-thief_seraphina_bridge_fixed"></span>**`thief_seraphina_bridge_fixed`** [Sly Seraphina](../monsters/tt_seraphina.md#v-thief_seraphina): “Please move along. There's nothing to see here.”

    - “I've been wondering, do you have anything to sell?” *(if NOT reached stage 3 of [Sutdover story flags (hidden flag)](../quests/sutdover_hidden.md#stage-3); NOT carry 1× [Armored helmet](../items/armored_helmet.md); NOT wearing [Armored helmet](../items/armored_helmet.md))* → [thief_seraphina_helmet_1](#d-thief_seraphina-thief_seraphina_helmet_1)
    - “Yes, ma'am.” → *conversation ends*
    - “The Guild needs you. Umar ...” *(if reached stage 100 of [Troubling times](../quests/troubling_times.md#stage-100); NOT reached stage 140 of [Troubling times](../quests/troubling_times.md#stage-140))* → [tt_sly_10](#d-thief_seraphina-tt_sly_10)
    - “Hi Seraphina, you were away so quickly after you gave me Luthor's ring.” *(if reached stage 270 of [Troubling times](../quests/troubling_times.md#stage-270); NOT reached stage 320 of [Troubling times](../quests/troubling_times.md#stage-320))* → [tt_sly_300](#d-thief_seraphina-tt_sly_300)

    <span id="d-thief_seraphina-thief_seraphina_80"></span>**`thief_seraphina_80`** Sly Seraphina: “Why are you looking at me like that?”

    - “I want my gold back. You thief!” → [thief_seraphina_81](#d-thief_seraphina-thief_seraphina_81)

    <span id="d-thief_seraphina-thief_seraphina_script_20"></span>**`thief_seraphina_script_20`** Sly Seraphina: “The bridge is broken. You're going nowhere.”


    <span id="d-thief_seraphina-thief_seraphina_20"></span>**`thief_seraphina_20`** Sly Seraphina: “Well, as a matter of fact, I do. I have a board right here under the bridge that you can place over the hole. But it's going to cost you 1,000 gold.”

    - “Wow! All you thieves are alike. Here, take it.” *(if pay 1,000 gold)* → [thief_seraphina_30](#d-thief_seraphina-thief_seraphina_30)

    <span id="d-thief_seraphina-thief_seraphina_helmet_1"></span>**`thief_seraphina_helmet_1`** Sly Seraphina: “What, do I look like a merchant?”

    - “Well...” → [thief_seraphina_helmet_2](#d-thief_seraphina-thief_seraphina_helmet_2)

    <span id="d-thief_seraphina-tt_sly_10"></span>**`tt_sly_10`** Sly Seraphina: “Umar? Who's that?”

    - “Oh well: I am nothing. You don't see me.” → [tt_sly_12](#d-thief_seraphina-tt_sly_12)

    <span id="d-thief_seraphina-tt_sly_300"></span>**`tt_sly_300`** Sly Seraphina: “What did you expect?”

    - “Well ...” → [tt_sly_310](#d-thief_seraphina-tt_sly_310)

    <span id="d-thief_seraphina-thief_seraphina_81"></span>**`thief_seraphina_81`** Sly Seraphina: “Do I know you?”

    - “Oh, you want to play dumb? Umar will hear about this!” → *conversation ends*
    - “No time to joke - the Guild needs you. Umar ...” *(if reached stage 100 of [Troubling times](../quests/troubling_times.md#stage-100); NOT reached stage 140 of [Troubling times](../quests/troubling_times.md#stage-140))* → [tt_sly_10](#d-thief_seraphina-tt_sly_10)

    <span id="d-thief_seraphina-thief_seraphina_30"></span>**`thief_seraphina_30`** Sly Seraphina: “Great! Now, let me see. Where is that board?”

    - Next → [thief_seraphina_40](#d-thief_seraphina-thief_seraphina_40)

    <span id="d-thief_seraphina-thief_seraphina_helmet_2"></span>**`thief_seraphina_helmet_2`** Sly Seraphina: “Well, I am not. But today is your lucky day.”

    - “It is?” → [thief_seraphina_helmet_3](#d-thief_seraphina-thief_seraphina_helmet_3)

    <span id="d-thief_seraphina-tt_sly_12"></span>**`tt_sly_12`** Sly Seraphina: “That's better, little child. Get used to it.”

    - “You are right.” → [tt_sly_20](#d-thief_seraphina-tt_sly_20)
    - “I'm not a little child anymore!” → [tt_sly_14](#d-thief_seraphina-tt_sly_14)

    <span id="d-thief_seraphina-tt_sly_310"></span>**`tt_sly_310`** Sly Seraphina: “OK, I admit that you are quite good.”

    - “Thank you!” → [tt_sly_320](#d-thief_seraphina-tt_sly_320)

    <span id="d-thief_seraphina-thief_seraphina_40"></span>**`thief_seraphina_40`** [Dummy NPC](../monsters/none.md): “Seraphina bends down to look under the bridge.”

    - Next → [thief_seraphina_50](#d-thief_seraphina-thief_seraphina_50)

    <span id="d-thief_seraphina-thief_seraphina_helmet_3"></span>**`thief_seraphina_helmet_3`** Sly Seraphina: “Yes. You see, I recently "acquired" this "beauty" from a dumb guy trying to cross the bridge before you fixed it. Do you want to take a look”

    - “Yes!” → *shop opens*
    - “No, thanks. I'm leaving.” → *conversation ends*

    <span id="d-thief_seraphina-tt_sly_20"></span>**`tt_sly_20`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 120 of [Troubling times](../quests/troubling_times.md#stage-120))* → [tt_sly_50](#d-thief_seraphina-tt_sly_50)
    - branch 2 *(if reached stage 110 of [Troubling times](../quests/troubling_times.md#stage-110))* → [tt_sly_40](#d-thief_seraphina-tt_sly_40)
    - branch 3 → [tt_sly_30](#d-thief_seraphina-tt_sly_30)

    <span id="d-thief_seraphina-tt_sly_14"></span>**`tt_sly_14`** Sly Seraphina: “Then stop stomping on the ground.”

    - Next → [tt_sly_20](#d-thief_seraphina-tt_sly_20)

    <span id="d-thief_seraphina-tt_sly_320"></span>**`tt_sly_320`** Sly Seraphina: “I would actually do a job with you again if the opportunity came up.”

    - “Yes, that would be nice.” → [tt_sly_330](#d-thief_seraphina-tt_sly_330)

    <span id="d-thief_seraphina-thief_seraphina_50"></span>**`thief_seraphina_50`** [Sly Seraphina](../monsters/tt_seraphina.md#v-thief_seraphina): “Um, it's not here.”

    - “What do you mean "it's not here"? Where is it?” → [thief_seraphina_60](#d-thief_seraphina-thief_seraphina_60)

    <span id="d-thief_seraphina-tt_sly_50"></span>**`tt_sly_50`** Sly Seraphina: “Now what does Umar want?”

    - “Listen ... [whispering the password] Now you believe me? We have to remove the Striking Spectacle ...” → [tt_sly_52](#d-thief_seraphina-tt_sly_52)

    <span id="d-thief_seraphina-tt_sly_40"></span>**`tt_sly_40`** Sly Seraphina: “Now what does Umar want?”

    - “We have to remove the Striking Spectacle Shadow spell from ...” → [tt_sly_42](#d-thief_seraphina-tt_sly_42)

    <span id="d-thief_seraphina-tt_sly_30"></span>**`tt_sly_30`** Sly Seraphina: “Now what does Umar want?”

    - “We have to remove the Striking Spectacle Shadow spell from members of the Thieves' Guild. Or the Guild may as well…” → [tt_sly_32](#d-thief_seraphina-tt_sly_32)

    <span id="d-thief_seraphina-tt_sly_330"></span>**`tt_sly_330`** Sly Seraphina: “And now buzz off, kid. ... $playername.” — **effects:** sets stage 320 of [Troubling times](../quests/troubling_times.md#stage-320)

    - “[Grinning] See you.” → [tt_sly_350](#d-thief_seraphina-tt_sly_350)

    <span id="d-thief_seraphina-thief_seraphina_60"></span>**`thief_seraphina_60`** Sly Seraphina: “It must have drifted down river. Sorry!”

    - “"Sorry"? I want my gold back.” → [thief_seraphina_70](#d-thief_seraphina-thief_seraphina_70)

    <span id="d-thief_seraphina-tt_sly_52"></span>**`tt_sly_52`** Sly Seraphina: “You are still repeating yourself.”

    - “Stop that game now and answer me!” → [tt_sly_54](#d-thief_seraphina-tt_sly_54)

    <span id="d-thief_seraphina-tt_sly_42"></span>**`tt_sly_42`** Sly Seraphina: “Yes, you've said already. Stop repeating yourself.”

    - “Sure. We need Luthor's ring, and ...” → [tt_sly_44](#d-thief_seraphina-tt_sly_44)

    <span id="d-thief_seraphina-tt_sly_32"></span>**`tt_sly_32`** Sly Seraphina: “And what do I have to do with it?”

    - “We need Luthor's ring, and you know ...” → [tt_sly_34](#d-thief_seraphina-tt_sly_34)

    <span id="d-thief_seraphina-tt_sly_350"></span>**`tt_sly_350`** Sly Seraphina: “See you.”


    <span id="d-thief_seraphina-thief_seraphina_70"></span>**`thief_seraphina_70`** Sly Seraphina: “Maybe next time you come by I'll have the board?” — **effects:** sets stage 38 of [Sullengard story flags (hidden flag)](../quests/sullengard_hidden.md#stage-38)


    <span id="d-thief_seraphina-tt_sly_54"></span>**`tt_sly_54`** Sly Seraphina: “All right. Umar wants me to give you Luthor's ring? And unleash evil on all of Dhayavar?”

    - “Why would that ring unleash evil?” → [tt_sly_56](#d-thief_seraphina-tt_sly_56)

    <span id="d-thief_seraphina-tt_sly_44"></span>**`tt_sly_44`** Sly Seraphina: “Forget it, kid. Buzz off!”

    - “Sure. We need Luthor's ring, and ...” → [tt_sly_46](#d-thief_seraphina-tt_sly_46)

    <span id="d-thief_seraphina-tt_sly_34"></span>**`tt_sly_34`** Sly Seraphina: “Likely story, kid. Buzz off!” — **effects:** sets stage 110 of [Troubling times](../quests/troubling_times.md#stage-110)


    <span id="d-thief_seraphina-tt_sly_56"></span>**`tt_sly_56`** Sly Seraphina: “Not the ring itself. But the cave does, if the door is opened.”

    - “That makes even less sense. Explain.” → [tt_sly_58](#d-thief_seraphina-tt_sly_58)

    <span id="d-thief_seraphina-tt_sly_46"></span>**`tt_sly_46`** Sly Seraphina: “And please, stop repeating yourself.”


    <span id="d-thief_seraphina-tt_sly_58"></span>**`tt_sly_58`** Sly Seraphina: “Say 'please'.”

    - “No.” *(if random chance (50%))* → [tt_sly_58](#d-thief_seraphina-tt_sly_58)
    - “Never.” *(if random chance (33%))* → [tt_sly_58](#d-thief_seraphina-tt_sly_58)
    - “Forget it.” *(if random chance (33%))* → [tt_sly_58](#d-thief_seraphina-tt_sly_58)
    - “[With rolling eyes] OK - please.” → [tt_sly_60](#d-thief_seraphina-tt_sly_60)

    <span id="d-thief_seraphina-tt_sly_60"></span>**`tt_sly_60`** Sly Seraphina: “You might remember Crackshot's hideout, do you?”

    - “Of course. Behind the many ugly larvals.” → [tt_sly_62](#d-thief_seraphina-tt_sly_62)

    <span id="d-thief_seraphina-tt_sly_62"></span>**`tt_sly_62`** Sly Seraphina: “Good. Do you know why that cave in the back was sealed?”

    - “No, tell me.” → [tt_sly_70](#d-thief_seraphina-tt_sly_70)

    <span id="d-thief_seraphina-tt_sly_70"></span>**`tt_sly_70`** Sly Seraphina: “A while back, when the Thieves' Guild got successful, we managed to acquire many items of value, including magical items.”

    - Next → [tt_sly_72](#d-thief_seraphina-tt_sly_72)

    <span id="d-thief_seraphina-tt_sly_72"></span>**`tt_sly_72`** Sly Seraphina: “A place was needed to keep them safely. We heard of this deep cave where you met and bested Crackshot.”

    - “That was no easy fight.” → [tt_sly_74](#d-thief_seraphina-tt_sly_74)
    - “Phh, child's stuff.” → [tt_sly_74](#d-thief_seraphina-tt_sly_74)

    <span id="d-thief_seraphina-tt_sly_74"></span>**`tt_sly_74`** Sly Seraphina: “So, when we created that deep cave hideout for our most precious items, we never imagined that the cave held such terrible monsters. While we were exploring, they came and attacked us!”

    - Next → [tt_sly_76](#d-thief_seraphina-tt_sly_76)

    <span id="d-thief_seraphina-tt_sly_76"></span>**`tt_sly_76`** [Dummy NPC](../monsters/none.md): “Seraphina suddenly shivers.”

    - “And then?” → [tt_sly_80](#d-thief_seraphina-tt_sly_80)

    <span id="d-thief_seraphina-tt_sly_80"></span>**`tt_sly_80`** [Sly Seraphina](../monsters/tt_seraphina.md#v-thief_seraphina): “We're thieves, not warriors. We tried to escape from there. Lost a few members ...”

    - Next → [tt_sly_82](#d-thief_seraphina-tt_sly_82)

    <span id="d-thief_seraphina-tt_sly_82"></span>**`tt_sly_82`** [Sly Seraphina](../monsters/tt_seraphina.md#v-thief_seraphina): “Lost Luthor's ring in the cave in the scramble to get out.”

    - Next → [tt_sly_84](#d-thief_seraphina-tt_sly_84)

    <span id="d-thief_seraphina-tt_sly_84"></span>**`tt_sly_84`** Sly Seraphina: “Still, we managed to hold off the cave monsters, and we managed to seal it.”

    - “Using Luthor's items?” → [tt_sly_90](#d-thief_seraphina-tt_sly_90)

    <span id="d-thief_seraphina-tt_sly_90"></span>**`tt_sly_90`** Sly Seraphina: “That's right!”

    - Next → [tt_sly_92](#d-thief_seraphina-tt_sly_92)

    <span id="d-thief_seraphina-tt_sly_92"></span>**`tt_sly_92`** Sly Seraphina: “We used Luthor's Key and his gloves to seal it, by creating a magical, impermeable door.”

    - Next → [tt_sly_94](#d-thief_seraphina-tt_sly_94)

    <span id="d-thief_seraphina-tt_sly_94"></span>**`tt_sly_94`** Sly Seraphina: “Umar and I decided to separate the key and the gloves. And the two of us never meet, to keep that door permanently sealed.” — **effects:** sets stage 130 of [Troubling times](../quests/troubling_times.md#stage-130)

    - “So that the door may never be opened.” → [tt_sly_96](#d-thief_seraphina-tt_sly_96)

    <span id="d-thief_seraphina-tt_sly_96"></span>**`tt_sly_96`** Sly Seraphina: “Exactly.”

    - “But we need to retrieve Luthor's ring now.” → [tt_sly_100](#d-thief_seraphina-tt_sly_100)

    <span id="d-thief_seraphina-tt_sly_100"></span>**`tt_sly_100`** Sly Seraphina: “Even Umar's current plea will not change my mind. Whatever ails the Guild - find another solution.”

    - “What?” → [tt_sly_110](#d-thief_seraphina-tt_sly_110)

    <span id="d-thief_seraphina-tt_sly_110"></span>**`tt_sly_110`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (17%))* → [tt_sly_116](#d-thief_seraphina-tt_sly_116)
    - branch 2 *(if random chance (20%))* → [tt_sly_115](#d-thief_seraphina-tt_sly_115)
    - branch 3 *(if random chance (25%))* → [tt_sly_114](#d-thief_seraphina-tt_sly_114)
    - branch 4 *(if random chance (33%))* → [tt_sly_113](#d-thief_seraphina-tt_sly_113)
    - branch 5 *(if random chance (50%))* → [tt_sly_112](#d-thief_seraphina-tt_sly_112)
    - branch 6 → [tt_sly_111](#d-thief_seraphina-tt_sly_111)

    <span id="d-thief_seraphina-tt_sly_116"></span>**`tt_sly_116`** *(silent check: the first matching branch below is taken)* — **effects:** spawns monsters on vilegard_s, spawns monsters on vilegard_s, faction “tt_hide” set to 6

    - branch 1 → [tt_sly_120](#d-thief_seraphina-tt_sly_120)

    <span id="d-thief_seraphina-tt_sly_115"></span>**`tt_sly_115`** *(silent check: the first matching branch below is taken)* — **effects:** spawns monsters on waterway6, spawns monsters on waterway6, faction “tt_hide” set to 5

    - branch 1 → [tt_sly_120](#d-thief_seraphina-tt_sly_120)

    <span id="d-thief_seraphina-tt_sly_114"></span>**`tt_sly_114`** *(silent check: the first matching branch below is taken)* — **effects:** spawns monsters on blackwater_mountain12, spawns monsters on blackwater_mountain12, faction “tt_hide” set to 4

    - branch 1 → [tt_sly_120](#d-thief_seraphina-tt_sly_120)

    <span id="d-thief_seraphina-tt_sly_113"></span>**`tt_sly_113`** *(silent check: the first matching branch below is taken)* — **effects:** spawns monsters on waytobrimhaven1, spawns monsters on waytobrimhaven1, faction “tt_hide” set to 3

    - branch 1 → [tt_sly_120](#d-thief_seraphina-tt_sly_120)

    <span id="d-thief_seraphina-tt_sly_112"></span>**`tt_sly_112`** *(silent check: the first matching branch below is taken)* — **effects:** spawns monsters on wild21, spawns monsters on wild21, faction “tt_hide” set to 2

    - branch 1 → [tt_sly_120](#d-thief_seraphina-tt_sly_120)

    <span id="d-thief_seraphina-tt_sly_111"></span>**`tt_sly_111`** *(silent check: the first matching branch below is taken)* — **effects:** spawns monsters on sullengard3, spawns monsters on sullengard3, faction “tt_hide” set to 1

    - branch 1 → [tt_sly_120](#d-thief_seraphina-tt_sly_120)

    <span id="d-thief_seraphina-tt_sly_120"></span>**`tt_sly_120`** Sly Seraphina: “Even us thieves are not so callous as to put Dhayavar in danger. You'll never find me.” — **effects:** sets stage 140 of [Troubling times](../quests/troubling_times.md#stage-140), removes monsters from lake_shore_road_9, removes monsters from lake_shore_road_9

    - “Hey, don't run away!!” → *NPC leaves*



### Version history

| Version | Change |
|---|---|
| [v0.8.8](../versions/0.8.8.md) | Added<br>Dialogue: 13 lines added |
| [v0.8.12.1](../versions/0.8.12.1.md) | Loot table added<br>Dialogue: 3 lines added, 1 line changed |
| [v0.8.13](../versions/0.8.13.md) | Dialogue: 43 lines added, 3 lines changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed<br>· text: “Well, as a matter of fact, I do. I have a board right here under the …” → “Well, as a matter of fact, I do. I have a board right here under the …” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (thief_seraphina)"

    | | |
    |---|---|
    | Entry ID | `thief_seraphina` |
    | Spawn group | `thief_seraphina` |
    | Loot table | `thief_seraphina_dl` |
    | Conversation | `thief_seraphina_selector` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_tometik7:38` |
    | Defined in | `res/raw/monsterlist_mt_galmore.json` |

    Raw data:

    ```json
    {
     "id": "thief_seraphina",
     "name": "Sly Seraphina",
     "iconID": "monsters_tometik7:38",
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "phraseID": "thief_seraphina_selector",
     "droplistID": "thief_seraphina_dl"
    }
    ```


## Crackshot hideout 3 (tt_seraphina2) { #v-tt_seraphina2 }

**Entry ID:** `tt_seraphina2` · **Type:** NPC

**Location:** [Crackshot hideout 3](../maps/crackshot_hideout3.md#pin-npc-tt_seraphina2)

### Quests

- [Troubling times](../quests/troubling_times.md): stages 200, 210
- [Troubling times story flags (hidden flag)](../quests/troubling_times_nd.md): stage 20

### Dialogue simulator

Set your quest stages and items, then talk to Sly Seraphina. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/tt_sly2.json" data-npc="Sly Seraphina" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-tt_seraphina2-tt_sly2"></span>**`tt_sly2`** Sly Seraphina: “At last! Did you sleep all the way here?” — **effects:** sets stage 200 of [Troubling times](../quests/troubling_times.md#stage-200)

    - “Polite as ever.” → [tt_sly2_10](#d-tt_seraphina2-tt_sly2_10)

    <span id="d-tt_seraphina2-tt_sly2_10"></span>**`tt_sly2_10`** Sly Seraphina: “Give me Luthor's key now.”

    - “Haha, funny. I forgot to bring it.” *(if NOT hand over 1× [Key of Luthor](../items/key_luthor.md))* → [tt_sly2_12](#d-tt_seraphina2-tt_sly2_12)
    - “Here it is. Let's do it.” *(if hand over 1× [Key of Luthor](../items/key_luthor.md))* → [tt_sly2_20](#d-tt_seraphina2-tt_sly2_20)

    <span id="d-tt_seraphina2-tt_sly2_12"></span>**`tt_sly2_12`** [Dummy NPC](../monsters/none.md): “Seraphina stares at you in disbelief.”

    - “Eh, I'm getting it, I'm running. Just a minute ...” → [tt_sly2_14](#d-tt_seraphina2-tt_sly2_14)

    <span id="d-tt_seraphina2-tt_sly2_20"></span>**`tt_sly2_20`** [Dummy NPC](../monsters/none.md): “Seraphina takes the key and easily unlocks the door. As quick as a weasel, she slips into the dark corridor.” — **effects:** sets stage 210 of [Troubling times](../quests/troubling_times.md#stage-210), sets stage 20 of [Troubling times story flags (hidden flag)](../quests/troubling_times_nd.md#stage-20), removes monsters from crackshot_hideout3

    - “I had better follow immediately.” → *conversation ends*

    <span id="d-tt_seraphina2-tt_sly2_14"></span>**`tt_sly2_14`** [Sly Seraphina](../monsters/tt_seraphina.md#v-tt_seraphina2): “Don't you dare to come back without it!”




### Version history

| Version | Change |
|---|---|
| [v0.8.13](../versions/0.8.13.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (tt_seraphina2)"

    | | |
    |---|---|
    | Entry ID | `tt_seraphina2` |
    | Spawn group | `tt_seraphina2` |
    | Loot table | – |
    | Conversation | `tt_sly2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik7:38` |
    | Defined in | `res/raw/monsterlist_troubling_times.json` |

    Raw data:

    ```json
    {
     "id": "tt_seraphina2",
     "name": "Sly Seraphina",
     "iconID": "monsters_tometik7:38",
     "monsterClass": "humanoid",
     "spawnGroup": "tt_seraphina2",
     "phraseID": "tt_sly2"
    }
    ```


## Crackshot hideout 4 (tt_seraphina3) { #v-tt_seraphina3 }

**Entry ID:** `tt_seraphina3` · **Type:** NPC

**Location:** [Crackshot hideout 4](../maps/crackshot_hideout4.md#pin-npc-tt_seraphina3)

### Dialogue simulator

Set your quest stages and items, then talk to Sly Seraphina. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/tt_sly3.json" data-npc="Sly Seraphina" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-tt_seraphina3-tt_sly3"></span>**`tt_sly3`** Sly Seraphina: “Don't push me. I need to concentrate.”




### Version history

| Version | Change |
|---|---|
| [v0.8.13](../versions/0.8.13.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (tt_seraphina3)"

    | | |
    |---|---|
    | Entry ID | `tt_seraphina3` |
    | Spawn group | `tt_seraphina3` |
    | Loot table | – |
    | Conversation | `tt_sly3` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik7:38` |
    | Defined in | `res/raw/monsterlist_troubling_times.json` |

    Raw data:

    ```json
    {
     "id": "tt_seraphina3",
     "name": "Sly Seraphina",
     "iconID": "monsters_tometik7:38",
     "monsterClass": "humanoid",
     "spawnGroup": "tt_seraphina3",
     "phraseID": "tt_sly3"
    }
    ```


## Crackshot hideout 4 (tt_seraphina3b) { #v-tt_seraphina3b }

**Entry ID:** `tt_seraphina3b` · **Type:** NPC

**Location:** [Crackshot hideout 4](../maps/crackshot_hideout4.md#pin-npc-tt_seraphina3b)

### Dialogue simulator

Set your quest stages and items, then talk to Sly Seraphina. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/tt_sly3.json" data-npc="Sly Seraphina" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [tt_sly3](#d-tt_seraphina3-tt_sly3).


### Version history

| Version | Change |
|---|---|
| [v0.8.13](../versions/0.8.13.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (tt_seraphina3b)"

    | | |
    |---|---|
    | Entry ID | `tt_seraphina3b` |
    | Spawn group | `tt_seraphina3b` |
    | Loot table | – |
    | Conversation | `tt_sly3` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik7:38` |
    | Defined in | `res/raw/monsterlist_troubling_times.json` |

    Raw data:

    ```json
    {
     "id": "tt_seraphina3b",
     "name": "Sly Seraphina",
     "iconID": "monsters_tometik7:38",
     "monsterClass": "humanoid",
     "spawnGroup": "tt_seraphina3b",
     "phraseID": "tt_sly3"
    }
    ```


## Crackshot hideout 4 (tt_seraphina4) { #v-tt_seraphina4 }

**Entry ID:** `tt_seraphina4` · **Type:** NPC

**Location:** [Crackshot hideout 4](../maps/crackshot_hideout4.md#pin-npc-tt_seraphina4)

### Quests

- [Troubling times](../quests/troubling_times.md): stages 250, 252
- [Troubling times story flags (hidden flag)](../quests/troubling_times_nd.md): stage 30

### Dialogue simulator

Set your quest stages and items, then talk to Sly Seraphina. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/tt_sly4.json" data-npc="Sly Seraphina" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (10 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-tt_seraphina4-tt_sly4"></span>**`tt_sly4`** Sly Seraphina: “It's good to ... see you are alive, kid.” — **effects:** faction “tt_sly_attack3” +999

    - “You look terrible.” *(if NOT reached stage 250 of [Troubling times](../quests/troubling_times.md#stage-250))* → [tt_sly4_2](#d-tt_seraphina4-tt_sly4_2)
    - “You are severely wounded.” *(if NOT reached stage 250 of [Troubling times](../quests/troubling_times.md#stage-250))* → [tt_sly4_10](#d-tt_seraphina4-tt_sly4_10)
    - “You look better now.” *(if reached stage 250 of [Troubling times](../quests/troubling_times.md#stage-250))* → [tt_sly4_4](#d-tt_seraphina4-tt_sly4_4)
    - “Hey, I'm back. Don't be alarmed, I'll squeeze past you.” *(if NOT reached stage 30 of [Troubling times story flags (hidden flag)](../quests/troubling_times_nd.md#stage-30))* → [tt_sly4_6](#d-tt_seraphina4-tt_sly4_6)

    <span id="d-tt_seraphina4-tt_sly4_2"></span>**`tt_sly4_2`** [Sly Seraphina](../monsters/tt_seraphina.md#v-tt_seraphina4): “Nice compliment, kid. Ooouw ...”

    - “You are severely wounded.” → [tt_sly4_10](#d-tt_seraphina4-tt_sly4_10)

    <span id="d-tt_seraphina4-tt_sly4_10"></span>**`tt_sly4_10`** Sly Seraphina: “Give me some healing potion ... please ...”

    - “Here, have a minor vial of health.” *(if hand over 1× [Minor vial of health](../items/health_minor.md))* → [tt_sly4_12](#d-tt_seraphina4-tt_sly4_12)
    - “Here, have a minor vial of health.” *(if hand over 1× [Minor potion of health](../items/health_minor2.md))* → [tt_sly4_12](#d-tt_seraphina4-tt_sly4_12)
    - “Here, have a potion of health.” *(if hand over 1× [Regular potion of health](../items/health.md))* → [tt_sly4_20](#d-tt_seraphina4-tt_sly4_20)
    - “Here, have a major potion of health.” *(if hand over 1× [Major potion of health](../items/health_major2.md))* → [tt_sly4_20](#d-tt_seraphina4-tt_sly4_20)
    - “Here, have a major flask of health.” *(if hand over 1× [Major flask of health](../items/health_major.md))* → [tt_sly4_20](#d-tt_seraphina4-tt_sly4_20)
    - “Here, have a bonemeal potion.” *(if hand over 1× [Bonemeal potion](../items/bonemeal_potion.md))* → [tt_sly4_20](#d-tt_seraphina4-tt_sly4_20)
    - “Here, have a bonemeal potion from Lodar.” *(if hand over 1× [Lodar's bonemeal potion](../items/pot_bm_lodar.md))* → [tt_sly4_20](#d-tt_seraphina4-tt_sly4_20)
    - “Here, have this nice potion. [give her a poison potion]” *(if NOT reached stage 252 of [Troubling times](../quests/troubling_times.md#stage-252); hand over 1× [Weak poison](../items/pot_poison_weak.md))* → [tt_sly4_22](#d-tt_seraphina4-tt_sly4_22)

    <span id="d-tt_seraphina4-tt_sly4_4"></span>**`tt_sly4_4`** Sly Seraphina: “Yes, thanks to you. Just give me a few seconds ...”


    <span id="d-tt_seraphina4-tt_sly4_6"></span>**`tt_sly4_6`** *(silent check: the first matching branch below is taken)* — **effects:** moves you to [Crackshot hideout 4](../maps/crackshot_hideout4.md), sets stage 30 of [Troubling times story flags (hidden flag)](../quests/troubling_times_nd.md#stage-30)


    <span id="d-tt_seraphina4-tt_sly4_12"></span>**`tt_sly4_12`** Sly Seraphina: “That didn't work. My wounds are too deep.”

    - “Oh dear, wait, I'll get something different.” → [tt_sly4_10](#d-tt_seraphina4-tt_sly4_10)

    <span id="d-tt_seraphina4-tt_sly4_20"></span>**`tt_sly4_20`** Sly Seraphina: “Ahh, that's good. Thank you, kid ... $playername.” — **effects:** sets stage 250 of [Troubling times](../quests/troubling_times.md#stage-250)

    - “[Embarrassed] Sure thing.” → [tt_sly4_30](#d-tt_seraphina4-tt_sly4_30)

    <span id="d-tt_seraphina4-tt_sly4_22"></span>**`tt_sly4_22`** Sly Seraphina: “[Spits] What is this stuff?! Throw it away before you drink it yourself. It's rotten.” — **effects:** sets stage 252 of [Troubling times](../quests/troubling_times.md#stage-252)

    - “So - sorry.” → [tt_sly4_24](#d-tt_seraphina4-tt_sly4_24)

    <span id="d-tt_seraphina4-tt_sly4_30"></span>**`tt_sly4_30`** Sly Seraphina: “Now don't just stand around here. Look lively and find Luthor's ring.”

    - “Ah, you're back to your old self already.” → *conversation ends*

    <span id="d-tt_seraphina4-tt_sly4_24"></span>**`tt_sly4_24`** [Dummy NPC](../monsters/none.md): “You hope that she doesn't notice your guilty conscience.”

    - “You are tough.” → [tt_sly4_2](#d-tt_seraphina4-tt_sly4_2)



### Version history

| Version | Change |
|---|---|
| [v0.8.13](../versions/0.8.13.md) | Added<br>Dialogue: 10 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (tt_seraphina4)"

    | | |
    |---|---|
    | Entry ID | `tt_seraphina4` |
    | Spawn group | `tt_seraphina4` |
    | Loot table | – |
    | Conversation | `tt_sly4` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik7:38` |
    | Defined in | `res/raw/monsterlist_troubling_times.json` |

    Raw data:

    ```json
    {
     "id": "tt_seraphina4",
     "name": "Sly Seraphina",
     "iconID": "monsters_tometik7:38",
     "monsterClass": "humanoid",
     "spawnGroup": "tt_seraphina4",
     "phraseID": "tt_sly4"
    }
    ```


## Crackshot hideout 4 (tt_seraphina5) { #v-tt_seraphina5 }

**Entry ID:** `tt_seraphina5` · **Type:** NPC

**Location:** [Crackshot hideout 4](../maps/crackshot_hideout4.md#pin-npc-tt_seraphina5)

### Quests

- [Troubling times](../quests/troubling_times.md): stages 260, 270
- [Troubling times story flags (hidden flag)](../quests/troubling_times_nd.md): stage 10

### Dialogue simulator

Set your quest stages and items, then talk to Sly Seraphina. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/tt_sly5.json" data-npc="Sly Seraphina" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (14 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-tt_seraphina5-tt_sly5"></span>**`tt_sly5`** Sly Seraphina: “Suits me, this place. Don't you think?”

    - “Better help me search.” *(if reached stage 10 of [Troubling times story flags (hidden flag)](../quests/troubling_times_nd.md#stage-10); 8 rounds passed since timer “tt_search”)* → [tt_sly5_10](#d-tt_seraphina5-tt_sly5_10)
    - “[Sarcastic] Truly royal.” → [tt_sly5_2](#d-tt_seraphina5-tt_sly5_2)
    - “This throne looks familiar to me.” → [tt_sly5_8](#d-tt_seraphina5-tt_sly5_8)

    <span id="d-tt_seraphina5-tt_sly5_10"></span>**`tt_sly5_10`** Sly Seraphina: “Of course I'll help you. What are you looking for?” — **effects:** sets stage 260 of [Troubling times](../quests/troubling_times.md#stage-260)

    - “Luthor's ring, of course. I just can't find it.” → [tt_sly5_12](#d-tt_seraphina5-tt_sly5_12)

    <span id="d-tt_seraphina5-tt_sly5_2"></span>**`tt_sly5_2`** Sly Seraphina: “Royal, yes.”

    - Next → [tt_sly5_3](#d-tt_seraphina5-tt_sly5_3)

    <span id="d-tt_seraphina5-tt_sly5_8"></span>**`tt_sly5_8`** Sly Seraphina: “So you've been to King Luthor's tomb. Yes, we have ... borrowed ... his throne.”

    - “Oh.” → [tt_sly5](#d-tt_seraphina5-tt_sly5)

    <span id="d-tt_seraphina5-tt_sly5_12"></span>**`tt_sly5_12`** Sly Seraphina: “Ah - you are looking for this ring here, am I right?”

    - “What? And I've been searching here for hours!” → [tt_sly5_20](#d-tt_seraphina5-tt_sly5_20)

    <span id="d-tt_seraphina5-tt_sly5_3"></span>**`tt_sly5_3`** Sly Seraphina: “In fact, I am King Luthor's heir. He's my ancestor.” — **effects:** sets stage 10 of [Troubling times story flags (hidden flag)](../quests/troubling_times_nd.md#stage-10)

    - “Really?” → [tt_sly5_4](#d-tt_seraphina5-tt_sly5_4)

    <span id="d-tt_seraphina5-tt_sly5_20"></span>**`tt_sly5_20`** Sly Seraphina: “Well, you were so engrossed in the matter that I didn't want to disturb you.”

    - “[Grumble]” → [tt_sly5_22](#d-tt_seraphina5-tt_sly5_22)

    <span id="d-tt_seraphina5-tt_sly5_4"></span>**`tt_sly5_4`** Sly Seraphina: “How else would I be able to wear his gloves without getting hurt?”

    - “True.” → [tt_sly5_6](#d-tt_seraphina5-tt_sly5_6)

    <span id="d-tt_seraphina5-tt_sly5_22"></span>**`tt_sly5_22`** Sly Seraphina: “Okay, we're done here. We should get out of here now.”

    - Next → [tt_sly5_24](#d-tt_seraphina5-tt_sly5_24)

    <span id="d-tt_seraphina5-tt_sly5_6"></span>**`tt_sly5_6`** Sly Seraphina: “Nothing to be proud of though. Forget it, child. I should have kept quiet about it.”


    <span id="d-tt_seraphina5-tt_sly5_24"></span>**`tt_sly5_24`** Sly Seraphina: “The monsters will come back. Then the door should be closed and sealed. From the outside.”

    - “And all the riches?” → [tt_sly5_26](#d-tt_seraphina5-tt_sly5_26)

    <span id="d-tt_seraphina5-tt_sly5_26"></span>**`tt_sly5_26`** Sly Seraphina: “Don't leave anything here you want to keep. We'll never go back in here.”

    - Next → [tt_sly5_30](#d-tt_seraphina5-tt_sly5_30)

    <span id="d-tt_seraphina5-tt_sly5_30"></span>**`tt_sly5_30`** Sly Seraphina: “Here, catch the ring! Keep it safe and take it to Talion. I'm off.” — **effects:** spawns monsters on lake_shore_road_9, spawns monsters on lake_shore_road_9, removes monsters from crackshot_hideout4, sets stage 270 of [Troubling times](../quests/troubling_times.md#stage-270), gives 1× [Luthor's Ring](../items/ring_luthor.md)

    - “Wait ...” → [tt_sly5_32](#d-tt_seraphina5-tt_sly5_32)

    <span id="d-tt_seraphina5-tt_sly5_32"></span>**`tt_sly5_32`** [Dummy NPC](../monsters/none.md): “A light breeze remains where Seraphina had just been sitting.”




### Version history

| Version | Change |
|---|---|
| [v0.8.13](../versions/0.8.13.md) | Added<br>Dialogue: 14 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (tt_seraphina5)"

    | | |
    |---|---|
    | Entry ID | `tt_seraphina5` |
    | Spawn group | `tt_seraphina5` |
    | Loot table | – |
    | Conversation | `tt_sly5` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik7:38` |
    | Defined in | `res/raw/monsterlist_troubling_times.json` |

    Raw data:

    ```json
    {
     "id": "tt_seraphina5",
     "name": "Sly Seraphina",
     "iconID": "monsters_tometik7:38",
     "monsterClass": "humanoid",
     "spawnGroup": "tt_seraphina5",
     "phraseID": "tt_sly5"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tt_seraphina.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tt_seraphina.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tt_seraphina.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tt_seraphina.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
