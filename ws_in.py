import asyncio
import datetime as dt

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
import voluptuous as vol

from homeassistant.components import websocket_api
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN, WS_TYPE_MESSAGE
import asyncio
from . import test
from .ws_out import ws_send_message


SCHEMA_WEBSOCKET_MESSAGE = websocket_api.BASE_COMMAND_MESSAGE_SCHEMA.extend(
    {"type": WS_TYPE_MESSAGE, "message": str, "wait": vol.Coerce(float)}
)


@callback
def websocket_handle_message(hass, connection, msg):
    print(f"\n##ws_handle_message: {msg}\n")
    connection.send_message(
        websocket_api.result_message(
            msg["id"], {"response": "success", "orig_msg": msg}
        )
    )

    ws_send_message(
        hass,
        event_type="ll_notify/message",
        event_data={
            "message": msg.get("message", "NO MESSAGE"),
            "wait": msg.get("wait"),
        },
    )
    return True


async def register_handlers(hass):
    hass.components.websocket_api.async_register_command(
        WS_TYPE_MESSAGE, websocket_handle_message, SCHEMA_WEBSOCKET_MESSAGE
    )
    return True
