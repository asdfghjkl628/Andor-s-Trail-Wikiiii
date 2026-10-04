# ![](../assets/icons/monsters/monsters_ld1_11.png){ .sprite } Unkorh

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 0 |
| Max AP | 10 |
| Attack cost | 10 |
| Move cost | 10 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Found on

- [guynmart_main_0](../maps/guynmart_main_0.md)

## Quests

- [Roses](../quests/guynmart.md): stages 161, 162
- [Search for Andor](../quests/andor.md): stages 90, 92

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Unkorh. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_steward4_10.json" data-npc="Unkorh" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (30 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guynmart_steward4_10"></span>**`guynmart_steward4_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 161 of [Roses](../quests/guynmart.md#stage-161))* → [guynmart_steward4_210](#d-guynmart_steward4_210)
    - branch 2 → [guynmart_steward4_12](#d-guynmart_steward4_12)

    <span id="d-guynmart_steward4_210"></span>**`guynmart_steward4_210`** Unkorh: “Watch out! Guynmart...” — **effects:** sets stage 161 of [Roses](../quests/guynmart.md#stage-161), removes monsters from guynmart_main_0

    - “What?” → [guynmart_steward4_220](#d-guynmart_steward4_220)

    <span id="d-guynmart_steward4_12"></span>**`guynmart_steward4_12`** Unkorh: “You again!”

    - “Yes, me. And I know what you have done! I talked to Norgothla in the woods and found Lord Guynmart and Lovis here in…” → [guynmart_steward4_120](#d-guynmart_steward4_120)

    <span id="d-guynmart_steward4_220"></span>**`guynmart_steward4_220`** Unkorh: “Guynmart tried to get at you from behind. I felt I had to do something quick, but it seems that it wasn't necessary. Obviously he stumbled and fell on his own knife.”

    - “Thank you. Really, I didn't expect this from Lord Guynmart.” → [guynmart_steward4_230](#d-guynmart_steward4_230)

    <span id="d-guynmart_steward4_120"></span>**`guynmart_steward4_120`** Unkorh: “Indeed. I am surprised to see you here.”

    - Next → [guynmart_steward4_122](#d-guynmart_steward4_122)

    <span id="d-guynmart_steward4_230"></span>**`guynmart_steward4_230`** Unkorh: “Yes, Guynmart had changed a lot recently. Here, please take Andor's bonemeal potion box and return it to him.” — **effects:** sets stage 92 of [Search for Andor](../quests/andor.md#stage-92), gives [Andor's bonemeal box](../items/guynmart_bonemealbox.md), [Bonemeal potion](../items/bonemeal_potion.md)

    - “If only I had finally found my brother.” → [guynmart_steward4_290](#d-guynmart_steward4_290)

    <span id="d-guynmart_steward4_122"></span>**`guynmart_steward4_122`** Unkorh: “I wanted to keep you out of all this. I'm sure you now have many questions. I will tell you everything.”

    - “I hope you have a good explanation.” → [guynmart_steward4_130](#d-guynmart_steward4_130)
    - “I don't want to hear your lies.” → [guynmart_steward4_124](#d-guynmart_steward4_124)

    <span id="d-guynmart_steward4_290"></span>**`guynmart_steward4_290`** Unkorh: “And now stick to your plan. Open the gate. My men will await Norgothla.”

    - Next → [guynmart_steward4_292](#d-guynmart_steward4_292)

    <span id="d-guynmart_steward4_130"></span>**`guynmart_steward4_130`** Unkorh: “Until recently, everything was fine. Guynmart was a righteous man, open-minded and tolerant. And Hannah was supposed to marry me when she was old enough.”

    - Next → [guynmart_steward4_140](#d-guynmart_steward4_140)

    <span id="d-guynmart_steward4_124"></span>**`guynmart_steward4_124`** Unkorh: “Please be patient, and give me a minute. This may be important to you.”

    - “No. I will never believe you unless you let Guynmart go!” → [guynmart_steward4_20](#d-guynmart_steward4_20)
    - “OK. One minute.” → [guynmart_steward4_130](#d-guynmart_steward4_130)

    <span id="d-guynmart_steward4_292"></span>**`guynmart_steward4_292`** Unkorh: “Then go to the farm south of here and stay there for the night. May The Shadow be with you!”

    - “Thank you.” → *NPC leaves*

    <span id="d-guynmart_steward4_140"></span>**`guynmart_steward4_140`** Unkorh: “Then one unfortunate day this Lovis appeared.”

    - Next → [guynmart_steward4_142](#d-guynmart_steward4_142)

    <span id="d-guynmart_steward4_20"></span>**`guynmart_steward4_20`** Unkorh: “I have had enough of you. This will be your end!”

    - “Oh dear. Have mercy, please. I am just a little kid.” → [guynmart_steward4_30](#d-guynmart_steward4_30)
    - “Do you think so? Traitor!” → [guynmart_steward4_50](#d-guynmart_steward4_50)

    <span id="d-guynmart_steward4_142"></span>**`guynmart_steward4_142`** Unkorh: “He kept playing on his probably magical flute and thus stole Hannah's heart.”

    - Next → [guynmart_steward4_144](#d-guynmart_steward4_144)

    <span id="d-guynmart_steward4_30"></span>**`guynmart_steward4_30`** Unkorh: “Now you will get what you deserve!”

    - “No, please, please don't hurt me!” → [guynmart_steward4_32](#d-guynmart_steward4_32)

    <span id="d-guynmart_steward4_50"></span>**`guynmart_steward4_50`** Unkorh: “What did you call me? I'll beat you until you whine for mercy.”

    - “Ha! So come on and try! No? I will put an end to you now!” → [guynmart_steward4_60](#d-guynmart_steward4_60)
    - “Oh dear, please forgive my rash words.” → [guynmart_steward4_30](#d-guynmart_steward4_30)

    <span id="d-guynmart_steward4_144"></span>**`guynmart_steward4_144`** Unkorh: “He also began to influence Guynmart more and more, until Guynmart would not make a single decision without hearing from Lovis.”

    - Next → [guynmart_steward4_150](#d-guynmart_steward4_150)

    <span id="d-guynmart_steward4_32"></span>**`guynmart_steward4_32`** Unkorh: “Pathetic. So run, and never let me set eyes on you again!”


    <span id="d-guynmart_steward4_60"></span>**`guynmart_steward4_60`** Unkorh: “OK. I will go now. But I will not forget you - fear my revenge! And before I leave, I will stab your beloved Guynmart...” — **effects:** sets stage 162 of [Roses](../quests/guynmart.md#stage-162), removes monsters from guynmart_main_0

    - “Nooo! What did you do? Stay and face me, you coward!” → [guynmart_200](#d-guynmart_200)

    <span id="d-guynmart_steward4_150"></span>**`guynmart_steward4_150`** Unkorh: “Shadow meetings were banned, and the use of bonemeal potions was prohibited.”

    - Next → [guynmart_steward4_152](#d-guynmart_steward4_152)

    <span id="d-guynmart_200"></span>**`guynmart_200`** [Guynmart](../monsters/guynmart.md): “[Groaning] ...open the gate...”

    - Next → [guynmart_210](#d-guynmart_210)

    <span id="d-guynmart_steward4_152"></span>**`guynmart_steward4_152`** Unkorh: “People had to hand over all their bonemeal supplies so that they could be destroyed. The farms, their inhabitants, and even visitors were searched.”

    - Next → [guynmart_steward4_160](#d-guynmart_steward4_160)

    <span id="d-guynmart_210"></span>**`guynmart_210`** [Guynmart](../monsters/guynmart.md): “...then go ... to Rhodita...”


    <span id="d-guynmart_steward4_160"></span>**`guynmart_steward4_160`** Unkorh: “A young man, who was my guest at that time, gave me his bonemeal potion box and asked me to take care of it. Otherwise it would have been destroyed too.”

    - Next → [guynmart_steward4_162](#d-guynmart_steward4_162)

    <span id="d-guynmart_steward4_162"></span>**`guynmart_steward4_162`** Unkorh: “So I took it for safekeeping. Look here.”

    - “I know this box - it belongs to my brother Andor!” → [guynmart_steward4_164](#d-guynmart_steward4_164)

    <span id="d-guynmart_steward4_164"></span>**`guynmart_steward4_164`** Unkorh: “Andor - yes, that was his name. He is your brother? That explains the similarity.”

    - Next → [guynmart_steward4_166](#d-guynmart_steward4_166)

    <span id="d-guynmart_steward4_166"></span>**`guynmart_steward4_166`** Unkorh: “We had long nights of interesting conversation.” — **effects:** sets stage 90 of [Search for Andor](../quests/andor.md#stage-90)

    - Next → [guynmart_steward4_170](#d-guynmart_steward4_170)

    <span id="d-guynmart_steward4_170"></span>**`guynmart_steward4_170`** Unkorh: “Well, Andor had to go on urgent business and left the castle the same night.”

    - Next → [guynmart_steward4_200](#d-guynmart_steward4_200)

    <span id="d-guynmart_steward4_200"></span>**`guynmart_steward4_200`** Unkorh: “Enough talk. Now you have to decide if you want to trust me or rather Guynmart.”

    - “I think I misjudged you. I will trust you.” → [guynmart_steward4_202](#d-guynmart_steward4_202)
    - “You did not convince me. I believe Guynmart more than you.” → [guynmart_steward4_202](#d-guynmart_steward4_202)

    <span id="d-guynmart_steward4_202"></span>**`guynmart_steward4_202`** Unkorh: “Are you sure? Listen to your heart. It is really important.”

    - “Yes, I will trust you.” → [guynmart_steward4_210](#d-guynmart_steward4_210)
    - “No, I believe Guynmart more than you.” → [guynmart_steward4_20](#d-guynmart_steward4_20)



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 30 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_steward4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_steward4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_steward4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_steward4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `guynmart_steward4` · Data from v0.8.18</small>
