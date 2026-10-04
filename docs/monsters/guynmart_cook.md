# ![](../assets/icons/monsters/monsters_ld1_18.png){ .sprite } Hofala

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_18.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `guynmart_cook` |
| **Type** | Shopkeeper |
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


## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Bread](../items/bread.md) | 100% | 5 |
| [Mushroom](../items/mushroom.md) | 100% | 10 |
| [Eggs](../items/eggs.md) | 100% | 10 |
| [Pear](../items/pear.md) | 100% | 10 |
| [Wine](../items/guynmart_wine.md) | 100% | 25 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [guynmart_main_2](../maps/guynmart_main_2.md) | Guynmart Castle | 1 | – |


## Quests

- [Roses](../quests/guynmart.md): stages 62, 64
- [guynmart_quest_cook_bread (hidden flag)](../quests/guynmart_quest_cook_bread.md): stages 1
- [guynmart_quest_cook_lunch (hidden flag)](../quests/guynmart_quest_cook_lunch.md): stages 1

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Hofala. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_cook_10.json" data-npc="Hofala" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (20 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guynmart_cook_10"></span>**`guynmart_cook_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 170 of [Roses](../quests/guynmart.md#stage-170))* → [guynmart_cook_14](#d-guynmart_cook_14)
    - branch 2 *(if hand over 1× [Hannah's special herbs](../items/guynmart_herbs.md))* → [guynmart_cook_100](#d-guynmart_cook_100)
    - branch 3 *(if reached stage 62 of [Roses](../quests/guynmart.md#stage-62); NOT reached stage 64 of [Roses](../quests/guynmart.md#stage-64))* → [guynmart_cook_22](#d-guynmart_cook_22)
    - branch 4 → [guynmart_cook_20](#d-guynmart_cook_20)

    <span id="d-guynmart_cook_14"></span>**`guynmart_cook_14`** Hofala: “I am glad the feast is over. It was hard work.”

    - “It's a pity that I couldn't attend the wedding.” → *conversation ends*
    - “Could I buy some provisions?” → *shop opens*

    <span id="d-guynmart_cook_100"></span>**`guynmart_cook_100`** Hofala: “Ah, the herbs. Good. You are not completely useless. I will add them to Lady Hannah's meal...”

    - Next → [guynmart_cook_102](#d-guynmart_cook_102)

    <span id="d-guynmart_cook_22"></span>**`guynmart_cook_22`** Hofala: “Did you bring the herbs for Hannah's lunch?”

    - “Oh. I knew I had forgotten something...” → *conversation ends*
    - “The steward told me you could give me some bread.” *(if reached stage 40 of [Roses](../quests/guynmart.md#stage-40))* → [guynmart_cook_30](#d-guynmart_cook_30)
    - “Could I buy some provisions?” → [guynmart_cook_50](#d-guynmart_cook_50)

    <span id="d-guynmart_cook_20"></span>**`guynmart_cook_20`** Hofala: “What do you want? Be quick - I am preparing the meal for a wedding and I have little time.”

    - “Hannah's maid asked me to take her lunch to her.” *(if reached stage 50 of [Roses](../quests/guynmart.md#stage-50); NOT reached stage 62 of [Roses](../quests/guynmart.md#stage-62))* → [guynmart_cook_60](#d-guynmart_cook_60)
    - “The steward told me you could give me some bread.” *(if reached stage 40 of [Roses](../quests/guynmart.md#stage-40))* → [guynmart_cook_30](#d-guynmart_cook_30)
    - “I would like to see Lady Hannah.” *(if NOT reached stage 62 of [Roses](../quests/guynmart.md#stage-62))* → [guynmart_cook_40](#d-guynmart_cook_40)
    - “Can I buy some provisions?” → [guynmart_cook_50](#d-guynmart_cook_50)

    <span id="d-guynmart_cook_102"></span>**`guynmart_cook_102`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if hand over 1× [Hannah's special herbs](../items/guynmart_herbs.md))* → [guynmart_cook_104](#d-guynmart_cook_104)
    - branch 2 → [guynmart_cook_110](#d-guynmart_cook_110)

    <span id="d-guynmart_cook_30"></span>**`guynmart_cook_30`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 1 of [guynmart_quest_cook_bread (hidden flag)](../quests/guynmart_quest_cook_bread.md#stage-1))* → [guynmart_cook_32](#d-guynmart_cook_32)
    - branch 2 → [guynmart_cook_34](#d-guynmart_cook_34)

    <span id="d-guynmart_cook_50"></span>**`guynmart_cook_50`** Hofala: “Yes, of course. But be quick, I still have a lot of work to do.”

    - “OK, show me what you have.” → *shop opens*

    <span id="d-guynmart_cook_60"></span>**`guynmart_cook_60`** Hofala: “Good idea! You can carry her lunch up all those stairs to the tower top, and I'll have more time to prepare the wedding meal.”

    - Next → [guynmart_cook_70](#d-guynmart_cook_70)

    <span id="d-guynmart_cook_40"></span>**`guynmart_cook_40`** Hofala: “Hmm. She might be in her room upstairs, or maybe on the top of the tower again. But of course you can't see her, so it doesn't really matter.”

    - “Yes, sure. I will leave now.” → *conversation ends*
    - “The steward told me that you could give me some bread.” *(if reached stage 40 of [Roses](../quests/guynmart.md#stage-40))* → [guynmart_cook_30](#d-guynmart_cook_30)
    - “Could I buy some provisions?” → [guynmart_cook_50](#d-guynmart_cook_50)

    <span id="d-guynmart_cook_104"></span>**`guynmart_cook_104`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if hand over 1× [Hannah's special herbs](../items/guynmart_herbs.md))* → [guynmart_cook_104](#d-guynmart_cook_104)
    - branch 2 → [guynmart_cook_106](#d-guynmart_cook_106)

    <span id="d-guynmart_cook_110"></span>**`guynmart_cook_110`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 64 of [Roses](../quests/guynmart.md#stage-64))* → [guynmart_cook_112](#d-guynmart_cook_112)
    - branch 2 → [guynmart_cook_120](#d-guynmart_cook_120)

    <span id="d-guynmart_cook_32"></span>**`guynmart_cook_32`** Hofala: “Do you think I am stupid? I already gave you two fine loaves of bread, for free! Out of my kitchen, you scum!”

    - “It was worth a try.” → *conversation ends*

    <span id="d-guynmart_cook_34"></span>**`guynmart_cook_34`** Hofala: “Yes, of course. Just a second.”

    - Next → [guynmart_cook_36](#d-guynmart_cook_36)

    <span id="d-guynmart_cook_70"></span>**`guynmart_cook_70`** Hofala: “Oh no! I am running out of Lady Hannah's special herbs, and these are essential for her lunch.”

    - Next → [guynmart_cook_72](#d-guynmart_cook_72)

    <span id="d-guynmart_cook_106"></span>**`guynmart_cook_106`** Hofala: “You should have brought just 1 portion. These herbs must be used fresh. Nevertheless I will take all the herbs. [All herb portions taken]”

    - “Eh, yes of course.” → [guynmart_cook_110](#d-guynmart_cook_110)

    <span id="d-guynmart_cook_112"></span>**`guynmart_cook_112`** Hofala: “Of course you won't get another serving of lunch!”

    - “Eh, yes, of course.” → *conversation ends*

    <span id="d-guynmart_cook_120"></span>**`guynmart_cook_120`** Hofala: “...and now it is suitable for her. Hurry now, while it is still hot!” — **effects:** gives [Hannah's lunch](../items/guynmart_lunch.md), sets stage 64 of [Roses](../quests/guynmart.md#stage-64), sets stage 1 of [guynmart_quest_cook_lunch (hidden flag)](../quests/guynmart_quest_cook_lunch.md#stage-1)

    - “Ouch! It is really hot!” → *conversation ends*

    <span id="d-guynmart_cook_36"></span>**`guynmart_cook_36`** Hofala: “Here I have some fresh bread for you. Enjoy it.” — **effects:** gives [Bread](../items/bread.md), sets stage 1 of [guynmart_quest_cook_bread (hidden flag)](../quests/guynmart_quest_cook_bread.md#stage-1)

    - “Many thanks. Bye.” → *conversation ends*
    - “I would like to see Lady Hannah.” → [guynmart_cook_40](#d-guynmart_cook_40)
    - “Could I also buy some provisions?” → [guynmart_cook_50](#d-guynmart_cook_50)

    <span id="d-guynmart_cook_72"></span>**`guynmart_cook_72`** Hofala: “Quick, run to Nuik, the old gardener. He will give you some fresh herbs.” — **effects:** sets stage 62 of [Roses](../quests/guynmart.md#stage-62)

    - “OK. I will get the herbs.” → *conversation ends*
    - “I've had enough! Do it yourself.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 20 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_cook.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_cook.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_cook.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_cook.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `guynmart_cook` |
    | Spawn group | `guynmart_cook` |
    | Loot table | `guynmart_drp_cook_shop` |
    | Conversation | `guynmart_cook_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:18` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_cook",
     "name": "Hofala",
     "iconID": "monsters_ld1:18",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_cook_10",
     "droplistID": "guynmart_drp_cook_shop"
    }
    ```


<small>Data from v0.8.18</small>
