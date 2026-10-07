---
description: "Oswald is a non-player character (NPC) in Andor's Trail, found in Brightport."
---

# ![](../assets/icons/monsters/monsters_ld1_56.png){ .sprite } Oswald

**Where to find Oswald:** Brightport: [brightport_school9](../maps/brightport_school9.md#pin-npc-brightportnpc6)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_56.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Brightport |
| **Entry ID** | `brightportnpc6` |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Quests

- [No rest for the wicked](../quests/Stanwickquest.md): stages 35, 46, 47, 96, 97, 100
- [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md): stages 75, 80, 85

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Oswald. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/oswald_selector.json" data-npc="Oswald" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (36 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-oswald_selector"></span>**`oswald_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 96 of [No rest for the wicked](../quests/Stanwickquest.md#stage-96))* → [oswald_end](#d-oswald_end)
    - Next *(if reached stage 85 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-85))* → [brightport_oswald13](#d-brightport_oswald13)
    - Next *(if reached stage 35 of [No rest for the wicked](../quests/Stanwickquest.md#stage-35))* → [oswald_quest](#d-oswald_quest)
    - Next *(if NOT reached stage 35 of [No rest for the wicked](../quests/Stanwickquest.md#stage-35))* → [oswald_start](#d-oswald_start)

    <span id="d-oswald_end"></span>**`oswald_end`** Oswald: “How unfortunate to be stuck inside, when the sun's so dazzling.”

    - “Excuse me sir. I was kicked out of the lecture room for misbehaving.” *(if reached stage 228 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-228))* → [brightport_oswald_selector_lecture](#d-brightport_oswald_selector_lecture)

    <span id="d-brightport_oswald13"></span>**`brightport_oswald13`** [Oswald](../monsters/brightportnpc6.md): “You've truly saved my skin - I mean, the people of Brightport! Yes, ahem.”

    - Next → [brightport_oswald14](#d-brightport_oswald14)

    <span id="d-oswald_quest"></span>**`oswald_quest`** Oswald: “Hey kid, any progress on finding the missing document?”

    - “I have the scroll here, take it.” *(if hand over 1× [Secret scroll](../items/brightport_scroll.md))* → [brightport_oswald12](#d-brightport_oswald12)
    - “Do you know who Bryma is?” *(if reached stage 55 of [No rest for the wicked](../quests/Stanwickquest.md#stage-55); NOT reached stage 60 of [No rest for the wicked](../quests/Stanwickquest.md#stage-60))* → [brightport_oswald27](#d-brightport_oswald27)
    - “Excuse me sir. I was kicked out of the lecture room for misbehaving.” *(if reached stage 228 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-228))* → [brightport_oswald26](#d-brightport_oswald26)
    - “If I could investigate the library, maybe I could find something.” *(if reached stage 45 of [No rest for the wicked](../quests/Stanwickquest.md#stage-45); NOT reached stage 46 of [No rest for the wicked](../quests/Stanwickquest.md#stage-46))* → [brightport_oswald7](#d-brightport_oswald7)
    - “Sir, what's that thing looking at us through the window?” *(if reached stage 46 of [No rest for the wicked](../quests/Stanwickquest.md#stage-46); NOT reached stage 50 of [No rest for the wicked](../quests/Stanwickquest.md#stage-50); NOT reached stage 47 of [No rest for the wicked](../quests/Stanwickquest.md#stage-47))* → [brightport_oswald_selector](#d-brightport_oswald_selector)
    - “No, not really.” → [brightport_oswald6](#d-brightport_oswald6)

    <span id="d-oswald_start"></span>**`oswald_start`** Oswald: “Hey, stop running around my office! You're distracting me from my work.”

    - “Excuse me sir. I wish to help Stanwick by investigating the theft. Could you tell me more about it?” *(if reached stage 25 of [No rest for the wicked](../quests/Stanwickquest.md#stage-25))* → [brightport_oswald](#d-brightport_oswald)
    - “Excuse me sir. I was kicked out of the lecture room for misbehaving.” *(if reached stage 228 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-228))* → [brightport_oswald23](#d-brightport_oswald23)

    <span id="d-brightport_oswald_selector_lecture"></span>**`brightport_oswald_selector_lecture`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 97 of [No rest for the wicked](../quests/Stanwickquest.md#stage-97))* → [brightport_oswald24](#d-brightport_oswald24)
    - Next *(if reached stage 100 of [No rest for the wicked](../quests/Stanwickquest.md#stage-100))* → [brightport_oswald25](#d-brightport_oswald25)

    <span id="d-brightport_oswald14"></span>**`brightport_oswald14`** Oswald: “Before we discuss what is next. Have you learned who the culprit was?”

    - “It was my brother Andor. He stole it many months ago, and gave it away in exchange for forbidden knowledge.” *(if reached stage 132 of [Search for Andor](../quests/andor.md#stage-132))* → [brightport_oswald15](#d-brightport_oswald15)
    - “I prefer not to say, as it would cause trouble for the people who helped me.” → [brightport_oswald17](#d-brightport_oswald17)
    - “A former baker named Bryma was in possesion of it. I'm unaware of how she acquired it.” → [brightport_oswald16](#d-brightport_oswald16)
    - “Hey, I spent a lot of time to find it! Why did you burn it?” → [brightport_oswald3](#d-brightport_oswald3)

    <span id="d-brightport_oswald12"></span>**`brightport_oswald12`** [Dummy NPC](../monsters/none.md): “The Headmaster hurriedly grabs the scroll and opens it to confirm its contents. A moment later, he breathes a sigh of relief as he moves it over the flame of a nearby candle.” — **effects:** sets stage 85 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-85)

    - Next → [brightport_oswald13](#d-brightport_oswald13)

    <span id="d-brightport_oswald27"></span>**`brightport_oswald27`** Oswald: “No. But how would that pertain to your investigation?”

    - “Never mind, bye.” → *conversation ends*

    <span id="d-brightport_oswald26"></span>**`brightport_oswald26`** Oswald: “Is that so? Then focus on the matter at hand. Asking Frederich won't be of much use anyway. I have a hard time dealing with him myself.”


    <span id="d-brightport_oswald7"></span>**`brightport_oswald7`** Oswald: “I won't allow it. If this is as far as you go with the investigation, then so be it.” — **effects:** sets stage 46 of [No rest for the wicked](../quests/Stanwickquest.md#stage-46)

    - Next → [brightport_oswald8](#d-brightport_oswald8)

    <span id="d-brightport_oswald_selector"></span>**`brightport_oswald_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 80 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-80))* → [brightport_oswald9](#d-brightport_oswald9)
    - Next → [brightport_oswald10](#d-brightport_oswald10)

    <span id="d-brightport_oswald6"></span>**`brightport_oswald6`** Oswald: “I had no expectations of you in the first place. Now stroll along.”


    <span id="d-brightport_oswald"></span>**`brightport_oswald`** Oswald: “Forget it. That is none of your concern. What makes you think you should be involved?”

    - “It's unfair that Stanwick, whose name stands to suffer the most from the theft, was told to stay put.” → [brightport_oswald2](#d-brightport_oswald2)
    - “I made a deal with Stanwick. I scratch his back, and he scratches mine.” → [brightport_oswald1](#d-brightport_oswald1)
    - “Nothing. I wish to help out, from the kindness of my heart.” → [brightport_oswald0](#d-brightport_oswald0)

    <span id="d-brightport_oswald23"></span>**`brightport_oswald23`** Oswald: “This time I'll forgive it. But maybe next time I won't, so don't do it again!” — **effects:** clears stage 228 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-228)


    <span id="d-brightport_oswald24"></span>**`brightport_oswald24`** Oswald: “Serves you right, $playername, don't misbehave.”


    <span id="d-brightport_oswald25"></span>**`brightport_oswald25`** Oswald: “I permit you to go back, you're a good kid.” — **effects:** clears stage 228 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-228)

    - “I'll be back.” → *conversation ends*

    <span id="d-brightport_oswald15"></span>**`brightport_oswald15`** Oswald: “Your brother, you say... That is quite serious. I have heard from Dibella that you are searching for him. If you find him, you must put in every effort to persuade him to turn away from his malicious ways.”

    - Next → [brightport_oswald18](#d-brightport_oswald18)

    <span id="d-brightport_oswald17"></span>**`brightport_oswald17`** Oswald: “If that is what you say, then so be it. What matters is that the Achilles' heel of our academy was removed without further damage. This lack of oversight on my part will not be repeated.”

    - Next → [brightport_oswald18](#d-brightport_oswald18)

    <span id="d-brightport_oswald16"></span>**`brightport_oswald16`** Oswald: “As I suspected, it was someone interested in its contents. Anyhow, that name is of little importance to us now. The academy's priority should be increasing the security of the library, and we'll start by changing the archive's lock. [The…”

    - Next → [brightport_oswald18](#d-brightport_oswald18)

    <span id="d-brightport_oswald3"></span>**`brightport_oswald3`** Oswald: “If the lord in charge of Brightport had learned what was on that scroll, we would have been accused of treason, and heads would've rolled. This was for the best. And thanks to you, it's all behind us now.”

    - Next → [brightport_oswald18](#d-brightport_oswald18)

    <span id="d-brightport_oswald8"></span>**`brightport_oswald8`** [Dummy NPC](../monsters/none.md): “You notice a key on a shelf under the desk. If he were distracted for a moment you could steal it.” — **effects:** sets stage 75 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-75)

    - “[I should distract him.]” → *conversation ends*
    - “[There has to be a different way.]” → *conversation ends*

    <span id="d-brightport_oswald9"></span>**`brightport_oswald9`** Oswald: “[The headmaster looks in the direction of the window. For a moment he is distracted.]” — **effects:** sets stage 80 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-80)

    - “[Grab the key.]” → [brightport_oswald11](#d-brightport_oswald11)

    <span id="d-brightport_oswald10"></span>**`brightport_oswald10`** Oswald: “I won't fall for the same joke twice. Find something better to do with your time.”


    <span id="d-brightport_oswald2"></span>**`brightport_oswald2`** Oswald: “I admit that this decision might put Stanwick's future employment in Nor City at risk. But the safety of the academy comes first. I am sure Stanwick is innocent, but we can never be too careful when it comes to matters like this. Do you…”

    - “Yes, it was a reasonable action.” → [brightport_oswald4](#d-brightport_oswald4)
    - “That still doesn't make it right.” → [brightport_oswald5](#d-brightport_oswald5)

    <span id="d-brightport_oswald1"></span>**`brightport_oswald1`** Oswald: “Those who are eager to help with nothing to gain are usually the most vicious bunch. At least I can take your word on that.”

    - Next → [brightport_oswald2](#d-brightport_oswald2)

    <span id="d-brightport_oswald0"></span>**`brightport_oswald0`** Oswald: “You sound like trouble. Take my advice and stick your nose somewhere else.”


    <span id="d-brightport_oswald18"></span>**`brightport_oswald18`** Oswald: “And now on the matter of Stanwick. The academy will release him, with an apology letter, and I will personally make sure this had no lasting impact on his reputation. Please tell him that he is free to leave his room.” — **effects:** sets stage 96 of [No rest for the wicked](../quests/Stanwickquest.md#stage-96)

    - Next → [brightport_oswald21](#d-brightport_oswald21)

    <span id="d-brightport_oswald11"></span>**`brightport_oswald11`** Oswald: “That's not funny. There is nothing there.” — **effects:** gives 1× [Library key](../items/brightport_key.md), sets stage 47 of [No rest for the wicked](../quests/Stanwickquest.md#stage-47)

    - “It was probably a bird. It must have flown away.” → *conversation ends*
    - “At your age, poor eyesight's not uncommon.” → *conversation ends*

    <span id="d-brightport_oswald4"></span>**`brightport_oswald4`** Oswald: “Very well, then. I accept your assistance on this matter. Report back to me on your findings.” — **effects:** sets stage 35 of [No rest for the wicked](../quests/Stanwickquest.md#stage-35)


    <span id="d-brightport_oswald5"></span>**`brightport_oswald5`** Oswald: “Then you have some growing up to do.”


    <span id="d-brightport_oswald21"></span>**`brightport_oswald21`** Oswald: “Oh, and I almost forgot...”

    - Next → [brightport_oswald19](#d-brightport_oswald19)

    <span id="d-brightport_oswald19"></span>**`brightport_oswald19`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 47 of [No rest for the wicked](../quests/Stanwickquest.md#stage-47))* → [brightport_oswald20](#d-brightport_oswald20)
    - Next *(if reached stage 47 of [No rest for the wicked](../quests/Stanwickquest.md#stage-47))* → [brightport_oswald22](#d-brightport_oswald22)

    <span id="d-brightport_oswald20"></span>**`brightport_oswald20`** Oswald: “Please have these Deerskin gloves as a sign of my gratitude. Those are as sturdy as leather can be.” — **effects:** gives 1× [Deerskin gloves](../items/brightportgloves.md), sets stage 100 of [No rest for the wicked](../quests/Stanwickquest.md#stage-100)

    - Next → [brighhtport_oswald23](#d-brighhtport_oswald23)

    <span id="d-brightport_oswald22"></span>**`brightport_oswald22`** Oswald: “Stealing the key was not very nice of you. Consider your reward the fact that I overlooked it this time.” — **effects:** sets stage 97 of [No rest for the wicked](../quests/Stanwickquest.md#stage-97)

    - Next → [brighhtport_oswald23](#d-brighhtport_oswald23)

    <span id="d-brighhtport_oswald23"></span>**`brighhtport_oswald23`** Oswald: “Good luck on your search. Bye.”




## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 36 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightportnpc6` |
    | Spawn group | `brightportnpc6` |
    | Loot table | – |
    | Conversation | `oswald_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:56` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportnpc6",
     "name": "Oswald",
     "iconID": "monsters_ld1:56",
     "unique": 1,
     "phraseID": "oswald_selector"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
