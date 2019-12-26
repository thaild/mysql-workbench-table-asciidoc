# mysql-workbench-table-asciidoc

A mysql workbench plugin for generating db schema design document in AsciiDoc.

[en](README.md) / [ja](README.ja.md)

## Installation

- Git clone the repository or directly download the file `mysql-workbench-table-asciidoc.py` from the repository.
- Select `Scripting` > `Install plugin/module` in the menu in MySQLWorkbench.
- Select mysql-workbench-table-asciidoc.py to install

## How to use

- Create/Load table EER diagram on MySQLWorkbench.
- Select `Tools` > `Utilities` > `Generate Schema Documentation in Asciidoc.` in the menu in MySQLWorkbench.
- Generated text should be copied to the clipboard.

## Note

- EER diagram can be reverse engineered from phsical database with MySQL Workbench.
- Script has been tested with MySQL Workbench v8.0.18.
- Virtualenv Python version 2.7.16 used for debugging.

## License

This script is released under the MIT license.
