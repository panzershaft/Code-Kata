from contextlib import contextmanager

@contextmanager
def managed_resource(a):
    # Code to acquire resource, e.g.:
    try:
      a['val'] = 'something'
      yield
    except Exception as e:
      a['error'] = 'error stuff'
      print("failed: " + str(e))
    finally:
        # Code to release resource, e.g.:
        pass

a = {}
with managed_resource(a):
  print("in the place")
  raise Exception("Oh crap")

print(a)
