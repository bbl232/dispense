import json

class User:

  def __init__(self, name, password = None, salt = None, email = None, typeOf = 'Normal'):
    self.name = name
    self.password = password
    self.salt = salt
    self.email = email
    self.typeOf = typeOf

  def to_json(self):
    return json.dumps(self.__dict__)

  def save(self):
    return self.to_json()

  def get(name = None):
    if name == None:
      return "All the users!"
    else:
      return "Just user " + name

  def update(name = None):
    pass

  def delete(name = None):
    pass
