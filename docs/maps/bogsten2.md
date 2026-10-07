# Bogsten2

<div class="infobox" markdown>

| | |
|---|---|
| **Map ID** | `bogsten2` |
| **Type** | Indoors / underground |
| **Size** | 16×21 tiles |
| **World map** | [Fungi panic](index.md) |
| **Introduced** | [v0.7.13](../versions/0.7.13.md) |
| **Enemy types** | 2 |
| **Quests** | 0 |

</div>

**Bogsten2** is an indoor map. It has no NPCs and 2 kinds of enemy. Exits lead to Bogsten0, Bogsten3.

## Map

<div class="map-legend" markdown="0"><label class="lg"><input type="checkbox" data-t="spawn" checked><span class="sw sw-spawn"></span><b>Red</b>&nbsp;Monsters / NPCs</label><label class="lg"><input type="checkbox" data-t="mapchange" checked><span class="sw sw-mapchange"></span><b>Blue</b>&nbsp;Exit to another map</label><label class="lg"><input type="checkbox" data-t="container" checked><span class="sw sw-container"></span><b>Yellow</b>&nbsp;Container (click to see contents)</label><label class="lg"><input type="checkbox" data-t="sign" checked><span class="sw sw-sign"></span><b>Purple</b>&nbsp;Sign</label><label class="lg"><input type="checkbox" data-t="rest" checked><span class="sw sw-rest"></span><b>Green</b>&nbsp;Resting place</label><label class="lg"><input type="checkbox" data-t="key" checked><span class="sw sw-key"></span><b>Orange dashed</b>&nbsp;Blocked until a quest step / item</label><label class="lg"><input type="checkbox" data-t="script"><span class="sw sw-script"></span><b>Grey dotted</b>&nbsp;Scripted event</label><label class="lg"><input type="checkbox" data-t="replace"><span class="sw sw-replace"></span><b>White dotted</b>&nbsp;Changes during a quest</label><label class="lg"><input type="checkbox" data-t="pin" checked><span class="sw sw-pin"></span><b>Numbers</b>&nbsp;Numbered key points (see the key below the map)</label></div>

<div class="map-wrap hide-script hide-replace" markdown="0"><img src="../../assets/maps/bogsten2.webp" alt="Map of Bogsten2" width="512" height="672" loading="lazy"><a id="place-exit" class="mo mo-mapchange" href="../bogsten0/#place-cave_entrance" title="Exit to Bogsten0" style="left:43.750%;top:4.762%;width:6.250%;height:4.762%"></a><a id="place-south" class="mo mo-mapchange" href="../bogsten3/#place-north" title="Exit to Bogsten3" style="left:81.250%;top:95.238%;width:6.250%;height:4.762%"></a><span class="mo mo-spawn" title="Spawns: Weak fungi" style="left:62.500%;top:14.286%;width:31.250%;height:19.048%"></span><span class="mo mo-spawn" title="Spawns: Weak fungi" style="left:12.500%;top:52.381%;width:87.500%;height:19.048%"></span><span class="mo mo-spawn" title="Spawns: Fungi" style="left:6.250%;top:61.905%;width:43.750%;height:33.333%"></span><span class="mo mo-spawn" title="Spawns: Fungi" style="left:50.000%;top:71.429%;width:43.750%;height:19.048%"></span><a class="mob" href="../../monsters/weak_fungi/" title="Weak fungi" style="left:62.500%;top:19.048%;width:6.250%;height:4.762%"><img src="../../assets/icons/monsters/monsters_gisons_3.png" alt="Weak fungi"></a><a class="mob" href="../../monsters/weak_fungi/" title="Weak fungi" style="left:31.250%;top:66.667%;width:6.250%;height:4.762%"><img src="../../assets/icons/monsters/monsters_gisons_3.png" alt="Weak fungi"></a><a class="mob" href="../../monsters/weak_fungi/" title="Weak fungi" style="left:75.000%;top:66.667%;width:6.250%;height:4.762%"><img src="../../assets/icons/monsters/monsters_gisons_3.png" alt="Weak fungi"></a><a class="mob" href="../../monsters/weak_fungi/" title="Weak fungi" style="left:31.250%;top:61.905%;width:6.250%;height:4.762%"><img src="../../assets/icons/monsters/monsters_gisons_3.png" alt="Weak fungi"></a><a class="mob" href="../../monsters/mid_fungi/" title="Fungi" style="left:31.250%;top:80.952%;width:6.250%;height:4.762%"><img src="../../assets/icons/monsters/monsters_gisons_4.png" alt="Fungi"></a><a class="mob" href="../../monsters/mid_fungi/" title="Fungi" style="left:31.250%;top:76.190%;width:6.250%;height:4.762%"><img src="../../assets/icons/monsters/monsters_gisons_4.png" alt="Fungi"></a><a class="mob" href="../../monsters/mid_fungi/" title="Fungi" style="left:56.250%;top:85.714%;width:6.250%;height:4.762%"><img src="../../assets/icons/monsters/monsters_gisons_4.png" alt="Fungi"></a><a class="mob" href="../../monsters/mid_fungi/" title="Fungi" style="left:62.500%;top:85.714%;width:6.250%;height:4.762%"><img src="../../assets/icons/monsters/monsters_gisons_4.png" alt="Fungi"></a><a class="mob" href="../../monsters/mid_fungi/" title="Fungi" style="left:62.500%;top:80.952%;width:6.250%;height:4.762%"><img src="../../assets/icons/monsters/monsters_gisons_4.png" alt="Fungi"></a><a class="pin pin-exit" href="#key-1" style="left:46.875%;top:7.143%" title="Exit (north): to [Bogsten0](../bogsten0.md)">1</a><a class="pin pin-exit" href="#key-2" style="left:84.375%;top:97.619%" title="Exit (south): to [Bogsten3](../bogsten3.md)">2</a></div>

??? abstract "Key to the numbers on the map"

    | # | What | Details |
    |---|---|---|
    | <span id="key-1"></span>1 | Exit (north) | to [Bogsten0](../bogsten0.md) |
    | <span id="key-2"></span>2 | Exit (south) | to [Bogsten3](../bogsten3.md) |


<p class="verified">Verified against v0.8.18 map data.</p>

## Connections

| Direction | Leads to | Region there | Map # |
|---|---|---|---|
| North | [Bogsten0](bogsten0.md) | Fallhaven | 1 |
| South | [Bogsten3](bogsten3.md) | – | 2 |

## Enemies

| Enemy | HP | Damage | Up to | Notes |
|---|---|---|---|---|
| [Weak fungi](../monsters/weak_fungi.md) | 20 | 1–2 | 4 | – |
| [Fungi](../monsters/mid_fungi.md) | 25 | 2–3 | 5 | – |

<small>“Up to” is the most that can be alive at once from the spawn areas on this map.</small>


## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=bogsten2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=bogsten2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=bogsten2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=bogsten2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Map ID | `bogsten2` |
    | File | `res/xml/bogsten2.tmx` |
    | Size | 16×21 tiles (512×672 px) |
    | outdoors property | – |
    | Layers drawn | ground, objects, above |
    | Tilesets | map_bed_1, map_border_1, map_bridge_1, map_broken_1, map_cavewall_1, map_cavewall_2, map_cavewall_3, map_chair_table_1, map_crate_1, map_cupboard_1, map_curtain_1, map_entrance_1, map_fence_1, map_fence_2, map_ground_1, map_ground_2, map_ground_3, map_ground_4, map_ground_5, map_ground_6, map_ground_7, map_ground_8, map_indoor_1, map_kitchen_1, map_outdoor_1, map_pillar_1, map_plant_1, map_rock_1, map_roof_1, map_roof_2, map_shop_1, map_sign_ladder_1, map_table_1, map_trail_1, map_tree_1, map_wall_1, map_wall_2, map_wall_3, map_window_1, map_window_2 |
    | Map objects | spawn: 4, mapchange: 2 |
    | World map position | segment `fungi_panic`, x 298, y 452 |


<small>Data from v0.8.18</small>
