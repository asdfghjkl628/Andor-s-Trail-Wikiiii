# ![](../assets/icons/monsters/monsters_men_4.png){ .sprite } Tharal

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_4.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `tharal` |
| **Type** | Shopkeeper |
| **Class** | Humanoid |
| **HP** | 1 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Minor potion of health](../items/health_minor2.md) | 100% | 10 |
| [Regular potion of health](../items/health.md) | 100% | 10 |
| [Major potion of health](../items/health_major2.md) | 100% | 10 |
| [Lesser shielding necklace](../items/necklace_shield_0.md) | 100% | 1 |
| [Crude ring of surehit](../items/ring_crude_surehit.md) | 100% | 1 |
| [Rough ring of damage](../items/ring_rough_damage.md) | 100% | 1 |
| [Crude ring of block](../items/ring_crude_block.md) | 100% | 1 |
| [Rough ring of life force](../items/ring_rough_life.md) | 100% | 1 |
| [Ring of damage +1](../items/ring_dmg1.md) | 100% | 1 |
| [Ring of surehit](../items/ring_atkch1.md) | 100% | 1 |
| [Ring of life force](../items/ring_life.md) | 100% | 1 |

## Quests

- [Disallowed substance](../quests/bonemeal.md): stages 20, 30
- [Taste is everything](../quests/antifoodp.md): stages 10

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Tharal. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/tharal1.json" data-npc="Tharal" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (12 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-tharal1"></span>**`tharal1`** Tharal: “Walk in the glow of the Shadow, my child.”

    - “Do you have anything to trade?” → *shop opens*
    - “What can you tell me about bonemeal?” *(if reached stage 10 of [Disallowed substance](../quests/bonemeal.md#stage-10))* → [tharal_bonemeal_select](#d-tharal_bonemeal_select)
    - “Do you have anything to help against food-poisoning?” → [tharal_antifoodp1](#d-tharal_antifoodp1)

    <span id="d-tharal_bonemeal_select"></span>**`tharal_bonemeal_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 30 of [Disallowed substance](../quests/bonemeal.md#stage-30))* → [tharal_bonemeal4](#d-tharal_bonemeal4)
    - branch 2 → [tharal_bonemeal1](#d-tharal_bonemeal1)

    <span id="d-tharal_antifoodp1"></span>**`tharal_antifoodp1`** Tharal: “No, sorry. I hear that the potion-maker in Fallhaven can create something to help against that though.”

    - Next → [tharal_antifoodp2](#d-tharal_antifoodp2)

    <span id="d-tharal_bonemeal4"></span>**`tharal_bonemeal4`** Tharal: “Oh yes, bonemeal. Mixed with the right components it can be one of the most effective healing agents around.”

    - Next → [tharal_bonemeal5](#d-tharal_bonemeal5)

    <span id="d-tharal_bonemeal1"></span>**`tharal_bonemeal1`** Tharal: “Bonemeal? We shouldn't talk about that. Lord Geomyr issued a decree. It's not allowed anymore.”

    - “Please?” → [tharal_bonemeal2_1](#d-tharal_bonemeal2_1)

    <span id="d-tharal_antifoodp2"></span>**`tharal_antifoodp2`** Tharal: “You should go see him and ask if he has anything to help against that. He can probably help you.” — **effects:** sets stage 10 of [Taste is everything](../quests/antifoodp.md#stage-10)

    - “Thanks, I'll go see him.” → [tharal1](#d-tharal1)

    <span id="d-tharal_bonemeal5"></span>**`tharal_bonemeal5`** Tharal: “We used to use it extensively before. But now that bastard Lord Geomyr has banned all use of it.”

    - Next → [tharal_bonemeal6](#d-tharal_bonemeal6)

    <span id="d-tharal_bonemeal2_1"></span>**`tharal_bonemeal2_1`** Tharal: “No, we really shouldn't talk about that.”

    - “Oh come on.” → [tharal_bonemeal2](#d-tharal_bonemeal2)

    <span id="d-tharal_bonemeal6"></span>**`tharal_bonemeal6`** Tharal: “How am I supposed to heal people now? Using regular healing potions? Bah, they're so ineffective.”

    - Next → [tharal_bonemeal7](#d-tharal_bonemeal7)

    <span id="d-tharal_bonemeal2"></span>**`tharal_bonemeal2`** Tharal: “Well if you really are that persistent. Bring me 5 insect wings that I can use for making potions and maybe we can talk more.” — **effects:** sets stage 20 of [Disallowed substance](../quests/bonemeal.md#stage-20)

    - “Here, I have the insect wings.” *(if hand over 5× [Insect wing](../items/insectwing.md))* → [tharal_bonemeal3](#d-tharal_bonemeal3)
    - “OK, I'll bring them.” → *conversation ends*

    <span id="d-tharal_bonemeal7"></span>**`tharal_bonemeal7`** Tharal: “I know someone that still has a supply of bonemeal if you are interested. Go talk to Thoronir, a fellow priest in Fallhaven. Tell him my password 'Glow of the Shadow'.”

    - “Thanks, bye.” → *conversation ends*

    <span id="d-tharal_bonemeal3"></span>**`tharal_bonemeal3`** Tharal: “Thanks kid. I knew I could count on you.” — **effects:** sets stage 30 of [Disallowed substance](../quests/bonemeal.md#stage-30)

    - Next → [tharal_bonemeal4](#d-tharal_bonemeal4)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 4 lines changed<br>· text: “I know someone that still has a supply of Bonemeal if you are interes…” → “I know someone that still has a supply of bonemeal if you are interes…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tharal.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tharal.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tharal.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tharal.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `tharal` |
    | Spawn group | `tharal` |
    | Loot table | `shop_tharal` |
    | Conversation | `tharal1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:4` |
    | Defined in | `res/raw/monsterlist_crossglen_npcs.json` |

    Raw data:

    ```json
    {
     "id": "tharal",
     "name": "Tharal",
     "iconID": "monsters_men:4",
     "monsterClass": "humanoid",
     "spawnGroup": "tharal",
     "phraseID": "tharal1",
     "droplistID": "shop_tharal"
    }
    ```


<small>Data from v0.8.18</small>
