import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title='WIN11TWEAKER',
    description='Документация сайта лучшего твикера для WIN11',
    version='18.3',
    openapi_url='/api/openapi.json',
    docs_url='/api/docs',
    swagger_ui_oauth2_redirect_url='/api/docs/oauth2-redirect',
    redoc_url=None,
)


@app.get('/api/v1/sus')
async def sus():
    return {'amogus': 'is_sus'}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', reload=True)  # , log_level='critical')
