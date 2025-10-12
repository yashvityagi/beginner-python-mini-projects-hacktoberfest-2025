# CPU Scheduling Algorithms Simulator

A comprehensive Streamlit web application for visualizing and comparing CPU scheduling algorithms including FCFS, SJF, Round Robin, and Priority Scheduling.

## Features

- **Interactive Simulation**: Run different CPU scheduling algorithms with customizable parameters
- **Visual Gantt Charts**: See how processes are scheduled over time
- **Performance Comparison**: Compare all algorithms side-by-side
- **Educational Content**: Detailed explanations of each algorithm with advantages/disadvantages
- **Export Functionality**: Download simulation results as CSV files

## Supported Algorithms

1. **First Come First Serve (FCFS)**: Non-preemptive scheduling in arrival order
2. **Shortest Job First (SJF)**: Non-preemptive scheduling by shortest burst time
3. **Round Robin (RR)**: Preemptive scheduling with time quantum
4. **Priority Scheduling**: Non-preemptive scheduling by priority levels

## Installation

1. Clone or download this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit application:

```bash
streamlit run cpu_scheduling_simulator.py
```

2. Open your web browser and navigate to the provided local URL (usually `http://localhost:8501`)

3. Use the sidebar to:
   - Select a scheduling algorithm
   - Choose the number of processes (3-15)
   - Input process data manually or generate random data
   - Set time quantum for Round Robin
   - Run the simulation

4. View results including:
   - Process execution table
   - Gantt chart visualization
   - Performance metrics
   - Comparative analysis

## Features Overview

### Process Data Input
- **Random Generation**: Automatically generate process data with random arrival times, burst times, and priorities
- **Manual Input**: Manually specify each process's parameters

### Visualization
- **Gantt Charts**: Interactive timeline showing process execution
- **Performance Metrics**: Average waiting time and turnaround time calculations
- **Comparison Charts**: Side-by-side comparison of all algorithms

### Educational Content
- Detailed algorithm explanations
- Theory and working principles
- Advantages and disadvantages
- Real-world use cases

## Technical Details

- Built with Streamlit for the web interface
- Uses Plotly for interactive visualizations
- Implements all four scheduling algorithms from scratch
- Supports both preemptive and non-preemptive scheduling
- Responsive design with modern UI components

## Educational Purpose

This simulator is designed to help students understand:
- How different CPU scheduling algorithms work
- The trade-offs between different scheduling strategies
- Performance implications of scheduling choices
- Real-world applications of scheduling algorithms

## Contributing

Feel free to contribute improvements, bug fixes, or additional features to make this educational tool even better!

---

## Video Demo
![Demo video](Demo_video.mp4)


