# Engineering Decisions

Non-trivial design decisions for Tortuga, with reasoning and trade-offs. This log exists so I can defend every choice in an interview and so future-me remembers why. Trivial choices (filament color, exact tolerances, fastener brands) are omitted.

---

### Decision 1: Raspberry Pi over Arduino as primary controller
**Decision:** Raspberry Pi 4 (4GB). **Why:** Camera streaming and higher-level autonomy are roadmap items an Arduino can't do. The Pi handles both. **Trade-off:** Higher power draw, less deterministic timing than a microcontroller.

### Decision 2: PETG for final parts, PLA for prototypes
**Decision:** PETG for final structural parts; PLA for fit-check prototypes. **Why:** PLA softens above ~60°C — a Tucson car interior exceeds that. PETG (~75-80°C) survives desert heat. PLA is cheaper and more accurate for verifying fit before committing. **Trade-off:** PETG is harder to print clean and warps more on large flat parts.

### Decision 3: Self-righting via deployable arm, not symmetric chassis
**Decision:** Single servo-driven arm that levers the rover upright. **Why:** A symmetric operate-either-way chassis doubles every constraint — sensors, camera, wheels all needing to work inverted. An arm isolates the complexity to one mechanism. **Trade-off:** Single point of failure; if the servo or arm breaks, no recovery.

### Decision 4: Flip detection via IMU Z-axis with a dead band
**Decision:** MPU-6050 Z-axis acceleration determines orientation, with a ±5 m/s² dead band — above +5 upright, below −5 flipped, between is indeterminate. **Why:** Testing against zero causes rapid state flicker at steep angles, which would fire the arm repeatedly. The dead band forces a decisive orientation change. Sensor reads ~10-11 m/s² flat (offset from nominal 9.81 — common on cheap MPU-6050s) but sign-based detection is unaffected. **Trade-off:** Can't distinguish "on its side" from "mid-transition" — both handled as indeterminate.

### Decision 5: Chassis outline and dimensions
**Decision:** Base plate 230 × 180 × 4mm (enlarged from an initial 215 × 160), top deck 180 × 130 × 3mm, uniform 40mm corner fillets. **Why:** Enlarged so the body reads proportional to the 80mm wheels rather than dwarfed by them. Rounded outline reduces catch points during a flip. Front/rear defined by hole pattern, not shape, since the fillets are symmetric — the deck must be marked to avoid backwards assembly. **Trade-off:** 230mm is near the Prusa Core One's 240mm bed limit — prints with zero margin for error.

### Decision 6: Standoff span held constant across base plate redesigns
**Decision:** Kept the 6-standoff span at 140 × 50mm even when enlarging the base plate. **Why:** Holding the span constant means the existing top deck still fits any base plate revision — enlarging the plate doesn't cascade into a new deck. The standoffs just sit more central on a bigger plate. **Trade-off:** None meaningful; this is the move that kept a resize from becoming a full redesign.

### Decision 7: 4-corner motor layout, skid steer
**Decision:** Four TT motors in the corners, long axis along the rover's length, wheels on the long sides. No steering mechanism — turns by driving left and right sides at different speeds (skid steer). **Why:** Matches Mars rover wheelbase convention, maximizes 4WD traction, needs no steering linkage to break. **Trade-off:** Wheels scrub sideways in turns and it uses more power to turn than steered wheels.

### Decision 8: Motor bracket — sourced and adapted, not designed
**Decision:** Used a third-party 3D-printable TT motor bracket, modified to add mounting holes matching the base plate. **Why:** The TT motor's mounting holes sit on its top face at ~18-20mm spacing, which didn't match the plate's flat hole pattern. A proven bracket solves this without reinventing a standard part — time better spent on the parts that are actually mine. **Trade-off:** Not my original design; cited as adapted. The chassis, deck, camera bracket, righting arm, and servo mount are my designs.

### Decision 9: 80mm off-road wheels
**Decision:** 80mm chunky-tread rubber wheels on the TT motors. **Why:** ~40mm ground clearance vs ~25mm on standard 65mm wheels — meaningful for desert terrain. Tread grips loose sand. Hub fits the D-shaft directly, no adapter. **Trade-off:** No encoders on TT motors, so no closed-loop speed control without a later add-on. High wheel-to-body ratio drove the chassis enlargement in Decision 5.

### Decision 10: CAD in SolidWorks
**Decision:** SolidWorks as the CAD environment. **Why:** Dominant in aerospace and defense (Lockheed, Northrop, Raytheon, Boeing, SpaceX) — every CAD hour doubles as career prep. Free through UA. **Trade-off:** Windows-only; version control handled through GitHub commits of the source files.

### Decision 11: Two-tier layout on standoffs
**Decision:** Heavy components (motors, battery, driver) on the base plate; brain and sensors (Pi, IMU, camera) on a top deck raised 35mm on standoffs. **Why:** Keeps center of mass low, which aids stability and self-righting. Separates power wiring from signal wiring. 35mm clears the Pi, battery, and L298N below. **Trade-off:** Off-the-shelf standoff height locks the deck spacing.

### Decision 12: Edge-mounted forward-facing camera on a separate bracket
**Decision:** Pi camera mounts vertically at the front edge via a dedicated L-bracket, looking forward down the rover's length. **Why:** Forward-facing matches real rover camera placement and gives a clear driving view. A separate bracket lets the camera mount iterate without reprinting the deck. Bracket orientation matters — mounting across two side-by-side holes would face the camera sideways, so it uses a dedicated hole placement to face forward. **Trade-off:** Extra part to print and align; the mount design took several revisions to fit the real camera's hole pattern.

### Decision 13: Fillet at bracket load joints
**Decision:** 4mm fillet where bracket bases meet vertical walls (camera bracket, servo mount). **Why:** Sharp inside corners concentrate stress — an impact on the vertical face during a flip loads that joint. A fillet spreads the load and improves print layer bonding across the transition. **Trade-off:** Negligible extra material.

### Decision 14: Servo power separated from the Pi
**Decision:** MG996R servo powered from the battery (via breadboard rails), never from the Pi's 5V pins — only the signal wire and a common ground connect to the Pi. **Why:** The servo's ~2.5A stall current would brown out or damage the Pi. **Trade-off:** More wiring; requires a shared-ground discipline that, if missed, makes the servo jitter.

### Decision 15: lgpio backend for stable servo control
**Decision:** Drive the servo through gpiozero's lgpio pin factory rather than the default. **Why:** The default software PWM jittered; lgpio's hardware-timed signal holds steady. Combined with charged cells, this resolved a persistent servo buzz. **Trade-off:** A faint residual hold-buzz remains, accepted because the servo only holds briefly during a flip — it sweeps in motion, where the buzz is irrelevant.

### Decision 16: Phased build, three-wave parts ordering
**Decision:** Build in phases (self-righting demo first, driving later), order parts in waves (compute and tools, then drivetrain and sensors after the chassis was verified, then future-phase parts). **Why:** Prioritizing the self-righting demo produces the strongest single portfolio artifact fastest. Ordering after chassis verification caps the cost of a design error. **Trade-off:** Slower overall; a blocked subsystem can idle work.
