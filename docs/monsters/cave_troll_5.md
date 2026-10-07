---
description: "Cave troll leader is an NPC who can also be fought in Andor's Trail, found in lakecave2."
---

# ![](../assets/icons/monsters/monsters_tometik5_18.png){ .sprite } Cave troll leader

**Where to find Cave troll leader:** [lakecave2](../maps/lakecave2.md#pin-npc-cave_troll_5)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik5_18.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | lakecave2 |
| **Class** | Giant |
| **HP** | 410 |
| **XP when defeated** | 518 |
| **Entry ID** | `cave_troll_5` |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Giant |
| HP | 410 |
| XP when defeated | 518 |
| Damage | 5 to 20 |
| Attack chance | 70 |
| Block chance | 50 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

**On hit:** On self: Stunned (magnitude 1, 3 rounds, 25% chance); On target: Stunned (magnitude 1, 3 rounds, 25% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 4 to 12 |
| [Sword of the annihilator](../items/sword_annihilator.md) | 100% | 1 |
| [Ruby gem](../items/gem2.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [lakecave2](../maps/lakecave2.md) | – | 1 | – |

## Quests

- [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md): stage 203

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Cave troll leader. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/lakecave2_troll_10.json" data-npc="Cave troll leader" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (15 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-lakecave2_troll_10"></span>**`lakecave2_troll_10`** Cave troll leader: “You! You have no business here! Get out of my cave!”

    - “Of course, sorry, please excuse the disturbance.” → *conversation ends*
    - “May I ask a question before I leave?” → [lakecave2_troll_12](#d-lakecave2_troll_12)

    <span id="d-lakecave2_troll_12"></span>**`lakecave2_troll_12`** Cave troll leader: “That was already a question! Hahaha! You are lucky that I am in good mood - and not hungry at the moment.”

    - Next → [lakecave2_troll_14](#d-lakecave2_troll_14)

    <span id="d-lakecave2_troll_14"></span>**`lakecave2_troll_14`** Cave troll leader: “What do you want?”

    - “I am looking for my brother Andor. Have you seen him?” → [lakecave2_troll_20](#d-lakecave2_troll_20)
    - “I am looking for some flowers called damerilias.” *(if reached stage 10 of [The roots of love](../quests/roots_love.md#stage-10))* → [lakecave2_troll_30](#d-lakecave2_troll_30)
    - “Someone lost a key here. Once I have found the key, you can have your wet, dark hole to yourself again.” *(if reached stage 10 of [A secret garden](../quests/secret_garden.md#stage-10); NOT reached stage 20 of [A secret garden](../quests/secret_garden.md#stage-20))* → [lakecave2_troll_40](#d-lakecave2_troll_40)
    - “I will leave now.” → *conversation ends*

    <span id="d-lakecave2_troll_20"></span>**`lakecave2_troll_20`** Cave troll leader: “No. If your brother looks like you then I have never seen him, and if I had then I would have eaten him! Now go!”

    - “I have another question.” → [lakecave2_troll_14](#d-lakecave2_troll_14)

    <span id="d-lakecave2_troll_30"></span>**`lakecave2_troll_30`** Cave troll leader: “Everyone is after my damerilias! For what? Such ugly, stinking things! No, I won't give you a single one. And you really should leave now, before I get hungry!”

    - “What do you need damerilias for, if you don't like them?” → [lakecave2_troll_32](#d-lakecave2_troll_32)

    <span id="d-lakecave2_troll_40"></span>**`lakecave2_troll_40`** Cave troll leader: “What do you know about the key? I keep the key safe. Are you associated with that thief who comes once a year and steals my damerilias?”

    - “Do you mean Noraed? He is dead.” → [lakecave2_troll_50](#d-lakecave2_troll_50)

    <span id="d-lakecave2_troll_32"></span>**`lakecave2_troll_32`** Cave troll leader: “The damerilias attract food for me; tasty, delicate, little people. Catching them is kind of a sport for me. It makes eating more fun.”

    - Next → [lakecave2_troll_34](#d-lakecave2_troll_34)

    <span id="d-lakecave2_troll_50"></span>**`lakecave2_troll_50`** Cave troll leader: “Dead? No - what a pity! I am really sorry. What a loss.”

    - Next → [lakecave2_troll_52](#d-lakecave2_troll_52)

    <span id="d-lakecave2_troll_34"></span>**`lakecave2_troll_34`** Cave troll leader: “But talking about food with a troll is not the smartest idea...”

    - “Right. I have another question.” → [lakecave2_troll_14](#d-lakecave2_troll_14)

    <span id="d-lakecave2_troll_52"></span>**`lakecave2_troll_52`** Cave troll leader: “I was so looking forward to eating him.”

    - “I would like to take some damerilias for his grave.” → [lakecave2_troll_60](#d-lakecave2_troll_60)

    <span id="d-lakecave2_troll_60"></span>**`lakecave2_troll_60`** Cave troll leader: “Forget it. Especially because you know those people who built that terrible statue near the entrance.”

    - “What is terrible about that statue?” → [lakecave2_troll_62](#d-lakecave2_troll_62)

    <span id="d-lakecave2_troll_62"></span>**`lakecave2_troll_62`** Cave troll leader: “It is a bane for all trolls. We avoid going past, or even near, her.”

    - Next → [lakecave2_troll_64](#d-lakecave2_troll_64)

    <span id="d-lakecave2_troll_64"></span>**`lakecave2_troll_64`** Cave troll leader: “I might let you go if you remove that ghastly statue. Maybe I'll even give you two of those ugly plants for that. Agreed?”

    - “[Lie] Agreed. Bring the Damerilias first.” → [lakecave2_troll_70](#d-lakecave2_troll_70)
    - “No. That statue is a blessing for the people here. Even if I could, I would not tear it down.” → [lakecave2_troll_90](#d-lakecave2_troll_90)

    <span id="d-lakecave2_troll_70"></span>**`lakecave2_troll_70`** Cave troll leader: “You lie. You think I am just a stupid troll.”

    - “Of course you are.” → [lakecave2_troll_90](#d-lakecave2_troll_90)
    - “It was worth a try.” → [lakecave2_troll_90](#d-lakecave2_troll_90)

    <span id="d-lakecave2_troll_90"></span>**`lakecave2_troll_90`** Cave troll leader: “Outrageous! I will put you in my pantry now.” — **effects:** sets stage 203 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-203)

    - “We'll see.” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 15 lines added |
| [v0.7.9](../versions/0.7.9.md) | hitEffect: {"conditionsSource": [{"chance": "25", … → {"conditionsSource": [{"chance": "25", … |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `cave_troll_5` |
    | Spawn group | `cave_troll_5` |
    | Loot table | `cave_troll_4` |
    | Conversation | `lakecave2_troll_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik5:18` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "cave_troll_5",
     "name": "Cave troll leader",
     "iconID": "monsters_tometik5:18",
     "maxHP": 410,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "giant",
     "attackDamage": {
      "min": 5,
      "max": 20
     },
     "spawnGroup": "cave_troll_5",
     "phraseID": "lakecave2_troll_10",
     "droplistID": "cave_troll_4",
     "attackCost": 5,
     "attackChance": 70,
     "blockChance": 50,
     "hitEffect": {
      "conditionsSource": [
       {
        "condition": "stunned",
        "magnitude": 1,
        "duration": 3,
        "chance": "25"
       }
      ],
      "conditionsTarget": [
       {
        "condition": "stunned",
        "magnitude": 1,
        "duration": 3,
        "chance": "25"
       }
      ]
     }
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cave_troll_5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cave_troll_5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cave_troll_5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cave_troll_5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
