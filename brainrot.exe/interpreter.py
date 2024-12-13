import webbrowser
s = dict()
ifOccurred = False
elifOccurred = False
operators = ['mew_streak', 'fanum_tax', 'demure', 'turbulence', 'gyatt']
starts = ['poggers', 'OwO', 'UwU', 'pookie', 'skibidi', 'let_him_cook', 'talktuah']

def interpret(filename):
    with open(filename) as file:
        lines = file.readlines()

    while_blocks = {}
    line_num = 0

    while line_num < len(lines):
        line = lines[line_num].strip()
        if line.startswith("skibidi"):
            condition = lines[line_num - 1].split("let_him_cook ")[1].strip().rstrip('{').replace("(", "").replace(")", "")
            start_line = line_num
            end_line = find_end_while(lines, line_num)
            while_blocks[start_line] = (condition, start_line, end_line)
            line_num = end_line
        line_num += 1

    line_num = 1
    minLines = min(while_blocks.keys()) - 1 if while_blocks else len(lines)
    for line in lines[:minLines]:
        if line.startswith("pookie "):
            definition = line.split("pookie ")[1]
            var, val = definition.split("rizzing")
            var = var.replace(" ","").replace("\n","")
            val = val.replace("\n","")
            val = math_parse(val)
            s[var] = val
        elif line.startswith("talktuah("):
            print_text = line.split("talktuah")[1].replace("(","").replace(")","").replace("\n","")
            if "\"" in print_text:
                print_text = print_text.replace("\"","")
                print(print_text)
            else:
                variable_name = print_text
                val = s[variable_name]
                print(val)
        elif line.startswith("UwU ") or line.startswith("OwO ") or line.startswith("poggers "):
            interpret_body(line, -1)
        else:
            url = "https://static.wikia.nocookie.net/amongus-fictional-entities/images/8/80/Static-assets-upload2210855008168198565.webp/revision/latest?cb=20230522055257"
            webbrowser.open(url)
            raise SyntaxError("Sussy Syntax on line " + str(line_num))
        line_num += 1
    global ifOccurred
    global elifOccurred
    for start_line, (condition, start, end) in while_blocks.items():
        while eval_expression(condition):
            ifOccurred, elifOccurred = False, False
            for line_num in range(start + 1, end):
                interpret_body(lines, line_num)

def find_end_while(lines, start):
    """ Find the corresponding end line for a while loop. """
    for line_num in range(start + 1, len(lines)):
        line = lines[line_num].strip()
        if line.startswith("}toilet"):
            return line_num
    url = "https://media1.tenor.com/m/lS_PA8oiqk8AAAAC/memes-fish.gif"
    webbrowser.open(url)
    raise SyntaxError("Womp Womp")

def interpret_body(lines, line_num):
    global ifOccurred
    global elifOccurred
    if line_num != -1:
        line = lines[line_num].strip()
    else:
        line = lines
    if line.startswith("pookie "):
        definition = line.split("pookie ")[1]
        var, val = definition.split("rizzing")
        var = var.strip()
        val = val.strip()
        val = math_parse(val)
        s[var] = val
    elif line.startswith("talktuah"):
        print_text = line.split("talktuah")[1].strip().replace("(", "").replace(")", "").strip()
        if "\"" in print_text:
            print_text = print_text.replace("\"", "")
            print(print_text)
        else:
            variable_name = print_text.strip()
            val = s.get(variable_name, None)
            if val is not None:
                print(val)
            else:
                print(f"Variable '{variable_name}' is not Him.")
    elif line.startswith("UwU "):
        condition = line[line.find('(') + 1:line.find(')')].strip()
        if eval_expression(condition):
            ifOccurred = True
            execute = line[line.find('{') + 1:line.find('}')].strip()
            interpret_body(execute, -1)
    elif line.startswith("OwO ") and not ifOccurred:
        condition = line[line.find('(') + 1:line.find(')')].strip()
        if eval_expression(condition):
            elifOccurred = True
            line_num += 1
            execute = line[line.find('{') + 1:line.find('}')].strip()
            interpret_body(execute, -1)
    elif line.startswith("poggers") and not ifOccurred and not elifOccurred:
        line_num += 1
        execute = line[line.find('{') + 1:line.find('}')].strip()
        interpret_body(execute, -1)
    elif not any([line.startswith(word) for word in starts]):
        url = "https://static.wikia.nocookie.net/amongus-fictional-entities/images/8/80/Static-assets-upload2210855008168198565.webp/revision/latest?cb=20230522055257"
        webbrowser.open(url)
        url = "https://www.youtube.com/watch?v=_-CzeGEmfwQ"
        webbrowser.open(url)
        raise SyntaxError("Sussy Syntax on line " + str(line_num + 1))

def is_float(element):
    try:
        float(element)
        return True
    except ValueError:
        return False

def math_parse(input):
    input = input.strip()

    comparison_operators = ["giga_chad", "vibe_check", "beta_male", "sigma_male", "beta", "sigma", "rizz"]
    if "rizz" in input:
        left, right = input.split("rizz", 1)
        return eval_expression(left.strip()) and eval_expression(right.strip())
    for op in comparison_operators:
        if op in input:
            left, right = input.split(op, 1)
            left_val = eval_expression(left.strip())
            right_val = eval_expression(right.strip())
            return compare_values(left_val, right_val, op)

    tokens = []
    current_token = []
    for char in input.split(' '):
        if char in operators:
            if current_token:
                tokens.append(''.join(current_token).strip())
                current_token = []
            tokens.append(char)
        elif char != ' ':
            current_token.append(char)
    if current_token:
        tokens.append(''.join(current_token).strip())


    return evaluate_tokens(tokens)

def evaluate_tokens(tokens):
    for ti in range(len(tokens)):
        if tokens[ti] in s:
            tokens[ti] = s[tokens[ti]]
        elif is_float(tokens[ti]):
            tokens[ti] = float(tokens[ti])
        elif tokens[ti] not in operators and tokens[ti] != 'Aura' and tokens[ti] != 'L_Rizz':
            url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUXbmV2ZXIgZ29ubmEgZ2l2ZSB5b3UgdXA%3D"
            webbrowser.open(url)
            raise NameError("Candice '" + tokens[ti] + "' is the Imposter.")

    i = 0
    while i < len(tokens):
        if isinstance(tokens[i], str) and tokens[i] == "demure":
            if tokens[i] == 'demure':
                result = tokens[i - 1] % tokens[i + 1]
            tokens[i - 1:i + 2] = [result]
            i = 0
        else:
            i += 1
    
    i = 0
    while i < len(tokens):
        if isinstance(tokens[i], str) and tokens[i] in ['gyatt', 'demure']:
            if tokens[i] == 'gyatt':
                result = tokens[i - 1] * tokens[i + 1]
            elif tokens[i] == 'demure':
                result = tokens[i - 1] / tokens[i + 1]
            tokens[i - 1:i + 2] = [result]
            i = 0
        else:
            i += 1

    i = 0
    while i < len(tokens):
        if isinstance(tokens[i], str) and tokens[i] in ['fanum_tax', 'mew_streak']:
            if tokens[i] == 'mew_streak':
                result = tokens[i - 1] + tokens[i + 1]
            elif tokens[i] == 'fanum_tax':
                result = tokens[i - 1] - tokens[i + 1]
            tokens[i - 1:i + 2] = [result]
            i = 0
        else:
            i += 1

    return tokens[0]

def eval_expression(expression):
    expression = expression.strip()
    if is_float(expression):
        return float(expression)
    elif expression in s:
        return s[expression]
    elif expression == "Aura":
        return True
    elif expression == "L_Rizz":
        return False
    else:
        return math_parse(expression)

def compare_values(left, right, operator):
    if operator == "giga_chad":
        return left == right
    elif operator == "vibe_check":
        return left != right
    elif operator == "beta_male":
        return left <= right
    elif operator == "sigma_male":
        return left >= right
    elif operator == "beta":
        return left < right
    elif operator == "sigma":
        return left > right
    else:
        url = "https://media1.tenor.com/m/5mp3o1MEuE0AAAAd/benjammins-cooked.gif"
        webbrowser.open(url)
        raise ValueError("Cooked.")

#interpret file command
interpret("brainrot.br")

interpret("looksmaxing.br")

interpret("spreadbrainrot.br")

imgur_url = "https://i.imgur.com/b880KIM.png"
webbrowser.open(imgur_url)
