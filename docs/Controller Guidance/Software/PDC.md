---
title: Pre-Departure Clearance (PDC)
---

## What is a PDC?

PDC, Pre-Departure Clearance, or DCL, Data link Clearance, are forms of transmitting an enroute clearance directly to the pilot's onboard computer via a text format. Issuing PDCs significantly reduces frequency congestion and reduces the potential for errors in pilots understanding the clearance.

Within the Kuwait & Iraq vACC, only Kuwait (OKKK) has Datalink Clearance implemented.

## Methods of issuing a PDC

Currently, all datalink data link communications are run through the [Hoppie](https://www.hoppie.nl/acars/ "Opens in a new tab"){target="_blank"} network and can be accessed through many plugins.
Within both the OKAC and ORBB setups, CPDLC can be accessed through the TopSky plugin.

Alternatively controllers may send a PDC via direct message using the `.pdc` alias.

When offering PDC via the Hoppie network, controllers should advertise it in the INFO lines in EuroScope. This is added by default to positions that should have CPDLC utilised.

### Registering for Hoppie ACARS

Prior to utilising the Hoppie network, controllers should complete a simple [registration process](https://www.hoppie.nl/acars/system/register.html "Opens in a new tab"){target="_blank"} where the Hoppie's logon code will then be sent to your email address.

---

## Connecting to CPDLC

When loading up the sector file you will notice a 'CPDLC Setting' menu. After connecting to the network and setting your primary frequency (priming), this will populate with the correct Login code (this should match the one in your info line).

