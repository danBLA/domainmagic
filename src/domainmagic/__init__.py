from fileupdate import FileUpdater

VERSION="0.0.2"


fileupdater=FileUpdater()
def updatefile(local_path,update_url,**kwargs):
    """decorator which automatically downlads/updates required files
    see fileupdate.Fileupdater.add_file() for possible arguments
    """
    fileupdater.add_file(local_path,update_url,**kwargs)
    def wrap(f):
        def wrapped_f(*args,**kwargs):
            fileupdater.wait_for_file(local_path)
            return f(*args,**kwargs)
        return wrapped_f
    return wrap

def check_installation():
    """check dependencies , returns a list of problems"""
    problems=[]
    
    from domainmagic.ip import PYGEOIP_AVAILABLE
    
    if not PYGEOIP_AVAILABLE:
        problems.append("pygeoip is not installed - geoip functions disabled")
    
    try:
        from dns import resolver
    except:
        problems.append("dnspython is not installed")
    
    return problems
 