---
title: "DEL - Kuwait Delivery"
toc_min_heading_level: 2
toc_max_heading_level: 6
---

### Amendment History

| **Revision** | **Effective Date** | **Notes**           |
|--------------|--------------------|---------------------|
| Version 1    | 13AUG25            | Initial Publication |
| Version 2    | 30OCT25            | Revision #1         |

----

## Chapter 1. Position Overview 
**Kuwait Delivery (DEL)** provides aircraft with a full departure clearance and is responsible for passing the local QNH as well as verifying the aircraft type of the departing aircraft. DEL Controller should ensure the flight plan filed by the pilot is correct and that the departure list is updated to indicate the correct assigned Standard Instrument Departure procedure, temporary altitude and assigned squawk code. 

Once clearance has been issued and readback correctly from the pilot the DEL controller will transfer the aircraft to the GMC controller when they report they are ready for pushback and start. During busy periods the GMC Controller can inform the DEL Controller of the requirement to not release aircraft in order to restrict the rate of departures. 

!!! info "DEL offline"
    When **Kuwait Delivery (DEL)** is offline, its responsibilities are assumed by **GMC-E (OKKK_E_GND)**, which is always the bandbox position. Pilots will call **Kuwait Ground on 121.700** for their clearance.

----

## Chapter 2. GEN | Standard Operating Procedures 

### 2.1 Issuing IFR Clearances 

In Kuwait International Airport, SIDs are used to provide a standardized, efficient, and safe route for aircraft departing an airport, especially in busy terminal areas. The SIDs have a unique designator code for different departure runways. 

It is the responsibility of the **DEL Controller** to issue clearances to departing aircraft. Pilots are expected to report the following information on initial contact with the **DEL Controller** when requesting clearance. 

- Callsign 
- Stand Number
- Aircraft Type
- Current ATIS Information Code they are in receipt of


The DEL Controller should ensure that both the **aircraft stand number and aircraft type** are confirmed by the pilot prior to issuing them with a departure clearance. Any departure clearance issued should be valid against the RouteChecker with a flight level that is **appropiate for the direction of flight**. 

An **IFR Clearance** should have the following information in this order: 

- Callsign
- Destination 
- Standard Instrument Departure (SID) 
- Initial Altitude 
- Assigned Squawk 

***IFR Departure Clearance Example***

> **DEL Controller:** **"JZR101, cleared to Bahrain, via BOXIK4E Departure, climb altitude 4000ft, squawk 4212"**

!!!node "Departure Runway?"
    It is not a requirement for the DEL Controller to issue the departure runway in the IFR Clearance, it is expected the pilot has correctly listened to the D-ATIS

The DEL Controller **must** obtain a full and correct read back of the departure clearance. If they do not, then the pilot must be challenged to read back the full and correct departure clearance. 

***Challenge Example***

> **DEL Controller:** _**"JZR101, Negative. Cleared to Bahrain via BOXIK4E Departure, climb altitude 4000ft, squawk 4212"**_

!!!node "Be Paitent and Assist"
    If you are required to challenge a pilot for a correct readback, repeat it back clearly and slowly to ensure the pilot has opportunity to understand the information provided

Once the pilot has correctly read back the clearance, if the pilot did not provide the current ATIS letter, you must provide it.

> **DEL Controller:** _**"JZR101, read back correct, Information Alpha current, report ready for push and start."**_

When the aircraft has reported ready for push and start they will be transferred to the GMC Controller, and it is to be assumed by the GMC Controller that the pilot has a **correct clearance and is squawking his assigned transpoder code.** 

> **DEL Controller:** **JZR101, hold position, contact Kuwait Ground 121.700.**

### 2.1.1 Datalink Clearances (DCL)
Kuwait offers the ability for pilots to request and receive their **departure clearance via datalink (DCL).** This helps reduce frequency congestion and reduces the workload of the DEL Controller. This service can only be provided to pilots whom's aircraft has sufficent systems installed such as ACARS to send and receive text messages from a controlling unit. 
It is a requirement of the DEL Controller to ensure datalink is available at all times.

### 2.1.2 Incorrect Filed Flight Plans
It is the responsibility of the DEL Controller to ensure flight plans are correctly filed and using valid routings in conjunction with the RouteChecker. 
If routes are not filed correctly you must inform the pilot that they have filed an incorrect flight plan by **private message.** 

If a pilot calls on frequency before you have the chance to send the **private message** please advise the pilot on frequency to expect a route change via **private message**.

You can use tools such as SimBrief to provide pilots with valid routes. **VATMENA** actively ensures routes are updated in SimBrief for pilots to use. 

### 2.1.3 Filed Flight Levels 
**Kuwait Delivery (DEL)** must ensure pilots are filing correct flight levels in accordance with their filed routes. If Pilots have incorrectly filed flight levels in their flight plan you must inform the pilot to refile their flight plan via **private message**. 

Kuwait utilises the Semi-Circular Rule. Flights flying Westbound should file **Even** levels and flights flying Eastbound should file **Odd** levels. 

#### 2.1.4 Flight Level Capping 
Multiple destinations across the Gulf Region have level capped routes due to operational reasons. The DEL Controller shall ensure adherence to the below table, it is the responsibility of the DEL Controller to ensure aircraft have filed a correct level in their flight plan prior to issuing a clearance. If an incorrect level has been filed the DEL Controller shall inform the pilot that they are required to file a revised flight plan with the new level in accordance with the below table for level capped routes. 

| **Destination** | **Max Altitude / Flight Level** |
|:---------------:|:-------------------------------:|
|       ORMM      |              FL160              |
|       OEDF      |              FL250              |
|       OBBI      |              FL270              |
|       OTHH      |              FL330              |

### 2.1.5 Flow Restrictions

#### 2.1.5.1 Target Off Block Time (TOBT)
When A-CDM procedures are active (typically during busy events), pilots must report their confirmed TOBT on vacdm.vatsim.me, which is then displayed in the controller's client on the departure list. A fully green time indicates a confirmed TOBT. If a pilot has not confirmed their TOBT, the controller should request it on frequency and update the departure list accordingly.

The TOBT system allows aircraft to push back, taxi to the runway holding point and depart on schedule without extended delays in the departure queue. If an aircraft reports ready for pushback before its assigned TOBT, it will be instructed to hold position and will be given its place in the pushback sequence, unless aerodrome conditions permit and a slot is available. If an aircraft is cleared for push and start but does not begin pushing within 2-5 minutes, the pushback clearance is cancelled, and a new TOBT is assigned.

Please note TOBTs are only issued during certain events, this will be outlined via Khaleej vACC Staff if TOBT procedures are to be implemented for that particular event.

### 2.2 Departure Procedures
In Kuwait all departures should be cleared via a **Standard Instrument Departure (SID)** which is selected based on the first waypoint in their filed Flight Plan (FPL). 
All **Standard Instrument Departures (SIDs)** in Kuwait are RNAV (Area Navigation) and provide aircraft with a pre-defined route taking them from the departure airport into the **Control Area (CTA)** where they will be taken into the en-route environment. 

**16:**

| **SID** | **Designator** | **Departure Runway** |
|---------|----------------|----------------------|
| ALVAX   | 1K             | 16                   |
| ASVIR   | 1K             | 16                   |
| BOXIK   | 1K             | 16                   |
| RALKA   | 1K             | 16                   |
| SESRU   | 1K             | 16                   |
| DEKOB   | 1K             | 16                   |
| KATOD   | 1K             | 16                   |
| NIDAP   | 1K             | 16                   |

**15R**

| **SID** | **Designator** | **Departure Runway** |
|---------|----------------|----------------------|
| ALVAX   | 5E             | 15R                  |
| ASVIR   | 5E             | 15R                  |
| BOXIK   | 5E             | 15R                  |
| RALKA   | 5E             | 15R                  |
| SESRU   | 5E             | 15R                  |
| DEKOB   | 1L             | 15R                  |
| KATOD   | 1L             | 15R                  |
| NIDAP   | 1L             | 15R                  |

**33L:**

| **SID** | **Designator** | **Departure Runway** |
|---------|----------------|----------------------|
| ALVAX   | 5F             | 33L                  |
| ASVIR   | 5F             | 33L                  |
| BOXIK   | 5F             | 33L                  |
| TASMI   | 5F             | 33L                  |
| SESRU   | 5F             | 33L                  |
| DEKOB   | 1J             | 33L                  |
| KATOD   | 1J             | 33L                  |
| NIDAP   | 1J             | 33L                  |

**34:**

| **SID** | **Designator** | **Departure Runway** |
|---------|----------------|----------------------|
| ALVAX   | 1I             | 34                   |
| ASVIR   | 1I             | 34                   |
| BOXIK   | 1I             | 34                   |
| TASMI   | 1I             | 34                   |
| SESRU   | 1I             | 34                   |
| DEKOB   | 1I             | 34                   |
| KATOD   | 1I             | 34                   |
| NIDAP   | 1I             | 34                   |

### 2.3 VFR Procedures
**Kuwait Delivery (DEL)** does **not** issue VFR clearances. All VFR clearances (circuits, zone exits and zone entries) are issued by **Kuwait Tower (TWR)**. See [Kuwait Tower 3.5](Kuwait%20Tower.md#35-vfr-procedures).

When a VFR aircraft calls for start-up, DEL shall assign:

- An SSR code
- The departure runway (VFR circuits are flown on RWY34 or RWY16 only, as advised by TWR)
- The QNH, and confirm the current ATIS information

The aircraft is then transferred to the **GMC Controller**, as for IFR departures.

!!! note "Act Promptly"
    When you see a pilot file a VFR flight plan, inform TWR straight away so they can coordinate with APP if the flight will leave the Control Zone (CTR). Do not wait for the pilot to call up on frequency.

***VFR Start-up Example***

> **Pilot:** _"Kuwait Delivery, 9K-VFR, Cessna 172, stand 101, information Alpha, VFR, request start-up"_

> **DEL Controller:** _**"9K-VFR, runway 34, squawk 7001, QNH 1013"**_

> **Pilot:** _"Runway 34, squawk 7001, QNH 1013, 9K-VFR"_

> **DEL Controller:** _**"9K-VFR, readback correct, contact Kuwait Ground 121.700"**_

If the readback is incorrect, correct only the item that was read back wrongly:

> **DEL Controller:** _**"9K-VFR, negative, squawk 7001"**_

!!! note "Callsign Shortening"
    After two-way communication has been established, and provided no confusion is likely, the callsign may be abbreviated, e.g. 9K-VFR to 9-FR (Niner - Foxtrot - Romeo).

### 2.4 Departure List Management 
The **DEL Controller** is responsible for ensuring the departure list is correct and maintained prior to handing aircraft off to the GMC Controller. This includes ensuring filed routings are correct, Standard Instrument Departures (SIDs) have been assigned, initial altitudes has been set correctly and a squawk code has been assigned. 

The A/C Status Column must be updated to show the aircraft is on frequency. 

### 2.4.1 Squawk Code Not Set 
If an aircraft who has received his clearance and calls ready for push and start but has not set their assigned squawk code the **DEL Controller** must advise the aircraft to set squawk code. Aircraft will not be handed off to GMC for push back until the squawk code has been set. 

### 2.5 Transferring Aircraft to the GMC Controller
When an aircraft has received his clearance and calls for push and start with his assigned squawk code set the **DEL Controller** will then hand the aircraft off to the **GMC Controller** to be sequenced for push and start. 

> **DEL Controller:** _**"KAC107, contact Kuwait Ground on 121.700"**_
