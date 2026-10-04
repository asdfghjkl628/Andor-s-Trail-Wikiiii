# scores

!!! info "Hidden story flag"
    An internal quest the game uses to track your progress behind the scenes. It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `scores` |
| **In journal** | No (hidden flag) |
| **Stages** | 53 |
| **Started by** | stepping on a trigger on [debugmap](../maps/debugmap.md), stepping on a trigger on [fallhaven_church](../maps/fallhaven_church.md) |
| **Related quests** | 4 |

</div>

!!! history "Version note"
    From v0.8.16.1, this quest could not be completed: it had no ending yet. It became completable in [v0.8.17](../versions/0.8.17.md).

## Overview

> Shadow score fixed

## Prerequisites to start

Start with stepping on a trigger on [debugmap](../maps/debugmap.md). Required:

- eaten 1000+ bonemeals


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [Thief apprentice](Thieves01.md#stage-50) | stage 50 there needs stage 18 here |
| Unlocks | [Disallowed substance](bonemeal.md#stage-40) | stage 40 there needs stage 18 here |
| Unlocks | [Disallowed substance](bonemeal.md#stage-50) | stage 50 there needs stage 18 here |
| Unlocks | [Disallowed substance](bonemeal.md#stage-100) | stage 100 there needs stage 18 here |
| Unlocks | [Disallowed substance](bonemeal.md#stage-110) | stage 110 there needs stage 18 here |
| Unlocks | [Key of Luthor](bucus.md#stage-20) | stage 20 there needs stage 18 here |
| Unlocks | [Thieves Hidden (hidden flag)](thieves_hidden.md#stage-80) | stage 80 there needs stage 18 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Shadow score fixed | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-11"></span>11 | Pro Shadow replies should be surpressed | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-12"></span>12 | Absolute Shadow hater<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Debugmap](../maps/debugmap.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fallhaven church](../maps/fallhaven_church.md).</span> | stepping on a trigger on [debugmap](../maps/debugmap.md) | – | clears stage 13 of [scores (hidden flag)](../quests/scores.md#stage-13)<br>clears stage 15 of [scores (hidden flag)](../quests/scores.md#stage-15)<br>clears stage 17 of [scores (hidden flag)](../quests/scores.md#stage-17)<br>clears stage 18 of [scores (hidden flag)](../quests/scores.md#stage-18) |
| <span id="stage-13"></span>13 | Shadow hater | stepping on a trigger on [debugmap](../maps/debugmap.md) | – | clears stage 12 of [scores (hidden flag)](../quests/scores.md#stage-12)<br>clears stage 15 of [scores (hidden flag)](../quests/scores.md#stage-15)<br>clears stage 17 of [scores (hidden flag)](../quests/scores.md#stage-17)<br>clears stage 18 of [scores (hidden flag)](../quests/scores.md#stage-18) |
| <span id="stage-15"></span>15 | Balanced Shadow feelings | stepping on a trigger on [debugmap](../maps/debugmap.md) | – | faction “factionCountShadow” set to 0<br>faction “factionCountThieves” set to 0<br>faction “scoreShadow” set to 0<br>faction “scoreFeygard” set to 0<br>faction “scoreThieves” set to 0<br>faction “scoreShadow2” set to 0<br>faction “scoreFeygard2” set to 0<br>faction “scoreThieves2” set to 0<br>faction “scoreShadowFeygard” set to 0<br>clears stage 11 of [scores (hidden flag)](../quests/scores.md#stage-11)<br>clears stage 13 of [scores (hidden flag)](../quests/scores.md#stage-13)<br>clears stage 17 of [scores (hidden flag)](../quests/scores.md#stage-17)<br>clears stage 18 of [scores (hidden flag)](../quests/scores.md#stage-18)<br>clears stage 21 of [scores (hidden flag)](../quests/scores.md#stage-21)<br>clears stage 23 of [scores (hidden flag)](../quests/scores.md#stage-23)<br>clears stage 27 of [scores (hidden flag)](../quests/scores.md#stage-27)<br>clears stage 28 of [scores (hidden flag)](../quests/scores.md#stage-28)<br>clears stage 31 of [scores (hidden flag)](../quests/scores.md#stage-31)<br>clears stage 33 of [scores (hidden flag)](../quests/scores.md#stage-33)<br>clears stage 37 of [scores (hidden flag)](../quests/scores.md#stage-37)<br>clears stage 38 of [scores (hidden flag)](../quests/scores.md#stage-38)<br>clears stage 101 of [scores (hidden flag)](../quests/scores.md#stage-101)<br>clears stage 102 of [scores (hidden flag)](../quests/scores.md#stage-102)<br>clears stage 12 of [scores (hidden flag)](../quests/scores.md#stage-12) |
| <span id="stage-17"></span>17 | Shadow fan | stepping on a trigger on [debugmap](../maps/debugmap.md) | – | clears stage 12 of [scores (hidden flag)](../quests/scores.md#stage-12)<br>clears stage 13 of [scores (hidden flag)](../quests/scores.md#stage-13)<br>clears stage 15 of [scores (hidden flag)](../quests/scores.md#stage-15)<br>clears stage 18 of [scores (hidden flag)](../quests/scores.md#stage-18) |
| <span id="stage-18"></span>18 | Absolute Shadow fan | stepping on a trigger on [debugmap](../maps/debugmap.md) | – | clears stage 12 of [scores (hidden flag)](../quests/scores.md#stage-12)<br>clears stage 13 of [scores (hidden flag)](../quests/scores.md#stage-13)<br>clears stage 15 of [scores (hidden flag)](../quests/scores.md#stage-15)<br>clears stage 17 of [scores (hidden flag)](../quests/scores.md#stage-17) |
| <span id="stage-20"></span>20 | Feygard score fixed | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-21"></span>21 | Pro Feygard replies should be surpressed | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-22"></span>22 | Absolute Feygard hater<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Debugmap](../maps/debugmap.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fallhaven church](../maps/fallhaven_church.md).</span> | stepping on a trigger on [debugmap](../maps/debugmap.md) | stage 10 | clears stage 23 of [scores (hidden flag)](../quests/scores.md#stage-23)<br>clears stage 25 of [scores (hidden flag)](../quests/scores.md#stage-25)<br>clears stage 27 of [scores (hidden flag)](../quests/scores.md#stage-27)<br>clears stage 28 of [scores (hidden flag)](../quests/scores.md#stage-28) |
| <span id="stage-23"></span>23 | Feygard hater | stepping on a trigger on [debugmap](../maps/debugmap.md) | stage 10 | clears stage 22 of [scores (hidden flag)](../quests/scores.md#stage-22)<br>clears stage 25 of [scores (hidden flag)](../quests/scores.md#stage-25)<br>clears stage 27 of [scores (hidden flag)](../quests/scores.md#stage-27)<br>clears stage 28 of [scores (hidden flag)](../quests/scores.md#stage-28) |
| <span id="stage-25"></span>25 | Balanced Feygard feelings | stepping on a trigger on [debugmap](../maps/debugmap.md) | stage 10 | faction “factionCountShadow” set to 0<br>faction “factionCountThieves” set to 0<br>faction “scoreShadow” set to 0<br>faction “scoreFeygard” set to 0<br>faction “scoreThieves” set to 0<br>faction “scoreShadow2” set to 0<br>faction “scoreFeygard2” set to 0<br>faction “scoreThieves2” set to 0<br>faction “scoreShadowFeygard” set to 0<br>clears stage 11 of [scores (hidden flag)](../quests/scores.md#stage-11)<br>clears stage 13 of [scores (hidden flag)](../quests/scores.md#stage-13)<br>clears stage 17 of [scores (hidden flag)](../quests/scores.md#stage-17)<br>clears stage 18 of [scores (hidden flag)](../quests/scores.md#stage-18)<br>clears stage 21 of [scores (hidden flag)](../quests/scores.md#stage-21)<br>clears stage 23 of [scores (hidden flag)](../quests/scores.md#stage-23)<br>clears stage 27 of [scores (hidden flag)](../quests/scores.md#stage-27)<br>clears stage 28 of [scores (hidden flag)](../quests/scores.md#stage-28)<br>clears stage 31 of [scores (hidden flag)](../quests/scores.md#stage-31)<br>clears stage 33 of [scores (hidden flag)](../quests/scores.md#stage-33)<br>clears stage 37 of [scores (hidden flag)](../quests/scores.md#stage-37)<br>clears stage 38 of [scores (hidden flag)](../quests/scores.md#stage-38)<br>clears stage 101 of [scores (hidden flag)](../quests/scores.md#stage-101)<br>clears stage 102 of [scores (hidden flag)](../quests/scores.md#stage-102)<br>clears stage 22 of [scores (hidden flag)](../quests/scores.md#stage-22) |
| <span id="stage-27"></span>27 | Feygard fan | stepping on a trigger on [debugmap](../maps/debugmap.md) | stage 10 | clears stage 22 of [scores (hidden flag)](../quests/scores.md#stage-22)<br>clears stage 23 of [scores (hidden flag)](../quests/scores.md#stage-23)<br>clears stage 25 of [scores (hidden flag)](../quests/scores.md#stage-25)<br>clears stage 28 of [scores (hidden flag)](../quests/scores.md#stage-28) |
| <span id="stage-28"></span>28 | Absolute Feygard fan | stepping on a trigger on [debugmap](../maps/debugmap.md) | stage 10 | clears stage 22 of [scores (hidden flag)](../quests/scores.md#stage-22)<br>clears stage 23 of [scores (hidden flag)](../quests/scores.md#stage-23)<br>clears stage 25 of [scores (hidden flag)](../quests/scores.md#stage-25)<br>clears stage 27 of [scores (hidden flag)](../quests/scores.md#stage-27) |
| <span id="stage-30"></span>30 | Thieves score fixed | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-31"></span>31 | Pro Thieves replies should be surpressed | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-32"></span>32 | Absolute Thieves guild hater<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Debugmap](../maps/debugmap.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fallhaven church](../maps/fallhaven_church.md).</span> | stepping on a trigger on [debugmap](../maps/debugmap.md) | stage 10, stage 20 | clears stage 33 of [scores (hidden flag)](../quests/scores.md#stage-33)<br>clears stage 35 of [scores (hidden flag)](../quests/scores.md#stage-35)<br>clears stage 37 of [scores (hidden flag)](../quests/scores.md#stage-37)<br>clears stage 38 of [scores (hidden flag)](../quests/scores.md#stage-38) |
| <span id="stage-33"></span>33 | Thieves guild hater | stepping on a trigger on [debugmap](../maps/debugmap.md) | stage 10, stage 20 | clears stage 32 of [scores (hidden flag)](../quests/scores.md#stage-32)<br>clears stage 35 of [scores (hidden flag)](../quests/scores.md#stage-35)<br>clears stage 37 of [scores (hidden flag)](../quests/scores.md#stage-37)<br>clears stage 38 of [scores (hidden flag)](../quests/scores.md#stage-38) |
| <span id="stage-35"></span>35 | Balanced Thieves guild feelings | stepping on a trigger on [debugmap](../maps/debugmap.md) | stage 10, stage 20 | faction “factionCountShadow” set to 0<br>faction “factionCountThieves” set to 0<br>faction “scoreShadow” set to 0<br>faction “scoreFeygard” set to 0<br>faction “scoreThieves” set to 0<br>faction “scoreShadow2” set to 0<br>faction “scoreFeygard2” set to 0<br>faction “scoreThieves2” set to 0<br>faction “scoreShadowFeygard” set to 0<br>clears stage 11 of [scores (hidden flag)](../quests/scores.md#stage-11)<br>clears stage 13 of [scores (hidden flag)](../quests/scores.md#stage-13)<br>clears stage 17 of [scores (hidden flag)](../quests/scores.md#stage-17)<br>clears stage 18 of [scores (hidden flag)](../quests/scores.md#stage-18)<br>clears stage 21 of [scores (hidden flag)](../quests/scores.md#stage-21)<br>clears stage 23 of [scores (hidden flag)](../quests/scores.md#stage-23)<br>clears stage 27 of [scores (hidden flag)](../quests/scores.md#stage-27)<br>clears stage 28 of [scores (hidden flag)](../quests/scores.md#stage-28)<br>clears stage 31 of [scores (hidden flag)](../quests/scores.md#stage-31)<br>clears stage 33 of [scores (hidden flag)](../quests/scores.md#stage-33)<br>clears stage 37 of [scores (hidden flag)](../quests/scores.md#stage-37)<br>clears stage 38 of [scores (hidden flag)](../quests/scores.md#stage-38)<br>clears stage 101 of [scores (hidden flag)](../quests/scores.md#stage-101)<br>clears stage 102 of [scores (hidden flag)](../quests/scores.md#stage-102)<br>clears stage 32 of [scores (hidden flag)](../quests/scores.md#stage-32) |
| <span id="stage-37"></span>37 | Thieves guild fan | stepping on a trigger on [debugmap](../maps/debugmap.md) | stage 10, stage 20 | clears stage 32 of [scores (hidden flag)](../quests/scores.md#stage-32)<br>clears stage 33 of [scores (hidden flag)](../quests/scores.md#stage-33)<br>clears stage 35 of [scores (hidden flag)](../quests/scores.md#stage-35)<br>clears stage 38 of [scores (hidden flag)](../quests/scores.md#stage-38) |
| <span id="stage-38"></span>38 | Absolute Thieves guild fan | stepping on a trigger on [debugmap](../maps/debugmap.md) | stage 10, stage 20 | clears stage 32 of [scores (hidden flag)](../quests/scores.md#stage-32)<br>clears stage 33 of [scores (hidden flag)](../quests/scores.md#stage-33)<br>clears stage 35 of [scores (hidden flag)](../quests/scores.md#stage-35)<br>clears stage 37 of [scores (hidden flag)](../quests/scores.md#stage-37) |
| <span id="stage-40"></span>40 | Kazaul score fixed | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-41"></span>41 | Pro Kazaul replies should be surpressed | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-42"></span>42 | Absolute Kazaul hater | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-43"></span>43 | Kazaul hater | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-45"></span>45 | Balanced Kazaul feelings | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-47"></span>47 | Kazaul fan | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-48"></span>48 | Absolute Kazaul fan | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-50"></span>50 | XX score fixed | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-51"></span>51 | Pro XX replies should be surpressed | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-52"></span>52 | Absolute XX hater | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-53"></span>53 | XX hater | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-55"></span>55 | Balanced XX feelings | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-57"></span>57 | XX fan | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-58"></span>58 | Absolute XX fan | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-101"></span>101 | Clear preference: Shadow over Feygard | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-102"></span>102 | Clear preference: Feygard over Shadow | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-112"></span>112 | Max Absolute Shadow hater<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Debugmap](../maps/debugmap.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fallhaven church](../maps/fallhaven_church.md).</span> | stepping on a trigger on [debugmap](../maps/debugmap.md) | stage 10, stage 20, stage 30 | clears stage 113 of [scores (hidden flag)](../quests/scores.md#stage-113)<br>clears stage 115 of [scores (hidden flag)](../quests/scores.md#stage-115)<br>clears stage 117 of [scores (hidden flag)](../quests/scores.md#stage-117)<br>clears stage 118 of [scores (hidden flag)](../quests/scores.md#stage-118) |
| <span id="stage-113"></span>113 | Max Shadow hater | stepping on a trigger on [debugmap](../maps/debugmap.md) | stage 10, stage 20, stage 30 | clears stage 112 of [scores (hidden flag)](../quests/scores.md#stage-112)<br>clears stage 115 of [scores (hidden flag)](../quests/scores.md#stage-115)<br>clears stage 117 of [scores (hidden flag)](../quests/scores.md#stage-117)<br>clears stage 118 of [scores (hidden flag)](../quests/scores.md#stage-118) |
| <span id="stage-115"></span>115 | Max Balanced Shadow feelings | stepping on a trigger on [debugmap](../maps/debugmap.md) | stage 10, stage 20, stage 30 | clears stage 112 of [scores (hidden flag)](../quests/scores.md#stage-112)<br>clears stage 113 of [scores (hidden flag)](../quests/scores.md#stage-113)<br>clears stage 117 of [scores (hidden flag)](../quests/scores.md#stage-117)<br>clears stage 118 of [scores (hidden flag)](../quests/scores.md#stage-118) |
| <span id="stage-117"></span>117 | Max Shadow fan | stepping on a trigger on [debugmap](../maps/debugmap.md) | stage 10, stage 20, stage 30 | clears stage 112 of [scores (hidden flag)](../quests/scores.md#stage-112)<br>clears stage 113 of [scores (hidden flag)](../quests/scores.md#stage-113)<br>clears stage 115 of [scores (hidden flag)](../quests/scores.md#stage-115)<br>clears stage 118 of [scores (hidden flag)](../quests/scores.md#stage-118) |
| <span id="stage-118"></span>118 | Max Absolute Shadow fan | stepping on a trigger on [debugmap](../maps/debugmap.md) | stage 10, stage 20, stage 30 | clears stage 112 of [scores (hidden flag)](../quests/scores.md#stage-112)<br>clears stage 113 of [scores (hidden flag)](../quests/scores.md#stage-113)<br>clears stage 115 of [scores (hidden flag)](../quests/scores.md#stage-115)<br>clears stage 117 of [scores (hidden flag)](../quests/scores.md#stage-117) |
| <span id="stage-122"></span>122 | Max Absolute Feygard hater<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Debugmap](../maps/debugmap.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fallhaven church](../maps/fallhaven_church.md).</span> | stepping on a trigger on [debugmap](../maps/debugmap.md) | stage 10, stage 20, stage 30 | clears stage 123 of [scores (hidden flag)](../quests/scores.md#stage-123)<br>clears stage 125 of [scores (hidden flag)](../quests/scores.md#stage-125)<br>clears stage 127 of [scores (hidden flag)](../quests/scores.md#stage-127)<br>clears stage 128 of [scores (hidden flag)](../quests/scores.md#stage-128) |
| <span id="stage-123"></span>123 | Max Feygard hater | stepping on a trigger on [debugmap](../maps/debugmap.md) | stage 10, stage 20, stage 30 | clears stage 122 of [scores (hidden flag)](../quests/scores.md#stage-122)<br>clears stage 125 of [scores (hidden flag)](../quests/scores.md#stage-125)<br>clears stage 127 of [scores (hidden flag)](../quests/scores.md#stage-127)<br>clears stage 128 of [scores (hidden flag)](../quests/scores.md#stage-128) |
| <span id="stage-125"></span>125 | Max Balanced Feygard feelings | stepping on a trigger on [debugmap](../maps/debugmap.md) | stage 10, stage 20, stage 30 | clears stage 122 of [scores (hidden flag)](../quests/scores.md#stage-122)<br>clears stage 123 of [scores (hidden flag)](../quests/scores.md#stage-123)<br>clears stage 127 of [scores (hidden flag)](../quests/scores.md#stage-127)<br>clears stage 128 of [scores (hidden flag)](../quests/scores.md#stage-128) |
| <span id="stage-127"></span>127 | Max Feygard fan | stepping on a trigger on [debugmap](../maps/debugmap.md) | stage 10, stage 20, stage 30 | clears stage 122 of [scores (hidden flag)](../quests/scores.md#stage-122)<br>clears stage 123 of [scores (hidden flag)](../quests/scores.md#stage-123)<br>clears stage 125 of [scores (hidden flag)](../quests/scores.md#stage-125)<br>clears stage 128 of [scores (hidden flag)](../quests/scores.md#stage-128) |
| <span id="stage-128"></span>128 | Max Absolute Feygard fan | stepping on a trigger on [debugmap](../maps/debugmap.md) | stage 10, stage 20, stage 30 | clears stage 122 of [scores (hidden flag)](../quests/scores.md#stage-122)<br>clears stage 123 of [scores (hidden flag)](../quests/scores.md#stage-123)<br>clears stage 125 of [scores (hidden flag)](../quests/scores.md#stage-125)<br>clears stage 127 of [scores (hidden flag)](../quests/scores.md#stage-127) |
| <span id="stage-132"></span>132 | Max Absolute Thieves guild hater | stepping on a trigger on [debugmap](../maps/debugmap.md) | stage 10, stage 20, stage 30 | clears stage 133 of [scores (hidden flag)](../quests/scores.md#stage-133)<br>clears stage 135 of [scores (hidden flag)](../quests/scores.md#stage-135)<br>clears stage 137 of [scores (hidden flag)](../quests/scores.md#stage-137)<br>clears stage 138 of [scores (hidden flag)](../quests/scores.md#stage-138) |
| <span id="stage-133"></span>133 | Max Thieves guild hater | stepping on a trigger on [debugmap](../maps/debugmap.md) | stage 10, stage 20, stage 30 | clears stage 132 of [scores (hidden flag)](../quests/scores.md#stage-132)<br>clears stage 135 of [scores (hidden flag)](../quests/scores.md#stage-135)<br>clears stage 137 of [scores (hidden flag)](../quests/scores.md#stage-137)<br>clears stage 138 of [scores (hidden flag)](../quests/scores.md#stage-138) |
| <span id="stage-135"></span>135 | Max Balanced Thieves guild feelings | stepping on a trigger on [debugmap](../maps/debugmap.md) | stage 10, stage 20, stage 30 | clears stage 132 of [scores (hidden flag)](../quests/scores.md#stage-132)<br>clears stage 133 of [scores (hidden flag)](../quests/scores.md#stage-133)<br>clears stage 137 of [scores (hidden flag)](../quests/scores.md#stage-137)<br>clears stage 138 of [scores (hidden flag)](../quests/scores.md#stage-138) |
| <span id="stage-137"></span>137 | Max Thieves guild fan | stepping on a trigger on [debugmap](../maps/debugmap.md) | stage 10, stage 20, stage 30 | clears stage 132 of [scores (hidden flag)](../quests/scores.md#stage-132)<br>clears stage 133 of [scores (hidden flag)](../quests/scores.md#stage-133)<br>clears stage 135 of [scores (hidden flag)](../quests/scores.md#stage-135)<br>clears stage 138 of [scores (hidden flag)](../quests/scores.md#stage-138) |
| <span id="stage-138"></span>138 | Max Absolute Thieves guild fan | stepping on a trigger on [debugmap](../maps/debugmap.md) | stage 10, stage 20, stage 30 | clears stage 132 of [scores (hidden flag)](../quests/scores.md#stage-132)<br>clears stage 133 of [scores (hidden flag)](../quests/scores.md#stage-133)<br>clears stage 135 of [scores (hidden flag)](../quests/scores.md#stage-135)<br>clears stage 137 of [scores (hidden flag)](../quests/scores.md#stage-137) |
| <span id="stage-999"></span>999 | - | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 12: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals → **stage 12**; also clears stage 13 of [scores (hidden flag)](../quests/scores.md#stage-13), clears stage 15 of [scores (hidden flag)](../quests/scores.md#stage-15), clears stage 17 of [scores (hidden flag)](../quests/scores.md#stage-17), clears stage 18 of [scores (hidden flag)](../quests/scores.md#stage-18)

???+ note "Stage 13: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; faction “fsc_shd2” ≥ 10 → **stage 13**; also clears stage 12 of [scores (hidden flag)](../quests/scores.md#stage-12), clears stage 15 of [scores (hidden flag)](../quests/scores.md#stage-15), clears stage 17 of [scores (hidden flag)](../quests/scores.md#stage-17), clears stage 18 of [scores (hidden flag)](../quests/scores.md#stage-18)

???+ note "Stage 15: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; NOT faction “fsc_shd9” ≥ 11 → **stage 15**; also clears stage 12 of [scores (hidden flag)](../quests/scores.md#stage-12), clears stage 13 of [scores (hidden flag)](../quests/scores.md#stage-13), clears stage 17 of [scores (hidden flag)](../quests/scores.md#stage-17), clears stage 18 of [scores (hidden flag)](../quests/scores.md#stage-18)

???+ note "Stage 17: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; faction “fsc_shd2” ≥ 60 → **stage 17**; also clears stage 12 of [scores (hidden flag)](../quests/scores.md#stage-12), clears stage 13 of [scores (hidden flag)](../quests/scores.md#stage-13), clears stage 15 of [scores (hidden flag)](../quests/scores.md#stage-15), clears stage 18 of [scores (hidden flag)](../quests/scores.md#stage-18)

???+ note "Stage 18: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; faction “fsc_shd2” ≥ 90 → **stage 18**; also clears stage 12 of [scores (hidden flag)](../quests/scores.md#stage-12), clears stage 13 of [scores (hidden flag)](../quests/scores.md#stage-13), clears stage 15 of [scores (hidden flag)](../quests/scores.md#stage-15), clears stage 17 of [scores (hidden flag)](../quests/scores.md#stage-17)

???+ note "Stage 22: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; reached stage 10 of [scores (hidden flag)](../quests/scores.md#stage-10) → **stage 22**; also clears stage 23 of [scores (hidden flag)](../quests/scores.md#stage-23), clears stage 25 of [scores (hidden flag)](../quests/scores.md#stage-25), clears stage 27 of [scores (hidden flag)](../quests/scores.md#stage-27), clears stage 28 of [scores (hidden flag)](../quests/scores.md#stage-28)

???+ note "Stage 23: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; reached stage 10 of [scores (hidden flag)](../quests/scores.md#stage-10); faction “fsc_fey2” ≥ 10 → **stage 23**; also clears stage 22 of [scores (hidden flag)](../quests/scores.md#stage-22), clears stage 25 of [scores (hidden flag)](../quests/scores.md#stage-25), clears stage 27 of [scores (hidden flag)](../quests/scores.md#stage-27), clears stage 28 of [scores (hidden flag)](../quests/scores.md#stage-28)

???+ note "Stage 25: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; reached stage 10 of [scores (hidden flag)](../quests/scores.md#stage-10); NOT faction “fsc_fey9” ≥ 11 → **stage 25**; also clears stage 22 of [scores (hidden flag)](../quests/scores.md#stage-22), clears stage 23 of [scores (hidden flag)](../quests/scores.md#stage-23), clears stage 27 of [scores (hidden flag)](../quests/scores.md#stage-27), clears stage 28 of [scores (hidden flag)](../quests/scores.md#stage-28)

???+ note "Stage 27: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; reached stage 10 of [scores (hidden flag)](../quests/scores.md#stage-10); faction “fsc_fey2” ≥ 60 → **stage 27**; also clears stage 22 of [scores (hidden flag)](../quests/scores.md#stage-22), clears stage 23 of [scores (hidden flag)](../quests/scores.md#stage-23), clears stage 25 of [scores (hidden flag)](../quests/scores.md#stage-25), clears stage 28 of [scores (hidden flag)](../quests/scores.md#stage-28)

???+ note "Stage 28: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; reached stage 10 of [scores (hidden flag)](../quests/scores.md#stage-10); faction “fsc_fey2” ≥ 90 → **stage 28**; also clears stage 22 of [scores (hidden flag)](../quests/scores.md#stage-22), clears stage 23 of [scores (hidden flag)](../quests/scores.md#stage-23), clears stage 25 of [scores (hidden flag)](../quests/scores.md#stage-25), clears stage 27 of [scores (hidden flag)](../quests/scores.md#stage-27)

???+ note "Stage 32: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; reached stage 10 of [scores (hidden flag)](../quests/scores.md#stage-10); reached stage 20 of [scores (hidden flag)](../quests/scores.md#stage-20) → **stage 32**; also clears stage 33 of [scores (hidden flag)](../quests/scores.md#stage-33), clears stage 35 of [scores (hidden flag)](../quests/scores.md#stage-35), clears stage 37 of [scores (hidden flag)](../quests/scores.md#stage-37), clears stage 38 of [scores (hidden flag)](../quests/scores.md#stage-38)

???+ note "Stage 33: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; reached stage 10 of [scores (hidden flag)](../quests/scores.md#stage-10); reached stage 20 of [scores (hidden flag)](../quests/scores.md#stage-20); faction “fsc_thv2” ≥ 10 → **stage 33**; also clears stage 32 of [scores (hidden flag)](../quests/scores.md#stage-32), clears stage 35 of [scores (hidden flag)](../quests/scores.md#stage-35), clears stage 37 of [scores (hidden flag)](../quests/scores.md#stage-37), clears stage 38 of [scores (hidden flag)](../quests/scores.md#stage-38)

???+ note "Stage 35: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; reached stage 10 of [scores (hidden flag)](../quests/scores.md#stage-10); reached stage 20 of [scores (hidden flag)](../quests/scores.md#stage-20); NOT faction “fsc_thv9” ≥ 11 → **stage 35**; also clears stage 32 of [scores (hidden flag)](../quests/scores.md#stage-32), clears stage 33 of [scores (hidden flag)](../quests/scores.md#stage-33), clears stage 37 of [scores (hidden flag)](../quests/scores.md#stage-37), clears stage 38 of [scores (hidden flag)](../quests/scores.md#stage-38)

???+ note "Stage 37: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; reached stage 10 of [scores (hidden flag)](../quests/scores.md#stage-10); reached stage 20 of [scores (hidden flag)](../quests/scores.md#stage-20); faction “fsc_thv2” ≥ 60 → **stage 37**; also clears stage 32 of [scores (hidden flag)](../quests/scores.md#stage-32), clears stage 33 of [scores (hidden flag)](../quests/scores.md#stage-33), clears stage 35 of [scores (hidden flag)](../quests/scores.md#stage-35), clears stage 38 of [scores (hidden flag)](../quests/scores.md#stage-38)

???+ note "Stage 38: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; reached stage 10 of [scores (hidden flag)](../quests/scores.md#stage-10); reached stage 20 of [scores (hidden flag)](../quests/scores.md#stage-20); faction “fsc_thv2” ≥ 90 → **stage 38**; also clears stage 32 of [scores (hidden flag)](../quests/scores.md#stage-32), clears stage 33 of [scores (hidden flag)](../quests/scores.md#stage-33), clears stage 35 of [scores (hidden flag)](../quests/scores.md#stage-35), clears stage 37 of [scores (hidden flag)](../quests/scores.md#stage-37)

???+ note "Stage 112: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; reached stage 10 of [scores (hidden flag)](../quests/scores.md#stage-10); reached stage 20 of [scores (hidden flag)](../quests/scores.md#stage-20); reached stage 30 of [scores (hidden flag)](../quests/scores.md#stage-30) → **stage 112**; also clears stage 113 of [scores (hidden flag)](../quests/scores.md#stage-113), clears stage 115 of [scores (hidden flag)](../quests/scores.md#stage-115), clears stage 117 of [scores (hidden flag)](../quests/scores.md#stage-117), clears stage 118 of [scores (hidden flag)](../quests/scores.md#stage-118)

???+ note "Stage 113: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; reached stage 10 of [scores (hidden flag)](../quests/scores.md#stage-10); reached stage 20 of [scores (hidden flag)](../quests/scores.md#stage-20); reached stage 30 of [scores (hidden flag)](../quests/scores.md#stage-30); faction “fsc_shd2” ≥ 10 → **stage 113**; also clears stage 112 of [scores (hidden flag)](../quests/scores.md#stage-112), clears stage 115 of [scores (hidden flag)](../quests/scores.md#stage-115), clears stage 117 of [scores (hidden flag)](../quests/scores.md#stage-117), clears stage 118 of [scores (hidden flag)](../quests/scores.md#stage-118)

???+ note "Stage 115: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; reached stage 10 of [scores (hidden flag)](../quests/scores.md#stage-10); reached stage 20 of [scores (hidden flag)](../quests/scores.md#stage-20); reached stage 30 of [scores (hidden flag)](../quests/scores.md#stage-30); NOT faction “fsc_shd9” ≥ 11 → **stage 115**; also clears stage 112 of [scores (hidden flag)](../quests/scores.md#stage-112), clears stage 113 of [scores (hidden flag)](../quests/scores.md#stage-113), clears stage 117 of [scores (hidden flag)](../quests/scores.md#stage-117), clears stage 118 of [scores (hidden flag)](../quests/scores.md#stage-118)

???+ note "Stage 117: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; reached stage 10 of [scores (hidden flag)](../quests/scores.md#stage-10); reached stage 20 of [scores (hidden flag)](../quests/scores.md#stage-20); reached stage 30 of [scores (hidden flag)](../quests/scores.md#stage-30); faction “fsc_shd2” ≥ 60 → **stage 117**; also clears stage 112 of [scores (hidden flag)](../quests/scores.md#stage-112), clears stage 113 of [scores (hidden flag)](../quests/scores.md#stage-113), clears stage 115 of [scores (hidden flag)](../quests/scores.md#stage-115), clears stage 118 of [scores (hidden flag)](../quests/scores.md#stage-118)

???+ note "Stage 118: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; reached stage 10 of [scores (hidden flag)](../quests/scores.md#stage-10); reached stage 20 of [scores (hidden flag)](../quests/scores.md#stage-20); reached stage 30 of [scores (hidden flag)](../quests/scores.md#stage-30); faction “fsc_shd2” ≥ 90 → **stage 118**; also clears stage 112 of [scores (hidden flag)](../quests/scores.md#stage-112), clears stage 113 of [scores (hidden flag)](../quests/scores.md#stage-113), clears stage 115 of [scores (hidden flag)](../quests/scores.md#stage-115), clears stage 117 of [scores (hidden flag)](../quests/scores.md#stage-117)

???+ note "Stage 122: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; reached stage 10 of [scores (hidden flag)](../quests/scores.md#stage-10); reached stage 20 of [scores (hidden flag)](../quests/scores.md#stage-20); reached stage 30 of [scores (hidden flag)](../quests/scores.md#stage-30) → **stage 122**; also clears stage 123 of [scores (hidden flag)](../quests/scores.md#stage-123), clears stage 125 of [scores (hidden flag)](../quests/scores.md#stage-125), clears stage 127 of [scores (hidden flag)](../quests/scores.md#stage-127), clears stage 128 of [scores (hidden flag)](../quests/scores.md#stage-128)

???+ note "Stage 123: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; reached stage 10 of [scores (hidden flag)](../quests/scores.md#stage-10); reached stage 20 of [scores (hidden flag)](../quests/scores.md#stage-20); reached stage 30 of [scores (hidden flag)](../quests/scores.md#stage-30); faction “fsc_fey2” ≥ 10 → **stage 123**; also clears stage 122 of [scores (hidden flag)](../quests/scores.md#stage-122), clears stage 125 of [scores (hidden flag)](../quests/scores.md#stage-125), clears stage 127 of [scores (hidden flag)](../quests/scores.md#stage-127), clears stage 128 of [scores (hidden flag)](../quests/scores.md#stage-128)

???+ note "Stage 125: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; reached stage 10 of [scores (hidden flag)](../quests/scores.md#stage-10); reached stage 20 of [scores (hidden flag)](../quests/scores.md#stage-20); reached stage 30 of [scores (hidden flag)](../quests/scores.md#stage-30); NOT faction “fsc_fey9” ≥ 11 → **stage 125**; also clears stage 122 of [scores (hidden flag)](../quests/scores.md#stage-122), clears stage 123 of [scores (hidden flag)](../quests/scores.md#stage-123), clears stage 127 of [scores (hidden flag)](../quests/scores.md#stage-127), clears stage 128 of [scores (hidden flag)](../quests/scores.md#stage-128)

???+ note "Stage 127: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; reached stage 10 of [scores (hidden flag)](../quests/scores.md#stage-10); reached stage 20 of [scores (hidden flag)](../quests/scores.md#stage-20); reached stage 30 of [scores (hidden flag)](../quests/scores.md#stage-30); faction “fsc_fey2” ≥ 60 → **stage 127**; also clears stage 122 of [scores (hidden flag)](../quests/scores.md#stage-122), clears stage 123 of [scores (hidden flag)](../quests/scores.md#stage-123), clears stage 125 of [scores (hidden flag)](../quests/scores.md#stage-125), clears stage 128 of [scores (hidden flag)](../quests/scores.md#stage-128)

???+ note "Stage 128: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; reached stage 10 of [scores (hidden flag)](../quests/scores.md#stage-10); reached stage 20 of [scores (hidden flag)](../quests/scores.md#stage-20); reached stage 30 of [scores (hidden flag)](../quests/scores.md#stage-30); faction “fsc_fey2” ≥ 90 → **stage 128**; also clears stage 122 of [scores (hidden flag)](../quests/scores.md#stage-122), clears stage 123 of [scores (hidden flag)](../quests/scores.md#stage-123), clears stage 125 of [scores (hidden flag)](../quests/scores.md#stage-125), clears stage 127 of [scores (hidden flag)](../quests/scores.md#stage-127)

???+ note "Stage 132: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; reached stage 10 of [scores (hidden flag)](../quests/scores.md#stage-10); reached stage 20 of [scores (hidden flag)](../quests/scores.md#stage-20); reached stage 30 of [scores (hidden flag)](../quests/scores.md#stage-30) → **stage 132**; also clears stage 133 of [scores (hidden flag)](../quests/scores.md#stage-133), clears stage 135 of [scores (hidden flag)](../quests/scores.md#stage-135), clears stage 137 of [scores (hidden flag)](../quests/scores.md#stage-137), clears stage 138 of [scores (hidden flag)](../quests/scores.md#stage-138)

???+ note "Stage 133: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; reached stage 10 of [scores (hidden flag)](../quests/scores.md#stage-10); reached stage 20 of [scores (hidden flag)](../quests/scores.md#stage-20); reached stage 30 of [scores (hidden flag)](../quests/scores.md#stage-30); faction “fsc_thv2” ≥ 10 → **stage 133**; also clears stage 132 of [scores (hidden flag)](../quests/scores.md#stage-132), clears stage 135 of [scores (hidden flag)](../quests/scores.md#stage-135), clears stage 137 of [scores (hidden flag)](../quests/scores.md#stage-137), clears stage 138 of [scores (hidden flag)](../quests/scores.md#stage-138)

???+ note "Stage 135: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; reached stage 10 of [scores (hidden flag)](../quests/scores.md#stage-10); reached stage 20 of [scores (hidden flag)](../quests/scores.md#stage-20); reached stage 30 of [scores (hidden flag)](../quests/scores.md#stage-30); NOT faction “fsc_thv9” ≥ 11 → **stage 135**; also clears stage 132 of [scores (hidden flag)](../quests/scores.md#stage-132), clears stage 133 of [scores (hidden flag)](../quests/scores.md#stage-133), clears stage 137 of [scores (hidden flag)](../quests/scores.md#stage-137), clears stage 138 of [scores (hidden flag)](../quests/scores.md#stage-138)

???+ note "Stage 137: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; reached stage 10 of [scores (hidden flag)](../quests/scores.md#stage-10); reached stage 20 of [scores (hidden flag)](../quests/scores.md#stage-20); reached stage 30 of [scores (hidden flag)](../quests/scores.md#stage-30); faction “fsc_shd2” ≥ 60 → **stage 137**; also clears stage 132 of [scores (hidden flag)](../quests/scores.md#stage-132), clears stage 133 of [scores (hidden flag)](../quests/scores.md#stage-133), clears stage 135 of [scores (hidden flag)](../quests/scores.md#stage-135), clears stage 138 of [scores (hidden flag)](../quests/scores.md#stage-138)

???+ note "Stage 138: 1 route"

    1. stepping on a trigger on [debugmap](../maps/debugmap.md) → the conversation leads here automatically — **conditions:** eaten 1000+ bonemeals; reached stage 10 of [scores (hidden flag)](../quests/scores.md#stage-10); reached stage 20 of [scores (hidden flag)](../quests/scores.md#stage-20); reached stage 30 of [scores (hidden flag)](../quests/scores.md#stage-30); faction “fsc_shd2” ≥ 90 → **stage 138**; also clears stage 132 of [scores (hidden flag)](../quests/scores.md#stage-132), clears stage 133 of [scores (hidden flag)](../quests/scores.md#stage-133), clears stage 135 of [scores (hidden flag)](../quests/scores.md#stage-135), clears stage 137 of [scores (hidden flag)](../quests/scores.md#stage-137)


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

**Completability:** From v0.8.16.1, this quest could not be completed: it had no ending yet. It became completable in [v0.8.17](../versions/0.8.17.md).

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Dialogue: 1 line added |
| [v0.8.15](../versions/0.8.15.md) | Added<br>Dialogue: 1 line changed |
| [v0.8.16.1](../versions/0.8.16.1.md) | journal visibility changed; stages added: 10, 20, 30, 40, 42, 43, 45, 47, 48, 50, 52, 53, 55, 57, 58, 112, 113, 115, 117, 118, 122, 123, 125, 127, 128, 132, 133, 135, 137, 138<br>Dialogue: 30 lines added |
| [v0.8.17](../versions/0.8.17.md) | journal visibility changed; stages added: 11, 21, 31, 41, 51 |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=scores.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=scores.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=scores.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=scores.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=scores.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `scores` |
    | showInLog | 0 |
    | Stage IDs | 10, 11, 12, 13, 15, 17, 18, 20, 21, 22, 23, 25, 27, 28, 30, 31, 32, 33, 35, 37, 38, 40, 41, 42, 43, 45, 47, 48, 50, 51, 52, 53, 55, 57, 58, 101, 102, 112, 113, 115, 117, 118, 122, 123, 125, 127, 128, 132, 133, 135, 137, 138, 999 |
    | Dialogue nodes setting stages | 12: `fsc_calc_shd_2`, 13: `fsc_calc_shd_3`, 15: `faction_count_shadow`, 15: `fsc_calc_shd_5`, 17: `fsc_calc_shd_7`, 18: `fsc_calc_shd_8`, 22: `fsc_calc_fey_2`, 23: `fsc_calc_fey_3`, 25: `faction_count_shadow`, 25: `fsc_calc_fey_5`, 27: `fsc_calc_fey_7`, 28: `fsc_calc_fey_8`, 32: `fsc_calc_thv_2`, 33: `fsc_calc_thv_3`, 35: `faction_count_shadow`, 35: `fsc_calc_thv_5`, 37: `fsc_calc_thv_7`, 38: `fsc_calc_thv_8`, 112: `fsc_calc_shd1_2`, 113: `fsc_calc_shd1_3`, 115: `fsc_calc_shd1_5`, 117: `fsc_calc_shd1_7`, 118: `fsc_calc_shd1_8`, 122: `fsc_calc_fey1_2`, 123: `fsc_calc_fey1_3`, 125: `fsc_calc_fey1_5`, 127: `fsc_calc_fey1_7`, 128: `fsc_calc_fey1_8`, 132: `fsc_calc_thv1_2`, 133: `fsc_calc_thv1_3`, 135: `fsc_calc_thv1_5`, 137: `fsc_calc_thv1_7`, 138: `fsc_calc_thv1_8` |
    | Dialogue nodes clearing stages | 11: `faction_count_shadow`, 13: `faction_count_shadow`, 13: `fsc_calc_shd_2`, 13: `fsc_calc_shd_5`, 13: `fsc_calc_shd_7`, 13: `fsc_calc_shd_8`, 17: `faction_count_shadow`, 17: `fsc_calc_shd_2`, 17: `fsc_calc_shd_3`, 17: `fsc_calc_shd_5` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
