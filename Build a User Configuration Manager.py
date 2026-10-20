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

     if key_ in test_settings:
          test_settings[key_] = value_
          print('Setting ' + key_.capitalize() + ' updated to ' + value_.capitalize() + ' successfully!')
     else:
          print('Setting ' + key_.capitalize() + ' does not exist! Cannot update a non-existing setting.')

def delete_setting(key):
     key_ = key.lower()

     if key_ in test_settings:
          del test_settings[key_]
          print("Setting deleted successfully!")
     else:
          print('Setting not found!')

def view_settings(settings):
     settings_ = settings
     new_settings = {}
     if len(settings_) == 0:
          print('No settings available.')
     else:
          for key, value in test_settings.items():
               new_key = key.capitalize()
               new_value = value.capitalize()
               new_settings[new_key] = new_value
          print(new_settings)

# test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}

# def add_setting(key, value):
#      key.lower()
#      value.lower()

#      if key and value in test_settings:
#           print('Setting ' + key + ' or ' + value + ' already exists! Cannot add a new setting with this name.')
#      else:
#           test_settings[key] = value

# def update_setting(key, value):
#      key.lower()
#      value.lower()

#      if key in test_settings:
#           test_settings[key] = value
#           print('Setting ' + key.capitalize() + ' updated to ' + value.capitalize() + ' successfully!')
#      else:
#           print('Setting ' + key.capitalize() + ' does not exist! Cannot update a non-existing setting.')

# def delete_setting(key):
#      key.lower()

#      if key in test_settings:
#           del test_settings[key]
#           print("Setting deleted successfully!")
#      else:
#           print('Setting not found!')

# def view_settings(settings):
#      settings_ = settings
#      new_settings = {}
#      if len(settings_) == 0:
#           print('No settings available.')
#      else:
#           for key, value in test_settings.items():
#                new_key = key.capitalize()
#                new_value = value.capitalize()
#                new_settings[new_key] = new_value
#           print(new_settings)

