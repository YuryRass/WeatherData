import asyncio

from weather.handler import get_weather_handler


async def main():
    handler = get_weather_handler()
    await asyncio.gather(
        handler.export_to_excel_with_input_command(),
        handler.periodic_save_weather_data(),
    )


if __name__ == "__main__":
    asyncio.run(main())
