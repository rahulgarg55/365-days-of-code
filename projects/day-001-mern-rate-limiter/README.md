# Day 001: Token Bucket Rate Limiter (MERN)

> A resilient, production-ready rate limiting engine implemented in MERN / Node.js & React Full-Stack.

## 📌 Problem Solved
Public APIs face denial of service and resource exhaustion when clients make unregulated bursts of requests. This project implements a mathematically precise Token Bucket rate limiter that allows controlled bursts while guaranteeing long-term traffic smoothing.

## 🚀 Key Features
- **Token Bucket Algorithm**: Handles bursts smoothly while refilling tokens continuously.
- **Persistence**: Persists state across restarts using transactional SQLite.
- **RFC 6585 Headers**: Outputs `X-RateLimit-Limit`, `X-RateLimit-Remaining`, and `Retry-After`.
- **Zero Heavy Dependencies**: Completely lightweight and easy to embed.

## 🛠️ Quickstart
```bash
# Clone and run
cd projects/day-001-mern-rate-limiter
# Check script instructions inside src/
```
