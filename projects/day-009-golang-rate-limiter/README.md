# Day 009: Token Bucket Rate Limiter (Go)

A production-grade rate limiting engine implemented in **Go (Golang) Concurrent Systems & CLI**.

## 📌 Problem Solved
Unregulated API traffic leads to server resource exhaustion, cascading microservice failures, and noisy-neighbor issues. This project implements a mathematically precise Token Bucket algorithm allowing controlled bursts while enforcing steady-state throughput limits.

## 🚀 Key Features
- **Token Bucket Core**: Handles bursts smoothly while continuously refilling tokens.
- **RFC 6585 Compliance**: Emits `X-RateLimit-Limit`, `X-RateLimit-Remaining`, and `Retry-After`.
- **Zero Heavy Dependencies**: Completely self-contained and embeddable.
- **Included Test Suite**: Verifies burst tolerance and recovery timing.

## 🛠️ Quickstart
```bash
# Run tests
cd projects/day-009-golang-rate-limiter
# Check test files inside tests/
```
