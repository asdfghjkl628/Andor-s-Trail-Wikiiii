# ![](../assets/icons/monsters/monsters_tometik7_38.png){ .sprite } Sly Seraphina

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

- [blackwater_mountain12](../maps/blackwater_mountain12.md)
- [sullengard3](../maps/sullengard3.md)
- [vilegard_s](../maps/vilegard_s.md)
- [waterway6](../maps/waterway6.md)
- [waytobrimhaven1](../maps/waytobrimhaven1.md)
- [waytobrimhaven3](../maps/waytobrimhaven3.md)
- [wild21](../maps/wild21.md)

## Quests

- [Troubling times](../quests/troubling_times.md): stages 180, 190, 192, 195

??? quote "Dialogue (15 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-tt_sly_200"></span>**`tt_sly_200`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT killed 5× [Seraphina's bodyguard](../monsters/tt_guys.md))* → [tt_sly_202](#d-tt_sly_202)
    - branch 2 → [tt_sly_210](#d-tt_sly_210)

    <span id="d-tt_sly_202"></span>**`tt_sly_202`** Sly Seraphina: “Watch out, kid. Behind you!”


    <span id="d-tt_sly_210"></span>**`tt_sly_210`** Sly Seraphina: “OK, you're tough, even if not smart, kid.” — **effects:** sets stage 180 of [Troubling times](../quests/troubling_times.md#stage-180), removes monsters from sullengard3, removes monsters from wild21, removes monsters from waytobrimhaven1, removes monsters from blackwater_mountain12, removes monsters from waterway6, removes monsters from vilegard_s

    - “Thank you?” → [tt_sly_211](#d-tt_sly_211)

    <span id="d-tt_sly_211"></span>**`tt_sly_211`** Sly Seraphina: “Smart enough to find me, and tough enough to beat my friends. You convinced me that we can do it.”

    - Next → [tt_sly_212](#d-tt_sly_212)

    <span id="d-tt_sly_212"></span>**`tt_sly_212`** Sly Seraphina: “As we discussed, Luthor's Ring can be found in the secret room which Crackshot tried to open with Luthor's key from Umar.”

    - Next → [tt_sly_213](#d-tt_sly_213)

    <span id="d-tt_sly_213"></span>**`tt_sly_213`** Sly Seraphina: “So you have to go and ask Umar for Luthor's key.” — **effects:** sets stage 192 of [Troubling times](../quests/troubling_times.md#stage-192)

    - “No problem.” → [tt_sly_214](#d-tt_sly_214)

    <span id="d-tt_sly_214"></span>**`tt_sly_214`** Sly Seraphina: “However, that door can only be opened if you also wear Luthor's gloves, which breaks the spell on it.”

    - “And the evil you mentioned are monsters, nothing more?” → [tt_sly_216](#d-tt_sly_216)

    <span id="d-tt_sly_216"></span>**`tt_sly_216`** Sly Seraphina: “In fact, I didn't take the time to look at them more closely. But they seemed terrible and deadly to me.”

    - Next → [tt_sly_220](#d-tt_sly_220)

    <span id="d-tt_sly_220"></span>**`tt_sly_220`** Sly Seraphina: “When the door opens, and these strong monsters escape into the open, they will attack Dhayavar, which we must avoid at all costs.”

    - Next → [tt_sly_222](#d-tt_sly_222)

    <span id="d-tt_sly_222"></span>**`tt_sly_222`** Sly Seraphina: “Which reminds me: Another kid was looking for information to open it.”

    - “That kid, did he look just like me, but older?” → [tt_sly_230](#d-tt_sly_230)

    <span id="d-tt_sly_230"></span>**`tt_sly_230`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 999 of [andor (hidden flag)](../quests/andor.md#stage-999)

    - branch 1 → [tt_sly_240](#d-tt_sly_240)

    <span id="d-tt_sly_240"></span>**`tt_sly_240`** Sly Seraphina: “Come to think of it, he did.” — **effects:** sets stage 130 of [andor (hidden flag)](../quests/andor.md#stage-130), sets stage 999 of [andor (hidden flag)](../quests/andor.md#stage-999)

    - “[to self] What was Andor trying to do now?” → [tt_sly_250](#d-tt_sly_250)

    <span id="d-tt_sly_250"></span>**`tt_sly_250`** Sly Seraphina: “Looking at your strength, kid, you may just be able to beat those monsters. We might give it a try.”

    - “Thanks again.” *(if reached stage 38 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-38); NOT reached stage 190 of [Troubling times](../quests/troubling_times.md#stage-190))* → [tt_sly_252](#d-tt_sly_252)
    - “Thanks again.” *(if NOT reached stage 38 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-38))* → [tt_sly_254](#d-tt_sly_254)

    <span id="d-tt_sly_252"></span>**`tt_sly_252`** Sly Seraphina: “By the way, here's your money back. 1,000 gold.” — **effects:** sets stage 190 of [Troubling times](../quests/troubling_times.md#stage-190), gives 1000× [Gold coins](../items/gold.md)

    - “Hmm, OK.” → [tt_sly_254](#d-tt_sly_254)

    <span id="d-tt_sly_254"></span>**`tt_sly_254`** Sly Seraphina: “Meet me at the door to the secret room, and bring Luthor's key. Together with Luthor's gloves the door will open.” — **effects:** sets stage 195 of [Troubling times](../quests/troubling_times.md#stage-195), spawns monsters on crackshot_hideout3, removes monsters from sullengard3, removes monsters from sullengard3, removes monsters from wild21, removes monsters from wild21, removes monsters from waytobrimhaven1, removes monsters from waytobrimhaven1, removes monsters from blackwater_mountain12, removes monsters from blackwater_mountain12, removes monsters from waterway6, removes monsters from waterway6, removes monsters from vilegard_s, removes monsters from vilegard_s

    - “OK.” → *NPC leaves*



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tt_seraphina.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tt_seraphina.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tt_seraphina.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tt_seraphina.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `tt_seraphina` · Data from v0.8.18</small>
