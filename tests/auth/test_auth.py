import jose.jwt
import pytest
from src.config import settings
from src.auth.utils import create_access_token


@pytest.mark.asyncio
async def test_create_access_token():
    token = create_access_token({"sub": "test"})
    assert token is not None
    decode_token = jose.jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    assert decode_token is not None
    assert decode_token.get("sub") == "test"
