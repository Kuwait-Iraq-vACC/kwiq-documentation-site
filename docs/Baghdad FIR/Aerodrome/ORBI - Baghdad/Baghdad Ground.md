---
title: "Baghdad Ground"
toc_min_heading_level: 2
toc_max_heading_level: 6
---

### Amendment History

| **Revision** | **Effective Date** | **Notes**           |
|--------------|--------------------|---------------------|
| Version 1    | 20JUN26            | Initial Publication |
| Version 2    | 20JUN26            | Added DEL and VFR procedures |

----

## Chapter 1. Position Overview
**Baghdad Ground (SMC)** is responsible for validating routes, issuing IFR clearances, coordinating VFR clearances with Baghdad **TWR**, and managing aircraft movement on the Baghdad aprons and taxiways within its area of responsibility. The SMC Controller will provide aircraft with pushback and start instructions when required, taxi departing aircraft toward the applicable runway holding point, and taxi arriving aircraft from the runway exit area to an appropriate stand or apron.

| **Position** | **Callsign**       | **Frequency** | **Logon Callsign** |
|--------------|--------------------|---------------|--------------------|
| Baghdad SMC  | Baghdad Ground     | 121.400       | ORBI_GND           |
| Baghdad TWR  | Baghdad Tower      | 118.900       | ORBI_TWR           |
| Baghdad ATIS |                    | 126.925       | ORBI_ATIS          |

---

<p align="center">
  <strong>1.1 - AREA OF RESPONSIBILITY</strong><br>
</p>
![AOR.png](img/AOR.png)

When Baghdad **TWR** is online, the aprons and taxiways west of Runways 33L and 15R are under the jurisdiction of **TWR**. Baghdad **SMC** shall relinquish control of these areas accordingly.

Taxiway **W** is under the jurisdiction of Baghdad **TWR** when online. This is to facilitate arrivals on Runways 33R, 33L, 15R, and 15L.

#### 1.1.1 Coordination With Tower

Any departing aircraft requiring Taxiway **W** must be coordinated by Baghdad **SMC** with Baghdad **TWR** before taxi instructions are issued.

Example:

> **SMC Controller:** _**"Request to taxi IAW23 on Whiskey, 33R."**_  
> **TWR Controller:** _**"Taxi IAW23 on Whiskey."**_

----

## Chapter 2. GEN | Standard Operating Procedures

### 2.1 IFR Clearance

IFR clearances are issued by Baghdad **SMC**, or by ACD when available. Baghdad **SMC** is responsible for validating the filed route, level, and departure details before issuing a clearance. Where the flight plan contains an invalid route, level, or departure procedure, Baghdad **SMC** shall ensure that the error is corrected before the aircraft is cleared.

Baghdad does not use SIDs, therefore aircraft receive departure instructions from **TWR** during line-up or take-off clearance. Baghdad **SMC** does not need to provide radar departure instructions as part of the IFR clearance.

Pilots may be expected to report the following information on first contact:

- Aircraft callsign
- Aircraft type
- Parking stand
- Destination
- ATIS letter and QNH.

The clearance issued by Baghdad **SMC** shall include:

- Destination
- Route clearance
- Departure runway
- Assigned squawk code.

If the pilot does not report the current ATIS letter on first contact, Baghdad **SMC** shall pass the current ATIS letter and QNH. A full readback of the clearance shall be obtained.

Example:

> **Pilot:** _**"Baghdad Ground, IAW123, request IFR clearance to Dubai, with information A."**_  
> **SMC Controller:** _**"IAW123, Baghdad Ground, cleared to Dubai, flight planned route, runway 33R, squawk 7403."**_  
> **Pilot:** _**"Cleared to Dubai, flight planned route, runway 33R, squawk 7403, IAW123."**_  
> **SMC Controller:** _**"IAW123, readback correct, report ready for push and start."**_

#### 2.1.1 Aircraft Requiring a Reroute

If an aircraft requires a reroute, the aircraft shall be informed as soon as practical after connecting to the network, either by private message or on frequency. Baghdad **SMC** shall issue a reroute if the pilot's route does not comply with the standard Baghdad routes.

Example:

> **SMC Controller:** _**"IAW123, cleared to Dubai, NOLDO, P975, SESRU, flight planned route, runway 33R, squawk 0553."**_

| **Direction** | **Routing**                                      |
|---------------|--------------------------------------------------|
| North         | BGD DCT NAMDI M860 NINVA                         |
| North         | BGD DCT TAGRU L718 KABAN                         |
| East          | BGD DCT NOLDO B411 PAXAT                         |
| South         | BGD DCT NOLDO P975 SIDAD                         |
| Southwest     | BGD DCT DELMI DCT RUKAM B411 MURIB               |
| West          | BGD DCT DELMI G202 MODIK                         |
| West          | BGD DCT DELMI G202 RAPLU R652 GIBUX L200 PASIP   |

If an aircraft files an invalid cruise level, Baghdad **SMC** shall advise the aircraft when delivering the clearance. In all cases, the next lowest valid cruise level should be assigned and the aircraft advised.

#### 2.1.2 Runway Change Procedure

Any runway change shall be coordinated with Baghdad **TWR** before being issued to departing aircraft.

### 2.2 Pushback and Start

Once the IFR clearance has been issued and the readback is correct, the aircraft should be instructed to report ready for push and start. Pushback and start instructions must only be issued when the movement area behind the aircraft is clear and the aircraft can safely enter the intended taxi route.

The **SMC Controller** should ensure that aircraft are not pushed into conflict with taxiing traffic, aircraft under the control of **TWR**, or any aircraft using Taxiway **W**.

### 2.3 Taxi Procedures

All departing aircraft shall normally be assigned Taxiway **Y**. Taxiway **W** falls under the jurisdiction of Baghdad **TWR** when online, therefore departing aircraft requiring Taxiway **W** must be coordinated with **TWR** before taxi is issued.

Example:

> **Pilot:** _**"Request taxi."**_  
> **SMC Controller:** _**"IAW123, taxi via Y, hold short S."**_

#### 2.3.1 Taxiway W Operations

Taxiway **W** is primarily protected for arrival flow and must not be used for departures unless Baghdad **TWR** has approved the movement. Baghdad **SMC** shall request approval from **TWR** before instructing aircraft to taxi on Taxiway **W**.

Example:

> **SMC Controller:** _**"Request to taxi IAW23 on Whiskey, 33R."**_  
> **TWR Controller:** _**"Taxi IAW23 on Whiskey."**_

### 2.4 Runway Modes

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

#### 2.4.1 Departure Runway Awareness

Baghdad **SMC** shall ensure taxi instructions match the active runway mode and that aircraft are routed toward the correct departure runway. Aircraft requiring a runway or taxiway that differs from the active plan should be coordinated with Baghdad **TWR** before taxi is issued.

### 2.5 Ground Movement Responsibilities

Baghdad **SMC** is responsible for maintaining an orderly flow of aircraft on the aprons and taxiways under its jurisdiction. Aircraft should be handed to Baghdad **TWR** as early as practical once they are clear of any ground conflict and approaching the runway holding point or any area under **TWR** control.

Arriving aircraft transferred from Baghdad **TWR** shall be taxied from the runway exit area to their assigned apron or stand while remaining clear of departing aircraft and any areas retained by **TWR**.

### 2.6 VFR Procedures

VFR aircraft must be coordinated with Baghdad **TWR** before receiving a clearance. Baghdad **TWR** may instruct Baghdad **SMC** to issue the VFR clearance, or may instruct Baghdad **SMC** to advise the aircraft to expect clearance at the holding point.

All VFR departures shall be assigned a discrete SSR code so that they may be identified on radar.

#### 2.6.1 VFR Departures Into Uncontrolled Airspace

VFR traffic departing into uncontrolled airspace shall be cleared via the most appropriate VFR route toward their destination. If necessary, the clearance may be amended by Baghdad **TWR** prior to departure.

#### 2.6.2 VFR Departures Into Controlled Airspace

VFR aircraft requesting clearance to climb into approach airspace shall only be cleared after prior coordination with the relevant approach or departure controller. Otherwise, the aircraft shall be instructed to remain outside controlled airspace after leaving the control zone.

Example:

> **Pilot:** _**"Baghdad Ground, A6-CTK, SR22, request eastbound departure, altitude 6500ft."**_  
> **SMC Controller:** _**"A6-CTK, Baghdad Ground, cleared eastbound departure, altitude 6500ft VFR, runway 33R, squawk 0611."**_  
> **Pilot:** _**"Cleared eastbound departure, altitude 6500ft VFR, runway 33R, squawk 0611, A6-CTK."**_  
> **SMC Controller:** _**"A6-CTK, readback correct, information A, QNH 1003, report ready for start-up."**_

#### 2.6.3 VFR Circuit Traffic

VFR traffic wishing to remain in the circuit shall be cleared only after prior coordination with Baghdad **TWR** and the relevant approach or departure controller. All VFR circuit traffic shall be assigned a discrete SSR code so that they may be identified on radar.

VFR circuits at Baghdad are only permitted on Runways **33L** and **15R**. Circuit traffic shall normally be assigned **1,000ft** and the following circuit directions:

| **Runway** | **Direction** |
|------------|---------------|
| 33L        | Left          |
| 15R        | Right         |

VFR circuits shall not be permitted during periods of increased IFR departure or arrival activity.

#### 2.6.4 VFR Aircraft Leaving the CTR

VFR aircraft requesting to leave the Baghdad CTR shall be coordinated with Baghdad **TWR**. Aircraft requesting to exit the CTR shall be assigned a clearance limit followed by a valid VFR cruising altitude.

| **Fix Name** | **Description**              |
|--------------|------------------------------|
| Tusk         | Building with blue windows   |
| Warthog      | Large farm compound          |
| Dakota       | -                            |
| Austin       | -                            |

----

## Chapter 3. Coordination

### 3.1 Departures

Due to the airspace structure at Baghdad, all departures shall be coordinated with the relevant Baghdad **TMA** controller before release.

Next coordination is **not** required to Baghdad **TMA** for aircraft that are:

- Departing from a runway nominated on the ATIS;
- Assigned the standard assignable level; and
- Assigned a procedural SID; or
- Assigned a standard assignable heading.

Next coordination is required for:

- Visual departures;
- All departures not on a standard assignable heading; and
- The next departure from that runway after a go-around.

#### 3.1.1 Standard Assignable Levels

| **Aircraft** | **Level** |
|--------------|-----------|
| IFR          | A060      |
| VFR          | A030      |

### 3.2 Standard Assignable Departure Headings

As there are no SIDs at Baghdad, aircraft must receive an assigned heading with their line-up or take-off clearance. This is issued by Baghdad **TWR**, however Baghdad **SMC** should remain aware of the standard assignable headings when sequencing and taxiing aircraft for departure.

| **Runway** | **Heading** |
|------------|-------------|
| 33R        | H325, H250  |
| 33L        | H325, H250  |
| 15R        | H145        |
| 15L        | H145        |

Where multiple standard assignable headings are available, the heading most suitable for the aircraft's direction of flight should be assigned by **TWR**.

#### 3.2.1 Aircraft Turn Altitudes

| **Runway** | **Altitude** |
|------------|--------------|
| 33R        | A012         |
| 33L        | A010         |
| 15R        | A007         |
| 15L        | A006         |

### 3.3 Baghdad Flow

The Baghdad **FMP** position shall only be activated during major events or when authorized by the ATS department. This position is in charge of sequencing aircraft for push and ensuring that all departures push on time.

During events, Baghdad **FMP** shall be in charge of:

- Ensuring event traffic pushes and departs on time according to event ETOT;
- Ensuring non-event traffic is coordinated and provided with a proper departure slot;
- Assisting Baghdad **TWR** with checking and validating flight plans; and
- Assisting Baghdad **SMC** with pushback time slots.

The responsibilities of Baghdad **FMP** may be delegated to Baghdad **TWR** when **SMC** workload is high but no separate **FMP** controller is available.
