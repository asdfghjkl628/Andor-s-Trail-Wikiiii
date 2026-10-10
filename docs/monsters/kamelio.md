---
description: "Kamelio is an NPC you can also fight in Andor's Trail, found in Elm 5f 2."
---

# ![](../assets/icons/monsters/monsters_tometik1_2.png){ .sprite } Kamelio

**Where to find Kamelio:** [Elm 5f 2](../maps/elm5f_2.md#pin-npc-kamelio)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik1_2.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Elm 5f 2 |
| **Class** | Demon |
| **HP** | 177 |
| **XP when defeated** | 602 |
| **Immune to crits** | Yes |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

!!! warning "You can fight Kamelio"
    The conversation can lead straight into a fight with Kamelio.

    Answering “For the shadow!” during [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-37) starts a fight with Kamelio.

    Answering “Betrayer, die!” during [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-37) starts a fight with Kamelio.

    Answering “OK, you're completely out of your mind.” during [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-37) starts a fight with Kamelio.

    Answering “Oh? Let's see if you can stand a single blow!” during [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-37) starts a fight with Kamelio.

## Combat

| | |
|---|---|
| Class | Demon |
| HP | 177 |
| XP when defeated | 602 |
| Damage | 17 to 20 |
| AC | 171 |
| BC | 123 |
| DR | 12 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | none |

**Immune to critical hits.**

**Its hits:** Heal HP: 1 to 4; On target: [Vulnerability](../conditions/vulnerability.md) (magnitude 7, 2 rounds, 10% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 1 to 99 |
| [Large bottle of mountain water](../items/bwm_water2.md) | 100% | 1 to 5 |
| [Spiked Gloves](../items/gauntlet_omi2_1.md) | 100% | 1 |
| [Ruby gem](../items/gem2.md) | 20% | 1 to 100 |

## Quests that count defeats

- A conversation with [General Ortholion](../monsters/ortholion.md) ([Blackwater mountain 29](../maps/blackwater_mountain29.md)), walking into a blocked passage on [Elm 5f 2](../maps/elm5f_2.md) checks that this enemy has been defeated.
- [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-38) with stepping on a trigger on [Elm 5f 2](../maps/elm5f_2.md) checks that this enemy has been defeated.

## Quests

- [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md): stage 37

## Dialogue simulator

Set your quest stages and items, then talk to Kamelio. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/kamelio_s.json" data-npc="Kamelio" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (12 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-kamelio_s"></span>**`kamelio_s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 37 of [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-37))* → *fight starts*
    - branch 2 → [kamelio_1](#d-kamelio_1)

    <span id="d-kamelio_1"></span>**`kamelio_1`** Kamelio: “Hello, unfortunate soul. I'm Kamelio.”

    - “Kamelio? You are one of those missing people from Prim!” → [kamelio_2a](#d-kamelio_2a)
    - “Jern will be glad you're alright.” *(if reached stage 23 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-23))* → [kamelio_2b](#d-kamelio_2b)
    - “I need your help! There's a man lying unconscious there.” → [kamelio_2c](#d-kamelio_2c)

    <span id="d-kamelio_2a"></span>**`kamelio_2a`** Kamelio: “Yes. Lorn, Duala and me were caught and tortured. Lorn... He spat everything out like the coward he was.”

    - “Who tortured you?” → [kamelio_3a](#d-kamelio_3a)
    - “What did he say?” → [kamelio_3c](#d-kamelio_3c)

    <span id="d-kamelio_2b"></span>**`kamelio_2b`** Kamelio: “Alright? My body has not seen better days. But that drunkard will never get to know it.”

    - Next → [kamelio_3b](#d-kamelio_3b)

    <span id="d-kamelio_2c"></span>**`kamelio_2c`** Kamelio: “Ah...Yes. Don't worry, you go first. *approaches you*” — **effects:** sets stage 37 of [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-37), spawns monsters on elm5f_2, spawns monsters on elm5f_2

    - “For the shadow!” → *fight starts*
    - “Wh...What?” → *fight starts*
    - “Don't beg me later.” → *fight starts*

    <span id="d-kamelio_3a"></span>**`kamelio_3a`** Kamelio: “That guy you were talking to before.”

    - “Ehrenfest! What has he done to you?!” → [kamelio_4a](#d-kamelio_4a)
    - “What did Lorn tell him?” → [kamelio_3c](#d-kamelio_3c)

    <span id="d-kamelio_3c"></span>**`kamelio_3c`** Kamelio: “Everything. From where the shrine was to how to enter and pass through the pitch black tunnels.”

    - “Who tortured you?” → [kamelio_3a](#d-kamelio_3a)
    - “How did you escape?” → [kamelio_4b](#d-kamelio_4b)

    <span id="d-kamelio_3b"></span>**`kamelio_3b`** Kamelio: “*approaching you* He's not going to see you alive again.” — **effects:** sets stage 37 of [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-37), spawns monsters on elm5f_2, spawns monsters on elm5f_2

    - “Betrayer, die!” → *fight starts*
    - “For the shadow!” → *fight starts*
    - “Wanna bet, weakling?” → *fight starts*

    <span id="d-kamelio_4a"></span>**`kamelio_4a`** Kamelio: “He just wanted to know an old shrine's location. And I forgive him everything. He came back and freed Duala and me and gave us food and a marvelous elixir he called a "recovery potion". Now my body is reborn and my mind is set free. I…”

    - “Hmm, yeah sure. Goodbye.” → [kamelio_5a](#d-kamelio_5a)
    - “What do you have to do?” → [kamelio_5b](#d-kamelio_5b)

    <span id="d-kamelio_4b"></span>**`kamelio_4b`** Kamelio: “Escape? When the torturer came back, he behaved totally different. He freed us and brought us some food and recovery potions. Since then, I feel like I have been reborn! All my injuries were cured, and my mind was set free. Now I know the…”

    - “You're starting to sound very weird. I'd better leave and seek help,” → [kamelio_5a](#d-kamelio_5a)
    - “What must you do?” → [kamelio_5b](#d-kamelio_5b)

    <span id="d-kamelio_5a"></span>**`kamelio_5a`** Kamelio: “Not so fast. My mind is clear, you need to die now along with that Feygard scum.” — **effects:** sets stage 37 of [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-37), spawns monsters on elm5f_2, spawns monsters on elm5f_2

    - “Oh? Let's see if you can stand a single blow!” → *fight starts*
    - “This hatred against Feygard is injuring you; I'll be your cure.” → *fight starts*
    - “For Feygard!!” → *fight starts*

    <span id="d-kamelio_5b"></span>**`kamelio_5b`** Kamelio: “Kill you first, then kill the guy over there. That's it.” — **effects:** sets stage 37 of [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-37), spawns monsters on elm5f_2, spawns monsters on elm5f_2

    - “OK, you're completely out of your mind.” → *fight starts*
    - “Kill me? How dare you. Die!” → *fight starts*
    - “Bad idea. For the Shadow!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added<br>Dialogue: 12 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `kamelio` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `kamelio` |
    | Loot table | `kamelio` |
    | Conversation | `kamelio_s` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_tometik1:2` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "kamelio",
     "name": "Kamelio",
     "iconID": "monsters_tometik1:2",
     "maxHP": 177,
     "moveCost": 2,
     "unique": 1,
     "monsterClass": "demon",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 17,
      "max": 20
     },
     "spawnGroup": "kamelio",
     "phraseID": "kamelio_s",
     "droplistID": "kamelio",
     "attackCost": 3,
     "attackChance": 171,
     "criticalSkill": 0,
     "criticalMultiplier": 0.0,
     "blockChance": 123,
     "damageResistance": 12,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 1,
       "max": 4
      },
      "conditionsTarget": [
       {
        "condition": "vulnerability",
        "magnitude": 7,
        "duration": 2,
        "chance": "10"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kamelio.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kamelio.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kamelio.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kamelio.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
