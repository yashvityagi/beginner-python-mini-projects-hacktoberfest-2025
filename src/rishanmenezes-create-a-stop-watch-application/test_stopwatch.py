"""Tests for the stopwatch implementation."""

import time
from unittest.mock import patch

import pytest

from .stopwatch import Stopwatch, Lap


def test_stopwatch_initial_state():
    """Test stopwatch initialization."""
    sw = Stopwatch()
    assert not sw.is_running
    assert sw.elapsed == 0.0
    assert len(sw.laps) == 0


def test_stopwatch_start():
    """Test starting the stopwatch."""
    sw = Stopwatch()
    sw.start()
    assert sw.is_running
    assert len(sw.laps) == 1
    assert sw.laps[0].number == 1


def test_stopwatch_stop():
    """Test stopping the stopwatch."""
    sw = Stopwatch()
    sw.start()
    time.sleep(0.1)  # Small delay
    sw.stop()
    assert not sw.is_running
    elapsed = sw.elapsed
    assert elapsed > 0
    time.sleep(0.1)  # Another delay
    assert sw.elapsed == elapsed  # Time should not increase after stop


def test_stopwatch_lap():
    """Test lap functionality."""
    sw = Stopwatch()
    sw.start()
    time.sleep(0.1)
    
    # Record first lap
    lap_time = sw.lap()
    assert lap_time > 0
    assert len(sw.laps) == 2  # Initial lap + new lap
    assert sw.laps[0].end_time > 0
    assert sw.laps[1].end_time == 0  # Current lap not ended
    
    # Record second lap
    time.sleep(0.1)
    lap_time = sw.lap()
    assert lap_time > 0
    assert len(sw.laps) == 3
    assert sw.laps[1].end_time > 0
    assert sw.laps[2].end_time == 0


def test_stopwatch_reset():
    """Test resetting the stopwatch."""
    sw = Stopwatch()
    sw.start()
    time.sleep(0.1)
    sw.lap()
    sw.reset()
    
    assert not sw.is_running
    assert sw.elapsed == 0.0
    assert len(sw.laps) == 0


def test_lap_properties():
    """Test Lap dataclass properties."""
    start_time = time.time()
    lap = Lap(number=1, start_time=start_time)
    
    # Test with ongoing lap
    assert lap.end_time == 0.0
    time.sleep(0.1)
    assert lap.duration > 0
    
    # Test with completed lap
    end_time = time.time()
    lap.end_time = end_time
    expected_duration = end_time - start_time
    assert lap.duration == expected_duration