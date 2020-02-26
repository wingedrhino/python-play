class MyError(Exception):
  """Base class for exceptions in this module."""
  def __str__(self):
    return self.message

class RhinoError(MyError):
  def __init__(self, error_code, output):
    self.error_code = error_code
    self.output = output
    self.message = f'RhinoError: Error Code: {self.error_code}; Output: "{self.output}"'

raise RhinoError(1, 'ouch')