import ast

def check_syntax(code):
    try:
        ast.parse(code)
        return True, "No syntax errors found."
    except Exception as e:
        return False, str(e)

def security_scan(code):
    dangerous = ["eval", "exec", "os.system"]

    found = []
    for item in dangerous:
        if item in code:
            found.append(item)

    if found:
        return "Unsafe functions found: " + ", ".join(found)
    else:
        return "No security issues detected."