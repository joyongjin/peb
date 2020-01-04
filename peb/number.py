import decimal


def half_round(num, fmt):
    """
    decimal_round(0.1235, '0.1') == 0.1
    decimal_round(0.1235, '0.01') == 0.12
    decimal_round(0.1235, '0.001') == 0.124
    decimal_round(0.1235, '0.0001') == 0.1235
    decimal_round(0.12345, '1') == 0.0
    """
    if fmt.find('.') >= 0:
        # Float
        n = decimal.Decimal(str(num)).quantize(decimal.Decimal(fmt), rounding=decimal.ROUND_HALF_UP)
        return float(n)
    else:
        # Integer
        pass


def clear_int(num, clear_with):
    clear_with = int('1'.zfill(intlen(clear_with)))

    if intlen(num) == intlen(clear_with):
        raise ValueError('You can not clear same length integer')
    return num // clear_with * clear_with


def intlen(num):
    return len(str(num))
