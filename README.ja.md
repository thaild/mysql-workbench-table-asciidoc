# mysql-workbench-table-asciidoc

AsciiDoc でスキーマの定義書を生成するための MySQL Workbench のプラグインです。

[en](README.md) / [ja](README.ja.md)

## インストール

- レポジトリを `clone` またはファイル( `mysql-workbench-table-asciidoc.py` )を直接ダウンロード。
- ワークベンチのメニューで `Go to Scripting` > `Install plugin/module` を選択。
- mysql-workbench-table-asciidoc.py を選択してインストール。

## 使い方

- MySQLWorkbench で EER ダイアグラムを作成/読み込む。
- `Tools` > `Utilities` > `Generate Schema Documentation in Asciidoc.` を選択。
- AsciiDoc がクリップボードにコピーされる。

## その他

- EER 図は MySQL Workbench を使用して物理データベースからリバースエンジニアリングが可能。
- スクリプトは MySQL Workbench v8.0.18 で動作確認済。
- デバッグに使用した Python バージョン 2.7.16。

## ライセンス

このスクリプトは、MIT ライセンスの下でリリースされています。
