import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import time
import random
from collections import deque
import io

# Set page config
st.set_page_config(
    page_title="CPU Scheduling Algorithms Simulator",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .algorithm-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .metric-card {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
    }
    .footer {
        text-align: center;
        padding: 2rem;
        background-color: #f8f9fa;
        border-radius: 0.5rem;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header">🖥️ CPU Scheduling Algorithms Simulator</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Visualize and Compare Scheduling Techniques</p>', unsafe_allow_html=True)

# Sidebar Controls
st.sidebar.header("🎛️ Simulation Controls")

# Algorithm selection
algorithm = st.sidebar.selectbox(
    "Select Scheduling Algorithm",
    ["First Come First Serve (FCFS)", "Shortest Job First (SJF)", "Round Robin (RR)", "Priority Scheduling"]
)

# Number of processes
num_processes = st.sidebar.slider("Number of Processes", min_value=3, max_value=15, value=5)

# Process data input method
input_method = st.sidebar.radio("Process Data Input", ["Random Generation", "Manual Input"])

# Initialize process data
process_data = []

if input_method == "Random Generation":
    st.sidebar.subheader("Random Generation Settings")
    if st.sidebar.button("Generate Random Processes"):
        process_data = []
        for i in range(num_processes):
            arrival_time = random.randint(0, 5)
            burst_time = random.randint(1, 10)
            priority = random.randint(1, 5)
            process_data.append({
                'Process ID': f'P{i+1}',
                'Arrival Time': arrival_time,
                'Burst Time': burst_time,
                'Priority': priority
            })
        st.session_state.process_data = process_data

else:
    st.sidebar.subheader("Manual Input")
    st.sidebar.write("Enter process details:")
    
    if 'process_data' not in st.session_state:
        st.session_state.process_data = []
    
    for i in range(num_processes):
        with st.sidebar.expander(f"Process P{i+1}"):
            arrival_time = st.number_input(f"Arrival Time", min_value=0, value=0, key=f"arrival_{i}")
            burst_time = st.number_input(f"Burst Time", min_value=1, value=1, key=f"burst_{i}")
            priority = st.number_input(f"Priority", min_value=1, value=1, key=f"priority_{i}")
            
            if st.button(f"Add P{i+1}", key=f"add_{i}"):
                process_data.append({
                    'Process ID': f'P{i+1}',
                    'Arrival Time': arrival_time,
                    'Burst Time': burst_time,
                    'Priority': priority
                })
                st.session_state.process_data = process_data
                st.success(f"Process P{i+1} added!")

# Time quantum for Round Robin
time_quantum = 2  # Default value
if "Round Robin" in algorithm:
    time_quantum = st.sidebar.number_input("Time Quantum", min_value=1, value=2)

# Simulation button
if st.sidebar.button("🚀 Run Simulation", type="primary"):
    if 'process_data' in st.session_state and st.session_state.process_data:
        st.session_state.run_simulation = True
    else:
        st.sidebar.error("Please generate or input process data first!")

# Algorithm Explanations
def display_algorithm_explanation(selected_algorithm):
    explanations = {
        "First Come First Serve (FCFS)": {
            "theory": "FCFS is the simplest CPU scheduling algorithm. It executes processes in the order they arrive in the ready queue.",
            "working": "Processes are executed in the order of their arrival time. Once a process starts executing, it runs until completion.",
            "advantages": [
                "Simple to understand and implement",
                "No starvation (every process gets executed)",
                "Fair scheduling (first come, first served)"
            ],
            "disadvantages": [
                "Poor performance for interactive systems",
                "Average waiting time can be high",
                "Convoy effect (short processes wait for long ones)"
            ],
            "use_case": "Batch processing systems where simplicity is more important than performance."
        },
        "Shortest Job First (SJF)": {
            "theory": "SJF selects the process with the smallest burst time for execution next.",
            "working": "The scheduler always picks the process with the shortest remaining burst time from the ready queue.",
            "advantages": [
                "Optimal for minimizing average waiting time",
                "Good for batch processing",
                "Theoretically optimal"
            ],
            "disadvantages": [
                "Can cause starvation of long processes",
                "Difficult to predict burst time",
                "Not suitable for interactive systems"
            ],
            "use_case": "Batch processing systems where job execution times are known in advance."
        },
        "Round Robin (RR)": {
            "theory": "Round Robin is a preemptive scheduling algorithm that assigns a fixed time slice to each process.",
            "working": "Each process gets a time quantum. If a process doesn't complete within its quantum, it's preempted and moved to the end of the queue.",
            "advantages": [
                "Fair scheduling (every process gets equal time)",
                "Good response time for interactive systems",
                "No starvation"
            ],
            "disadvantages": [
                "Performance depends on time quantum size",
                "Context switching overhead",
                "Not optimal for batch processing"
            ],
            "use_case": "Time-sharing systems and interactive applications."
        },
        "Priority Scheduling": {
            "theory": "Priority scheduling assigns priorities to processes and executes them based on priority levels.",
            "working": "Processes with higher priority are executed first. If priorities are equal, FCFS is used as a tie-breaker.",
            "advantages": [
                "Flexible (can be preemptive or non-preemptive)",
                "Good for real-time systems",
                "Can handle different process types"
            ],
            "disadvantages": [
                "Can cause starvation of low-priority processes",
                "Priority inversion problem",
                "Difficult to assign appropriate priorities"
            ],
            "use_case": "Real-time systems and operating systems with different process types."
        }
    }
    
    exp = explanations[selected_algorithm]
    
    # Use Streamlit's native components instead of HTML
    st.markdown(f"### 📚 {selected_algorithm} - Theory & Explanation")
    
    st.markdown("**Theory:**")
    st.info(exp['theory'])
    
    st.markdown("**Working Principle:**")
    st.info(exp['working'])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**✅ Advantages:**")
        for adv in exp['advantages']:
            st.markdown(f"• {adv}")
    
    with col2:
        st.markdown("**❌ Disadvantages:**")
        for dis in exp['disadvantages']:
            st.markdown(f"• {dis}")
    
    st.markdown("**🎯 Use Case:**")
    st.success(exp['use_case'])

# Scheduling Algorithm Implementations
def fcfs_scheduling(processes):
    """First Come First Serve Scheduling"""
    # Sort by arrival time
    sorted_processes = sorted(processes, key=lambda x: x['Arrival Time'])
    
    current_time = 0
    results = []
    
    for process in sorted_processes:
        if current_time < process['Arrival Time']:
            current_time = process['Arrival Time']
        
        waiting_time = current_time - process['Arrival Time']
        completion_time = current_time + process['Burst Time']
        turnaround_time = completion_time - process['Arrival Time']
        
        results.append({
            'Process ID': process['Process ID'],
            'Arrival Time': process['Arrival Time'],
            'Burst Time': process['Burst Time'],
            'Completion Time': completion_time,
            'Waiting Time': waiting_time,
            'Turnaround Time': turnaround_time,
            'Start Time': current_time
        })
        
        current_time = completion_time
    
    return results

def sjf_scheduling(processes):
    """Shortest Job First Scheduling (Non-preemptive)"""
    # Sort by arrival time first, then by burst time
    sorted_processes = sorted(processes, key=lambda x: (x['Arrival Time'], x['Burst Time']))
    
    current_time = 0
    results = []
    remaining_processes = sorted_processes.copy()
    
    while remaining_processes:
        # Find processes that have arrived
        available_processes = [p for p in remaining_processes if p['Arrival Time'] <= current_time]
        
        if not available_processes:
            # No process has arrived yet, move time forward
            current_time = min(p['Arrival Time'] for p in remaining_processes)
            available_processes = [p for p in remaining_processes if p['Arrival Time'] <= current_time]
        
        # Select process with shortest burst time
        selected_process = min(available_processes, key=lambda x: x['Burst Time'])
        
        waiting_time = current_time - selected_process['Arrival Time']
        completion_time = current_time + selected_process['Burst Time']
        turnaround_time = completion_time - selected_process['Arrival Time']
        
        results.append({
            'Process ID': selected_process['Process ID'],
            'Arrival Time': selected_process['Arrival Time'],
            'Burst Time': selected_process['Burst Time'],
            'Completion Time': completion_time,
            'Waiting Time': waiting_time,
            'Turnaround Time': turnaround_time,
            'Start Time': current_time
        })
        
        current_time = completion_time
        remaining_processes.remove(selected_process)
    
    return results

def round_robin_scheduling(processes, time_quantum):
    """Round Robin Scheduling"""
    # Sort by arrival time
    sorted_processes = sorted(processes, key=lambda x: x['Arrival Time'])
    
    # Create a queue of processes
    process_queue = deque()
    process_index = 0
    current_time = 0
    results = []
    
    # Initialize remaining burst times
    remaining_burst = {p['Process ID']: p['Burst Time'] for p in sorted_processes}
    start_times = {}
    
    while process_index < len(sorted_processes) or process_queue:
        # Add processes that have arrived
        while process_index < len(sorted_processes) and sorted_processes[process_index]['Arrival Time'] <= current_time:
            process_queue.append(sorted_processes[process_index]['Process ID'])
            process_index += 1
        
        if process_queue:
            current_process = process_queue.popleft()
            
            # Record start time if not already recorded
            if current_process not in start_times:
                start_times[current_process] = current_time
            
            # Execute for time quantum or until completion
            execution_time = min(time_quantum, remaining_burst[current_process])
            remaining_burst[current_process] -= execution_time
            current_time += execution_time
            
            if remaining_burst[current_process] > 0:
                # Process not completed, add back to queue
                process_queue.append(current_process)
            else:
                # Process completed
                process_info = next(p for p in sorted_processes if p['Process ID'] == current_process)
                waiting_time = current_time - process_info['Burst Time'] - process_info['Arrival Time']
                completion_time = current_time
                turnaround_time = completion_time - process_info['Arrival Time']
                
                results.append({
                    'Process ID': current_process,
                    'Arrival Time': process_info['Arrival Time'],
                    'Burst Time': process_info['Burst Time'],
                    'Completion Time': completion_time,
                    'Waiting Time': waiting_time,
                    'Turnaround Time': turnaround_time,
                    'Start Time': start_times[current_process]
                })
        else:
            # No process in queue, move time forward
            if process_index < len(sorted_processes):
                current_time = sorted_processes[process_index]['Arrival Time']
    
    return results

def priority_scheduling(processes):
    """Priority Scheduling (Non-preemptive)"""
    # Sort by arrival time first, then by priority (lower number = higher priority)
    sorted_processes = sorted(processes, key=lambda x: (x['Arrival Time'], x['Priority']))
    
    current_time = 0
    results = []
    remaining_processes = sorted_processes.copy()
    
    while remaining_processes:
        # Find processes that have arrived
        available_processes = [p for p in remaining_processes if p['Arrival Time'] <= current_time]
        
        if not available_processes:
            # No process has arrived yet, move time forward
            current_time = min(p['Arrival Time'] for p in remaining_processes)
            available_processes = [p for p in remaining_processes if p['Arrival Time'] <= current_time]
        
        # Select process with highest priority (lowest priority number)
        selected_process = min(available_processes, key=lambda x: x['Priority'])
        
        waiting_time = current_time - selected_process['Arrival Time']
        completion_time = current_time + selected_process['Burst Time']
        turnaround_time = completion_time - selected_process['Arrival Time']
        
        results.append({
            'Process ID': selected_process['Process ID'],
            'Arrival Time': selected_process['Arrival Time'],
            'Burst Time': selected_process['Burst Time'],
            'Completion Time': completion_time,
            'Waiting Time': waiting_time,
            'Turnaround Time': turnaround_time,
            'Start Time': current_time
        })
        
        current_time = completion_time
        remaining_processes.remove(selected_process)
    
    return results

# Visualization Functions
def create_gantt_chart(results, algorithm_name):
    """Create Gantt Chart for process scheduling"""
    fig = go.Figure()
    
    colors = px.colors.qualitative.Set3
    
    for i, process in enumerate(results):
        fig.add_trace(go.Scatter(
            x=[process['Start Time'], process['Completion Time'], process['Completion Time'], process['Start Time'], process['Start Time']],
            y=[i, i, i+0.8, i+0.8, i],
            fill='toself',
            fillcolor=colors[i % len(colors)],
            line=dict(color=colors[i % len(colors)]),
            name=process['Process ID'],
            text=f"{process['Process ID']}<br>Duration: {process['Burst Time']}",
            hovertemplate=f"<b>{process['Process ID']}</b><br>" +
                         f"Start: {process['Start Time']}<br>" +
                         f"End: {process['Completion Time']}<br>" +
                         f"Duration: {process['Burst Time']}<br>" +
                         f"<extra></extra>"
        ))
    
    fig.update_layout(
        title=f"Gantt Chart - {algorithm_name}",
        xaxis_title="Time",
        yaxis_title="Processes",
        yaxis=dict(
            tickmode='array',
            tickvals=list(range(len(results))),
            ticktext=[p['Process ID'] for p in results]
        ),
        height=400,
        showlegend=True
    )
    
    return fig

def create_comparison_chart(algorithm_results):
    """Create comparison chart for multiple algorithms"""
    algorithms = list(algorithm_results.keys())
    avg_waiting = [np.mean([p['Waiting Time'] for p in results]) for results in algorithm_results.values()]
    avg_turnaround = [np.mean([p['Turnaround Time'] for p in results]) for results in algorithm_results.values()]
    
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=('Average Waiting Time', 'Average Turnaround Time'),
        specs=[[{"type": "bar"}, {"type": "bar"}]]
    )
    
    fig.add_trace(
        go.Bar(x=algorithms, y=avg_waiting, name='Waiting Time', marker_color='lightblue'),
        row=1, col=1
    )
    
    fig.add_trace(
        go.Bar(x=algorithms, y=avg_turnaround, name='Turnaround Time', marker_color='lightcoral'),
        row=1, col=2
    )
    
    fig.update_layout(
        title="Algorithm Performance Comparison",
        height=400,
        showlegend=False
    )
    
    return fig

# Main App Logic
if 'process_data' in st.session_state and st.session_state.process_data:
    # Display current process data
    st.subheader("📊 Current Process Data")
    df_processes = pd.DataFrame(st.session_state.process_data)
    st.dataframe(df_processes, use_container_width=True)
    
    # Algorithm explanation
    with st.expander("📚 Algorithm Explanation", expanded=True):
        display_algorithm_explanation(algorithm)
    
    # Run simulation if requested
    if st.session_state.get('run_simulation', False):
        st.subheader("🎯 Simulation Results")
        
        # Run selected algorithm
        if "FCFS" in algorithm:
            results = fcfs_scheduling(st.session_state.process_data)
        elif "SJF" in algorithm:
            results = sjf_scheduling(st.session_state.process_data)
        elif "Round Robin" in algorithm:
            results = round_robin_scheduling(st.session_state.process_data, time_quantum)
        elif "Priority" in algorithm:
            results = priority_scheduling(st.session_state.process_data)
        
        # Display results
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📋 Results Table")
            df_results = pd.DataFrame(results)
            st.dataframe(df_results, use_container_width=True)
            
            # Calculate metrics
            avg_waiting = np.mean([p['Waiting Time'] for p in results])
            avg_turnaround = np.mean([p['Turnaround Time'] for p in results])
            
            st.subheader("📈 Performance Metrics")
            col1_1, col1_2 = st.columns(2)
            with col1_1:
                st.metric("Average Waiting Time", f"{avg_waiting:.2f}")
            with col1_2:
                st.metric("Average Turnaround Time", f"{avg_turnaround:.2f}")
        
        with col2:
            st.subheader("📊 Gantt Chart")
            gantt_fig = create_gantt_chart(results, algorithm)
            st.plotly_chart(gantt_fig, use_container_width=True)
        
        # Reset simulation flag
        st.session_state.run_simulation = False
        
        # Export functionality
        st.subheader("💾 Export Results")
        csv = df_results.to_csv(index=False)
        st.download_button(
            label="Download Results as CSV",
            data=csv,
            file_name=f"{algorithm.replace(' ', '_')}_results.csv",
            mime="text/csv"
        )
    
    # Comparative Analysis
    st.subheader("🔄 Comparative Analysis")
    
    # Time quantum for comparison (if not already set)
    if "Round Robin" not in algorithm:
        comparison_time_quantum = st.number_input("Time Quantum for Round Robin (in comparison)", min_value=1, value=2, key="comparison_quantum")
    else:
        comparison_time_quantum = time_quantum
    
    if st.button("Compare All Algorithms", type="secondary"):
        st.subheader("📊 All Algorithms Comparison")
        
        # Run all algorithms
        all_results = {}
        algorithms = ["FCFS", "SJF", "Round Robin", "Priority"]
        
        for alg in algorithms:
            if alg == "FCFS":
                all_results[alg] = fcfs_scheduling(st.session_state.process_data)
            elif alg == "SJF":
                all_results[alg] = sjf_scheduling(st.session_state.process_data)
            elif alg == "Round Robin":
                all_results[alg] = round_robin_scheduling(st.session_state.process_data, comparison_time_quantum)
            elif alg == "Priority":
                all_results[alg] = priority_scheduling(st.session_state.process_data)
        
        # Create comparison chart
        comparison_fig = create_comparison_chart(all_results)
        st.plotly_chart(comparison_fig, use_container_width=True)
        
        # Create comparison table
        comparison_data = []
        for alg, results in all_results.items():
            avg_waiting = np.mean([p['Waiting Time'] for p in results])
            avg_turnaround = np.mean([p['Turnaround Time'] for p in results])
            comparison_data.append({
                'Algorithm': alg,
                'Average Waiting Time': f"{avg_waiting:.2f}",
                'Average Turnaround Time': f"{avg_turnaround:.2f}"
            })
        
        st.subheader("📋 Performance Comparison Table")
        df_comparison = pd.DataFrame(comparison_data)
        st.dataframe(df_comparison, use_container_width=True)
        
        # Highlight best algorithm
        best_waiting = min(comparison_data, key=lambda x: float(x['Average Waiting Time']))
        best_turnaround = min(comparison_data, key=lambda x: float(x['Average Turnaround Time']))
        
        col1, col2 = st.columns(2)
        with col1:
            st.success(f"🏆 Best for Waiting Time: {best_waiting['Algorithm']} ({best_waiting['Average Waiting Time']})")
        with col2:
            st.success(f"🏆 Best for Turnaround Time: {best_turnaround['Algorithm']} ({best_turnaround['Average Turnaround Time']})")

else:
    st.info("👈 Please configure your simulation parameters in the sidebar and generate process data to begin!")

# Educational Footer
st.markdown("""
<div class="footer">
    <h3>Built with ❤️ using Streamlit</h3>
    <p>This interactive simulator helps students learn CPU Scheduling Algorithms through visualization and comparison.</p>
    <p><strong>Educational Purpose:</strong> Understanding the trade-offs between different scheduling algorithms is crucial for operating systems design.</p>
</div>
""", unsafe_allow_html=True)
