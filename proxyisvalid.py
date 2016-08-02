import ipaddress
# To use ipaddress module, the version of Python must be greater than 3.3


def ip_isvalid(address):
    try: 
        ipaddress.IPv4Address(address)
        return True
    except ipaddress.AddressValueError:
        return False

def port_isvalid(port):
    try:    
        if( int(port) < 65535 and int(port) > 1):
            return True
        else:
            return False
    except ValueError:
        return False

def protocol_isvalid(protocol=""):
    try:
        if(protocol.upper()=="HTTP" or protocol.upper()=="HTTPS"):
            return True
        else:
            return False
    except AttributeError as e:
        print("Parameter must be string. "+str(e))
        return False


