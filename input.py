import csv
import os

CSV_FILE = 'sales_data.csv'


def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['id', '日付', '会社名', '商品', '数'])


def get_next_id():
    with open(CSV_FILE, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # ヘッダーをスキップ
        return sum(1 for _ in reader) + 1


def add_entry():
    date = input("日付を入力してください (例: 2024/8/29): ")
    company = input("会社名を入力してください: ")
    product = input("商品名を入力してください: ")
    quantity = input("数量を入力してください: ")

    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([get_next_id(), date, company, product, quantity])

    print("エントリーが追加されました。")


def main():
    initialize_csv()
    print("CSVファイルにデータを追加します。")
    add_entry()
    print("データが正常に追加されました。アプリケーションを終了します。")


if __name__ == "__main__":
    main()
