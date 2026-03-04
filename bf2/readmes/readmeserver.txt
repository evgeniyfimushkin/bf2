Battlefield 2™ Dedicated Server Readme v1.0 (new revision)
July 21st 2008
Copyright Electronic Arts
Battlefield 2™ v1.50

=================
Table of Contents
=================

I.	Installing the Windows Dedicated Server
II.	Configuring and starting the Windows server using the Server Launcher
IIa. 	Configuring and starting the Windows server using the server executable
III.	The Map List
IV.	Installing the Linux Dedicated Server
V.	Configuring and starting the Linux Dedicated Server
VI.	Hosting a Battlefield 2™ Server
VII.	Remote Console (rcon) Access
VIII.	BattleRecorder
IX.	Points to note when using BattleRecorder
X.	Remote VOIP Server
XI.	Appendix A – Map Names, Sizes & Modes
XII.	Appendix B – Useful commands
XIII.	Appendix C - Hardware Requirements
XIV.	Appendix D - Server settings and their functions
XV.	Version notes

==========================================
I. Installing the Windows Dedicated Server
==========================================

To install the server, double click the “Battlefield 2 Server.exe” file and follow the on screen prompts. It is recommended you install PunkBuster even if you are not running a Ranked server.

Note that if your system clock and date are not set correctly this can lead to issues with stats processing on Ranked servers. Please ensure the time and date are set correctly before starting the game server.

=========================================================================
II. Configuring and starting the Windows server using the Server Launcher
=========================================================================

Run the shortcut to start the server – “Start” – “Programs” – “EA Games” – “Battlefield 2 Server” – “Run Dedicated Server” and the Server Launcher window will appear.

Click the “+” at the bottom to create a new profile.

Enter a suitable name (no spaces or special characters allowed) and click “OK”.

Edit the settings in the server GUI as needed. Note that clicking once on an option will display a brief description of what function that command carries out.

See Appendix D for a list of the server commands and their functions.

============================================================================
IIa. Configuring and starting the Windows server using the server executable
============================================================================

It is possible to start the server without using the Server Launcher GUI. This is done by creating a shortcut to the server executable (BF2_w32ded.exe) and applying startup parameters to it. The syntax for the parameters are as follows:

+config <path to serversettings.con file>
+mapList <path to maplist.con file>"

Example:

"C:\Program Files\Electronic Arts\Battlefield 2 Server\BF2_w32ded.exe" +config C:\serversettings.con +mapList C:\maplist.con 

This setup is designed primarily for Ranked Server Partners. For individual servers it is more convenient to use the Server Launcher. 

=================
III. The Map List
=================

The maplist tab allows you to select the maps and game modes you want to run on the server. By default this will display Conquest maps, but the game mode can be selected by clicking on the right hand dropdown box:

The available game modes are as follows:

Gpm_cq – Conquest
Gpm_coop – Cooperative

Different maplists are available for each game mode. Not all game modes are available on all maps. Note that coop can only be played on maps that are enabled for single player. Also note that Cooperative mode is not supported on Ranked servers. If Cooperative mode is selected on a Ranked server the ranking system will be disabled while the Coop map plays.

See Appendix A for a list of all the map names and their supported modes and sizes.

To add a map to the maplist, simply highlight it in the left hand window and click the right arrow to add it. You may also add maps by double clicking them, or use CTRL + click or SHIFT + click to add multiple maps. Use the up and down arrows to re-order the maps in the right hand window.

Maps may be removed from the maplist in the same fashion.

Once you have configured your settings and added the maps you want, click the “Save” button to save the configuration and then click the “Start” button to start the server. Note that clicking on “Start” again will set the server to auto-restart if it should end unexpectedly.

=========================================
IV. Installing the Linux Dedicated Server
=========================================

Copy the install archive onto your server PC and double click it to begin the installation.Select “Run in a Terminal” from the resulting pop up. 

Note that if you are carrying out a remote installation using SSH or other remote admin tool you may need to use the “chmod” command to allow the correct file access privileges. Please consult your Linux documentation on how to use the “chmod” command.

Once the archive has unpacked, you will be required to read and accept the EULA both for the server and for PunkBuster before installation will continue. 

Enter a suitable path to complete the installation, for example /Home/<user>/. The server will automatically create a folder called “BF2” in that path and install the server into it.

Note that if your system clock and date are not set correctly this can lead to issues with stats processing on Ranked servers. Please ensure the time and date are set correctly before starting the game server.

======================================================
V. Configuring and starting the Linux Dedicated Server
======================================================

The command files for the Linux server are stored in the following folder:

Battlefield 2 - <install path>/BF2/Mods/BF2/Settings
Special Forces - <install path>/BF2/Mods/xpack/Settings

The files are called “serversettings.con” which holds all of the settings for the server, and “maplist.con” which contains all of the settings for which maps to load, what size and in which order to run them. These files may be opened and edited using any text editing program. 

See Appendix D for a list of the server commands and their functions.

To add a map to the maplist, you must prefix each entry with the “maplist.append” command. The correct syntax for this command is as follows:

Maplist.append <map name> <game mode> <map size>

For example, to add the map “Dalian Plant” to the maplist to run in 64 player Conquest mode the command would be as follows:

Maplist.append dalian_plant gpm_cq 64

Note that if the map size is not added to the end of the command, the map size will be taken from the “sv.MaxPlayers” value in the “serversettings.con” file. Adding a map size to the map list is useful for running small maps with larger numbers of players, for example running a 32 player map with 64 players. Note that this is not supported for Ranked servers and made lead to your server being removed from the Ranked Server Providers list if you do so.

Please see Appendix A for a list of all of the map names and the supported sizes and game modes.

It is recommended that you make a backup copy of your “serversettings.con” and “maplist.con” files in case you need to replace them at any time, or if you wish to quickly switch server configurations.

To start the server, open the “BF2” folder and run “start.sh”. It is recommended you run the server in a terminal window to enable easier monitoring and control of the server.

To start a Special Forces server, open the “BF2” folder and run “start.sh /xpack”.

=====================================
VI. Hosting a Battlefield 2™ Server
=====================================
 
In order to host a Battlefield 2™ server, you must have the following ports open in your firewall. 
           
UDP		27900
UDP/TCP 	29900
TCP    		80
TCP     	4711
UDP     	27901
UDP     	1500-4999
UDP/TCP 	1024-1124
UDP     	29900
UDP/TCP 	27900
UDP     	17567
UDP     	55123-55125
UDP/TCP		18000
UDP/TCP		18300

Please note this is for a single server instance. Should you wish to run multiple instances on one host, all of the instances must run on unique ports.

=================================
VII. Remote Console (rcon) Access
=================================

To setup remote console access to the server:

- On the server create a new plain text document in \admin\ called default.cfg

- Enter the following text into the new file:

port=4711
password=YourPassword

- Save the file, and start the server.

To use Rcon while on the server, press the "Tilde" (~) key on your keyboard to open the console, and type the commands you wish to run in the following fashion:

- rcon login <YourPassword>
Use this command to login to the server.

- rcon users
This command lists all the users connected to the server.
Very similar to admin.listPlayers

- rcon exec <command name>
Replace <command name> with a console command you would like to execute on the server.
For example: rcon exec admin.kickPlayer 3

====================
VIII. BattleRecorder
====================

The Battlefield 2™ Server includes a facility called BattleRecorder. This records all of the gameplay for a particular round and makes it available for players in that round to download and view at a later date. There are two components to BattleRecorder, which are described below.

To set up BattleRecorder on your server, follow the instructions below:

The Dedicated Server requires the following information:

- AutoRecord
Set AutoRecord to on (sv.autorecord 1) to enable the BattleRecorder. Every round played on the server will now be recorded to a file.

- DemoDownloadURL <http://YourServer.com/YourDirectory/>
This is the URL that will be passed to all the connected clients at the end of the round. This is the URL that the Battlefield 2™ front end will try and download the demo file from when the user selects 'download'. The demo file must be in the directory specified in the URL, or the demo download will fail. The URL specified here is case sensitive and must match exactly the URL of your web site.

- AutoDemoHook <adminutils/demo/Your_Script.exe>
The server runs this script at the end of every round where AutoRecord is enabled. In the majority of cases the default script may be used.

- DemoQuality <value>
You can control the quality of the recording made by the BattleRecorder. '1' is the default setting, and we recommend this is used for internet games. '10' is the highest setting, using this will increase the size of the file by around a factor of 8.
Higher settings will also increase the load on the server.

The second component to BattleRecorder is the script that is run when a round ends. This script can be rewritten or replaced as needed. The Battlefield 2™ server will simply attempt to execute the script specified in AutoDemoHook at the end of each round.

The default script, called auto_rotate, was written in Python and then built in to an executable.

The Python script can be found here \adminutils\demo\rotate_demo.py

The script will move a BattleRecorder file from the server to a new local location, or to an FTP site. You can also specify the number of files to keep archived.

The script is configured using a configuration file, called 'auto_rotate.cfg', found in the root of the Battlefield 2™ Server installation root directory.

In this file you can configure:

- file_limit = <value>
Use this value to set the number of BattleRecorder files you would like to keep available. The default is 30. Once the limit is reached, a new file will replace the oldest one.

- target_root = <local directory path>
If you intend to transfer to a local directory, enter the path here.

- use_ftp = <bool>
Set this to 1 if you wish to FTP the DemoRecorder file to a new location.

- ftp_target_dir = <path to webroot demos>
Enter the path on the FTP site where you want the DemoRecording transferred to. Note this path is case sensitive and must match exactly the folder name of your FTP upload site.

- ftp_server = <server URL or IP>
Enter the URL or IP of your FTP server. Again this is case sensitive and must match exactly the full URL of your FTP upload site.

For example, if the URL of your web site is:

“www.myftp.com/BF2/Demos”

Then your “ftp_target_dir” should be “/BF2/Demos/” (without the quotes) and your “ftp_server” should be “ftp.myftp.com” (without the quotes). In the “serversettings.con” file or in the Server Launcher, your “DemoDownloadURL” should be “http://www.myftp.com/BF2/Demos/” (again without the quotes).

- ftp_user = <FTP login username>
Enter your FTP sites login username.

- ftp_password = <password>
Enter the password for your login account.

============================================
IX. Points to note when using BattleRecorder
============================================

BattleRecorder will significantly increase your server's load; therefore we do not recommend running 64 player games with the BattleRecorder feature enabled.

BattleRecorder files become larger as you increase the number of players and the ticket allocation. For a round with 64 players with 250 tickets on each side, you should expect a file size of around 10-12 Mb with the DemoQuality set to 1.

When you download a BattleRecorder file, using the 'Community' function in the Battlefield 2™ front end, it is saved in:

\My Documents\Battlefield 2\Profiles\Default\Demos\

Every profile on your computer will save BattleRecorder files to this location.

It is possible to download BattleRecorder files from a friend or website and copy them into the BattleRecorder directory above. They will then appear on the 'Community' page for you to play.

=====================
X. Remote VOIP Server
=====================

Battlefield 2™ Server includes a remote VOIP server. This is included to run as a standalone VOIP server to remove the need for the game server to handle VOIP as well as the game.

To use the remote VOIP server, install the Battlefield 2™ Dedicated Server onto the PC you wish to use as a remote VOIP server. There are two files to pay attention to:

BF2VoipServer_w32ded.exe - The server executable.
voip.con - The remote server configuration file.

To set up the server, open the "voip.con" file and edit the entries to support your game server setup. The syntax is as follows:

<port> <password> <game server interface IP>

55125 no_password 123.123.123.123

Note that it is only necessary to include the game server interface IP if you are connecting multiple game servers to a single remote VOIP server, for example:

55125 no_password 123.123.123.123
55126 no_password 123.123.123.124
55127 no_password 123.123.123.125

Also note that all game servers that connect to a remote VOIP server must do so over unique ports.

==========================================
XI. Appendix A – Map Names, Sizes & Modes
==========================================

- Dalian Plant
Map name – dalian_plant
Sizes – 16, 32, 64
Modes – gpm_coop, gpm_cq

- Daqing Oilfields
Map name – daqing_oilfields
Sizes – 16, 32, 64
Modes – gpm_coop, gpm_cq

- Dragon Valley
Map name – dragon_valley
Sizes – 16, 32, 64
Modes – gpm_coop, gpm_cq

- FuShe Pass
Map name – fushe_pass
Sizes – 16, 32, 64
Modes – gpm_coop, gpm_cq

- Gulf of Oman
Map name – gulf_of_oman
Sizes – 16, 32, 64
Modes – gpm_coop, gpm_cq

- Kubra Dam
Map name – kubra_dam
Sizes – 16, 32, 64
Modes – gpm_coop, gpm_cq

- Mashtuur City
Map name – mashtuur_city
Sizes – 16, 32, 64
Modes – gpm_coop, gpm_cq

- Operation Clean Sweep
Map name – operation_clean_sweep
Sizes – 16, 32, 64
Modes – gpm_coop, gpm_cq

- Sharqi Peninsula
Map name – sharqi_peninsula
Sizes – 16, 32, 64
Modes – gpm_coop, gpm_cq

- Songhua Stalemate
Map name – songhua_stalemate
Sizes – 16, 32, 64
Modes – gpm_coop, gpm_cq

- Strike at Kerkand
Map name – strike_at_karkand
Sizes – 16, 32, 64
Modes – gpm_coop, gpm_cq

- Zatar Wetlands
Map name – zatar_wetlands
Sizes – 16, 32, 64
Modes – gpm_coop, gpm_cq

===========
Euro Forces
===========

- Great Wall
Map name – greatwall
Sizes – 16, 32
Modes – gpm_coop, gpm_cq

- Operation Smoke Screen
Map name – operationsmokescreen
Sizes – 16, 32
Modes – gpm_coop, gpm_cq

- Taraba Quarry
Map name – taraba_quarry
Sizes – 16, 32
Modes – gpm_coop, gpm_cq

============
Armored Fury
============

- Midnight Sun
Map name – midnight_sun
Sizes – 16, 32, 64
Modes – gpm_coop, gpm_cq

- Operation Harvest
Map name – operationharvest
Sizes – 16, 32, 64
Modes – gpm_coop, gpm_cq

- Operation Road Rage
Map name – operationroadrage
Sizes – 16, 32, 64
Modes – gpm_coop, gpm_cq

===============
Additional Maps
===============

- Wake Island 2007
Map name – wake_island_2007
Sizes – 64
Modes – gpm_cq

- Road to Jalalabad
Map name – road_to_jalalabad
Sizes – 16, 32, 64
Modes – gpm_coop, gpm_cq

- Highway Tampa
Map name – highway_tampa
Sizes – 16, 32, 64
Modes – gpm_cq

==============
Special Forces
==============

- Devils Perch
Map name – devils_perch
Sizes – 16, 32, 64
Modes – gpm_coop, gpm_cq

- Ghost Town
Map name – ghost_town
Sizes – 16, 32, 64
Modes – gpm_coop, gpm_cq

- Iron Gator
Map name – iron_gator
Sizes – 16, 32, 64
Modes – gpm_cq

- Leviathan
Map name – leviathan
Sizes – 16, 32, 64
Modes – gpm_cq

- Mass Destruction
Map name – mass_destruction
Sizes – 16, 32, 64
Modes – gpm_coop, gpm_cq

- Night Flight
Map name – night_flight
Sizes – 16, 32, 64
Modes – gpm_coop, gpm_cq

- Surge
Map name – surge
Sizes – 16, 32, 64
Modes – gpm_coop, gpm_cq

- Warlord
Map name – warlord
Sizes – 16, 32, 64
Modes – gpm_coop, gpm_cq

==================================
XII. Appendix B – Useful commands
==================================

To view all the available server commands, once the server has started, in the console press the “Tab” key twice. This will display all of the server command roots, such as “sv.” and “admin.”. To view each command subset, type a root command followed by pressing the “Tab” key twice, for example type “sv.” then “tab” twice (minus the quotes).

================
Maplist Commands
================

- mapList.list
Every map on the server has an ID number, which is used for voting to change maps. This command lists those numbers, the map name, game mode and the number of players if specified.

- mapList.configFile <new location for file>
Used to specify the location of the _mapList.con
The default is \My Documents\Battlefield 2\ServerConfigs\

- mapList.mapCount
Shows the total number of maps in the current map list

- mapList.currentMap
Shows the map list ID number of the current map being played

- mapList.clear
Clears the current map list.
Warning: If there are no maps in the map list when the server starts loading a new map, all clients will be left on the loading screen.

- mapList.remove <map ID number>
Removes the map you specify from the map list

- mapList.append <map name> <game mode> [number of players]
Add a new map to the end of the map list.
You must specify the map name and the game mode. Number of players is optional, if not specified will default to the current server setting.

- mapList.insert <map ID number> <map name> <game mode> [number of players]
Exactly the same as mapList.append, but with this command you can specify at what map ID number to insert the new map into the list at.

==============
Admin Commands
==============

- admin.listPlayers
Lists the players connected to the server.
This command lists the players ID number, their player name and if the player is remote it also lists the players IP number.

- admin.runNextLevel
Forces the server to end the round and start the next map in the map list.

- admin.currentLevel
Shows the map list ID number for the current map being played.
The same as mapList.currentMap.

- admin.nextLevel <map ID number>
This allows you to set which map to run next in the rotation.

- admin.restartMap
Restarts the current map.

- admin.banPlayer <player ID number> [timeout]
Enter the player ID number you would like to ban. Bans the player from this server by using their IP address.
Bans can be set on CD key hashes.
Bans are stored as absolute times in banlist.con. Existing bans in banlist.con will be interpreted as permanent bans.
You can choose from a selection of time outs:
Entering 'perm' means that the ban is permanent. This is the default if no time out is entered.
An integral number meaning the number of seconds the ban will be active (i.e. 3600 means one hour).
Entering 'round' means the ban is active until the next map.
A whole number preceded by a colon (i.e. :1234567), meaning the epoch expiration time of the ban (number of seconds since 1 Jan 1970).

- admin.banPlayerKey <player ID number> [timeout]
Enter the player ID number you would like to ban. Bans the player from this server by using their CD key hash.
You can also specify a time out. See admin.banPlayer for the time out list.

- admin.addAddressToBanList <IP address> [timeout]
Enter the IP number you would like to ban.
You can also specify a time out. See admin.banPlayer for the time out list.

- admin.addKeyToBanList <CD key hash> [timeout]
Enter the CD key hash you would like to ban.
You can also specify a time out. See admin.banPlayer for the time out list.

- admin.removeAddressFromBanList <IP address>
Enter the IP address you would like to remove from the ban list.

- admin.removeKeyFromBanList <CD key hash>
Enter the CD key hash you would like to remove from the ban list.  

- admin.clearBanList
Clears all ban lists.

- admin.listBannedAddresses
Displays a list of the currently banned IP addresses.

- admin.listBannedKeys
Displays a list of the currently banned CD keys.

- admin.kickPlayer <player ID number>
Enter the ID number of the player you would like to kick.

=======================================
XIII. Appendix C - Hardware Requirements
=======================================

We highly recommend Battlefield 2™ servers are run on dedicated server platforms. Currently, the best performance is on a machine with the following specifications:

=====
LINUX
===== 

- Minimum Specification, based on playing a 16 player game:
  CPU: 1 Ghz
  RAM: 256 Mb

- Recommended Specification, based on playing a 64 player game:
  CPU: 3 Ghz. For AMD Athlon 64 CPU: 3500+ (2.2 Ghz)
  RAM: 2 Gb

- Recommended Specification, based on playing a 48 player Titan game:
  CPU: 3.6 Ghz. For AMD Athlon 64 CPU: 4800+
  RAM: 2 Gb

- Optimal Specification, based on playing a 64 player Conquest game:
  Only run one instance of BF2 per physical CPU with Hyperthreading disabled
  CPU: AMD Athlon 64 4800+ or 3.6GHz Xeon.
  RAM: 2Gb per physical CPU

- Optimal Specification, based on playing a 48 player Titan game:
  Only run one instance of BF2 per physical CPU with Hyperthreading disabled
  CPU: AMD Athlon 64 4800+ or 3.8GHz Xeon.
  RAM: 2Gb per physical CPU

=======
WINDOWS
=======

- Minimum Specification, based on playing a 16 player game:
  CPU: 1 Ghz
  RAM: 384 Mb

- Recommended Specification, based on playing a 64 player game:
  CPU: 3 Ghz. For AMD Athlon 64 CPU: 3500+ (2.2 Ghz)
  RAM: 2 Gb

- Optimal Specification based on playing a 64 player Conquest or game:
  Only run one instance of BF2 per physical CPU with Hyperthreading disabled
  CPU: AMD Athlon 64 4800+ or 3.66GHz Xeon.
  RAM: 2Gb per physical CPU

=========
BANDWIDTH
=========

- Minimum
  2.5 Mbit

- Recommended
  5Mbit

Note that the server requires more upstream bandwidth (server to client) than downstream (client to server). The above bandwidth recommendations are upstream speeds.

As always if you can increase any of the above hardware you will improve your overall gameplay experience.

========
FIREWALL
========

The use of a software firewall on the server is not recommended, as it can adversely affect server performance and the overall gameplay experience.

====================================================
XIV. Appendix D - Server settings and their functions
====================================================

Note that the following commands are prefixed "sv." when use in the serversettings.con file or server console on both Windows and Linux.

- ServerName – This is the name that the server will display in the server browser.

- Password – This allows you to set a password for the server. Note that Ranked servers cannot be password protected.

- Internet – Check this box to have the server display in the “Multiplay” menu in the 2142 client. Ranked servers must have this option checked.

- Ranked – This sets whether or not the server will use the official Ranking system and send end of round scores to the backend stats system. To run a Ranked server the server IP address must be listed in the Ranked Server Providers list – contact your server provider for this facility.

- WelcomeMessage – This allows you to enter text that will be displayed on the server info window while the client is loading the map.

- ServerIP – This sets the IP address that the server will display to the client. This is primarily for servers that have a front-end game IP and a back-end admin IP.

- ServerPort – This is the port that the clients will use to communicate with the server. Note that if multiple server instances are run on the same host PC, this value must be unique to each instance. Recommended range is from the default 16567 to 16570.

- AllowFreeCam – This setting allows the player to use the free camera mode while waiting to spawn into the game (press Space on the spawn screen to activate).

- AllowExternalViews – This allows the players to switch between the normal internal view and the various external views while in vehicles.

- AllowNoseCam – This allows the player to use the nose camera (eliminating the vehicle model) while in aircraft.

- HitIndicator – This setting controls whether the hit indicator will be displayed to the clients when shooting enemy targets.

- MaxPlayers – This sets how many players will be allowed to join the server. It also sets the map size that will be loaded in Conquest mode. Note the maximimum number of players in Titans Mode is 48. In Cooperative mode this value sets the amount of bots to load. As human players join bots will be removed on a one for one basis.

- NumPlayersNeededToStart – How many players need to be connected to the server before the round starts. This setting has mandatory values for Ranked servers – 6 players for a 16 player server, 6 for 32 player and 8 for 48/64 player.

- NotEnoughPlayersRestartDelay – This sets how long the round will continue if the number of players falls below the value set above. Once this time has expired the server will end the round.

- CoopBotRatio - This detemines the percentage of total bots that will be on team 1 which is the MEC and Chinese. This setting does not affect human players.

- CoopBotCount - This specifies the total number of bots that will spawn in a Coop game. This does not affect the number of human players.

- CoopBotDifficulty - This determines how tough the bots are in Coop mode with 10 being the easiest, 50 being medium and 100 being the hardest.

- NoVehicles - This sets the server in "Infantry Only" mode and removes all vehicles except boats. Boats are excluded to allow gameplay on maps like Wake Island.

- StartDelay – this sets the time period between the required number of players joining the server and the round starting (this will be displayed to the clients as the “Commander Election” period).

- EndDelay – This sets the time period between the round ending and the server rotating to the next round/map.

- SpawnTime – How long a player must wait before respawning. The default 15 seconds is mandatory on Ranked servers and cannot be changed.

- ManDownTime – The time period during which a player may be revived. This value must be lower than the SpawnTime value. Again this is a mandatory 15 seconds on Ranked servers.

- TicketRatio – How many tickets each team will have. Note this is a percentage figure, not how many actual tickets each team has. The actual number of tickets is set by the map size and the game mode, for example on Conquest: Assault maps where one team has an uncapturable base, that team will start with less tickets than the team with no uncap. The default value of 100 is mandatory on Ranked servers. This value has no bearing on gpm_ti game modes.

- RoundsPerMap – How many rounds will be played on each map before loading the next map.

- TimeLimit – This value (in minutes) sets how long the round will last before ending. The round can still be ended normally if one team loses all of its tickets or its Titan is destroyed. Note that time limits may not be used on Ranked servers. Also note that this value is listed in seconds in the "serversettings.con" file on Linux servers. Time limits may not be set on gpm_ti game modes.

- SoldierFriendlyFire – A percentage value of how much damage will be caused by direct infantry weapon fire to players on the same team.

- VehicleFriendlyFire - A percentage value of how much damage will be caused by direct vehicle weapon fire to players on the same team.

- SoldierSplashFriendlyFire - A percentage value of how much damage will be caused by indirect infantry weapon fire to players on the same team.

- VehicleSplashFriendlyFire - A percentage value of how much damage will be caused by indirect infantry weapon fire to players on the same team.

- TkPunishEnabled – Controls whether or not the punish system for team killing is on or off.

- TkNumPunishToKick – The number of times a player may be punished for team kills before being automatically kicked from the server.

- TkPunishByDefault – This setting will automatically punish players for teamkilling if the victim does not choose to punish or forgive.

- VotingEnabled – Controls whether or not players may vote for map changes, commander mutiny and player kicks.

- VoteTime – The time (in seconds) that a vote will last for before the result is applied.

- MinPlayersForVoting – How many players are required to vote for the vote to be successful.

- VoipEnabled – Controls whether or not the Voice Over IP system will be used by the clients.

- VoipServerRemote – Controls whether or not the server will use its own in-built Voip system or the Battlefield Remote VOIP Server.

- VoipServerRemoteIP – The IP address of the remote VOIP server, if one is to be used.

- VoipServerPort – The port used by the server to control VOIP

- VoipBFClientPort – The VOIP port used by the clients to communicate.

- VoipBFServerPort – The VOIP port the server uses to resend messages on to the clients. 

Note – all the above ports must be unique if more than one instance is hosted on one PC.

- VoipSharedPassword – The password set on a remote VOIP server. This will be communicated by the server to the clients to enable them to use the remote server.

- VoipQuality – This sets how much bandwidth will be allocated to ensure good VOIP communication.

- GameSpyPort – The port over which the server will communicate with the GameSpy back-end system. Again this must be unique for multiple instances on a common host. It is recommended to stay between the default port 29900 and port 29950.

- AllowNATNegotiation – This determines whether or not clients behind a NAT enabled router or firewall will be able to join the server. In 99% of cases this setting is not needed.

- InterfaceIP – This is used to communicate with the remote VOIP server. This IP must be set in the "voip.con" file if multiple servers are to use the same remote VOIP server.

- AutoBalanceTeam – Determines whether or not the server will force the teams to be even.

- TeamRatioPercent – This is a percentage value of how many players need to be on each team before the server considers the teams even. The default value of 100 will split the players evenly across both teams.

- AutoRecord – Enables the BattleRecorder feature.

- DemoDownloadURL – This is the URL for the website where the BattleRecorder demo files will be stored. This is communicated to the clients so they can retrieve the demos.

- AutoDemoHook – Leave as default unless you are very familiar with the python scripting language.

- DemoQuality – This sets the quality of the recording.

- AdminScript – Allows the use of custom python scripts for server administration. Leave as default if you are not familiar with the python scripting language.

- SponsorLogoURL – The URL of an image that will be displayed in the server info window in the server browser when the server is highlighted.

- CommunityLogoURL – The URL of an image that will be displayed in the server info window while the client loads the map.

- PunkBuster – Determines whether or not the PunkBuster anti-cheat system will be used. This is mandatory for Ranked servers. Visit www.evenbalance.com for more info on PunkBuster.

- UseGlobalRank – Determines whether or not players ranks will be displayed in-game. This setting is always set to on for Ranked servers.

- UseGlobalUnlocks - Determines whether or not players will be allowed to use items they have unlocked on Ranked servers. This setting is always "on" for Ranked servers and cannot be turned off.

- NumReservedSlots – Determines the number of reserved player slots on the server. The player nicknames that are allowed to use these reserved slots are listed in the file “reservedslots.con” in the "settings" folder of the server install (this file needs to be  created manually). 

- FriendlyFireWithMines - When set to off, this prevents mines and claymores from being detonated by friendly players and vehicles.

==================
XV. Version Notes
==================

v1.50

- Various changes made to prevent cheating.
- Added checks to prevent "runway grieving"
- Added Highway Tampa to the default build to make it a compulsory update.
- Added the new map Operation Blue Pearl.
- Special thanks to Blackbird at the TV2 community www.battle.no 

v1.41

- Fixed an extremely intermittent server crash bug.

v1.4

- Added a new map, Road to Jalalabad.
- Fixed the Linux server hangs when trying to load a Special Forces Co-Op map.
- Fixed a crash in Co-op after a player is revived without a kit.
- Fixed a server crash on Linux 32 when trying to rotate maps in Coop Mode.
- Adjusted the minimum number of players to start the round on ranked servers. 
The new values for 16, 32 and 64 players are 6, 8 and 8 respectively.
- Re-enabled unlocks on unranked servers.
- Ranked Servers now force unlocks.
- Added support for multiple gamemodes in single maplist for mods.

v1.3

- Added support for Armored Fury booster pack
- Co-op: 
Co-op Mode allows you to play Single Player levels on the Internet and LAN with both AI controlled bots and human players. Several new options have been created that will allow the server creator to modify how the bots behave in game.
Number of Bots: This setting allows you to determine the total number of bots that will spawn in game.

Bot Ratio: This setting allows you to determine the percentage of total bots that will spawn for each team. For example, setting this value to 25 means that 25% of the total bots will spawn in Team 1, and 75% in Team 2. Team 1 is always the MEC, Chinese, or their allies, while Team 2 is always the USA, EU, and their allies.

Bot Difficulty: This setting determines the skill level of the bots. 10 is easiest, 100 is the most difficult.

- Fixed issues with remote console and linux server

v1.22

- Improved Server Stability
- Various client side fixes

v1.21

- Fixed the Hmmwv with TOW crash on Battlefield 2: Special Forces maps
- Fixed the Battle Recorder crash
- Fixed the error in Client - Server communication causing sound, animation and other sync issues.

v1.2

- Added support for Euro Forces booster pack

v1.12

- Improved server stability
- Various client side fixes

v1.03

- Added a new map, Wake Island 2007
- Added reserved slot functionality
- Changed automatic TK banning to ban by cd-key instead of IP address
- Fixed a crash in the Ranked Linux server when communication with stats 
back-end ceased.

v1.02

- Fixed a server memory leak

v1.01

- Various client side fixes