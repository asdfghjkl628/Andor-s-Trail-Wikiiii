# ![](../assets/icons/monsters/monsters_newb_1_41.png){ .sprite } Nanath

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

- [fallhaven_derelict2](../maps/fallhaven_derelict2.md)

## Quests

- [Troubling times](../quests/troubling_times.md): stages 10, 20, 30, 40, 50, 82, 90, 95, 105, 115, 150, 160, 193, 302, 310

??? quote "Dialogue (55 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-nanath"></span>**`nanath`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 310 of [Troubling times](../quests/troubling_times.md#stage-310))* → [nanath_310](#d-nanath_310)
    - branch 2 *(if reached stage 290 of [Troubling times](../quests/troubling_times.md#stage-290))* → [nanath_290](#d-nanath_290)
    - branch 3 *(if reached stage 270 of [Troubling times](../quests/troubling_times.md#stage-270))* → [nanath_200](#d-nanath_200)
    - branch 4 *(if reached stage 160 of [Troubling times](../quests/troubling_times.md#stage-160))* → [nanath_190](#d-nanath_190)
    - branch 5 *(if reached stage 110 of [Troubling times](../quests/troubling_times.md#stage-110))* → [nanath_150](#d-nanath_150)
    - branch 6 *(if reached stage 95 of [Troubling times](../quests/troubling_times.md#stage-95))* → [nanath_110](#d-nanath_110)
    - branch 7 *(if reached stage 70 of [Troubling times](../quests/troubling_times.md#stage-70))* → [nanath_70](#d-nanath_70)
    - branch 8 *(if reached stage 70 of [Wanted men](../quests/wanted_men.md#stage-70))* → [nanath_10](#d-nanath_10)
    - branch 9 *(if reached stage 77 of [Wanted men](../quests/wanted_men.md#stage-77))* → [nanath_12](#d-nanath_12)
    - branch 10 *(if reached stage 80 of [Wanted men](../quests/wanted_men.md#stage-80))* → [nanath_20](#d-nanath_20)
    - branch 11 *(if reached stage 57 of [Wanted men](../quests/wanted_men.md#stage-57); NOT reached stage 70 of [Wanted men](../quests/wanted_men.md#stage-70))* → [nanath_20](#d-nanath_20)

    <span id="d-nanath_310"></span>**`nanath_310`** Nanath: “Stay safe, kid.”


    <span id="d-nanath_290"></span>**`nanath_290`** Nanath: “You were obviously successful. We seem to be inconspicuous again.”

    - Next → [nanath_300](#d-nanath_300)

    <span id="d-nanath_200"></span>**`nanath_200`** Nanath: “Hi kid.”

    - “I have got Luthor's ring.” → [nanath_272](#d-nanath_272)

    <span id="d-nanath_190"></span>**`nanath_190`** Nanath: “Have you found Seraphina yet?”

    - “No.” *(if NOT reached stage 180 of [Troubling times](../quests/troubling_times.md#stage-180))* → [nanath_182](#d-nanath_182)
    - “Yes. She told me I would need Luthor's key.” *(if reached stage 180 of [Troubling times](../quests/troubling_times.md#stage-180); reached stage 192 of [Troubling times](../quests/troubling_times.md#stage-192); NOT reached stage 193 of [Troubling times](../quests/troubling_times.md#stage-193))* → [nanath_192](#d-nanath_192)
    - “Yes. She told me I would need Luthor's key.” *(if reached stage 193 of [Troubling times](../quests/troubling_times.md#stage-193))* → [nanath_193](#d-nanath_193)

    <span id="d-nanath_150"></span>**`nanath_150`** Nanath: “How progresses the task? I hope you've done it? We're in a pickle here, kid. No time to dawdle.”

    - “Dawdle! Do it yourself if you know everything better!” → [nanath_152](#d-nanath_152)
    - “Well ...” → [nanath_160](#d-nanath_160)

    <span id="d-nanath_110"></span>**`nanath_110`** Nanath: “Have you found Luthor's ring yet?” — **effects:** sets stage 95 of [Troubling times](../quests/troubling_times.md#stage-95)

    - “I am looking for it now.” *(if NOT reached stage 100 of [Troubling times](../quests/troubling_times.md#stage-100))* → *conversation ends*
    - “I have no idea where to look any more.” *(if reached stage 100 of [Troubling times](../quests/troubling_times.md#stage-100))* → [nanath_120](#d-nanath_120)

    <span id="d-nanath_70"></span>**`nanath_70`** Nanath: “Oh, back again? I hope you bring good news.”

    - “Maybe. Talion, a Shadow priest, has put the Striking Spectacle Shadow spell on us.” *(if NOT reached stage 82 of [Troubling times](../quests/troubling_times.md#stage-82))* → [nanath_72](#d-nanath_72)
    - “I have been looking for the things for Talion.” *(if reached stage 82 of [Troubling times](../quests/troubling_times.md#stage-82))* → [nanath_92](#d-nanath_92)
    - “About Luthor's ring ...” *(if reached stage 95 of [Troubling times](../quests/troubling_times.md#stage-95); NOT reached stage 105 of [Troubling times](../quests/troubling_times.md#stage-105))* → [nanath_110](#d-nanath_110)
    - “I am still looking for Seraphina.” *(if reached stage 105 of [Troubling times](../quests/troubling_times.md#stage-105))* → [nanath_140](#d-nanath_140)

    <span id="d-nanath_10"></span>**`nanath_10`** Nanath: “You? How dare you show your face?” — **effects:** sets stage 10 of [Troubling times](../quests/troubling_times.md#stage-10), sets stage 20 of [Troubling times](../quests/troubling_times.md#stage-20)

    - “Why?” → [nanath_18](#d-nanath_18)

    <span id="d-nanath_12"></span>**`nanath_12`** Nanath: “You? How dare you show your face?” — **effects:** sets stage 10 of [Troubling times](../quests/troubling_times.md#stage-10), sets stage 30 of [Troubling times](../quests/troubling_times.md#stage-30)

    - “Why?” → [nanath_18](#d-nanath_18)

    <span id="d-nanath_20"></span>**`nanath_20`** Nanath: “Hi there. I am Nanath, the oldest and most experienced man in the guild. No need to introduce yourself, I know who you are, $playername.”

    - “Oh. Hi Nanath. You look scared.” → [nanath_22](#d-nanath_22)

    <span id="d-nanath_300"></span>**`nanath_300`** Nanath: “Good job! I didn't think you could do it. But you did.”

    - “Yes. The search was a nice change.” → [nanath_302](#d-nanath_302)

    <span id="d-nanath_272"></span>**`nanath_272`** Nanath: “Then take it to Talion. Quickly.”


    <span id="d-nanath_182"></span>**`nanath_182`** Nanath: “Let me think: Fallhaven would be too near. Sullengard, Stoutford, Vilegard and Prim come to my mind. And Loneford or Brimhaven, of course.” — **effects:** sets stage 160 of [Troubling times](../quests/troubling_times.md#stage-160)

    - “OK.” → [nanath_184](#d-nanath_184)

    <span id="d-nanath_192"></span>**`nanath_192`** Nanath: “I spoke to Umar. He already suspected that you would need this key.”

    - Next → [nanath_192a](#d-nanath_192a)

    <span id="d-nanath_193"></span>**`nanath_193`** Nanath: “I have given it to you already, forgotten?”

    - “Oh, right. I'm ashamed of myself for trying to trick you.” → [nanath_194](#d-nanath_194)

    <span id="d-nanath_152"></span>**`nanath_152`** Nanath: “Calm down. I'm just nervous. Did you make any progress?”

    - “Yes.” → [nanath_160](#d-nanath_160)

    <span id="d-nanath_160"></span>**`nanath_160`** Nanath: “Tell me.”

    - “Seraphina doesn't trust me.” *(if reached stage 110 of [Troubling times](../quests/troubling_times.md#stage-110); NOT reached stage 140 of [Troubling times](../quests/troubling_times.md#stage-140))* → [nanath_170](#d-nanath_170)
    - “Seraphina has disappeared. She's scared to unleash some monsters which she says Umar and her sealed up.” *(if reached stage 140 of [Troubling times](../quests/troubling_times.md#stage-140); NOT reached stage 180 of [Troubling times](../quests/troubling_times.md#stage-180))* → [nanath_180](#d-nanath_180)
    - “About Seraphina ...” *(if reached stage 180 of [Troubling times](../quests/troubling_times.md#stage-180))* → [nanath_190](#d-nanath_190)

    <span id="d-nanath_120"></span>**`nanath_120`** Nanath: “Looks like it ended up being kept somewhere dangerous.”

    - “Seems so.” → [nanath_122](#d-nanath_122)

    <span id="d-nanath_72"></span>**`nanath_72`** Nanath: “And?”

    - “And ... I think I have to talk to Talion again.” *(if NOT reached stage 80 of [Troubling times](../quests/troubling_times.md#stage-80))* → [nanath_80](#d-nanath_80)
    - “Talion said he can help dispel it.” *(if reached stage 80 of [Troubling times](../quests/troubling_times.md#stage-80))* → [nanath_80](#d-nanath_80)

    <span id="d-nanath_92"></span>**`nanath_92`** Nanath: “Do you already have all of the items?”

    - “I don't have Troublemaker's ring yet.” *(if NOT carry 1× [Troublemaker's ring](../items/ring_troublemaker.md))* → [nanath_94](#d-nanath_94)
    - “I don't have the Ring of backstabbing yet.” *(if NOT carry 1× [Ring of backstabbing](../items/ring_backstab.md))* → [nanath_94](#d-nanath_94)
    - “I don't have the Villain's ring yet.” *(if NOT carry 1× [Villain's ring](../items/ring_villain.md))* → [nanath_94](#d-nanath_94)
    - “I don't have the Tears of the Shadow yet.” *(if NOT carry 1× [Tears of the Shadow](../items/pot_shadowtear.md))* → [nanath_94](#d-nanath_94)
    - “I have already brought the 4 easier things.” *(if carry 1× [Troublemaker's ring](../items/ring_troublemaker.md); carry 1× [Ring of backstabbing](../items/ring_backstab.md); carry 1× [Villain's ring](../items/ring_villain.md); carry 1× [Tears of the Shadow](../items/pot_shadowtear.md))* → [nanath_100](#d-nanath_100)

    <span id="d-nanath_140"></span>**`nanath_140`** Nanath: “Then go and find her, now.”


    <span id="d-nanath_18"></span>**`nanath_18`** Nanath: “You betrayed the Guild over the task with Defy. Get out!”


    <span id="d-nanath_22"></span>**`nanath_22`** Nanath: “Well, one of our ex-clients, Lady Dameni, has put an adverse Shadow spell on us.”

    - “So?” → [nanath_24](#d-nanath_24)

    <span id="d-nanath_302"></span>**`nanath_302`** Nanath: “Sly Seraphina has already been here and returned Luthor's key to Umar. So the room with those dangerous creatures is sealed again.” — **effects:** sets stage 302 of [Troubling times](../quests/troubling_times.md#stage-302), clears stage 20 of [troubling_times_nd (hidden flag)](../quests/troubling_times_nd.md#stage-20)

    - “So quick?” → [nanath_304](#d-nanath_304)

    <span id="d-nanath_184"></span>**`nanath_184`** Nanath: “She must be found. By any means.”

    - “Yes, sir” → *conversation ends*

    <span id="d-nanath_192a"></span>**`nanath_192a`** Nanath: “Here you have it, handle it carefully.” — **effects:** sets stage 193 of [Troubling times](../quests/troubling_times.md#stage-193), gives 1× [Key of Luthor](../items/key_luthor.md)

    - “Of course.” → *conversation ends*

    <span id="d-nanath_194"></span>**`nanath_194`** Nanath: “I truly hope you are.”


    <span id="d-nanath_170"></span>**`nanath_170`** Nanath: “She must. Go to Umar. He's the only one she'll listen to.” — **effects:** sets stage 115 of [Troubling times](../quests/troubling_times.md#stage-115)

    - “OK.” → *conversation ends*

    <span id="d-nanath_180"></span>**`nanath_180`** Nanath: “So, that's what Umar is hush-hush about.”

    - “He could really be more talkative sometimes.” *(if NOT reached stage 180 of [Troubling times](../quests/troubling_times.md#stage-180))* → [nanath_181](#d-nanath_181)

    <span id="d-nanath_122"></span>**`nanath_122`** Nanath: “Then ... only one person may know: Fanamor's friend Sly Seraphina.”

    - “Sly Seraphina? Where can she be found?” *(if NOT reached stage 38 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-38))* → [nanath_130](#d-nanath_130)
    - “On no! Not Seraphina! I refuse to talk to her.” *(if reached stage 38 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-38))* → [nanath_132](#d-nanath_132)

    <span id="d-nanath_80"></span>**`nanath_80`** Nanath: “What a relief.”

    - Next → [nanath_82](#d-nanath_82)

    <span id="d-nanath_94"></span>**`nanath_94`** Nanath: “Well, then go and find it. Hurry now!”


    <span id="d-nanath_100"></span>**`nanath_100`** Nanath: “Good, that's a start.”

    - “I expect to be reimbursed of course.” → [nanath_102](#d-nanath_102)
    - “I am glad you approve.” → [nanath_102](#d-nanath_102)

    <span id="d-nanath_24"></span>**`nanath_24`** Nanath: “It makes us noticeable, and thus vulnerable to being caught - paralyzing our honest bread and butter work.”

    - “Oh. Sounds awful.” → [nanath_26](#d-nanath_26)

    <span id="d-nanath_304"></span>**`nanath_304`** Nanath: “Sure. You should know her by now.”

    - Next → [nanath_308](#d-nanath_308)

    <span id="d-nanath_181"></span>**`nanath_181`** Nanath: “Anyway, we must find her. I know some of her usual hidings.” — **effects:** sets stage 150 of [Troubling times](../quests/troubling_times.md#stage-150)

    - Next → [nanath_181a](#d-nanath_181a)

    <span id="d-nanath_130"></span>**`nanath_130`** Nanath: “She's the thief near the Sutdover bridge.”

    - “Sutdover bridge? So I'll look for her to the south.” → [nanath_136](#d-nanath_136)

    <span id="d-nanath_132"></span>**`nanath_132`** Nanath: “You must. For the Guild!”

    - “All right, I hate to, but for the greater good I'll go.” → [nanath_136](#d-nanath_136)

    <span id="d-nanath_82"></span>**`nanath_82`** Nanath: “What does he want in return?”

    - “Lady Dameni paid him. Talion wants 50,000 gold to dispel us.” → [nanath_84](#d-nanath_84)

    <span id="d-nanath_102"></span>**`nanath_102`** Nanath: “Umar will refund you, but only if you succeed.” — **effects:** sets stage 90 of [Troubling times](../quests/troubling_times.md#stage-90)

    - Next → [nanath_110](#d-nanath_110)

    <span id="d-nanath_26"></span>**`nanath_26`** Nanath: “Umar wants me to handle it. He wants me to get it dispelled, so that the Thieves' Guild can work again.”

    - “Ah, OK then.” → [nanath_28](#d-nanath_28)

    <span id="d-nanath_308"></span>**`nanath_308`** Nanath: “Umar asked me to reimburse you for your expenses. And something as a thank you. So here are 75,000 shining pieces of gold.” — **effects:** sets stage 310 of [Troubling times](../quests/troubling_times.md#stage-310), gives 75000× [Gold coins](../items/gold.md)

    - “Thank you.” → [nanath_310](#d-nanath_310)

    <span id="d-nanath_181a"></span>**`nanath_181a`** Nanath: “She prefers to be close to a town so she can easily stock up.”

    - “Makes sense.” → [nanath_182](#d-nanath_182)

    <span id="d-nanath_136"></span>**`nanath_136`** Nanath: “Then it's all settled. Go and find her, now.” — **effects:** sets stage 105 of [Troubling times](../quests/troubling_times.md#stage-105)


    <span id="d-nanath_84"></span>**`nanath_84`** Nanath: “That's a lot, but it was to be expected. It's good that he doesn't want more.”

    - “Well ... he also wants the following items: The Villain's ring, Troublemaker's ring, the Ring of backstabbing and the…” → [nanath_86](#d-nanath_86)

    <span id="d-nanath_28"></span>**`nanath_28`** Nanath: “The thing is I don't know much about the Shadow or any other so-called powers. My life has been being an honest thief, a score here, a score there - I don't tangle with the supernatural stuff.”

    - Next → [nanath_30](#d-nanath_30)

    <span id="d-nanath_86"></span>**`nanath_86`** Nanath: “That's fine with me.”

    - “And - most important - Luthor's ring.” → [nanath_90](#d-nanath_90)

    <span id="d-nanath_30"></span>**`nanath_30`** Nanath: “Can't anyone help?” — **effects:** sets stage 10 of [Troubling times](../quests/troubling_times.md#stage-10), sets stage 40 of [Troubling times](../quests/troubling_times.md#stage-40)

    - “I can help. I've had some dealings with the Shadow.” → [nanath_32](#d-nanath_32)

    <span id="d-nanath_90"></span>**`nanath_90`** Nanath: “What?! He must be crazy!” — **effects:** sets stage 82 of [Troubling times](../quests/troubling_times.md#stage-82)

    - Next → [nanath_92](#d-nanath_92)

    <span id="d-nanath_32"></span>**`nanath_32`** Nanath: “Really? Like what?”

    - “Sorry, hush-hush stuff around Loneford and Vilegard.” → [nanath_34](#d-nanath_34)

    <span id="d-nanath_34"></span>**`nanath_34`** Nanath: “Of course.”

    - “You want my help?” → [nanath_40](#d-nanath_40)

    <span id="d-nanath_40"></span>**`nanath_40`** Nanath: “First things first, how can we know the nature of the spell?”

    - Next → [nanath_42](#d-nanath_42)

    <span id="d-nanath_42"></span>**`nanath_42`** Nanath: “Or its name?”

    - “Hmm ...” → [nanath_44](#d-nanath_44)

    <span id="d-nanath_44"></span>**`nanath_44`** Nanath: “Maybe talking to a Shadow priest may help?” — **effects:** sets stage 50 of [Troubling times](../quests/troubling_times.md#stage-50)

    - “I'll see what I can do.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.13](../versions/0.8.13.md) | Added<br>Dialogue: 55 lines added |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 2 lines changed<br>· text: “Umar asked me to reimburse you for your expenses. And something as a …” → “Umar asked me to reimburse you for your expenses. And something as a …” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=nanath.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=nanath.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=nanath.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=nanath.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `nanath` · Data from v0.8.18</small>
