from configparser import ConfigParser

def read_cfg():
    #read_ini
    conf = ConfigParser()
    conf.read('cfg.ini', encoding='utf-8')
    cfg_data = []

    sections = conf.sections()
    zentao_sel = sections[0]

    for items in conf.items(zentao_sel):
        cfg_data.append(items[1])
        
    return cfg_data

if __name__ == "__main__":
    read_cfg()
    
    
