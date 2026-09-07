/**
 * High-Performance In-Memory Token Bucket Rate Limiter
 * Implements fractional token refill and RFC 6585 compliance.
 */
class TokenBucket {
  constructor(capacity, refillRate) {
    if (capacity <= 0 || refillRate <= 0) {
      throw new Error('Capacity and refill rate must be positive numbers');
    }
    this.capacity = capacity;
    this.refillRate = refillRate;
    this.tokens = capacity;
    this.lastRefill = Date.now();
  }

  _replenish() {
    const now = Date.now();
    const elapsedSeconds = (now - this.lastRefill) / 1000;
    const addedTokens = elapsedSeconds * this.refillRate;
    this.tokens = Math.min(this.capacity, this.tokens + addedTokens);
    this.lastRefill = now;
  }

  acquire(tokens = 1) {
    this._replenish();

    if (this.tokens >= tokens) {
      this.tokens -= tokens;
      return {
        allowed: true,
        headers: {
          'X-RateLimit-Limit': this.capacity,
          'X-RateLimit-Remaining': Math.floor(this.tokens),
        }
      };
    }

    const needed = tokens - this.tokens;
    const retryAfter = Math.ceil(needed / this.refillRate);

    return {
      allowed: false,
      headers: {
        'X-RateLimit-Limit': this.capacity,
        'X-RateLimit-Remaining': 0,
        'Retry-After': retryAfter,
      }
    };
  }

  middleware() {
    return (req, res, next) => {
      const result = this.acquire(1);
      Object.entries(result.headers).forEach(([k, v]) => res.setHeader(k, v));
      if (result.allowed) {
        return next();
      }
      return res.status(429).json({
        error: 'Too Many Requests',
        retryAfter: result.headers['Retry-After']
      });
    };
  }
}

module.exports = TokenBucket;
