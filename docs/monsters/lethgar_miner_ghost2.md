# ![](../assets/icons/monsters/monsters_gisons_13.png){ .sprite } Lethgar miner ghost

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_gisons_13.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `lethgar_miner_ghost2` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | undertell_1_1 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

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
| [undertell_1_1](../maps/undertell_1_1.md) | – | 1 | – |


## Quests

- [hidden_undertell (hidden flag)](../quests/undertell_hidden.md): stages 50

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Lethgar miner ghost. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/lethgar_miner_ghost2_welcome.json" data-npc="Lethgar miner ghost" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (13 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-lethgar_miner_ghost2_welcome"></span>**`lethgar_miner_ghost2_welcome`** Lethgar miner ghost: “What? A live human, down here? How? Why?”

    - “Shannal let me through.” → [lethgar_miner_ghost2_shannal_10](#d-lethgar_miner_ghost2_shannal_10)
    - “I found these ash covered dragon scales. Was this place once home to a dragon?” *(if latest stage of [The fifth master](../quests/fifth_master.md#stage-65) is 65; NOT reached stage 50 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-50); carry 1× [Ash covered dragon scales](../items/ancient_dragon_scales.md))* → [lethgar_miner_ghost2_dragon_10](#d-lethgar_miner_ghost2_dragon_10)
    - “I'm here for the Heartstone, of course!” *(if NOT reached stage 40 of [Lost treasures](../quests/nocmar.md#stage-40))* → [lethgar_miner_ghost2_heartstone_10](#d-lethgar_miner_ghost2_heartstone_10)

    <span id="d-lethgar_miner_ghost2_shannal_10"></span>**`lethgar_miner_ghost2_shannal_10`** Lethgar miner ghost: “Oh, Shannal! She's my girlfriend, you know?”

    - “Oh, really?” → [lethgar_miner_ghost2_shannal_20](#d-lethgar_miner_ghost2_shannal_20)

    <span id="d-lethgar_miner_ghost2_dragon_10"></span>**`lethgar_miner_ghost2_dragon_10`** Lethgar miner ghost: “Ah...so some of his scales remain. Then it's true - not all the old stories were lies.”

    - “Whose scales are these?” → [lethgar_miner_ghost2_dragon_20](#d-lethgar_miner_ghost2_dragon_20)

    <span id="d-lethgar_miner_ghost2_heartstone_10"></span>**`lethgar_miner_ghost2_heartstone_10`** Lethgar miner ghost: “The Heartstone? Don't speak that name down here.”

    - “Why? What's so dangerous about it?” → [lethgar_miner_ghost2_heartstone_20](#d-lethgar_miner_ghost2_heartstone_20)

    <span id="d-lethgar_miner_ghost2_shannal_20"></span>**`lethgar_miner_ghost2_shannal_20`** Lethgar miner ghost: “Well...I want her to be. I love that woman.”

    - “Does she know that?” → [lethgar_miner_ghost2_shannal_30](#d-lethgar_miner_ghost2_shannal_30)

    <span id="d-lethgar_miner_ghost2_dragon_20"></span>**`lethgar_miner_ghost2_dragon_20`** Lethgar miner ghost: “Long before the Rift tore this place apart, a great serpent of flame slept beneath the stone. Some said his breath warmed the forges. Others feared he kept the mountain alive when it should have died.”

    - “Did you ever see him yourself?” → [lethgar_miner_ghost2_dragon_30](#d-lethgar_miner_ghost2_dragon_30)
    - “Maybe those scales are just from a monster, not a dragon.” → [lethgar_miner_ghost2_dragon_40](#d-lethgar_miner_ghost2_dragon_40)

    <span id="d-lethgar_miner_ghost2_heartstone_20"></span>**`lethgar_miner_ghost2_heartstone_20`** Lethgar miner ghost: “We dug near its glow once. The air turned to ash, and our skin blistered from the inside. When we struck it, the light screamed...and then the tunnels fell quiet forever.”

    - “You mean it's cursed?” → [lethgar_miner_ghost2_heartstone_30](#d-lethgar_miner_ghost2_heartstone_30)
    - “That sounds like a story meant to scare miners.” → [lethgar_miner_ghost2_heartstone_40](#d-lethgar_miner_ghost2_heartstone_40)

    <span id="d-lethgar_miner_ghost2_shannal_30"></span>**`lethgar_miner_ghost2_shannal_30`** Lethgar miner ghost: “No way! Even after so many many years, I'm still terrified to tell her.”

    - “Wimp. Girls don't bite, well some do I guess. Good luck with that.” → *conversation ends*

    <span id="d-lethgar_miner_ghost2_dragon_30"></span>**`lethgar_miner_ghost2_dragon_30`** Lethgar miner ghost: “No. By the time I was born, he was already legend. We mined the heat, not the truth. But sometimes...the walls breathed, and the stones glowed like coals in a hearth. That was enough for me.”

    - “Then maybe the legend was real.” → [lethgar_miner_ghost2_dragon_50](#d-lethgar_miner_ghost2_dragon_50)

    <span id="d-lethgar_miner_ghost2_dragon_40"></span>**`lethgar_miner_ghost2_dragon_40`** Lethgar miner ghost: “Heh...maybe. But the Kazaul feared that heat. They sealed off the deepest tunnels where the warmth was strongest. Even they left it undisturbed - and that tells you something, doesn't it?”

    - “Maybe it does.” → [lethgar_miner_ghost2_dragon_50](#d-lethgar_miner_ghost2_dragon_50)

    <span id="d-lethgar_miner_ghost2_heartstone_30"></span>**`lethgar_miner_ghost2_heartstone_30`** Lethgar miner ghost: “Not cursed. Hungry. It drinks the warmth of living things. Leave it buried, or it will remember the taste of us.”

    - “I'll keep that in mind.” → *conversation ends*

    <span id="d-lethgar_miner_ghost2_heartstone_40"></span>**`lethgar_miner_ghost2_heartstone_40`** Lethgar miner ghost: “We thought that too. Then the ground split, and the glow swallowed our camp. Don't go looking for it, child.”

    - “Maybe you're right.” → *conversation ends*

    <span id="d-lethgar_miner_ghost2_dragon_50"></span>**`lethgar_miner_ghost2_dragon_50`** Lethgar miner ghost: “If he still lives, child, best let him sleep. Some fires burn long after they should have gone out.” — **effects:** sets stage 50 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-50)

    - “I'll remember that.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 13 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lethgar_miner_ghost2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lethgar_miner_ghost2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lethgar_miner_ghost2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lethgar_miner_ghost2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `lethgar_miner_ghost2` |
    | Spawn group | `lethgar_miner_ghost2` |
    | Loot table | – |
    | Conversation | `lethgar_miner_ghost2_welcome` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_gisons:13` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "lethgar_miner_ghost2",
     "name": "Lethgar miner ghost",
     "iconID": "monsters_gisons:13",
     "monsterClass": "humanoid",
     "phraseID": "lethgar_miner_ghost2_welcome"
    }
    ```


<small>Data from v0.8.18</small>
