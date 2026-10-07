---
description: "Forenza is an NPC who can also be fought in Andor's Trail, found in Lake Laeroth, Brimhaven."
---

# ![](../assets/icons/monsters/monsters_tometik7_22.png){ .sprite } Forenza

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik7_22.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Lake Laeroth, Brimhaven |
| **Class** | Humanoid |
| **HP** | 215 |
| **XP when defeated** | 302 |
| **Entries in game data** | 2 |
| **Introduced** | [v0.8.11](../versions/0.8.11.md) |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Forenza. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location, combat statistics, loot or shop stock, appearance, movement. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`forenza`](#v-forenza) | NPC/Enemy | Lake Laeroth: [laerothbasement2](../maps/laerothbasement2.md#pin-npc-forenza) | – | 215 |
| [`forenza_waytobrimhaven3`](#v-forenza_waytobrimhaven3) | NPC | Brimhaven: [waytobrimhaven3](../maps/waytobrimhaven3.md#pin-npc-forenza_waytobrimhaven3) | – | – |

## Lake Laeroth, Laerothbasement2 (forenza) { #v-forenza }

**Entry ID:** `forenza` · **Type:** NPC/Enemy

**Location:** Lake Laeroth: [laerothbasement2](../maps/laerothbasement2.md#pin-npc-forenza)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 215 |
| XP when defeated | 302 |
| Damage | 10 to 22 |
| Attack chance | 70 |
| Block chance | 50 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 2 AP |
| Critical skill | 30 |
| Critical multiplier | 2.0 |
| Critical hit chance | 19% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Forenza's key](../items/forenza_key.md) | 100% | 1 |
| [Necklace of strike](../items/necklace_strike.md) | 100% | 1 |
| [Azure gem](../items/gem6.md) | 15% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [laerothbasement2](../maps/laerothbasement2.md) | Lake Laeroth | 1 | Appears later, during a quest |

### Quests

- [The odd coin collector](../quests/odd_coin_collector.md): stages 41, 42, 43, 44, 45, 46, 47, 48, 50
- [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md): stage 104

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Forenza. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/forenza_island_selector.json" data-npc="Forenza" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (32 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-forenza-forenza_island_selector"></span>**`forenza_island_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104))* → [forenza_island_injured](#d-forenza-forenza_island_injured)
    - branch 2 → [forenza_island_initial_phrase](#d-forenza-forenza_island_initial_phrase)

    <span id="d-forenza-forenza_island_injured"></span>**`forenza_island_injured`** Forenza: “Hey, you. I need your help!”

    - “What? Who are you? How did you get in here?” → [forenza_island_injured_need_help](#d-forenza-forenza_island_injured_need_help)
    - “What kind of help?” → [forenza_island_injured_explained](#d-forenza-forenza_island_injured_explained)

    <span id="d-forenza-forenza_island_initial_phrase"></span>**`forenza_island_initial_phrase`** Forenza: “What do you think you are doing here?”

    - “Returning to Gylew what is rightfully his.” *(if reached stage 45 of [The odd coin collector](../quests/odd_coin_collector.md#stage-45))* → *fight starts*
    - “I am working a job for a man name Gylew.” *(if NOT reached stage 45 of [The odd coin collector](../quests/odd_coin_collector.md#stage-45))* → [forenza_island_10](#d-forenza-forenza_island_10)
    - “Um...I am returning something to a man named Gylew.” *(if NOT reached stage 45 of [The odd coin collector](../quests/odd_coin_collector.md#stage-45))* → [forenza_island_10](#d-forenza-forenza_island_10)

    <span id="d-forenza-forenza_island_injured_need_help"></span>**`forenza_island_injured_need_help`** Forenza: “Nerver mind that now. I am injured and I need your help!”

    - “What kind of help?” → [forenza_island_injured_explained](#d-forenza-forenza_island_injured_explained)

    <span id="d-forenza-forenza_island_injured_explained"></span>**`forenza_island_injured_explained`** Forenza: “Seriously?! Can't you see that I am bleeding and weak?” — **effects:** sets stage 41 of [The odd coin collector](../quests/odd_coin_collector.md#stage-41)

    - “Well, I have this ointment for stopping wounds. Take it.” *(if hand over 1× [Ointment of bleeding wounds](../items/pot_bleeding_ointment.md))* → [forenza_island_injured_ointment](#d-forenza-forenza_island_injured_ointment)
    - “What do you want? A healing potion maybe?” → [forenza_island_injured_help](#d-forenza-forenza_island_injured_help)

    <span id="d-forenza-forenza_island_10"></span>**`forenza_island_10`** Forenza: “I don't think you want to do that.”

    - “And why is that?” → [forenza_island_20](#d-forenza-forenza_island_20)

    <span id="d-forenza-forenza_island_injured_ointment"></span>**`forenza_island_injured_ointment`** Forenza: “Oh, that's wonderful. Thank you.” — **effects:** sets stage 42 of [The odd coin collector](../quests/odd_coin_collector.md#stage-42), sets stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104)

    - Next → [forenza_island_injured_help](#d-forenza-forenza_island_injured_help)

    <span id="d-forenza-forenza_island_injured_help"></span>**`forenza_island_injured_help`** Forenza: “Please. I'll take whatever you have that could heal me.”

    - “Well I have a bonemeal potion. It's yours now. Take it.” *(if hand over 1× [Bonemeal potion](../items/bonemeal_potion.md))* → [forenza_island_injured_help_bm](#d-forenza-forenza_island_injured_help_bm)
    - “Well I have a special bonemeal potion. It's yours now. Take it.” *(if hand over 1× [Lodar's bonemeal potion](../items/pot_bm_lodar.md))* → [forenza_island_injured_help_bm](#d-forenza-forenza_island_injured_help_bm)
    - “Here, take it. It's a really strong potion of healing.” *(if hand over 1× [Major potion of health](../items/health_major2.md))* → [forenza_island_injured_help_mph](#d-forenza-forenza_island_injured_help_mph)
    - “I have this really special potion of healing that I got from a very wise old man. Take it!” *(if hand over 1× [Lodar's potion of health](../items/pot_healthlodar.md))* → [forenza_island_injured_help_lph](#d-forenza-forenza_island_injured_help_lph)
    - “I have an ordinary potion of health for you. Take it!” *(if hand over 1× [Regular potion of health](../items/health.md))* → [forenza_island_injured_help_rph](#d-forenza-forenza_island_injured_help_rph)
    - “I have an little health potion for you. It's all I have. Take it!” *(if hand over 1× [Minor potion of health](../items/health_minor2.md))* → [forenza_island_injured_help_minor_ph](#d-forenza-forenza_island_injured_help_minor_ph)
    - “I'm so sorry, but I have nothing that can help you.” *(if NOT carry 1× [Bonemeal potion](../items/bonemeal_potion.md); NOT carry 1× [Lodar's bonemeal potion](../items/pot_bm_lodar.md); NOT carry 1× [Lodar's potion of health](../items/pot_healthlodar.md); NOT carry 1× [Major potion of health](../items/health_major2.md); NOT carry 1× [Regular potion of health](../items/health.md); NOT carry 1× [Minor potion of health](../items/health_minor2.md))* → [forenza_island_injured_help_not](#d-forenza-forenza_island_injured_help_not)

    <span id="d-forenza-forenza_island_20"></span>**`forenza_island_20`** Forenza: “Well, for starters, that chest that you are carrying belongs to me.”

    - “How do you figure?” → [forenza_island_30](#d-forenza-forenza_island_30)

    <span id="d-forenza-forenza_island_injured_help_bm"></span>**`forenza_island_injured_help_bm`** Forenza: “Oh, this stuff is great!” — **effects:** sets stage 43 of [The odd coin collector](../quests/odd_coin_collector.md#stage-43), sets stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104)

    - Next → [forenza_island_initial_phrase](#d-forenza-forenza_island_initial_phrase)

    <span id="d-forenza-forenza_island_injured_help_mph"></span>**`forenza_island_injured_help_mph`** Forenza: “This stuff tastes nasty, but I swear I can feel it helping already.” — **effects:** sets stage 44 of [The odd coin collector](../quests/odd_coin_collector.md#stage-44), sets stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104)

    - Next → [forenza_island_initial_phrase](#d-forenza-forenza_island_initial_phrase)

    <span id="d-forenza-forenza_island_injured_help_lph"></span>**`forenza_island_injured_help_lph`** Forenza: “Oh, now this stuff feels like its healing power will last just a little bit longer.” — **effects:** sets stage 46 of [The odd coin collector](../quests/odd_coin_collector.md#stage-46), sets stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104)

    - Next → [forenza_island_initial_phrase](#d-forenza-forenza_island_initial_phrase)

    <span id="d-forenza-forenza_island_injured_help_rph"></span>**`forenza_island_injured_help_rph`** Forenza: “Oh, this should help. Thank you.” — **effects:** sets stage 47 of [The odd coin collector](../quests/odd_coin_collector.md#stage-47), sets stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104)

    - Next → [forenza_island_initial_phrase](#d-forenza-forenza_island_initial_phrase)

    <span id="d-forenza-forenza_island_injured_help_minor_ph"></span>**`forenza_island_injured_help_minor_ph`** Forenza: “Oh, this should help. I guess.” — **effects:** sets stage 48 of [The odd coin collector](../quests/odd_coin_collector.md#stage-48), sets stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104)

    - Next → [forenza_island_initial_phrase](#d-forenza-forenza_island_initial_phrase)

    <span id="d-forenza-forenza_island_injured_help_not"></span>**`forenza_island_injured_help_not`** Forenza: “You are a disappointment. Anyways...” — **effects:** sets stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104)

    - Next → [forenza_island_initial_phrase](#d-forenza-forenza_island_initial_phrase)

    <span id="d-forenza-forenza_island_30"></span>**`forenza_island_30`** Forenza: “Because I said it does! Now give me that chest before you get hurt.”

    - “Don't make me laugh. You hurt me? Do you know who I am? Explain yourself now.” → [forenza_island_40](#d-forenza-forenza_island_40)
    - “Explain yourself now or Gylew gets his treasure.” → [forenza_island_40](#d-forenza-forenza_island_40)

    <span id="d-forenza-forenza_island_40"></span>**`forenza_island_40`** Forenza: “The story starts many many years ago.”

    - “[You rudely interrupt] Oh great, please spare me the grandpa story.” → [forenza_island_50](#d-forenza-forenza_island_50)

    <span id="d-forenza-forenza_island_50"></span>**`forenza_island_50`** Forenza: “Anyways...it was back when we were kids. You see, Gylew and I are half-brothers.”

    - Next → [forenza_island_60](#d-forenza-forenza_island_60)

    <span id="d-forenza-forenza_island_60"></span>**`forenza_island_60`** Forenza: “We have the same father. After Gylew's mom died of the Great Plague, father traveled to Brightport in search of a new wife.”

    - Next → [forenza_island_70](#d-forenza-forenza_island_70)

    <span id="d-forenza-forenza_island_70"></span>**`forenza_island_70`** Forenza: “To "spare you of the grandpa story" as you called it, I will skip details.”

    - “Thank you very much.” → [forenza_island_80](#d-forenza-forenza_island_80)

    <span id="d-forenza-forenza_island_80"></span>**`forenza_island_80`** Forenza: “Eventually, they were married and I was soon born. Gylew and I were close in age and often got along great.”

    - Next → [forenza_island_90](#d-forenza-forenza_island_90)

    <span id="d-forenza-forenza_island_90"></span>**`forenza_island_90`** Forenza: “But father always favored Gylew. They often took long trips in search of exotic and unique coins. I was left out of these adventures most of the time.”

    - Next → [forenza_island_100](#d-forenza-forenza_island_100)

    <span id="d-forenza-forenza_island_100"></span>**`forenza_island_100`** Forenza: “I was only allowed to go after mother insisted to father that I go too.”

    - “What happened to skipping the details?” → [forenza_island_110](#d-forenza-forenza_island_110)
    - “Please continue.” → [forenza_island_110](#d-forenza-forenza_island_110)

    <span id="d-forenza-forenza_island_110"></span>**`forenza_island_110`** Forenza: “OK...Gylew and father discovered this story of looted gold coins that were rumored to be hidden here in the Laeroth Manor. But neither was strong enough to dare try to retrieve it.”

    - Next → [forenza_island_120](#d-forenza-forenza_island_120)

    <span id="d-forenza-forenza_island_120"></span>**`forenza_island_120`** Forenza: “For many years afterwards, this is all the family ever talked about. During this time, my father and I grew apart and eventually, my mother and I left him and returned to her hometown of Brightport.”

    - Next → [forenza_island_130](#d-forenza-forenza_island_130)

    <span id="d-forenza-forenza_island_130"></span>**`forenza_island_130`** Forenza: “I was able to make it back to him shortly before his death in an attempt to repair our broken relationship.”

    - “What happened to skipping the details?” → [forenza_island_140](#d-forenza-forenza_island_140)
    - “Please, continue.” → [forenza_island_140](#d-forenza-forenza_island_140)

    <span id="d-forenza-forenza_island_140"></span>**`forenza_island_140`** Forenza: “Angry with him, I was able to steal this key [Forenza shows you what you suspect is the key to the chest] from his estate before it was given to Gylew.”

    - Next → [forenza_island_150](#d-forenza-forenza_island_150)

    <span id="d-forenza-forenza_island_150"></span>**`forenza_island_150`** Forenza: “A few years later I learned what this key opened and this is why I am here. To my disappointment, I quickly realized I was missing the second key.”

    - “Where do you think the other key is?” → [forenza_island_160](#d-forenza-forenza_island_160)
    - “[Sarcasm] I like the 'stories with Grandpa hour'. But seriously, skip the details and tell me where the other key is.” → [forenza_island_160](#d-forenza-forenza_island_160)

    <span id="d-forenza-forenza_island_160"></span>**`forenza_island_160`** Forenza: “Isn't it obvious? Gylew must have it.”

    - “You have been wronged by your family and deserve this treasure. I can get Gylew's key for you.” → [forenza_island_170](#d-forenza-forenza_island_170)
    - “Gylew is the rightful owner of his father's estate and that key belongs to the estate.” → [forenza_island_170_attack](#d-forenza-forenza_island_170_attack)

    <span id="d-forenza-forenza_island_170"></span>**`forenza_island_170`** Forenza: “You will do this for me?”

    - “Yes.” → [forenza_island_180](#d-forenza-forenza_island_180)
    - “On second thought...” → [forenza_island_170_attack](#d-forenza-forenza_island_170_attack)

    <span id="d-forenza-forenza_island_170_attack"></span>**`forenza_island_170_attack`** Forenza: “What are you going to do about it?” — **effects:** sets stage 45 of [The odd coin collector](../quests/odd_coin_collector.md#stage-45)

    - “Kill you and take that key!” → *fight starts*

    <span id="d-forenza-forenza_island_180"></span>**`forenza_island_180`** Forenza: “Great. Go to Gylew and get his key. Then bring it and the chest to me. I will meet you outside of Brimhaven.” — **effects:** sets stage 50 of [The odd coin collector](../quests/odd_coin_collector.md#stage-50), removes monsters from laerothbasement2, spawns monsters on waytobrimhaven3




### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 32 lines added |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 2 lines changed<br>· text: “I was only allowed to go after mother instisted to father that I go t…” → “I was only allowed to go after mother insisted to father that I go to…”<br>· text: “Nervermind that now. I am injured and I need your help!” → “Nerver mind that now. I am injured and I need your help!” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 2 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (forenza)"

    | | |
    |---|---|
    | Entry ID | `forenza` |
    | Spawn group | `forenza_laerothisland2` |
    | Loot table | `forenza_dl` |
    | Conversation | `forenza_island_selector` |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_tometik7:22` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "forenza",
     "name": "Forenza",
     "iconID": "monsters_tometik7:22",
     "maxHP": 215,
     "moveCost": 2,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 10,
      "max": 22
     },
     "spawnGroup": "forenza_laerothisland2",
     "phraseID": "forenza_island_selector",
     "droplistID": "forenza_dl",
     "attackCost": 4,
     "attackChance": 70,
     "criticalSkill": 30,
     "criticalMultiplier": 2.0,
     "blockChance": 50
    }
    ```


## Brimhaven, Waytobrimhaven3 (forenza_waytobrimhaven3) { #v-forenza_waytobrimhaven3 }

**Entry ID:** `forenza_waytobrimhaven3` · **Type:** NPC

**Location:** Brimhaven: [waytobrimhaven3](../maps/waytobrimhaven3.md#pin-npc-forenza_waytobrimhaven3)

### Quests

- [The odd coin collector](../quests/odd_coin_collector.md): stages 60, 110, 115
- [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md): stages 44, 45, 47, 48
- [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md): stage 255
- [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md): stages 106, 107, 108

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Forenza. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/forenza_waytobrimhaven3_initial_phrase.json" data-npc="Forenza" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (36 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-forenza_waytobrimhaven3-forenza_waytobrimhaven3_initial_phrase"></span>**`forenza_waytobrimhaven3_initial_phrase`** Forenza: “Hey, kid, nice to see you again.”

    - “It's nice to see you too. Can we talk about the Korhald coins?” *(if latest stage of [The odd coin collector](../quests/odd_coin_collector.md#stage-63) is 63; NOT reached stage 60 of [The odd coin collector](../quests/odd_coin_collector.md#stage-60))* → [forenza_brimhaven_5](#d-forenza_waytobrimhaven3-forenza_brimhaven_5)
    - “Hey. I found the Korhald tomb and it had two items that I think might interest you.” *(if latest stage of [The odd coin collector](../quests/odd_coin_collector.md#stage-65) is 65; carry 1× [Shield of the Brave](../items/shield_of_brave.md); carry 1× [Coin of Prestige](../items/hero_coin.md))* → [forenza_korhald_cop_0](#d-forenza_waytobrimhaven3-forenza_korhald_cop_0)
    - “Hey. I found the Korhald tomb and it had two items that I think might interest you.” *(if latest stage of [The odd coin collector](../quests/odd_coin_collector.md#stage-65) is 65; wearing [Shield of the Brave](../items/shield_of_brave.md); carry 1× [Coin of Prestige](../items/hero_coin.md))* → [forenza_korhald_cop_0](#d-forenza_waytobrimhaven3-forenza_korhald_cop_0)
    - “Inside the Korhald tomb, I found a locked chest. Do you know where I can find its key?” *(if reached stage 65 of [The odd coin collector](../quests/odd_coin_collector.md#stage-65); reached stage 50 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-50))* → [odd_coin_collector_ask_about_locked_chest](#d-forenza_waytobrimhaven3-odd_coin_collector_ask_about_locked_chest)
    - “I tried to get Gylew's key, but...” *(if latest stage of [The odd coin collector](../quests/odd_coin_collector.md#stage-62) is 62)* → [forenza_korhald_gylew_not_dead](#d-forenza_waytobrimhaven3-forenza_korhald_gylew_not_dead)
    - “I have not gone back to see Gylew since our last encounter. Why am I wasting time talking to you when the job is not…” *(if latest stage of [The odd coin collector](../quests/odd_coin_collector.md#stage-50) is 50)* → *conversation ends*
    - “Hey. I need to go now and follow this map.” *(if latest stage of [The odd coin collector](../quests/odd_coin_collector.md#stage-60) is 60)* → *conversation ends*
    - “I found these glowing coins in a pit beneath the well in Wexlow Village. They seem magical.” *(if reached stage 110 of [The odd coin collector](../quests/odd_coin_collector.md#stage-110); carry 3× [Mysterious coin](../items/mysterious_coin.md))* → [coin_collector_troll_coins](#d-forenza_waytobrimhaven3-coin_collector_troll_coins)
    - “I visited your daughter Florencia in Brightport. She wishes you would come home more often.” *(if reached stage 254 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-254); NOT reached stage 255 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-255))* → [brightport_forenza](#d-forenza_waytobrimhaven3-brightport_forenza)
    - “We have no more business to discuss. I'll see you later.” *(if reached stage 110 of [The odd coin collector](../quests/odd_coin_collector.md#stage-110))* → *conversation ends*
    - “I found these glowing coins in a pit beneath the well in Wexlow Village. They seem magical.” *(if reached stage 115 of [The odd coin collector](../quests/odd_coin_collector.md#stage-115); carry 3× [Mysterious coin](../items/mysterious_coin.md))* → [coin_collector_troll_coins](#d-forenza_waytobrimhaven3-coin_collector_troll_coins)
    - “I hope that these coins will enable you to make peace with your father. Take care.” *(if reached stage 115 of [The odd coin collector](../quests/odd_coin_collector.md#stage-115))* → *conversation ends*
    - “[Lie] I have these bronze and silver coins that I "acquired" in a game of chance. I would like to know if you are…” *(if reached stage 106 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-106); reached stage 80 of [Wanted men](../quests/wanted_men.md#stage-80); carry 60× [Silver coin](../items/silver_coin.md); carry 50× [Bronze coin](../items/bronze_coin.md); NOT reached stage 107 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-107))* → [coin_collector_thief_coins_10](#d-forenza_waytobrimhaven3-coin_collector_thief_coins_10)

    <span id="d-forenza_waytobrimhaven3-forenza_brimhaven_5"></span>**`forenza_brimhaven_5`** Forenza: “Do you have Gylew's key?”

    - “Yes, and I also have the chest. Here, take them. [You give both items to Forenza]” *(if hand over 1× [Gylew's key](../items/gylew_key.md); hand over 1× [Korhald coin chest](../items/korhald_coins.md))* → [forenza_brimhaven_10](#d-forenza_waytobrimhaven3-forenza_brimhaven_10)
    - “Yes, but I don't have the chest.” *(if carry 1× [Gylew's key](../items/gylew_key.md); NOT carry 1× [Korhald coin chest](../items/korhald_coins.md))* → [forenza_brimhaven_15](#d-forenza_waytobrimhaven3-forenza_brimhaven_15)
    - “What are you talking about? I already gave it to you along with the chest I found on the island.” *(if reached stage 108 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-108); NOT reached stage 60 of [The odd coin collector](../quests/odd_coin_collector.md#stage-60))* → [forenza_brimhaven_11](#d-forenza_waytobrimhaven3-forenza_brimhaven_11)
    - “No” *(if NOT carry 1× [Gylew's key](../items/gylew_key.md))* → [forenza_brimhaven_15](#d-forenza_waytobrimhaven3-forenza_brimhaven_15)

    <span id="d-forenza_waytobrimhaven3-forenza_korhald_cop_0"></span>**`forenza_korhald_cop_0`** Forenza: “Oh, really?! Let me see them and we can talk more.”

    - “[You show Forenza the Coin of Prestige and the Shield of the brave]” → [forenza_korhald_cop_10](#d-forenza_waytobrimhaven3-forenza_korhald_cop_10)

    <span id="d-forenza_waytobrimhaven3-odd_coin_collector_ask_about_locked_chest"></span>**`odd_coin_collector_ask_about_locked_chest`** Forenza: “A locked chest you say? Well, I'm not really sure, but logic tells me to look back in the Laeroth Manor.”

    - “Oh, yeah. That makes sense.” → *conversation ends*
    - “Oh, come on! I don't want to go back there again.” → *conversation ends*

    <span id="d-forenza_waytobrimhaven3-forenza_korhald_gylew_not_dead"></span>**`forenza_korhald_gylew_not_dead`** Forenza: “You wimp! Get me my brother's key now.”


    <span id="d-forenza_waytobrimhaven3-coin_collector_troll_coins"></span>**`coin_collector_troll_coins`** Forenza: “Ah, these are Enchanted Coins, crafted by ancient wizards who once drew magic from the well's waters. The runes on these coins change patterns, a sign of their magical origin. Such artifacts are rare indeed.”

    - “What can you tell me about their enchantment?” → [coin_collector_troll_coins_2](#d-forenza_waytobrimhaven3-coin_collector_troll_coins_2)
    - “Boring.” → *conversation ends*

    <span id="d-forenza_waytobrimhaven3-brightport_forenza"></span>**`brightport_forenza`** Forenza: “Yes... maybe I should do that sometime. Take care, $playername.” — **effects:** sets stage 255 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-255)


    <span id="d-forenza_waytobrimhaven3-coin_collector_thief_coins_10"></span>**`coin_collector_thief_coins_10`** Forenza: “Sure. Let's see what you have.”

    - “[Show the coins]” → [coin_collector_thief_coins_20](#d-forenza_waytobrimhaven3-coin_collector_thief_coins_20)

    <span id="d-forenza_waytobrimhaven3-forenza_brimhaven_10"></span>**`forenza_brimhaven_10`** [Dummy NPC](../monsters/none.md): “With an ever growing smile upon his face, Forenza inserts the first key and then the second. He then proceeds to slowly open the chest.” — **effects:** sets stage 108 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-108)

    - Next → [korhald_chest_examine_10](#d-forenza_waytobrimhaven3-korhald_chest_examine_10)

    <span id="d-forenza_waytobrimhaven3-forenza_brimhaven_15"></span>**`forenza_brimhaven_15`** Forenza: “Well, go get it and bring me back both the key and the chest.”

    - “Yes sir!” → *conversation ends*

    <span id="d-forenza_waytobrimhaven3-forenza_brimhaven_11"></span>**`forenza_brimhaven_11`** Forenza: “Oh, yeah. Let's look in that chest now.”

    - Next → [korhald_chest_examine_10](#d-forenza_waytobrimhaven3-korhald_chest_examine_10)

    <span id="d-forenza_waytobrimhaven3-forenza_korhald_cop_10"></span>**`forenza_korhald_cop_10`** Forenza: “Hmm...these are indeed interesting. Very interesting in fact.”

    - “[While trying to hold back the giant smile that you can feel growing upon your face, you ask:] 'Why is that'?” → [forenza_korhald_cop_20](#d-forenza_waytobrimhaven3-forenza_korhald_cop_20)

    <span id="d-forenza_waytobrimhaven3-coin_collector_troll_coins_2"></span>**`coin_collector_troll_coins_2`** Forenza: “The coins hold a faint echo of the well's enchantment. Though their magic is subtle, they carry the essence of the well's power. As a token of my gratitude for bringing these to me, I offer you this rare artifact in exchange for three of…”

    - “Without knowing more about this "rare artifact", I'm afraid that I will have to pass on your offer.” → [coin_collector_troll_coins_3a](#d-forenza_waytobrimhaven3-coin_collector_troll_coins_3a)
    - “Umm, I guess I can trust you now.” *(if hand over 3× [Mysterious coin](../items/mysterious_coin.md))* → [coin_collector_troll_coins_3b](#d-forenza_waytobrimhaven3-coin_collector_troll_coins_3b)

    <span id="d-forenza_waytobrimhaven3-coin_collector_thief_coins_20"></span>**`coin_collector_thief_coins_20`** Forenza: “[The coin collector eagerly examines the pilfered coins, eyes gleaming with fascination.]...”

    - Next → [coin_collector_thief_coins_30](#d-forenza_waytobrimhaven3-coin_collector_thief_coins_30)

    <span id="d-forenza_waytobrimhaven3-korhald_chest_examine_10"></span>**`korhald_chest_examine_10`** Forenza: “He then begins to feverlessly sift through the coins, transferring each one to his bag. When to his surpirse, he finds something...”

    - Next → [korhald_chest_examine_20](#d-forenza_waytobrimhaven3-korhald_chest_examine_20)

    <span id="d-forenza_waytobrimhaven3-forenza_korhald_cop_20"></span>**`forenza_korhald_cop_20`** Forenza: “Well, for obvious reasons. Didn't you notice that the shield has the Korhald family crest engraved on its front side? This clearly belonged to Korhald himself. You should keep this item as it could aid you in your adventures.”

    - Next → [forenza_korhald_cop_30](#d-forenza_waytobrimhaven3-forenza_korhald_cop_30)

    <span id="d-forenza_waytobrimhaven3-coin_collector_troll_coins_3a"></span>**`coin_collector_troll_coins_3a`** Forenza: “Well, if you change your mind, I will be here.”


    <span id="d-forenza_waytobrimhaven3-coin_collector_troll_coins_3b"></span>**`coin_collector_troll_coins_3b`** Forenza: “For your effort in retrieving these valuable coins, take this rare artifact. It is a relic from the same era as the coins, crafted with similar enchantments. It will serve you well in your journeys, offering protection and a touch of…” — **effects:** gives 1× [Circlet of clarity](../items/circlet_clarity.md)


    <span id="d-forenza_waytobrimhaven3-coin_collector_thief_coins_30"></span>**`coin_collector_thief_coins_30`** Forenza: “Ah, these coins tell a tale of clandestine dealings and shadowy alliances.”

    - Next → [coin_collector_thief_coins_35](#d-forenza_waytobrimhaven3-coin_collector_thief_coins_35)

    <span id="d-forenza_waytobrimhaven3-korhald_chest_examine_20"></span>**`korhald_chest_examine_20`** [Forenza](../monsters/forenza.md#v-forenza_waytobrimhaven3): “Look at what I found at the bottom of the chest. A pendant and a map. [Shows item to you]”

    - “A map? Really? Where does it point to?” → [korhald_chest_examine_30](#d-forenza_waytobrimhaven3-korhald_chest_examine_30)

    <span id="d-forenza_waytobrimhaven3-forenza_korhald_cop_30"></span>**`forenza_korhald_cop_30`** Forenza: “But this coin you have here really gives my pause, as I never believed the stories about its existence were true. I don't know much about it, but I do know that it has great value. Can I have it? I will reward you for it of course.”

    - “Reward?! I always love the sound of that. What are we talking here? 10,000 gold? 20,000 gold?” → [forenza_korhald_cop_40](#d-forenza_waytobrimhaven3-forenza_korhald_cop_40)
    - “Here, take it. I have enough coins.” *(if hand over 1× [Coin of Prestige](../items/hero_coin.md))* → [forenza_korhald_cop_35](#d-forenza_waytobrimhaven3-forenza_korhald_cop_35)

    <span id="d-forenza_waytobrimhaven3-coin_collector_thief_coins_35"></span>**`coin_collector_thief_coins_35`** Forenza: “These bronze pieces bear the mark of the Lunar Whisper, an infamous thieves' guild that once ruled the underground markets. Legend has it, these coins were minted in secret, their alloy infused with fragments of moonstone to enhance the…”

    - Next → [coin_collector_thief_coins_40](#d-forenza_waytobrimhaven3-coin_collector_thief_coins_40)

    <span id="d-forenza_waytobrimhaven3-korhald_chest_examine_30"></span>**`korhald_chest_examine_30`** Forenza: “Well, that is really hard to say. You see [he shows you the map], it is really old and a lot of the landmarks no longer exist in Dhayavar.”

    - “Yeah, I can see what you mean.” → [korhald_chest_examine_40](#d-forenza_waytobrimhaven3-korhald_chest_examine_40)

    <span id="d-forenza_waytobrimhaven3-forenza_korhald_cop_40"></span>**`forenza_korhald_cop_40`** Forenza: “[While laughing] Now, now, who do you think I am, Gylew? I don't have that kind of gold. How about 7,000 gold?”

    - “Sounds like a great deal. I'll take it.” *(if hand over 1× [Coin of Prestige](../items/hero_coin.md))* → [forenza_korhald_cop_50](#d-forenza_waytobrimhaven3-forenza_korhald_cop_50)
    - “Let me think about it. I will be back shortly.” → [forenza_korhald_41](#d-forenza_waytobrimhaven3-forenza_korhald_41)

    <span id="d-forenza_waytobrimhaven3-forenza_korhald_cop_35"></span>**`forenza_korhald_cop_35`** Forenza: “Oh, how very generous of you to just hand it over for free. I'll tell you what, once you find your way to Brightport, seek out my family. They will reward you for all of your generosity and hard work.” — **effects:** sets stage 115 of [The odd coin collector](../quests/odd_coin_collector.md#stage-115), clears stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47), sets stage 106 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-106)


    <span id="d-forenza_waytobrimhaven3-coin_collector_thief_coins_40"></span>**`coin_collector_thief_coins_40`** Forenza: “These silver coins hold the captivating history of a nomadic people, a seafaring tribe whose exploits were as boundless as the horizon. Born from the hands of skilled minters among the maritime wanderers, these coins tell the tale of the…”

    - Next → [coin_collector_thief_coins_45](#d-forenza_waytobrimhaven3-coin_collector_thief_coins_45)

    <span id="d-forenza_waytobrimhaven3-korhald_chest_examine_40"></span>**`korhald_chest_examine_40`** Forenza: “But not all hope is lost. You see this map shows the great river that is just right over there [points northeast] behind those trees. Anyone who follows the map going east, should have no problem reaching wherever this map is leading to.”

    - Next → [korhald_chest_examine_50](#d-forenza_waytobrimhaven3-korhald_chest_examine_50)

    <span id="d-forenza_waytobrimhaven3-forenza_korhald_cop_50"></span>**`forenza_korhald_cop_50`** Forenza: “Excellent. Come see me if you ever find any more interesting coins.” — **effects:** gives [Gold coins](../items/gold.md), sets stage 110 of [The odd coin collector](../quests/odd_coin_collector.md#stage-110), clears stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47), sets stage 106 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-106)


    <span id="d-forenza_waytobrimhaven3-forenza_korhald_41"></span>**`forenza_korhald_41`** Forenza: “OK, but don't keep this coin collector waiting too long. I want that coin.” — **effects:** sets stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47)


    <span id="d-forenza_waytobrimhaven3-coin_collector_thief_coins_45"></span>**`coin_collector_thief_coins_45`** Forenza: “The silver pieces depict a mighty ship sailing under the moonlit sky, capturing the essence of the Ocean Nomads' freedom and unity. Legends speak of these coins being crafted during the tribe's grand gatherings, where sailors from various…”

    - “So they are priceless?” → [coin_collector_thief_coins_50](#d-forenza_waytobrimhaven3-coin_collector_thief_coins_50)

    <span id="d-forenza_waytobrimhaven3-korhald_chest_examine_50"></span>**`korhald_chest_examine_50`** Forenza: “Here, take the map and the pendant. If you need me, I'll be here for a little bit longer.” — **effects:** gives 1× [Mysterious Korhald map](../items/korhald_map.md), sets stage 60 of [The odd coin collector](../quests/odd_coin_collector.md#stage-60), gives 1× [Mysterious Korhald pendant](../items/korhald_chamber_key.md), sets stage 44 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-44), sets stage 45 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-45), sets stage 48 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-48)


    <span id="d-forenza_waytobrimhaven3-coin_collector_thief_coins_50"></span>**`coin_collector_thief_coins_50`** Forenza: “[The collector pauses, his gaze lingering on the coins.] These pieces are not merely currency; they are artifacts of a hidden past, a glimpse into the underground world where alliances were forged in secrecy. I'd be willing to make you an…”

    - “So you want to buy them all?” → [coin_collector_thief_coins_55](#d-forenza_waytobrimhaven3-coin_collector_thief_coins_55)

    <span id="d-forenza_waytobrimhaven3-coin_collector_thief_coins_55"></span>**`coin_collector_thief_coins_55`** Forenza: “Well, yes. But not all of them. Afterall, who needs 110 of these?”

    - “OK, so what do you want to buy?” → [coin_collector_thief_coins_60](#d-forenza_waytobrimhaven3-coin_collector_thief_coins_60)

    <span id="d-forenza_waytobrimhaven3-coin_collector_thief_coins_60"></span>**`coin_collector_thief_coins_60`** Forenza: “Well, let's talk price first. You see, the silver coin is worth 11 gold in weight and the bronze is worth 5 gold in weight. But, to a collector they are worth more. Let's make this simple. I will pay you double those values for each coin…”

    - “So how much total than?” → [coin_collector_thief_coins_65](#d-forenza_waytobrimhaven3-coin_collector_thief_coins_65)

    <span id="d-forenza_waytobrimhaven3-coin_collector_thief_coins_65"></span>**`coin_collector_thief_coins_65`** Forenza: “110 gold for the silver and 50 for the bronze coins.”

    - “That little? No, thanks” → *conversation ends*
    - “Well, something is better than nothing.” *(if hand over 5× [Silver coin](../items/silver_coin.md); hand over 5× [Bronze coin](../items/bronze_coin.md))* → [coin_collector_thief_coins_70](#d-forenza_waytobrimhaven3-coin_collector_thief_coins_70)

    <span id="d-forenza_waytobrimhaven3-coin_collector_thief_coins_70"></span>**`coin_collector_thief_coins_70`** Forenza: “Thank you so much.” — **effects:** gives 160× [Gold coins](../items/gold.md), sets stage 107 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-107)




### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 31 lines added |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 4 lines added, 4 lines changed<br>· text: “[The collector pauses, his gaze lingering on the coins.] These pieces…” → “[The collector pauses, his gaze lingering on the coins.] These pieces…”<br>· text: “Well, for obvious reasons. Didn't you notice that the shield has the …” → “Well, for obvious reasons. Didn't you notice that the shield has the …” |
| [v0.8.13](../versions/0.8.13.md) | Dialogue: 1 line changed<br>· text: “These bronze pieces bear the mark of the Lunar Whispe, an infamous th…” → “These bronze pieces bear the mark of the Lunar Whisper, an infamous t…” |
| [v0.8.16.1](../versions/0.8.16.1.md) | Dialogue: 1 line added, 1 line changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 4 lines changed<br>· text: “[While laughing] Now, now, who do you think I am, Gylew? I don't have…” → “[While laughing] Now, now, who do you think I am, Gylew? I don't have…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (forenza_waytobrimhaven3)"

    | | |
    |---|---|
    | Entry ID | `forenza_waytobrimhaven3` |
    | Spawn group | `forenza_waytobrimhaven3` |
    | Loot table | – |
    | Conversation | `forenza_waytobrimhaven3_initial_phrase` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_tometik1:86` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "forenza_waytobrimhaven3",
     "name": "Forenza",
     "iconID": "monsters_tometik1:86",
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "spawnGroup": "forenza_waytobrimhaven3",
     "phraseID": "forenza_waytobrimhaven3_initial_phrase"
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forenza.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forenza.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forenza.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forenza.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
