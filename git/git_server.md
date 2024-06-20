# GitaLabサーバー

## GitLabサーバー起動手順

1. docker-compose.yamlと同じ階層に移動し、以下コマンドを実行する。

  ```shell
  $ docker compose up d
  ```

1. Google Chromeを起動し、「http://localhost:20080」にアクセスする。  

1. /etc/gitlab/initial_root_passwordで初期パスワードを確認する。  

1. ユーザ名(root)とパスワード(initila_root_password)でログインする。  
