import asyncio
from .const import DOMAIN


async def send_every_five(hass):
    print("### TEST: from server")
    # hass.bus.async_fire(
    #     event_type="ll_notify/success",
    #     event_data={"message": "Send Message Every 5 Seconds", "wait": 10},
    # )
    await hass.services.async_call(
        DOMAIN, "success", {"message": "TEST: from SERVER", "wait": 5}
    )

    await asyncio.sleep(5)
    await asyncio.create_task(send_every_five(hass))
