# DB
## データベースについて
データベース名は、アプリ名と同じく「UMIRU」となっている。

## テーブルについて
このデータベースのテーブルは、ASARIから得た情報をまとめたものである。

テーブル名は、「"場所"_"タンク名"」で構成され、テーブルの中身は固定となっている。

テーブルの中身は、以下のようになる。dtは情報取得日時、tempは水温、shibuは塩分濃度、condactは伝導率、do_perは、溶存酸素量のパーセンテージ表記、do_mgは溶存酸素量のmg/L表記となっている。

```mysql
+---------+----------+------+-----+---------+-------+
| Field   | Type     | Null | Key | Default | Extra |
+---------+----------+------+-----+---------+-------+
| dt      | datetime | YES  |     | NULL    |       |
| temp    | float    | YES  |     | NULL    |       |
| shibu   | float    | YES  |     | NULL    |       |
| condact | float    | YES  |     | NULL    |       |
| do_per  | float    | YES  |     | NULL    |       |
| do_mg   | float    | YES  |     | NULL    |       |
+---------+----------+------+-----+---------+-------+
```

## CSVからデータをインポートする方法
1. 「2_insert_data.py」を実行する。
   ```winbatch
   # 実行コマンド
   python 2_insert_data.py
   ```

   もし、実行に必要なライブラリがない場合、以下を実行する
   ```winbatch
   pip install pymysql
   pip install tkinter
   ```
