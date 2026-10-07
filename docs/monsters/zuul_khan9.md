# ![](../assets/icons/monsters/monsters_rltiles2_88.png){ .sprite } Zuul'khan

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_88.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `zuul_khan9` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 175 |
| **XP when killed** | 214 |
| **Found in** | mushroom_m3_1 |
| **Introduced** | [v0.7.13](../versions/0.7.13.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 175 |
| Damage | 3 to 6 |
| Attack chance | 110 |
| Block chance | 40 |
| Damage resistance | 0 |
| Max AP | 20 |
| Attack cost | 5 AP |
| Attacks per turn | 4 |
| Move cost | 6 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Bone](../items/bone.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [mushroom_m3_1](../maps/mushroom_m3_1.md) | – | 1 | – |


## Quests that count kills

- [Fungi panic](../quests/fungi_panic.md#stage-169) with [Black fog](../monsters/zuul_khan9_blocker.md) ([mushroom_m3_1](../maps/mushroom_m3_1.md)) checks that you've killed at least 1
- A conversation with [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) checks that you've killed at least 1
- A conversation with [Nimael](../monsters/nimael.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) checks that you've killed at least 1


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Zuul'khan. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/zuul_khan9.json" data-npc="Zuul&#x27;khan" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (7 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-zuul_khan9"></span>**`zuul_khan9`** Zuul'khan: “You again! How did you get into here?”

    - “I could ask you the same.” → [zuul_khan9_10](#d-zuul_khan9_10)

    <span id="d-zuul_khan9_10"></span>**`zuul_khan9_10`** Zuul'khan: “May I finally practice my black magic in peace?”

    - “No, not if I can help it. By the way - your book looks strange.” → [zuul_khan9_20](#d-zuul_khan9_20)

    <span id="d-zuul_khan9_20"></span>**`zuul_khan9_20`** Zuul'khan: “What do you mean?”

    - “It is a cookbook. I see lots of delicious recipes.” → [zuul_khan9_30](#d-zuul_khan9_30)

    <span id="d-zuul_khan9_30"></span>**`zuul_khan9_30`** Zuul'khan: “Oh that. That's a good cover. I got the book from a 'friend'. In between there are recipes of a completely different kind.”

    - “You mean these strange letters next to the recipe of the Delicious Mushroom Soup?” → [zuul_khan9_40](#d-zuul_khan9_40)

    <span id="d-zuul_khan9_40"></span>**`zuul_khan9_40`** Zuul'khan: “Be glad that you can't decipher these letters. They are dangerous.”

    - Next → [zuul_khan9_42](#d-zuul_khan9_42)

    <span id="d-zuul_khan9_42"></span>**`zuul_khan9_42`** Zuul'khan: “It takes great power to tame these spells. My fungi leader grows in strength every day!”

    - “At school I was good at spelling: A B C ...” → [zuul_khan9_90](#d-zuul_khan9_90)

    <span id="d-zuul_khan9_90"></span>**`zuul_khan9_90`** Zuul'khan: “I've had enough of your cheekiness now. These were your last words!”

    - “We'll see...” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 7 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=zuul_khan9.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=zuul_khan9.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=zuul_khan9.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=zuul_khan9.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `zuul_khan9` |
    | Spawn group | `zuul_khan9` |
    | Loot table | `zuul_khan9` |
    | Conversation | `zuul_khan9` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:88` |
    | Defined in | `res/raw/monsterlist_fungi_panic.json` |

    Raw data:

    ```json
    {
     "id": "zuul_khan9",
     "name": "Zuul'khan",
     "iconID": "monsters_rltiles2:88",
     "maxHP": 175,
     "maxAP": 20,
     "moveCost": 6,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 3,
      "max": 6
     },
     "spawnGroup": "zuul_khan9",
     "phraseID": "zuul_khan9",
     "droplistID": "zuul_khan9",
     "attackCost": 5,
     "attackChance": 110,
     "blockChance": 40
    }
    ```


<small>Data from v0.8.18</small>
