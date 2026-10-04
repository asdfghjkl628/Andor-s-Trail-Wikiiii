# ![](../assets/icons/monsters/monsters_karvis2_5.png){ .sprite } Old man

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_karvis2_5.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `guynmart_wise` |
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
| [guynmart_wood_10](../maps/guynmart_wood_10.md) | Guynmart Castle | 1 | – |


## Quests

- [Rare delicacies](../quests/guynmart_wise.md): stages 10, 20, 30, 90
- [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md): stages 35

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Old man. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_wise_10.json" data-npc="Old man" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (42 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guynmart_wise_10"></span>**`guynmart_wise_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 35 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-35))* → [guynmart_wise_14](#d-guynmart_wise_14)
    - branch 2 → [guynmart_wise_12](#d-guynmart_wise_12)

    <span id="d-guynmart_wise_14"></span>**`guynmart_wise_14`** Old man: “Oh, it is you again. I am delighted!”

    - “De-lighted indeed. Might you need anything?” → [guynmart_wise_110](#d-guynmart_wise_110)

    <span id="d-guynmart_wise_12"></span>**`guynmart_wise_12`** Old man: “Oh, a visitor. Come closer. Do not be afraid of me.”

    - “I am not afraid. What happened to you?” → [guynmart_wise_20](#d-guynmart_wise_20)
    - “Eh, I have to go.” → *conversation ends*

    <span id="d-guynmart_wise_110"></span>**`guynmart_wise_110`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 90 of [Rare delicacies](../quests/guynmart_wise.md#stage-90))* → [guynmart_wise_116](#d-guynmart_wise_116)
    - branch 2 *(if reached stage 30 of [Rare delicacies](../quests/guynmart_wise.md#stage-30))* → [guynmart_wise_112](#d-guynmart_wise_112)
    - branch 3 *(if reached stage 20 of [Rare delicacies](../quests/guynmart_wise.md#stage-20))* → [guynmart_wise_170](#d-guynmart_wise_170)
    - branch 4 *(if reached stage 10 of [Rare delicacies](../quests/guynmart_wise.md#stage-10))* → [guynmart_wise_114](#d-guynmart_wise_114)
    - branch 5 → [guynmart_wise_118](#d-guynmart_wise_118)

    <span id="d-guynmart_wise_20"></span>**`guynmart_wise_20`** Old man: “It happened in the mines of Mount Galmore. Don't ask any more, I do not wish to recall the memories. It was horrible.”

    - Next → [guynmart_wise_60](#d-guynmart_wise_60)

    <span id="d-guynmart_wise_116"></span>**`guynmart_wise_116`** Old man: “No, thank you.”

    - Next → [guynmart_wise_900](#d-guynmart_wise_900)

    <span id="d-guynmart_wise_112"></span>**`guynmart_wise_112`** Old man: “Do you bring bread and wine, together with my favorite cheddar?”

    - “Yes, finally I got it. I hope the cheddar is still fresh after the long journey.” *(if hand over 2× [Bread](../items/bread.md); hand over 1× [Charwood cheddar](../items/charwood_cheddar.md); hand over 1× [Wine](../items/guynmart_wine.md))* → [guynmart_wise_200](#d-guynmart_wise_200)
    - “No, not yet.” → [guynmart_wise_800](#d-guynmart_wise_800)

    <span id="d-guynmart_wise_170"></span>**`guynmart_wise_170`** Old man: “...”

    - Next → [guynmart_wise_172](#d-guynmart_wise_172)

    <span id="d-guynmart_wise_114"></span>**`guynmart_wise_114`** Old man: “Do you bring bread, cheese and wine?”

    - “Yes, here you are. Enjoy it!” *(if hand over 2× [Bread](../items/bread.md); hand over 1× [Cheese](../items/cheese.md); hand over 1× [Wine](../items/guynmart_wine.md))* → [guynmart_wise_150](#d-guynmart_wise_150)
    - “No, not yet.” → [guynmart_wise_800](#d-guynmart_wise_800)

    <span id="d-guynmart_wise_118"></span>**`guynmart_wise_118`** Old man: “Just recently my supply of bread has run low again. And I haven't seen eggs for such a long time...”

    - “I can help with that. I can spare 2 loaves of bread.” *(if hand over 2× [Bread](../items/bread.md))* → [guynmart_wise_120](#d-guynmart_wise_120)
    - “I could give you 3 eggs.” *(if hand over 3× [Eggs](../items/eggs.md))* → [guynmart_wise_120](#d-guynmart_wise_120)
    - “I could spare bread, some cheese and a bottle of red wine.” *(if reached stage 10 of [Rare delicacies](../quests/guynmart_wise.md#stage-10); hand over 2× [Bread](../items/bread.md); hand over 1× [Cheese](../items/cheese.md); hand over 1× [Wine](../items/guynmart_wine.md))* → [guynmart_wise_150](#d-guynmart_wise_150)
    - “Unfortunately I have nothing I could give you.” → [guynmart_wise_900](#d-guynmart_wise_900)
    - “Sad for you. I have to go now. Bye.” → *conversation ends*

    <span id="d-guynmart_wise_60"></span>**`guynmart_wise_60`** Old man: “When I returned here at last, people started to avoid me, whispering behind my back. I got very lonely.”

    - Next → [guynmart_wise_100](#d-guynmart_wise_100)

    <span id="d-guynmart_wise_900"></span>**`guynmart_wise_900`** Old man: “It was nice to talk to you. Come again, as often as you like!”

    - “Yes, we will meet again.” → *conversation ends*

    <span id="d-guynmart_wise_200"></span>**`guynmart_wise_200`** Old man: “Cheddar! I can't believe it!” — **effects:** sets stage 90 of [Rare delicacies](../quests/guynmart_wise.md#stage-90)

    - Next → [guynmart_wise_202](#d-guynmart_wise_202)

    <span id="d-guynmart_wise_800"></span>**`guynmart_wise_800`** Old man: “Ah - I can see it before my eyes: a loaf of bread with a piece of delicious cheese! No, better two loaves of bread.”

    - Next → [guynmart_wise_802](#d-guynmart_wise_802)

    <span id="d-guynmart_wise_172"></span>**`guynmart_wise_172`** Old man: “Eh...”

    - “Yes?” → [guynmart_wise_174](#d-guynmart_wise_174)

    <span id="d-guynmart_wise_150"></span>**`guynmart_wise_150`** Old man: “What a feast! I have no words to thank you!”

    - Next → [guynmart_wise_160](#d-guynmart_wise_160)

    <span id="d-guynmart_wise_120"></span>**`guynmart_wise_120`** Old man: “Thank you! Thank you very much!”

    - Next → [guynmart_wise_122](#d-guynmart_wise_122)

    <span id="d-guynmart_wise_100"></span>**`guynmart_wise_100`** Old man: “Eventually I had enough of all the anxious, disturbed looks, so I came up here on this lonely hill.”

    - Next → [guynmart_wise_102](#d-guynmart_wise_102)

    <span id="d-guynmart_wise_202"></span>**`guynmart_wise_202`** Old man: “[Eating]”

    - Next → [guynmart_wise_900](#d-guynmart_wise_900)

    <span id="d-guynmart_wise_802"></span>**`guynmart_wise_802`** Old man: “Along with a bottle of good red wine!”

    - Next → [guynmart_wise_804](#d-guynmart_wise_804)

    <span id="d-guynmart_wise_174"></span>**`guynmart_wise_174`** Old man: “now...”

    - “Oh dear! Just say what is on your mind. What's up?” → [guynmart_wise_180](#d-guynmart_wise_180)

    <span id="d-guynmart_wise_160"></span>**`guynmart_wise_160`** Old man: “So take this ring as a token of my gratitude. Certain beings in the cellars of Guynmart Castle will not harm you if they see my ring on your finger.” — **effects:** gives 1× [Old man's ring of bone](../items/guynmart_bonering.md), sets stage 20 of [Rare delicacies](../quests/guynmart_wise.md#stage-20)

    - “The ring looks interesting. Thank you.” → [guynmart_wise_170](#d-guynmart_wise_170)

    <span id="d-guynmart_wise_122"></span>**`guynmart_wise_122`** Old man: “Would it be really outrageous if I asked you to fulfill my heart's desire?”

    - “Sorry, I really must go now.” → [guynmart_wise_900](#d-guynmart_wise_900)
    - “Just say what you would like. What can I do for you?” → [guynmart_wise_130](#d-guynmart_wise_130)

    <span id="d-guynmart_wise_102"></span>**`guynmart_wise_102`** Old man: “From time to time a friendly soul brings me some food, but no one stays for long. I have noticed that their pace uphill is usually much slower than back downhill.” — **effects:** sets stage 35 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-35)

    - Next → [guynmart_wise_110](#d-guynmart_wise_110)

    <span id="d-guynmart_wise_804"></span>**`guynmart_wise_804`** Old man: “The bread maybe still warm ...”

    - Next → [guynmart_wise_806](#d-guynmart_wise_806)

    <span id="d-guynmart_wise_180"></span>**`guynmart_wise_180`** Old man: “The cheese that you brought - It was OK. But it is not the best cheese, you know? The best cheese is from Charwood.”

    - “Oh?” → [guynmart_wise_182](#d-guynmart_wise_182)

    <span id="d-guynmart_wise_130"></span>**`guynmart_wise_130`** Old man: “I long for a meal with bread and cheese and a good bottle of wine. Oh, what would I give for that?” — **effects:** sets stage 10 of [Rare delicacies](../quests/guynmart_wise.md#stage-10)

    - “Here I have bread, some cheese and a bottle of red wine.” *(if hand over 2× [Bread](../items/bread.md); hand over 1× [Cheese](../items/cheese.md); hand over 1× [Wine](../items/guynmart_wine.md))* → [guynmart_wise_150](#d-guynmart_wise_150)
    - “Really? That is all? I will come back soon.” → [guynmart_wise_132](#d-guynmart_wise_132)
    - “Be content with what you got, you greedy old man.” → *conversation ends*

    <span id="d-guynmart_wise_806"></span>**`guynmart_wise_806`** Old man: “Sigh.”

    - Next → [guynmart_wise_810](#d-guynmart_wise_810)

    <span id="d-guynmart_wise_182"></span>**`guynmart_wise_182`** Old man: “Their Cheddar is a dream! But they sell it only when you explicitly ask for it.” — **effects:** sets stage 30 of [Rare delicacies](../quests/guynmart_wise.md#stage-30)

    - “No problem. I will go and get some.” → [guynmart_wise_190](#d-guynmart_wise_190)
    - “I am not going to go all the way to Charwood for some cheddar.” *(if reached stage 19 of [Destined for great things](../quests/charwood1.md#stage-19))* → *conversation ends*
    - “Where is Charwood?” *(if NOT reached stage 19 of [Destined for great things](../quests/charwood1.md#stage-19))* → *conversation ends*

    <span id="d-guynmart_wise_132"></span>**`guynmart_wise_132`** Old man: “Oh yes - you get the best cheese in Charwood, if you don't mind!”

    - “Charwood? That's not exactly next door...” *(if reached stage 19 of [Destined for great things](../quests/charwood1.md#stage-19))* → *conversation ends*
    - “I have heard of Charwood, but I don't know where it is.” *(if reached stage 10 of [Destined for great things](../quests/charwood1.md#stage-10); NOT reached stage 19 of [Destined for great things](../quests/charwood1.md#stage-19))* → *conversation ends*
    - “I have heard of Charwood, but I don't know where it is.” *(if reached stage 11 of [Destined for great things](../quests/charwood1.md#stage-11); NOT reached stage 19 of [Destined for great things](../quests/charwood1.md#stage-19))* → *conversation ends*
    - “Charwood? I have never heard of it.” → *conversation ends*

    <span id="d-guynmart_wise_810"></span>**`guynmart_wise_810`** Old man: “Two loaves of bread! Hmmmm.”

    - “Well ...” → [guynmart_wise_812](#d-guynmart_wise_812)

    <span id="d-guynmart_wise_190"></span>**`guynmart_wise_190`** Old man: “Great! I will wait for your return.”


    <span id="d-guynmart_wise_812"></span>**`guynmart_wise_812`** Old man: “And cheese - how I missed it!”

    - “But ...” → [guynmart_wise_814](#d-guynmart_wise_814)

    <span id="d-guynmart_wise_814"></span>**`guynmart_wise_814`** Old man: “A bottle of red wine with it, of course. Ooooh!”

    - “I'm beginning to find your requests outrageous. I have to leave now.” → [guynmart_wise_820](#d-guynmart_wise_820)
    - “OK, OK, I understand.” → [guynmart_wise_830](#d-guynmart_wise_830)

    <span id="d-guynmart_wise_820"></span>**`guynmart_wise_820`** Old man: “Noo! Please, don't go! I didn't mean it.”

    - “Forget it, bye.” → *conversation ends*
    - “OK. Bread, cheese and vine - that's it?” → [guynmart_wise_800](#d-guynmart_wise_800)

    <span id="d-guynmart_wise_830"></span>**`guynmart_wise_830`** Old man: “Great! It's settled then, I'll wait for you here.”

    - “I'll hurry now. See you soon.” → [guynmart_wise_840](#d-guynmart_wise_840)

    <span id="d-guynmart_wise_840"></span>**`guynmart_wise_840`** Old man: “Ah - bread ...”

    - Next → [guynmart_wise_841](#d-guynmart_wise_841)

    <span id="d-guynmart_wise_841"></span>**`guynmart_wise_841`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (50%))* → [guynmart_wise_842](#d-guynmart_wise_842)
    - branch 2 → [guynmart_wise_844](#d-guynmart_wise_844)

    <span id="d-guynmart_wise_842"></span>**`guynmart_wise_842`** Old man: “And cheese ...”

    - Next → [guynmart_wise_843](#d-guynmart_wise_843)

    <span id="d-guynmart_wise_844"></span>**`guynmart_wise_844`** Old man: “Vine ...”

    - Next → [guynmart_wise_845](#d-guynmart_wise_845)

    <span id="d-guynmart_wise_843"></span>**`guynmart_wise_843`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (50%))* → [guynmart_wise_840](#d-guynmart_wise_840)
    - branch 2 → [guynmart_wise_844](#d-guynmart_wise_844)

    <span id="d-guynmart_wise_845"></span>**`guynmart_wise_845`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (50%))* → [guynmart_wise_840](#d-guynmart_wise_840)
    - branch 2 → [guynmart_wise_842](#d-guynmart_wise_842)



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 27 lines added |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 1 line changed<br>· text: “Cheddar! I can't belive it!” → “Cheddar! I can't believe it!” |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 1 line changed<br>· text: “It happend in the mines of Mount Galmore. Don't ask any more, I do no…” → “It happened in the mines of Mount Galmore. Don't ask any more, I do n…” |
| [v0.7.14](../versions/0.7.14.md) | Dialogue: 15 lines added, 2 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_wise.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_wise.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_wise.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_wise.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `guynmart_wise` |
    | Spawn group | `guynmart_wise` |
    | Loot table | – |
    | Conversation | `guynmart_wise_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:5` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_wise",
     "name": "Old man",
     "iconID": "monsters_karvis2:5",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_wise_10"
    }
    ```


<small>Data from v0.8.18</small>
