# 🍅 Pomodoro Timer

A beginner-friendly desktop Pomodoro Timer built with Python's Tkinter library. This app helps boost productivity by breaking work into focused intervals separated by short breaks.

## What is the Pomodoro Technique?

The Pomodoro Technique is a time management method that uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks. After 4 work sessions, you take a longer break.

## Features

- **Work Sessions**: 25-minute focused work periods (customizable)
- **Short Breaks**: 5-minute breaks between work sessions (customizable)
- **Long Breaks**: 15-minute breaks after every 4 work sessions (customizable)
- **Visual Timer**: Large, easy-to-read countdown display
- **Session Tracking**: Keeps track of completed sessions
- **Sound Notifications**: Audio alert when timer finishes
- **Quick Settings**: Preset timer configurations (25/5, 45/10, 90/15 minutes)
- **Control Options**: Start, pause, and reset functionality
- **Clean UI**: Modern dark theme with color-coded session types

## Files

- `pomodoro_timer.py` — Main Python script with GUI and timer logic
- `README.md` — This documentation file

## How to Run

1. **Prerequisites**: Make sure you have Python 3.8+ installed on your system.

2. **Run the application**:
   ```bash
   python pomodoro_timer.py
   ```

3. **Using the Timer**:
   - Click **Start** to begin a work session
   - Click **Pause** to pause/resume the current session
   - Click **Reset** to restart the current session
   - Use quick settings buttons to change timer durations
   - The app will automatically alternate between work sessions and breaks

## Color Coding

- **Red Timer**: Work session in progress
- **Green Timer**: Short break in progress  
- **Blue Timer**: Long break in progress

## Quick Settings

The app includes three preset configurations:
- **25/5 min**: Traditional Pomodoro (25 min work, 5 min break, 15 min long break)
- **45/10 min**: Extended focus (45 min work, 10 min break, 20 min long break)
- **90/15 min**: Deep work (90 min work, 15 min break, 30 min long break)

## Technical Details

- **GUI Framework**: Tkinter (Python standard library)
- **Threading**: Uses separate thread for timer to keep UI responsive
- **Sound**: Uses `winsound` on Windows, fallback to console bell on other systems
- **Dependencies**: None (uses only Python standard library)

## Platform Compatibility

- **Windows**: Full functionality including system sound notifications
- **macOS/Linux**: Full functionality with console bell notifications

## Sample Output

When running, you'll see:
- Current session type (Work Session 1, Short Break, Long Break)
- Large countdown timer (MM:SS format)
- Session progress counter
- Control buttons for timer management

## Learning Notes

This project demonstrates:
- Tkinter GUI development
- Threading for non-blocking timers
- Event handling and state management
- Cross-platform compatibility considerations
- Clean code organization and documentation

## License

This project is original implementation and free to use for learning purposes.

## Tips for Effective Use

1. **Eliminate Distractions**: Close unnecessary apps and notifications during work sessions
2. **Plan Your Tasks**: Decide what to work on before starting the timer
3. **Take Real Breaks**: Step away from your computer during break periods
4. **Stay Consistent**: Try to complete full cycles without interruption
5. **Adjust as Needed**: Use different presets based on the type of work you're doing

Enjoy your productive Pomodoro sessions! 🍅