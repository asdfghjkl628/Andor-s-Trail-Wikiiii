# ![](../assets/icons/monsters/monsters_mage_0.png){ .sprite } Jhaeld

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_mage_0.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `lae_jhaeld3` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 200 |
| **XP when killed** | 258 |
| **Found in** | final_cave2 |
| **Introduced** | [v0.8.11](../versions/0.8.11.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 200 |
| Damage | 10 to 22 |
| Attack chance | 70 |
| Block chance | 50 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 4 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Scroll of fire](../items/final_cave_f.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [final_cave2](../maps/final_cave2.md) | – | 1 | appears later in a quest |


## Quests

- [Not Pony Island](../quests/lae_centaurs.md): stages 200

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Jhaeld. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_algangror3.json" data-npc="Jhaeld" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (15 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-lae_algangror3"></span>**`lae_algangror3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if killed 1× [Dorhantarh](../monsters/lae_island_boss.md))* → [lae_algangror3_100](#d-lae_algangror3_100)
    - branch 2 *(if reached stage 200 of [Not Pony Island](../quests/lae_centaurs.md#stage-200))* → [lae_algangror3_40](#d-lae_algangror3_40)
    - branch 3 → [lae_algangror3_10](#d-lae_algangror3_10)

    <span id="d-lae_algangror3_100"></span>**`lae_algangror3_100`** Jhaeld: “NO! What have you done to our master?!”

    - “The same that I'll do to you now.” → *fight starts*

    <span id="d-lae_algangror3_40"></span>**`lae_algangror3_40`** Jhaeld: “Now go ahead, you'll be a tasty dinner for our master Dorhantarh tonight.” — **effects:** sets stage 200 of [Not Pony Island](../quests/lae_centaurs.md#stage-200)

    - Next → [lae_algangror3_42](#d-lae_algangror3_42)

    <span id="d-lae_algangror3_10"></span>**`lae_algangror3_10`** Jhaeld: “Surprised to see me here?”

    - Next → [lae_algangror3_12](#d-lae_algangror3_12)

    <span id="d-lae_algangror3_42"></span>**`lae_algangror3_42`** Jhaeld: “You're so speechless. Hahaha! Go now.”

    - “Well wait - attack!” → [lae_algangror3_50](#d-lae_algangror3_50)

    <span id="d-lae_algangror3_12"></span>**`lae_algangror3_12`** Jhaeld: “You should see your face! Hahaha!”

    - Next → [lae_algangror3_20](#d-lae_algangror3_20)

    <span id="d-lae_algangror3_50"></span>**`lae_algangror3_50`** Jhaeld: “No no no. It is not proper to draw a weapon in the presence of our Master.”


    <span id="d-lae_algangror3_20"></span>**`lae_algangror3_20`** Jhaeld: “Of course we are not what you think you see. Ever heard of posers? You were great, that was really fun.”

    - Next → [lae_algangror3_22](#d-lae_algangror3_22)

    <span id="d-lae_algangror3_22"></span>**`lae_algangror3_22`** Jhaeld: “Even the many gold is all fake. We had a lot of fun decorating this ugly room as a treasure trove.”

    - Next → [lae_algangror3_24](#d-lae_algangror3_24)

    <span id="d-lae_algangror3_24"></span>**`lae_algangror3_24`** Jhaeld: “Making rocks look like piles of gold and stuff like that.”

    - “And the walls? The element scrolls and the globes?” → [lae_algangror3_26](#d-lae_algangror3_26)

    <span id="d-lae_algangror3_26"></span>**`lae_algangror3_26`** Jhaeld: “The point of all this was just to lure you down here to our master Dorhantarh without you becoming suspicious.”

    - Next → [lae_algangror3_28](#d-lae_algangror3_28)

    <span id="d-lae_algangror3_28"></span>**`lae_algangror3_28`** Jhaeld: “So it couldn't be too easy for you. That's why I came up with the idea of the scrolls and glass balls.”

    - “Does that mean this complex mechanism doesn't work at all?” → [lae_algangror3_30](#d-lae_algangror3_30)

    <span id="d-lae_algangror3_30"></span>**`lae_algangror3_30`** Jhaeld: “Oh yes, of course it works. Why do you think the wall closed again?”

    - “Yes, why did it?” → [lae_algangror3_32](#d-lae_algangror3_32)

    <span id="d-lae_algangror3_32"></span>**`lae_algangror3_32`** Jhaeld: “Well, because I brought a scroll from the table here with me. That's why.”

    - “What?! You ...” → [lae_algangror3_34](#d-lae_algangror3_34)

    <span id="d-lae_algangror3_34"></span>**`lae_algangror3_34`** Jhaeld: “Hahaha!”

    - Next → [lae_algangror3_40](#d-lae_algangror3_40)



## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 15 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_jhaeld3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_jhaeld3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_jhaeld3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_jhaeld3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `lae_jhaeld3` |
    | Spawn group | `lae_jhaeld3` |
    | Loot table | `lae_algangror3` |
    | Conversation | `lae_algangror3` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_mage:0` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_jhaeld3",
     "name": "Jhaeld",
     "iconID": "monsters_mage:0",
     "maxHP": 200,
     "moveCost": 4,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 10,
      "max": 22
     },
     "spawnGroup": "lae_jhaeld3",
     "phraseID": "lae_algangror3",
     "droplistID": "lae_algangror3",
     "attackCost": 4,
     "attackChance": 70,
     "blockChance": 50
    }
    ```


<small>Data from v0.8.18</small>
