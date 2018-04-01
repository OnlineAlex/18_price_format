import argparse


def get_price():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'price',
        type=float,
        help='Напишите цену товара'
    )
    return parser.parse_args().price


def format_price(price):
    if type(price) == bool:
        return None
    if type(price) != float:
        try:
            price = float(price)
        except (ValueError, TypeError):
            return None

    if price.is_integer():
        price_format_str = '{:_.0f}'.format(price)
    else:
        price_format_str = '{:_.2f}'.format(price)

    price_show = price_format_str.replace('_', ' ')
    return price_show


if __name__ == '__main__':
    price_str = get_price()
    print(format_price(price_str))
