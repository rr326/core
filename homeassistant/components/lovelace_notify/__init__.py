"""The Lovelace Notify integration."""
import asyncio
import datetime as dt

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN
import asyncio

# TODO List the platforms that you want to support.
# For your initial PR, limit it to 1 platform.
PLATFORMS = ["app"]
STATE_ENTITY = f"{DOMAIN}.state"


def create_attributes(attributes, text=None):
    now = dt.datetime.now()
    if not text:
        text = f"Message: {now.isoformat()}"
    attributes[now.isoformat()] = text
    return attributes


async def add_message(hass: HomeAssistant):
    cur_state = hass.states.get(STATE_ENTITY)
    cur_attributes = dict(cur_state.attributes) if cur_state else {}
    new_attributes = create_attributes(attributes=cur_attributes)

    hass.states.async_set(
        STATE_ENTITY,
        f"{dt.datetime.now()}",
        attributes=new_attributes,
    )
    print(f"#### lovelace_notify attributes: {new_attributes}")
    await asyncio.sleep(5)
    asyncio.create_task(add_message(hass))


async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Lovelace Notify component."""
    asyncio.create_task(add_message(hass))
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Lovelace Notify from a config entry."""
    # TODO Store an API object for your platforms to access
    # hass.data[DOMAIN][entry.entry_id] = MyApi(...)

    for component in PLATFORMS:
        hass.async_create_task(
            hass.config_entries.async_forward_entry_setup(entry, component)
        )

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    unload_ok = all(
        await asyncio.gather(
            *[
                hass.config_entries.async_forward_entry_unload(entry, component)
                for component in PLATFORMS
            ]
        )
    )
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
