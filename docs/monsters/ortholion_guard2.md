# ![](../assets/icons/monsters/monsters_omi2_12.png){ .sprite } Feygard scout

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_omi2_12.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `ortholion_guard2` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Prim |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

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


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Minor potion of health](../items/health_minor2.md) | 100% | 1 to 10 |
| [Regular potion of health](../items/health.md) | 100% | 1 to 10 |
| [Animal hair](../items/hair.md) | 100% | 1 to 10 |
| [Rough ring of damage](../items/ring_rough_damage.md) | 100% | 0 to 3 |
| [Iqhan pendant](../items/iqhan_pendant.md) | 33.3333% | 0 to 2 |
| [Runed scepter](../items/scptr_runed.md) | 33.3333% | 0 to 2 |
| [Superior leather boots](../items/boots2.md) | 25% | 1 to 2 |
| [Black axe](../items/axe_black1.md) | 25% | 1 |
| [Redfoot beast hair](../items/redfthair.md) | 25% | 1 to 10 |
| [Bottle of mountain water](../items/bwm_water1.md) | 20% | 0 to 10 |
| [Large bottle of mountain water](../items/bwm_water2.md) | 20% | 1 to 10 |
| [Jinxed ring of damage resistance](../items/ring_jinxed1.md) | 20% | 1 to 3 |
| [Cold Lava Rock](../items/lava_rock_cold.md) | 10% | 1 to 10 |
| [Steel broadsword](../items/broadsword2.md) | 10% | 1 |
| [Blackwater brew](../items/bwm_brew.md) | 10% | 1 to 20 |
| [Sharp steel rapier](../items/rapier_steel.md) | 5% | 1 |
| [Venomfang dirk](../items/venomfang_dagger.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [blackwater_mountain29](../maps/blackwater_mountain29.md) | Prim | 1 | appears later in a quest |


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Feygard scout. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/ortholion_guard6_1.json" data-npc="Feygard scout" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ortholion_guard6_1"></span>**`ortholion_guard6_1`** Feygard scout: “*Looks nervous* Kid! Go back now, it's really dangerous past here.”

    - “Come with me, we'll cover each other's backs.” → [ortholion_guard6_2](#d-ortholion_guard6_2)
    - “Can you clear the way for me then?” → [ortholion_guard6_2](#d-ortholion_guard6_2)
    - “Where's the general?” → [ortholion_guard6_5](#d-ortholion_guard6_5)

    <span id="d-ortholion_guard6_2"></span>**`ortholion_guard6_2`** Feygard scout: “No way! I have a home to go back to you know? And you probably do too.”

    - “Step aside then, you're in my way.” → *conversation ends*
    - “What are you scared of?” → [ortholion_guard6_3](#d-ortholion_guard6_3)

    <span id="d-ortholion_guard6_5"></span>**`ortholion_guard6_5`** Feygard scout: “We...We haven't seen him. The other scout entered the tunnel... *looks back* Two men are guarding the rearback. Something's off with this place.”

    - “What's wrong with those passages?” → [ortholion_guard6_3](#d-ortholion_guard6_3)
    - “I will look for him, bye.” → *conversation ends*

    <span id="d-ortholion_guard6_3"></span>**`ortholion_guard6_3`** Feygard scout: “*stares at the tunnels* They're dark, stinky, and narrow. We were going to pass in line through them. But seconds after the other scout entered, a horrible scream came from inside there... It was him, I'm sure!”

    - Next → [ortholion_guard6_4](#d-ortholion_guard6_4)

    <span id="d-ortholion_guard6_4"></span>**`ortholion_guard6_4`** Feygard scout: “...I ran away. I am sure there's something dangerous inside there. Really dangerous! Dangerous enough to make a Feygard soldier scream that way.”

    - “I'll be careful. Thanks.” → *conversation ends*
    - “It was surely a cave rat. I will find out now.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `ortholion_guard2` |
    | Spawn group | `ortholion_guard2` |
    | Loot table | `ortholion_guard2` |
    | Conversation | `ortholion_guard6_1` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_omi2:12` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "ortholion_guard2",
     "name": "Feygard scout",
     "iconID": "monsters_omi2:12",
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "spawnGroup": "ortholion_guard2",
     "faction": "",
     "phraseID": "ortholion_guard6_1",
     "droplistID": "ortholion_guard2"
    }
    ```


<small>Data from v0.8.18</small>
