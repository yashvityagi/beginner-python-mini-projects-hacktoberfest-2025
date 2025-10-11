

-----

# Interactive Rock Classification Analysis 🗿

## Project Overview

This project provides an interactive command-line script for training and evaluating machine learning models to classify rock types based on feature data. The script guides the user through the process of loading data, selecting a model, and running the analysis. Finally, it generates a plot comparing the performance of the best model against human classification accuracy.

This tool is designed for easy experimentation, allowing users to quickly test different models without modifying the source code.

-----

##  Author

  * **Manvi Gawande**
  * **Contact:https://github.com/Manvi234/** 

-----


##  Requirements

To run this script, you will need:

  * **Python 3.6** or newer
  * The following Python libraries:
      * `pandas`
      * `scikit-learn`
      * `matplotlib`
      * `openpyxl` (for reading Excel files)

-----

##  Installation

1.  **Clone or download the repository** containing the script and data files.
2.  **Install the required libraries** using pip. Open your terminal and run the following command:
    ```bash
    pip install pandas scikit-learn matplotlib openpyxl
    ```

-----

##  File Structure

Make sure the following files are all located in the **same directory** before running the script:

  * `run_analysis.py`: The main interactive Python script.
  * `aggregateRockData.xlsx`: The Excel file containing the rock type labels.
  * `feature_presence540.txt`: The text file containing the feature data for each rock sample.
  * `trialData.csv`: The CSV file containing the human performance data for comparison.

-----

##  How to Use

1.  **Open your terminal** (Command Prompt on Windows, Terminal on macOS/Linux).
2.  **Navigate to the project directory** using the `cd` command.
    ```bash
    cd path/to/your/project_folder
    ```
3.  **Run the script** with the following command:
    ```bash
    python run_analysis.py
    ```
4.  **Follow the on-screen prompts.** The script will guide you through the analysis step-by-step.

-----

##  Output

The script produces two types of output:

1.  **Terminal Output:** Performance metrics (Accuracy and F1 Score) for the trained models on the training, validation, and test sets will be printed directly to your console.
2.  **Plot Image:** If you choose to save the plot, an image file named `human_vs_model_accuracy.png` will be created in your project directory. This plot visually compares the model's accuracy against human accuracy for each rock type.
