def pre_process(text: str):
    lines = text.split('\n')
    res = []
    for line in lines:
        if "//" not in line and "#" not in line:
            # remove comments and directives
            res.append(line)

    return "\n".join(res)
