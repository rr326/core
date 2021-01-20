import asyncio


async def send_every_five(hass):
    print("### ll_notify: send_message:  ll_notify/message")
    hass.bus.async_fire(
        event_type="ll_notify/message",
        event_data={"message": "Send Message Every 5 Seconds", "wait": 10},
    )

    await asyncio.sleep(5)
    await asyncio.create_task(send_every_five(hass))
