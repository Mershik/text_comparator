def compare_texts(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        text1 = file1.read()
        text2 = file2.read()

    differences = []
    for line_num, (line1, line2) in enumerate(zip(text1.splitlines(), text2.splitlines()), start=1):
        if line1 != line2:
            differences.append(f"Line {line_num}:\n- {line1}\n+ {line2}")
    
    return differences