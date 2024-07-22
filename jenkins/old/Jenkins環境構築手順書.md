# Jenkins環境構築手順 WSL編

## Jenkinsマスターの環境構築

1. jenkins_build.shをWSL上で実行する。  

   ```
   $ sh jenkins_build.sh
   ```
```
version: '3.3'

services:
  gitlab:
    image: gitlab/gitlab-ce:latest
    container_name: gitlab
    hostname: localhost
    environment:
      GITLAB_OMNIBUS_CONFIG: |
        external_url 'http://localhost'
        gitlab_rails['lfs_enabled'] = true
        gitlab_rails['gitlab_shell_ssh_port'] = 22
        gitlab_rails['gitlab_shell_ssh_host'] = 'localhost'
        nginx['listen_port'] = 80
        nginx['listen_https'] = false
    ports:
      - "80:80"
      - "22:22"
    volumes:
      - gitlab_data:/var/opt/gitlab
      - gitlab_logs:/var/log/gitlab
      - gitlab_config:/etc/gitlab

  jenkins:
    image: jenkins/jenkins:lts
    container_name: jenkins
    ports:
      - "8080:8080"
      - "50000:50000"
    volumes:
      - jenkins_home:/var/jenkins_home

volumes:
  gitlab_data:
  gitlab_logs:
  gitlab_config:
  jenkins_home:

```

2. 

## Jenkinsスレーブの環境構築

