---
title: "GND - Najaf Ground"
toc_min_heading_level: 2
toc_max_heading_level: 6
---

## Chapter 1. Position Overview
**Al-Najaf Ground (SMC)** is responsible for issuing IFR clearances and managing aircraft movement on the Al-Najaf aprons and taxiways. The SMC Controller will provide aircraft with pushback instructions when required, taxi departing aircraft to the applicable runway holding point, and taxi arriving aircraft to an appropriate stand or apron.

| **Position** | **Callsign**       | **Frequency** | **Logon Callsign** |
|--------------|--------------------|---------------|--------------------|
| Al-Najaf SMC | Al-Najaf Ground    | 121.700       | ORNI_GND           |
| Al-Najaf TWR | Al-Najaf Tower     | 119.100       | ORNI_TWR           |
| Al-Najaf ATIS|                    | 123.900       | ORNI_ATIS          |

---

<p align="center">
  <strong>1.1 - AREA OF RESPONSIBILITY</strong><br>
</p>

Al-Najaf **SMC** is responsible for aircraft movement on the apron and taxiways under Ground control. When Al-Najaf **TWR** is online, aircraft should be handed to Tower as early as practical once they are clear of ground conflicts and approaching the active runway holding point.

----

## Chapter 2. GEN | Standard Operating Procedures

### 2.1 IFR Clearance
IFR clearances are issued by Al-Najaf **SMC**, ensuring appropriate routing. All aircraft shall normally be assigned a **Standard Instrument Departure (SID)**.

Controllers shall assign the proper SID exit waypoint based on the first enroute waypoint in the aircraft's flight plan, and the proper procedure identifier based on the selected runway for departure. All SIDs with an identifier of **1A** and **1C** are valid for Runway **10**. SIDs with an identifier of **1B** are valid for Runway **28**.

| **SID** | **Runway 10** | **Runway 28** |
|---------|---------------|---------------|
| SIGBI   | 1A            | 1B            |
| ILMAP   | 1A            | 1B            |
| LAGLO   | 1A            | 1B            |
| NOLDO   | 1A, 1C        | 1B            |
| SEPTU   | 1A            | 1B            |

Departures should primarily adhere to the published SID routes. Radar vectors should be avoided whenever feasible. If radar vectors are assigned, a specific reason must be provided.

Example:

> **Pilot:** _**"Al-Najaf Ground, IAW123, request clearance to Dubai, with information Alpha."**_  
> **SMC Controller:** _**"IAW123, Al-Najaf Ground, cleared to Dubai, SEPT1A departure, flight planned route, squawk 4301."**_

#### 2.1.1 Published SID Initial Climb Altitudes
The initial climb clearance is stated on published SID charts and does not need to be read to the pilot by default. If the pilot asks for the initial climb altitude, the controller shall advise them of the following initial climb clearances:

| **SID** | **Runway** | **Initial Climb Clearance** |
|---------|------------|-----------------------------|
| SIGBI 1A | 10        | 6000ft                      |
| ILMAP 1B | 28        | 6000ft                      |
| LAGLO 1A | 10        | 10000ft                     |
| NOLDO 1A | 10        | 10000ft                     |
| SEPTU 1A | 10        | 10000ft                     |
| NOLDO 1C | 10        | 11000ft                     |
| ILMAP 1A | 10        | 14000ft                     |
| LAGLO 1B | 28        | 14000ft                     |
| NOLDO 1B | 28        | 14000ft                     |
| SEPTU 1B | 28        | 14000ft                     |
| SIGBI 1B | 28        | 14000ft                     |

#### 2.1.2 Omni-Directional Departures
Aircraft may be assigned an omni-directional departure if they are unable to fly a SID, such as aircraft that are not RNAV capable, or for departures to the southwest filing via **RUKAM** or **ALI DCT RUKAM**. Al-Najaf **SMC** is required to adjust phraseology for an omni-directional departure.

Example:

> **Pilot:** _**"Al-Najaf Ground, IAW123, request clearance to Dubai, unable SID, with information Alpha."**_  
> **SMC Controller:** _**"IAW123, Al-Najaf Ground, cleared to Dubai, expect radar vectors to ILMAP after departure, flight planned route, squawk 4301."**_

### 2.2 Pushback Clearance
The **SMC Controller** is responsible for providing departing aircraft with a pushback clearance when required. Pushback clearance must only be issued when it is safe to do so and the area into which the aircraft has been cleared to push is clear of all obstructions.

The **SMC Controller** should ensure aircraft do not push into conflict with taxiing traffic, aircraft under the control of Al-Najaf **TWR**, or aircraft taxiing on Taxiway **C**.

### 2.3 Taxi Procedures
All departing aircraft shall be assigned the most appropriate taxiway onto Taxiway **C**. Al-Najaf **SMC** must exercise extreme caution on Taxiway **C**, as conflicts can easily occur between arriving and departing traffic.

Example:

> **SMC Controller:** _**"IAW123, taxi to holding point runway 10 via C."**_

#### 2.3.1 Conditional Taxi Instructions
If the taxi route for an aircraft is not clear, a conditional taxi instruction may be issued to ensure the aircraft remains clear of any conflict.

Example:

> **SMC Controller:** _**"IAW123, taxi via C, hold short of D, give way to the company Airbus A320 on Taxiway C."**_

### 2.4 Runway Modes
Winds must always be considered for runway modes. Crosswind must be less than **20 knots** and tailwind must be less than **5 knots**. The preferred order of runway modes at Al-Najaf is listed below.

| **Priority - Mode** | **Arrivals** | **Departures** | **Remarks** |
|---------------------|--------------|----------------|-------------|
| 1 - MODE A          | 28           | 10             | Opposite direction operations |
| 2 - MODE B          | 10           | 28             | Opposite direction operations |
| 3 - MODE C          | 28           | 28             |             |
| 4 - MODE D          | 10           | 10             |             |

This preferential runway configuration applies opposite runway direction operations. This may not always be possible due to weather conditions, specifically when the tailwind component is greater than **5 knots**, or during high traffic volumes where opposite direction operations are unsuitable.

### 2.5 VFR Coordination
All VFR clearances are assigned by Al-Najaf **TWR**. VFR aircraft requesting clearance through Ground shall be coordinated with Tower before any clearance is issued, or instructed to expect clearance at the holding point if directed by Tower.

----

## Chapter 3. Coordination

### 3.1 Departure Procedures
Due to the airspace structure at Al-Najaf, all departures shall be coordinated and receive a release for departure with the relevant Baghdad **TMA** controller.

Next coordination is required to the following stations in the following scenarios:

| **Coordination Station** | **Departing Procedure** |
|--------------------------|-------------------------|
| ORBI_APP                 | All SIDs except ILMAP departures, and omni-directional departures expected to enter Baghdad TMA, mainly departures to the north |
| ORNI_APP/ORMM_APP        | ILMAP departures and all other omni-directional departures |

ORNI_APP/ORMM_APP must be notified of aircraft that are being released on an omni-directional departure to ORBI_APP.

Next coordination is additionally required for:

- Visual departures; and
- The next departure from that runway after a go-around.

The standard assignable level from Al-Najaf **TWR** to Baghdad **TMA** is:

| **Aircraft** | **Level** |
|--------------|-----------|
| IFR          | A080      |
| VFR          | A050      |

Next coordination is mandatory for **all** aircraft departing Al-Najaf.
