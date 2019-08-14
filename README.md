[English Ver.](#english)
[Japanese Ver.](#japanese)

<a name="english"/>

# TODO APP (English Ver.)

This web applicaiton is designed to help you check out things you want to do. 

## Built With

Python 3.6 and Django 2.0

### Libraries 

* **Django libraries** - django.shortcuts django.db.models django.utils django.contrib django.http django.urls

* **Python libraries** - datetime

## Usage and Design

After creating todo lists, you could add todos under them. 
You need to give title and deadline to todos before you can create them.
Each todo has a button that indicates the status whether or not it is completed. 
If you click the button, the status will be reversed. 
At the bottom of the todo detail page, whose url ends with "*/detail/todolist_id/*", you can find two buttons.
First one deletes the todo list this todo belongs to. Second one deletes completed todos in the same todo list.  
Searching for todo lists and todos are also possible by clicking the link on the top-right corner.

## Set up Development Environment

First, clone this repository from github.

```bash
git clone https://github.com/shiiyan/Todo-App.git
```

After move to the main directory of this app, run

```bash
cd myproject
python manage.py runserver
```

and you are ready to go.

---
<a name="japanese"/>

# TODO APP（日本語版）

## 開発背景・目的

- ユーザーのTODOからストレス度合いを検知、過度なストレスを防ぐため
- 夏休みの宿題を最後の一日にやる病を治すため

## ER図

![TODOAPP_er](https://user-images.githubusercontent.com/36617009/62995138-44cc6e00-be9a-11e9-8d10-2f36d082ee8b.png)

## 特徴・オリジナル性

- ストレス感知機能

## 機能

- ストレス度合い通知機能
- TODO登録
- TODO詳細表示 
- TODO集計機能
- TODO検索機能
- ユーザーログイン機能
- 管理ユーザー追加・ログイン機能
- DBテーブルリレーション管理
- DBマイグレーション制御

### 実装する予定のある機能

- ユーザー新規登録
- 画像ファイルアップロード
- ページネーション
- 単体テストと統合テスト

## 使った技術

- Python Djangoフレームワーク
- SQLite DB
- フロントエンドのHTML CSS
- virtualenv仮想環境

## 実装環境

- EC2、pythonanywhere、herokuでホスティング

## 画面例

![スクリーンショット 2019-08-14 12 48 47](https://user-images.githubusercontent.com/36617009/62993540-adafe800-be92-11e9-8446-f9d332386cdb.png)
![スクリーンショット 2019-08-14 12 49 22](https://user-images.githubusercontent.com/36617009/62993541-adafe800-be92-11e9-8c26-8bbd98396486.png)
![スクリーンショット 2019-08-14 12 49 49](https://user-images.githubusercontent.com/36617009/62993544-adafe800-be92-11e9-9ba0-e195d47426aa.png)
![スクリーンショット 2019-08-14 12 51 43](https://user-images.githubusercontent.com/36617009/62993547-ae487e80-be92-11e9-9009-9c44c3381f20.png)
![スクリーンショット 2019-08-14 12 50 47](https://user-images.githubusercontent.com/36617009/62993546-ae487e80-be92-11e9-8fe8-a37d3f678e9a.png)
![スクリーンショット 2019-08-14 12 52 21](https://user-images.githubusercontent.com/36617009/62993549-ae487e80-be92-11e9-9f06-7ef353ae8f64.png)
![スクリーンショット 2019-08-14 12 52 12](https://user-images.githubusercontent.com/36617009/62993548-ae487e80-be92-11e9-8357-a4271e239924.png)
