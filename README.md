# Tortuga

A self-righting, dust-tolerant scout rover. Mechanical engineering portfolio project.

**Built by:** Rodolfo Yanez — Mechanical Engineering, University of Arizona
**Status:** Phase 1 — chassis CAD complete, electronics integration next
**Timeline:** Summer 2026

---

## What problem does this solve?

Most student rovers are kit assemblies — they demonstrate integration, not engineering. Tortuga is built around two failure modes that have ended real Mars missions:

1. **Inversion.** A flipped rover is a dead rover without active recovery.
2. **Dust ingress.** Martian regolith degrades unsealed drivetrains.

The goal is not to replicate JPL hardware. The goal is to take JPL-class problems, scope them to hobby budget, and document the engineering decisions — at hobby scale, in the Sonoran Desert.

---

## Design highlights

- **Tortoise-shell chassis** — asymmetric rounded outline reduces catch points during inversion
- **Self-righting mechanism** — single servo-driven arm, IMU-triggered recovery
- **Sealed drivetrain** — labyrinth seals + sealed bearings for desert operation
- **SolidWorks parametric CAD** — every dimension is driven, fully editable
- **PETG construction** — survives Tucson summer heat (PLA would deform)

---

## Specs

| | |
|---|---|
| Footprint | 215mm × 160mm |
| Ground clearance | ~40mm |
| Drive | 4WD, TT gear motors, 80mm off-road wheels |
| Brain | Raspberry Pi 4 (4GB) |
| Sensors | HC-SR04 ultrasonic, MPU-6050 IMU, Pi Camera v2 |
| Power | 3x 18650 Li-ion |
| Target operating time | 45+ min continuous |

Full bill of materials in [`docs/bom.md`](docs/bom.md).

---

## Build phases

| Phase | What ships | Status |
|-------|-----------|--------|
| 1 | Drive + obstacle avoidance + camera stream | In progress |
| 1.5 | Self-righting + sealed drivetrain | Planned |
| 2 | Sonoran Desert field testing + dust analysis | Planned |
| 3 | GPS waypoint navigation, sample-collection gripper | Fall |

---

## Documentation

- [Engineering decision log](docs/decisions.md) — every non-trivial design choice and the reasoning behind it
- [Bill of materials](docs/bom.md) — components, sources, costs
- [Build schedule](docs/Rover_Project_Plan.docx) — 10-week project plan with milestones
- [CAD files](cad/) — SolidWorks source + STL exports, organized by subsystem

---

## Skills demonstrated

Mechanical design (SolidWorks) - Parametric CAD - 3D printing for functional parts - Statics applied to mechanism design - Electronics integration - Embedded Python - Technical documentation
