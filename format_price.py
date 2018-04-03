import argparse


def get_price():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'price',
        type=float,
        help='Напишите цену товара'
    )
    return parser.parse_args()


def format_price(price):
    if type(price) == bool:
        return None
    try:
        price = float(price)
    except (ValueError, TypeError):
        return None

    if price.is_integer():
        price_format_str = '{:_.0f}'.format(price)
    else:
        price_format_str = '{:_.2f}'.format(price)

    pretty_price = price_format_str.replace('_', ' ')
    return pretty_price


if __name__ == '__main__':
    price_str = get_price().price
    formatted_price = format_price(price_str)
    if formatted_price:
        print(formatted_price)
    else:
        print('Цена указанна не верно')
