"""
Tech stack configurations and rotation patterns for the 365 Days of Code Engine.
"""

from typing import List, Dict, Any

# Primary tech stacks rotating through days
TECH_STACKS: List[Dict[str, Any]] = [
    {
        "id": "mern",
        "name": "MERN / Node.js & React Full-Stack",
        "category": "Full-Stack Web & Real-Time",
        "primary_languages": ["JavaScript", "TypeScript", "HTML/CSS"],
        "recommended_tools": ["Express", "React", "MongoDB / Mongoose / In-memory DB", "Socket.io", "TailwindCSS/CSS Modules"],
        "archetypes": [
            "Real-time event notification hub with WebSockets",
            "Rate-limited developer API gateway with JWT rotation",
            "Collaborative multi-user state synchronizer / whiteboard backplane",
            "Time-series log stream aggregator and real-time dashboard",
            "Distributed task orchestrator with dead-letter queue",
            "Encrypted secret sharing vault with auto-expiring links",
            "Markdown knowledge-base engine with instant full-text search",
            "Webhook ingestion pipeline with signature verification and retry ledger"
        ],
        "guidelines": "Build a modular client/server structure (or unified full-stack service). Include a working backend API and an intuitive, clean frontend interface."
    },
    {
        "id": "php",
        "name": "PHP Modern (OOP & Micro-Service)",
        "category": "Backend Engineering & Systems",
        "primary_languages": ["PHP", "SQL"],
        "recommended_tools": ["PHP 8.2+", "PDO SQLite", "Composer PSR-4", "cURL", "CLI or lightweight Router"],
        "archetypes": [
            "HMAC-SHA256 webhook dispatcher with replay attack protection",
            "Token-bucket rate limiter with SQLite persistence and middleware design",
            "Multi-tenant invoice and tax calculation engine with PDF/HTML export",
            "Zero-dependency PSR-7/PSR-15 style HTTP router and middleware pipeline",
            "Background job queue worker utilizing SQLite locking mechanisms",
            "Role-Based Access Control (RBAC) engine with granular permission matrix",
            "Audit trail logger capturing state diffs and cryptographic checksums",
            "S3-compatible multi-part file upload chunker and verification tool"
        ],
        "guidelines": "Emphasize modern object-oriented PHP (types, readonly classes, PSR-4 autoloading, dependency injection). Avoid archaic procedural spaghetti. Include zero-setup SQLite or standalone CLI runner."
    },
    {
        "id": "python",
        "name": "Python / FastAPI / Async Systems",
        "category": "High-Performance APIs & Automation",
        "primary_languages": ["Python"],
        "recommended_tools": ["FastAPI", "Pydantic v2", "Uvicorn", "AsyncIO", "SQLite / SQLModel", "httpx"],
        "archetypes": [
            "Distributed circuit breaker middleware for resilient microservice calls",
            "SSL certificate expiration & HTTP endpoint health surveillance worker",
            "Git repository changelog parser and semantic versioning recommender",
            "Inverted index search engine with BM25 ranking algorithm",
            "Asynchronous web scraper with token bucket throttler and robots.txt compliance",
            "System performance telemetry daemon publishing Prometheus-compatible metrics",
            "Dynamic feature flag evaluation engine with cohort percentage rollouts",
            "Config validation and drift detector comparing YAML/JSON schemas"
        ],
        "guidelines": "Leverage type hints, Pydantic data validation, async/await concurrency, and clean project architecture."
    },
    {
        "id": "golang",
        "name": "Go (Golang) Concurrent Systems & CLI",
        "category": "Concurrency & High-Throughput Services",
        "primary_languages": ["Go"],
        "recommended_tools": ["Go standard library (net/http, sync, context)", "goroutines & channels", "Cobra / Chi / Fiber"],
        "archetypes": [
            "Concurrent worker pool with dynamic autoscaling based on queue depth",
            "High-speed TCP/HTTP port scanner with banner grabbing and CIDR support",
            "In-memory key-value cache with LRU eviction and Write-Ahead Log (WAL)",
            "Reverse proxy with round-robin load balancing and active health probes",
            "Structured JSON log shipping pipeline with buffer batching and compression",
            "Deadlock detector and goroutine leak diagnostic probe",
            "Command-line developer clipboard history manager with fuzzy search",
            "Distributed barrier synchronization coordinator"
        ],
        "guidelines": "Emphasize idiomatic Go: clean error handling, effective channel/goroutine synchronization, context cancellation, and zero unneeded external bloat."
    },
    {
        "id": "typescript_fullstack",
        "name": "TypeScript Full-Stack & Developer Tooling",
        "category": "Developer Experience & Utilities",
        "primary_languages": ["TypeScript", "Node.js"],
        "recommended_tools": ["Node.js / Bun / Deno", "TypeScript strict", "Zod", "Modern Vanilla / Hono / Express"],
        "archetypes": [
            "Interactive CLI dev tool for API benchmarking and latency profiling",
            "OpenAPI / JSON-Schema contract drift tester with automatic diff generation",
            "OAuth 2.0 PKCE authorization server simulator with token introspection",
            "WebSocket-based distributed pub/sub broker with topic wildcard subscriptions",
            "Virtual file system in memory with snapshot and time-travel rollback",
            "Dynamic SQL query builder with type-safe AST query validation",
            "Event sourcing demo: Ledger system with append-only event log and state projection"
        ],
        "guidelines": "Use strict TypeScript typings, comprehensive error boundaries, and self-contained run scripts."
    }
]


def get_stack_for_day(day: int) -> Dict[str, Any]:
    """Returns the rotated tech stack for a given day (1-indexed)."""
    index = (day - 1) % len(TECH_STACKS)
    return TECH_STACKS[index]
