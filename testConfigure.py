import ConfigParser
import io
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.read("example.cfg")
print config.get('mysql', 'user')
print config.get('mysql', 'password')
