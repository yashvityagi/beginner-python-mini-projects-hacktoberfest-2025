#!/usr/bin/env python3
"""
Demo script to run the CPU Scheduling Algorithms Simulator
"""

import subprocess
import sys
import os

def main():
    """Run the Streamlit application"""
    print("🚀 Starting CPU Scheduling Algorithms Simulator...")
    print("📚 This educational tool helps visualize CPU scheduling algorithms")
    print("🌐 The application will open in your default web browser")
    print("⏹️  Press Ctrl+C to stop the application")
    print("-" * 60)
    
    try:
        # Run the Streamlit app
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", 
            "cpu_scheduling_simulator.py",
            "--server.port", "8501",
            "--server.address", "localhost"
        ])
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error running application: {e}")
        print("💡 Make sure you have installed all requirements: pip install -r requirements.txt")

if __name__ == "__main__":
    main()
