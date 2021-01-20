from .ws_out import ws_send_message
from .const import DOMAIN

DEFAULT_MESSAGE = "DEFAULT MESSAGE - You are probably not calling this properly!"


async def setup_services(hass, config):
    def handle_success(call):
        """Handle ll_notify/success"""
        print(f"## handle_success called. f{call.data}")
        ws_send_message(
            hass,
            event_type="success",
            event_data={
                "message": call.data.get("message", DEFAULT_MESSAGE),
                "wait": call.data.get("wait"),
            },
        )

    hass.services.async_register(DOMAIN, "success", handle_success)

    return True