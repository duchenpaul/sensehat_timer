import toolkit_config

SEGMENT = 8
configFile = 'config.ini'

configDict = toolkit_config.read_config_general(configFile)['PROFILE']

sleep_prof_list = []
for k, v in configDict.items():
    sleep_prof_list.append(int(v))


