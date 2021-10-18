from fastapi.applications import FastAPI

from weather import AppBuilder, Settings

# load settings from .env file or environment variables
settings = Settings()
app: FastAPI = AppBuilder(settings).build()

 
if __name__ == '__main__':
    # in case of running python main.py
    import asyncio

    import uvloop
    from hypercorn.config import Config
    from hypercorn.asyncio import serve

    uvloop.install()

    config = Config()
    config.bind = ['0.0.0.0:8000']
    config.use_reloader = True

    asyncio.run(serve(app, config))
