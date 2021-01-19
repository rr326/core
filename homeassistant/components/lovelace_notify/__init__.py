"""The Lovelace Notify integration."""
import asyncio
import datetime as dt

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
import voluptuous as vol

from homeassistant.components import websocket_api
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN, WS_TYPE_MESSAGE
import asyncio


SCHEMA_WEBSOCKET_MESSAGE = websocket_api.BASE_COMMAND_MESSAGE_SCHEMA.extend(
    {"type": WS_TYPE_MESSAGE, "message": str, "wait": vol.Coerce(float)}
)


async def send_message(hass):
    print("### ll_notify: send_message:  ll_notify/message")
    hass.bus.async_fire(
        event_type="ll_notify/message",
        event_data={"message": "Send Message Every 5 Seconds", "wait": 10},
    )

    await asyncio.sleep(5)
    await asyncio.create_task(send_message(hass))


@callback
def websocket_handle_message(hass, connection, msg):
    print(f"\n##ws_handle_message: {msg}\n")
    connection.send_message(
        websocket_api.result_message(
            msg["id"], {"response": "success", "orig_msg": msg}
        )
    )


async def async_setup(hass: HomeAssistant, config: dict):
    hass.components.websocket_api.async_register_command(
        WS_TYPE_MESSAGE, websocket_handle_message, SCHEMA_WEBSOCKET_MESSAGE
    )
    hass.async_add_job(send_message(hass))

    return True
