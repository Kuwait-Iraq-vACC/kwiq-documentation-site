# 3. Departure Clearance Procedures
## 3.1 General provisions
Baghdad delivery (ORBI_DEL) is responsible for validating routes and shall provide IFR clearance to departing aircraft, as delivery is a non-standard position Baghdad ground (ORBI_GND) is responsible for validating routes and shall provide IFR clearance to departing aircraft, whilst Baghdad delivery is not in use. The controller shall assign the correct departure procedure to the aircraft based on the first point that is filed on the flight plan.

Where the flight plan contains an invalid route, level, or departure procedure, delivery shall ensure that the error is corrected before the aircraft is given its clearance.

!!! warning   
    Baghdad delivery is a non-standard position and can only be opened with prior approval from the Levant vACC ATS department. Baghdad ground (ORBI_GND) shall assume all responsibilities of delivery.   

## 3.2 Departure clearance
### 3.2.1 General
The delivery is responsible for issuing clearances for departing aircraft. Pilots may be expected to report the following information on first contact:

- Aircraft Callsign;
- Aircraft type;
- Parking Stand;
- Destination;
- ATIS letter & QNH

### 3.2.2 Information contained in a departure clearance
An IFR clearance shall be in the following format:

- Callsign;
- Destination;
- Routing;
- Departure runway;
- Initially cleared altitude;
- Assigned SSR code

Delivery shall obtain a full readback of the clearance. If the pilot does not report the current ATIS letter on first contact, delivery shall pass the current ATIS letter and QNH.

Departing aircraft shall be instructed to report ready for pushback.

!!! phraseology  
    **IAW123**: Baghdad Ground, IAW123, request IFR clearance to Dubai, with information A.  
    **BI SMC**: IAW123, Baghdad Ground, cleared to Dubai, flight planned route, runway 33R, squawk 7403.  
    **IAW123**: Cleared Dubai, flight planned route, runway 33R, squawk 7403, IAW123.  
    **BI SMC**: IAW123, readback correct, report ready for push and start.  

!!! info   
    At Baghdad no SIDs are used, aircraft receive departure instructions in their line up/takeoff clearance, thus delivery (or ground) doesn't need to provide departure instructions.  

### 3.2.3 Aircraft requiring a reroute
If an aircraft requires a reroute, they shall be informed of such as soon as they have connected to the network by private message or on frequency. 

An aircraft shall be issued a reroute by delivery if the pilot’s route doesn’t comply with the standard routes laid out in Table 3-1.

## 3.3 Departure Procedures
### 3.3.1 Radar departures
At Baghdad there are no RNAV standard instrument departure procedures, thus aircraft are not given any departure procedures in there initial clearance with delivery (or ground).

In the take-off clearance, Baghdad Tower (ORBI_TWR) shall assign a heading to fly after departure and initial climb, aswell as a "turn altitue" appropriate to the Baghdad TMA exit point.

## 3.4 Rerouting aircraft
An aircraft shall be issued a reroute by delivery if the pilot’s route doesn’t comply with the standard routes laid out in Table 3-1. 

Several routing restrictions exist within Iraqi airspace and must be complied with when issuing a departure clearance.

!!! example   
    **Controller**: "IAW123, cleared to Dubai, NOLDO, P975, SESRU, flight planned route, squawk 0553."

!!! note
    The Levant vACC Operations Department maintains an up-to-date route database on SimBrief. These routes can be accessed by selecting the ***"User Submitted Routes"*** option, highlighted in purple, when planning a flight.

<figure markdown>
| Destination                                                    | Level Restrictions          | Routing                                      |
|----------------------------------------------------------------|-----------------------------|----------------------------------------------|
| North                                                          | -                           | BGD DCT NAMDI M860 NINVA                     |
| North                                                          | -                           | BGD DCT TAGRU L718 KABAN                     |
| East                                                           | -                           | BGD DCT NOLDO B411 PAXAT                     |
| South                                                          | -                           | BGD DCT NOLDO P975 SIDAD                     |
| Southwest                                                      | -                           | BGD DCT DELMI DCT RUKAM B411 MURIB           |
| West                                                           | -                           | BGD DCT DELMI G202 MODIK                     |
| West                                                           | -                           |BGD DCT DELMI G202 RAPLU R652 GIBUX L200 PASIP|

  <figcaption>Table 3-1: Standard routes</figcaption>
</figure>

!!! info 
      Should an aircraft file an invalid cruise level, delivery shall advise the aircraft of this when delivering the clearance. In **all** cases, the next lowest valid cruise level should be assigned and the aircraft advised.

!!! note
      Offering two valid levels (one above and below their requested level) is discouraged; a lower level than what is requested can be complied with certainty factoring the aircraft's maximum capable cruise level as per their gross weight. On the other hand, higher levels may be rejected due to aircraft performance or maximum cruise altitude capabilities.

      Thus, resorting to issuing the next lowest valid cruise level minimises radio transmissions and simplifies the correction process between the controller and the aircraft.


## 3.5 Runway change procedure
Runway change shall be coordinated with Baghdad tower (ORBI_TWR).

## 3.6 VFR aircraft
VFR aircraft must be coordinated with tower before receiving any clearance, tower may instruct delivery to provide the VFR clearance or delivery to inform the aircraft to "expect clearance at holding point".

### 3.6.1 VFR departures into uncontrolled airspace
VFR traffic shall be cleared via the most appropriate VFR route towards their destination. If necessary, the clearance may be amended by AIR prior to departure.

All VFR departures shall be assigned a discrete SSR code so that they may be identified on radar.

### 3.6.2 VFR departures into controlled airspace
VFR aircraft requesting clearance to climb into approach airspace (above 1500 ft) shall only be cleared after prior coordination with approach/departure control. Otherwise, they shall be instructed to remain outside controlled airspace after leaving the control zone.

All VFR departures shall be assigned a discrete SSR code so that they may be identified on radar.

!!! example
      **Pilot:** Al Maktoum Ground, A6-CTK, SR22, request eastbound departure on track Fujeirah, altitude 6500ft.

      **Controller:** A6-CTK, Al Maktoum Ground, cleared eastbound departure, altitude 6500ft VFR, Runway 30, Squawk 0611.

      **Pilot:** Cleared eastbound departure, altitude 6500ft VFR, Runway 30, Squawk 0611, A6-CTK.

      **Controller:** A6-CTK, readback correct, information A, QNH 1003, Report ready for start-up.

### 3.6.3 VFR traffic remaining in circuit
VFR traffic wishing to remain in the circuit shall be cleared only after prior coordination with AIR and Approach/Departure control.
All VFR circuit traffic shall be assigned a discrete SSR code so that they may be identified on radar.

All VFR aircraft shall be instructed to conduct circuits to the north of the aerodrome (right-hand circuits for 30 and left-hand circuits for 12) at an altitude of 1000 ft. EFTA aircraft shall be instructed to conduct circuits to the south of the aerodrome (left-hand circuits for 31 and right-hand circuits for 13) at an altitude of 1000 ft, **only** during the academy operational hours. Aircraft may also be cleared to conduct circuits at 1500 ft, if required.