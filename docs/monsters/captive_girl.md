---
description: "Emmeline is a non-player character (NPC) in Andor's Trail, found in Flagstone Prison."
---

# ![](../assets/icons/monsters/monsters_ld1_220.png){ .sprite } Emmeline

**Where to find Emmeline:** Flagstone Prison: [Lake shore road 1](../maps/lake_shore_road_1.md#pin-npc-captive_girl)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_220.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Flagstone Prison |
| **Entry ID** | `captive_girl` |
| **Introduced** | [v0.8.8](../versions/0.8.8.md) |

</div>

## Quests

- [A Wicked witch](../quests/wicked_witch.md): stages 80, 85, 90, 95, 96
- [Sutdover story flags (hidden flag)](../quests/sutdover_hidden.md): stage 1

## Dialogue simulator

Set your quest stages and items, then talk to Emmeline. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/captive_girl_selector.json" data-npc="Emmeline" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (19 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-captive_girl_selector"></span>**`captive_girl_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 90 of [A Wicked witch](../quests/wicked_witch.md#stage-90); NOT reached stage 95 of [A Wicked witch](../quests/wicked_witch.md#stage-95); NOT reached stage 96 of [A Wicked witch](../quests/wicked_witch.md#stage-96))* → [captive_girl_10](#d-captive_girl_10)
    - Next *(if latest stage of [A Wicked witch](../quests/wicked_witch.md#stage-90) is 90)* → [captive_girl_50](#d-captive_girl_50)
    - Next *(if reached stage 95 of [A Wicked witch](../quests/wicked_witch.md#stage-95))* → [captive_girl_75](#d-captive_girl_75)
    - Next → [captive_girl_31](#d-captive_girl_31)

    <span id="d-captive_girl_10"></span>**`captive_girl_10`** Emmeline: “Excuse me, young one! Wait! Thank you for sparing me earlier. You've shown true compassion.”

    - “What ... do I know you? You're just a young girl?” → [captive_girl_20](#d-captive_girl_20)

    <span id="d-captive_girl_50"></span>**`captive_girl_50`** Emmeline: “I really need to get my hands on a lot of those 'Tonic of Blood' potions. Can you help me? I need a lot.” — **effects:** sets stage 85 of [A Wicked witch](../quests/wicked_witch.md#stage-85)

    - “Well, I have twenty-five of those for you.” *(if hand over 25× [Tonic of blood](../items/tonic_of_blood.md))* → [captive_girl_71](#d-captive_girl_71)
    - “Well, I have twenty of those for you.” *(if carry 20× [Tonic of blood](../items/tonic_of_blood.md); NOT carry 25× [Tonic of blood](../items/tonic_of_blood.md))* → [captive_girl_54](#d-captive_girl_54)
    - “Well, I have ten of those for you.” *(if carry 10× [Tonic of blood](../items/tonic_of_blood.md); NOT carry 20× [Tonic of blood](../items/tonic_of_blood.md))* → [captive_girl_56](#d-captive_girl_56)
    - “Well, I have five of those for you and I'm not sure where I got them. Do you know where I can get some?” *(if carry 5× [Tonic of blood](../items/tonic_of_blood.md); NOT carry 10× [Tonic of blood](../items/tonic_of_blood.md))* → [captive_girl_56](#d-captive_girl_56)
    - “Well, I only have one of those for you and I don't remember where I got it. Do you know where I can get some more?” *(if carry 1× [Tonic of blood](../items/tonic_of_blood.md); NOT carry 5× [Tonic of blood](../items/tonic_of_blood.md))* → [captive_girl_56](#d-captive_girl_56)
    - “I'm sorry, but I don't have any of those.” *(if NOT carry 1× [Tonic of blood](../items/tonic_of_blood.md))* → [captive_girl_56](#d-captive_girl_56)

    <span id="d-captive_girl_75"></span>**`captive_girl_75`** Emmeline: “Before you go, I was able to steal this from the witch as I was escaping. I want you to have it. I need to go now.” — **effects:** gives [Enchanted evergreen rod](../items/witch_scepter.md), removes monsters from lake_shore_road_1


    <span id="d-captive_girl_31"></span>**`captive_girl_31`** Emmeline: “Thank you again, my savior! I will go now.”

    - Next → *NPC leaves*

    <span id="d-captive_girl_20"></span>**`captive_girl_20`** Emmeline: “Yes, I was under a spell that made me appear as the witch. She wanted to test your heart. I'm glad you proved kind.” — **effects:** sets stage 80 of [A Wicked witch](../quests/wicked_witch.md#stage-80), sets stage 1 of [Sutdover story flags (hidden flag)](../quests/sutdover_hidden.md#stage-1), spawns monsters on lake_shore_road_0, changes map lake_shore_road_0

    - “Thank you, but you don't look well.” → [captive_girl_30](#d-captive_girl_30)

    <span id="d-captive_girl_71"></span>**`captive_girl_71`** Emmeline: “WOW! You actually managed to find twenty-five! I am so grateful.” — **effects:** sets stage 95 of [A Wicked witch](../quests/wicked_witch.md#stage-95)

    - Next → [captive_girl_75](#d-captive_girl_75)

    <span id="d-captive_girl_54"></span>**`captive_girl_54`** Emmeline: “Only twenty? I was really hoping for twenty-five.”

    - “Whatever! Fine. I will go get you five more.” → *conversation ends*
    - “I know that you "asked" for twenty-five, but I have twenty and they are hard to get. Please take these.” *(if hand over 20× [Tonic of blood](../items/tonic_of_blood.md))* → [captive_girl_70](#d-captive_girl_70)

    <span id="d-captive_girl_56"></span>**`captive_girl_56`** Emmeline: “Can you get me twenty-five of them?”

    - “Where can I get some?” → [captive_girl_55](#d-captive_girl_55)

    <span id="d-captive_girl_30"></span>**`captive_girl_30`** Emmeline: “I am not well. Which is why I have not run far from this awful place and this awful witch.”

    - “What's wrong? Why can't you leave?” → [captive_girl_35](#d-captive_girl_35)
    - “What happened to you here? How did you get here?” → [captive_girl_35a](#d-captive_girl_35a)

    <span id="d-captive_girl_70"></span>**`captive_girl_70`** Emmeline: “OK. I won't make you go back just for five more when you've already brought me twenty.” — **effects:** sets stage 96 of [A Wicked witch](../quests/wicked_witch.md#stage-96)

    - Next → [captive_girl_76](#d-captive_girl_76)

    <span id="d-captive_girl_55"></span>**`captive_girl_55`** Emmeline: “Well, I am not exactly sure about that as the witch would make it. Damn! I hate that smell. Damn! I love that taste however.”

    - “Can you help me out a little bit? Do you know anything about them?” → [captive_girl_60](#d-captive_girl_60)

    <span id="d-captive_girl_35"></span>**`captive_girl_35`** Emmeline: “I need nutrients! You see, I've been held down in that basement of that horrific house for what feels like a year.”

    - Next → [captive_girl_40](#d-captive_girl_40)

    <span id="d-captive_girl_35a"></span>**`captive_girl_35a`** Emmeline: “I am too sick to talk about this right now.”

    - Next → [captive_girl_35](#d-captive_girl_35)

    <span id="d-captive_girl_76"></span>**`captive_girl_76`** Emmeline: “I need to go now. Thanks a lot.” — **effects:** removes monsters from lake_shore_road_1


    <span id="d-captive_girl_60"></span>**`captive_girl_60`** Emmeline: “Hold on. Let me think....”

    - Next → [captive_girl_65](#d-captive_girl_65)

    <span id="d-captive_girl_40"></span>**`captive_girl_40`** Emmeline: “All the witch ever gave me is something called 'Tonic of Blood'. At first, I refused to drink it, but soon I became desperate and I drank it.”

    - “I've had one or two of those. They are not that bad.” *(if used 1× [Tonic of blood](../items/tonic_of_blood.md))* → [captive_girl_45](#d-captive_girl_45)
    - “Are those things even good for you?” *(if NOT used 1× [Tonic of blood](../items/tonic_of_blood.md))* → [captive_girl_45](#d-captive_girl_45)

    <span id="d-captive_girl_65"></span>**`captive_girl_65`** Emmeline: “Ah, YES. I remember her saying that an "undead" friend of her's east of here taught her how to make them.” — **effects:** sets stage 90 of [A Wicked witch](../quests/wicked_witch.md#stage-90)

    - “OK. Stay here. I will be back with more of them.” → *conversation ends*

    <span id="d-captive_girl_45"></span>**`captive_girl_45`** Emmeline: “Yes, maybe in moderation. But after a few dozen, they do something to your body as I can no longer consume anything but them.”

    - Next → [captive_girl_50](#d-captive_girl_50)



## Version history

| Version | Change |
|---|---|
| [v0.8.8](../versions/0.8.8.md) | Added<br>Dialogue: 19 lines added |
| [v0.8.9](../versions/0.8.9.md) | Dialogue: 2 lines changed<br>· text: “Ah, YES. I remember her saying that an "undead" friend of her's east …” → “Ah, YES. I remember her saying that an "undead" friend of her's east …” |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 1 line changed<br>· text: “Well, I am not eactly sure about that as the witch would make it. Dam…” → “Well, I am not exactly sure about that as the witch would make it. Da…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `captive_girl` |
    | Spawn group | `captive_girl` |
    | Loot table | – |
    | Conversation | `captive_girl_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:220` |
    | Defined in | `res/raw/monsterlist_mt_galmore.json` |

    Raw data:

    ```json
    {
     "id": "captive_girl",
     "name": "Emmeline",
     "iconID": "monsters_ld1:220",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "captive_girl_selector"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=captive_girl.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=captive_girl.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=captive_girl.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=captive_girl.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
