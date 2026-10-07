# ![](../assets/icons/monsters/monsters_tometik5_87.png){ .sprite } Tiqui

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik5_87.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `tiqui` |
| **Type** | NPC |
| **Class** | ? |
| **HP** | 145 |
| **XP when killed** | 306 |
| **Found in** | lodar14 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 145 |
| Damage | 0 to 9 |
| Attack chance | 90 |
| Block chance | 120 |
| Damage resistance | 9 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Tiqui's shield](../items/tiqui.md) | 100% | 1 |
| [Olwyn's curse](../items/hmr_olwyns.md) | 100% | 1 |
| [Gold coins](../items/gold.md) | 100% | 50 to 150 |
| [Polished ring](../items/ring2.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [lodar14](../maps/lodar14.md) | – | 1 | – |


## Quests

- [No rest for the guilty](../quests/lodar13_rest.md): stages 20, 22, 24, 30, 41, 60, 65

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Tiqui. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/tiqui.json" data-npc="Tiqui" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (25 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-tiqui"></span>**`tiqui`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 30 of [No rest for the guilty](../quests/lodar13_rest.md#stage-30))* → [tiqui_atk](#d-tiqui_atk)
    - branch 2 *(if reached stage 60 of [No rest for the guilty](../quests/lodar13_rest.md#stage-60))* → [tiqui_wb0](#d-tiqui_wb0)
    - branch 3 *(if reached stage 41 of [No rest for the guilty](../quests/lodar13_rest.md#stage-41))* → [tiqui_r1](#d-tiqui_r1)
    - branch 4 *(if reached stage 22 of [No rest for the guilty](../quests/lodar13_rest.md#stage-22))* → [tiqui_r0](#d-tiqui_r0)
    - branch 5 → [tiqui0](#d-tiqui0)

    <span id="d-tiqui_atk"></span>**`tiqui_atk`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 31 of [No rest for the guilty](../quests/lodar13_rest.md#stage-31))* → [tiqui_atk1](#d-tiqui_atk1)
    - branch 2 → [tiqui_atk0](#d-tiqui_atk0)

    <span id="d-tiqui_wb0"></span>**`tiqui_wb0`** Tiqui: “My helping friend! Thank you, thank you!”

    - Next → [tiqui_r2](#d-tiqui_r2)

    <span id="d-tiqui_r1"></span>**`tiqui_r1`** Tiqui: “Yes! Yes! The smell is gone. You friend of Tiqui now! Tiqui help you when we meet again!” — **effects:** sets stage 41 of [No rest for the guilty](../quests/lodar13_rest.md#stage-41)

    - Next → [tiqui_r2](#d-tiqui_r2)

    <span id="d-tiqui_r0"></span>**`tiqui_r0`** Tiqui: “Hello, friend of Tiqui. Can Tiqui have revenge for friends?”

    - “I won't listen to any more of your lies. You'll die now!” → [tiqui_atk](#d-tiqui_atk)
    - “Can you tell me your story again?” → [tiqui3](#d-tiqui3)
    - “I've dealt with Aulowenn for you.” *(if hand over 1× [Aulowenn's signet ring](../items/aulowenn.md))* → [tiqui_r1](#d-tiqui_r1)

    <span id="d-tiqui0"></span>**`tiqui0`** Tiqui: “You not belong here. You leave now.”

    - “I am sent here by Aulowenn to take care of you.” *(if reached stage 11 of [No rest for the guilty](../quests/lodar13_rest.md#stage-11))* → [tiqui1](#d-tiqui1)

    <span id="d-tiqui_atk1"></span>**`tiqui_atk1`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 65 of [No rest for the guilty](../quests/lodar13_rest.md#stage-65)

    - branch 1 → [tiqui_atk0](#d-tiqui_atk0)

    <span id="d-tiqui_atk0"></span>**`tiqui_atk0`** Tiqui: “No, you die now! You one of them! Tiqui angry!” — **effects:** sets stage 24 of [No rest for the guilty](../quests/lodar13_rest.md#stage-24), sets stage 30 of [No rest for the guilty](../quests/lodar13_rest.md#stage-30)

    - “Attack!” → *fight starts*
    - “Sorry, I wasn't listening since I was so distracted by your hideous appearance and your foul smell. Here, let me fix…” → *fight starts*

    <span id="d-tiqui_r2"></span>**`tiqui_r2`** Tiqui: “You also use bed of smelly men, and Tiqui keep you safe.” — **effects:** sets stage 60 of [No rest for the guilty](../quests/lodar13_rest.md#stage-60)

    - “Thank you. I'll feel much safer now that I know you'll watch over me when I rest in Aulowenn's old bed.” → [tiqui_r3](#d-tiqui_r3)

    <span id="d-tiqui3"></span>**`tiqui3`** Tiqui: “You can smell them from far away even. We sense something bad would happen when we first noticed them.”

    - Next → [tiqui4](#d-tiqui4)

    <span id="d-tiqui1"></span>**`tiqui1`** Tiqui: “Tiqui not want fight. Tiqui angry that men who smell bad kill his friends.” — **effects:** sets stage 20 of [No rest for the guilty](../quests/lodar13_rest.md#stage-20)

    - “I won't listen to any of your lies. You'll die now!” → [tiqui_atk](#d-tiqui_atk)
    - “They killed your friends?” → [tiqui2](#d-tiqui2)

    <span id="d-tiqui_r3"></span>**`tiqui_r3`** Tiqui: “You good friend of Tiqui!”


    <span id="d-tiqui4"></span>**`tiqui4`** Tiqui: “First we try stay away from them. They notice us, but we stay away. They trespass deeper.”

    - Next → [tiqui5](#d-tiqui5)

    <span id="d-tiqui2"></span>**`tiqui2`** Tiqui: “They did. Men who smell bad do not belong here. Everything quiet before they came.”

    - “I won't listen to any of your lies. You'll die now!” → [tiqui_atk](#d-tiqui_atk)
    - “I'll listen to your story.” → [tiqui3](#d-tiqui3)

    <span id="d-tiqui5"></span>**`tiqui5`** Tiqui: “One smelly man walked into snake trap. Snake trap not meant for smelly man.”

    - Next → [tiqui6](#d-tiqui6)

    <span id="d-tiqui6"></span>**`tiqui6`** Tiqui: “Other smelly men angry at snake trap. Tiqui not understand. Smelly men should be angry at stupid man who walk into snake trap.”

    - Next → [tiqui7](#d-tiqui7)

    <span id="d-tiqui7"></span>**`tiqui7`** Tiqui: “After, smelly men angry at us. Hunt us. Kill us.”

    - Next → [tiqui8](#d-tiqui8)

    <span id="d-tiqui8"></span>**`tiqui8`** Tiqui: “Much fight. Much blood on ground. But blood good for trees.”

    - Next → [tiqui9](#d-tiqui9)

    <span id="d-tiqui9"></span>**`tiqui9`** Tiqui: “Tiqui head of clan. Tiqui make decision of revenge.”

    - Next → [tiqui10](#d-tiqui10)

    <span id="d-tiqui10"></span>**`tiqui10`** Tiqui: “Smelly men hunt us down. Kill many.”

    - “The smelly men you speak of must be the guards from Feygard. They've been killing you off?” → [tiqui11](#d-tiqui11)
    - “I won't listen to any more of your lies. You'll die now!” → [tiqui_atk](#d-tiqui_atk)

    <span id="d-tiqui11"></span>**`tiqui11`** Tiqui: “Yes. Smelly men kill us when they see us.”

    - “I won't listen to any more of your lies. You'll die now!” → [tiqui_atk](#d-tiqui_atk)
    - “What can I do to help?” → [tiqui12](#d-tiqui12)

    <span id="d-tiqui12"></span>**`tiqui12`** Tiqui: “You help Tiqui? Tiqui want revenge for dead friends.”

    - Next → [tiqui13](#d-tiqui13)

    <span id="d-tiqui13"></span>**`tiqui13`** Tiqui: “Tiqui knows smelly person with crates [points in the direction to where Aulowenn is].”

    - Next → [tiqui14](#d-tiqui14)

    <span id="d-tiqui14"></span>**`tiqui14`** Tiqui: “You go take care of last smelly person. Tiqui can be friend to you. Tiqui can have revenge.” — **effects:** sets stage 22 of [No rest for the guilty](../quests/lodar13_rest.md#stage-22)

    - “I won't listen to any more of your lies. You'll die now!” → [tiqui_atk](#d-tiqui_atk)
    - “I will gladly kill more of those Feygard scum.” → [tiqui15](#d-tiqui15)
    - “No, I think I'll find your village and take whatever riches you have instead.” → [tiqui_atk](#d-tiqui_atk)
    - “OK. I will help you.” → [tiqui15](#d-tiqui15)
    - “It sounds like they have been wrongfully killing you. I will help you.” → [tiqui15](#d-tiqui15)

    <span id="d-tiqui15"></span>**`tiqui15`** Tiqui: “You friend of Tiqui.”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 6 lines changed<br>· text: “Tiqui not want fight. Tiqui angry that men who smell bad kill his fri…” → “Tiqui not want fight. Tiqui angry that men who smell bad kill his fri…”<br>· text: “Tiqui knows smelly person with crates. [points in the direction to wh…” → “Tiqui knows smelly person with crates [points in the direction to whe…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tiqui.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tiqui.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tiqui.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tiqui.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `tiqui` |
    | Spawn group | `tiqui` |
    | Loot table | `tiqui` |
    | Conversation | `tiqui` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik5:87` |
    | Defined in | `res/raw/monsterlist_v070_npcs.json` |

    Raw data:

    ```json
    {
     "id": "tiqui",
     "name": "Tiqui",
     "iconID": "monsters_tometik5:87",
     "maxHP": 145,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "attackDamage": {
      "min": 0,
      "max": 9
     },
     "phraseID": "tiqui",
     "droplistID": "tiqui",
     "attackCost": 3,
     "attackChance": 90,
     "blockChance": 120,
     "damageResistance": 9
    }
    ```


<small>Data from v0.8.18</small>
