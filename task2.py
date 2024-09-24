alphabet = int(input())  # 26
many_symbols = int(input())  # 10
many_passwords = int(input())  # 50
bytes_for_symbol = 0
for i in range(1, alphabet // 2 + 1):
    if 2 ** i >= alphabet:
        bytes_for_symbol = i
        break
bytes_for_all_passwords = many_symbols * many_passwords * bytes_for_symbol
print(f"{bytes_for_all_passwords} битов")