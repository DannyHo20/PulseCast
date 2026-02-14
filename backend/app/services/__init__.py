"""
Service-layer integrations for the PulseCast backend.

This package hosts implementations for:
- Content ingestion (web pages, PDFs, raw text).
- Audio synthesis and post-processing.
"""

from .audio import AudioResult, AudioSegment, synthesize_podcast_audio
from .ingestion import IngestionResult, ingest_source

__all__ = [
    "AudioResult",
    "AudioSegment",
    "IngestionResult",
    "ingest_source",
    "synthesize_podcast_audio",
]

