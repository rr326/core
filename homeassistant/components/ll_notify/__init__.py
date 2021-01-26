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
from . import test
from .services import setup_services
from .ws_out import ws_send_message
from .serve_js import auto_load_ll_notify_js


async def async_setup(hass: HomeAssistant, config: dict):
    await setup_services(hass, config)
    await hass.services.async_call(DOMAIN, "get_defaults")
    await auto_load_ll_notify_js(hass, config)

    # hass.async_add_job(test.send_every_five(hass))

    return True
