import pydantic


class Code39(pydantic.BaseModel):
    code: str
    add_checksum: bool = False

    @pydantic.field_validator("code")
    def valid_code(cls, code: str) -> str:
        valid_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.$/+%*"
        if not all(char in valid_chars for char in code):
            raise ValueError("Code contains invalid characters.")
        return code


class Code128(pydantic.BaseModel):
    code: str

    @pydantic.field_validator("code")
    def valid_code(cls, code: str) -> str:
        # Code 128 allows all ASCII characters from 0 to 127
        if not all(0 <= ord(char) <= 127 for char in code):
            raise ValueError("Code contains invalid characters.")
        return code


class PZN7(pydantic.BaseModel):
    code: str

    @pydantic.field_validator("code")
    def valid_code(cls, code: str) -> str:
        if not code.isdigit() or len(code) != 7:
            raise ValueError("Code must be a 7-digit number.")
        return code


class EuropeanArticleNumber13(pydantic.BaseModel):
    code: str
    no_checksum: bool = False
    guardbar: bool = False

    @pydantic.field_validator("code")
    def valid_code(cls, code: str) -> str:
        # EAN-13 code must be exactly 13 digits long
        # and contain only numeric characters
        if not code.isdigit() or len(code) != 13:
            raise ValueError("Code must be a 13-digit numeric string.")
        return code


class EuropeanArticleNumber8(pydantic.BaseModel):
    code: str
    no_checksum: bool = False
    guardbar: bool = False

    @pydantic.field_validator("code")
    def valid_code(cls, code: str) -> str:
        # EAN-8 code must be exactly 8 digits long and
        # contain only numeric characters
        if not code.isdigit() or len(code) != 8:
            raise ValueError("Code must be an 8-digit numeric string.")
        return code


class JapanArticleNumber(pydantic.BaseModel):
    code: str

    @pydantic.field_validator("code")
    def valid_code(cls, code: str) -> str:
        # JAN code must be either 8 or 13 digits long
        # and contain only numeric characters
        if not code.isdigit() or (len(code) != 8 and len(code) != 13):
            raise ValueError("Code must be an 8 or 13-digit numeric string.")
        return code


class InternationalStandardBookNumber13(pydantic.BaseModel):
    code: str

    @pydantic.field_validator("code")
    def valid_code(cls, code: str) -> str:
        # Remove hyphens from the code
        cleaned_code = code.replace("-", "")

        # ISBN-13 code must be exactly 13 digits long
        # and contain only numeric characters
        if not cleaned_code.isdigit() or len(cleaned_code) != 13:
            raise ValueError(
                "Code must be a 13-digit numeric string, \
                    optionally separated by hyphens."
            )

        return code


class InternationalStandardBookNumber10(pydantic.BaseModel):
    code: str

    @pydantic.field_validator("code")
    def valid_code(cls, code: str) -> str:
        # Remove hyphens from the code
        cleaned_code = code.replace("-", "")

        # ISBN-10 code must be exactly 10 characters long
        if len(cleaned_code) != 10:
            raise ValueError(
                "Code must be a 10-character string, \
                    optionally separated by hyphens."
            )

        # The first 9 characters must be digits
        if not cleaned_code[:9].isdigit():
            raise ValueError("The first 9 characters must be digits.")

        # The last character must be a digit or 'X'
        if not (cleaned_code[-1].isdigit() or cleaned_code[-1] == "X"):
            raise ValueError("The last character must be a digit or 'X'.")

        return code


class InternationalStandardSerialNumber(pydantic.BaseModel):
    code: str

    @pydantic.field_validator("code")
    def valid_code(cls, code: str) -> str:
        # Remove hyphens from the code
        cleaned_code = code.replace("-", "")

        # ISSN code must be exactly 8 characters long
        if len(cleaned_code) != 8:
            raise ValueError(
                "Code must be an 8-character string, \
                    optionally separated by hyphens."
            )

        # The first 7 characters must be digits
        if not cleaned_code[:7].isdigit():
            raise ValueError("The first 7 characters must be digits.")

        # The last character must be a digit or 'X'
        if not (cleaned_code[-1].isdigit() or cleaned_code[-1] == "X"):
            raise ValueError("The last character must be a digit or 'X'.")

        return code


class UniversalProductCodeA(pydantic.BaseModel):
    code: str
    make_ean: bool = False

    @pydantic.field_validator("code")
    def valid_code(cls, code: str) -> str:
        # UPC-A code must be exactly 12 digits long
        # and contain only numeric characters
        if not code.isdigit() or len(code) != 12:
            raise ValueError("Code must be a 12-digit numeric string.")
        return code


class EuropeanArticleNumber14(pydantic.BaseModel):
    code: str
    no_checksum: bool = False
    guardbar: bool = False

    @pydantic.field_validator("code")
    def valid_code(cls, code: str) -> str:
        # EAN-14 code must be exactly 14 digits long
        # and contain only numeric characters
        if not code.isdigit() or len(code) != 14:
            raise ValueError("Code must be a 14-digit numeric string.")
        return code


class Gs1_128(pydantic.BaseModel):
    code: str

    @pydantic.field_validator("code")
    def valid_code(cls, code: str) -> str:
        # GS1-128 code must be a non-empty string and can contain alphanumeric
        # characters and special characters
        if not code:
            raise ValueError("Code must not be empty.")

        # GS1-128 code typically starts with
        # a function code (AI) followed by data
        # For simplicity, we'll just check
        # if the code contains valid characters
        valid_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        if not all(char in valid_chars for char in code):
            raise ValueError("Code contains invalid characters.")

        return code
