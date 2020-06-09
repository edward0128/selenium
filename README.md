# selenium 自動化測試專案

使用 selenium + python3 進行產品測試 

#### 啟用 grid Server
```
mkdir -p ~/video
docker run -d -e VIDEO=false -v ~/video:/videos --name=grid -p 4444:24444 -p 5905:25900  -e SCREEN_WIDTH=1024 -e SCREEN_HEIGHT=768   elgalu/selenium
```
使用 vnc viewer 連接到 grid server

需使用本機IP
```
example
192.168.1.5:5905
```
#### 使用教學
  ```
  將 container 內部的資料夾 /home 掛到使用者的目錄
  
  your_home_path:/home 
  
  example:
  mkdir -p ~/test
  
  docker run -it -v ~/test:/home yusongwang1991/selenium-python:latest bash
  ```  
#### 啟動後 執行初始化腳本,取得最新的測試代碼
  ```
  ./selenium_starup.sh
  
  將最新的測試用代碼,下載到 /home 目錄
  ```
#### 移動到測試目錄
  ```
  cd /home/selenium/test-case/
  ```
#### 修改 config.ini

需修改 XXXXX 為本機 ip 

```
[webdriver]
server=http://XXXXXX:4444/wd/hub
browser=chrome
[xportal]
url=http://10.16.44.1:32666/
[k8s]
k8s_name=k8s-1
k8s_ip=10.16.44.2
```
  
#### 執行測試
  ```
  python3 xportal_test001.py
  ```
