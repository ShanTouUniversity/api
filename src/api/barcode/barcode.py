from io import BytesIO

import barcode
import barcode.writer
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from .models import (
    PZN7,
    Code39,
    Code128,
    EuropeanArticleNumber8,
    EuropeanArticleNumber13,
    EuropeanArticleNumber14,
    Gs1_128,
    InternationalStandardBookNumber10,
    InternationalStandardBookNumber13,
    InternationalStandardSerialNumber,
    JapanArticleNumber,
    UniversalProductCodeA,
)

# python-barcode 支持的条形码格式
# __BARCODE_MAP = {
#     "ean8": EAN8,
#     "ean8-guard": EAN8_GUARD,
#     "ean13": EAN13,
#     "ean13-guard": EAN13_GUARD,
#     "ean": EAN13,
#     "gtin": EAN14,
#     "ean14": EAN14,
#     "jan": JAN,
#     "upc": UPCA,
#     "upca": UPCA,
#     "isbn": ISBN13,
#     "isbn13": ISBN13,
#     "gs1": ISBN13,
#     "isbn10": ISBN10,
#     "issn": ISSN,
#     "code39": Code39,
#     "pzn": PZN,
#     "code128": Code128,
#     "itf": ITF,
#     "gs1_128": Gs1_128,
#     "codabar": CODABAR,
#     "nw-7": CODABAR,
# }

SUPPORTED_CODE_FORMATS = [
    "ean8",
    "ean8-guard",
    "ean13",
    "ean13-guard",
    "ean",
    "gtin",
    "ean14",
    "jan",
    "upc",
    "upca",
    "isbn",
    "isbn13",
    "gs1",
    "isbn10",
    "issn",
    "code39",
    "pzn",
    "code128",
    "itf",
    "gs1_128",
    "codabar",
    "nw-7",
]  # 支持的条形码类型

SUPPORTED_RESULT_FORMATS = ["png", "svg"]


router = APIRouter()


# Code39(code: str, writer=None, add_checksum: bool = True)
@router.api_route("/code39", methods=["GET", "HEAD", "OPTIONS"])
async def generate_code39(
    code: str,
    add_checksum: bool = False,
):
    try:
        code39 = Code39(code=code, add_checksum=add_checksum)
    except Exception as e:
        raise HTTPException(400, detail=str(e)) from e

    try:
        output = generate_barcode_image(
            code39.code, "code39", add_checksum=code39.add_checksum
        )
    except Exception as e:
        raise HTTPException(500, detail=str(e)) from e

    return StreamingResponse(output, media_type="image/png")


# Code128(code, writer=None)
@router.api_route("/code128", methods=["GET", "HEAD", "OPTIONS"])
async def generate_code128(code: str):
    try:
        code128 = Code128(code=code)
    except Exception as e:
        raise HTTPException(400, detail=str(e)) from e

    try:
        output = generate_barcode_image(code128.code, "code128")
    except Exception as e:
        raise HTTPException(500, detail=str(e)) from e

    return StreamingResponse(output, media_type="image/png")


# PZN7(pzn, writer=None)
@router.api_route("/pzn7", methods=["GET", "HEAD", "OPTIONS"])
async def generate_pzn7(code: str):
    try:
        pzn7 = PZN7(code=code)
    except Exception as e:
        raise HTTPException(400, detail=str(e)) from e

    try:
        output = generate_barcode_image(pzn7.code, "pzn")
    except Exception as e:
        raise HTTPException(500, detail=str(e)) from e

    return StreamingResponse(output, media_type="image/png")


# EuropeanArticleNumber13(ean, writer=None, no_checksum=False, guardbar=False)
@router.api_route("/ean13", methods=["GET", "HEAD", "OPTIONS"])
async def generate_ean13(
    code: str, no_checksum: bool = False, guardbar: bool = False
):
    try:
        ean13 = EuropeanArticleNumber13(
            code=code, no_checksum=no_checksum, guardbar=guardbar
        )
    except Exception as e:
        raise HTTPException(400, detail=str(e)) from e

    try:
        output = generate_barcode_image(
            ean13.code, "ean13", add_checksum=ean13.no_checksum
        )
    except Exception as e:
        raise HTTPException(500, detail=str(e)) from e

    return StreamingResponse(output, media_type="image/png")


# EuropeanArticleNumber8(ean, writer=None, no_checksum=False, guardbar=False)
@router.api_route("/ean8", methods=["GET", "HEAD", "OPTIONS"])
async def generate_ean8(
    code: str, no_checksum: bool = False, guardbar: bool = False
):
    try:
        ean8 = EuropeanArticleNumber8(
            code=code, no_checksum=no_checksum, guardbar=guardbar
        )
    except Exception as e:
        raise HTTPException(400, detail=str(e)) from e

    try:
        output = generate_barcode_image(
            ean8.code, "ean8", add_checksum=ean8.no_checksum
        )
    except Exception as e:
        raise HTTPException(500, detail=str(e)) from e

    return StreamingResponse(output, media_type="image/png")


# JapanArticleNumber(jan, *args, **kwargs)
@router.api_route("/jan", methods=["GET", "HEAD", "OPTIONS"])
async def generate_jan(code: str):
    try:
        jan = JapanArticleNumber(code=code)
    except Exception as e:
        raise HTTPException(400, detail=str(e)) from e

    try:
        output = generate_barcode_image(jan.code, "jan")
    except Exception as e:
        raise HTTPException(500, detail=str(e)) from e

    return StreamingResponse(output, media_type="image/png")


# InternationalStandardBookNumber13(isbn, writer=None)
@router.api_route("/isbn13", methods=["GET", "HEAD", "OPTIONS"])
async def generate_isbn13(code: str):
    try:
        isbn13 = InternationalStandardBookNumber13(code=code)
    except Exception as e:
        raise HTTPException(400, detail=str(e)) from e

    try:
        output = generate_barcode_image(isbn13.code, "isbn13")
    except Exception as e:
        raise HTTPException(500, detail=str(e)) from e

    return StreamingResponse(output, media_type="image/png")


# InternationalStandardBookNumber10(isbn, writer=None)
@router.api_route("/isbn10", methods=["GET", "HEAD", "OPTIONS"])
async def generate_isbn10(code: str):
    try:
        isbn10 = InternationalStandardBookNumber10(code=code)
    except Exception as e:
        raise HTTPException(400, detail=str(e)) from e

    try:
        output = generate_barcode_image(isbn10.code, "isbn10")
    except Exception as e:
        raise HTTPException(500, detail=str(e)) from e

    return StreamingResponse(output, media_type="image/png")


# InternationalStandardSerialNumber(issn, writer=None)
@router.api_route("/issn", methods=["GET", "HEAD", "OPTIONS"])
async def generate_issn(code: str):
    try:
        issn = InternationalStandardSerialNumber(code=code)
    except Exception as e:
        raise HTTPException(400, detail=str(e)) from e

    try:
        output = generate_barcode_image(issn.code, "issn")
    except Exception as e:
        raise HTTPException(500, detail=str(e)) from e

    return StreamingResponse(output, media_type="image/png")


# UniversalProductCodeA(upc, writer=None, make_ean=False)
@router.api_route("/upc", methods=["GET", "HEAD", "OPTIONS"])
async def generate_upc(code: str, make_ean: bool = False):
    try:
        upc = UniversalProductCodeA(code=code, make_ean=make_ean)
    except Exception as e:
        raise HTTPException(400, detail=str(e)) from e

    try:
        output = generate_barcode_image(upc.code, "upc")
    except Exception as e:
        raise HTTPException(500, detail=str(e)) from e

    return StreamingResponse(output, media_type="image/png")


# EuropeanArticleNumber14(ean, writer=None, no_checksum=False, guardbar=False)
@router.api_route("/ean14", methods=["GET", "HEAD", "OPTIONS"])
async def generate_ean14(
    code: str, no_checksum: bool = False, guardbar: bool = False
):
    try:
        ean14 = EuropeanArticleNumber14(
            code=code, no_checksum=no_checksum, guardbar=guardbar
        )
    except Exception as e:
        raise HTTPException(400, detail=str(e)) from e

    try:
        output = generate_barcode_image(
            ean14.code, "ean14", add_checksum=ean14.no_checksum
        )
    except Exception as e:
        raise HTTPException(500, detail=str(e)) from e

    return StreamingResponse(output, media_type="image/png")


# Gs1_128(code, writer=None)
@router.api_route("/gs1_128", methods=["GET", "HEAD", "OPTIONS"])
async def generate_gs1_128(code: str):
    try:
        gs1_128 = Gs1_128(code=code)
    except Exception as e:
        raise HTTPException(400, detail=str(e)) from e

    try:
        output = generate_barcode_image(gs1_128.code, "gs1_128")
    except Exception as e:
        raise HTTPException(500, detail=str(e)) from e

    return StreamingResponse(output, media_type="image/png")


def generate_barcode_image(
    code: str,
    code_name: str,
    add_checksum: bool = True,
    no_checksum: bool = False,
    guardbar: bool = False,
    make_ean: bool = False,
) -> BytesIO:
    """
    在非异步线程中生成条形码图片流

    :param code: 条形码内容
    :param code_name: 条形码格式，参见 SUPPORTED_CODE_FORMATS
    :param add_checksum: 是否启用校验和，仅适用于 code39 格式
    :param no_checksum: 是否启用校验和，仅适用于 ean8/ean13/ean14 格式
    :param guardbar: 是否启用校验和，仅适用于 ean8/ean13/ean14 格式
    :param make_ean: 是否启用校验和，仅适用于 upc 格式
    :return: 条形码图片流
    """
    # 创建条形码类实例
    barcode_class = barcode.get_barcode_class(code_name)

    # 创建内存中的图片流
    output = BytesIO()
    writer = barcode.writer.ImageWriter()

    # 生成条形码并写入内存
    if code_name in ["code39"]:
        barcode_instance = barcode_class(
            code, writer=writer, add_checksum=add_checksum
        )

    elif code_name in ["upc"]:
        barcode_instance = barcode_class(code, writer=writer, make_ean=make_ean)
    elif code_name in ["ean14", "ean8", "ean13"]:
        barcode_instance = barcode_class(
            code, no_checksum=no_checksum, guardbar=guardbar
        )

    elif code_name in [
        "gs1_128",
        "issn",
        "isbn10",
        "isbn13",
        "jan",
        "pzn",
        "code128",
    ]:
        barcode_instance = barcode_class(code, writer=writer)
    else:
        raise ValueError(f"Unsupported code format: {code_name}")

    barcode_instance.write(output)

    # 将指针移动到流的开头
    output.seek(0)
    return output
