---
description: "Agent is a non-player character (NPC) in Andor's Trail, found in Blackwater mountain 5, Prim, Blackwater Mountain. Starts The agent and the beast."
---

# ![](../assets/icons/monsters/monsters_men_4.png){ .sprite } Agent

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_4.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Starts [The agent and the beast](../quests/bwm_agent.md) |
| **Found in** | Blackwater mountain 5, Prim, Blackwater Mountain |
| **Entries in game data** | 6 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "6 entries in the game data"
    The game data defines 6 separate characters named Agent. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation, location. Each entry has its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`agent1`](#v-agent1) | NPC | [Blackwater mountain 5](../maps/blackwater_mountain5.md#pin-npc-agent1) | starts [The agent and the beast](../quests/bwm_agent.md) |
| [`agent2`](#v-agent2) | NPC | Prim: [Blackwater mountain 9](../maps/blackwater_mountain9.md#pin-npc-agent2) | – |
| [`agent3`](#v-agent3) | NPC | Blackwater Mountain: [Blackwater mountain 14](../maps/blackwater_mountain14.md#pin-npc-agent3) | – |
| [`agent4`](#v-agent4) | NPC | Blackwater Mountain: [Blackwater mountain 17](../maps/blackwater_mountain17.md#pin-npc-agent4) | – |
| [`agent5`](#v-agent5) | NPC | Blackwater Mountain: [Blackwater mountain 30](../maps/blackwater_mountain30.md#pin-npc-agent5) | – |
| [`agent6`](#v-agent6) | NPC | Blackwater Mountain: [Blackwater mountain 38](../maps/blackwater_mountain38.md#pin-npc-agent6) | – |

## Blackwater mountain 5 (agent1) { #v-agent1 }

**Entry ID:** `agent1` · **Type:** NPC · **Role:** Starts [The agent and the beast](../quests/bwm_agent.md)

**Location:** [Blackwater mountain 5](../maps/blackwater_mountain5.md#pin-npc-agent1)

### Quests

- [The agent and the beast](../quests/bwm_agent.md): stages 1, 5, 10

### Dialogue simulator

Set your quest stages and items, then talk to Agent. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/bwm_agent_1_start.json" data-npc="Agent" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (14 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-agent1-bwm_agent_1_start"></span>**`bwm_agent_1_start`** Agent: “Oh, someone from the outside! Please, adventurer, you have to help us!”

    - “What is the matter?” → [bwm_agent_1_2](#d-agent1-bwm_agent_1_2)
    - “'Us'? I only see you here.” → [bwm_agent_1_3](#d-agent1-bwm_agent_1_3)

    <span id="d-agent1-bwm_agent_1_2"></span>**`bwm_agent_1_2`** Agent: “We urgently need help from someone outside!”

    - Next → [bwm_agent_1_4](#d-agent1-bwm_agent_1_4)

    <span id="d-agent1-bwm_agent_1_3"></span>**`bwm_agent_1_3`** Agent: “Very funny. I was sent by my settlement to get help from the outside.”

    - Next → [bwm_agent_1_4](#d-agent1-bwm_agent_1_4)

    <span id="d-agent1-bwm_agent_1_4"></span>**`bwm_agent_1_4`** Agent: “The people of my settlement, the Blackwater mountain, are slowly being reduced in numbers by the monsters and the savage bandits.” — **effects:** sets stage 1 of [The agent and the beast](../quests/bwm_agent.md#stage-1)

    - Next → [bwm_agent_1_5](#d-agent1-bwm_agent_1_5)

    <span id="d-agent1-bwm_agent_1_5"></span>**`bwm_agent_1_5`** Agent: “The monsters are closing in on us, and we desperately need help by some able fighter.”

    - “I guess I could help, I have killed a few monsters here and there.” → [bwm_agent_1_7](#d-agent1-bwm_agent_1_7)
    - “A fight, great. I'm in!” → [bwm_agent_1_7](#d-agent1-bwm_agent_1_7)
    - “Will there be a reward for this?” → [bwm_agent_1_6](#d-agent1-bwm_agent_1_6)
    - “Hmm, no. I had better not get involved in this.” → *conversation ends*

    <span id="d-agent1-bwm_agent_1_7"></span>**`bwm_agent_1_7`** Agent: “Excellent. The Blackwater mountain settlement is some distance away. Frankly, I am amazed that I made it this far alive.” — **effects:** sets stage 5 of [The agent and the beast](../quests/bwm_agent.md#stage-5)

    - Next → [bwm_agent_1_8](#d-agent1-bwm_agent_1_8)

    <span id="d-agent1-bwm_agent_1_6"></span>**`bwm_agent_1_6`** Agent: “Reward? Hmm, I was hoping you would help us for other reasons than a reward. But I guess my master will reward you sufficiently if you survive.”

    - “Alright, I'll do it.” → [bwm_agent_1_7](#d-agent1-bwm_agent_1_7)

    <span id="d-agent1-bwm_agent_1_8"></span>**`bwm_agent_1_8`** Agent: “I must warn you though, that there are some nasty monsters on the way.”

    - Next → [bwm_agent_1_9](#d-agent1-bwm_agent_1_9)

    <span id="d-agent1-bwm_agent_1_9"></span>**`bwm_agent_1_9`** Agent: “But I guess you seem strong enough.”

    - “Yeah, I can handle myself.” → [bwm_agent_1_10](#d-agent1-bwm_agent_1_10)
    - “No problem.” → [bwm_agent_1_10](#d-agent1-bwm_agent_1_10)

    <span id="d-agent1-bwm_agent_1_10"></span>**`bwm_agent_1_10`** Agent: “Good. First though, we must cross this mine to the other side.”

    - Next → [bwm_agent_1_11](#d-agent1-bwm_agent_1_11)

    <span id="d-agent1-bwm_agent_1_11"></span>**`bwm_agent_1_11`** Agent: “The mine shaft over there [points] has collapsed, so I guess you won't make it through there.”

    - Next → [bwm_agent_1_12](#d-agent1-bwm_agent_1_12)

    <span id="d-agent1-bwm_agent_1_12"></span>**`bwm_agent_1_12`** Agent: “You will have to go through the abandoned mine below. Beware that the mine is pitch-black, so you will have to navigate in there without any light.”

    - “What about you?” → [bwm_agent_1_13](#d-agent1-bwm_agent_1_13)
    - “OK, I'll go through the pitch-black mine.” → [bwm_agent_1_14](#d-agent1-bwm_agent_1_14)

    <span id="d-agent1-bwm_agent_1_13"></span>**`bwm_agent_1_13`** Agent: “I'll try to crawl back through the mine shaft here. That's how I got here in the first place.”

    - Next → [bwm_agent_1_14](#d-agent1-bwm_agent_1_14)

    <span id="d-agent1-bwm_agent_1_14"></span>**`bwm_agent_1_14`** Agent: “Let's meet at the other side of this mine shaft.” — **effects:** sets stage 10 of [The agent and the beast](../quests/bwm_agent.md#stage-10), removes monsters from blackwater_mountain5

    - “OK. You crawl through the shaft, and I'll go below. See you on the other side!” → *NPC leaves*



### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 6 lines changed<br>· text: “Excellent. The Blackwater settlement is some distance away. Frankly, …” → “Excellent. The Blackwater mountain settlement is some distance away. …”<br>· text: “Reward? Hm, I was hoping you would help us for other reasons than a r…” → “Reward? Hmm, I was hoping you would help us for other reasons than a …” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed<br>· text: “Oh, someone from the outside! Please, sir! You have to help us!” → “Oh, someone from the outside! Please, adventurer, you have to help us!” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (agent1)"

    | | |
    |---|---|
    | Entry ID | `agent1` |
    | Spawn group | `bwm_agent_1` |
    | Loot table | – |
    | Conversation | `bwm_agent_1_start` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:4` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "agent1",
     "name": "Agent",
     "iconID": "monsters_men:4",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "bwm_agent_1",
     "phraseID": "bwm_agent_1_start"
    }
    ```


## Prim, Blackwater mountain 9 (agent2) { #v-agent2 }

**Entry ID:** `agent2` · **Type:** NPC

**Location:** Prim: [Blackwater mountain 9](../maps/blackwater_mountain9.md#pin-npc-agent2)

### Quests

- [The agent and the beast](../quests/bwm_agent.md): stage 20

### Dialogue simulator

Set your quest stages and items, then talk to Agent. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/bwm_agent_2_start.json" data-npc="Agent" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (12 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-agent2-bwm_agent_2_start"></span>**`bwm_agent_2_start`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 20 of [The agent and the beast](../quests/bwm_agent.md#stage-20))* → [bwm_agent_2_7](#d-agent2-bwm_agent_2_7)
    - branch 2 → [bwm_agent_2_1](#d-agent2-bwm_agent_2_1)

    <span id="d-agent2-bwm_agent_2_7"></span>**`bwm_agent_2_7`** Agent: “I'll wait for you by the steps up to the mountain pass. See you there! Remember, go east once you exit the mine.” — **effects:** sets stage 20 of [The agent and the beast](../quests/bwm_agent.md#stage-20)

    - “OK, see you there!” → *NPC leaves*

    <span id="d-agent2-bwm_agent_2_1"></span>**`bwm_agent_2_1`** Agent: “Hello again. You made it through alive, well done!”

    - “These monsters, what are they?” → [bwm_agent_2_2](#d-agent2-bwm_agent_2_2)
    - “You never told me it would be pitch-black down there. I almost got killed!” → [bwm_agent_2_12](#d-agent2-bwm_agent_2_12)
    - “Yeah, piece of cake.” → [bwm_agent_2_5](#d-agent2-bwm_agent_2_5)

    <span id="d-agent2-bwm_agent_2_2"></span>**`bwm_agent_2_2`** Agent: “The gornauds? I have no idea where they come from, one day they just showed up here around the mountain.”

    - Next → [bwm_agent_2_3](#d-agent2-bwm_agent_2_3)

    <span id="d-agent2-bwm_agent_2_12"></span>**`bwm_agent_2_12`** Agent: “Actually, I did tell you that it would be pitch-black down there. Good work navigating through there!”

    - Next → [bwm_agent_2_4](#d-agent2-bwm_agent_2_4)

    <span id="d-agent2-bwm_agent_2_5"></span>**`bwm_agent_2_5`** Agent: “We should hurry now.”

    - Next → [bwm_agent_2_6](#d-agent2-bwm_agent_2_6)

    <span id="d-agent2-bwm_agent_2_3"></span>**`bwm_agent_2_3`** Agent: “Nasty beasts, they are.”

    - Next → [bwm_agent_2_4](#d-agent2-bwm_agent_2_4)

    <span id="d-agent2-bwm_agent_2_4"></span>**`bwm_agent_2_4`** Agent: “Anyway, let's get going now. We are now one step closer to the Blackwater mountain settlement.”

    - Next → [bwm_agent_2_5](#d-agent2-bwm_agent_2_5)

    <span id="d-agent2-bwm_agent_2_6"></span>**`bwm_agent_2_6`** Agent: “Once we exit this mine, it is very important that you go directly east from there. Do not travel to other places other than going east now!”

    - “OK, I'll go east once I have exited the mine. Got it.” → [bwm_agent_2_7](#d-agent2-bwm_agent_2_7)
    - “Why east? What else is there here?” → [bwm_agent_2_8](#d-agent2-bwm_agent_2_8)

    <span id="d-agent2-bwm_agent_2_8"></span>**`bwm_agent_2_8`** Agent: “Oh, nothing. There are dangerous places here. You should definitely not head any other direction than east.”

    - “Sure, I'll head east.” → [bwm_agent_2_7](#d-agent2-bwm_agent_2_7)
    - “Dangerous? Sounds like my kind of place!” → [bwm_agent_2_10](#d-agent2-bwm_agent_2_10)
    - “Is there something you are not telling me?” → [bwm_agent_2_11](#d-agent2-bwm_agent_2_11)

    <span id="d-agent2-bwm_agent_2_10"></span>**`bwm_agent_2_10`** Agent: “It would be your loss. Don't say I didn't warn you. Safest route would be to head east.”

    - “Sure, I'll head east.” → [bwm_agent_2_7](#d-agent2-bwm_agent_2_7)
    - “Is there something you are not telling me?” → [bwm_agent_2_11](#d-agent2-bwm_agent_2_11)

    <span id="d-agent2-bwm_agent_2_11"></span>**`bwm_agent_2_11`** Agent: “No no, just head east and I'll explain everything to you once we get to the Blackwater mountain settlement.”

    - “OK, I promise to head east once we exit the mine.” → [bwm_agent_2_7](#d-agent2-bwm_agent_2_7)
    - “[Lie] OK, I promise to head east once we exit the mine.” → [bwm_agent_2_7](#d-agent2-bwm_agent_2_7)



### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 5 lines changed<br>· text: “The Gornauds? I have no idea where they come from, one day they just …” → “The gornauds? I have no idea where they come from, one day they just …” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (agent2)"

    | | |
    |---|---|
    | Entry ID | `agent2` |
    | Spawn group | `bwm_agent_2` |
    | Loot table | – |
    | Conversation | `bwm_agent_2_start` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:4` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "agent2",
     "name": "Agent",
     "iconID": "monsters_men:4",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "bwm_agent_2",
     "phraseID": "bwm_agent_2_start"
    }
    ```


## Blackwater Mountain, Blackwater mountain 14 (agent3) { #v-agent3 }

**Entry ID:** `agent3` · **Type:** NPC

**Location:** Blackwater Mountain: [Blackwater mountain 14](../maps/blackwater_mountain14.md#pin-npc-agent3)

### Quests

- [The agent and the beast](../quests/bwm_agent.md): stage 30

### Dialogue simulator

Set your quest stages and items, then talk to Agent. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/bwm_agent_3_start.json" data-npc="Agent" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (8 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-agent3-bwm_agent_3_start"></span>**`bwm_agent_3_start`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 30 of [The agent and the beast](../quests/bwm_agent.md#stage-30))* → [bwm_agent_3_4](#d-agent3-bwm_agent_3_4)
    - branch 2 → [bwm_agent_3_1](#d-agent3-bwm_agent_3_1)

    <span id="d-agent3-bwm_agent_3_4"></span>**`bwm_agent_3_4`** Agent: “Beware of the nasty monsters, they can really cause some harm!” — **effects:** sets stage 30 of [The agent and the beast](../quests/bwm_agent.md#stage-30)

    - “OK, I will follow this path up the mountain.” → *NPC leaves*
    - “Great, more monsters. Just what I needed.” → *NPC leaves*

    <span id="d-agent3-bwm_agent_3_1"></span>**`bwm_agent_3_1`** Agent: “Hello. You made it here, good.”

    - “I talked to some people in the village Prim. They had some interesting things to say about Blackwater mountain.” *(if reached stage 25 of [The agent and the beast](../quests/bwm_agent.md#stage-25))* → [bwm_agent_3_5](#d-agent3-bwm_agent_3_5)
    - “I went east, as you said.” → [bwm_agent_3_2](#d-agent3-bwm_agent_3_2)

    <span id="d-agent3-bwm_agent_3_5"></span>**`bwm_agent_3_5`** Agent: “Do not listen to their lies. They poison your thoughts and would not hesitate to stab you in the back once they get the chance.”

    - “What have they done?” → [bwm_agent_3_6](#d-agent3-bwm_agent_3_6)
    - “Yes, they do seem a bit shady.” → [bwm_agent_3_7](#d-agent3-bwm_agent_3_7)

    <span id="d-agent3-bwm_agent_3_2"></span>**`bwm_agent_3_2`** Agent: “Good. Now let's get up this mountain. I will meet you halfway up there.”

    - Next → [bwm_agent_3_3](#d-agent3-bwm_agent_3_3)

    <span id="d-agent3-bwm_agent_3_6"></span>**`bwm_agent_3_6`** Agent: “I will not talk of them now. Follow me up to the Blackwater mountain settlement and we will talk more there.”

    - “Sure.” → [bwm_agent_3_2](#d-agent3-bwm_agent_3_2)
    - “I'm keeping my eye on you. But I'll agree to your terms for now.” → [bwm_agent_3_2](#d-agent3-bwm_agent_3_2)

    <span id="d-agent3-bwm_agent_3_7"></span>**`bwm_agent_3_7`** Agent: “Indeed they do.”

    - Next → [bwm_agent_3_6](#d-agent3-bwm_agent_3_6)

    <span id="d-agent3-bwm_agent_3_3"></span>**`bwm_agent_3_3`** Agent: “This path leads up to the Blackwater mountain settlement. Follow this path and we will talk later.”

    - Next → [bwm_agent_3_4](#d-agent3-bwm_agent_3_4)



### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 3 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (agent3)"

    | | |
    |---|---|
    | Entry ID | `agent3` |
    | Spawn group | `bwm_agent_3` |
    | Loot table | – |
    | Conversation | `bwm_agent_3_start` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:4` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "agent3",
     "name": "Agent",
     "iconID": "monsters_men:4",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "bwm_agent_3",
     "phraseID": "bwm_agent_3_start"
    }
    ```


## Blackwater Mountain, Blackwater mountain 17 (agent4) { #v-agent4 }

**Entry ID:** `agent4` · **Type:** NPC

**Location:** Blackwater Mountain: [Blackwater mountain 17](../maps/blackwater_mountain17.md#pin-npc-agent4)

### Quests

- [The agent and the beast](../quests/bwm_agent.md): stage 40

### Dialogue simulator

Set your quest stages and items, then talk to Agent. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/bwm_agent_4_start.json" data-npc="Agent" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (8 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-agent4-bwm_agent_4_start"></span>**`bwm_agent_4_start`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 40 of [The agent and the beast](../quests/bwm_agent.md#stage-40))* → [bwm_agent_4_5](#d-agent4-bwm_agent_4_5)
    - branch 2 → [bwm_agent_4_1](#d-agent4-bwm_agent_4_1)

    <span id="d-agent4-bwm_agent_4_5"></span>**`bwm_agent_4_5`** Agent: “Meet me further up the mountain, and we will talk more.” — **effects:** sets stage 40 of [The agent and the beast](../quests/bwm_agent.md#stage-40)

    - “OK, see you there.” → *NPC leaves*

    <span id="d-agent4-bwm_agent_4_1"></span>**`bwm_agent_4_1`** Agent: “Hello again. Well done defeating the gornaud beasts.”

    - “Their attacks really hurt. What are these things?” → [bwm_agent_4_6](#d-agent4-bwm_agent_4_6)
    - “How come they do not attack you?” → [bwm_agent_4_3](#d-agent4-bwm_agent_4_3)
    - “Yeah, no problem. Just another trail of dead bodies behind me.” → [bwm_agent_4_2](#d-agent4-bwm_agent_4_2)

    <span id="d-agent4-bwm_agent_4_6"></span>**`bwm_agent_4_6`** Agent: “I do not know where they come from. All I know is that they started to appear one day, blocking the path up the mountain.”

    - Next → [bwm_agent_4_7](#d-agent4-bwm_agent_4_7)

    <span id="d-agent4-bwm_agent_4_3"></span>**`bwm_agent_4_3`** Agent: “Me? There must be something about me that scares them. I have no idea what it would be, some scent perhaps?”

    - Next → [bwm_agent_4_4](#d-agent4-bwm_agent_4_4)

    <span id="d-agent4-bwm_agent_4_2"></span>**`bwm_agent_4_2`** Agent: “Careful what you wish for, for it may come true.”

    - Next → [bwm_agent_4_4](#d-agent4-bwm_agent_4_4)

    <span id="d-agent4-bwm_agent_4_7"></span>**`bwm_agent_4_7`** Agent: “And, their attacks are tough. Once one of them gets a hold of you, the other ones seem really eager to hit you too.”

    - “Nothing I can't handle.” → [bwm_agent_4_4](#d-agent4-bwm_agent_4_4)
    - “How come they do not attack you?” → [bwm_agent_4_3](#d-agent4-bwm_agent_4_3)

    <span id="d-agent4-bwm_agent_4_4"></span>**`bwm_agent_4_4`** Agent: “Anyway, we should get going. I'll run ahead of you up the mountain.”

    - Next → [bwm_agent_4_5](#d-agent4-bwm_agent_4_5)



### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 3 lines changed<br>· text: “Hello again. Well done defeating the Gornaud beasts.” → “Hello again. Well done defeating the gornaud beasts.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (agent4)"

    | | |
    |---|---|
    | Entry ID | `agent4` |
    | Spawn group | `bwm_agent_4` |
    | Loot table | – |
    | Conversation | `bwm_agent_4_start` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:4` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "agent4",
     "name": "Agent",
     "iconID": "monsters_men:4",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "bwm_agent_4",
     "phraseID": "bwm_agent_4_start"
    }
    ```


## Blackwater Mountain, Blackwater mountain 30 (agent5) { #v-agent5 }

**Entry ID:** `agent5` · **Type:** NPC

**Location:** Blackwater Mountain: [Blackwater mountain 30](../maps/blackwater_mountain30.md#pin-npc-agent5)

### Quests

- [The agent and the beast](../quests/bwm_agent.md): stage 50

### Dialogue simulator

Set your quest stages and items, then talk to Agent. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/bwm_agent_5_start.json" data-npc="Agent" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (7 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-agent5-bwm_agent_5_start"></span>**`bwm_agent_5_start`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 50 of [The agent and the beast](../quests/bwm_agent.md#stage-50))* → [bwm_agent_5_6](#d-agent5-bwm_agent_5_6)
    - branch 2 → [bwm_agent_5_1](#d-agent5-bwm_agent_5_1)

    <span id="d-agent5-bwm_agent_5_6"></span>**`bwm_agent_5_6`** Agent: “Now hurry. We are almost there. Follow the snowy path to the north, and you should reach the settlement in no time.” — **effects:** sets stage 50 of [The agent and the beast](../quests/bwm_agent.md#stage-50)

    - “OK, I will follow the path to the north, further up the mountain.” → *NPC leaves*

    <span id="d-agent5-bwm_agent_5_1"></span>**`bwm_agent_5_1`** Agent: “Hello again. Well done getting through those monsters.”

    - Next → [bwm_agent_5_2](#d-agent5-bwm_agent_5_2)

    <span id="d-agent5-bwm_agent_5_2"></span>**`bwm_agent_5_2`** Agent: “We are almost there now. Just a little bit more.”

    - Next → [bwm_agent_5_3](#d-agent5-bwm_agent_5_3)

    <span id="d-agent5-bwm_agent_5_3"></span>**`bwm_agent_5_3`** Agent: “We should hurry this last bit, my settlement is close now.”

    - Next → [bwm_agent_5_4](#d-agent5-bwm_agent_5_4)

    <span id="d-agent5-bwm_agent_5_4"></span>**`bwm_agent_5_4`** Agent: “I hope you can manage the cold out here.”

    - Next → [bwm_agent_5_5](#d-agent5-bwm_agent_5_5)

    <span id="d-agent5-bwm_agent_5_5"></span>**`bwm_agent_5_5`** Agent: “Also, stay away from the wyrms. They have a really nasty bite.”

    - Next → [bwm_agent_5_6](#d-agent5-bwm_agent_5_6)



### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (agent5)"

    | | |
    |---|---|
    | Entry ID | `agent5` |
    | Spawn group | `bwm_agent_5` |
    | Loot table | – |
    | Conversation | `bwm_agent_5_start` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:4` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "agent5",
     "name": "Agent",
     "iconID": "monsters_men:4",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "bwm_agent_5",
     "phraseID": "bwm_agent_5_start"
    }
    ```


## Blackwater Mountain, Blackwater mountain 38 (agent6) { #v-agent6 }

**Entry ID:** `agent6` · **Type:** NPC

**Location:** Blackwater Mountain: [Blackwater mountain 38](../maps/blackwater_mountain38.md#pin-npc-agent6)

### Quests

- [The agent and the beast](../quests/bwm_agent.md): stage 60

### Dialogue simulator

Set your quest stages and items, then talk to Agent. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/bwm_agent_6_start.json" data-npc="Agent" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (9 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-agent6-bwm_agent_6_start"></span>**`bwm_agent_6_start`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 60 of [The agent and the beast](../quests/bwm_agent.md#stage-60))* → [bwm_agent_6_3](#d-agent6-bwm_agent_6_3)
    - branch 2 → [bwm_agent_6_0](#d-agent6-bwm_agent_6_0)

    <span id="d-agent6-bwm_agent_6_3"></span>**`bwm_agent_6_3`** Agent: “Go ahead, I will meet you inside.”

    - “OK, see you inside.” → *NPC leaves*

    <span id="d-agent6-bwm_agent_6_0"></span>**`bwm_agent_6_0`** Agent: “We meet again. Well done fighting your way up here.”

    - Next → [bwm_agent_6_1](#d-agent6-bwm_agent_6_1)

    <span id="d-agent6-bwm_agent_6_1"></span>**`bwm_agent_6_1`** Agent: “I am glad you followed me up the mountain to help us out.”

    - “How did you get up here so fast?” → [bwm_agent_6_6](#d-agent6-bwm_agent_6_6)
    - “Those were some tough fights, but I can manage.” → [bwm_agent_6_5](#d-agent6-bwm_agent_6_5)
    - “Are we there yet?” → [bwm_agent_6_2](#d-agent6-bwm_agent_6_2)

    <span id="d-agent6-bwm_agent_6_6"></span>**`bwm_agent_6_6`** Agent: “I learned some shortcuts up and down the mountain a while back. Nothing strange about that right?”

    - Next → [bwm_agent_6_7](#d-agent6-bwm_agent_6_7)

    <span id="d-agent6-bwm_agent_6_5"></span>**`bwm_agent_6_5`** Agent: “Yes, you seem like an able fighter.”

    - “Are we there yet?” → [bwm_agent_6_2](#d-agent6-bwm_agent_6_2)

    <span id="d-agent6-bwm_agent_6_2"></span>**`bwm_agent_6_2`** Agent: “Oh yes. In fact, our Blackwater mountain settlement is just down these stairs.”

    - Next → [bwm_agent_6_4](#d-agent6-bwm_agent_6_4)

    <span id="d-agent6-bwm_agent_6_7"></span>**`bwm_agent_6_7`** Agent: “Anyway, we are right at the settlement now. In fact, our Blackwater mountain settlement is just down these stairs.”

    - Next → [bwm_agent_6_4](#d-agent6-bwm_agent_6_4)

    <span id="d-agent6-bwm_agent_6_4"></span>**`bwm_agent_6_4`** Agent: “You should go down these stairs and talk to our battle master, Harlenn. He can usually be found at the third level down.” — **effects:** sets stage 60 of [The agent and the beast](../quests/bwm_agent.md#stage-60)

    - Next → [bwm_agent_6_3](#d-agent6-bwm_agent_6_3)



### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (agent6)"

    | | |
    |---|---|
    | Entry ID | `agent6` |
    | Spawn group | `bwm_agent_6` |
    | Loot table | – |
    | Conversation | `bwm_agent_6_start` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:4` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "agent6",
     "name": "Agent",
     "iconID": "monsters_men:4",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "bwm_agent_6",
     "phraseID": "bwm_agent_6_start"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agent1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agent1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agent1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agent1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
