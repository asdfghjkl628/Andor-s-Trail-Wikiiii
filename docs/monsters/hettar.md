# ![](../assets/icons/monsters/monsters_ld1_20.png){ .sprite } Little Hettar

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_20.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `hettar` |
| **Type** | NPC |
| **Class** | Humanoid |
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

- [Where is Norry?](../quests/hettar_dog.md): stages 10, 20, 30, 80, 90

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Little Hettar. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/hettar.json" data-npc="Little Hettar" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (17 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-hettar"></span>**`hettar`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 90 of [Where is Norry?](../quests/hettar_dog.md#stage-90))* → [hettar_90](#d-hettar_90)
    - branch 2 *(if reached stage 80 of [Where is Norry?](../quests/hettar_dog.md#stage-80))* → [hettar_80](#d-hettar_80)
    - branch 3 *(if reached stage 50 of [Where is Norry?](../quests/hettar_dog.md#stage-50))* → [hettar_50](#d-hettar_50)
    - branch 4 *(if reached stage 30 of [Where is Norry?](../quests/hettar_dog.md#stage-30))* → [hettar_30](#d-hettar_30)
    - branch 5 *(if reached stage 20 of [Where is Norry?](../quests/hettar_dog.md#stage-20))* → [hettar_20](#d-hettar_20)
    - branch 6 *(if reached stage 10 of [Where is Norry?](../quests/hettar_dog.md#stage-10))* → [hettar_10](#d-hettar_10)
    - branch 7 → [hettar_1](#d-hettar_1)

    <span id="d-hettar_90"></span>**`hettar_90`** Little Hettar: “My poor Norry! Why did you have to die so young? * Sob *”

    - Next → [hettar_90_10](#d-hettar_90_10)

    <span id="d-hettar_80"></span>**`hettar_80`** Little Hettar: “Thank you again a thousand times for rescuing my little Norry!”


    <span id="d-hettar_50"></span>**`hettar_50`** Little Hettar: “Haha! You know what? Norry has come back all alone! You have made all the way down unnecessarily.”

    - “Now guess who had persuaded him to do so? He was absorbed by a pile of monster bones.” → [hettar_50_10](#d-hettar_50_10)

    <span id="d-hettar_30"></span>**`hettar_30`** Little Hettar: “I can read it in your face - there is no hope for Norry.”

    - “This brute attacked me, so I had to kill it.” *(if killed 1× [Wolfhound](../monsters/hettar_dog3.md))* → [hettar_10_6](#d-hettar_10_6)
    - “This brute growled at me, but I got away and let it live.” *(if reached stage 1 of [hettar_dog_nd (hidden flag)](../quests/hettar_dog_nd.md#stage-1); NOT killed 1× [Wolfhound](../monsters/hettar_dog3.md))* → [hettar_20](#d-hettar_20)
    - “I am still searching.” → *conversation ends*

    <span id="d-hettar_20"></span>**`hettar_20`** Little Hettar: “Please go down there and look for my doggie. Maybe he is injured? Bring him back! You must!”

    - “OK, I'll do it.” *(if NOT killed 1× [Wolfhound](../monsters/hettar_dog3.md))* → [hettar_20_10](#d-hettar_20_10)
    - “This brute attacked me, so I had to kill it.” *(if killed 1× [Wolfhound](../monsters/hettar_dog3.md))* → [hettar_10_6](#d-hettar_10_6)
    - “Eh, I have to leave.” → *conversation ends*

    <span id="d-hettar_10"></span>**`hettar_10`** Little Hettar: “Please help to find Norry. He is my only friend, and he is helpless without me.”

    - “How can I help you?” → [hettar_20](#d-hettar_20)
    - “The wolfhound down there had brown fur with a white patch on the breast. He was enjoying himself gnawing some huge…” *(if reached stage 1 of [hettar_dog_nd (hidden flag)](../quests/hettar_dog_nd.md#stage-1))* → [hettar_10_4](#d-hettar_10_4)

    <span id="d-hettar_1"></span>**`hettar_1`** Little Hettar: “Norry! Nooorryyyy!”

    - “Hush! Don't make such noise with all these monsters around!” → [hettar_1_4](#d-hettar_1_4)
    - “Who is Norry?” → [hettar_1_2](#d-hettar_1_2)

    <span id="d-hettar_90_10"></span>**`hettar_90_10`** Little Hettar: “Go away! I hate you!”


    <span id="d-hettar_50_10"></span>**`hettar_50_10`** Little Hettar: “Oh. Thank you then.” — **effects:** sets stage 80 of [Where is Norry?](../quests/hettar_dog.md#stage-80)


    <span id="d-hettar_10_6"></span>**`hettar_10_6`** Little Hettar: “[Hettar fell on the floor] Nooo! What did you do?!” — **effects:** sets stage 90 of [Where is Norry?](../quests/hettar_dog.md#stage-90)


    <span id="d-hettar_20_10"></span>**`hettar_20_10`** Little Hettar: “Great! Go immediately, as long as he might be alive still.” — **effects:** sets stage 20 of [Where is Norry?](../quests/hettar_dog.md#stage-20), removes monsters from blackwater_mountain55, spawns monsters on blackwater_mountain55

    - “I hope he will follow me.” *(if NOT reached stage 30 of [Where is Norry?](../quests/hettar_dog.md#stage-30))* → [hettar_20_30](#d-hettar_20_30)
    - “I hope he will follow me.” *(if reached stage 30 of [Where is Norry?](../quests/hettar_dog.md#stage-30))* → [hettar_20_20](#d-hettar_20_20)
    - “I have no time just now. I'll be back soon.” → *conversation ends*

    <span id="d-hettar_10_4"></span>**`hettar_10_4`** Little Hettar: “This must be him! Go and get him here - be quick!”

    - “That would be of no use. This brute had attacked me, so I had to kill it.” *(if killed 1× [Wolfhound](../monsters/hettar_dog3.md))* → [hettar_10_6](#d-hettar_10_6)
    - “This brute growled at me, but I got away unharmed.” *(if NOT killed 1× [Wolfhound](../monsters/hettar_dog3.md))* → [hettar_20](#d-hettar_20)
    - “Eh, I have to leave.” → *conversation ends*

    <span id="d-hettar_1_4"></span>**`hettar_1_4`** Little Hettar: “I can see these Gornauds myself. That's why I must find Norry urgently. Nooorryyyy!”

    - “Who is Norry?” → [hettar_1_2](#d-hettar_1_2)

    <span id="d-hettar_1_2"></span>**`hettar_1_2`** Little Hettar: “Norry is my little doggie. He fell down the steep slope and has not found his way back yet.” — **effects:** sets stage 10 of [Where is Norry?](../quests/hettar_dog.md#stage-10)

    - “Oh dear.” → [hettar_10](#d-hettar_10)
    - “A dog! He will be back soon... I better go now.” → *conversation ends*
    - “I have seen a great wolfhound down there a short while ago. But you say you are missing a little doggie.” *(if reached stage 1 of [hettar_dog_nd (hidden flag)](../quests/hettar_dog_nd.md#stage-1))* → [hettar_10](#d-hettar_10)

    <span id="d-hettar_20_30"></span>**`hettar_20_30`** Little Hettar: “Good that you have mentioned it. I'll give you a nice raw piece of Wyrm meat that I have as food for Norry. He loves them.” — **effects:** sets stage 30 of [Where is Norry?](../quests/hettar_dog.md#stage-30), gives 1× [Wyrm meat](../items/hettar_bone.md)


    <span id="d-hettar_20_20"></span>**`hettar_20_20`** Little Hettar: “I gave you my last piece of Wyrm meat for Norry. Did you lose it?”




## Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added<br>Dialogue: 17 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hettar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hettar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hettar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hettar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `hettar` |
    | Spawn group | `hettar` |
    | Loot table | – |
    | Conversation | `hettar` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:20` |
    | Defined in | `res/raw/monsterlist_brimhaven_2b.json` |

    Raw data:

    ```json
    {
     "id": "hettar",
     "name": "Little Hettar",
     "iconID": "monsters_ld1:20",
     "monsterClass": "humanoid",
     "spawnGroup": "hettar",
     "phraseID": "hettar"
    }
    ```


<small>Data from v0.8.18</small>
