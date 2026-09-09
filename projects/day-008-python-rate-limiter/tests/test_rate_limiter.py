import time
from src.rate_limiter import TokenBucket

def test_token_bucket():
    # Capacity 5, refill 2 tokens/sec
    limiter = TokenBucket(capacity=5, refill_rate=2.0)
    
    # Burst 5 requests
    for i in range(5):
        allowed, headers = limiter.acquire(1)
        assert allowed is True, f"Request {i+1} should be permitted"

    # 6th request should be denied
    allowed, headers = limiter.acquire(1)
    assert allowed is False, "Request 6 should exceed bucket capacity"
    assert "Retry-After" in headers

    # Wait 0.6 seconds (replenishes ~1.2 tokens)
    time.sleep(0.6)
    allowed, headers = limiter.acquire(1)
    assert allowed is True, "Request after refill should be permitted"
    print("All Rate Limiter tests passed successfully!")

if __name__ == "__main__":
    test_token_bucket()
