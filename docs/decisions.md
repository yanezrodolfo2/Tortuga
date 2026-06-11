[decisions.md](https://github.com/user-attachments/files/28832220/decisions.md)
# Engineering Decisions

This log captures every non-trivial design decision made during the Tortuga build, along with the reasoning and trade-offs accepted. It exists for two reasons:

1. **Future me** — to remember why I chose what I chose, six months from now
2. **Future reviewers** — to see how engineering judgment was applied, not just what was built

Trivial choices (filament color, exact hole tolerance values, fastener brand) are not logged. Architectural choices are.

---

### Decision 1: Raspberry Pi over Arduino as primary controller

**Decision:** Raspberry Pi 4 (4GB) for main control. **Why:** Camera streaming and image processing are roadmap items. Arduino can drive motors but cannot stream video or run higher-level autonomy code. The Pi handles both. A microcontroller may be added later for real-time motor control if latency becomes an issue. **Trade-off accepted:** Higher power draw, less deterministic timing.

### Decision 2: PETG over PLA for chassis and seal housings

**Decision:** PETG for all structural and sealing parts. **Why:** PLA glass-transition temperature is ~60°C. A car interior in Tucson summer routinely exceeds this. PETG (~75–80°C Tg) handles desert heat. ASA would be better but is harder to print reliably on the UA student printers. **Trade-off accepted:** PETG is harder to print cleanly than PLA; first prints may need tuning.

### Decision 3: Self-righting via deployable arm (not symmetric chassis)

**Decision:** Single servo-driven arm that pushes the rover back upright when inverted. **Why:** Symmetric (operate-either-side-up) chassis was considered but doubles the design constraints — every external sensor, the camera, and the wheels would need to work in either orientation. A deployable arm isolates the complexity to one mechanism. **Trade-off accepted:** Single point of failure. If the servo or linkage breaks, no recovery.

### Decision 4: Labyrinth seals over lip seals

**Decision:** *(Pending — to be finalized during detailed drivetrain CAD in Week 6-7.)* **Why:** Seal geometry depends on final motor shaft diameter, wheel hub design, and printer tolerance testing. Will resolve once Phase 1 drivetrain is built and dust exposure can be characterized empirically.

### Decision 5: Base plate dimensions and tortoise-shell outline

**Decision:** 215mm × 160mm × 4mm PETG base plate with asymmetric oval outline — 40mm radius front corners, 30mm radius rear corners. **Why:** Larger than initial 200×150mm estimate to accommodate righting arm mechanism, battery pack, and electronics with margin. Rounded outline reduces catch points during inversion events, improving self-righting reliability — a functional choice, not just aesthetic. Asymmetric front-rear shape provides visual orientation cue and supports project identity (Tortuga = tortoise in Spanish). 215mm length maintains 5mm margin on standard 220mm printer beds, avoiding edge-of-bed adhesion issues. Front of rover defined as the 40mm-radius edge. **Trade-off accepted:** Heavier than a minimum-size plate; will require larger righting arm servo to overcome the added moment arm.

### Decision 6: Motor and wheel selection — medium-mode off-road

**Decision:** 4× TT gear motors (3-6V, 1:48 reduction) paired with 80mm chunky-tread rubber off-road wheels. **Why:** TT motors are inexpensive (~$15 for 4) with adequate torque for hobby-scale off-road driving. 80mm wheels provide ~40mm ground clearance vs. ~25mm with standard 65mm wheels — meaningful improvement for Sonoran Desert terrain. Chunky rubber tread grips loose sand and dirt where smooth wheels would slip. Wheel hub fits TT motor D-shaft directly — no adapter required, fewer failure points. **Trade-off accepted:** No built-in encoders; closed-loop speed control not possible without adding magnetic encoders later (~$10 future upgrade). Lower top speed than 12V geared motors — acceptable for a scout-class rover where torque matters more than speed.

### Decision 7: Motor mounting pattern — 4-corner long-axis layout

**Decision:** Four motors mounted in the four corners of the base plate, with each motor's long axis parallel to the rover's length (215mm direction). Mounting holes spaced 37mm apart along the length axis. Motor shafts point outward perpendicular to the direction of travel. Front-left and rear-left motors are ~103mm apart center-to-center on each side; ~23mm clearance between front and rear wheels on each side. **Why:** Standard rover/automotive layout — direction of travel along the long axis, wheels on the long sides. Matches Mars rover (Curiosity, Perseverance) wheelbase convention. Maximizes traction with 4WD and minimizes turning radius for skid-steer. **Trade-off accepted:** Front and rear wheels are close together (~23mm gap) — restricts use of even larger wheels in future upgrades without lengthening the chassis.

### Decision 8: CAD software — SolidWorks over Fusion 360

**Decision:** SolidWorks selected as the primary CAD environment for this project. **Why:** SolidWorks is the dominant CAD tool in aerospace and defense engineering — Lockheed Martin, Northrop Grumman, Raytheon, Boeing, and SpaceX all use it heavily. Building fluency in SolidWorks during a portfolio project compounds career value: every CAD hour is also resume preparation. Hole Wizard, Mirror, and parametric design features make symmetric layouts faster than Fusion 360 equivalents. Free through the UA student license. **Trade-off accepted:** Windows-only — less flexible than Fusion 360's cross-platform support. Cloud collaboration is weaker; version control managed via GitHub commits of `.SLDPRT` files.

### Decision 9: Top deck dimensions and offset

**Decision:** 180mm × 130mm × 3mm PETG top deck, centered over the base plate with 17.5mm inset on each side along length and 15mm inset along width. Same tortoise outline as base plate. **Why:** Inset gives clearance for the righting arm mechanism to swing around the deck without collision, leaves room for wire bundles to route up from below, and produces a visually layered "deck on chassis" silhouette consistent with Mars rover conventions. 3mm thickness is structurally sufficient since the deck carries low load (Pi + IMU + camera ≈ 80g total). **Trade-off accepted:** Less mounting real estate than a full-sized deck — must lay out electronics carefully to fit.

### Decision 10: Standoff configuration

**Decision:** 6× M3 standoffs, 35mm height, in a 4-corner-plus-2-mid-edge pattern. **Why:** 4 corners provide primary structural support; 2 mid-edge standoffs prevent deck sag under the Pi's weight (located near deck center). 35mm height accommodates Pi (17mm tall with USB), battery pack (22mm tall), and L298N motor driver (~20mm tall) on the base plate below with 5mm wire clearance. Off-the-shelf metal standoffs chosen over 3D-printed pillars for strength and dimensional precision. **Trade-off accepted:** Off-the-shelf height locks deck spacing — cannot adjust without re-buying standoffs.

### Decision 11: Wire pass-through layout

**Decision:** 2× Ø10mm wire pass-through holes in the top deck, positioned over the centerline of the base plate between the front motor pair and between the rear motor pair. **Why:** Two passes instead of one keeps wire runs short and segregates front and rear motor wiring — easier to debug, less bundling. **Trade-off accepted:** Holes weaken the deck slightly in the center; mitigated by the 6-standoff support pattern.

### Decision 12: Edge-mounted camera

**Decision:** Pi Camera v2 will mount vertically at the front edge of the top deck via a separate L-bracket part, looking horizontally forward. **Why:** Edge-mounted orientation matches real rover/robot camera placement (Mars rovers, Boston Dynamics products) — looks deliberate, not improvised. Vertical mounting gives the camera a clear forward field of view unobstructed by the deck itself. Separate bracket part isolates the camera mount from the deck design — can be iterated independently without reprinting the deck. **Trade-off accepted:** Two parts to print/assemble instead of one. Slightly less rigid than a deck-integrated mount.
