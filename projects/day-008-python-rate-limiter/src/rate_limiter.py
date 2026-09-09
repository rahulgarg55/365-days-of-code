"""
Token Bucket Rate Limiter
A high-precision, thread-safe rate limiter implementing fractional token refill.
"""

import time
import threading
from typing import Tuple, Dict, Any, Optional

class TokenBucket:
    """
    Thread-safe Token Bucket Rate Limiter.
    Allows bursts up to `capacity` tokens, replenishing at `refill_rate` tokens per second.
    """
    def __init__(self, capacity: int, refill_rate: float):
        if capacity <= 0 or refill_rate <= 0:
            raise ValueError("Capacity and refill rate must be positive values")
        self.capacity = float(capacity)
        self.refill_rate = float(refill_rate)
        self.tokens = float(capacity)
        self.last_refill = time.monotonic()
        self._lock = threading.Lock()

    def _refill(self, now: float) -> None:
        elapsed = now - self.last_refill
        refill_amount = elapsed * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + refill_amount)
        self.last_refill = now

    def acquire(self, tokens: int = 1) -> Tuple[bool, Dict[str, Any]]:
        """
        Attempts to acquire `tokens`.
        Returns a tuple of (allowed: bool, headers: dict) conforming to RFC 6585.
        """
        with self._lock:
            now = time.monotonic()
            self._refill(now)

            if self.tokens >= tokens:
                self.tokens -= tokens
                return True, {
                    "X-RateLimit-Limit": int(self.capacity),
                    "X-RateLimit-Remaining": int(self.tokens),
                    "X-RateLimit-Reset": int(self.last_refill + (1.0 / self.refill_rate))
                }
            
            # Calculate wait time until enough tokens are replenished
            needed = tokens - self.tokens
            retry_after = needed / self.refill_rate
            return False, {
                "X-RateLimit-Limit": int(self.capacity),
                "X-RateLimit-Remaining": 0,
                "Retry-After": round(retry_after, 2)
            }
