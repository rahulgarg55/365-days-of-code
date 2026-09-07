const TokenBucket = require('../src/RateLimiter');

const limiter = new TokenBucket(3, 1);

// Test burst
for (let i = 0; i < 3; i++) {
  const res = limiter.acquire(1);
  if (!res.allowed) throw new Error(`Request ${i+1} failed unexpectedly`);
}

// Throttled request
const throttled = limiter.acquire(1);
if (throttled.allowed) throw new Error('Expected 4th request to be throttled');

console.log('✅ RateLimiter tests passed successfully!');
