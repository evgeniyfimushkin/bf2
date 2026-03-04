
------------------------------------------------------------------------------
Release notes: Battlefield 2 free dedicated Linux server
Battlefield 2 is a registered trademark of Digital Illusions CE AB.
(c) 2000-2005 Digital Illusions CE AB
------------------------------------------------------------------------------

Quick start
==============================================================================

- Run the server installer and follow the instructions.

  IMPORTANT:
	Please note that if you choose to install the server over an existing
	installation the existing installation directory will be removed!

  Example:
  $ sh bf2_linuxded-x.y.z-installer.sh

- Modify mods/bf2/settings/serversettings.con to your taste.

  Example:
  $ cd /path/to/installation/bf2
  $ vi mods/bf2/settings/serversettings.con

- Modify mods/bf2/settings/maplist.con to your taste.

  Example:
  $ cd /path/to/installation/bf2
  $ vi mods/bf2/settings/serversettings.con

  IMPORTANT:
    Please see the information below to understand the new map list format.

- Run the server from within the top-level directory by typing
  ./start.sh [arguments] from a shell.

  Example:
  $ cd /path/to/installation/bf2
  $ ./start.sh

- If you are starting the server from a remote connection you will need to
  encapsulate it inside a "screen" session to let it stay behind when you log
  out from the shell.

  Example (to start the server):
  $ cd /path/to/installation/bf2
  $ screen ./start.sh
  Now press Ctrl-A followed by Ctrl-D to detach the screen session, leaving it
  running in the background. You can now log out without affecting the server.

  Example (to reconnect to the server status monitor):
  $ screen -r

  Please see the man page for screen to learn more about what it can do.


More information
==============================================================================

Welcome to the Battlefield 2 dedicated server. For patch-specific
information please refer to the generic read me file included with both the
Linux and win32 distributions.

For discussion with the developers and other users of this server please
subscribe to the bf1942 mailing list. To join the list, send a message to
<bf1942-subscribe@icculus.org> and follow the instructions given to you in the
reply.

If you prefer to use a forum, there is one set up at the distribution site for
the open beta series at http://www.bf1942.lightcubed.com . You can report bugs
both in the forum and on the mailing list. Please don't send bug reports in
private mail, use the forum or the list instead.

BattleRecorder
==============================================================================
See ReadmeServer.txt located in the same directory as this file for information
on what the BattleRecorder can do.
To get this to work on linux you will need to have Python installed on your
machine. You can find python at http://www.python.org.

The file case confusion problem solved
==============================================================================

The BF2 Linux server will read lower-case filenames ONLY. All file names
encountered at runtime are lower-cased before a filesystem access is
attempted. The only exception is Python-scripts. You should therefore make sure 
all files are lower-case when installing third-party modifications and maps.

To aid you with this there is an included python script called
lowercaseDir.py which recursively changes the case of files and directories from
the directory where it's run.

Usage:
lowercaseDir.py <directory> [--pretend] [--verbose]

You can simulate the actions of the script with these options:
 $ ./lowercaseDir.py mods/yourMod --pretend

When you're certain it looks good run the conversion:
 $ ./lowercaseDir.py mods/yourMod --verbose


Known issues
==============================================================================

OVERLAY SERVERS
- You must set sv.allowNATNegotiation to 1 in order to broadcast all instances
  of overlay servers.


Option summary
==============================================================================

The following information was included in the Win32 Server Launcher and is
repeated here for your convenience.

sv.serverName			This is the name your server will be listed by
				in the Internet or LAN server browser.

sv.password			If you set a password, players will need to
				enter it before connecting to your server.

sv.internet			Set this to report your server to the Internet
				server browser list.

sv.maxConnectionType		Players who exceed this limit will n0t be
				allowed to connect to your server.

sv.allowFreeCam			Allow players to use a free-roaming camera
				while waiting to spawn.  Players can activate
				this camera using the JUMP key.

sv.allowExternalViews		Use this to enable or disable the use of 3rd
				person cameras in vehicles.

sv.allowNoseCam			Use this to enable or disable the use of
				nose-cam in certain vehicles (planes/helicopters).

sv.maxPlayers			The maximum number of players allowed on your
				server at once.  This setting also determines
				whether the 16, 32 or 64 player configuration
				of maps is used.

sv.startDelay			This is the amount of time in seconds players
				are kept waiting for the game to start, once
				the minimum number of players has been reached.

sv.endDelay			This is the amount of time in seconds between
				when a round ends and a new round begins.

sv.spawnTime			This is the amount of time in seconds that
				players will wait to spawn in the game again
				after being killed.

sv.manDownTime			This is the amount of time players will
				wait to spawn in the game again after being
				incapacitated and able to be revived by a medic.
				We recommend that this is set to the same value
				as sv.spawnTime.

sv.ticketRatio			You can set the percentage of the normal number
				of tickets you wish to use.

sv.roundsPerMap			Set the number of rounds to complete before the
				map automatically changes to the next on the list.

sv.timeLimit			After this amount of time is reached, the round
				will end.

sv.soldierFriendlyFire		This is the percentage of direct damage that
				soldiers will receive from other players on the
				same team.

sv.vehicleFriendlyFire		This is the percentage of direct damage that
				vehicles will receive from other players on the
				same team.

sv.soldierSplashFriendlyFire	This is the percentage of splash damage that
				soldiers will receive from other players on the
				same team.

sv.vehicleSplashFriendlyFire	This is the percentage of splash damage that
				vehicles will receive from other players on the
				same team.

sv.voteTime			This is the amount of time that a poll such as a
				kick vote or map vote stays open.

sv.minPlayersForVoting		This is the minimum number of votes needed for a
				poll to be successful.

sv.autoRecord			Enable or disable automatic demo recording.

sv.demoDownloadURL		If demo recording is enabled, this should be set
				to the publicly accessible URL where the demo
				files can be downloaded.

sv.autoDemoHook			This is the application or script that is called
				on to manage demo recordings at the end of rounds.

sv.adminScript			Set the path to a custom admin script to run.

sv.hitIndicator			This setting toggles whether or not players
				receive crosshair feedback indicating they have
				hit a target.

sv.numPlayersNeededToStart	The minimum number of players needed for a round
				to begin.  Until this number of players have
				joined, the server stays in a "pre-game" state
				and neither team loses any tickets.

sv.tkPunishEnabled		Enable the system through which players can
				punish teamkillers in an attempt to kick
				them from the server.

sv.tkNumPunishToKick		When punishing is enabled, this sets the
				number of punished teamkills required to be
				kicked from the server.

sv.tkPunishByDefault		This sets whether or not a player is
				automatically punished for a teamkill.

sv.voipEnabled			Enable the use of VOIP for squad communication.

sv.voipServerRemote		Enable the use of an external BF2 VOIP Server,
				thereby disabling the integrated VOIP server.

sv.voipServerRemoteIP		When using an external VOIP server, this should
				be set with it's IP address.

sv.voipServerPort		The VOIP server uses this port to receive BF2
				server data.  When using an external VOIP server,
				this should be set to the port associated with
				the shared password from the VOIP server's
				configuration.

sv.voipBFClientPort		This is the port the BF2 client uses for
				communication with the voip server.

sv.voipBFServerPort		The BF2 server uses this port to communicate
				with the VOIP server.

sv.voipSharedPassword		When using an external VOIP server, this
				should be set to the password associated with
				the VOIP Server port from the VOIP server's
				configuration.

sv.voipQuality			Use this to adjust the quality of VOIP audio.
				Raising the quality level will increase the
				amount of bandwidth your server uses.
				Recommended settings are 5 for LAN and 3 for
				Internet.

sv.gameSpyPort			Your server sends information about settings
				and status through this port.  You only need
				to change this if it is in conflict with
				another port being used on your system.
				For best results, this value should stay
				between 29900 and 29950.

sv.allowNATNegotiation		Allow Network Address Translation negotiation.
				Try this if you use a router or gateway device
				and are having problems hosting a server.

sv.autoBalanceTeam		Enabling this will automatically move players
				to the team with less players when they die,
				and will prevent players from switching teams
				if it would cause then to be too unbalanced.

sv.teamRatioPercent		This ratio represents how autoBalanceTeam
				considers the desired ratio between team 1
				and team 2.  The percent represents what
				percent of team 1's current players is
				considered 'even' for team 2.

sv.sponsorLogoURL		Enter a URL to an image, and it will be
				displayed in the server browser when the
				server is highlighted.  The image must be in
				PNG or JPG format, and should have a 4:1 aspect
				ratio for best results.

sv.svPunkBuster			Enable PunkBuster automatic cheat protection.
				Visit http://www.evenbalance.com for more
				information about PunkBuster.

sv.useGlobalRank		This setting toggles whether or not players can
				use and show their official rank they have
				earned by playing on ranked servers.

sv.useGlobalUnlocks		This setting toggles whether or not players can
				use the unlocks they have earned by playing on
				ranked servers.

sv.welcomeMessage		This text is displayed on the map load screen
				when connecting to the server.

sv.serverIP			This setting allows you to set the network
				interface IP address for your server.

sv.serverPort			This setting allows you to customize the port
				used for gameplay network traffic.

sv.votingEnabled		Enable or disable voting.

sv.communityLogoURL		Enter a URL to an image, and it will be
				displayed in the loading screen when connecting
				to the server.  The image must be in PNG or JPG
				format, and should have a 4:1 aspect ratio for
				best results.

sv.demoQuality			Set the quality of demo recording, if enabled,
				on the server.  INCREASING THE VALUE OF THIS
				SETTING WILL SEVERLY IMPACT THE PERFORMANCE OF
				THIS SERVER.



Have fun with your Linux server!

Andreas Andersson <andreas.andersson@dice.se>


Licensing information
==============================================================================

The Battlefield 2 server is linked with the GNU C and C++ libraries which
are under the LGPL license. By linking dynamically we ensure that you as a
user can use this software with other versions of these libraries.

A statically linked binary also linked with these libraries is supplied purely
for convenience should you not be able to run the dynamically linked binary.

The LGPL license text is included with this release and can be found on the
web at http://www.gnu.org/licenses/lgpl.html.

Please note that the Battlefield 2 dedicated server itself is not covered
by the LGPL license.


==============================================================================
Revision history
==============================================================================



==============================================================================
DICE Copyright

Copyright © 2002-2005 Digital Illusions CE AB. 

ALL RIGHTS RESERVED.
==============================================================================
