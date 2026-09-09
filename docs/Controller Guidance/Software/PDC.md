---
title: Pre-Departure Clearance (PDC)
---

## What is a PDC?

PDC, Pre-Departure Clearance, or DCL, Data link Clearance, also known as **ARINC-623** is a service used in Europe and other parts of the world (excluding the US) that provides transmitting an enroute clearance directly to the pilot's onboard computer via a text format. Issuing PDCs significantly reduces frequency congestion and reduces the potential for errors in pilots understanding the clearance.

Within the Kuwait & Iraq vACC, only Kuwait (OKKK) has Datalink Clearance implemented.

## Methods of issuing a PDC

Currently, all datalink data link communications are run through the [Hoppie](https://www.hoppie.nl/acars/ "Opens in a new tab"){target="_blank"} network and can be accessed through many plugins.
Within both the OKAC and ORBB setups, CPDLC can be accessed through the TopSky plugin.

Alternatively controllers may send a PDC via direct message using the `.pdc` alias.

When offering PDC via the Hoppie network, controllers should advertise it in the INFO lines in EuroScope. This is added by default to positions that should have CPDLC utilised.

### Registering for Hoppie ACARS

Prior to utilising the Hoppie network, controllers should complete a simple [registration process](https://www.hoppie.nl/acars/system/register.html "Opens in a new tab"){target="_blank"} where the Hoppie's logon code will then be sent to your email address.

---

## Connecting to Hoppie

When loading up the sector file you will notice a 'CPDLC Setting' menu. After connecting to the network and setting your primary frequency (priming), this will populate with the correct Login code (this should match the one in your info line).

Your 'Login' is a unique code, and should only be tied to one Hoppie code. The login code is an abbreviation of the station you are controlling.
In the 'Logon Code' section, you should enter the ACARS logon code that you received via email.

!!! tip
    Go to `OKAC/ORBB > Plugins > TopSky Aerodrome > TopSkyCPDLChoppieCode.txt` and replace all contents of the file to store your logon code.

All the other settings are all automatically configured. If required, these can be adjusted as necessary.

As an aerodrome controller, it is important that you only check DCL/PDC in the CPDLC setting window.

<figure markdown="span">
  ![CPDLC Setting.png](../img/CPDLC%20Setting.png)
  <figcaption>CPDLC Setting Window</figcaption>
</figure>

After clicking on the 'Connect' button, it will turn green, indicating an online status.


<figure markdown="span">
  ![CPDLC Setting Online.png](../img/CPDLC%20Setting%20Online.png)
  <figcaption>CPDLC Setting Window with an active connection to the Hoppie server</figcaption>
</figure>

---

## Issuing a PDC

When a pilot submits a PDC request an audible alert will play and a the 'DCL' column will show a ![yellow.svg](../img/yellow.svg)yellow "RCD" text.

!!! info "Remarks text"
    If the pilot includes remarks text after the ATIS indicator, the text will show "RCD•".

<figure markdown="span">
  ![PDC RCD.png](../img/PDC%20RCD.png)
  <figcaption>Pilot requesting clearance via data link</figcaption>
</figure>

By left clicking on the "RCD", the Departure Clearance Window opens.
Here, you will find the information that the pilot has sent over, and any free text that they have submitted.
Below that, the data for your reply can be found. Mainly this is all automatically filled out.

Once you have checked that all the information in the window is correct you can click the "Send MSG" button. This will then change the "RCD" text to "SENT". If no response is received from the aircraft, the data link clearance is automatically rejected and a message is sent saying so.
If anything needs to be changed on the flight plan, the "R/T" button will send the pilot a "REVERT TO VOICE PROCEDURES" message.

<figure markdown="span">
  ![PDC Departure Clearance Window.png](../img/PDC%20Departure%20Clearance%20Window.png)
  <figcaption>Departure Clearance Window</figcaption>
</figure>

<figure markdown="span">
  ![PDC SENT.png](../img/PDC%20SENT.png)
  <figcaption>"SENT" text</figcaption>
</figure>

!!! tip "Sent Clearance"
    CLD 1530 260909 OKKK PDC 086

    UAE854 CLRD TO OMDB OFF 33L VIA SESRU5F
 
    SQUAWK 1402 ATIS T

    EOBT 1548

    ALT 4000FT

After the pilot has acknowledged the clearance, it becomes valid. This can either be done with the pilot replying with a "WILCO" message or a telex CDA message that matches the CLD.

Once acknowledged, the system will set the DCL text to "DONE" and the CRF automatically.

<figure markdown="span">
  ![PDC DONE.png](../img/PDC%20DONE.png)
  <figcaption>Validated PDC</figcaption>
</figure>