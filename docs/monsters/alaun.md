# ![](../assets/icons/monsters/monsters_mage2_0.png){ .sprite } Alaun

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

- [fallhaven_alaun](../maps/fallhaven_alaun.md)

## Quests

- [Delicious soup](../quests/gison_soup.md): stages 10, 30, 35
- [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md): stages 10, 11, 15, 16, 20, 21, 30

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Alaun. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/alaun_start.json" data-npc="Alaun" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (28 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-alaun_start"></span>**`alaun_start`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 120 of [Delicious soup](../quests/gison_soup.md#stage-120))* → [alaun_bela_soup](#d-alaun_bela_soup)
    - branch 2 *(if reached stage 30 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-30))* → [alaun_fail](#d-alaun_fail)
    - branch 3 *(if reached stage 40 of [Delicious soup](../quests/gison_soup.md#stage-40))* → [alaun_complete](#d-alaun_complete)
    - branch 4 → [alaun](#d-alaun)

    <span id="d-alaun_bela_soup"></span>**`alaun_bela_soup`** Alaun: “Ah, my friend! Have you heard the great news? Gison and Nimael have started supplying the tavern here in Fallhaven with their newest soup. It's marvelous!”


    <span id="d-alaun_fail"></span>**`alaun_fail`** Alaun: “You dare show your face in my home again? Out! Now! [Alaun starts throwing things at you again]” — **effects:** applies condition fear


    <span id="d-alaun_complete"></span>**`alaun_complete`** Alaun: “Ah, my hero returns. Thank you for the soup, it was incredible. What can I help you with today?”

    - “Have you seen my brother Andor? He looks similar to me.” → [alaun_2](#d-alaun_2)

    <span id="d-alaun"></span>**`alaun`** Alaun: “Hello. I'm Alaun. How can I help you?”

    - “Have you seen my brother Andor? He looks similar to me.” → [alaun_2](#d-alaun_2)
    - “Do you have a job for me?” *(if NOT reached stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10))* → [alaun_1](#d-alaun_1)
    - “About the soup...” *(if latest stage of [Delicious soup](../quests/gison_soup.md#stage-10) is 10)* → [alaun_return_blindstart](#d-alaun_return_blindstart)
    - “About the soup...” *(if reached stage 50 of [Delicious soup](../quests/gison_soup.md#stage-50))* → [alaun_return_blindstart](#d-alaun_return_blindstart)
    - “Gison gave me some of his soup.” *(if reached stage 20 of [Delicious soup](../quests/gison_soup.md#stage-20); NOT reached stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30); NOT reached stage 50 of [Delicious soup](../quests/gison_soup.md#stage-50))* → [alaun_return](#d-alaun_return)

    <span id="d-alaun_2"></span>**`alaun_2`** Alaun: “You are looking for your brother you say? Looks like you? Hmm.”

    - Next → [alaun_3](#d-alaun_3)

    <span id="d-alaun_1"></span>**`alaun_1`** Alaun: “Oh, how surprising. How nice of you. Indeed there is something you could do for me.”

    - “Tell me what it is.” → [alaun_5](#d-alaun_5)
    - “Maybe later.” → *conversation ends*
    - “Let's talk about payment first.” → [alaun_4](#d-alaun_4)

    <span id="d-alaun_return_blindstart"></span>**`alaun_return_blindstart`** Alaun: “Yes. I asked you to bring me some of that delicious mushroom soup from Gison.”

    - “Can you explain the way again?” → [alaun_startquest_go](#d-alaun_startquest_go)
    - “Yes, I'm on my way.” → *conversation ends*
    - “I was not able to bring you the soup.” *(if reached stage 50 of [Delicious soup](../quests/gison_soup.md#stage-50))* → [alaun_return_fail](#d-alaun_return_fail)

    <span id="d-alaun_return"></span>**`alaun_return`** Alaun: “Aah, you are back. Wonderful. I will stop working for now and take a little break.”

    - Next → [alaun_return_evaluation](#d-alaun_return_evaluation)

    <span id="d-alaun_3"></span>**`alaun_3`** Alaun: “No, I cannot recall seeing anyone by that description. Maybe you should try in Crossglen village west of here.”


    <span id="d-alaun_5"></span>**`alaun_5`** Alaun: “I'll give you 10 gold if you do this little job for me: Bring me some of that delicious soup which Gison cooks using mushrooms and wild herbs.”

    - “Sounds easy, I'll do it!” → [alaun_startquest10](#d-alaun_startquest10)
    - “Give me 15 and I'll do it.” → [alaun_more1](#d-alaun_more1)
    - “Give me 20 and I'll do it.” → [alaun_more2](#d-alaun_more2)
    - “No way, I'm not your gopher.” → *conversation ends*

    <span id="d-alaun_4"></span>**`alaun_4`** Alaun: “Ahh, you are here to earn some money, okay.”

    - Next → [alaun_5](#d-alaun_5)

    <span id="d-alaun_startquest_go"></span>**`alaun_startquest_go`** Alaun: “You can find Gison and his wife Nimael south of here. Cross the path and head into the woods. You will find their house soon.”

    - “OK. See you later.” → *conversation ends*

    <span id="d-alaun_return_fail"></span>**`alaun_return_fail`** Alaun: “That can't be. Get out of here! [Alaun starts throwing things at you]” — **effects:** applies condition fear, sets stage 30 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-30)

    - “But...” → *conversation ends*
    - “Listen...” → *conversation ends*

    <span id="d-alaun_return_evaluation"></span>**`alaun_return_evaluation`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if carry 1× [Gison's mushroom soup](../items/gison_soup.md); 10 rounds passed since timer “gison_soup”)* → [alaun_return_coldsoup](#d-alaun_return_coldsoup)
    - branch 2 *(if reached stage 20 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-20); hand over 1× [Gison's mushroom soup](../items/gison_soup.md))* → [alaun_return20](#d-alaun_return20)
    - branch 3 *(if reached stage 15 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-15); hand over 1× [Gison's mushroom soup](../items/gison_soup.md))* → [alaun_return15](#d-alaun_return15)
    - branch 4 *(if reached stage 10 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-10); hand over 1× [Gison's mushroom soup](../items/gison_soup.md))* → [alaun_return10](#d-alaun_return10)
    - branch 5 → [alaun_return_nosoup](#d-alaun_return_nosoup)

    <span id="d-alaun_startquest10"></span>**`alaun_startquest10`** Alaun: “That's really nice of you.” — **effects:** sets stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10), sets stage 10 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-10)

    - Next → [alaun_startquest_go](#d-alaun_startquest_go)

    <span id="d-alaun_more1"></span>**`alaun_more1`** Alaun: “15? Let me think...erm... OK, I'll give you 15.”

    - “Sounds good. I will do it.” → [alaun_startquest15](#d-alaun_startquest15)
    - “I changed my mind.” → *conversation ends*

    <span id="d-alaun_more2"></span>**`alaun_more2`** Alaun: “20? Let me think...erm... OK. I'll give you 20. But please, bring it hot or I won't pay you.”

    - “Sounds good. I will do it.” → [alaun_startquest20](#d-alaun_startquest20)
    - “I changed my mind.” → *conversation ends*

    <span id="d-alaun_return_coldsoup"></span>**`alaun_return_coldsoup`** Alaun: “This soup is cold. Return to me with a hot soup!”

    - “Sorry. I will try again.” → *conversation ends*
    - “It still tastes...” → *conversation ends*

    <span id="d-alaun_return20"></span>**`alaun_return20`** Alaun: “Here is the money I promised you. Next time I will buy Nimael's soup.” — **effects:** sets stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30), gives 20× [Gold coins](../items/gold.md), gives 1× [Empty bottle](../items/bottle_empty.md), sets stage 21 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-21), sets stage 35 of [Delicious soup](../quests/gison_soup.md#stage-35)

    - “Nimael's soup?” → [alaun_return_nimael](#d-alaun_return_nimael)

    <span id="d-alaun_return15"></span>**`alaun_return15`** Alaun: “Here is the money I promised you. Next time I will buy Nimael's soup.” — **effects:** gives 15× [Gold coins](../items/gold.md), gives 1× [Empty bottle](../items/bottle_empty.md), sets stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30), sets stage 16 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-16), sets stage 35 of [Delicious soup](../quests/gison_soup.md#stage-35)

    - “Nimael's soup?” → [alaun_return_nimael](#d-alaun_return_nimael)

    <span id="d-alaun_return10"></span>**`alaun_return10`** Alaun: “Here is the money I promised you. And as a bonus I will give you some of this bread. Next time I will buy Nimael's soup.” — **effects:** sets stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30), gives 10× [Gold coins](../items/gold.md), gives 5× [Bread](../items/bread.md), gives 1× [Empty bottle](../items/bottle_empty.md), sets stage 11 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-11), sets stage 35 of [Delicious soup](../quests/gison_soup.md#stage-35)

    - “Nimael's soup?” → [alaun_return_nimael](#d-alaun_return_nimael)

    <span id="d-alaun_return_nosoup"></span>**`alaun_return_nosoup`** Alaun: “Where is it?”

    - “Oops, I forgot that there is a hole in my bag.” → [alaun_return_nosoup_1](#d-alaun_return_nosoup_1)
    - “I ate it.” → [alaun_return_nosoup_1](#d-alaun_return_nosoup_1)

    <span id="d-alaun_startquest15"></span>**`alaun_startquest15`** Alaun: “That's nice of you.” — **effects:** sets stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10), sets stage 15 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-15)

    - Next → [alaun_startquest_go](#d-alaun_startquest_go)

    <span id="d-alaun_startquest20"></span>**`alaun_startquest20`** Alaun: “OK, please bring it hot!” — **effects:** sets stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10), sets stage 20 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-20)

    - Next → [alaun_startquest_go](#d-alaun_startquest_go)

    <span id="d-alaun_return_nimael"></span>**`alaun_return_nimael`** Alaun: “Yes. Nimael also makes very good soup. Vegetables with forest herbs. If I buy both I hope they will argue less about whose is better.”

    - Next → [alaun_return_end](#d-alaun_return_end)

    <span id="d-alaun_return_nosoup_1"></span>**`alaun_return_nosoup_1`** Alaun: “What are you waiting for? Go on, bring me some soup. Hurry, I'm hungry!”

    - “Yes, I will return quickly.” → *conversation ends*

    <span id="d-alaun_return_end"></span>**`alaun_return_end`** Alaun: “Thanks again. And remember to take the bottle back to Gison. Now go please. I want to eat.”

    - “Enjoy your meal.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed<br>· text: “You are looking for your brother you say? Looks like you? Hm.” → “You are looking for your brother you say? Looks like you? Hmm.” |
| [v0.7.13](../versions/0.7.13.md) | phraseID: alaun → alaun_start<br>Dialogue: 25 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=alaun.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=alaun.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=alaun.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=alaun.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `alaun` · Data from v0.8.18</small>
