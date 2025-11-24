import subprocess
import time
import os
import sys

def run_notebook(notebook_path):
    """
    Runs a Jupyter notebook using nbconvert.
    This creates a fresh kernel for the notebook, executes it, and then shuts it down.
    """
    print(f"[{time.strftime('%H:%M:%S')}] Starting execution of {notebook_path}...")
    
    # Check if file exists
    if not os.path.exists(notebook_path):
        print(f"Error: Notebook not found at {notebook_path}")
        return False

    try:
        # Construct the command
        # --to notebook: keep it as a notebook
        # --execute: execute the cells
        # --inplace: overwrite the file with the output (useful to see results)
        # --ExecutePreprocessor.timeout=-1: no timeout
        command = [
            "jupyter", "nbconvert",
            "--to", "notebook",
            "--execute",
            "--inplace",
            "--ExecutePreprocessor.timeout=-1",
            notebook_path
        ]
        
        # Run the command
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"[{time.strftime('%H:%M:%S')}] Successfully finished {notebook_path}")
            return True
        else:
            print(f"[{time.strftime('%H:%M:%S')}] Error running {notebook_path}:")
            print(result.stderr)
            return False

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def main():
    # List of notebooks to run in order
    notebooks = [
        "notebooks/test_nb_1.ipynb",
        "notebooks/test_nb_2.ipynb"
    ]
    
    # You can also scan the directory if needed:
    # notebooks = [os.path.join("notebooks", f) for f in os.listdir('notebooks') if f.endswith('.ipynb')]
    # notebooks.sort()

    print("Starting sequential notebook scheduler...")
    print("----------------------------------------")

    for nb in notebooks:
        success = run_notebook(nb)
        if not success:
            print("Stopping execution due to failure.")
            sys.exit(1)
        
        # Optional: explicit garbage collection or wait if needed, 
        # though the process termination handles resource release.
        print("Kernel cleared and resources released.\n")

    print("----------------------------------------")
    print("All notebooks executed successfully.")

if __name__ == "__main__":
    main()
