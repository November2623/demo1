def command_substituation(command):
    cmd = command[0][1:-1].split()
    if len(command) == 1 and check(cmd):
        return cmd


def check(command):
    for i in command:
        if "`" not in i:
            return True
    return False
