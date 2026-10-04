# ![](../assets/icons/monsters/monsters_karvis2_5.png){ .sprite } Old hermit

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_karvis2_5.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `dds_oldhermit` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | waytolake12 |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

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
| [waytolake12](../maps/waytolake12.md) | – | 1 | – |


## Quests

- [Darkness in the Daylight](../quests/darkness_in_daylight.md): stages 170, 180

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Old hermit. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/dds_oldhermit.json" data-npc="Old hermit" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (9 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-dds_oldhermit"></span>**`dds_oldhermit`** Old hermit: “Go away. Leave me alone.”

    - Next *(if reached stage 160 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-160); NOT reached stage 180 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-180))* → [dds_oldhermit_12](#d-dds_oldhermit_12)

    <span id="d-dds_oldhermit_12"></span>**`dds_oldhermit_12`** Old hermit: “I thought hiding on this hill would ensure no riff-raff would find me.”

    - Next → [dds_oldhermit_14](#d-dds_oldhermit_14)

    <span id="d-dds_oldhermit_14"></span>**`dds_oldhermit_14`** Old hermit: “This tower has long been deserted after all.”

    - “I'm no riff-raff, and I'm not here to see the sights. I've come to meet you.” → [dds_oldhermit_20](#d-dds_oldhermit_20)

    <span id="d-dds_oldhermit_20"></span>**`dds_oldhermit_20`** Old hermit: “Leave me alone. I am no one.”

    - “You are not no one. You have a copy of Azimyran Secrets.” → [dds_oldhermit_30](#d-dds_oldhermit_30)

    <span id="d-dds_oldhermit_30"></span>**`dds_oldhermit_30`** Old hermit: “So? I'm not giving it to anyone. I'm too old to be threatened. And I want nothing.” — **effects:** sets stage 170 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-170)

    - “Can I at least read it? I need to copy only one chant.” → [dds_oldhermit_40](#d-dds_oldhermit_40)

    <span id="d-dds_oldhermit_40"></span>**`dds_oldhermit_40`** Old hermit: “Kazaul again, eh?”

    - “How did you know?” → [dds_oldhermit_50](#d-dds_oldhermit_50)

    <span id="d-dds_oldhermit_50"></span>**`dds_oldhermit_50`** Old hermit: “Hehe. I'm a hermit, but not senile. In fact, I moved here to stay away from all those holier-than-thou morons: Geomyr, Shadow, Elythom ...”

    - “Sounds oddly appealing. Can I copy the rest of the chant?” → [dds_oldhermit_60](#d-dds_oldhermit_60)

    <span id="d-dds_oldhermit_60"></span>**`dds_oldhermit_60`** Old hermit: “Sure. Here you go.” — **effects:** sets stage 180 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-180)

    - “[Flipping through the pages] Ah, here's the rest of chant. [Talking to the hermit]: Thanks! Here's the book back.” → [dds_oldhermit_70](#d-dds_oldhermit_70)

    <span id="d-dds_oldhermit_70"></span>**`dds_oldhermit_70`** Old hermit: “Welcome! Try and not disturb me again, if you can.”

    - “Unless my brother comes this way, we won't disturb you again.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 9 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_oldhermit.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_oldhermit.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_oldhermit.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_oldhermit.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `dds_oldhermit` |
    | Spawn group | `dds_oldhermit` |
    | Loot table | – |
    | Conversation | `dds_oldhermit` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:5` |
    | Defined in | `res/raw/monsterlist_darknessanddaylight.json` |

    Raw data:

    ```json
    {
     "id": "dds_oldhermit",
     "name": "Old hermit",
     "iconID": "monsters_karvis2:5",
     "monsterClass": "humanoid",
     "spawnGroup": "dds_oldhermit",
     "phraseID": "dds_oldhermit"
    }
    ```


<small>Data from v0.8.18</small>
