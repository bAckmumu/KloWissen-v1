KloWissen-v1.5
============

KloWissen is a Raspberry Pi podcast player. This is the First version of it.

## Linux applications
### gPodder 
`sudo apt install gpodder`
https://gpodder.github.io

`gpo`

#### Subscriptions in gPodder

`subscribe https://www.deutschlandfunk.de/podcast-nachrichten.1257.de.podcast.xml Nachrichten`

`subscribe https://www.dinowitz.de/feed/mp3/ Dinowitz`

`subscribe http://static.orf.at/podcast/fm4/fm4_ombudsmann.xml Ombudsmann`

`subscribe https://feeds.theincomparable.com/robot RobotOrNot`

`subscribe https://detektor.fm/feeds/feinkost-der-food-podcast Feinkost`

`subscribe https://detektor.fm/feeds/mission-energiewende MissionEnergiewende`

## Python 
pygame is used for audio playback, which ich installed by default with Raspberry Pi OS

### Phython Skripte
player

### Starting the player
`./player > player.log &`

`nohup ./player &`

`jobs -l`

`kill -1 `