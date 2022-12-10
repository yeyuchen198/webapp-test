# from flask import Flask

# app = Flask('app')

# @app.route('/')
# def hello_world():
#   return 'Hello, World!'

# app.run(host='0.0.0.0', port=8080)

import requests
import subprocess
import os
import zipfile, shutil

# print('hello world')
# print(subprocess.call(("ls -l"), shell=True))


def create_dir(file_path):
  if os.path.exists(file_path) is False:
    os.makedirs(file_path)
    print('create_dir successs:', file_path)


def downloadFile(url, savepath):
  down_res = requests.get(url=url, params={})
  with open(savepath, "wb") as file:
    file.write(down_res.content)
  print('download success, file save at:', savepath)


def unzipFile(file, savepath):
  print('unzipFile...')
  zip_file = zipfile.ZipFile(file)
  for f in zip_file.namelist():
    zip_file.extract(f, savepath)
    print(f)
  zip_file.close()
  print(f'unzip {file} success.')


def runService():
  print('---run xray service---')
  print(
    subprocess.call(("/run/xray/bin/xray -config  /run/xray/bin/config.json"),
                    shell=True))


file = '/run/xray/bin/xray'
if os.path.isfile(file):
  print(f'{file} exist.')
  runService()
  exit(0)
else:
  print(f'{file} not found.')

create_dir('/run/xray/bin')

url = 'https://github.com/XTLS/Xray-core/releases/latest/download/Xray-linux-64.zip'
savepath = '/run/xray/xray.zip'
downloadFile(url, savepath)

# unzip /run/xray/xray.zip -d /run/xray
# install -m 755 /run/xray/xray /run/xray/bin/xray

unzipFile(savepath, '/run/xray')
print('---start install xray---')
print(
  subprocess.call(("install -m 755 /run/xray/xray /run/xray/bin/xray"),
                  shell=True))

shutil.copy('config.json', '/run/xray/bin/config.json')
print('---copy config.json successs.---')
runService()
