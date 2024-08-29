"""
このモジュールは、sales_data.csvファイルのレコードを修正するための関数を提供します。
ユーザーは修正したいレコードのIDを入力し、各フィールドの新しい値を入力することで
レコードを更新できます。

関数:
   - get_record_by_id(file_path, record_id):
       指定されたIDを持つレコードをCSVファイルから取得します。

   - update_record(file_path, record_id, updated_data):
       指定されたIDを持つレコードを、updated_dataの内容で更新します。
       更新後のデータでCSVファイルを上書きします。

   - main():
       ユーザーにレコードIDと更新内容を入力させ、レコードを更新します。

使用例:
   python sales_data_updater.py
"""

import csv


def get_record_by_id(file_path, record_id):
    """
    指定されたIDを持つレコードをCSVファイルから取得します。

    Args:
        file_path (str): 読み込むCSVファイルのパス。
        record_id (str): 取得したいレコードのID。

    Returns:
        dict: 指定されたIDを持つレコードの辞書。見つからない場合はNone。
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == record_id:
                return row
    return None


def update_record(file_path, record_id, updated_data):
    """
    指定されたIDを持つレコードを、updated_dataの内容で更新します。
    更新後のデータでCSVファイルを上書きします。

    Args:
        file_path (str): 読み書きするCSVファイルのパス。
        record_id (str): 更新するレコードのID。
        updated_data (dict): 更新内容の辞書。キーはフィールド名、値は新しい値。

    Returns:
        None
    """
    records = []

    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == record_id:
                row.update(updated_data)  # 指定されたレコードを更新
            records.append(row)

    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        fieldnames = ['id', '日付', '会社名', '商品', '数']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # ヘッダー行を書き込み
        writer.writerows(records)  # 更新後のレコードを書き込み


def main():
    """
    ユーザーにレコードIDと更新内容を入力させ、レコードを更新します。
    """
    file_path = 'sales_data.csv'
    record_id = input("修正するレコードのIDを入力してください: ")
    record = get_record_by_id(file_path, record_id)

    updated_data = {}
    print("修正する項目を入力してください（空白のままEnterを押すと修正しません）:")
    for field in ['日付', '会社名', '商品', '数']:
        current_value = record[field]
        value = input(f"{field} [{current_value}]: ")
        if value:
            updated_data[field] = value

    update_record(file_path, record_id, updated_data)
    print("レコードが修正されました。")


if __name__ == '__main__':
    main()
