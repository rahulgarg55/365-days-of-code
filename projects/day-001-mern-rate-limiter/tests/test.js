const TokenBucket = require('../src/RateLimiter');

function runTests() {
  console.log('Running TokenBucket Rate Limiter test suite...');

  const limiter = new TokenBucket(3, 1.0); // 3 capacity, 1 token/sec

  // Test burst
  for (let i = 1; i <= 3; i++) {
    const res = limiter.acquire(1);
    console.log(`Request ${i}: allowed=${res.allowed}, remaining=${res.headers['X-RateLimit-Remaining']}`);
    if (!res.allowed) throw new Error(`Request ${i} should have succeeded under burst limit`);
  }

  // 4th request must be throttled
  const throttled = limiter.acquire(1);
  console.log(`Request 4: allowed=${throttled.allowed}, retryAfter=${throttled.headers['Retry-After']}`);
  if (throttled.allowed) throw new Error('Request 4 should have been throttled');

  console.log('✅ All TokenBucket tests passed!');
}

runTests();
