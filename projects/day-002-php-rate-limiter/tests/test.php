<?php
declare(strict_types=1);

require_once __DIR__ . '/../src/RateLimiter.php';

use RateLimiter\RateLimiter;

echo "Running PHP RateLimiter test suite...\n";

$limiter = new RateLimiter(capacity: 3, refillRatePerSecond: 1.0);

// Burst 3
for ($i = 1; $i <= 3; $i++) {
    $res = $limiter->consume(1);
    echo "Request $i: allowed=" . ($res['allowed'] ? 'true' : 'false') . ", remaining=" . $res['headers']['X-RateLimit-Remaining'] . "\n";
    assert($res['allowed'] === true, "Request $i should be allowed under burst capacity");
}

// 4th request must be throttled
$res = $limiter->consume(1);
echo "Request 4: allowed=" . ($res['allowed'] ? 'true' : 'false') . ", retryAfter=" . $res['headers']['Retry-After'] . "\n";
assert($res['allowed'] === false, "Request 4 must be throttled");

echo "✅ All PHP RateLimiter tests passed!\n";
