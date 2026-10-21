import pytest
from utils.api_keys import APIKeyRotator, AllKeysExhaustedError, KeyManager


@pytest.mark.asyncio
async def test_api_key_rotator_round_robin_per_request():
    """Verifies that every single request uses a new round-robin key to prevent rate limits."""
    keys = ["key_alpha_12345", "key_beta_67890", "key_gamma_11223"]
    rotator = APIKeyRotator("TestProvider", keys, cooldown_seconds=2.0)

    # Request 1 -> key_alpha
    key1 = await rotator.get_key()
    assert key1 == "key_alpha_12345"
    await rotator.report_success(key1)

    # Request 2 -> key_beta (different key on consecutive request)
    key2 = await rotator.get_key()
    assert key2 == "key_beta_67890"
    await rotator.report_success(key2)

    # Request 3 -> key_gamma
    key3 = await rotator.get_key()
    assert key3 == "key_gamma_11223"
    await rotator.report_success(key3)

    # Request 4 -> loops back to key_alpha
    key4 = await rotator.get_key()
    assert key4 == "key_alpha_12345"


@pytest.mark.asyncio
async def test_api_key_rotator_failover():
    keys = ["key_alpha_12345", "key_beta_67890"]
    rotator = APIKeyRotator("TestProvider", keys, cooldown_seconds=10.0)

    key1 = await rotator.get_key()
    assert key1 == "key_alpha_12345"

    # Alpha fails (e.g. 429 rate limit)
    await rotator.report_failure(key1, error_code=429)

    # Should rotate to Beta
    key2 = await rotator.get_key()
    assert key2 == "key_beta_67890"

    # Beta also fails
    await rotator.report_failure(key2, error_code=429)

    # All keys exhausted
    with pytest.raises(AllKeysExhaustedError):
        await rotator.get_key()


def test_key_manager_singleton():
    km1 = KeyManager.get_instance()
    km2 = KeyManager.get_instance()
    assert km1 is km2
    assert km1.tavily.total_keys >= 2
    assert km1.gemini.total_keys >= 2
    assert km1.groq.total_keys >= 13
    assert km1.firecrawl.total_keys >= 3
    assert km1.jina.total_keys >= 1
