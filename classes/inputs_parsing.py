def parse_input(user_input: str):
    cmd, *args = user_input.strip().split()
    cmd = cmd.lower().strip()
    return cmd, *args