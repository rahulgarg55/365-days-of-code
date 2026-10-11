<?php
require_once __DIR__ . '/../src/TokenBucket.php';

use RateLimiter\TokenBucket;

$bucket = new TokenBucket(capacity: 3, refillRatePerSecond: 1.0);

// Burst 3
for ($i = 0; $i < 3; $i++) {
    $res = $bucket->consume(1);
    assert($res['allowed'] === true, "Request " . ($i+1) . " should pass");
}

// 4th request fails
$res = $bucket->consume(1);
assert($res['allowed'] === false, "4th request should be throttled");
echo "PHP TokenBucket Rate Limiter tests passed!\n";
