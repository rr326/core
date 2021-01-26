"""
Automatically insert `ll_notify.js` into the Lovelace frontend.

This trick is taken from here:
https://github.com/thomasloven/hass-browser_mod/blob/master/custom_components/browser_mod/mod_view.py
"""

from aiohttp import web
from homeassistant.components.http import HomeAssistantView
import logging

_LOGGER = logging.getLogger(__name__)

from .const import FRONTEND_SCRIPT_URL, DATA_EXTRA_MODULE_URL, VIEW_NAME, SCRIPT_PATH


async def auto_load_ll_notify_js(hass, config):
    """
    Auto-load ll_notify.js in frontend.
    """
    # Will autoload anything named 'frontend_extra_module_url'
    if DATA_EXTRA_MODULE_URL not in hass.data:
        hass.data[DATA_EXTRA_MODULE_URL] = set()
    hass.data[DATA_EXTRA_MODULE_URL].add(FRONTEND_SCRIPT_URL)

    hass.http.register_view(ModView(hass, FRONTEND_SCRIPT_URL))
    return True


class ModView(HomeAssistantView):

    name = VIEW_NAME
    requires_auth = False

    def __init__(self, hass, url):
        self.url = url

    async def get(self, request):
        try:
            filecontent = SCRIPT_PATH.read_text(encoding="utf-8", errors="ignore")
        except Exception as err:
            _LOGGER.error(f"Unable to read {SCRIPT_PATH}. Err: {err}")
            print(f"Unable to read {SCRIPT_PATH}.")
            filecontent = ""

        return web.Response(
            body=filecontent, content_type="text/javascript", charset="utf-8"
        )
