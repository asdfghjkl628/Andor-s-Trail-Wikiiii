---
description: "Fields 3 is an outdoor location in Andor's Trail. NPCs: Sheep. Enemies: Grasslands snake, Tough grasslands snake. Exits to Fields 2, Fields 9."
---

# Fields 3

<div class="infobox" markdown>

| | |
|---|---|
| **Map ID** | `fields3` |
| **Type** | Outdoors |
| **Size** | 20×20 tiles |
| **World map** | [World 1](index.md) |
| **Introduced** | v0.7.0 or earlier |
| **NPCs** | 1 |
| **Enemy types** | 2 |
| **Quests** | 2 |

</div>

**Fields 3** is an outdoor map. It has 1 NPC and 2 kinds of enemy. Exits lead to Fields 2, Fields 9.

## Map

<div class="map-legend" markdown="0"><label class="lg"><input type="checkbox" data-t="spawn" checked><span class="sw sw-spawn"></span><b>Red</b>&nbsp;Monsters / NPCs</label><label class="lg"><input type="checkbox" data-t="mapchange" checked><span class="sw sw-mapchange"></span><b>Blue</b>&nbsp;Exit to another map</label><label class="lg"><input type="checkbox" data-t="container" checked><span class="sw sw-container"></span><b>Yellow</b>&nbsp;Container (click to see contents)</label><label class="lg"><input type="checkbox" data-t="sign" checked><span class="sw sw-sign"></span><b>Purple</b>&nbsp;Sign</label><label class="lg"><input type="checkbox" data-t="rest" checked><span class="sw sw-rest"></span><b>Green</b>&nbsp;Resting place</label><label class="lg"><input type="checkbox" data-t="key" checked><span class="sw sw-key"></span><b>Orange dashed</b>&nbsp;Blocked until a quest step / item</label><label class="lg"><input type="checkbox" data-t="script"><span class="sw sw-script"></span><b>Grey dotted</b>&nbsp;Scripted event</label><label class="lg"><input type="checkbox" data-t="replace"><span class="sw sw-replace"></span><b>White dotted</b>&nbsp;Changes during a quest</label><label class="lg"><input type="checkbox" data-t="pin" checked><span class="sw sw-pin"></span><b>Numbers</b>&nbsp;Numbered key points (see the key below the map)</label></div>

<div class="map-wrap hide-script hide-replace" markdown="0"><img src="../../assets/maps/fields3.webp" alt="Map of Fields 3" width="640" height="640" loading="lazy"><a id="place-east" class="mo mo-mapchange" href="../fields2/#place-west" title="Exit to Fields 2" style="left:95.000%;top:10.000%;width:5.000%;height:85.000%"></a><a id="place-south" class="mo mo-mapchange" href="../fields9/#place-north" title="Exit to Fields 9" style="left:15.000%;top:95.000%;width:85.000%;height:5.000%"></a><span class="mo mo-spawn" title="Spawns: Sheep" style="left:10.000%;top:10.000%;width:80.000%;height:80.000%"></span><span class="mo mo-spawn" title="Spawns: Grasslands snake, Tough grasslands snake" style="left:15.000%;top:15.000%;width:75.000%;height:75.000%"></span><a class="mob" href="../../monsters/sheep1/#v-lostsheep3" title="Sheep" style="left:70.000%;top:45.000%;width:5.000%;height:5.000%"><img src="../../assets/icons/monsters/monsters_karvis2_8.png" alt="Sheep"></a><a class="mob" href="../../monsters/grass_snake/" title="Grasslands snake" style="left:30.000%;top:65.000%;width:5.000%;height:5.000%"><img src="../../assets/icons/monsters/monsters_rltiles2_25.png" alt="Grasslands snake"></a><a class="mob" href="../../monsters/grass_snake/" title="Grasslands snake" style="left:80.000%;top:20.000%;width:5.000%;height:5.000%"><img src="../../assets/icons/monsters/monsters_rltiles2_25.png" alt="Grasslands snake"></a><a class="pin pin-exit" href="#key-1" style="left:97.500%;top:52.500%" title="Exit (east): to [Fields 2](fields2.md)">1</a><a class="pin pin-exit" href="#key-2" style="left:57.500%;top:97.500%" title="Exit (south): to [Fields 9](fields9.md)">2</a><a id="pin-npc-lostsheep3" class="pin pin-npc" href="#key-3" style="left:72.500%;top:47.500%" title="[Sheep](../../monsters/sheep1.md#v-lostsheep3): 2 quests">3</a></div>

??? abstract "Key to the numbers on the map"

    | # | What | Details |
    |---|---|---|
    | <span id="key-1"></span>1 | Exit (east) | to [Fields 2](fields2.md) |
    | <span id="key-2"></span>2 | Exit (south) | to [Fields 9](fields9.md) |
    | <span id="key-3"></span>3 | [Sheep](../monsters/sheep1.md#v-lostsheep3) | 2 quests |


<p class="verified">Verified against v0.8.18 map data.</p>

## Connections

| Direction | Leads to | Region there | Map # |
|---|---|---|---|
| East | [Fields 2](fields2.md) | Crossroads Guardhouse | 1 |
| South | [Fields 9](fields9.md) | Crossroads Guardhouse | 2 |

## NPCs

- [Sheep](../monsters/sheep1.md#v-lostsheep3) — can be fought — quests: [Cheap cuts](../quests/benbyr.md), [Lost sheep](../quests/tinlyn.md) (#3)

## Enemies

| Enemy | HP | Damage | Up to | Notes |
|---|---|---|---|---|
| [Grasslands snake](../monsters/grass_snake.md) | 36 | 0–6 | 2 | shares spawn with Tough grasslands snake |
| [Tough grasslands snake](../monsters/grass_snake2.md) | 38 | 1–7 | 2 | shares spawn with Grasslands snake |

<small>“Up to” is the most that can be alive at once from the spawn areas on this map.</small>

## Quests

- [Cheap cuts](../quests/benbyr.md): [Sheep](../monsters/sheep1.md#v-lostsheep3) is involved
- [Lost sheep](../quests/tinlyn.md): [Sheep](../monsters/sheep1.md#v-lostsheep3) is involved


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.1](../versions/0.7.1.md) | Map layout or objects changed |
| [v0.7.2](../versions/0.7.2.md) | Map layout or objects changed |
| [v0.8.12.1](../versions/0.8.12.1.md) | Map layout or objects changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=fields3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=fields3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=fields3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=fields3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Map ID | `fields3` |
    | File | `res/xml/fields3.tmx` |
    | Size | 20×20 tiles (640×640 px) |
    | outdoors property | 1 |
    | Layers drawn | ground, objects, above |
    | Tilesets | map_bed_1, map_border_1, map_bridge_1, map_bridge_2, map_broken_1, map_cavewall_1, map_cavewall_2, map_cavewall_3, map_cavewall_4, map_chair_table_1, map_chair_table_2, map_crate_1, map_cupboard_1, map_curtain_1, map_entrance_1, map_entrance_2, map_fence_1, map_fence_2, map_fence_3, map_fence_4, map_ground_1, map_ground_2, map_ground_3, map_ground_4, map_ground_5, map_ground_6, map_ground_7, map_ground_8, map_house_1, map_house_2, map_indoor_1, map_indoor_2, map_kitchen_1, map_outdoor_1, map_pillar_1, map_pillar_2, map_plant_1, map_plant_2, map_rock_1, map_rock_2, map_roof_1, map_roof_2, map_roof_3, map_shop_1, map_sign_ladder_1, map_table_1, map_trail_1, map_transition_1, map_transition_2, map_transition_3, map_transition_4, map_transition_5, map_tree_1, map_tree_2, map_wall_1, map_wall_2, map_wall_3, map_wall_4, map_window_1, map_window_2 |
    | Map objects | mapchange: 2, spawn: 2 |
    | World map position | segment `world1`, x 127, y 263 |


<small>Data from v0.8.18</small>
