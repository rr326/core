from .const import DOMAIN


def ws_send_message(hass, event_type: str, event_data: dict) -> bool:
    """
    Send a websocket message

    event_type = SUB event.
    eg: event_type = "success", websocket event = "ll_notify/success"

    Note this is not marked async, but it is called internally
    as async. (ie: this is non-blocking)

    This is a simple wrapper that all my code should use so if I find a
    more proper way to send messages I can update it here.
    """
    if not event_type.startswith(DOMAIN):
        event_type = f"{DOMAIN}/{event_type}"

    print(f"### ll_notify: send_message: {event_type}")
    hass.bus.fire(
        event_type=event_type,
        event_data=event_data,
    )
    return True