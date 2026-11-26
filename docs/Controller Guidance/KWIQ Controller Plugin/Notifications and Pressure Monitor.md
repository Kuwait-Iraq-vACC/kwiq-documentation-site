---
title: Notifications and Pressure Monitor
---

Both follow the airports you are working, worked out top-down from who is online.

## Procedure Notifications
Staff post procedure updates for groups of airports. When you log on, and whenever new ones arrive, a flashing **KWIQ_NOTIFICATIONS** chat tab says how many are unread for your position.

Open **Notifications** in the KWIQ menu, or type `.kwiq notifications`, to list those for the airports where you provide a service. When you aren't logged on, all of them are listed. Use **Mark read** and **Mark unread** to keep track, and **Open link** to read more. Your read state is kept by the vACC, so it follows your API key.

The full list of procedure updates is on the [Procedure Updates](../Procedure%20Updates/index.md) page.

## Pressure Monitor
While you are logged on, the plugin watches the QNH of every airport in your position's top-down order. When a QNH changes, a flashing **PRESSURE_MONITOR** chat tab says so, with the transition level only when it changes too:

```
Pressure monitor: OKKK QNH now 1019 (was 1018)
Pressure monitor: ORBI QNH now 979 (was 981) TRL FL170 (was FL160)
```

A re-issued METAR with the same QNH doesn't trigger it. Type `.kwiq qnh <ICAO>` to see one airport's QNH and transition level at any time.
