# ![](../assets/icons/monsters/monsters_rltiles1_2.png){ .sprite } Glowing flame

| Stat | Value |
|---|---|
| Class | construct |
| HP | 112 |
| Max AP | 10 |
| Attack cost | 3 |
| Move cost | 5 |
| Damage | 0 to 9 |
| Attack chance | 153 |
| Block chance | 94 |
| Damage resistance | 6 |
| Critical skill | 15 |
| Critical multiplier | 2.5 |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons can't be critically hit. Your crit build will have to sit this one out.

## On hit

- **On target:** Ablaze (magnitude 1, 5 rounds, 20% chance)

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Burnt ash](../items/ash.md) | 10% | 0 to 1 |
| [Glass gem](../items/gem1.md) | 100% | 1 to 3 |

## Found on

- [lostmine10](../maps/lostmine10.md)
- [lostmine9](../maps/lostmine9.md)

## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | attackDamage: {"max": 9} → {"max": 9, "min": 0}; criticalMultiplier: 2.5 → 2.5; hitEffect: {"conditionsTarget": [{"chance": 20, "c… → {"conditionsTarget": [{"chance": "20", … |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

<small>Monster ID: `fire5` · Data from v0.8.18</small>
