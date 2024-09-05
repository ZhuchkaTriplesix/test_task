import uvicorn
import config
from configuration.app import App


app = App().app

if __name__ == "__main__":
    uvicorn.run(app, **config.uvicorn.dict())
