# Highlight String Code

Highlight string as SQL, HTML, CSS or JavaScript in most languages.
在代码中，高亮 SQL、HTML、CSS 或者 JavaScript 代码。

## 文档

[English](https://github.com/iuyoy/highlight-string-code/blob/master/README.md) | [中文文档](https://github.com/iuyoy/highlight-string-code/blob/master/docs/README_CN.md)

## 需求

- 推荐使用Visual Studio Code v1.6.0及以上版本（可能不准确，用最新的应该没问题）

## 特性

- 语法高亮
- 按子语言的规则注释
- 括号高亮匹配
- 括号自动配合
- 快速输入代码块高亮标记对

## 用法

| 支持语言 | 代码块高亮标记对              | 代码块高亮标记对快捷键        | 备注                                                                                            |
| -------- | ----------------------------- | ----------------------------- | ----------------------------------------------------------------------------------------------- |
| SQL      | `--sql` & `;`                 | -                             |
| SQL      | `--beginsql`, `--endsql`      | `hsql`, `highlight-sql`       |
| SQL      | `--begin-sql`, `--end-sql`    | -                             |
| SQL      | UPPERCASE KEYWORD, `;`        | -                             |
| Hive SQL | `--hive`, `--!hive`           | `hhsql`, `highlight-hive-sql` | 需要插件[Hive SQL](https://marketplace.visualstudio.com/items?itemName=josephtbradley.hive-sql) |
| HTML     | `<!--html-->`, `<!--!html-->` | `hhtml`, `highlight-html`     |
| CSS      | `/*css*/`, `/*!css*/`         | `hcss`, `highlight-css`       |
| JS       | `//js`, `//!js`               | `hjs`, `highlight-javascript` |

- SQL
  1. 在 `--sql` 和 `;` 中插入单条SQL语句。<br>
  ![single SQL stirng with Sign](./single_SQL_with_Sign.png)
  2. 在以 `--beginsql` 或 `--begin-sql` 为开始，以 `--endsql` 或 `--end-sql` 为结束的代码块中插入多条SQL语句。 <br>
  ![multi SQL stirng with Sign](./multi_SQL_with_Sign.png)
  3. 任何以 **大写** SQL关键词 (比如 `SELECT`、 `INSERT`、 `UPDATE` 等等) 和一个**空白符** (`' ','\n','\t','\r'和'\f'`) 开始, 以 `;` 结束的字符串都会被自动高亮为SQL。<br>
  ![SQL stirng no Sign](./SQL_without_Sign.png)
- HTML, CSS, JS
  - 出现在标志 `<!--html-->` 和 `<!--!html-->`、 `/*css*/` 和 `/*!css*/` 以及 `//js` 和 `//!js` 中的代码会分别被高亮为 HTML、 CSS 或者 JS。其他注释可以出现在 *标志语言* 之后。<br>
  ![HTML with Sign](./HTML_with_Sign.png)
- 其他
  - 在嵌套语言是 `SQL` 和 `HTML` 的代码中，高亮 `{` 和 `}` 中出现的变量。本意是给 PYTHON 和 SHELL 用的，但是目前对所有的语言都生效。<br>
  ![Variables](./SQL_with_variable.png)
- 快速输入代码块高亮标记对
  - 输入 `h{language_abbr}` 或 `highlight-{language_name}` 来插入用于高亮代码的代码块标记对。例如， 输入 `hjs` 或者 `highlight-javascript` 来快速插入 `// js` 和 `// !js`。
  ![Snippets](./hjs-snippets.png)

## 安装

- 从 VS Code extensions 安装(在 win 中按下 `ctrl + shift + x` 或者在mac 中按下 `cmd + shift + x`)。
- 从 [VSIX](https://github.com/iuyoy/highlight-string-code/releases) 文件手动安装。

## 更新日志

见 [CHANGELOG.md](./CHANGELOG.md)

## 疑问？

如果你有任何疑问或者建议，请在[Github Issues](https://github.com/iuyoy/highlight-string-code/issues)页面提出 Issue 。

## 参考

- Forked from [bashmish/es6-string-css](https://github.com/bashmish/es6-string-css) > [ptweir/python-string-sql](https://github.com/ptweir/python-string-sql)
- Visual Studio Code Extension API
  - [syntax-highlight-guide](https://code.visualstudio.com/api/language-extensions/syntax-highlight-guide)
  - [language identifiers](https://code.visualstudio.com/docs/languages/identifiers)
- TextMate 手册
  - [Language Grammars](https://macromates.com/manual/en/language_grammars)
  - [Scope Selectors](https://macromates.com/manual/en/scope_selectors)
- Issue [Highlighting of fenced code in markdown for known but non-default languages](https://github.com/microsoft/vscode/issues/71888)
  - [vscode-fenced-code-block-grammar-injection-example](https://github.com/mjbvz/vscode-fenced-code-block-grammar-injection-example)
  - [vscode-comment-tagged-templates](https://github.com/mjbvz/vscode-comment-tagged-templates)
