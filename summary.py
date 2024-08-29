import csv
from collections import defaultdict


def calculate_product_totals(file_path):
    product_totals = {}

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            product = row["商品"]
            quantity = int(row["数"])
            if product in product_totals:
                product_totals[product] += quantity
            else:
                product_totals[product] = quantity

    return product_totals


def main():
    file_path = 'sales_data.csv'
    product_totals = calculate_product_totals(file_path)

    print("商品ごとの合計:")
    for product, total in product_totals.items():
        print(f"{product}: {total}")


if __name__ == '__main__':
    main()
