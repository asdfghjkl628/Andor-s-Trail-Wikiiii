---
description: "Lodar 1 is an outdoor location in Andor's Trail, near Loneford (settlement). Enemies: Giant dungfly, Aggressive dungfly, Mudfiend, Tough mudfiend. Exits to Lodar 0, Lodar 1cave 0."
---

# Lodar 1

<div class="infobox" markdown>

| | |
|---|---|
| **Map ID** | `lodar1` |
| **Region** | Near Loneford (settlement) |
| **Type** | Outdoors |
| **Size** | 17×12 tiles |
| **World map** | [World 1](index.md) |
| **Introduced** | v0.7.0 or earlier |
| **Enemy types** | 4 |
| **Quests** | 0 |

</div>

**Lodar 1** is an outdoor map, near Loneford (settlement). It has no NPCs and 4 kinds of enemy. Exits lead to Lodar 0, Lodar 1cave 0.

## Map

<div class="map-legend" markdown="0"><label class="lg"><input type="checkbox" data-t="spawn" checked><span class="sw sw-spawn"></span><b>Red</b>&nbsp;Monsters / NPCs</label><label class="lg"><input type="checkbox" data-t="mapchange" checked><span class="sw sw-mapchange"></span><b>Blue</b>&nbsp;Exit to another map</label><label class="lg"><input type="checkbox" data-t="container" checked><span class="sw sw-container"></span><b>Yellow</b>&nbsp;Container (click to see contents)</label><label class="lg"><input type="checkbox" data-t="sign" checked><span class="sw sw-sign"></span><b>Purple</b>&nbsp;Sign</label><label class="lg"><input type="checkbox" data-t="rest" checked><span class="sw sw-rest"></span><b>Green</b>&nbsp;Resting place</label><label class="lg"><input type="checkbox" data-t="key" checked><span class="sw sw-key"></span><b>Orange dashed</b>&nbsp;Blocked until a quest step / item</label><label class="lg"><input type="checkbox" data-t="script"><span class="sw sw-script"></span><b>Grey dotted</b>&nbsp;Scripted event</label><label class="lg"><input type="checkbox" data-t="replace"><span class="sw sw-replace"></span><b>White dotted</b>&nbsp;Changes during a quest</label><label class="lg"><input type="checkbox" data-t="pin" checked><span class="sw sw-pin"></span><b>Numbers</b>&nbsp;Numbered key points (see the key below the map)</label></div>

<div class="map-wrap hide-script hide-replace" markdown="0"><img src="../../assets/maps/lodar1.webp" alt="Map of Lodar 1" width="544" height="384" loading="lazy"><a id="place-east" class="mo mo-mapchange" href="../lodar0/#place-west" title="Exit to Lodar 0" style="left:94.118%;top:50.000%;width:5.882%;height:8.333%"></a><a id="place-down lodar1" class="mo mo-mapchange" href="../lodar1cave0/#place-up lodar1cave0" title="Exit to Lodar 1cave 0" style="left:11.765%;top:50.000%;width:5.882%;height:8.333%"></a><span class="mo mo-spawn" title="Spawns: Aggressive dungfly, Giant dungfly" style="left:23.529%;top:25.000%;width:64.706%;height:66.667%"></span><span class="mo mo-spawn" title="Spawns: Mudfiend, Tough mudfiend" style="left:23.529%;top:41.667%;width:5.882%;height:16.667%"></span><a class="mob" href="../../monsters/dungfly2/" title="Aggressive dungfly" style="left:23.529%;top:83.333%;width:5.882%;height:8.333%"><img src="../../assets/icons/monsters/monsters_rltiles2_168.png" alt="Aggressive dungfly"></a><a class="mob" href="../../monsters/dungfly2/" title="Aggressive dungfly" style="left:76.471%;top:83.333%;width:5.882%;height:8.333%"><img src="../../assets/icons/monsters/monsters_rltiles2_168.png" alt="Aggressive dungfly"></a><a class="mob" href="../../monsters/dungfly2/" title="Aggressive dungfly" style="left:41.176%;top:33.333%;width:5.882%;height:8.333%"><img src="../../assets/icons/monsters/monsters_rltiles2_168.png" alt="Aggressive dungfly"></a><a class="mob" href="../../monsters/dungfly1/" title="Giant dungfly" style="left:70.588%;top:58.333%;width:5.882%;height:8.333%"><img src="../../assets/icons/monsters/monsters_rltiles2_168.png" alt="Giant dungfly"></a><a class="mob" href="../../monsters/dungfly2/" title="Aggressive dungfly" style="left:82.353%;top:50.000%;width:5.882%;height:8.333%"><img src="../../assets/icons/monsters/monsters_rltiles2_168.png" alt="Aggressive dungfly"></a><a class="mob" href="../../monsters/mudfiend1/" title="Mudfiend" style="left:23.529%;top:50.000%;width:5.882%;height:8.333%"><img src="../../assets/icons/monsters/monsters_ld2_133.png" alt="Mudfiend"></a><a class="pin pin-exit" href="#key-1" style="left:97.059%;top:54.167%" title="Exit (east): to [Lodar 0](lodar0.md)">1</a><a class="pin pin-exit" href="#key-2" style="left:14.706%;top:54.167%" title="Exit (cave entrance): to [Lodar 1cave 0](lodar1cave0.md)">2</a></div>

??? abstract "Key to the numbers on the map"

    | # | What | Details |
    |---|---|---|
    | <span id="key-1"></span>1 | Exit (east) | to [Lodar 0](lodar0.md) |
    | <span id="key-2"></span>2 | Exit (cave entrance) | to [Lodar 1cave 0](lodar1cave0.md) |


<p class="verified">Verified against v0.8.18 map data.</p>

## Connections

| Direction | Leads to | Region there | Map # |
|---|---|---|---|
| East | [Lodar 0](lodar0.md) | Loneford | 1 |
| Cave entrance | [Lodar 1cave 0](lodar1cave0.md) | – | 2 |

## Enemies

| Enemy | HP | Damage | Up to | Notes |
|---|---|---|---|---|
| [Giant dungfly](../monsters/dungfly1.md) | 16 | 4–5 | 5 | shares spawn with Aggressive dungfly |
| [Aggressive dungfly](../monsters/dungfly2.md) | 23 | 5–7 | 5 | shares spawn with Giant dungfly |
| [Mudfiend](../monsters/mudfiend1.md) | 37 | 4–6 | 1 | shares spawn with Tough mudfiend |
| [Tough mudfiend](../monsters/mudfiend2.md) | 41 | 5–6 | 1 | shares spawn with Mudfiend |

<small>“Up to” is the most that can be alive at once from the spawn areas on this map.</small>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.1](../versions/0.7.1.md) | Map layout or objects changed |
| [v0.7.2](../versions/0.7.2.md) | Map layout or objects changed |
| [v0.8.10](../versions/0.8.10.md) | Map layout or objects changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=lodar1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=lodar1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=lodar1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=lodar1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Map ID | `lodar1` |
    | File | `res/xml/lodar1.tmx` |
    | Size | 17×12 tiles (544×384 px) |
    | outdoors property | 1 |
    | Layers drawn | ground, objects, above |
    | Tilesets | map_bed_1, map_border_1, map_bridge_1, map_bridge_2, map_broken_1, map_cavewall_1, map_cavewall_2, map_cavewall_3, map_cavewall_4, map_chair_table_1, map_chair_table_2, map_crate_1, map_cupboard_1, map_curtain_1, map_entrance_1, map_entrance_2, map_fence_1, map_fence_2, map_fence_3, map_fence_4, map_ground_1, map_ground_2, map_ground_3, map_ground_4, map_ground_5, map_ground_6, map_ground_7, map_ground_8, map_house_1, map_house_2, map_indoor_1, map_indoor_2, map_kitchen_1, map_outdoor_1, map_pillar_1, map_pillar_2, map_plant_1, map_plant_2, map_rock_1, map_rock_2, map_roof_1, map_roof_2, map_roof_3, map_shop_1, map_sign_ladder_1, map_table_1, map_trail_1, map_transition_1, map_transition_2, map_transition_3, map_transition_4, map_transition_5, map_tree_1, map_tree_2, map_wall_1, map_wall_2, map_wall_3, map_wall_4, map_window_1, map_window_2 |
    | Map objects | mapchange: 2, spawn: 2 |
    | World map position | segment `world1`, x 232, y 309 |


<small>Data from v0.8.18</small>
