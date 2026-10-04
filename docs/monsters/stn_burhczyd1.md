# ![](../assets/icons/monsters/monsters_ld2_8.png){ .sprite } Burhczyd

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld2_8.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `stn_burhczyd1` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

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



??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `stn_burhczyd1` |
    | Spawn group | `stn_burhczyd1` |
    | Loot table | – |
    | Conversation | `stn_burhczyd1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:8` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_burhczyd1",
     "name": "Burhczyd",
     "iconID": "monsters_ld2:8",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "stn_burhczyd1"
    }
    ```


<small>Data from v0.8.18</small>
