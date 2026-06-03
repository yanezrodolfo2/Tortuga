# Tortuga
Self-righting, dust-tolerant scout rover. Mechanical engineering portfolio project.
[README.md](https://github.com/user-attachments/files/28533366/README.md)
# Scout Rover

A self-righting, dust-tolerant scout rover designed and built as a single-semester engineering portfolio project. Built to investigate two real challenges in Mars surface robotics — **flip recovery** and **dust ingress** — at hobby scale, using analog testing in the Sonoran Desert (Tucson, AZ).

**Author:** Rodolfo Yanez — Mechanical Engineering, University of Arizona
**Status:** In development — Phase 1
**Target completion:** End of Spring 2026 semester

---

## Why This Project Exists

Most student rovers are kit assemblies: drop-in chassis, hobby motors, off-the-shelf brain, demo on a clean floor. They demonstrate *integration*, not *engineering*.

This project takes a different approach. It picks two failure modes that have ended real Mars missions and treats them as the central design problem:

1. **Loss of mobility from inversion.** A flipped rover is a dead rover unless it can recover autonomously. Curiosity and Perseverance avoid this problem with low, wide chassis geometry — but that geometry limits the terrain they can attempt. Smaller scout-class rovers need active recovery.

2. **Dust ingress.** Martian regolith is electrostatically charged and abrasive. Spirit's wheel actuators degraded from dust exposure. JPL invests significant engineering effort in seals, filters, and dust-tolerant mechanisms. Hobby rovers ignore this entirely.

The goal is not to replicate JPL hardware. The goal is to take JPL-class *problems*, scope them down to hobby budget and timeline, and document the engineering decisions made along the way.

---

## Design Goals (Measurable)

| # | Goal | Target | Status |
|---|------|--------|--------|
| 1 | Autonomous obstacle avoidance | No collision over 5-min run | Pending |
| 2 | Live camera stream | <500 ms latency, 480p min | Pending |
| 3 | Self-right from any inverted orientation | 100% success over 10 trials | Pending |
| 4 | Sealed drivetrain | Operate 2+ hours in desert sand without bearing/motor degradation | Pending |
| 5 | Thermal tolerance | Continuous operation in 95°F+ ambient | Pending |
| 6 | Battery life | ≥45 min continuous drive | Pending |

These targets will be revised as design progresses. Every revision will be logged in the [Engineering Decisions](#engineering-decisions) section.

---

## Phased Build Plan

The project is structured in phases. Each phase produces a working, demoable milestone — not a half-finished system.

### Phase 1 — Drive + perceive *(Weeks 1–5)*
- Chassis CAD complete, 3D printed
- 4-wheel drive functional under remote control
- Ultrasonic obstacle avoidance working
- Raspberry Pi camera streaming over local network
- **Milestone:** Rover drives itself around an indoor course without collisions

### Phase 1.5 — The differentiators *(Weeks 6–8)*
- Self-righting mechanism integrated
- Sealed drivetrain components installed (labyrinth seals, sealed bearings)
- IMU-triggered recovery sequence working
- **Milestone:** Rover recovers from forced flips in lab conditions

### Phase 2 — Field testing *(Weeks 9–10)*
- Outdoor testing in Tucson desert terrain
- Dust exposure protocol: run, disassemble, document wear
- Before/after photos of drivetrain components
- **Milestone:** Documented test results showing seal performance

### Phase 3 — *(Future, post-semester)*
- GPS waypoint navigation
- Possibly: sample-collection gripper (MSR-inspired)

---

## Engineering Decisions

This section logs every non-trivial design decision and the reasoning behind it. It is the most important part of this document.

### Decision 1: Raspberry Pi over Arduino as primary controller
**Decision:** Raspberry Pi 4 (4GB) for main control.
**Why:** Camera streaming and image processing are roadmap items. Arduino can drive motors but cannot stream video or run higher-level autonomy code. The Pi handles both. A microcontroller may be added later for real-time motor control if latency becomes an issue.
**Trade-off accepted:** Higher power draw, less deterministic timing.

### Decision 2: PETG over PLA for chassis and seal housings
**Decision:** PETG for all structural and sealing parts.
**Why:** PLA glass-transition temperature is ~60°C. A car interior in Tucson summer routinely exceeds this. PETG (~75–80°C Tg) handles desert heat. ASA would be better but is harder to print reliably on the UA student printers.
**Trade-off accepted:** PETG is harder to print cleanly than PLA; first prints may need tuning.

### Decision 3: Self-righting via deployable arm (not symmetric chassis)
**Decision:** Single servo-driven arm that pushes the rover back upright when inverted.
**Why:** Symmetric (operate-either-side-up) chassis was considered but doubles the design constraints — every external sensor, the camera, and the wheels would need to work in either orientation. A deployable arm isolates the complexity to one mechanism.
**Trade-off accepted:** Single point of failure. If the servo or linkage breaks, no recovery.

### Decision 4: Labyrinth seals over lip seals
**Decision:** *(Pending — to be finalized during CAD)*
**Why:** *(To be documented.)*

*(More decisions will be added as the project progresses.)*

---

## Calculations

Detailed engineering calculations live in `/docs/calcs/`. Summary:

- **Center of mass estimation** — *(pending)*
- **Self-righting arm sizing** (length × torque vs. CoM offset) — *(pending)*
- **Servo torque selection** — *(pending)*
- **Motor torque required for 30° slope climb** — *(pending)*
- **Bearing radial load per wheel** — *(pending)*
- **Battery capacity vs. drive time** — *(pending)*

---

## Bill of Materials

*(Finalized at end of CAD phase. Placeholder estimates below.)*

| Subsystem | Component | Source | Est. Cost |
|-----------|-----------|--------|-----------|
| Compute | Raspberry Pi 4 (4GB) | Adafruit | $55 |
| Compute | 32GB microSD | Amazon | $10 |
| Drive | TT gear motors ×4 | Amazon | $15 |
| Drive | L298N motor driver | Amazon | $8 |
| Drive | Sealed bearings 608ZZ ×8 | Amazon | $10 |
| Sensing | HC-SR04 ultrasonic ×3 | Amazon | $10 |
| Sensing | Pi Camera Module v2 | Adafruit | $25 |
| Sensing | MPU-6050 IMU | Amazon | $5 |
| Power | 18650 cells ×3 + holder | Amazon | $20 |
| Power | TP4056 charger | Amazon | $5 |
| Power | 5V buck converter | Amazon | $8 |
| Mechanism | MG996R servo | Amazon | $8 |
| Hardware | M3 screws, standoffs, jumper wires | Amazon | $30 |
| Hardware | PETG filament | UA printer | ~$20 |
| **Total Phase 1 + 1.5** | | | **~$229** |

---

## Repository Structure

```
/cad         — Fusion 360 files and STL exports
/code        — Rover firmware and control scripts
/docs        — Engineering writeups, calculations, test data
/docs/calcs  — Hand calculations and analysis
/docs/tests  — Test protocols and results
/media       — Photos and demo videos
```

---

## Testing Protocol

*(To be expanded as testing begins.)*

- **Lab tests:** Indoor obstacle course, forced-flip recovery trials
- **Field tests:** Desert terrain runs at [location TBD] near Tucson
- **Documentation:** Photo log of drivetrain components before and after dust exposure

---

## Skills Demonstrated

*(For recruiters — updated as the project progresses.)*

- Mechanical design and CAD (Fusion 360)
- 3D printing for functional parts
- Statics applied to real mechanism design (CoM analysis, torque calculations)
- Electronics integration (Pi, motor drivers, sensors, power systems)
- Embedded software (Python on Raspberry Pi)
- Test design and field testing
- Technical documentation

---

## Contact

Rodolfo Yanez — Mechanical Engineering, University of Arizona
yanezrod21@gmail.com
