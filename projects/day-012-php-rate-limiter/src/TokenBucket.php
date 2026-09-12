<?php
declare(strict_types=1);

namespace RateLimiter;

/**
 * Modern PHP 8.2+ Object-Oriented Token Bucket Implementation
 */
final class TokenBucket
{
    private float $tokens;
    private float $lastRefillTimestamp;

    public function __construct(
        public readonly int $capacity,
        public readonly float $refillRatePerSecond
    ) {
        if ($capacity <= 0 || $refillRatePerSecond <= 0) {
            throw new \InvalidArgumentException("Capacity and refill rate must be positive values.");
        }
        $this->tokens = (float) $capacity;
        $this->lastRefillTimestamp = microtime(true);
    }

    private function replenish(): void
    {
        $now = microtime(true);
        $elapsed = $now - $this->lastRefillTimestamp;
        $refill = $elapsed * $this->refillRatePerSecond;
        $this->tokens = min((float) $this->capacity, $this->tokens + $refill);
        $this->lastRefillTimestamp = $now;
    }

    public function consume(int $tokens = 1): array
    {
        $this->replenish();

        if ($this->tokens >= $tokens) {
            $this->tokens -= $tokens;
            return [
                'allowed' => true,
                'headers' => [
                    'X-RateLimit-Limit' => $this->capacity,
                    'X-RateLimit-Remaining' => (int) floor($this->tokens),
                ]
            ];
        }

        $needed = $tokens - $this->tokens;
        $retryAfter = ceil($needed / $this->refillRatePerSecond);

        return [
            'allowed' => false,
            'headers' => [
                'X-RateLimit-Limit' => $this->capacity,
                'X-RateLimit-Remaining' => 0,
                'Retry-After' => (int) $retryAfter,
            ]
        ];
    }
}
