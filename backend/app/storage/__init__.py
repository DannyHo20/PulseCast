"""
Storage and caching abstractions for PulseCast.

This package is intended to hide concrete dependencies such as Postgres /
Supabase and Redis behind simple interfaces that the graph and API layers
can depend on.
"""

from .repository import InMemoryPodcastStateRepository, get_repository

__all__ = [
    "InMemoryPodcastStateRepository",
    "get_repository",
]

