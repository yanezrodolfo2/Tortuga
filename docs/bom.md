# Bill of Materials

Estimated Phase 1 + 1.5 component costs. Final list locked in at end of CAD phase. All electronics sourced from Amazon, Adafruit, or SparkFun — never general hardware stores. Hardware (screws, standoffs) and tools sourced locally where convenient.

---

## Phase 1 + 1.5 components

| Subsystem | Component | Source | Est. Cost |
|-----------|-----------|--------|-----------|
| Compute | Raspberry Pi 4 (4GB) | Adafruit | $55 |
| Compute | 32GB microSD card | Amazon | $10 |
| Drive | TT gear motors ×4 + wheels | Amazon | $15 |
| Drive | L298N motor driver | Amazon | $8 |
| Drive | 80mm off-road rubber wheels ×4 | Amazon | $12 |
| Drive | Sealed bearings 608ZZ ×8 | Amazon | $10 |
| Sensing | HC-SR04 ultrasonic ×3 | Amazon | $10 |
| Sensing | Pi Camera Module v2 | Adafruit | $25 |
| Sensing | MPU-6050 IMU | Amazon | $5 |
| Power | 18650 cells ×3 + holder | Amazon | $20 |
| Power | TP4056 charger module | Amazon | $5 |
| Power | 5V buck converter | Amazon | $8 |
| Mechanism | MG996R servo (righting arm) | Amazon | $8 |
| Hardware | M3 standoffs kit (35mm + assorted) | Amazon | $15 |
| Hardware | M3 screws, nuts, washers | Amazon | $15 |
| Hardware | Jumper wires + breadboard | Amazon | $10 |
| Hardware | PETG filament (1kg) | UA makerspace | $20 |
| **Total Phase 1 + 1.5** | | | **~$251** |

---

## Phase 2 (field testing)

| Component | Source | Est. Cost |
|-----------|--------|-----------|
| Spare batteries + chargers | Amazon | $15 |
| Replacement parts buffer | Amazon | $30 |
| Field photography setup (phone tripod) | Amazon | $20 |
| **Phase 2 total** | | **~$65** |

---

## Phase 3 (post-semester — future)

| Component | Source | Est. Cost |
|-----------|--------|-----------|
| GPS module (NEO-6M or similar) | Amazon | $15 |
| Servo + linkage for sample gripper | Amazon | $25 |
| Magnetic encoders (TT motor add-on) | Amazon | $10 |
| **Phase 3 total** | | **~$50** |

---

## Project budget summary

| Phase | Estimate |
|-------|----------|
| Phase 1 + 1.5 | $251 |
| Phase 2 buffer | $65 |
| Phase 3 (future) | $50 |
| **Total project envelope** | **~$366** |

Project budget cap: $300–$500. Phase 1 + 1.5 alone fits within budget with ~$50 cushion for failed components (expect to lose 1–2 parts as a first-time builder). Phase 3 is post-semester scope and not part of the initial budget.

---

## Sourcing notes

- **Avoid Arduino-branded boards.** 2–3× markup vs. clones with identical functionality.
- **Verify TT motor + wheel hub compatibility before ordering.** Some 80mm wheels ship without the D-shaft adapter and require a separate coupling.
- **Order PETG in advance.** UA makerspace stocks PLA reliably but PETG availability is inconsistent.
- **Buffer for failures.** First electronics build expects 1–2 fried components from reverse polarity or wrong voltage. Budget includes this — do not skip the buffer.
