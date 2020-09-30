from globals import app

import authentication

#App Rests
import RestAppUserRegister
import RestAppUser

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)


