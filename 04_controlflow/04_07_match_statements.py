
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 500|501|502|503|504:
            return "Server error"
        case _:#通用字元，永遠不會匹配失敗
            return "Something's wrong with the internet"
        
status = int(input("Please enter http status code: "))

print(http_error(status))