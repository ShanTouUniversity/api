import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import logger, uvicorn_config
from .barcode import barcode_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 或者指定具体域名列表
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有请求头
)

app.include_router(barcode_router)


@app.get("/")
async def root():
    return {"message": "Hello from ShanTou.University Public API!"}


def main() -> int:  # pragma: no cover
    logger.info("Start ... ")
    try:
        uvicorn.run(
            app=uvicorn_config.app,
            host=uvicorn_config.host,
            port=uvicorn_config.port,
            reload=uvicorn_config.reload,
            reload_includes=(
                uvicorn_config.reload_includes
                if uvicorn_config.reload
                else None
            ),
            log_level=uvicorn_config.log_level,
            workers=uvicorn_config.workders,
        )

        return 0
    except KeyboardInterrupt:
        logger.info("Done ...")
        return 1
