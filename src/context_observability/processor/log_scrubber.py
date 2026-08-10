"""Log scrubber processor."""
import re

PII_PATTERN = re.compile(r"\b\d{3}-\d{2}-\d{4}\b|\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")

class LogScrubber:
    """Scrub PII from logs before storage."""

    def sanitize(self, message: str) -> str:
        return PII_PATTERN.sub("[REDACTED]", message)
