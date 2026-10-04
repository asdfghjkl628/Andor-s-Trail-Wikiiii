# ![](../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite } Feygard patrol watch

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 80 |
| Max AP | 10 |
| Attack cost | 5 |
| Move cost | 10 |
| Damage | 2 to 7 |
| Attack chance | 70 |
| Block chance | 80 |
| Damage resistance | 3 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Feygard patrol ring](../items/ffguard_qitem.md) | 100% | 1 |
| [Small empty vial](../items/vial_empty1.md) | 100% | 1 |
| [Wooden buckler](../items/shield1.md) | 100% | 1 |
| [Iron sword](../items/ironsword1.md) | 100% | 1 |

## Found on

- [road1](../maps/road1.md)

## Quests

- [Spies in the foam](../quests/jolnor.md): stages 20, 21

??? quote "Dialogue (26 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ff_outsideguard_select"></span>**`ff_outsideguard_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 20 of [Spies in the foam](../quests/jolnor.md#stage-20))* → [ff_outsideguard_trouble_24](#d-ff_outsideguard_trouble_24)
    - branch 2 → [ff_outsideguard_1](#d-ff_outsideguard_1)

    <span id="d-ff_outsideguard_trouble_24"></span>**`ff_outsideguard_trouble_24`** Feygard patrol watch: “I will go inside in a minute. Will you stand watch while I go inside?” — **effects:** sets stage 20 of [Spies in the foam](../quests/jolnor.md#stage-20)

    - “Sure, I will do that.” → [ff_outsideguard_trouble_25](#d-ff_outsideguard_trouble_25)
    - “[Lie] Sure, I will do that.” → [ff_outsideguard_trouble_25](#d-ff_outsideguard_trouble_25)

    <span id="d-ff_outsideguard_1"></span>**`ff_outsideguard_1`** Feygard patrol watch: “Hello there. Should you be here? This is a tavern, you know. The Foaming Flask, to be precise.”

    - “Who are you?” → [ff_outsideguard_2](#d-ff_outsideguard_2)

    <span id="d-ff_outsideguard_trouble_25"></span>**`ff_outsideguard_trouble_25`** Feygard patrol watch: “Thanks a lot my friend.”


    <span id="d-ff_outsideguard_2"></span>**`ff_outsideguard_2`** Feygard patrol watch: “I am a member of the royal guard patrol from Feygard.”

    - “Feygard, where is that?” → [ff_outsideguard_3](#d-ff_outsideguard_3)
    - “What do you do around here?” → [ff_outsideguard_3](#d-ff_outsideguard_3)

    <span id="d-ff_outsideguard_3"></span>**`ff_outsideguard_3`** Feygard patrol watch: “Go talk to the captain inside if you want to talk. I must stay alert on my post.”

    - “OK. Goodbye.” → *conversation ends*
    - “Why must you stay alert outside a tavern?” *(if reached stage 10 of [Spies in the foam](../quests/jolnor.md#stage-10))* → [ff_outsideguard_trouble_1](#d-ff_outsideguard_trouble_1)

    <span id="d-ff_outsideguard_trouble_1"></span>**`ff_outsideguard_trouble_1`** Feygard patrol watch: “Really, I cannot talk to you. I could get into trouble.”

    - “OK. I won't bother you anymore. Shadow be with you.” → [ff_outsideguard_shadow_1](#d-ff_outsideguard_shadow_1)
    - “OK. I won't bother you anymore. Goodbye.” → *conversation ends*
    - “What trouble?” → [ff_outsideguard_trouble_2](#d-ff_outsideguard_trouble_2)

    <span id="d-ff_outsideguard_shadow_1"></span>**`ff_outsideguard_shadow_1`** Feygard patrol watch: “Shadow? How curious that you would mention that. Explain yourself!”

    - “I did not mean a thing by it. Never mind I said anything.” → [ff_outsideguard_shadow_2](#d-ff_outsideguard_shadow_2)
    - “The Shadow watches over us when we sleep.” → [ff_outsideguard_shadow_3](#d-ff_outsideguard_shadow_3)

    <span id="d-ff_outsideguard_trouble_2"></span>**`ff_outsideguard_trouble_2`** Feygard patrol watch: “No really, the captain might see me. I must be aware on my post at all times. *sigh*”

    - “OK. I won't bother you anymore. Shadow be with you.” → [ff_outsideguard_shadow_1](#d-ff_outsideguard_shadow_1)
    - “OK. I won't bother you anymore. Goodbye.” → *conversation ends*
    - “Do you like your job here?” → [ff_outsideguard_trouble_3](#d-ff_outsideguard_trouble_3)

    <span id="d-ff_outsideguard_shadow_2"></span>**`ff_outsideguard_shadow_2`** Feygard patrol watch: “Good. Now be gone before I will have to deal with you.”


    <span id="d-ff_outsideguard_shadow_3"></span>**`ff_outsideguard_shadow_3`** Feygard patrol watch: “What? Are you one of those troublemakers sent here to sabotage our mission?”

    - “The Shadow protects us.” → [ff_outsideguard_shadow_4](#d-ff_outsideguard_shadow_4)
    - “Fine. I better not start a fight with the royal guard.” → *conversation ends*

    <span id="d-ff_outsideguard_trouble_3"></span>**`ff_outsideguard_trouble_3`** Feygard patrol watch: “My job? I guess the royal guard is OK. I mean, Feygard is a really nice place to live in.”

    - Next → [ff_outsideguard_trouble_4](#d-ff_outsideguard_trouble_4)

    <span id="d-ff_outsideguard_shadow_4"></span>**`ff_outsideguard_shadow_4`** Feygard patrol watch: “That does it. You better fight or flee right now kid.”

    - “Good. I have been waiting for a fight!” → [ff_outsideguard_shadow_5](#d-ff_outsideguard_shadow_5)
    - “For the Shadow!” → [ff_outsideguard_shadow_5](#d-ff_outsideguard_shadow_5)
    - “Never mind. I was just kidding with you.” → [ff_outsideguard_shadow_2](#d-ff_outsideguard_shadow_2)

    <span id="d-ff_outsideguard_trouble_4"></span>**`ff_outsideguard_trouble_4`** Feygard patrol watch: “Standing guard on duty out here in the middle of nowhere is not really what I signed up for.”

    - “I bet. This place is really boring.” → [ff_outsideguard_trouble_5](#d-ff_outsideguard_trouble_5)
    - “You must get tired of just standing here also.” → [ff_outsideguard_trouble_5](#d-ff_outsideguard_trouble_5)

    <span id="d-ff_outsideguard_shadow_5"></span>**`ff_outsideguard_shadow_5`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 21 of [Spies in the foam](../quests/jolnor.md#stage-21)

    - branch 1 → *fight starts*

    <span id="d-ff_outsideguard_trouble_5"></span>**`ff_outsideguard_trouble_5`** Feygard patrol watch: “Yeah I know. I would rather be inside in the tavern drinking like the senior officers and the captain. How come I have to stand out here?”

    - “At least the Shadow watches over you.” → [ff_outsideguard_shadow_1](#d-ff_outsideguard_shadow_1)
    - “Why not just leave if it's not what you want to do?” → [ff_outsideguard_trouble_7](#d-ff_outsideguard_trouble_7)
    - “The greater cause of the royal guard, to keep the peace, is worth it in the long run.” → [ff_outsideguard_trouble_6](#d-ff_outsideguard_trouble_6)

    <span id="d-ff_outsideguard_trouble_7"></span>**`ff_outsideguard_trouble_7`** Feygard patrol watch: “No, my loyalty is to Feygard. If I would leave, I would also leave my loyalty behind.”

    - “What does that mean if you are not satisfied with what you do?” → [ff_outsideguard_trouble_9](#d-ff_outsideguard_trouble_9)
    - “Yes, that sounds right. Feygard sounds like a nice place from what I have heard.” → [ff_outsideguard_trouble_6](#d-ff_outsideguard_trouble_6)

    <span id="d-ff_outsideguard_trouble_6"></span>**`ff_outsideguard_trouble_6`** Feygard patrol watch: “Yes, you are right of course. Our duty is to Feygard and to keep the peace from all that want to disrupt it.”

    - “Yes. The Shadow will not look favorably upon those that disrupt the peace.” → [ff_outsideguard_shadow_1](#d-ff_outsideguard_shadow_1)
    - “Yes. The troublemakers should be punished.” → [ff_outsideguard_trouble_8](#d-ff_outsideguard_trouble_8)

    <span id="d-ff_outsideguard_trouble_9"></span>**`ff_outsideguard_trouble_9`** Feygard patrol watch: “Well, I am convinced that we must follow the laws laid down by our rulers. If we don't obey the law, what are we left with?”

    - Next → [ff_outsideguard_trouble_10](#d-ff_outsideguard_trouble_10)

    <span id="d-ff_outsideguard_trouble_8"></span>**`ff_outsideguard_trouble_8`** Feygard patrol watch: “Right. I like you, kid. Tell you what, I could put in a good word for you in the barracks when we get back to Feygard if you want.”

    - “Sure, that sounds good to me.” → [ff_outsideguard_trouble_20](#d-ff_outsideguard_trouble_20)
    - “No thanks. I have enough to do already.” → [ff_outsideguard_trouble_20](#d-ff_outsideguard_trouble_20)

    <span id="d-ff_outsideguard_trouble_10"></span>**`ff_outsideguard_trouble_10`** Feygard patrol watch: “Chaos. Disorder. No, I prefer the lawful way of Feygard. My loyalty is firm.”

    - “Sounds good to me. Laws are made to be followed.” → [ff_outsideguard_trouble_8](#d-ff_outsideguard_trouble_8)
    - “I do not agree. We should follow our heart, even if that goes against the rules.” → [ff_outsideguard_trouble_12](#d-ff_outsideguard_trouble_12)

    <span id="d-ff_outsideguard_trouble_20"></span>**`ff_outsideguard_trouble_20`** Feygard patrol watch: “Was there anything else you wanted?”

    - “I was wondering about why you stand guard here.” → [ff_outsideguard_trouble_21](#d-ff_outsideguard_trouble_21)

    <span id="d-ff_outsideguard_trouble_12"></span>**`ff_outsideguard_trouble_12`** Feygard patrol watch: “That troubles me. We might see each other again in the future. But then we might not be able to have this kind of civil discussion.”


    <span id="d-ff_outsideguard_trouble_21"></span>**`ff_outsideguard_trouble_21`** Feygard patrol watch: “Right, we went over this before. As I said, I would rather be inside by the fire.”

    - “I could spot for you if you want to go inside.” → [ff_outsideguard_trouble_23](#d-ff_outsideguard_trouble_23)
    - “Tough luck. I guess you are left out here, while your captain and buddies are inside.” → [ff_outsideguard_trouble_22](#d-ff_outsideguard_trouble_22)

    <span id="d-ff_outsideguard_trouble_23"></span>**`ff_outsideguard_trouble_23`** Feygard patrol watch: “Really? Yes that would be great. Then I can at least get something to eat and a bit of warmth from the fire.”

    - Next → [ff_outsideguard_trouble_24](#d-ff_outsideguard_trouble_24)

    <span id="d-ff_outsideguard_trouble_22"></span>**`ff_outsideguard_trouble_22`** Feygard patrol watch: “Yeah, that's just my luck.”




## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_patrol_watch.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_patrol_watch.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_patrol_watch.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_patrol_watch.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `feygard_patrol_watch` · Data from v0.8.18</small>
