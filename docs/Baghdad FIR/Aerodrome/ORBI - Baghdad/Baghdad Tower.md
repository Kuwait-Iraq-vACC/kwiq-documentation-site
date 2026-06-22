---
title: "TWR - Baghdad Tower"
---

## Chapter 1. Position Overview
**Baghdad Tower (TWR)** controls aircraft on the active runway, aircraft holding at runway holding points, and aircraft operating within the Baghdad Control Zone. The **TWR Controller** is responsible for selecting the active runway mode, issuing line-up, take-off, landing, and go-around instructions, and ensuring traffic information is passed between IFR and VFR aircraft within the Baghdad CTR.

The **TWR Controller** also has responsibility for the aprons and taxiways west of Runways **33L** and **15R** when Baghdad **TWR** is online. Baghdad **SMC** shall relinquish control of these areas accordingly.

| **Position** | **Callsign**       | **Frequency** | **Logon Callsign** |
|--------------|--------------------|---------------|--------------------|
| Baghdad TWR  | Baghdad Tower      | 118.900       | ORBI_TWR           |
| Baghdad SMC  | Baghdad Ground     | 121.400       | ORBI_GND           |
| Baghdad ATIS |                    | 126.925       | ORBI_ATIS          |

----

## Chapter 2. Airspace
The Baghdad Control Zone is **Class D Airspace**. Baghdad **TWR** is responsible for the West Baghdad CTR from the surface to **A030**, and the East Baghdad CTR from **A010** to **A030**.

| **Airspace Type** | **Airspace**      | **Class** | **Vertical Limits** | **Controller** |
|-------------------|-------------------|-----------|---------------------|----------------|
| Control Zone      | Baghdad CTR WEST  | D         | SFC - 3000ft        | ORBI_TWR       |
| Control Zone      | Baghdad CTR EAST  | D         | 1000ft - 3000ft     | ORBI_TWR       |

---

![Baghdad CTR](img/Baghdad structure.png)

---

## Chapter 3. GEN | Standard Operating Procedures

### 3.1 Runway Selection
Winds must always be considered when selecting the runway mode. Crosswind must be less than **20 knots** and tailwind must be less than **5 knots**. The preferred order of runway modes at Baghdad is listed below.

| **Priority - Mode** | **Arrivals** | **Departures** | **Remarks** |
|---------------------|--------------|----------------|-------------|
| 1 - MODE A          | 33R          | 33R            | VFR 33L     |
| 2 - MODE B          | 33R          | 33R            |             |
| 3 - MODE C          | 15L          | 15L            | VFR 15R     |
| 4 - MODE D          | 15L          | 15R, 15L       |             |
| 5 - MODE E          | 33R, 33L     | 33R, 33L       |             |
| 6 - MODE F          | 15R, 15L     | 15R, 15L       |             |

During Modes **A** and **C**, Runways **33L** and **15R** shall only be assigned to VFR and military traffic. During Modes **B**, **D**, **E**, and **F**, Runways **33L** and **15R** may be assigned to any flight or aircraft type. Runways **33R** and **15L** may also be used for VFR and military traffic if requested by the pilot during Modes **B**, **D**, **E**, and **F**.

#### 3.1.1 Runway Change
If the **TWR Controller** deems it necessary to change the active runway mode due to wind, traffic flow, or operational requirement, this must be coordinated with Baghdad **SMC** and the relevant Baghdad **TMA** controller. Any runway change affecting aircraft already cleared or taxiing for departure shall be coordinated before new instructions are issued.

#### 3.1.2 Runway Information
Baghdad International Airport has two published runway pairs: **15L/33R** and **15R/33L**.

| **Runway** | **Dimensions** | **True Bearing** | **Elevation** |
|------------|----------------|------------------|---------------|
| 33L        | 3301M x 45M    | 326              | 111ft         |
| 15R        | 3301M x 45M    | 146              | 114ft         |
| 33R        | 4000M x 60M    | 326              | 110ft         |
| 15L        | 4000M x 60M    | 146              | 113ft         |

### 3.2 Line Up Procedures
The **TWR Controller** must issue clear and precise instructions when instructing aircraft to line up on the active runway. Line-up instructions should include the runway designator, holding point or runway entry point when required, and relevant traffic information.

Example:

> **TWR Controller:** _**"IAW23, via S, line up and wait runway 33R."**_

#### 3.2.1 Conditional Line Up Clearance
Conditional line-up clearances may be issued when required to maximise runway efficiency. The condition must be clear, unambiguous, and include the word **behind** at the beginning and end of the instruction.

Example:

> **TWR Controller:** _**"IAW23, behind the landing Iraqi Airways Boeing 737, via S, line up and wait runway 33R, behind."**_

### 3.3 Take Off Procedures

#### 3.3.1 Departure Instructions
Baghdad does not use SIDs. Aircraft shall receive departure instructions from Baghdad **TWR** with the line-up or take-off clearance. These instructions shall include the initial climb, assigned heading, and the appropriate turn altitude.

The standard assignable level from Baghdad **TWR** to Baghdad **TMA** is:

| **Aircraft** | **Level** |
|--------------|-----------|
| IFR          | A060      |
| VFR          | A030      |

The following standard assignable departure headings may be issued without next coordination when the aircraft is departing from a runway nominated on the ATIS and is assigned the standard assignable level.

| **Runway** | **Heading** |
|------------|-------------|
| 33R        | H325, H250  |
| 33L        | H325, H250  |
| 15R        | H145        |
| 15L        | H145        |

Where multiple standard assignable headings are available, assign the heading most suitable for the aircraft's direction of flight. If strong winds are present at altitude, Baghdad **TWR** and Baghdad **TMA** should discuss slight changes to these headings to compensate for large crosswind components.

#### 3.3.2 Aircraft Turn Altitudes

| **Runway** | **Altitude** |
|------------|--------------|
| 33R        | A012         |
| 33L        | A010         |
| 15R        | A007         |
| 15L        | A006         |

#### 3.3.3 Take Off Clearances
Aircraft should only be given take-off clearance once the runway is clear of obstructions and required separation from any preceding departure or arrival has been achieved.

Example:

> **Pilot:** _**"Baghdad Tower, IAW23 ready for departure."**_  
> **TWR Controller:** _**"IAW23, after departure climb to altitude 6000ft, passing 1200ft turn left heading 250. Surface winds variable at 3 knots, runway 33R cleared for take-off."**_

#### 3.3.4 Handing Off
Departing aircraft shall be transferred to the relevant Baghdad **TMA** controller once safely airborne and clear of immediate Tower responsibility.

Example:

> **TWR Controller:** _**"IAW23, contact Baghdad Approach 124.800."**_

#### 3.3.5 Stopping a Departure
If a departure must be stopped after take-off clearance has been issued, the instruction must be issued immediately and clearly.

Example:

> **TWR Controller:** _**"IAW23, stop immediately, I say again, stop immediately, runway incursion."**_

For an aircraft that has not yet begun the take-off roll, cancel take-off clearance and instruct the aircraft to hold position.

Example:

> **TWR Controller:** _**"IAW23, hold position, cancel take-off, I say again, cancel take-off due runway incursion."**_

### 3.4 Arrival Procedures
The **TWR Controller** is responsible for issuing landing clearances and ensuring the runway is clear before an aircraft lands. Arriving aircraft shall be sequenced with due regard to runway occupancy and any departures awaiting release.

#### 3.4.1 Landing Clearance

Example:

> **TWR Controller:** _**"IAW1017, surface winds 320 degrees 5 knots, runway 33R, cleared to land."**_

#### 3.4.2 Late Landing Clearance
When required due to departing traffic or traffic vacating ahead, the **TWR Controller** may advise the aircraft to expect a late landing clearance. Landing clearance must be issued only when the runway is clear and safe for landing.

Example:

> **TWR Controller:** _**"IAW1017, expect late landing clearance, one to vacate ahead."**_

#### 3.4.3 Vacating Traffic
Taxiway **W** is under the jurisdiction of Baghdad **TWR** when online. This is to facilitate arrivals on Runways **33R**, **33L**, **15R**, and **15L**. Arriving aircraft vacating onto Taxiway **W** should remain with Baghdad **TWR** until they can be safely transferred to Baghdad **SMC**.

Baghdad **TWR** should avoid transferring aircraft in a way that causes them to stop and block the runway exit or Taxiway **W**.

Example:

> **TWR Controller:** _**"IAW1017, continue taxi via W, contact Baghdad Ground 121.400."**_

#### 3.4.4 Go Around Procedures
The **TWR Controller** shall issue go-around instructions if the runway is obstructed, landing clearance cannot be safely issued, or separation is lost on final approach.

Example:

> **TWR Controller:** _**"IAW1017, go around, I say again, go around, acknowledge."**_

After the go-around is acknowledged, Baghdad **TWR** shall issue the appropriate missed approach or coordination instructions and notify the relevant Baghdad **TMA** controller as soon as practical.

### 3.5 VFR Procedures
All VFR clearances are assigned by Baghdad **TWR**. VFR aircraft operating inside the Baghdad CTR must remain at or below **A030** unless otherwise coordinated. VFR departures shall be assigned a discrete SSR code.

Traffic information should be provided between IFR and VFR flights, and VFR aircraft shall be sequenced with due consideration to IFR arrival and departure traffic.

#### 3.5.1 VFR Traffic Remaining in Circuit
VFR circuits are only permitted on Runways **33L** and **15R**. Aircraft wishing to remain in the circuit shall normally be issued **1,000ft** and the following circuit directions:

| **Runway** | **Circuit Direction** |
|------------|-----------------------|
| 33L        | Left-Hand             |
| 15R        | Right-Hand            |

VFR circuits shall not be permitted during periods of increased IFR departure or arrival activity.

#### 3.5.1.1 VFR Circuit Phraseology

> **Pilot:** _**"Baghdad Tower, ABC holding short P2 runway 33L."**_  
> **TWR Controller:** _**"ABC, Baghdad Tower, cleared to operate in the circuit area not above altitude 3000ft, left hand circuits, report downwind, surface winds 320 degrees 5 knots, cleared for take-off runway 33L."**_  
> **Pilot:** _**"Cleared to operate in the circuit area not above altitude 3000ft, will report downwind, cleared for take-off runway 33L, ABC."**_

#### 3.5.2 Zone Exit Clearances
VFR aircraft requesting to leave the Baghdad CTR shall be assigned a clearance limit followed by a valid VFR cruising altitude. Once the aircraft begins the crosswind turn, the aircraft shall be instructed to report leaving the Baghdad CTR.

Example:

> **Pilot:** _**"Baghdad Tower, YYC is requesting to exit the Baghdad CTR via direct Al Najaf, altitude 3500ft."**_  
> **TWR Controller:** _**"YYC, Baghdad Tower, cleared to leave the Baghdad CTR direct Al Najaf, maintain altitude 3500ft, squawk 7403, QNH 998 hectopascals."**_  
> **Pilot:** _**"Cleared to leave the Baghdad CTR direct Al Najaf, maintain altitude 3500ft, QNH 998, squawk 7403, YYC."**_

Once airborne:

> **TWR Controller:** _**"FYI, report leaving the Baghdad CTR, maintain altitude 3000ft."**_

#### 3.5.2.1 Visual Reporting Points
VFR helicopter traffic requesting to leave the CTR may be cleared to leave via the visual reporting points below:

| **Fix Name** | **Description**              |
|--------------|------------------------------|
| Tusk         | Building with blue windows   |
| Warthog      | Large farm compound          |
| Dakota       | -                            |
| Austin       | -                            |

#### 3.5.3 Inbound VFR Traffic
Inbound VFR aircraft shall be sent to Baghdad **TWR** with enough time for two-way radio communications to be established before the aircraft receives clearance to enter the Baghdad CTR.

On initial contact, Baghdad **TWR** shall pass instructions for joining the circuit and any relevant traffic information. During periods of heavy IFR arrival activity, VFR arrivals may be denied entry into the CTR and instructed to hold outside the CTR awaiting further instructions.

Example:

> **Pilot:** _**"Baghdad Tower, YYC is requesting to enter the Baghdad CTR from the west for circuits."**_  
> **TWR Controller:** _**"YYC, Baghdad Tower, information A, cleared to enter the Baghdad CTR, maintain at or below altitude 3000ft, report left downwind runway 33L with intentions, squawk 7403."**_  
> **Pilot:** _**"Information A, cleared to enter the Baghdad CTR, at or below altitude 3000ft, will report left downwind runway 33L with intentions, squawk 7403, YYC."**_  
> **TWR Controller:** _**"YYC, correct, QNH 998 hectopascals."**_

----

## Chapter 4. Coordination

### 4.1 Departure Release
Due to the airspace structure at Baghdad, all departures shall be coordinated with the relevant Baghdad **TMA** controller before release.

Next coordination is **not** required to Baghdad **TMA** for aircraft that are:

- Departing from a runway nominated on the ATIS
- Assigned the standard assignable level and
- Assigned a procedural SID or
- Assigned a standard assignable heading.

Next coordination is required for:

- Visual departures
- All departures not on a standard assignable heading and
- The next departure from that runway after a go-around.

### 4.2 Between TWR and SMC
Taxiway **W** is under the jurisdiction of Baghdad **TWR** when online. Any departing aircraft requiring Taxiway **W** must be coordinated by Baghdad **SMC** with Baghdad **TWR** before taxi is approved.

Example:

> **SMC Controller:** _**"Request to taxi IAW23 on Whiskey, 33R."**_  
> **TWR Controller:** _**"Taxi IAW23 on Whiskey."**_

### 4.3 Baghdad Flow
The Baghdad **FMP** position shall only be activated during major events or when authorized by the ATS department. During events, Baghdad **FMP** may assist Baghdad **TWR** with checking and validating flight plans, sequencing aircraft for push, and ensuring event traffic departs according to event ETOT.

The responsibilities of Baghdad **FMP** may be delegated to Baghdad **TWR** when Baghdad **SMC** workload is high but no separate **FMP** controller is available.
