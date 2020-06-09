# selenium 自動化測試專案

使用 selenium + python3 進行產品測試 

#### 使用教學
  ```
  將 container 內部的資料夾 /home 掛到使用者的目錄
  
  your_home_path:/home 
  
  example:
  docker run -it -v /home/test:/home yusongwang1991/selenium-python:latest bash
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
#### 執行測試
  ```
  python3 xportal_test001.py
  ```
