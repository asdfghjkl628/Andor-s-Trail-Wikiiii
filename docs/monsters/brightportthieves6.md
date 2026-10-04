# ![](../assets/icons/monsters/monsters_ld1_207.png){ .sprite } Elysa

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_207.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `brightportthieves6` |
| **Type** | NPC |
| **Class** | ? |
| **HP** | 1 |
| **Found in** | Brightport |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

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
| [brightport_thieves](../maps/brightport_thieves.md) | Brightport | 1 | – |


## Quests

- [Boxed in](../quests/brightport_thieves.md): stages 10, 50, 70
- [Search for Andor](../quests/andor.md): stages 131
- [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md): stages 130, 196, 244, 256

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Elysa. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_thiefboss_selector.json" data-npc="Elysa" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (43 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightport_thiefboss_selector"></span>**`brightport_thiefboss_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 196 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-196))* → [brightport_elysa_common](#d-brightport_elysa_common)
    - Next *(if reached stage 20 of [Boxed in](../quests/brightport_thieves.md#stage-20))* → [brightport_meeting](#d-brightport_meeting)
    - Next *(if reached stage 10 of [Boxed in](../quests/brightport_thieves.md#stage-10); NOT reached stage 20 of [Boxed in](../quests/brightport_thieves.md#stage-20))* → [brightport_elysa6](#d-brightport_elysa6)
    - Next *(if reached stage 130 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-130))* → [brightport_elysa_greeting](#d-brightport_elysa_greeting)
    - Next *(if NOT reached stage 130 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-130))* → [brightport_thiefboss_introduction](#d-brightport_thiefboss_introduction)

    <span id="d-brightport_elysa_common"></span>**`brightport_elysa_common`** Elysa: “Hello $playername, I don't have any work to give you.”

    - “You haven't told me about Andor.” *(if NOT reached stage 131 of [Search for Andor](../quests/andor.md#stage-131))* → [brightport_elysa_andor_selector](#d-brightport_elysa_andor_selector)
    - “Can you tell me about Andor again?” *(if reached stage 131 of [Search for Andor](../quests/andor.md#stage-131))* → [brightport_elysa_caught4](#d-brightport_elysa_caught4)

    <span id="d-brightport_meeting"></span>**`brightport_meeting`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 220 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-220))* → [brightport_elysa_jail](#d-brightport_elysa_jail)
    - Next *(if reached stage 40 of [Boxed in](../quests/brightport_thieves.md#stage-40))* → [brightport_elysa_caught](#d-brightport_elysa_caught)
    - Next *(if NOT reached stage 40 of [Boxed in](../quests/brightport_thieves.md#stage-40); reached stage 32 of [Boxed in](../quests/brightport_thieves.md#stage-32))* → [brightport_elysa_package](#d-brightport_elysa_package)

    <span id="d-brightport_elysa6"></span>**`brightport_elysa6`** Elysa: “Have you been the to the meeting place yet?”

    - “The courier was not there. Apparently he got arrested.” *(if reached stage 136 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-136))* → [brightport_elysa16](#d-brightport_elysa16)
    - “Not yet. [Leave.]” → *conversation ends*

    <span id="d-brightport_elysa_greeting"></span>**`brightport_elysa_greeting`** Elysa: “Hello, $playername. Here to work for us? If so we still have that errand for you.”

    - “Fine I'll do it.” → [brightport_elysa0](#d-brightport_elysa0)
    - “I don't feel like working for you right now.” → [brightport_elysa11](#d-brightport_elysa11)

    <span id="d-brightport_thiefboss_introduction"></span>**`brightport_thiefboss_introduction`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 50 of [The ruthless Crackshot](../quests/Thieves03.md#stage-50))* → [brightport_thiefboss_introduction0](#d-brightport_thiefboss_introduction0)
    - Next *(if reached stage 50 of [The ruthless Crackshot](../quests/Thieves03.md#stage-50))* → [brightport_thiefboss_introduction1](#d-brightport_thiefboss_introduction1)

    <span id="d-brightport_elysa_andor_selector"></span>**`brightport_elysa_andor_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 220 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-220); NOT reached stage 131 of [Search for Andor](../quests/andor.md#stage-131))* → [brightport_elysa_andor](#d-brightport_elysa_andor)
    - Next *(if reached stage 220 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-220); reached stage 244 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-244))* → [brightport_elysa_andor](#d-brightport_elysa_andor)
    - Next *(if reached stage 220 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-220); NOT reached stage 244 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-244))* → [brightport_elysa_jail1](#d-brightport_elysa_jail1)

    <span id="d-brightport_elysa_caught4"></span>**`brightport_elysa_caught4`** Elysa: “First, as Umar told you, Andor was looking for directions to the potion maker named Lodar; and second, he wanted information.” — **effects:** sets stage 244 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-244)

    - “What kind of information?” → [brightport_elysa_caught5](#d-brightport_elysa_caught5)

    <span id="d-brightport_elysa_jail"></span>**`brightport_elysa_jail`** Elysa: “You don't have to tell me, I know $playername, you got caught and they took the package. We don't have much left to discuss. I will still tell you about your brother Andor, but not for free.” — **effects:** sets stage 70 of [Boxed in](../quests/brightport_thieves.md#stage-70), sets stage 196 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-196)

    - “For how much?” → [brightport_elysa_jail1](#d-brightport_elysa_jail1)
    - “I actually have the package here!” *(if carry 1× [Package](../items/brightportpackage.md))* → [brightport_elysa_jail0](#d-brightport_elysa_jail0)

    <span id="d-brightport_elysa_caught"></span>**`brightport_elysa_caught`** Elysa: “$playername, you're all covered in grime, how did it go.”

    - “The guards came in after I got it from the agent. I tried hiding, but they found me and took the package with them.” *(if NOT carry 1× [Package](../items/brightportpackage.md))* → [brightport_elysa_caught1](#d-brightport_elysa_caught1)
    - “The guards came in after I got it from the agent. I tried hiding, but they found me. They left me the package but they…” *(if carry 1× [Package](../items/brightportpackage.md))* → [brightport_elysa_caught_alt](#d-brightport_elysa_caught_alt)

    <span id="d-brightport_elysa_package"></span>**`brightport_elysa_package`** Elysa: “$playername, you're all covered in grime, how did it go.”

    - “Easy as pie.” → [brightport_elysa7](#d-brightport_elysa7)

    <span id="d-brightport_elysa16"></span>**`brightport_elysa16`** Elysa: “Sigh. I thought we'd be safe away from the town. My mood is soured. I'll still tell you about Andor, but only for some gold.”

    - “How much gold?” → [brightport_elysa_jail1](#d-brightport_elysa_jail1)

    <span id="d-brightport_elysa0"></span>**`brightport_elysa0`** Elysa: “First you must know more about our activities and how the Guild operates in Brightport.”

    - “Sure.” → [brightport_elysa1](#d-brightport_elysa1)
    - “I don't have time, can't we get on with it already?” → [brightport_elysa2](#d-brightport_elysa2)

    <span id="d-brightport_elysa11"></span>**`brightport_elysa11`** Elysa: “Is that so? I believe you'll change your mind.”


    <span id="d-brightport_thiefboss_introduction0"></span>**`brightport_thiefboss_introduction0`** Elysa: “A familiar face, but you're not exactly the one I remember. Pleased to meet you, $playername.”

    - “I heard my brother Andor came to speak with you before. I was hoping you could tell me about your meeting with him.” → [brightport_thiefboss_introduction2](#d-brightport_thiefboss_introduction2)

    <span id="d-brightport_thiefboss_introduction1"></span>**`brightport_thiefboss_introduction1`** Elysa: “Well well, if it isn't one of Umar's little helpers. Did Umar run out of work for you already?”

    - “I heard my brother Andor came to speak with you before. I was hoping you could tell me about your meeting with him.” → [brightport_thiefboss_introduction2](#d-brightport_thiefboss_introduction2)

    <span id="d-brightport_elysa_andor"></span>**`brightport_elysa_andor`** Elysa: “Yes, because YOU, were rude enough to leave in the middle of our conversation. You have no patience, and you should feel ashamed.”

    - “I'm sorry, please tell me about Andor.” → [brightport_elysa_caught4](#d-brightport_elysa_caught4)

    <span id="d-brightport_elysa_jail1"></span>**`brightport_elysa_jail1`** Elysa: “Your work was supposed to pay for it, however now I feel inclined to put a price on it. 1,000 gold.”

    - “Here it is.” *(if pay 1,000 gold)* → [brightport_elysa_gold](#d-brightport_elysa_gold)
    - “I don't have the gold now. I will come later.” → *conversation ends*

    <span id="d-brightport_elysa_caught5"></span>**`brightport_elysa_caught5`** Elysa: “He wanted to know who our members are and what skills they possess. Lastly, he asked for a map of Feygard's sewers, and more importantly, the area directly under the palace. I shared this information with your brother, as his little…” — **effects:** sets stage 131 of [Search for Andor](../quests/andor.md#stage-131)

    - “Interesting, is that all?” → [brightport_elysa15](#d-brightport_elysa15)

    <span id="d-brightport_elysa_jail0"></span>**`brightport_elysa_jail0`** Elysa: “You've pleasantly surprised me $playername! I didn't think you would get to keep it after your failure.”

    - “Here you go. [Give her the package.]” *(if hand over 1× [Package](../items/brightportpackage.md))* → [brightport_elysa_jail2](#d-brightport_elysa_jail2)

    <span id="d-brightport_elysa_caught1"></span>**`brightport_elysa_caught1`** Elysa: “And they haven't arrested you, at least that's good. Have they opened the package to see what's inside?”

    - “Yes. [Tell her what happened.]” → [brightport_elysa_caught2](#d-brightport_elysa_caught2)

    <span id="d-brightport_elysa_caught_alt"></span>**`brightport_elysa_caught_alt`** Elysa: “And they haven't arrested you. That's good. Have they examined the contents of the package?”

    - “Yes. [Tell her what happened.]” → [brightport_elysa_caught2](#d-brightport_elysa_caught2)

    <span id="d-brightport_elysa7"></span>**`brightport_elysa7`** Elysa: “Good, well then where is the package?”

    - “Here it is.” *(if hand over 1× [Package](../items/brightportpackage.md))* → [brightport_elysa8](#d-brightport_elysa8)
    - “Here it is.” *(if reached stage 256 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-256))* → [brightport_elysa8](#d-brightport_elysa8)
    - “Sorry I think I dropped it somewhere.” *(if NOT carry 1× [Package](../items/brightportpackage.md))* → [brightport_elysa9](#d-brightport_elysa9)
    - “It's lost, and I can't find it.” *(if NOT carry 1× [Package](../items/brightportpackage.md))* → [brightport_elysa_failsafe](#d-brightport_elysa_failsafe)

    <span id="d-brightport_elysa1"></span>**`brightport_elysa1`** Elysa: “For most of the time since its existence, the Guild in Brightport was a place to train new recruits, away from the soldiers of Feygard and the more established thieves of Nor City.”

    - Next → [brightport_elysa4](#d-brightport_elysa4)

    <span id="d-brightport_elysa2"></span>**`brightport_elysa2`** Elysa: “Fine, $playername. I'll skip the details then.”

    - Next → [brightport_elysa3](#d-brightport_elysa3)

    <span id="d-brightport_thiefboss_introduction2"></span>**`brightport_thiefboss_introduction2`** Elysa: “I was expecting your visit after receiving a letter from Fallhaven. Umar wrote that you would come and ask some questions.”

    - Next → [brightport_thiefboss_introduction3](#d-brightport_thiefboss_introduction3)

    <span id="d-brightport_elysa_gold"></span>**`brightport_elysa_gold`** Elysa: “Thank you for your business.”

    - Next → [brightport_elysa_caught4](#d-brightport_elysa_caught4)

    <span id="d-brightport_elysa15"></span>**`brightport_elysa15`** Elysa: “That is all I feel inclined to share.”

    - “Thanks, bye.” → *conversation ends*

    <span id="d-brightport_elysa_jail2"></span>**`brightport_elysa_jail2`** [Dummy NPC](../monsters/none.md): “Elysa takes the package, opens it and takes a long look at you.”

    - Next → [brightport_elysa_jail3](#d-brightport_elysa_jail3)

    <span id="d-brightport_elysa_caught2"></span>**`brightport_elysa_caught2`** Elysa: “They will never be able to tell that it was a code. We will simply have to ask the client directly for any additional details.”

    - Next → [brightport_elysa_caught3](#d-brightport_elysa_caught3)

    <span id="d-brightport_elysa8"></span>**`brightport_elysa8`** [Dummy NPC](../monsters/none.md): “Elysa opens the small box, glances at the item inside, and closes it again.” — **effects:** sets stage 256 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-256)

    - Next → [brightport_elysa13](#d-brightport_elysa13)

    <span id="d-brightport_elysa9"></span>**`brightport_elysa9`** Elysa: “What incompetence! go pick it up.”


    <span id="d-brightport_elysa_failsafe"></span>**`brightport_elysa_failsafe`** Elysa: “You lost it? Sigh. I had higher expectations of you, my mood is soured. I'll still tell you about Andor, but only for some gold.” — **effects:** sets stage 70 of [Boxed in](../quests/brightport_thieves.md#stage-70)

    - “How much gold?” → [brightport_elysa_jail1](#d-brightport_elysa_jail1)

    <span id="d-brightport_elysa4"></span>**`brightport_elysa4`** Elysa: “But with Remgard's increasing exports of quality steel over the past hundred years, our guildhall was expanded to accomodate the growing demand for weapon smuggling.”

    - Next → [brightport_elysa5](#d-brightport_elysa5)

    <span id="d-brightport_elysa3"></span>**`brightport_elysa3`** Elysa: “We need you to pick up a package from the mediator of one of our clients. We've received word that he'll be waiting in the old building east of town. Be discreet, and make sure the guards don't see you.” — **effects:** sets stage 10 of [Boxed in](../quests/brightport_thieves.md#stage-10)

    - “I'll pick up that package for you.” → *conversation ends*

    <span id="d-brightport_thiefboss_introduction3"></span>**`brightport_thiefboss_introduction3`** Elysa: “I don't know anything more than what Umar has told you. However there is a single detail about your brother that might help you.” — **effects:** sets stage 130 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-130)

    - “A detail about my brother? I'm all ears.” *(if NOT reached stage 900 of [Excluded endings for the main quest andor (hidden flag)](../quests/andor_ending.md#stage-900))* → [brightport_elysa](#d-brightport_elysa)
    - “My journey in search of him is over, but I wouldn't mind hearing something new.” *(if reached stage 900 of [Excluded endings for the main quest andor (hidden flag)](../quests/andor_ending.md#stage-900))* → [brightport_elysa](#d-brightport_elysa)

    <span id="d-brightport_elysa_jail3"></span>**`brightport_elysa_jail3`** [Elysa](../monsters/brightportthieves6.md): “Have you come to make a fool of yourself $playername? The package is empty.” — **effects:** sets stage 196 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-196)

    - “Uh oh.” → *conversation ends*

    <span id="d-brightport_elysa_caught3"></span>**`brightport_elysa_caught3`** [Elysa](../monsters/brightportthieves6.md): “And now, let's talk about you, $playername. I'm a bit disheartened that you got caught, but I'm still willing to tell you what I know of your brother. I was planning on telling you in the first place, but a good opportunity didn't arise.” — **effects:** sets stage 70 of [Boxed in](../quests/brightport_thieves.md#stage-70), sets stage 196 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-196)

    - “I'm all ears.” → [brightport_elysa_caught4](#d-brightport_elysa_caught4)

    <span id="d-brightport_elysa13"></span>**`brightport_elysa13`** [Elysa](../monsters/brightportthieves6.md): “Very good work, $playername. I heard the guards went on patrol while you were there, and you skillfully avoided them. The Guild would very much like to have your skills again in the future.” — **effects:** sets stage 50 of [Boxed in](../quests/brightport_thieves.md#stage-50), sets stage 196 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-196)

    - Next → [brightport_elysa14](#d-brightport_elysa14)

    <span id="d-brightport_elysa5"></span>**`brightport_elysa5`** Elysa: “With the restrictions on the trade of weapons and steel by Feygard, our importance has only increased. However, the newly established inspections have made carrying out our activities in town a nuisance. Several of my men have already…”

    - Next → [brightport_elysa3](#d-brightport_elysa3)

    <span id="d-brightport_elysa"></span>**`brightport_elysa`** Elysa: “But as you know very well, the Guild has it's rules, we're not keen on doing charity. Luckily we have just the right errand for you.”

    - “Sure. What is it?” → [brightport_elysa12](#d-brightport_elysa12)
    - “I don't feel like working for you right now.” → [brightport_elysa11](#d-brightport_elysa11)

    <span id="d-brightport_elysa14"></span>**`brightport_elysa14`** Elysa: “And now the information I promised. Your brother Andor came here and asked a few questions.”

    - Next → [brightport_elysa_caught4](#d-brightport_elysa_caught4)

    <span id="d-brightport_elysa12"></span>**`brightport_elysa12`** Elysa: “Just a little errand for the Guild, I believe you are well acquainted with those.”

    - Next → [brightport_elysa0](#d-brightport_elysa0)



## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 43 lines added |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed<br>· text: “Your work was supposed to pay for it, however now I feel inclined to …” → “Your work was supposed to pay for it, however now I feel inclined to …” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportthieves6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportthieves6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportthieves6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportthieves6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `brightportthieves6` |
    | Spawn group | `brightportthieves6` |
    | Loot table | – |
    | Conversation | `brightport_thiefboss_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:207` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportthieves6",
     "name": "Elysa",
     "iconID": "monsters_ld1:207",
     "phraseID": "brightport_thiefboss_selector"
    }
    ```


<small>Data from v0.8.18</small>
