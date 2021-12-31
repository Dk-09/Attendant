from main import app
import pyfiglet

if __name__ == "__main__":
    result = pyfiglet.figlet_format("Debugger", font = "banner3-D" )
    print("\n\033[94m" + result + "\033[92m")
    print("\033[08m \033[42m !!! \033[0m = INFO")
    print("\033[08m \033[41m !!! \033[0m = ERROR")
    print("\033[08m \033[43m !!! \033[0m = WARNING\n")
    app.run(debug=False)