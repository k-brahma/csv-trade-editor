import csv
from datetime import datetime


def main():
    # CSVファイルのパスを指定
    csv_file = "sales_data.csv"

    # 日付の入力を求める
    date_str = input("取引日付を入力してください (YYYY/MM/DD): ")

    try:
        # 入力された日付を datetime オブジェクトに変換
        target_date = datetime.strptime(date_str, "%Y/%m/%d")

        # CSVファイルを読み込む
        with open(csv_file, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            # ヘッダーを出力
            print("id,会社名,商品,数")

            # 各行を処理
            for row in reader:
                # CSVの日付を datetime オブジェクトに変換
                row_date = datetime.strptime(row["日付"], "%Y/%m/%d")

                # 指定された日付と一致する行だけを出力
                if row_date.date() == target_date.date():
                    print(f"{row['id']},{row['会社名']},{row['商品']},{row['数']}")

    except ValueError:
        print("無効な日付形式です。YYYY/MM/DD の形式で入力してください。")


if __name__ == "__main__":
    main()
