---
title: RDF and TrackAudio
---

RDF (Radio Direction Finder) and its TrackAudio bridge are built into the plugin. Don't load `RDFPlugin.dll` or afv-euroscope-bridge as well: if you do, the plugin says so and leaves RDF off.

Both need [TrackAudio](../Audio%20Clients/TrackAudio.md) 1.3.0 Beta 5 or later.

## Direction Finding
A circle is drawn on each aircraft transmitting on your frequencies. When the aircraft is off screen, a line from the middle of the screen points to it. The circle is red when more than one aircraft transmits at once.

Middle-click to show the last transmission again. The **RDF state** tag item shows `!` while the aircraft is transmitting.

The vACC sets whether RDF draws for each position. Override it for yourself with **RDF Drawing** in the KWIQ menu, or `.rdf draw on` and `.rdf draw off`. Type `.rdf draw core` to go back to the vACC's setting.

## The TrackAudio Bridge
When you set a station to RX or TX in TrackAudio (or the AFV standalone client), the matching EuroScope voice channel follows, so you only set frequencies in one place. The bridge only works on a direct connection.

The **TrackAudio** row in the KWIQ menu shows the connection, which the plugin makes by itself:

| State | Meaning |
| ----- | ------- |
| Connected | TrackAudio is connected |
| AFV client | The AFV standalone client is connected instead |
| Not running | Neither is running |
| Off | RDF didn't start, or the bridge is off for your position |

Click the row to sync the channels again while connected, or to try to connect straight away while not.

If TrackAudio isn't running 15 seconds after you log on, the plugin tells you once.

| Command | What it does |
| ------- | ------------ |
| `.rdf refresh` | Turns the channels off and syncs them again from TrackAudio |
| `.rdf reload` | Reconnects to TrackAudio |
