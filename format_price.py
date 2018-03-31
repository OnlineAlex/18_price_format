import argparse


def parsing_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'price',
        type=float,
        help='Напишите цену товара'
    )
    return parser.parse_args()


def convert_price_float(unfloat_data):
    if type(unfloat_data) == str and unfloat_data.find(','):
        unfloat_data = unfloat_data.replace(',', '.')

    try:
        float_number = float(unfloat_data)
        return float_number
    except (ValueError, TypeError):
        return None


def format_price(price):
    if type(price) != float:
        price = convert_price_float(price)
        if not price:
            return None
    price_int_path = str(int(price))
    price_path = []

    while price_int_path:
        price_path.append(price_int_path[-3:])
        price_int_path = price_int_path[:-3]

    price_path.reverse()
    if not price.is_integer():
        price = str(price)
        fraction = price[price.find('.'):]
        price_path[-1] += fraction
    return ' '.join(price_path)


if __name__ == '__main__':
    price_str = parsing_arguments().price
    print(format_price(price_str))
