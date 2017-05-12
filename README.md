# Eurovison 2017 entertainment using a C.H.I.P.

A small project to play a song (in this case "Yodel it" from Romania) whenever someone enters the bathroom and turns on the lights.

 ## How to make it work

1. Use a C.H.I.P or similar device.
2. Connect a photoresistor to a `GPIO pin` and `GRND`.
3. Configure the `PIN` and `MUSIC_FILE` constants in mgp.py to suit your needs.
4. Run the application with sudo privileges in a terminal multiplexer like tmux or screen.
5. Connect a speaker to the C.H.I.P. aux port.
