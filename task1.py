alphabet = int(input())  # 16
strs = int(input())  # 65
letters = int(input())  # 156
bytes_for_symbol = 0
for i in range(1, alphabet // 2 + 1):
    if 2 ** i == alphabet:
        bytes_for_symbol = i
bytes_on_page = strs * letters * bytes_for_symbol
print(f"{bytes_on_page} битов")