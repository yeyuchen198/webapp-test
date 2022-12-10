import subprocess

print(
    subprocess.call(("./xray -config  ./config.json"),
                    shell=True))
