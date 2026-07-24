# Engineering Decisions

Design decisions made during the Tortuga build, with reasoning and trade-offs. Trivial choices (filament color, fastener brand) are not logged. Architectural choices are.

---

### Decision 1: Raspberry Pi over Arduino as primary controller

**Decision:** Raspberry Pi 4 (4GB) for main control. **Why:** Camera streaming and image processing are roadmap items. Arduino can drive motors but cannot stream video or run higher-level autonomy code. The Pi handles both. A microcontroller may be added later for real-time motor control if latency becomes an issue. **Trade-off accepted:** Higher power draw, less deterministic timing.

### Decision 2: PETG for final parts, PLA for prototypes

**Decision:** PETG for all structural and sealing parts in the final build; PLA for fit-check prototypes. **Why:** PLA glass-transition temperature is ~60°C — a car interior in Tucson summer routinely exceeds this. PETG (~75-80°C Tg) handles desert heat. PLA is cheaper, faster, and dimensionally more accurate, making it the right choice for parts that only need to verify fit and will never leave the desk. **Trade-off accepted:** Two print runs instead of one. Justified by catching design errors on cheap parts.

### Decision 3: Self-righting via deployable arm, not symmetric chassis

**Decision:** Single servo-driven arm that pushes the rover back upright when inverted. **Why:** A symmetric operate-either-side-up chassis was considered but doubles the design constraints — every external sensor, the camera, and the wheels would need to function in either orientation. A deployable arm isolates the complexity to one mechanism. **Trade-off accepted:** Single point of failure. If the servo or linkage breaks, no recovery.

### Decision 4: Labyrinth seals over lip seals

**Decision:** *Pending — to be finalized during detailed drivetrain CAD.* **Why:** Seal geometry depends on final motor shaft diameter, wheel hub design, and printer tolerance testing. Will resolve once the Phase 1 drivetrain is built and dust exposure can be characterized empirically.

### Decision 5: Chassis dimensions and outline

**Decision:** 215 x 160 x 4 mm base plate, 180 x 130 x 3 mm top deck, uniform 40 mm corner fillets on both. **Why:** Rounded outline reduces catch points during inversion events, improving self-righting reliability. 215 mm length maintains margin on a 240 mm printer bed. Deck is inset 17.5 mm in X and 15 mm in Z, leaving clearance for the righting arm to swing and for wire bundles to route up from below. Front/rear orientation is defined by hole pattern — camera bracket mounts at X=20, servo mount at X=125 — rather than by external geometry. **Trade-off accepted:** No visual orientation cue from the shape; the deck must be marked to avoid assembly confusion.

### Decision 6: Motor and wheel selection

**Decision:** 4x TT gear motors (3-6V, 1:48 reduction) with 80 mm chunky-tread rubber off-road wheels. **Why:** TT motors are inexpensive (~$15 for 4) with adequate torque for hobby-scale off-road driving. 80 mm wheels give ~40 mm ground clearance versus ~25 mm with standard 65 mm wheels — meaningful for Sonoran Desert terrain. Wheel hub fits the TT D-shaft directly, eliminating an adapter and a failure point. **Trade-off accepted:** No built-in encoders, so closed-loop speed control is not possible without a later magnetic encoder upgrade (~$10). Lower top speed than 12V motors, acceptable for a scout-class rover where torque matters more.

### Decision 7: Motor mounting pattern — 4-corner long-axis layout

**Decision:** Four motors in the four corners of the base plate, each motor's long axis parallel to the rover's 215 mm length. Mounting holes 37 mm apart along the length axis; shafts point outward perpendicular to travel. Front and rear motors on each side are ~103 mm apart center-to-center, giving ~23 mm clearance between wheels. **Why:** Standard rover/automotive layout — travel along the long axis, wheels on the long sides. Matches Mars rover wheelbase convention. Maximizes traction with 4WD and minimizes turning radius for skid-steer. **Trade-off accepted:** Wheel-to-wheel clearance is tight, restricting future upgrades to larger wheels without lengthening the chassis.

### Decision 8: SolidWorks over Fusion 360

**Decision:** SolidWorks as the primary CAD environment. **Why:** SolidWorks dominates aerospace and defense engineering — Lockheed Martin, Northrop Grumman, Raytheon, Boeing, and SpaceX all use it heavily. Building fluency during a portfolio project compounds career value: every CAD hour doubles as interview preparation. Free through the UA student license. **Trade-off accepted:** Windows-only. Weaker cloud collaboration than Fusion; version control handled through GitHub commits of `.SLDPRT` files.

### Decision 9: Standoff configuration

**Decision:** 6x M3 standoffs at 35 mm height, in a 4-corner-plus-2-mid-edge pattern. Base plate holes at X = 37.5 / 107.5 / 177.5, Z = 55 / 105. Deck holes at X = 20 / 90 / 160, Z = 40 / 90. **Why:** Four corners provide primary support; two mid-edge posts prevent deck sag under the Pi's weight. 35 mm accommodates the Pi (17 mm), battery pack (22 mm), and L298N (~20 mm) on the base plate with wire clearance. Off-the-shelf metal standoffs chosen over printed pillars for strength and dimensional precision. **Trade-off accepted:** Off-the-shelf height locks the deck spacing — changing it means re-buying hardware.

### Decision 10: Standoff hole coordinate correction (deck v4 to v5)

**Decision:** Deck standoff holes moved from Z = 20 / 110 to Z = 40 / 90. **Why:** The original coordinates gave a 90 mm Z-span while the base plate span was 50 mm, so the plates could not stack. Caught by measuring both printed parts with the CAD Measure tool rather than by visual inspection — the mismatch was not obvious by eye. **Trade-off accepted:** One wasted prototype print of the deck. Cheap lesson: verify mating dimensions numerically across parts before printing, not after.

### Decision 11: Wire pass-through layout

**Decision:** 2x diameter-10 mm pass-through holes in the top deck at X = 45 and X = 135, both on the centerline. **Why:** Two passes rather than one keeps wire runs short and separates front and rear motor wiring, making debugging easier and reducing bundling. **Trade-off accepted:** Holes weaken the deck slightly at center; mitigated by the standoff support pattern.

### Decision 12: Edge-mounted camera on a separate bracket

**Decision:** Pi Camera v2 mounts vertically at the front edge of the top deck via a separate L-bracket, looking horizontally forward. **Why:** Edge-mounting matches real rover and field-robot camera placement — it reads as deliberate rather than improvised — and gives an unobstructed forward field of view. A separate part isolates camera-mount iteration from the deck, so the bracket can be revised without reprinting a large plate. **Trade-off accepted:** Two parts to print and assemble instead of one; slightly less rigid than an integrated mount.

### Decision 13: Camera bracket geometry

**Decision:** L-bracket with a 73 x 30 x 3 mm horizontal base and a 30 x 30 x 3 mm vertical face, joined by a 4 mm fillet. Base has 2x diameter-3.2 mm bolt holes 50 mm apart, matching deck standoff holes S1 and S4. Vertical face carries 4x diameter-2.2 mm camera holes and a diameter-10 mm lens aperture. **Why:** The 50 mm bolt spacing follows directly from the corrected deck geometry. Base length of 73 mm leaves 10 mm of material past each hole — 60 mm would leave only ~3.4 mm, which cracks in printed plastic. The fillet relieves stress at the joint, which carries impact load if the rover lands nose-first during a flip, and improves layer bonding across the transition. **Trade-off accepted:** Camera hole pattern is based on published Pi Camera v2 specs rather than direct measurement; holes are diameter-2 mm in plastic and can be re-drilled by hand if the pattern is off.

### Decision 14: Righting arm geometry

**Decision:** Straight bar, 120 x 20 x 4 mm, with semicircular caps at both ends. Pivot end has a central clearance hole for the servo horn hub plus 4 screw holes matching the stock MG996R horn. **Why:** Arm length set at approximately 0.7x the rover's short-axis dimension (160 mm x 0.7 = 112 mm) with margin. Estimated torque requirement ~9.6 kg-cm at worst case, within the MG996R's ~11 kg-cm rating at 6V. A straight bar minimizes CAD and print complexity for a first iteration. Horn fit verified against the physical servo horn — the arm seats flat with all four screws engaged. **Trade-off accepted:** No mechanical advantage from curved geometry; performance depends entirely on servo torque. Upgrade path to a curved or forked arm exists if testing shows insufficient authority.

### Decision 15: Servo mount

**Decision:** L-bracket bolted to the top deck at X = 125, Z = 50 / 80. Base flange 50 x 60 x 3 mm with 2x diameter-3.2 mm bolt holes 30 mm apart; vertical wall carries 4x holes matching the MG996R flange pattern and a central cutout for the servo body to pass through. 4 mm fillet at the joint. **Why:** A bracket isolates the servo from the deck, allowing it to be swapped or upgraded without reprinting a large part. Vertical mounting orients the shaft parallel to the rover's width axis so the arm sweeps in the flip plane. Rear placement keeps the electronics area clear and puts the arm's mass behind the center of mass, aiding flip dynamics. The body cutout is required — without it the servo flanges cannot seat flush against the wall. **Trade-off accepted:** Mount position at X = 125 was chosen to clear standoff holes at X = 160; the servo sits slightly inboard of the rear edge, marginally reducing the arm's reach.

### Decision 16: Power architecture

**Decision:** 2-cell 18650 pack (7.4V nominal) supplying motors through the L298N and the servo through a dedicated rail. The Pi runs on its own regulated supply. All grounds tied common. **Why:** A 3-cell pack (11.1V) exceeds the TT motors' 3-6V rating even after the L298N's ~2V internal drop; 2 cells land motors in-spec. The MG996R draws up to ~2.5A at stall, far beyond what the Pi's 5V rail can source — powering it from the Pi would brown out or damage the board, so the servo takes battery-side power with only its signal wire on GPIO. Common ground is required for signal reference across all three subsystems. **Trade-off accepted:** Reduced battery capacity versus a 3-cell pack. An LM2596 buck converter is planned to allow the 3-cell pack with a regulated 6V motor rail in a later revision.

### Decision 17: Flip detection threshold

**Decision:** Rover orientation determined from MPU-6050 Z-axis acceleration with a plus/minus 5 m/s-squared dead band — above +5 is upright, below -5 is inverted, between is indeterminate. **Why:** Testing against zero would cause rapid state oscillation at steep angles, repeatedly triggering the righting mechanism. The dead band requires a decisive orientation change before a state transition. Measured Z reads ~10-11 m/s-squared when flat, above the nominal 9.81 due to sensor offset, which does not affect sign-based detection. **Trade-off accepted:** The rover cannot distinguish "on its side" from "mid-transition" — both fall in the dead band and are handled as indeterminate.
