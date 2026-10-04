# ![](../assets/icons/monsters/monsters_karvis2_3.png){ .sprite } Villager

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

- [loneford2](../maps/loneford2.md)

## Quests

- [It makes no fence](../quests/tunlon_fence.md): stages 150, 210, 230

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Villager. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/loneford_villager2.json" data-npc="Villager" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (7 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-loneford_villager2"></span>**`loneford_villager2`** Villager: “Don't disturb me, I need to finish chopping this wood. Go bother someone else.”

    - “Do you by any chance have some fences?” *(if reached stage 100 of [It makes no fence](../quests/tunlon_fence.md#stage-100); NOT reached stage 150 of [It makes no fence](../quests/tunlon_fence.md#stage-150))* → [loneford_villager2_fence](#d-loneford_villager2_fence)
    - “Do you by any chance have some fences?” *(if reached stage 110 of [It makes no fence](../quests/tunlon_fence.md#stage-110); NOT reached stage 150 of [It makes no fence](../quests/tunlon_fence.md#stage-150))* → [loneford_villager2_fence](#d-loneford_villager2_fence)
    - “Unfortunately the fences you gave me are not tall enough. Do you have others?” *(if reached stage 200 of [It makes no fence](../quests/tunlon_fence.md#stage-200); NOT reached stage 210 of [It makes no fence](../quests/tunlon_fence.md#stage-210))* → [loneford_villager2_fence2](#d-loneford_villager2_fence2)
    - “The Craftsman told me that I should get some wood from you.” *(if reached stage 220 of [It makes no fence](../quests/tunlon_fence.md#stage-220); NOT reached stage 230 of [It makes no fence](../quests/tunlon_fence.md#stage-230))* → [loneford_villager2_fence4](#d-loneford_villager2_fence4)

    <span id="d-loneford_villager2_fence"></span>**`loneford_villager2_fence`** Villager: “Oh actually I do right here. You can have them for 100 gold pieces.”

    - “Great, I'll take them.” *(if pay 100 gold)* → [loneford_villager2_fence1](#d-loneford_villager2_fence1)
    - “100 gold is too much.” → [loneford_villager2_fence1a](#d-loneford_villager2_fence1a)

    <span id="d-loneford_villager2_fence2"></span>**`loneford_villager2_fence2`** Villager: “No, I don't.”

    - “So ... could you make any?” → [loneford_villager2_fence3](#d-loneford_villager2_fence3)

    <span id="d-loneford_villager2_fence4"></span>**`loneford_villager2_fence4`** Villager: “[pointing to a pile of wood] There.” — **effects:** sets stage 230 of [It makes no fence](../quests/tunlon_fence.md#stage-230), gives [Pile of wood](../items/tunlon_wood.md)

    - “Thank you ... I guess.” → *conversation ends*

    <span id="d-loneford_villager2_fence1"></span>**`loneford_villager2_fence1`** Villager: “Here you go.” — **effects:** sets stage 150 of [It makes no fence](../quests/tunlon_fence.md#stage-150), gives [Sturdy fence](../items/tunlon_fence1.md)

    - “Thank you! [and I won't tell you that Tunlon gave me 200 gold]” → *conversation ends*

    <span id="d-loneford_villager2_fence1a"></span>**`loneford_villager2_fence1a`** Villager: “Take it or leave it. 100 gold pieces.”

    - “OK. I'll take them.” *(if pay 100 gold)* → [loneford_villager2_fence1](#d-loneford_villager2_fence1)
    - “Forget it.” → *conversation ends*

    <span id="d-loneford_villager2_fence3"></span>**`loneford_villager2_fence3`** Villager: “Kid, look. I am a woodcutter, not a craftsman. Go east to Brimhaven if you want other fences.” — **effects:** sets stage 210 of [It makes no fence](../quests/tunlon_fence.md#stage-210)

    - “Thank you. I will go there now.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.8.10](../versions/0.8.10.md) | Dialogue: 6 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=loneford_villager2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=loneford_villager2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=loneford_villager2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=loneford_villager2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `loneford_villager2` · Data from v0.8.18</small>
