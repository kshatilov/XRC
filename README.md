# XRC
eXtended Reality Coliseum (XRC)

Master UI for collaborative XR experiences 

1. Dota 2 */dota2/*

Displays:
 - any visual interpretation of Dota 2 minimap (*/res/map/*);
 - AR markers for T1-T2-T3 towers for betting and the AR-app;
 - dynamic AR markers for location of the heroes;
 - players's (and teams) webcam footage (as well as URI/QR of each video stream);
 - dynamic light-weight connections between player's video footage and hero's location on the map;
 - dynamic AR marker for the observer's (or player's) camera.

Controls:
 - start/pause/restart for the entire scene;
 - -/+1(5) seconds scrolling;
 - change frame to the video-stream (based on players attention);
 - change layout of the minimap (simplistic, 3D-terrain etc);
 -   

Depedent on the following micro-services:
 (a) TODO replay parser;
 (b) AR-markers shared lib;
 (c) 3rd party observers and video stream providers;
    https://www.twitch.tv/videos/10046399

2. Horse racing */horse_racing/*

Displays:
 - any visual interpretation of a Hippodrome;
 - AR markers for tuples of (horse, jockey) for betting and the AR-app;
 - dynamic AR markers for location of the horses;
 - available footage (as well as URI/QR of each video stream);
 - dynamic light-weight connections between video footage and horse's location on the map;
 - dynamic AR marker for the main camera position and focus vector.

Controls:
 - start/pause/restart for the entire scene;
 - size/rotation/offset of the hippodrome for the entire scene;


Depedent on the following micro-services:
 (a) *g_server.py @ localhost:1488* that parses racing videos given the tracking boxes;
 (b) AR-markers shared lib;
 (c) 3rd party observers and video stream providers;
    
    TODO get .png from procreate 




