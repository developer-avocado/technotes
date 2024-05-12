import subprocess
from subprocess import PIPE

result = subprocess.run(['git', 'checkout', 'main'], shell=True, stdout=PIPE, text=True)

result = subprocess.run(['git', 'branch', '--all'], shell=True, stdout=PIPE, text=True)
print(result)

branch_list = result.stdout.strip().split('\n')

# delete all branch without main
for branch in branch_list:
    if 'remotes' in branch and not 'main' in branch:
        print(f"1:{branch}")
        remote = branch.split('/')[1]
        branch = branch.split('/')[2]
        result = subprocess.run(['git', 'push', f"{remote}", f"{branch.strip()}",'--delete'], shell=True, stdout=PIPE, text=True)
    if not 'remotes' in branch and not 'main' in branch:
        print(f"2:{branch}")
        result = subprocess.run(['git', 'branch', '-d' ,f"{branch.strip()}"], shell=True, stdout=PIPE, text=True)
    else:
        print(f"3:{branch}")
        pass

# Create branches and push them
for branch in ['a', 'b', 'c']:
    result = subprocess.run(['git', 'checkout', '-b', f"{branch}", 'origin/main'], shell=True, stdout=PIPE, text=True)
    result = subprocess.run(['git', 'push', '-u', 'origin', f"{branch}"], shell=True, stdout=PIPE, text=True)
