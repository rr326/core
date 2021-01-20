# Lovelace Notify


## HomeAssistant PR/Feedback
* [docs wrong: to_write](https://developers.home-assistant.io/docs/frontend/extending/websocket-api) - this is incorrect. Probably an old api. (There IS a `._to_write` but that is now clearly intended to be internal). I've used `hass.bus.async_fire`