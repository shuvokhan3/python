import subprocess

res = subprocess.run(
    ['php','--ini'],
    capture_output=True,
    text=True
)

print(res.stdout)