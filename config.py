import toolkit_config

SEGMENT = 8
configFile = 'config.ini'

configDict = toolkit_config.read_config_general(configFile)['PROFILE']

sleep_prof_list = []
for key in sorted(configDict):
    sleep_prof_list.append(int(configDict[key]))


# print(sleep_prof_list)