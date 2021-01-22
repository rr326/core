from .ws_out import ws_send_message
from .const import DOMAIN
from functools import partial

DEFAULT_MESSAGE = "DEFAULT MESSAGE - You are probably not calling this properly!"


async def setup_services(hass, config):

    #
    # success, error, warning, message, notify, dismiss_all
    #
    def handle_generic_ws_call(event_type, call):
        """
        Just pass through the websocket data back to the websocket.
        This allows you to have a button or action that does "ll_notify/success" in the UI
        and have that trigger the front end to run a success notification.
        """
        print(f"## handle_{event_type}. data: {call.data}")
        ws_send_message(hass, event_type=event_type, event_data=call.data)

    ws_events = [
        "success",
        "error",
        "warning",
        "message",
        "notify",
        "dismiss_all",
    ]
    for event_type in ws_events:
        handler = partial(handle_generic_ws_call, event_type)
        print(f"Registering websocket listener: {event_type:12} ==> {handler}")
        hass.services.async_register(DOMAIN, event_type, handler)

    #
    # get_defaults
    #
    def handle_get_defaults(call):
        """ Handle ll_notify/get_defaults """
        defaults = config.get(DOMAIN, {}).get("defaults")
        print(f"## handle_get_defaults called. defaults: f{defaults}")
        ws_send_message(hass, event_type="get_defaults", event_data=defaults)

    hass.services.async_register(DOMAIN, "get_defaults", handle_get_defaults)

    #
    # ping
    #
    def handle_ping(call):
        """ Handle ll_notify/ping """
        print(f"## handle_ping called.")
        ws_send_message(hass, event_type="ping", event_data=call.data)

    hass.services.async_register(DOMAIN, "ping", handle_ping)

    #
    # fire_event
    #
    def handle_fire_event(call):
        """ Handle ll_notify/fire_event """
        print(f"## handle_fire_event called. event_data: {call.data}")

        if "event_name" not in call.data:
            print(f"### ERROR - No event_name in fire_event. {call.data}")
            return
        hass.bus.fire(call.data["event_name"], call.data.get("event_data"))

    hass.services.async_register(DOMAIN, "fire_event", handle_fire_event)

    return True