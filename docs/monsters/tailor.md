# ![](../assets/icons/monsters/monsters_men2_0.png){ .sprite } Tailor

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

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Green hat](../items/hat1.md) | 100% | 1 |
| [Fine green hat](../items/hat2.md) | 100% | 1 |
| [Cloth shirt](../items/shirt1.md) | 100% | 1 |
| [Torn shirt](../items/shirt_torn.md) | 100% | 1 |
| [Weathered shirt](../items/shirt_weathered.md) | 100% | 1 |
| [Patched cloth shirt](../items/shirt_patched_cloth.md) | 100% | 1 |
| [Fine shirt](../items/shirt2.md) | 100% | 1 |
| [Hardened leather shirt](../items/shirt_dmgresist.md) | 100% | 1 |
| [Gloves of fumbling](../items/gloves_fumbling.md) | 100% | 1 |
| [Fancy gloves](../items/gloves_fancy.md) | 100% | 1 |
| [Crude cloth gloves](../items/gloves_crude_cloth.md) | 100% | 1 |
| [Blood-stained gloves](../items/used_gloves.md) | 100% | 1 |
| [Bar brawler's gloves](../items/gloves_barbrawler.md) | 100% | 1 |
| [Gloves of swift attack](../items/gloves_attack1.md) | 100% | 1 |
| [Crude leather boots](../items/boots_crude_leather.md) | 100% | 1 |
| [Sewn footwear](../items/boots_sewn.md) | 100% | 1 |
| [Leather boots](../items/boots1.md) | 100% | 1 |
| [Snakeskin boots](../items/boots3.md) | 100% | 1 |
| [Jewel of Fallhaven](../items/jewel_fallhaven.md) | 100% | 1 |
| [Ring of fumbling](../items/ring_fumbling.md) | 100% | 1 |
| [Mundane ring](../items/ring1.md) | 100% | 1 |
| [Polished ring](../items/ring2.md) | 100% | 1 |

## Found on

- [fallhaven_clothes](../maps/fallhaven_clothes.md)

## Quests

- [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md): stages 68

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Tailor. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/fallhaven_clothes_0.json" data-npc="Tailor" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (9 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-fallhaven_clothes_0"></span>**`fallhaven_clothes_0`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 69 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-69))* → [fallhaven_clothes](#d-fallhaven_clothes)
    - Next *(if reached stage 66 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-66))* → [fallhaven_clothes_10](#d-fallhaven_clothes_10)
    - Next *(if reached stage 68 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-68))* → [fallhaven_clothes_40](#d-fallhaven_clothes_40)
    - Next → [fallhaven_clothes](#d-fallhaven_clothes)

    <span id="d-fallhaven_clothes"></span>**`fallhaven_clothes`** Tailor: “Welcome to my shop. Please browse my selection of fine clothing and jewelry.”

    - “Let me see your wares.” → *shop opens*

    <span id="d-fallhaven_clothes_10"></span>**`fallhaven_clothes_10`** [Tailor](../monsters/tailor.md): “Hey! What are you doing here? How did you get in?” — **effects:** sets stage 68 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-68)

    - “By the door. Why?” → [fallhaven_clothes_20](#d-fallhaven_clothes_20)

    <span id="d-fallhaven_clothes_40"></span>**`fallhaven_clothes_40`** Tailor: “I know your face. How dare you to come back?”

    - “Are you sure you don't mix me with my brother?” → [fallhaven_clothes_42](#d-fallhaven_clothes_42)

    <span id="d-fallhaven_clothes_20"></span>**`fallhaven_clothes_20`** Tailor: “Nonsense. I would have noticed.”

    - Next → [fallhaven_clothes_30](#d-fallhaven_clothes_30)

    <span id="d-fallhaven_clothes_42"></span>**`fallhaven_clothes_42`** Tailor: “Andor? I know that boy all too well.”

    - “Let me see your wares.” *(if wearing [Jewel of Fallhaven](../items/jewel_fallhaven.md))* → [fallhaven_clothes_44](#d-fallhaven_clothes_44)
    - “Let me see your wares.” *(if NOT wearing [Jewel of Fallhaven](../items/jewel_fallhaven.md))* → *shop opens*

    <span id="d-fallhaven_clothes_30"></span>**`fallhaven_clothes_30`** [Tailor](../monsters/tailor.md): “Leave immediatly, or I'll call the guards!”

    - Next → [fallhaven_clothes_32](#d-fallhaven_clothes_32)

    <span id="d-fallhaven_clothes_44"></span>**`fallhaven_clothes_44`** Tailor: “You wear the stolen valuable necklace and dare lie to my face?”

    - Next → [fallhaven_clothes_30](#d-fallhaven_clothes_30)

    <span id="d-fallhaven_clothes_32"></span>**`fallhaven_clothes_32`** Tailor: “And don't dare to enter my house again!”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.8.12.1](../versions/0.8.12.1.md) | phraseID: fallhaven_clothes → fallhaven_clothes_0<br>Dialogue: 8 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tailor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tailor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tailor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tailor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `tailor` · Data from v0.8.18</small>
