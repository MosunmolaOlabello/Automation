from configparser import ConfigParser

def Browser(section,key):
    config = ConfigParser()
    config.read("C:/Users/HP/PycharmProjects/ZendWallet/ConfigurativeFiles/Config.cfg")
    return config.get(section,key)


def Element(section,key):
    config = ConfigParser()
    config.read("C:/Users/HP/PycharmProjects/ZendWallet/ConfigurativeFiles/Element.cfg")
    return config.get(section,key)