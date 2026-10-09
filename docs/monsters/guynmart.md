---
description: "Guynmart is a non-player character (NPC) in Andor's Trail, found in Guynmart Castle."
---

# ![](../assets/icons/monsters/monsters_tometik1_2.png){ .sprite } Guynmart

**Where to find Guynmart:** Guynmart Castle: [Guynmart main 0](../maps/guynmart_main_0.md#pin-npc-guynmart)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik1_2.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Guynmart Castle |
| **Entry ID** | `guynmart` |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Quests

- [Roses](../quests/guynmart.md): stages 160, 161, 162
- [Search for Andor](../quests/andor.md): stages 90, 92

## Dialogue simulator

Set your quest stages and items, then talk to Guynmart. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_10.json" data-npc="Guynmart" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (37 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_10"></span>**`guynmart_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 162 of [Roses](../quests/guynmart.md#stage-162))* → [guynmart_200](#d-guynmart_200)
    - branch 2 *(if reached stage 161 of [Roses](../quests/guynmart.md#stage-161))* → [guynmart_250](#d-guynmart_250)
    - branch 3 → [guynmart_12](#d-guynmart_12)

    <span id="d-guynmart_200"></span>**`guynmart_200`** [Guynmart](../monsters/guynmart.md): “[Groaning] ...open the gate...”

    - Next → [guynmart_210](#d-guynmart_210)

    <span id="d-guynmart_250"></span>**`guynmart_250`** [Guynmart](../monsters/guynmart.md): “[Groaning]”


    <span id="d-guynmart_12"></span>**`guynmart_12`** Guynmart: “Who is there?”

    - “A friend.” → [guynmart_20](#d-guynmart_20)

    <span id="d-guynmart_210"></span>**`guynmart_210`** [Guynmart](../monsters/guynmart.md): “...then go ... to Rhodita...”


    <span id="d-guynmart_20"></span>**`guynmart_20`** Guynmart: “Good. At last. Go and bring Norgothla here.”

    - “Norgothla is out in the woods and awaits you there with his men. Unkorh persuaded him that you commanded that.” → [guynmart_30](#d-guynmart_30)

    <span id="d-guynmart_30"></span>**`guynmart_30`** Guynmart: “Unkorh! I curse the day when I made him my steward.”

    - “How can I help you now? Shall I search for the keys to your cell?” → [guynmart_40](#d-guynmart_40)

    <span id="d-guynmart_40"></span>**`guynmart_40`** Guynmart: “No time for that. I am too weak to be of much help. We need Norgothla now.”

    - “Lovis is on his way to him. He can probably persuade Norgothla to come to the castle.” → [guynmart_50](#d-guynmart_50)

    <span id="d-guynmart_50"></span>**`guynmart_50`** Guynmart: “Good. Norgothla knows and trusts him. Tell me - is the main gate shut?”

    - “Yes. I came through the garden door.” → [guynmart_100](#d-guynmart_100)

    <span id="d-guynmart_100"></span>**`guynmart_100`** Guynmart: “Then you must open the gate! Go to the gatehouse and open it, so that my men can get in. Be quick. After that go to the farm south of here. I expect a ferocious battle.” — **effects:** sets stage 160 of [Roses](../quests/guynmart.md#stage-160), spawns monsters on guynmart_main_0, removes monsters from guynmart_tower_2

    - “OK.” → [guynmart_110](#d-guynmart_110)

    <span id="d-guynmart_110"></span>**`guynmart_110`** [Unkorh](../monsters/guynmart_steward.md#v-guynmart_steward4): “YOU AGAIN!”

    - “Yikes! The steward!” → [guynmart_steward4_120](#d-guynmart_steward4_120)

    <span id="d-guynmart_steward4_120"></span>**`guynmart_steward4_120`** Guynmart: “Indeed. I am surprised to see you here.”

    - Next → [guynmart_steward4_122](#d-guynmart_steward4_122)

    <span id="d-guynmart_steward4_122"></span>**`guynmart_steward4_122`** Guynmart: “I wanted to keep you out of all this. I'm sure you now have many questions. I will tell you everything.”

    - “I hope you have a good explanation.” → [guynmart_steward4_130](#d-guynmart_steward4_130)
    - “I don't want to hear your lies.” → [guynmart_steward4_124](#d-guynmart_steward4_124)

    <span id="d-guynmart_steward4_130"></span>**`guynmart_steward4_130`** Guynmart: “Until recently, everything was fine. Guynmart was a righteous man, open-minded and tolerant. And Hannah was supposed to marry me when she was old enough.”

    - Next → [guynmart_steward4_140](#d-guynmart_steward4_140)

    <span id="d-guynmart_steward4_124"></span>**`guynmart_steward4_124`** Guynmart: “Please be patient, and give me a minute. This may be important to you.”

    - “No. I will never believe you unless you let Guynmart go!” → [guynmart_steward4_20](#d-guynmart_steward4_20)
    - “OK. One minute.” → [guynmart_steward4_130](#d-guynmart_steward4_130)

    <span id="d-guynmart_steward4_140"></span>**`guynmart_steward4_140`** Guynmart: “Then one unfortunate day this Lovis appeared.”

    - Next → [guynmart_steward4_142](#d-guynmart_steward4_142)

    <span id="d-guynmart_steward4_20"></span>**`guynmart_steward4_20`** Guynmart: “I have had enough of you. This will be your end!”

    - “Oh dear. Have mercy, please. I am just a little kid.” → [guynmart_steward4_30](#d-guynmart_steward4_30)
    - “Do you think so? Traitor!” → [guynmart_steward4_50](#d-guynmart_steward4_50)

    <span id="d-guynmart_steward4_142"></span>**`guynmart_steward4_142`** Guynmart: “He kept playing on his probably magical flute and thus stole Hannah's heart.”

    - Next → [guynmart_steward4_144](#d-guynmart_steward4_144)

    <span id="d-guynmart_steward4_30"></span>**`guynmart_steward4_30`** Guynmart: “Now you will get what you deserve!”

    - “No, please, please don't hurt me!” → [guynmart_steward4_32](#d-guynmart_steward4_32)

    <span id="d-guynmart_steward4_50"></span>**`guynmart_steward4_50`** Guynmart: “What did you call me? I'll beat you until you whine for mercy.”

    - “Ha! So come on and try! No? I will put an end to you now!” → [guynmart_steward4_60](#d-guynmart_steward4_60)
    - “Oh dear, please forgive my rash words.” → [guynmart_steward4_30](#d-guynmart_steward4_30)

    <span id="d-guynmart_steward4_144"></span>**`guynmart_steward4_144`** Guynmart: “He also began to influence Guynmart more and more, until Guynmart would not make a single decision without hearing from Lovis.”

    - Next → [guynmart_steward4_150](#d-guynmart_steward4_150)

    <span id="d-guynmart_steward4_32"></span>**`guynmart_steward4_32`** Guynmart: “Pathetic. So run, and never let me set eyes on you again!”


    <span id="d-guynmart_steward4_60"></span>**`guynmart_steward4_60`** Guynmart: “OK. I will go now. But I will not forget you - fear my revenge! And before I leave, I will stab your beloved Guynmart...” — **effects:** sets stage 162 of [Roses](../quests/guynmart.md#stage-162), removes monsters from guynmart_main_0

    - “Nooo! What did you do? Stay and face me, you coward!” → [guynmart_200](#d-guynmart_200)

    <span id="d-guynmart_steward4_150"></span>**`guynmart_steward4_150`** Guynmart: “Shadow meetings were banned, and the use of bonemeal potions was prohibited.”

    - Next → [guynmart_steward4_152](#d-guynmart_steward4_152)

    <span id="d-guynmart_steward4_152"></span>**`guynmart_steward4_152`** Guynmart: “People had to hand over all their bonemeal supplies so that they could be destroyed. The farms, their inhabitants, and even visitors were searched.”

    - Next → [guynmart_steward4_160](#d-guynmart_steward4_160)

    <span id="d-guynmart_steward4_160"></span>**`guynmart_steward4_160`** Guynmart: “A young man, who was my guest at that time, gave me his bonemeal potion box and asked me to take care of it. Otherwise it would have been destroyed too.”

    - Next → [guynmart_steward4_162](#d-guynmart_steward4_162)

    <span id="d-guynmart_steward4_162"></span>**`guynmart_steward4_162`** Guynmart: “So I took it for safekeeping. Look here.”

    - “I know this box - it belongs to my brother Andor!” → [guynmart_steward4_164](#d-guynmart_steward4_164)

    <span id="d-guynmart_steward4_164"></span>**`guynmart_steward4_164`** Guynmart: “Andor - yes, that was his name. He is your brother? That explains the similarity.”

    - Next → [guynmart_steward4_166](#d-guynmart_steward4_166)

    <span id="d-guynmart_steward4_166"></span>**`guynmart_steward4_166`** Guynmart: “We had long nights of interesting conversation.” — **effects:** sets stage 90 of [Search for Andor](../quests/andor.md#stage-90)

    - Next → [guynmart_steward4_170](#d-guynmart_steward4_170)

    <span id="d-guynmart_steward4_170"></span>**`guynmart_steward4_170`** Guynmart: “Well, Andor had to go on urgent business and left the castle the same night.”

    - Next → [guynmart_steward4_200](#d-guynmart_steward4_200)

    <span id="d-guynmart_steward4_200"></span>**`guynmart_steward4_200`** Guynmart: “Enough talk. Now you have to decide if you want to trust me or rather Guynmart.”

    - “I think I misjudged you. I will trust you.” → [guynmart_steward4_202](#d-guynmart_steward4_202)
    - “You did not convince me. I believe Guynmart more than you.” → [guynmart_steward4_202](#d-guynmart_steward4_202)

    <span id="d-guynmart_steward4_202"></span>**`guynmart_steward4_202`** Guynmart: “Are you sure? Listen to your heart. It is really important.”

    - “Yes, I will trust you.” → [guynmart_steward4_210](#d-guynmart_steward4_210)
    - “No, I believe Guynmart more than you.” → [guynmart_steward4_20](#d-guynmart_steward4_20)

    <span id="d-guynmart_steward4_210"></span>**`guynmart_steward4_210`** Guynmart: “Watch out! Guynmart...” — **effects:** sets stage 161 of [Roses](../quests/guynmart.md#stage-161), removes monsters from guynmart_main_0

    - “What?” → [guynmart_steward4_220](#d-guynmart_steward4_220)

    <span id="d-guynmart_steward4_220"></span>**`guynmart_steward4_220`** Guynmart: “Guynmart tried to get at you from behind. I felt I had to do something quick, but it seems that it wasn't necessary. Obviously he stumbled and fell on his own knife.”

    - “Thank you. Really, I didn't expect this from Lord Guynmart.” → [guynmart_steward4_230](#d-guynmart_steward4_230)

    <span id="d-guynmart_steward4_230"></span>**`guynmart_steward4_230`** Guynmart: “Yes, Guynmart had changed a lot recently. Here, please take Andor's bonemeal potion box and return it to him.” — **effects:** sets stage 92 of [Search for Andor](../quests/andor.md#stage-92), gives [Andor's bonemeal box](../items/guynmart_bonemealbox.md), [Bonemeal potion](../items/bonemeal_potion.md)

    - “If only I had finally found my brother.” → [guynmart_steward4_290](#d-guynmart_steward4_290)

    <span id="d-guynmart_steward4_290"></span>**`guynmart_steward4_290`** Guynmart: “And now stick to your plan. Open the gate. My men will await Norgothla.”

    - Next → [guynmart_steward4_292](#d-guynmart_steward4_292)

    <span id="d-guynmart_steward4_292"></span>**`guynmart_steward4_292`** Guynmart: “Then go to the farm south of here and stay there for the night. May The Shadow be with you!”

    - “Thank you.” → *NPC leaves*



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 37 lines added |
| [v0.7.9](../versions/0.7.9.md) | Dialogue: 1 line changed<br>· text: “Then you must open the gate! Go to the gatehouse and open it, so that…” → “Then you must open the gate! Go to the gatehouse and open it, so that…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `guynmart` |
    | Spawn group | `guynmart` |
    | Loot table | – |
    | Conversation | `guynmart_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik1:2` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart",
     "name": "Guynmart",
     "iconID": "monsters_tometik1:2",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_10"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
