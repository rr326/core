def ws_send_message(hass, event_type, event_data):
    """
    Send a websocket message

    Note this is not marked async, but it is called internally
    as async. (ie: this is non-blocking)

    This is a simple wrapper that all my code should use so if I find a
    more proper way to send messages I can update it here.
    """
    print("### ll_notify: send_message:  ll_notify/message")
    hass.bus.async_fire(
        event_type=event_type,
        event_data=event_data,
    )
    return True