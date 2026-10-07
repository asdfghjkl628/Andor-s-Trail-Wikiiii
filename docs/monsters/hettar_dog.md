# ![](../assets/icons/monsters/monsters_dogs_3.png){ .sprite } Wolfhound

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_dogs_3.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `hettar_dog` |
| **Type** | NPC |
| **Class** | Animal |
| **HP** | 1 |
| **Found in** | Blackwater Mountain |
| **Introduced** | [v0.7.12](../versions/0.7.12.md) |

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


## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [blackwater_mountain55](../maps/blackwater_mountain55.md) | Blackwater Mountain | 1 | – |


## Quests

- [Where is Norry?](../quests/hettar_dog.md): stages 40, 50
- [hettar_dog_nd (hidden flag)](../quests/hettar_dog_nd.md): stages 1, 2

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Wolfhound. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/hettar_dog.json" data-npc="Wolfhound" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-hettar_dog"></span>**`hettar_dog`** Wolfhound: “Growl!” — **effects:** sets stage 1 of [hettar_dog_nd (hidden flag)](../quests/hettar_dog_nd.md#stage-1)

    - “Hey Norry, look here! I have some much better food for you from Hettar.” *(if hand over 1× [Wyrm meat](../items/hettar_bone.md); reached stage 2 of [hettar_dog_nd (hidden flag)](../quests/hettar_dog_nd.md#stage-2))* → [hettar_dog_10](#d-hettar_dog_10)
    - “Hey Norry, look here! I have a Wyrm steak for you from Hettar.” *(if carry 1× [Wyrm meat](../items/hettar_bone.md); NOT reached stage 2 of [hettar_dog_nd (hidden flag)](../quests/hettar_dog_nd.md#stage-2))* → [hettar_dog_50](#d-hettar_dog_50)
    - “Now run to Hettar! He is waiting for you.” *(if reached stage 40 of [Where is Norry?](../quests/hettar_dog.md#stage-40))* → [hettar_dog_20](#d-hettar_dog_20)
    - “OK, I go. Stupid dog.” → *conversation ends*

    <span id="d-hettar_dog_10"></span>**`hettar_dog_10`** [Dummy NPC](../monsters/none.md): “The wolfhound fetched the meat from your hand and devoured it greedily in a few seconds.” — **effects:** sets stage 2 of [hettar_dog_nd (hidden flag)](../quests/hettar_dog_nd.md#stage-2), sets stage 40 of [Where is Norry?](../quests/hettar_dog.md#stage-40)

    - “There, there. And now run to Hettar! He is waiting for you.” → [hettar_dog_20](#d-hettar_dog_20)

    <span id="d-hettar_dog_50"></span>**`hettar_dog_50`** Wolfhound: “Grrrowl.”

    - “Ah, I see. These monstrous bones here on the ground are delicious too.” → *conversation ends*

    <span id="d-hettar_dog_20"></span>**`hettar_dog_20`** [Dummy NPC](../monsters/none.md): “A moment later the huge wolfhound was gone.” — **effects:** removes monsters from blackwater_mountain55, spawns monsters on blackwater_mountain55, sets stage 50 of [Where is Norry?](../quests/hettar_dog.md#stage-50)




## Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hettar_dog.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hettar_dog.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hettar_dog.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hettar_dog.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `hettar_dog` |
    | Spawn group | `hettar_dog` |
    | Loot table | – |
    | Conversation | `hettar_dog` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_dogs:3` |
    | Defined in | `res/raw/monsterlist_brimhaven_2b.json` |

    Raw data:

    ```json
    {
     "id": "hettar_dog",
     "name": "Wolfhound",
     "iconID": "monsters_dogs:3",
     "monsterClass": "animal",
     "spawnGroup": "hettar_dog",
     "phraseID": "hettar_dog"
    }
    ```


<small>Data from v0.8.18</small>
