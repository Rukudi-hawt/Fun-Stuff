test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}

def add_setting(key, value):
     key_ = key.lower()
     value_ = value.lower()

     if key_ and value_ in test_settings:
          print('Setting ' + key_ + ' or ' + value_ + ' already exists! Cannot add a new setting with this name.')
     else:
          test_settings[key_] = value_

def update_setting(key, value):
     key_ = key.lower()
     value_ = value.lower()