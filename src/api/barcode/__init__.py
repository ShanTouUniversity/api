from fastapi import APIRouter

barcode_router = APIRouter(
    prefix="/barcode",
    tags=["Barcode"],
)

from .barcode import router

barcode_router.include_router(router)
