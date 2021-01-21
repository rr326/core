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


SCHEMA_GET_DEFAULTS = websocket_api.BASE_COMMAND_MESSAGE_SCHEMA.extend(
    {"type": "getDefaults"}
)


@callback
def websocket_handle_get_defaults(hass, connection, msg):
    # Ack
    connection.send_message(
        websocket_api.result_message(
            msg["id"], {"response": "success", "orig_msg": msg}
        )
    )

    print(f"##ws_send setDefaults: {hass.config.get(DOMAIN, {}).get('defaults')}")
    ws_send_message(
        hass,
        event_type="setDefaults",
        event_data=hass.config.get(DOMAIN, {}).get("defaults"),
    )
    return True


async def register_handlers(hass):
    hass.components.websocket_api.async_register_command(
        WS_TYPE_MESSAGE, websocket_handle_get_defaults, SCHEMA_GET_DEFAULTS
    )
    return True
