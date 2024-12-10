import os
import git
import datetime
from git import Repo

# Path to your local Git repository
repo_path = r"C:\Users\jagdi\Music\personal projects\Tower-Defense-Game"  # Raw string
  # Change this to your local repo path

# GitHub username and email
github_username = 'jagdish575'
github_email = 'jagdishprajapati573@gmail.com'

# Initialize repository
repo = Repo(repo_path)
assert not repo.bare

# Set the dates you missed (from 23 Oct to 10 Dec)
start_date = datetime.date(2024, 9, 19)
end_date = datetime.date(2024, 10, 23)

# Loop through each date
current_date = start_date
while current_date <= end_date:
    # Create a new file with the date in the filename
    file_name = f"new_file_{current_date.isoformat()}.txt"
    file_path = os.path.join(repo_path, file_name)

    # Write the commit date and unique content to the new file
    with open(file_path, 'w') as f:
        f.write(f'# Commit for {current_date} - Simulated update.\n')
        f.write(f'Changes made on {current_date.isoformat()} - This is a unique change for this day.\n')
        f.write(f'Date stored inside this file: {current_date.isoformat()}\n')  # Store the date in the file

    # Stage and commit the new file
    repo.git.add(file_path)
    
    # Set the author and commit
    author = git.Actor(github_username, github_email)
    repo.index.commit(f'Commit for {current_date} - New file for {current_date}', author=author)  # Unique commit message

    # Set the commit date to match the loop date
    repo.git.commit('--amend', '--no-edit', f'--date={current_date.isoformat()}')

    # Push the changes
    repo.git.push()

    # Move to the next day
    current_date += datetime.timedelta(days=1)

print("Code successfully pushed for the specified dates.")
