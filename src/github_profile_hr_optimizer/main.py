#!/usr/bin/env python
import sys
from github_profile_hr_optimizer.crew import GithubProfileHrOptimizerCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    # Check if username is passed as CLI argument (e.g., main.py run <username>)
    github_username = None
    if len(sys.argv) > 2:
        github_username = sys.argv[2]
    
    # If not in args, check env var
    if not github_username:
        import os
        github_username = os.getenv("GITHUB_USERNAME")
        
    # If still not found and in an interactive terminal, prompt user
    if not github_username:
        try:
            if sys.stdin.isatty():
                github_username = input("Enter the GitHub username to analyze: ").strip()
        except Exception:
            pass

    # Fallback to default
    if not github_username:
        github_username = 'sample_value'

    print(f"Running GithubProfileHrOptimizer crew for username: {github_username}")
    inputs = {
        'github_username': github_username
    }
    result = GithubProfileHrOptimizerCrew().crew().kickoff(inputs=inputs)

    # Print the result to stdout
    print("\n" + "="*50)
    print("CREW EXECUTION RESULT")
    print("="*50)
    print(result.raw)
    print("="*50 + "\n")

    # Write the result to a markdown report file
    report_filename = f"github_report_{github_username}.md"
    try:
        with open(report_filename, "w", encoding="utf-8") as f:
            f.write(result.raw)
        print(f"Report successfully saved to: {report_filename}")
    except Exception as e:
        print(f"Failed to save report to file: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'github_username': 'sample_value'
    }
    try:
        GithubProfileHrOptimizerCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        GithubProfileHrOptimizerCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'github_username': 'sample_value'
    }
    try:
        GithubProfileHrOptimizerCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
