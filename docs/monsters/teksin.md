# ![](../assets/icons/monsters/monsters_tometik2_71.png){ .sprite } Teksin

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 0 |
| Max AP | 10 |
| Attack cost | 10 |
| Move cost | 10 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Irdegh poison elixir](../items/pot_irdegh_poison_elixir.md) | 100% | 2 to 3 |
| [Blackwater boots](../items/bwm_boots.md) | 100% | 1 |
| [Bread](../items/bread.md) | 100% | 1 to 3 |
| [Balanced steel sword](../items/sword_balanced_steel.md) | 100% | 1 |
| [Sharp steel dagger](../items/dagger_sharp_steel.md) | 100% | 1 |
| [Lightweight splint mail](../items/ltbdy_spmail.md) | 100% | 1 |
| [Fine green hat](../items/hat2.md) | 100% | 1 to 2 |
| [Ring of damage resistance](../items/ring_dr1.md) | 100% | 1 |
| [Cured ham](../items/cured_ham.md) | 100% | 1 to 4 |
| [Ring of dexterity](../items/ring_dexterity.md) | 100% | 1 |
| [Superior combat boots](../items/boots_combat3.md) | 100% | 1 |
| [Superior hard leather armor](../items/armor4.md) | 100% | 1 |
| [Fine gloves of swift attack](../items/gloves_attack2.md) | 100% | 1 |
| [Lesser ring of block](../items/ring_block1.md) | 100% | 1 |
| [Necklace of strike](../items/necklace_strike.md) | 100% | 1 |
| [Blackwater gloves](../items/bwm_gloves.md) | 100% | 1 |
| [Brandistock](../items/brandistock.md) | 100% | 1 |

## Found on

- [waytolake11](../maps/waytolake11.md)

## Quests

- [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md): stages 140, 150, 160

??? quote "Dialogue (14 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-teksin_10"></span>**`teksin_10`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 140 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-140))* → [teksin11](#d-teksin11)
    - Next *(if NOT reached stage 140 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-140))* → [teksin12](#d-teksin12)

    <span id="d-teksin11"></span>**`teksin11`** Teksin: “Hello again.”

    - “How do I get to Remgard?” *(if reached stage 160 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-160))* → [teksin70](#d-teksin70)
    - “What can you tell me about Remgard?” *(if reached stage 160 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-160))* → [teksin60](#d-teksin60)
    - “Do you have anything to trade?” → [teksin80](#d-teksin80)
    - “I'm looking for my brother, Andor. He looks a bit like me.” → [teksin20](#d-teksin20)

    <span id="d-teksin12"></span>**`teksin12`** Teksin: “Hello. My name is Teksin. I'm a trader. Who are you?” — **effects:** sets stage 140 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-140)

    - “I am $playername. I am looking for my brother, Andor. He looks a bit like me.” → [teksin20](#d-teksin20)

    <span id="d-teksin70"></span>**`teksin70`** Teksin: “You have to go back down to the river, then south until you find some caves. Go through the caves, up through the mountains, and then around the lake we are now standing next to. It's a long way, and as I said, there are some very bad…”

    - “I can handle it. I'm on my way.” → *conversation ends*
    - “It sounds dangerous. I think I'll go somewhere else.” → *conversation ends*
    - “Thanks for the information. Do you have anything to trade?” → [teksin80](#d-teksin80)

    <span id="d-teksin60"></span>**`teksin60`** Teksin: “Remgard is a town that is well protected by the lake that we are next to. It is peaceful, and far from any enemies, which makes it somewhat surprising that they make excellent armor there. The high quality of the goods available in…”

    - “How do I get to Remgard?” → [teksin70](#d-teksin70)
    - “Thanks for the information, but I have to leave now.” → *conversation ends*

    <span id="d-teksin80"></span>**`teksin80`** Teksin: “Yes. I think you will see that I sell quality items from many places. Under the circumstances I can only sell you limited provisions though.”

    - Next → [teksin85](#d-teksin85)

    <span id="d-teksin20"></span>**`teksin20`** Teksin: “Sorry. I haven't seen anyone that looks like you.”

    - Next → [teksin30](#d-teksin30)

    <span id="d-teksin85"></span>**`teksin85`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 150 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-150))* → [teksin90](#d-teksin90)
    - “OK. Show me what you have.” → *shop opens*

    <span id="d-teksin30"></span>**`teksin30`** Teksin: “I have been out in the wild for a while, and have seen nobody since I left the main road weeks ago.”

    - Next → [teksin40](#d-teksin40)

    <span id="d-teksin90"></span>**`teksin90`** Teksin: “I do also have one special item. It is a potion that increases your attack speed. It is very rare, and therefore expensive, but I am willing to part with it if the price is right.”

    - “No thanks. Show me what else you have.” → *shop opens*
    - “How expensive is "expensive"?” → [teksin100](#d-teksin100)

    <span id="d-teksin40"></span>**`teksin40`** Teksin: “I decided that I should find a better route to Remgard. The road through the mountains to the east is plagued by terrible monsters. My quest for a better route was a mistake though.”

    - Next → [teksin50](#d-teksin50)

    <span id="d-teksin100"></span>**`teksin100`** Teksin: “For you, I will offer the special price of 4,999 gold.”

    - “I don't have that much gold. Please show me what else you have.” *(if have 4,999 gold)* → *shop opens*
    - “That's too expensive. Please show me what else you have.” *(if have 4,999 gold)* → *shop opens*
    - “OK. I'll take it.” *(if pay 4,999 gold)* → [teksin110](#d-teksin110)
    - “I think I'll just be on my way.” → *conversation ends*

    <span id="d-teksin50"></span>**`teksin50`** Teksin: “This is as close as I can get coming this way. I am an experienced traveler, and I know that Remgard is close. It's north across this lake, but there is no way to cross, or to go further east around the lake.” — **effects:** sets stage 160 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-160)

    - “It sounds like you are not quite the experienced traveler you claim to be.” → *conversation ends*
    - “I guess it was worth a try. What can you tell me about Remgard?” → [teksin60](#d-teksin60)
    - “How do I get to Remgard?” → [teksin70](#d-teksin70)
    - “Do you have anything to trade?” → [teksin80](#d-teksin80)

    <span id="d-teksin110"></span>**`teksin110`** Teksin: “Use it wisely. Such a potion is very hard to obtain. It is unlikely I will have any more to sell in the future.” — **effects:** sets stage 150 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-150), gives 1× [Potion of lightning attack](../items/pot_light_attack.md)

    - “Thanks for the advice. Please show me what else you have to trade.” → *shop opens*
    - “Thanks for the advice. I need to go now.” → *conversation ends*



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=teksin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=teksin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=teksin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=teksin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `teksin` · Data from v0.8.18</small>
