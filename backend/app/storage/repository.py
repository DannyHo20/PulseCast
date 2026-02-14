"""
Repository interfaces for persisting `PodcastState` and related artifacts.

This module provides an in-memory implementation for v1. In production,
this would be backed by Postgres/Supabase.
"""

from __future__ import annotations

from typing import Dict, Optional

from ..models.state import PodcastState


class InMemoryPodcastStateRepository:
    """
    In-memory implementation of podcast state persistence.

    For v1, this provides a simple dict-based storage. In production,
    this would be replaced with Postgres/Supabase.
    """

    def __init__(self) -> None:
        self._store: Dict[str, PodcastState] = {}

    async def save_state(self, state: PodcastState) -> None:
        """Persist the given podcast state."""
        self._store[state.id] = state

    async def load_state(self, job_id: str) -> Optional[PodcastState]:
        """Load the latest podcast state for a job, or None if not found."""
        return self._store.get(job_id)

    async def delete_state(self, job_id: str) -> None:
        """Remove a job's state from storage."""
        self._store.pop(job_id, None)

    async def list_jobs(self) -> list[str]:
        """List all job IDs in storage."""
        return list(self._store.keys())


_repository: Optional[InMemoryPodcastStateRepository] = None


def get_repository() -> InMemoryPodcastStateRepository:
    """Get the singleton repository instance."""
    global _repository
    if _repository is None:
        _repository = InMemoryPodcastStateRepository()
    return _repository
