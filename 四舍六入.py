# 文件名
# @author: Ma Yilin
def four_six_round(number, decimals=1):
    # 将数字转换为字符串，便于操作小数点后的每一位
    num_str = f"{number:f}"
    # 获取小数部分
    decimal_part = num_str.split('.')[1]

    # 获取要舍入部分的第一位
    rounding_digit = int(decimal_part[decimals])
    # 获取舍去部分第一位之后的数字
    following_digits = decimal_part[decimals + 1:] if decimals < len(decimal_part) - 1 else ''

    # 根据规则进行判断和处理
    if rounding_digit <= 4:
        # 四舍：直接截断
        rounded_num = float(num_str[:num_str.index('.') + decimals + 1])
    elif rounding_digit >= 6:
        # 六入：进位
        rounded_num = round(float(num_str[:num_str.index('.') + decimals+1]) + 0.1 ** decimals,decimals)
    elif rounding_digit == 5:
        # 五的处理
        if following_digits != '0' * len(following_digits):  # 五后非零则进一
            rounded_num = round(float(num_str[:num_str.index('.') + decimals+1]) + 0.1 ** decimals,decimals)
        else:  # 五后皆零，看前一位奇偶
            before_digit = int(decimal_part[decimals-1])
            if before_digit % 2 == 1:  # 前一位是奇数则进一
                rounded_num = round(float(num_str[:num_str.index('.') + decimals+1]) + 0.1 ** decimals,decimals)
            else:  # 前一位是偶数则不进
                rounded_num = float(num_str[:num_str.index('.') + decimals + 1])
    return rounded_num


# 测试函数
print(four_six_round(5.185000))  # 应输出5.8
print(four_six_round(5.18632))  # 应输出5.9
print(four_six_round(5.18501))  # 应输出5.9
print(four_six_round(5.18500))  # 应输出5.8
print(four_six_round(5.17500))  # 应输出5.8