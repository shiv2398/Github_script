import subprocess
import os

def git_add_commit_push(file_path, commit_message):
    """
    Add, commit, and push a file to a Git repository.

    Args:
        file_path (str): Path to the file you want to contribute.
        commit_message (str): Commit message for the contribution.

    Raises:
        subprocess.CalledProcessError: If any of the Git commands fail.

    """
    try:
        # Change to the directory containing the file
        os.chdir(os.path.dirname(file_path))
        
        # Set the GIT_TRACE environment variable to enable debug output
        os.environ['GIT_TRACE'] = '1'
        
        # Git commands
        git_add = ['git', 'add', file_path]
        git_commit = ['git', 'commit', '-m', commit_message]
        git_push = ['git', 'push', '-f', 'origin', 'main']
        
        # Execute git add, commit, and push commands
        subprocess.run(git_add, check=True)
        subprocess.run(git_commit, check=True)
        subprocess.run(git_push, check=True)
        
        print("\033[1m\033[36m\033[4mFile is committed.\033[0m")
    except subprocess.CalledProcessError as e:
        print(f"\033[1m\033[31mGit command failed: {e.cmd}\033[0m")
        print(f"\033[1m\033[31mError output: {e.output}\033[0m")

# Example usage
path = ''#give the directory path
for i, file in enumerate(os.listdir(path)):
    print(f"\033[1m\033[36m\033[4m File {i+1} is being committed.\033[0m")
    file_path = os.path.join(path, file)
    commit_message = '.'  # Replace with your desired commit message

    git_add_commit_push(file_path, commit_message)

