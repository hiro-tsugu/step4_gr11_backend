# step4_gr11_backend
Tech0のStep4でGr11のアプリ開発用のリポジトリ

実装予定のフォルダ構成は以下の通りです。
backend/
│── app/                      # アプリケーションの主要コード
│   ├── __init__.py           # Flaskアプリの初期化
│   ├── config.py             # 環境変数の管理
│   ├── models.py             # SQLAlchemyモデル（データベース定義）
│   ├── database.py           # DB接続設定
│   ├── routes/               # ルーティング関連
│   │   ├── __init__.py
│   │   ├── user_routes.py    # ユーザー関連API
│   │   ├── donation_routes.py # 寄付関連API
│   │   ├── municipality_routes.py # 自治体関連API : RFPで出した機能No.5はここに格納予定
│   │   ├── feedback_routes.py # フィードバック関連API
│   ├── services/             # ビジネスロジック層
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   ├── donation_service.py
│   ├── schemas/              # リクエスト/レスポンスのスキーマ定義
│   │   ├── __init__.py
│   │   ├── user_schema.py
│   │   ├── donation_schema.py
│   ├── utils/                # ユーティリティ関数
│   │   ├── __init__.py
│   │   ├── security.py        # パスワードハッシュ化、トークン管理
│── migrations/               # データベースのマイグレーション管理（Flask-Migrate）
│── tests/                    # テストコード
│   ├── __init__.py
│   ├── test_users.py         # ユーザーAPIのテスト
│── .env                      # 環境変数ファイル（DB接続情報など）
│── .gitignore                # Git管理しないファイルを定義
│── requirements.txt          # Pythonの依存ライブラリ一覧
│── run.py                    # アプリケーションのエントリーポイント
│── README.md                 # プロジェクトの説明
│── docker-compose.yml        # Dockerで開発環境を構築
│── Dockerfile                # Dockerイメージの設定
│── Makefile                  # 簡単なコマンド管理
