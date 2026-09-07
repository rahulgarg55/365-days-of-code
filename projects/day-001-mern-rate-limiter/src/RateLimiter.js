/**
 * Token Bucket Rate Limiter
 * High-performance, in-memory rate limiter with fractional token refill
 * and RFC 6585 compliance.
 */

class TokenBucket {
  /**
   * @param {number} capacity - Maximum burst capacity of tokens
   * @param {number} refillRate - Tokens added per second
   */
  constructor(capacity, refillRate) {
    if (capacity <= 0 || refillRate <= 0) {
      throw new Error('Capacity and refill rate must be positive numbers');
    }
    this.capacity = capacity;
    this.refillRate = refillRate;
    this.tokens = capacity;
    this.lastRefill = Date.now();
  }

  /**
   * Replenishes tokens based on the elapsed wall-clock time.
   * @private
   */
  _replenish() {
    const now = Date.now();
    const elapsedSeconds = (now - this.lastRefill) / 1000;
    const addedTokens = elapsedSeconds * this.refillRate;
    this.tokens = Math.min(this.capacity, this.tokens + addedTokens);
    this.lastRefill = now;
  }

  /**
   * Attempts to consume tokens.
   * @param {number} tokens - Number of tokens to acquire
   * @returns {{ allowed: boolean, headers: Object }}
   */
  acquire(tokens = 1) {
    this._replenish();

    if (this.tokens >= tokens) {
      this.tokens -= tokens;
      return {
        allowed: true,
        headers: {
          'X-RateLimit-Limit': this.capacity,
          'X-RateLimit-Remaining': Math.floor(this.tokens),
          'X-RateLimit-Reset': Math.ceil((this.lastRefill + 1000) / 1000)
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
        'Retry-After': retryAfter
      }
    };
  }

  /**
   * Connects as standard Express / Node.js middleware.
   * @returns {Function}
   */
  middleware() {
    return (req, res, next) => {
      const result = this.acquire(1);
      Object.entries(result.headers).forEach(([key, val]) => {
        res.setHeader(key, val);
      });

      if (result.allowed) {
        return next();
      }

      return res.status(429).json({
        error: 'Too Many Requests',
        message: 'Rate limit exceeded. Please retry later.',
        retryAfter: result.headers['Retry-After']
      });
    };
  }
}

module.exports = TokenBucket;
