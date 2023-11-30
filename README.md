# Amazon-TelegramBot
This project is a bot that, if connected to Telegram, checks Amazon offers and sends them to your channel.

-> The offers mainly deal with the sectors of cars, motorcycles, tools, work tools for mechanics and anything related to technology auto 🚗 🏍️ 🔋

## Requirements

### INSTALLER - script

Now you can run the ```script.sh``` file from the terminal to install all dependencies, included paapi5 package. Open a terminal in the working directory, then type ```bash script.sh``` and launch the command. 



### MANUAL INSTALLER

### **If you used the ```script.sh``` method you can skip the following step.**

In order to use this bot you must complete the following steps:

- Create a telegram bot (https://core.telegram.org/bots)
  
- Create an Amazon Affiliation (https://programma-affiliazione.amazon.it/)
  
- Put all of your keys (Amazon and Telegram API Keys) in the code, we are going to define how below

- **Install packages**:
In the root of the project run:
```bash
pip3 install -r requirements.txt
cd paapi5-python-sdk
python3 setup.py build
python3 setup.py install
cd ..
```

## Usage

After cloning the repository, define all parameters in the code, install all packages and then start bot with command:
```python bot.py``` or ```python3 bot.py```

In progress...
