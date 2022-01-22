from main import app

def bordered(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (s + ' ' * width))   
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)

if __name__ == "__main__":
    print("""\n\033[94m
██████╗ ███████╗██████╗ ██╗   ██╗ ██████╗  ██████╗ ███████╗██████╗ 
██╔══██╗██╔════╝██╔══██╗██║   ██║██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
██║  ██║█████╗  ██████╔╝██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝
██║  ██║██╔══╝  ██╔══██╗██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗
██████╔╝███████╗██████╔╝╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║
╚═════╝ ╚══════╝╚═════╝  ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                   \u001b[0m""")

    print(bordered("\n \033[1mWEB APP :- http://127.0.0.1:5000/login\n\n"))
    print(bordered("\033[08m \033[42m !!! \033[0m = INFO"))
    print(bordered("\033[08m \033[41m !!! \033[0m = ERROR"))
    print(bordered("\033[08m \033[43m !!! \033[0m = WARNING\n"))
    app.run(debug=False)