# Git環境構築手順

## GitLabサーバー起動手順

1. 以下データが存在する場合は、それらを削除する。  

      - '/srv/gitlab/config:/etc/gitlab'
      - '/srv/gitlab/logs:/var/log/gitlab'
      - '/srv/gitlab/data:/var/opt/gitlab'

1. docker-composeをインストールする。

  ```
  $ sudo apt install docker-compose -y
  ```

1. docker-compose.yamlと同じ階層に移動し、以下コマンドを実行する。

  ```shell
  $ docker compose up -d
  ```

1. Google Chromeを起動し、「http://localhost:20080」にアクセスする。  

1. /etc/gitlab/initial_root_passwordで初期パスワードを確認する。  

   ```
   $  docker exec git_env-web-1 cat /etc/gitlab/initial_root_password
   ```

1. ユーザ名(root)とパスワード(initila_root_password)でログインする。  
  
## Gitクライアント設定手順

1. sshキーを作成する。

  ```
  $ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
  ```

2. 以下に作成したSSHキー(*.pub)を登録する。

  http://localhost:20080/-/profile/keys

