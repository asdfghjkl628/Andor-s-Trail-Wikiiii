# ![](../assets/icons/monsters/monsters_johny_2.png){ .sprite } Three-fang-elyzard

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_johny_2.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `brightport_lizardking` |
| **Type** | NPC |
| **Class** | Reptile |
| **HP** | 400 |
| **XP when killed** | 1,489 |
| **Found in** | Greenscale tribe |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 400 |
| Damage | 20 to 35 |
| Attack chance | 230 |
| Block chance | 200 |
| Damage resistance | 8 |
| Max AP | 15 |
| Attack cost | 5 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 25 |
| Critical multiplier | 2.0 |
| Crit chance | 17% |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Lizardman bone](../items/brightport_bone.md) | 30% | 1 to 2 |
| [Gold coins](../items/gold.md) | 100% | 160 to 350 |
| [King's hide](../items/brightport_kingarmor.md) | 100% | 1 |
| [Lizard skin](../items/lizard_skin.md) | 100% | 1 to 3 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [brightport_lizard1](../maps/brightport_lizard1.md) | Greenscale tribe | 1 | – |


## Quests that count kills

- [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-120) with stepping on a trigger on [brightport_cave17](../maps/brightport_cave17.md) checks that you've killed at least 1
- [The balance of scales](../quests/brightport_lizard.md#stage-32) with stepping on a trigger on [brightport_lizard1](../maps/brightport_lizard1.md) checks that you've killed at least 1


## Quests

- [The balance of scales](../quests/brightport_lizard.md): stages 40, 60, 90, 95
- [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md): stages 117, 118

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Three-fang-elyzard. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_lizardking.json" data-npc="Three-fang-elyzard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (19 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightport_lizardking"></span>**`brightport_lizardking`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 90 of [The balance of scales](../quests/brightport_lizard.md#stage-90))* → [brightport_elyzard8](#d-brightport_elyzard8)
    - Next *(if reached stage 60 of [The balance of scales](../quests/brightport_lizard.md#stage-60); NOT reached stage 95 of [The balance of scales](../quests/brightport_lizard.md#stage-95))* → [brightport_elyzard4](#d-brightport_elyzard4)
    - Next *(if reached stage 40 of [The balance of scales](../quests/brightport_lizard.md#stage-40); NOT reached stage 60 of [The balance of scales](../quests/brightport_lizard.md#stage-60))* → [brightport_elyzard1](#d-brightport_elyzard1)
    - Next *(if NOT reached stage 40 of [The balance of scales](../quests/brightport_lizard.md#stage-40))* → [brightport_elyzard](#d-brightport_elyzard)

    <span id="d-brightport_elyzard8"></span>**`brightport_elyzard8`** Three-fang-elyzard: “You are welcome here, outsider. Rest well.”


    <span id="d-brightport_elyzard4"></span>**`brightport_elyzard4`** Three-fang-elyzard: “Help the Shadow Chaplain with task, only then our trust be restored.”

    - “I helped Dominio with his task.” *(if reached stage 127 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-127))* → [brightport_elyzard5](#d-brightport_elyzard5)

    <span id="d-brightport_elyzard1"></span>**`brightport_elyzard1`** Three-fang-elyzard: “Outsider, have you returned with the bones?”

    - “Yes, 13 as promised.” *(if hand over 13× [Lizardman bone](../items/brightport_bone.md))* → [brightport_elyzard2](#d-brightport_elyzard2)
    - “Not yet.” → [brightport_elyzard0_1](#d-brightport_elyzard0_1)

    <span id="d-brightport_elyzard"></span>**`brightport_elyzard`** Three-fang-elyzard: “I have heard from Emyro. You come before me, but there can be no talk before you return what the witch stole!”

    - “I swear to return what was taken from you, what should I do?” → [brightport_elyzard0_0](#d-brightport_elyzard0_0)
    - “I've changed my mind, we will talk with our swords!” → [brightport_lizardkingfight](#d-brightport_lizardkingfight)

    <span id="d-brightport_elyzard5"></span>**`brightport_elyzard5`** Three-fang-elyzard: “The spirits of our kin see your worth, outsider. Accept this gift from our tribe's great treasures.” — **effects:** sets stage 90 of [The balance of scales](../quests/brightport_lizard.md#stage-90), gives 1× [Argentscale diadem](../items/brightport_crown.md)

    - Next → [brightport_elyzard6](#d-brightport_elyzard6)

    <span id="d-brightport_elyzard2"></span>**`brightport_elyzard2`** Three-fang-elyzard: “We thank you outsider. But not enough to repair our trust.”

    - Next → [brightport_elyzard3](#d-brightport_elyzard3)

    <span id="d-brightport_elyzard0_1"></span>**`brightport_elyzard0_1`** Three-fang-elyzard: “Our fangs hunger for retribution and our claws follow swiftly, we will not wait for long.”


    <span id="d-brightport_elyzard0_0"></span>**`brightport_elyzard0_0`** [Dummy NPC](../monsters/none.md): “The lizard king's advisor interjects”

    - Next → [brightport_elyzard0](#d-brightport_elyzard0)

    <span id="d-brightport_lizardkingfight"></span>**`brightport_lizardkingfight`** [Three-fang-elyzard](../monsters/brightport_lizardking.md): “Despicable creature, you show your true self before us. Your days end!” — **effects:** faction “lizardman” set to -110, sets stage 118 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-118), faction “lizardfight” set to -110

    - Next *(if NOT reached stage 117 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-117))* → [brightport_lizardfight](#d-brightport_lizardfight)

    <span id="d-brightport_elyzard6"></span>**`brightport_elyzard6`** Three-fang-elyzard: “Our trust is given, what else do you wish to ask for.”

    - “Would you agree to trade Bryma the bones of animals you hunt?” *(if reached stage 221 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-221))* → [brightport_elyzard7](#d-brightport_elyzard7)
    - “Peace is enough.” → [brightport_elyzard9](#d-brightport_elyzard9)

    <span id="d-brightport_elyzard3"></span>**`brightport_elyzard3`** Three-fang-elyzard: “Speak with Dominio our Shadow chaplain, he will tell you the task.” — **effects:** sets stage 60 of [The balance of scales](../quests/brightport_lizard.md#stage-60)


    <span id="d-brightport_elyzard0"></span>**`brightport_elyzard0`** [Tail-swing-tyliad](../monsters/brightport_lizardadvisor.md): “Minion of the witch! From our burial chamber 13 bones of our ancestors were shamelessly stolen. Return them to us or we will return them ourselves.” — **effects:** sets stage 40 of [The balance of scales](../quests/brightport_lizard.md#stage-40)


    <span id="d-brightport_lizardfight"></span>**`brightport_lizardfight`** *(silent check: the first matching branch below is taken)* — **effects:** spawns monsters on brightport_cave17, spawns monsters on brightport_cave17, spawns monsters on brightport_cave17, spawns monsters on brightport_lizard1, sets stage 117 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-117), faction “lizardfight” set to -111, removes monsters from brightport_lizard3, removes monsters from brightport_lizard2, removes monsters from brightport_lizard3, removes monsters from brightport_lizard1, removes monsters from brightport_lizard1

    - Next *(if NOT reached stage 118 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-118))* → [brightport_lizardfight1_1](#d-brightport_lizardfight1_1)
    - Next *(if reached stage 118 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-118))* → [brightport_lizardkingfight1](#d-brightport_lizardkingfight1)

    <span id="d-brightport_elyzard7"></span>**`brightport_elyzard7`** Three-fang-elyzard: “It is agreed. Now go and rest well, we welcome you.” — **effects:** sets stage 95 of [The balance of scales](../quests/brightport_lizard.md#stage-95)


    <span id="d-brightport_elyzard9"></span>**`brightport_elyzard9`** Three-fang-elyzard: “It is agreed. Now go and rest well, we welcome you.”


    <span id="d-brightport_lizardfight1_1"></span>**`brightport_lizardfight1_1`** Three-fang-elyzard: “As you make your way to the settlement, you freeze in your step, a loud hissing sound resounding in your ears.”

    - Next → [brightport_lizardfight1](#d-brightport_lizardfight1)

    <span id="d-brightport_lizardkingfight1"></span>**`brightport_lizardkingfight1`** *(silent check: the first matching branch below is taken)*

    - branch 1 → *fight starts*

    <span id="d-brightport_lizardfight1"></span>**`brightport_lizardfight1`** [Lizard warrior](../monsters/brightport_lizard00.md): “Your days end here, troublesome intruder!”

    - “I will polish my blade in your blood.” → *conversation ends*
    - “Is it too late to apologize?” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 19 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_lizardking.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_lizardking.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_lizardking.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_lizardking.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `brightport_lizardking` |
    | Spawn group | `brightport_lizardking` |
    | Loot table | `brightport_greenlizardking` |
    | Conversation | `brightport_lizardking` |
    | Faction | `lizardman` |
    | Movement | helpOthers |
    | Icon | `monsters_johny:2` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_lizardking",
     "name": "Three-fang-elyzard",
     "iconID": "monsters_johny:2",
     "maxHP": 400,
     "maxAP": 15,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "reptile",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 20,
      "max": 35
     },
     "faction": "lizardman",
     "phraseID": "brightport_lizardking",
     "droplistID": "brightport_greenlizardking",
     "attackCost": 5,
     "attackChance": 230,
     "criticalSkill": 25,
     "criticalMultiplier": 2.0,
     "blockChance": 200,
     "damageResistance": 8
    }
    ```


<small>Data from v0.8.18</small>
