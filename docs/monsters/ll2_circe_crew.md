# ![](../assets/icons/monsters/monsters_rltiles2_55.png){ .sprite } Crew

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_55.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `ll2_circe_crew` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
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



??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `ll2_circe_crew` |
    | Spawn group | `ll2_circe_crew` |
    | Loot table | – |
    | Conversation | `ll2_circe_crew` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:55` |
    | Defined in | `res/raw/monsterlist_lake_laeroth_2.json` |

    Raw data:

    ```json
    {
     "id": "ll2_circe_crew",
     "name": "Crew",
     "iconID": "monsters_rltiles2:55",
     "monsterClass": "humanoid",
     "spawnGroup": "ll2_circe_crew",
     "phraseID": "ll2_circe_crew"
    }
    ```


<small>Data from v0.8.18</small>
