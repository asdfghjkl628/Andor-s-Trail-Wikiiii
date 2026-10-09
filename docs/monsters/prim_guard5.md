---
description: "Prim guard captain is a non-player character (NPC) in Andor's Trail, found in Prim."
---

# ![](../assets/icons/monsters/monsters_rltiles1_65.png){ .sprite } Prim guard captain

**Where to find Prim guard captain:** Prim: [Blackwater mountain 29](../maps/blackwater_mountain29.md#pin-npc-prim_guard5)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_65.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Prim |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

## Quests

- [Climbing up is forbidden](../quests/Omi2_bwm1.md): stages 9, 40
- [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md): stages 18, 43

## Dialogue simulator

Set your quest stages and items, then talk to Prim guard captain. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/prim_guard5_s.json" data-npc="Prim guard captain" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (64 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-prim_guard5_s"></span>**`prim_guard5_s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 43 of [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-43))* → [capvjern_41](#d-capvjern_41)
    - branch 2 *(if reached stage 56 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-56); reached stage 18 of [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-18))* → [capvjern_23](#d-capvjern_23)
    - branch 3 *(if reached stage 40 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-40))* → [capvjern_22](#d-capvjern_22)
    - branch 4 *(if reached stage 18 of [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-18))* → [capvjern_15](#d-capvjern_15)
    - branch 5 *(if reached stage 17 of [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-17))* → [capvjern_1](#d-capvjern_1)
    - branch 6 → [prim_guard5_1](#d-prim_guard5_1)

    <span id="d-capvjern_41"></span>**`capvjern_41`** [Prim guard captain](../monsters/prim_guard5.md): “I'll wait here. Farewell, $playername.”

    - “Bye.” → *conversation ends*
    - “Shadow be with you.” → *conversation ends*
    - “As useful as always, captain.” → *conversation ends*

    <span id="d-capvjern_23"></span>**`capvjern_23`** [Prim guard captain](../monsters/prim_guard5.md): “Hey, $playername! You're back, where is the general?”

    - Next → [capvjern_24](#d-capvjern_24)

    <span id="d-capvjern_22"></span>**`capvjern_22`** Prim guard captain: “$playername, you must reach Blackwater Settlement and get help from General Ortholion.”

    - “OK, bye.” → *conversation ends*
    - “Shadow be with you.” → *conversation ends*

    <span id="d-capvjern_15"></span>**`capvjern_15`** [Prim guard captain](../monsters/prim_guard5.md): “We're short of men, and we don't even know where he is right now. *Meanwhile Jern stares at you.*” — **effects:** sets stage 18 of [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-18)

    - “I don't know!” → [capvjern_16a](#d-capvjern_16a)
    - “I can't be of help this time...” → [capvjern_16b](#d-capvjern_16b)

    <span id="d-capvjern_1"></span>**`capvjern_1`** [Jern](../monsters/prim_bar_regular.md): “C'mon! Dare to raise your sword! You! You left my partners to DIE!” — **effects:** removes monsters from blackwater_mountain22, spawns monsters on blackwater_mountain29

    - Next → [capvjern_2](#d-capvjern_2)

    <span id="d-prim_guard5_1"></span>**`prim_guard5_1`** Prim guard captain: “This is no place for kids.”

    - “I will report your bad manners to your chief.” → *conversation ends*
    - “I might have some information about the recent disappearances.” → [prim_guard5_2](#d-prim_guard5_2)

    <span id="d-capvjern_24"></span>**`capvjern_24`** [Jern](../monsters/prim_bar_regular.md): “It sure took you a while. What happened?”

    - “General Ortholion was almost murdered by Ehrenfest, but I was there to save him.” → [capvjern_25a](#d-capvjern_25a)
    - “I killed Kamelio. Twice.” → [capvjern_25b](#d-capvjern_25b)

    <span id="d-capvjern_16a"></span>**`capvjern_16a`** [Prim guard captain](../monsters/prim_guard5.md): “Do you remember anything out of the ordinary?”

    - “He's been shady since the very beginning.” → [capvjern_17a](#d-capvjern_17a)
    - “No...Apart from his need to not be heard by the Feygard soldiers.” → [capvjern_17b](#d-capvjern_17b)

    <span id="d-capvjern_16b"></span>**`capvjern_16b`** [Jern](../monsters/prim_bar_regular.md): “Or maybe yes.”

    - Next → [capvjern_16a](#d-capvjern_16a)

    <span id="d-capvjern_2"></span>**`capvjern_2`** [Prim guard captain](../monsters/prim_guard5.md): “Stop, OK?! I'm really sorry, Jern! *sheathes his sword* We were scared. That's all, OK?! Gornauds have been decimating us while you were in the tavern day and night.”

    - Next → [capvjern_3](#d-capvjern_3)

    <span id="d-prim_guard5_2"></span>**`prim_guard5_2`** Prim guard captain: “Yeah, we already know about the gornauds.”

    - “No, I did not mean...” → [prim_guard5_3a](#d-prim_guard5_3a)
    - “The gornauds?” → [prim_guard5_3b](#d-prim_guard5_3b)

    <span id="d-capvjern_25a"></span>**`capvjern_25a`** [Prim guard captain](../monsters/prim_guard5.md): “You sure are brave enough, kid. I hope you'll be staying around for a while.”

    - “Eh...” → [capvjern_26a](#d-capvjern_26a)
    - “I don't think the job is paid well enough.” → [capvjern_26a](#d-capvjern_26a)
    - “Sorry, but I must do as I was told and find my brother Andor.” → [capvjern_26a](#d-capvjern_26a)

    <span id="d-capvjern_25b"></span>**`capvjern_25b`** Prim guard captain: “You WHAT?!”

    - “Hey, hey, calm down big man! Let me explain.” → [capvjern_26c](#d-capvjern_26c)
    - “I had no other choice.” → [capvjern_26b](#d-capvjern_26b)

    <span id="d-capvjern_17a"></span>**`capvjern_17a`** Prim guard captain: “Anything more specific?”

    - “Give me some time to remember.” → [capvjern_18a](#d-capvjern_18a)
    - “Umm...No, but I think he was scared of Feygard soldiers hearing our conversation.” → [capvjern_17b](#d-capvjern_17b)

    <span id="d-capvjern_17b"></span>**`capvjern_17b`** Prim guard captain: “I see...Feygard soldiers.”

    - Next → [capvjern_18b](#d-capvjern_18b)

    <span id="d-capvjern_3"></span>**`capvjern_3`** [Jern](../monsters/prim_bar_regular.md): “Ah! Now your incompetence is my fault?”

    - Next → [capvjern_4](#d-capvjern_4)

    <span id="d-prim_guard5_3a"></span>**`prim_guard5_3a`** Prim guard captain: “Look, I have more important things to do than babysitting a kid, OK?” — **effects:** sets stage 9 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-9)

    - “Bye.” → *conversation ends*
    - “Hmpf, when the gornauds get the village surrounded I'll be the one babysitting all of you.” → *conversation ends*

    <span id="d-prim_guard5_3b"></span>**`prim_guard5_3b`** Prim guard captain: “Yes. They seem to be learning from every attack and their numbers are increasing.”

    - “Can I help?” → [prim_guard5_4](#d-prim_guard5_4)
    - “Will you hear what I have to say then?” → [prim_guard5_3a](#d-prim_guard5_3a)

    <span id="d-capvjern_26a"></span>**`capvjern_26a`** [Jern](../monsters/prim_bar_regular.md): “Ha HA! You want the kid to do your job for free? You see, $playername? We have not even begun clearing the mountain entrance. I wonder why!”

    - “Do you need any help with that?” → [capvjern_27a](#d-capvjern_27a)

    <span id="d-capvjern_26c"></span>**`capvjern_26c`** Prim guard captain: “Explain, explain it already!”

    - Next → [capvjern_26b](#d-capvjern_26b)

    <span id="d-capvjern_26b"></span>**`capvjern_26b`** [Prim guard captain](../monsters/prim_guard5.md): “Calm down, Jern. Kamelio, alive? How? Where?”

    - “Deep in a cave below the Elm mine.” → [capvjern_27b](#d-capvjern_27b)

    <span id="d-capvjern_18a"></span>**`capvjern_18a`** [Jern](../monsters/prim_bar_regular.md): “Don't worry, We'll talk later.”


    <span id="d-capvjern_18b"></span>**`capvjern_18b`** [Jern](../monsters/prim_bar_regular.md): “Asking for their help seems not to be the worst idea right now.”

    - “Yes.” → [capvjern_19](#d-capvjern_19)
    - “Maybe...” → [capvjern_19](#d-capvjern_19)
    - “Are you sure?” → [capvjern_19](#d-capvjern_19)

    <span id="d-capvjern_4"></span>**`capvjern_4`** [Prim guard captain](../monsters/prim_guard5.md): “*raises his hands* Drop it already! We're getting more and more surrounded by those beasts, you know? Right now there's no point to worrying about somebody who fell off the mountain!”

    - Next → [capvjern_5](#d-capvjern_5)

    <span id="d-prim_guard5_4"></span>**`prim_guard5_4`** Prim guard captain: “Of course you can. Go back home and let me and the rest do our job. Understood?”

    - “But I have important information!” → [prim_guard5_3a](#d-prim_guard5_3a)
    - “Whatever, you won't stand up after a Gornaud blow.” → *conversation ends*
    - “Understood, bye.” → *conversation ends*

    <span id="d-capvjern_27a"></span>**`capvjern_27a`** [Prim guard captain](../monsters/prim_guard5.md): “We have more important matters to attend. Now, where is the general? What about the workers of the mine?”

    - “Uh ... The general will certainly let you know in full detail ... Soon enough.” → [capvjern_28c](#d-capvjern_28c)
    - “No survivors, except Arghest. Many Feygard soldiers have fallen too.” → [capvjern_28b](#d-capvjern_28b)

    <span id="d-capvjern_27b"></span>**`capvjern_27b`** [Jern](../monsters/prim_bar_regular.md): “For the Shadow, tell me why you had to kill my beloved friend!!”

    - “It was me or him. He was no longer your friend.” → [capvjern_28d](#d-capvjern_28d)
    - “I am truly sorry, but he did try to kill us too.” → [capvjern_28a](#d-capvjern_28a)

    <span id="d-capvjern_19"></span>**`capvjern_19`** [Prim guard captain](../monsters/prim_guard5.md): “That's right. But I feel that's what they wanted since the very beginning.”

    - Next → [capvjern_20](#d-capvjern_20)

    <span id="d-capvjern_5"></span>**`capvjern_5`** [Jern](../monsters/prim_bar_regular.md): “Are you out of your mind? Lorn would never have died from something like that!”

    - Next → [capvjern_6](#d-capvjern_6)

    <span id="d-capvjern_28c"></span>**`capvjern_28c`** [Prim guard captain](../monsters/prim_guard5.md): “We will wait for him here, in that case.”

    - Next → [capvjern_29c](#d-capvjern_29c)

    <span id="d-capvjern_28b"></span>**`capvjern_28b`** Prim guard captain: “Anything else?”

    - “General Ortholion is inside the mine dependencies. I found Kamelio, he tried to kill us but I defeated him.” → [capvjern_28a](#d-capvjern_28a)
    - “You better ask the general, I am tired already. He is still in the Elm mine celebrating he's still alive.” → [capvjern_28c](#d-capvjern_28c)

    <span id="d-capvjern_28d"></span>**`capvjern_28d`** Prim guard captain: “You or ...? That's utter nonsense!”

    - Next → [capvjern_28a](#d-capvjern_28a)

    <span id="d-capvjern_28a"></span>**`capvjern_28a`** [Prim guard captain](../monsters/prim_guard5.md): “That's absurd! Kamelio?! Trying to kill a kid? Be reasonable, $playername. We cannot simply believe that.”

    - “Kamelio was no longer the person you knew.” → [capvjern_29b](#d-capvjern_29b)
    - “General Ortholion was there.” → [capvjern_29a](#d-capvjern_29a)

    <span id="d-capvjern_20"></span>**`capvjern_20`** [Jern](../monsters/prim_bar_regular.md): “$playername, what do you think? This is probably our best bet.”

    - “I'm gonna rest for a while. See you later.” → *conversation ends*
    - “I will warn the general then.” → [capvjern_21](#d-capvjern_21)

    <span id="d-capvjern_6"></span>**`capvjern_6`** [Prim guard captain](../monsters/prim_guard5.md): “How can you be so sure? Accidents happen! He could have fallen off during an attack or a rock slide.”

    - Next → [capvjern_7](#d-capvjern_7)

    <span id="d-capvjern_29c"></span>**`capvjern_29c`** [Jern](../monsters/prim_bar_regular.md): “Speak for yourself, cap! I'll head to the mine.”

    - “You are needed here more.” → [capvjern_30c](#d-capvjern_30c)
    - “The mine is no longer a safe place.” → [capvjern_30d](#d-capvjern_30d)

    <span id="d-capvjern_29b"></span>**`capvjern_29b`** Prim guard captain: “I cannot believe in your words, $playername.”

    - Next → [capvjern_30b](#d-capvjern_30b)

    <span id="d-capvjern_29a"></span>**`capvjern_29a`** [Jern](../monsters/prim_bar_regular.md): “So? You want me to believe that Kamelio went crazy and tried to kill you?”

    - “Believe what you want. I give up.” → *conversation ends*
    - “I am not lying!” → [capvjern_29a](#d-capvjern_29a)
    - “This is his cloak, right? [Show the Kazarite cloak]” *(if carry 1× [Kazarite cloak](../items/kamelio_drop3.md))* → [capvjern_30a](#d-capvjern_30a)

    <span id="d-capvjern_21"></span>**`capvjern_21`** [Prim guard captain](../monsters/prim_guard5.md): “It's settled then. We will spread the word among the guards.” — **effects:** sets stage 40 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-40)

    - “Great. Shadow be with you.” → *conversation ends*
    - “We'll meet soon, then.” → *conversation ends*

    <span id="d-capvjern_7"></span>**`capvjern_7`** [Prim guard captain](../monsters/prim_guard5.md): “That is what the guy who reported it told me, too! Now I'm starting to welcome those Feygard guys. There aren't attacks anymore since they guard the village.”

    - Next → [capvjern_8](#d-capvjern_8)

    <span id="d-capvjern_30c"></span>**`capvjern_30c`** [Jern](../monsters/prim_bar_regular.md): “Hmpf ... You know what? Right, someone has to patrol this settlement.”

    - Next → [capvjern_31a](#d-capvjern_31a)

    <span id="d-capvjern_30d"></span>**`capvjern_30d`** [Prim guard captain](../monsters/prim_guard5.md): “I can believe that. Jern, let Feygard folks take care of the mine for a while, we have a lot to do here.”

    - Next → [capvjern_30c](#d-capvjern_30c)

    <span id="d-capvjern_30b"></span>**`capvjern_30b`** Prim guard captain: “But the truth is that I can neither believe you killed him for the sake of it. Plus, the General is alive as you say, and it is thanks to you.”

    - Next → [capvjern_29a](#d-capvjern_29a)

    <span id="d-capvjern_30a"></span>**`capvjern_30a`** [Prim guard captain](../monsters/prim_guard5.md): “What in the world ...? It moves!”

    - “Yes. This strange substance was responsible of your friend's behaviour.” → [capvjern_31b](#d-capvjern_31b)
    - “Do you believe me now?” → [capvjern_31b](#d-capvjern_31b)

    <span id="d-capvjern_8"></span>**`capvjern_8`** [Jern](../monsters/prim_bar_regular.md): “Eh?! What Feyga...”

    - “Who told you that?” → [capvjern_9](#d-capvjern_9)

    <span id="d-capvjern_31a"></span>**`capvjern_31a`** Prim guard captain: “Take this old key. I used to work in the mines when I was younger. I am sure there was a supply chest somewhere inside.”

    - Next → [capvjern_32a](#d-capvjern_32a)

    <span id="d-capvjern_31b"></span>**`capvjern_31b`** [Jern](../monsters/prim_bar_regular.md): “[staring at the cloak] I have never seen this before. Not even when I used to work there. What in the world is this?”

    - Next → [capvjern_32b](#d-capvjern_32b)

    <span id="d-capvjern_9"></span>**`capvjern_9`** [Prim guard captain](../monsters/prim_guard5.md): “*stares at you* What the hell kid? Why're you here again?”

    - Next → [capvjern_10](#d-capvjern_10)

    <span id="d-capvjern_32a"></span>**`capvjern_32a`** [Jern](../monsters/prim_bar_regular.md): “Thank you again. *looks at the captain* I'll be going.” — **effects:** gives 1× [Rusted key](../items/elm2_key.md), removes monsters from blackwater_mountain29, sets stage 43 of [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-43)

    - “Shadow be with you.” → *NPC leaves*
    - “Good luck in your shift.” → *NPC leaves*
    - “Bye.” → *NPC leaves*

    <span id="d-capvjern_32b"></span>**`capvjern_32b`** [Prim guard captain](../monsters/prim_guard5.md): “[looks at you]”

    - Next → [capvjern_33](#d-capvjern_33)

    <span id="d-capvjern_10"></span>**`capvjern_10`** [Jern](../monsters/prim_bar_regular.md): “Hey, show some respect. This youngster dared to go where you didn't. He told me what happened, too.”

    - Next → [capvjern_11](#d-capvjern_11)

    <span id="d-capvjern_33"></span>**`capvjern_33`** Prim guard captain: “[stares at the cloak again]”

    - Next → [capvjern_34](#d-capvjern_34)

    <span id="d-capvjern_11"></span>**`capvjern_11`** [Prim guard captain](../monsters/prim_guard5.md): “*puts on an exhausted face* Whatever...I don't know his name. Just another one of the very few visitors we receive here. He was wearing a blue cloak, I think.”

    - “Ehrenfest!” → [capvjern_12](#d-capvjern_12)

    <span id="d-capvjern_34"></span>**`capvjern_34`** Prim guard captain: “[stares at you again]”

    - “What ...?” → [capvjern_35](#d-capvjern_35)
    - “You alright?” → [capvjern_35](#d-capvjern_35)

    <span id="d-capvjern_12"></span>**`capvjern_12`** [Jern](../monsters/prim_bar_regular.md): “The shady guy, isn't it?”

    - “He lied to me again!” → [capvjern_13](#d-capvjern_13)

    <span id="d-capvjern_35"></span>**`capvjern_35`** [Jern](../monsters/prim_bar_regular.md): “[puts his hand over the captain's shoulder] Hey, captain, wake up.”

    - “[Put the cloak away]” → [capvjern_36](#d-capvjern_36)

    <span id="d-capvjern_13"></span>**`capvjern_13`** [Prim guard captain](../monsters/prim_guard5.md): “This is serious. That guy might be behind the disappearances.”

    - “He has been in the mine during these last few days.” → [capvjern_14](#d-capvjern_14)

    <span id="d-capvjern_36"></span>**`capvjern_36`** [Prim guard captain](../monsters/prim_guard5.md): “... It is un...unbearable.”

    - Next → [capvjern_37](#d-capvjern_37)

    <span id="d-capvjern_14"></span>**`capvjern_14`** [Jern](../monsters/prim_bar_regular.md): “We should look for him. This Ehrenfest guy needs to clear up many things.”

    - Next → [capvjern_15](#d-capvjern_15)

    <span id="d-capvjern_37"></span>**`capvjern_37`** Prim guard captain: “[breathing heavily] That ... that substance is dangerous! $playername, you must destroy the cloak!”

    - “The mine is full of it! Do you believe me now?” → [capvjern_38](#d-capvjern_38)

    <span id="d-capvjern_38"></span>**`capvjern_38`** Prim guard captain: “I do. [looks at Jern] I do believe in what the kid says.”

    - Next → [capvjern_39](#d-capvjern_39)

    <span id="d-capvjern_39"></span>**`capvjern_39`** [Jern](../monsters/prim_bar_regular.md): “Grgh ... Let's go to the mine, then. We must take Kamelio's corpse from there and give it a proper burial!”

    - “It is too dangerous, you mustn't go.” → [capvjern_40](#d-capvjern_40)
    - “Trained soldiers were lost down there. Let General's men handle this.” → [capvjern_40](#d-capvjern_40)

    <span id="d-capvjern_40"></span>**`capvjern_40`** Prim guard captain: “So you suggest what? Staying here doing nothing!? I am NOT leaving my friend's corpse there.”

    - “What about those who are alive here?” → [capvjern_30c](#d-capvjern_30c)
    - “Do not lose your life for a bunch of dead bones. You must live for your friends.” → [capvjern_30c](#d-capvjern_30c)



## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added<br>Dialogue: 31 lines added |
| [v0.8.8](../versions/0.8.8.md) | Dialogue: 33 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `prim_guard5` |
    | Type (wiki) | NPC |
    | Spawn group | `prim_guard5` |
    | Loot table | – |
    | Conversation | `prim_guard5_s` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:65` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "prim_guard5",
     "name": "Prim guard captain",
     "iconID": "monsters_rltiles1:65",
     "monsterClass": "humanoid",
     "spawnGroup": "prim_guard5",
     "phraseID": "prim_guard5_s"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_guard5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_guard5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_guard5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_guard5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
