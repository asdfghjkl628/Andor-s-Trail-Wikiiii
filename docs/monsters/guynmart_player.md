# ![](../assets/icons/monsters/monsters_ld1_0.png){ .sprite } Guynmart guard

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_0.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `guynmart_player` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Guynmart Castle |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

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


## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [guynmart](../maps/guynmart.md) | Guynmart Castle | 2 | – |


## Quests

- [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md): stages 1, 2
- [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md): stages 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Guynmart guard. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_player_10.json" data-npc="Guynmart guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (28 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guynmart_player_10"></span>**`guynmart_player_10`** Guynmart guard: “Hi kid! Would you like to play a card game?”

    - “Sure!” → [guynmart_player_20](#d-guynmart_player_20)
    - “No, not today!” → *conversation ends*
    - “No thanks. My father warned me that certain card games can become a bad habit.” → *conversation ends*

    <span id="d-guynmart_player_20"></span>**`guynmart_player_20`** Guynmart guard: “We always play card color guessing. Do you have any money?”

    - “Of course I have.” *(if have 100 gold)* → [guynmart_player_80](#d-guynmart_player_80)
    - “I would never play for money.” → *conversation ends*
    - “Please explain the rules to me.” → [guynmart_player_30](#d-guynmart_player_30)

    <span id="d-guynmart_player_80"></span>**`guynmart_player_80`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if have 100 gold)* → [guynmart_player_80_2](#d-guynmart_player_80_2)
    - branch 2 → [guynmart_player_80_1](#d-guynmart_player_80_1)

    <span id="d-guynmart_player_30"></span>**`guynmart_player_30`** Guynmart guard: “I will draw a card, and you have to guess whether it is Red or Black.”

    - Next → [guynmart_player_32](#d-guynmart_player_32)

    <span id="d-guynmart_player_80_2"></span>**`guynmart_player_80_2`** Guynmart guard: “OK. I have drawn a card. Which color is it?”

    - “Red” → [guynmart_player_84](#d-guynmart_player_84)
    - “Black” → [guynmart_player_86](#d-guynmart_player_86)
    - “Blue” *(if reached stage 1 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-1); reached stage 3 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-3))* → [guynmart_player_82](#d-guynmart_player_82)
    - “Blue” *(if reached stage 2 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-2); reached stage 7 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-7))* → [guynmart_player_82](#d-guynmart_player_82)

    <span id="d-guynmart_player_80_1"></span>**`guynmart_player_80_1`** Guynmart guard: “Hey, you look like you have no money left.”

    - “Yes indeed, I'm broke. Sorry, then I have to leave.” → *conversation ends*

    <span id="d-guynmart_player_32"></span>**`guynmart_player_32`** Guynmart guard: “If you get it right, I will give you gold 100 coins. If your guess is wrong, you owe me 100.”

    - “OK, got it.” → [guynmart_player_80](#d-guynmart_player_80)
    - “Eh, could you explain once more?” → [guynmart_player_30](#d-guynmart_player_30)

    <span id="d-guynmart_player_84"></span>**`guynmart_player_84`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 1 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-1), clears stage 2 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-2)

    - branch 1 → [guynmart_player_90](#d-guynmart_player_90)

    <span id="d-guynmart_player_86"></span>**`guynmart_player_86`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 2 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-2), clears stage 1 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-1)

    - branch 1 → [guynmart_player_90](#d-guynmart_player_90)

    <span id="d-guynmart_player_82"></span>**`guynmart_player_82`** Guynmart guard: “Oh dear. Just Red or Black. Please try to remember. *Sigh*”

    - “Yes. Sorry.” → [guynmart_player_80](#d-guynmart_player_80)

    <span id="d-guynmart_player_90"></span>**`guynmart_player_90`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 12 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-12))* → [guynmart_player_112](#d-guynmart_player_112)
    - branch 2 *(if reached stage 11 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-11))* → [guynmart_player_111](#d-guynmart_player_111)
    - branch 3 *(if reached stage 10 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-10))* → [guynmart_player_110](#d-guynmart_player_110)
    - branch 4 *(if reached stage 9 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-9))* → [guynmart_player_109](#d-guynmart_player_109)
    - branch 5 *(if reached stage 8 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-8))* → [guynmart_player_108](#d-guynmart_player_108)
    - branch 6 *(if reached stage 7 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-7))* → [guynmart_player_107](#d-guynmart_player_107)
    - branch 7 *(if reached stage 6 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-6))* → [guynmart_player_106](#d-guynmart_player_106)
    - branch 8 *(if reached stage 5 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-5))* → [guynmart_player_105](#d-guynmart_player_105)
    - branch 9 *(if reached stage 4 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-4))* → [guynmart_player_104](#d-guynmart_player_104)
    - branch 10 *(if reached stage 3 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-3))* → [guynmart_player_103](#d-guynmart_player_103)
    - branch 11 *(if reached stage 2 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-2))* → [guynmart_player_102](#d-guynmart_player_102)
    - branch 12 *(if reached stage 1 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-1))* → [guynmart_player_101](#d-guynmart_player_101)
    - branch 13 → [guynmart_player_100](#d-guynmart_player_100)

    <span id="d-guynmart_player_112"></span>**`guynmart_player_112`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 12 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-12), sets stage 1 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-1)

    - branch 1 *(if reached stage 1 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-1); pay -100 gold)* → [guynmart_player_161](#d-guynmart_player_161)
    - branch 2 *(if reached stage 2 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-2); pay -100 gold)* → [guynmart_player_162](#d-guynmart_player_162)

    <span id="d-guynmart_player_111"></span>**`guynmart_player_111`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 11 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-11), sets stage 12 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-12)

    - branch 1 *(if reached stage 1 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-1); pay 100 gold)* → [guynmart_player_151](#d-guynmart_player_151)
    - branch 2 *(if reached stage 2 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-2); pay 100 gold)* → [guynmart_player_152](#d-guynmart_player_152)

    <span id="d-guynmart_player_110"></span>**`guynmart_player_110`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 10 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-10), sets stage 11 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-11)

    - branch 1 *(if reached stage 1 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-1); pay 100 gold)* → [guynmart_player_151](#d-guynmart_player_151)
    - branch 2 *(if reached stage 2 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-2); pay 100 gold)* → [guynmart_player_152](#d-guynmart_player_152)

    <span id="d-guynmart_player_109"></span>**`guynmart_player_109`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 9 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-9), sets stage 10 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-10)

    - branch 1 *(if reached stage 1 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-1); pay -100 gold)* → [guynmart_player_161](#d-guynmart_player_161)
    - branch 2 *(if reached stage 2 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-2); pay -100 gold)* → [guynmart_player_162](#d-guynmart_player_162)

    <span id="d-guynmart_player_108"></span>**`guynmart_player_108`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 8 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-8), sets stage 9 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-9)

    - branch 1 *(if reached stage 1 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-1); pay -100 gold)* → [guynmart_player_161](#d-guynmart_player_161)
    - branch 2 *(if reached stage 2 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-2); pay -100 gold)* → [guynmart_player_162](#d-guynmart_player_162)

    <span id="d-guynmart_player_107"></span>**`guynmart_player_107`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 7 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-7), sets stage 8 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-8)

    - branch 1 *(if reached stage 1 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-1); pay 100 gold)* → [guynmart_player_151](#d-guynmart_player_151)
    - branch 2 *(if reached stage 2 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-2); pay 100 gold)* → [guynmart_player_152](#d-guynmart_player_152)

    <span id="d-guynmart_player_106"></span>**`guynmart_player_106`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 6 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-6), sets stage 7 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-7)

    - branch 1 *(if reached stage 1 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-1); pay 100 gold)* → [guynmart_player_151](#d-guynmart_player_151)
    - branch 2 *(if reached stage 2 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-2); pay 100 gold)* → [guynmart_player_152](#d-guynmart_player_152)

    <span id="d-guynmart_player_105"></span>**`guynmart_player_105`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 5 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-5), sets stage 6 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-6)

    - branch 1 *(if reached stage 1 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-1); pay -100 gold)* → [guynmart_player_161](#d-guynmart_player_161)
    - branch 2 *(if reached stage 2 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-2); pay -100 gold)* → [guynmart_player_162](#d-guynmart_player_162)

    <span id="d-guynmart_player_104"></span>**`guynmart_player_104`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 4 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-4), sets stage 5 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-5)

    - branch 1 *(if reached stage 1 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-1); pay 100 gold)* → [guynmart_player_151](#d-guynmart_player_151)
    - branch 2 *(if reached stage 2 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-2); pay 100 gold)* → [guynmart_player_152](#d-guynmart_player_152)

    <span id="d-guynmart_player_103"></span>**`guynmart_player_103`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 3 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-3), sets stage 4 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-4)

    - branch 1 *(if reached stage 1 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-1); pay -100 gold)* → [guynmart_player_161](#d-guynmart_player_161)
    - branch 2 *(if reached stage 2 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-2); pay -100 gold)* → [guynmart_player_162](#d-guynmart_player_162)

    <span id="d-guynmart_player_102"></span>**`guynmart_player_102`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 2 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-2), sets stage 3 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-3)

    - branch 1 *(if reached stage 1 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-1); pay 100 gold)* → [guynmart_player_151](#d-guynmart_player_151)
    - branch 2 *(if reached stage 2 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-2); pay 100 gold)* → [guynmart_player_152](#d-guynmart_player_152)

    <span id="d-guynmart_player_101"></span>**`guynmart_player_101`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 1 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-1), sets stage 2 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-2)

    - branch 1 *(if reached stage 1 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-1); pay 100 gold)* → [guynmart_player_151](#d-guynmart_player_151)
    - branch 2 *(if reached stage 2 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-2); pay 100 gold)* → [guynmart_player_152](#d-guynmart_player_152)

    <span id="d-guynmart_player_100"></span>**`guynmart_player_100`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 1 of [guynmart_q2 Step (hidden flag)](../quests/guynmart_q2.md#stage-1)

    - branch 1 *(if reached stage 1 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-1); pay -100 gold)* → [guynmart_player_161](#d-guynmart_player_161)
    - branch 2 *(if reached stage 2 of [guynmart_q1 (hidden flag)](../quests/guynmart_q1.md#stage-2); pay -100 gold)* → [guynmart_player_162](#d-guynmart_player_162)

    <span id="d-guynmart_player_161"></span>**`guynmart_player_161`** Guynmart guard: “Red! How did you know? Here you get 100 again. [Gold received] Can you do this again?”

    - Next → [guynmart_player_80](#d-guynmart_player_80)

    <span id="d-guynmart_player_162"></span>**`guynmart_player_162`** Guynmart guard: “Black! You guessed it right again. Here you get 100 gold. [Gold received] Let's try another card.”

    - Next → [guynmart_player_80](#d-guynmart_player_80)

    <span id="d-guynmart_player_151"></span>**`guynmart_player_151`** Guynmart guard: “I have Black! Sorry for you, kid. I get 100 now. [Gold taken] Let's try another card.”

    - Next → [guynmart_player_80](#d-guynmart_player_80)

    <span id="d-guynmart_player_152"></span>**`guynmart_player_152`** Guynmart guard: “I have Red! Sorry for you, kid. I get 100. [Gold taken] Let's try another card.”

    - Next → [guynmart_player_80](#d-guynmart_player_80)



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 28 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_player.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_player.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_player.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_player.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `guynmart_player` |
    | Spawn group | `guynmart_player` |
    | Loot table | – |
    | Conversation | `guynmart_player_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:0` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_player",
     "name": "Guynmart guard",
     "iconID": "monsters_ld1:0",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_player_10"
    }
    ```


<small>Data from v0.8.18</small>
