# ![](../assets/icons/monsters/monsters_omi2_2.png){ .sprite } Thalen

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_omi2_2.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `thalen` |
| **Type** | NPC |
| **Class** | Undead |
| **HP** | 1 |
| **Found in** | undertell_3_lava_00 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

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
| [undertell_3_lava_00](../maps/undertell_3_lava_00.md) | – | 1 | – |


## Quests

- [About a girl](../quests/about_a_girl.md): stages 50
- [The fifth master](../quests/fifth_master.md): stages 10, 20, 80
- [hidden_undertell (hidden flag)](../quests/undertell_hidden.md): stages 5, 7

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Thalen. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/thalen_initial_selector.json" data-npc="Thalen" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (23 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-thalen_initial_selector"></span>**`thalen_initial_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 5 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-5))* → [kazaul_masters_not_met_10](#d-kazaul_masters_not_met_10)
    - branch 2 *(if reached stage 5 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-5); NOT reached stage 10 of [The fifth master](../quests/fifth_master.md#stage-10))* → [kazaul_masters_met_but_no_quest_started_10](#d-kazaul_masters_met_but_no_quest_started_10)
    - branch 3 *(if reached stage 10 of [The fifth master](../quests/fifth_master.md#stage-10); NOT reached stage 20 of [The fifth master](../quests/fifth_master.md#stage-20))* → [the_fifth_master_10](#d-the_fifth_master_10)
    - branch 4 *(if carry 1× [The Ritual of Five Aspects](../items/ancient_kazaul_ritual.md))* → [thalen_receives_ritual_10](#d-thalen_receives_ritual_10)
    - branch 5 *(if reached stage 90 of [The fifth master](../quests/fifth_master.md#stage-90))* → [thalen_after_fifth_master](#d-thalen_after_fifth_master)
    - branch 6 → [thalen_intro_10_narrator](#d-thalen_intro_10_narrator)

    <span id="d-kazaul_masters_not_met_10"></span>**`kazaul_masters_not_met_10`** Thalen: “[While pointing its finger in your direction.] You! How did you get past our army?”

    - “"Our"? There's more of you bosses?” → [kazaul_masters_not_met_20](#d-kazaul_masters_not_met_20)

    <span id="d-kazaul_masters_met_but_no_quest_started_10"></span>**`kazaul_masters_met_but_no_quest_started_10`** Thalen: “If you ever leave while I am talking to you again, I will end your life. Understood?”

    - “[Terrified] Yes.” → [kazaul_masters_not_met_30](#d-kazaul_masters_not_met_30)

    <span id="d-the_fifth_master_10"></span>**`the_fifth_master_10`** Thalen: “[The air grows heavy as the master studies you.] You are bold to walk here. Perhaps bold enough to be of use. One of our own is missing. The fifth master, Anavrin, lies silent. The Ritual of Five Aspects was taken from us long ago.…” — **effects:** sets stage 10 of [The fifth master](../quests/fifth_master.md#stage-10)

    - “You want me to find this ritual?” → [the_fifth_master_20](#d-the_fifth_master_20)

    <span id="d-thalen_receives_ritual_10"></span>**`thalen_receives_ritual_10`** Thalen: “So, you have found it. The Ritual of Five Aspects...it returns to us at last.”

    - “You said this would seal the rift forever.” → [thalen_receives_ritual_20](#d-thalen_receives_ritual_20)

    <span id="d-thalen_after_fifth_master"></span>**`thalen_after_fifth_master`** Thalen: “So...the circle is whole again. I warned the others that some truths should remain buried. But curiosity always feeds the dark.”

    - “[Leave.]” → *conversation ends*
    - “I am looking for a folded copper talisman.” *(if reached stage 40 of [About a girl](../quests/about_a_girl.md#stage-40); NOT reached stage 50 of [About a girl](../quests/about_a_girl.md#stage-50))* → [master_thalen_about_girl_20](#d-master_thalen_about_girl_20)

    <span id="d-thalen_intro_10_narrator"></span>**`thalen_intro_10_narrator`** [Dummy NPC](../monsters/none.md): “An ancient presence hums behind your eyes.”

    - Next → [thalen_intro_10](#d-thalen_intro_10)

    <span id="d-kazaul_masters_not_met_20"></span>**`kazaul_masters_not_met_20`** Thalen: “We are "masters", not "bosses". And yes, there are five of us.” — **effects:** sets stage 5 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-5)

    - Next → [kazaul_masters_not_met_30](#d-kazaul_masters_not_met_30)

    <span id="d-kazaul_masters_not_met_30"></span>**`kazaul_masters_not_met_30`** Thalen: “Well, currently there are only four of us masters. We are not complete.”

    - “"Complete"? What is that supposed to mean?” → [the_fifth_master_10](#d-the_fifth_master_10)

    <span id="d-the_fifth_master_20"></span>**`the_fifth_master_20`** Thalen: “Yes. The Ritual of Five Aspects lies lost among your kind. Long ago, a mortal scribe named Varnel served the Kazaul, writing our words into form. But when fear took him, he fled with the ritual and hid among your people. Bring it back to…” — **effects:** sets stage 20 of [The fifth master](../quests/fifth_master.md#stage-20)

    - “Then I will find it.” → [the_fifth_master_accept](#d-the_fifth_master_accept)
    - “I do not trust you, but I will look.” → [the_fifth_master_accept](#d-the_fifth_master_accept)

    <span id="d-thalen_receives_ritual_20"></span>**`thalen_receives_ritual_20`** Thalen: “Yes...or so it must be believed. The power it binds will quiet the rift if spoken by the faithful. Bring it to the shrine of Anavrin, the Silent One. One of our lesser kin will meet you there to perform the rite.”

    - “Then I will take it to the shrine.” *(if hand over 1× [The Ritual of Five Aspects](../items/ancient_kazaul_ritual.md))* → [thalen_receives_ritual_30](#d-thalen_receives_ritual_30)

    <span id="d-master_thalen_about_girl_20"></span>**`master_thalen_about_girl_20`** Thalen: “A child's charm. Folded copper. Fear pretending to be faith.”

    - “It mattered to her.” → [master_thalen_about_girl_30](#d-master_thalen_about_girl_30)

    <span id="d-thalen_intro_10"></span>**`thalen_intro_10`** [Thalen](../monsters/thalen.md): “Another seeker of knowledge? Few survive long enough to regret such curiosity.”

    - “I only want to understand what happened here.” → [thalen_intro_20](#d-thalen_intro_20)

    <span id="d-the_fifth_master_accept"></span>**`the_fifth_master_accept`** Thalen: “[The master's eyes flare with dim light.] Then go, mortal. Seek the lost ritual. In the ruins of your kind lies our key to completion. Return only when it is found.”

    - “I understand.” → *conversation ends*

    <span id="d-thalen_receives_ritual_30"></span>**`thalen_receives_ritual_30`** Thalen: “No. Give it to me and I will give it to the kin. You have done what none of the living could. Do not fail now, mortal. The silence of Anavrin waits to be broken.” — **effects:** sets stage 80 of [The fifth master](../quests/fifth_master.md#stage-80), spawns monsters on undertell_5, sets stage 7 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-7)

    - “I understand.” → *conversation ends*

    <span id="d-master_thalen_about_girl_30"></span>**`master_thalen_about_girl_30`** Thalen: “Yes. And fear is the purest lens for understanding devotion. We examined it. Measured what clung to it.”

    - “What did you find?” → [master_thalen_about_girl_40](#d-master_thalen_about_girl_40)

    <span id="d-thalen_intro_20"></span>**`thalen_intro_20`** Thalen: “Leave now, before you can't”


    <span id="d-master_thalen_about_girl_40"></span>**`master_thalen_about_girl_40`** Thalen: “That belief leaves an imprint. Not divine. Not benign. Something old listens when it is named.”

    - “The Shadow?” → [master_thalen_about_girl_50](#d-master_thalen_about_girl_50)

    <span id="d-master_thalen_about_girl_50"></span>**`master_thalen_about_girl_50`** Thalen: “Names are doors. Some were spoken long before your kind learned prayer. The Kazaul understood this well.”

    - “You are saying the Shadow answers to them.” → [master_thalen_about_girl_60](#d-master_thalen_about_girl_60)

    <span id="d-master_thalen_about_girl_60"></span>**`master_thalen_about_girl_60`** Thalen: “I am saying echoes do not choose who repeats them.”

    - “Where is the talisman now?” → [master_thalen_about_girl_70](#d-master_thalen_about_girl_70)

    <span id="d-master_thalen_about_girl_70"></span>**`master_thalen_about_girl_70`** Thalen: “Sealed. Labeled. Forgotten. As most inconvenient things are.”

    - “You want me to retrieve it.” → [master_thalen_about_girl_80](#d-master_thalen_about_girl_80)

    <span id="d-master_thalen_about_girl_80"></span>**`master_thalen_about_girl_80`** Thalen: “I want it removed from circulation. Belief is dangerous when it spreads without instruction.”

    - “Where do I find it?” → [master_thalen_about_girl_90](#d-master_thalen_about_girl_90)

    <span id="d-master_thalen_about_girl_90"></span>**`master_thalen_about_girl_90`** Thalen: “In the lower records. Where discarded faith is kept for study, not mercy.” — **effects:** sets stage 50 of [About a girl](../quests/about_a_girl.md#stage-50)




## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 23 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=thalen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=thalen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=thalen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=thalen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `thalen` |
    | Spawn group | `thalen` |
    | Loot table | – |
    | Conversation | `thalen_initial_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_omi2:2` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "thalen",
     "name": "Thalen",
     "iconID": "monsters_omi2:2",
     "maxHP": 1,
     "unique": 1,
     "monsterClass": "undead",
     "phraseID": "thalen_initial_selector"
    }
    ```


<small>Data from v0.8.18</small>
