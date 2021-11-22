datalist = ["John", "Marta", "James", "Amanda", "Marianna"]
line_width = 21
first_line = "Names".center(line_width, '*')
line_format = '{:>21}\n' * len(datalist)
all_lines_nf = f'{first_line}\n{line_format}'
print_text = all_lines_nf.format(*datalist)
print(print_text)