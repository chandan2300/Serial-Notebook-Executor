# Jupyter Notebook Scheduler

A simple Python script to execute multiple Jupyter Notebooks sequentially. This tool ensures that each notebook runs in a separate process, guaranteeing that GPU memory and other resources are fully released between runs.

## Features

- **Sequential Execution**: Runs notebooks one after another.
- **Resource Isolation**: Each notebook runs in a fresh process, clearing the kernel and freeing GPU memory upon completion.
- **Detailed Logging**: 
    - Real-time cell-level progress in the console (clean output).
    - Automatic log file generation in `logs/` for each run.
    - **Captures Cell Outputs**: Actual output from code cells (print statements, etc.) is saved to the log file but **hidden from the console** to keep it tidy.
- **Robust Error Handling**: 
    - Stops execution if a notebook fails.
    - **Saves the failed notebook** with the error traceback, allowing for easy debugging.

## Installation

**Option A: Install from PyPI (Recommended)**

```bash
pip install jupyter-serial-scheduler
```

**Option B: Install from Source**

1.  Clone the repository:
    ```bash
    git clone https://github.com/chandan2300/Serial-Notebook-Executor.git
    cd Serial-Notebook-Executor
    ```

2.  Install the package:
    ```bash
    pip install .
    ```

## Usage

Once installed, you can use the `nb-scheduler` command from anywhere.

1.  **Place Notebooks**:
    Put your `.ipynb` files in a directory (e.g., `notebooks/`).

2.  **Run the Scheduler**:
    
    **Option A: Run default list (defined in script)**
    ```bash
    nb-scheduler
    ```

    **Option B: Run specific notebooks**
    ```bash
    nb-scheduler notebooks/test_nb_1.ipynb notebooks/test_nb_2.ipynb
    ```

## Configuration

You can modify `scheduler.py` to change the list of notebooks or the directory they are located in.
