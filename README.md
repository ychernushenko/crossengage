## Install
git clone https://github.com/yury-chernushenko/blackbill.git  
sudo pip install -U docker-compose // Might take some time

## Usage

### Configure  
This version has a drawback (unfinished part), keywords should be changed in the file scraper/scraper.py (line 21):  
`search_list = ['C++', 'python', 'java', 'javascript', 'rust', 'elexir']`

### Start
docker-compose build 
docker-compose start mysql
docker-compose up  

> If there were errors while starting containers, try to cancel (Ctrl+C and restart)  

### Interface
in browser open - localhost:5000 
