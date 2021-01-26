# Dev Notes

## TODO
* Implewment services.yaml

## HomeAssistant PR/Feedback
* [docs wrong: to_write](https://developers.home-assistant.io/docs/frontend/extending/websocket-api) - this is incorrect. Probably an old api. (There IS a `._to_write` but that is now clearly intended to be internal). I've used `hass.bus.async_fire`

## Misc
* Making the screen recording gif:
    1. Screen capture: Sh-Cmd-5
    2. Imovie
    3. `ffmpeg -i ~/Desktop/ll_notify.mp4 -filter:v scale=720:-1   -f gif - | gifsicle --optimize=3 --delay=3 > screenshot.gif`