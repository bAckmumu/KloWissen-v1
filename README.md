KloWissen-v1
============

KloWissen is a Raspberry Pi podcast player. This is the First version of it.

## Linux applications
### mpd (Music Player Daemon)
`sudo apt install mpd`

### mpc
`sudo apt install mpc`

### gPodder 
`sudo apt install gpodder`
https://gpodder.github.io

## cron Jobs
* crontab -e
* 01 * * * * /home/pi/script/loadpodcasts
* 05 * * * * /home/pi/script/deleteday >> /home/pi/script/del.log

## Phython Skripte
* deletday
* loadpodcast
* player
