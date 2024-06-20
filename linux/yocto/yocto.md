# Yocto Project

## Yoctoイメージ構築

### 参考図書 / Reference

- [brief-yoctoprojectqs](https://docs.yoctoproject.org/3.1/brief-yoctoprojectqs/brief-yoctoprojectqs.html)

### ビルド手順

pokyをローカルPCにダウンロードする。  

```bash
$ git clone git://git.yoctoproject.org/poky
```

pokyのタグ一覧を取得する。  

```bash
$ cd poky
$ git fetch --tags
$ git tag
```

バージョン3.1のyoctoに切り替える。  

```bash
$ git checkout tags/yocto-3.1 -b my-yocto-3.1
```

ビルド環境を初期化する。

```bash
$ source oe-init-build-env
```

必要なパッケージをインストールする。  

```bash
$ sudo apt install chrpath diffstat gawk
```

ビルドを開始する。  

```bash
$ bitbake core-image-sato
```

qemu-system-x86をインストールする。  

```shell
$ sudo apt install qemu-system-x86
```

qemuでイメージを起動する。  

```bash
$ qemu-system-x86_64 -kernel ./bzImage -drive file=./core-image-sato-qemux86-64.ext4,if=virtio,format=raw -append "root=/dev/vda rw console=ttyS0" -m 16384 -smp 4 -net nic -net user -nographic -display vnc=:2
```

```bash
runqemu qemux86-64
```

VNCクラインアントからVNCサーバーにアクセスする。  

## レイヤーの追加手順

## Tips

__bbファイルを検索する__

```bash
$ ls meta*/recipes*/*images/*.bb
```

## bblayer.confとlocal.confの相違点

Yocto Projectは、エンベデッドLinuxディストリビューションを構築するためのツールセットであり、bblayer.confとlocal.confはその中で重要なファイルです。

bblayer.confファイルは、ビルドに必要なレイヤーを定義するためのファイルであり、Yocto ProjectのビルドシステムであるBitBakeがレイヤーを検索するために使用されます。このファイルは、ビルドするために使用するメタレイヤーを含む、レイヤーのパスを指定します。

一方、local.confファイルは、ビルドをカスタマイズするためのファイルです。このファイルには、ビルドに必要な変数、パッケージ、ツール、およびビルドプロセスを制御する設定が含まれます。たとえば、カーネルのバージョン、クロスコンパイルツールチェインの場所、イメージファイルの名前、およびルートファイルシステムの場所を指定できます。

bblayer.confファイルは、ビルドシステムがレイヤーを見つけるために使用され、local.confファイルはビルドをカスタマイズするために使用されます。これらのファイルは、Yocto Projectのビルドプロセスを制御するために重要です。

