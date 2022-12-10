import subprocess

# print(subprocess.call(("install -m 755 ./xray ./bin/xray"), shell=True))

print(
    subprocess.call(("./xray -config  ./config.json"),
                    shell=True))
