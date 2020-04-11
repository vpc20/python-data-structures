def bin_to_dec(bin_num):
    dec_val = 0
    dec_str = str(bin_num)
    len_str = len(dec_str)
    for i in range(len_str):
        dec_val += int(dec_str[i]) * 2**(len_str - i - 1)
    return dec_val


print(bin_to_dec(1010))
