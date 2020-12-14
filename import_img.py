import configparser

config = configparser.ConfigParser()
config.readfp(open(r'config.txt'))
folder_riferimenti = config.get('Ambiente_test', 'folder_riferimenti')
folder_suggeriti = config.get('Ambiente_test', 'folder_suggeriti')
