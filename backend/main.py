import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse


app = FastAPI(
    title='WIN11TWEAKER',
    description='Документация сайта лучшего твикера для WIN11',
    version='18.3',
    openapi_url='/docs/openapi.json',
    default_response_class=ORJSONResponse,
    docs_url='/docs',
    redoc_url=None,
)


@app.get('/api/v1/sus')
async def sus():
    return {'amogus': 'is_sus'}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', reload=True)  # , log_level='critical')
