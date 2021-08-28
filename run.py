from main import app
import os
import platform

if __name__ == "__main__":
    # if platform.system() == 'Linux':
    #     os.system("xdg-open http://127.0.0.1:5000/login > /dev/null")
        
    # else:
    #     os.system("start http://127.0.0.1:5000/login")
    app.run(debug=True)