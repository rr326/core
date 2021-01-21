from .ws_out import ws_send_message
from .const import DOMAIN

DEFAULT_MESSAGE = "DEFAULT MESSAGE - You are probably not calling this properly!"


async def setup_services(hass, config):
    def handle_success(call):
        """ Handle ll_notify/success """
        print(f"## handle_success called. f{call.data}")
        ws_send_message(hass, event_type="success", event_data=call.data)

    def handle_error(call):
        """ Handle ll_notify/error """
        print(f"## handle_error called. f{call.data}")
        ws_send_message(hass, event_type="error", event_data=call.data)

    def handle_warning(call):
        """ Handle ll_notify/warning """
        print(f"## handle_warning called. f{call.data}")
        ws_send_message(hass, event_type="warning", event_data=call.data)

    def handle_message(call):
        """ Handle ll_notify/message """
        print(f"## handle_message called. f{call.data}")
        ws_send_message(hass, event_type="message", event_data=call.data)

    def handle_notify(call):
        """ Handle ll_notify/notify """
        print(f"## handle_notify called. f{call.data}")
        ws_send_message(hass, event_type="success", event_data=call.data)

    def handle_dismiss_all(call):
        """ Handle ll_notify/dismiss_all """
        print(f"## handle_dismiss_all called. ")
        ws_send_message(hass, event_type="dismiss_all", event_data=call.data)

    def handle_get_defaults(call):
        """ Handle ll_notify/get_defaults """

        defaults = config.get(DOMAIN, {}).get("defaults")
        print(f"## handle_get_defaults called. defaults: f{defaults}")
        ws_send_message(hass, event_type="get_defaults", event_data=defaults)

    hass.services.async_register(DOMAIN, "get_defaults", handle_get_defaults)
    hass.services.async_register(DOMAIN, "success", handle_success)
    hass.services.async_register(DOMAIN, "error", handle_error)
    hass.services.async_register(DOMAIN, "warning", handle_warning)
    hass.services.async_register(DOMAIN, "message", handle_message)
    hass.services.async_register(DOMAIN, "notify", handle_notify)
    hass.services.async_register(DOMAIN, "dismiss_all", handle_dismiss_all)

    return True