"""Simple stopwatch implementation."""

import time
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Lap:
    """Represents a lap time with start and end timestamps."""
    number: int
    start_time: float
    end_time: float = 0.0

    @property
    def duration(self) -> float:
        """Get lap duration in seconds."""
        if self.end_time == 0.0:
            return time.time() - self.start_time
        return self.end_time - self.start_time


class Stopwatch:
    """A simple stopwatch with lap timing functionality."""
    
    def __init__(self):
        self._start_time: float = 0.0
        self._stop_time: float = 0.0
        self._is_running: bool = False
        self._laps: List[Lap] = []
    
    def start(self) -> None:
        """Start the stopwatch. If already running, does nothing."""
        if not self._is_running:
            now = time.time()
            self._start_time = now
            self._is_running = True
            # Start first lap
            self._laps.append(Lap(number=1, start_time=now))
    
    def stop(self) -> None:
        """Stop the stopwatch. If not running, does nothing."""
        if self._is_running:
            self._stop_time = time.time()
            self._is_running = False
            # End current lap
            if self._laps:
                self._laps[-1].end_time = self._stop_time
    
    def lap(self) -> Optional[float]:
        """Record a lap time and start a new lap.
        
        Returns:
            Duration of the completed lap in seconds, or None if not running
        """
        if not self._is_running:
            return None
            
        now = time.time()
        # End current lap
        if self._laps:
            self._laps[-1].end_time = now
            duration = self._laps[-1].duration
        else:
            duration = 0.0
            
        # Start new lap
        self._laps.append(Lap(
            number=len(self._laps) + 1,
            start_time=now
        ))
        return duration
    
    def reset(self) -> None:
        """Reset the stopwatch to initial state."""
        self._start_time = 0.0
        self._stop_time = 0.0
        self._is_running = False
        self._laps.clear()
    
    @property
    def elapsed(self) -> float:
        """Get total elapsed time in seconds."""
        if not self._start_time:
            return 0.0
        if self._is_running:
            return time.time() - self._start_time
        return self._stop_time - self._start_time
    
    @property
    def is_running(self) -> bool:
        """Check if the stopwatch is currently running."""
        return self._is_running
    
    @property
    def laps(self) -> List[Lap]:
        """Get the list of recorded laps."""
        return self._laps.copy()  # Return copy to prevent modification