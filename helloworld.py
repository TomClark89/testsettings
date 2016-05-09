import configparser
config = configparser.ConfigParser()

config.read('settings.ini')
secretstuff = config['SECRETSTUFF']


for key in secretstuff:
    print ('    ' + key + ':' + secretstuff[key])

print('hello world')