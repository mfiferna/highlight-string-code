# Highlight String Code

Highlight string as SQL, HTML, CSS or JavaScript in most languages.

## Requirements

- Visual Studio Code v1.6.0 and above is recommended, but I'm not sure.

## Features

- Highlighting
- Commenting
- Bracket matching
- Closing pairs
- Snippet selection

## Usages
- SQL
  1. Insert sign pair `--sql` and `;` to highlight one SQL sequence.<br>
  ![single SQL stirng with Sign](./docs/single_SQL_with_Sign.png)
  2. Insert sign pair `--beginsql` or `--begin-sql` and `--endsql` or `--end-sql` to highlight one and more SQL suquences.<br>
  ![multi SQL stirng with Sign](./docs/multi_SQL_with_Sign.png)
  3. Any SQL sequence starts with **UPPERCASE** keyword (such as `SELECT`, `INSERT`, `UPDATE` and etc) and one of **WHITESPACE** character(such as `' ','\n','\t','\r','\f'`), and ends with `;` will be highlighted automatically.<br>
  ![SQL stirng no Sign](./docs/SQL_without_Sign.png)
- HTML, CSS, JS
  - Insert sign pairs `<!--html-->` and `<!--!html-->`, `/*css*/` and `/*!css*/`, `//js` and `//!js` to highlight one and more HTML suquences. Other comments can be added after *language name*.<br>
  ![HTML with Sign](./docs/HTML_with_Sign.png)
- Other
  - Highlight Variables in *highlighted* string code for `SQL` and `HTML`<br>
  ![Variables](./docs/SQL_with_variable.png)

## Installation

- Install from VS Code extensions (`ctrl + shift + x` or `cmd + shift + x` on mac).
- Install from [VSIX](https://github.com/iuyoy/highlight-string-code/releases) manually.

## Release Notes

See [CHANGELOG.md](./CHANGELOG.md)

## Issues
If you have any suggestion or issue, please feel free to subbmit it at [Repo Issues](https://github.com/iuyoy/highlight-string-code/issues)

## References

- Forked from [bashmish/es6-string-css](https://github.com/bashmish/es6-string-css) > [ptweir/python-string-sql](https://github.com/ptweir/python-string-sql)
- Visual Studio Code Extension API
  - [syntax-highlight-guide](https://code.visualstudio.com/api/language-extensions/syntax-highlight-guide)
  - [language identifiers](https://code.visualstudio.com/docs/languages/identifiers)
- TextMate Manual
  - [Language Grammars](https://macromates.com/manual/en/language_grammars)
  - [Scope Selectors](https://macromates.com/manual/en/scope_selectors)
- Issue [Highlighting of fenced code in markdown for known but non-default languages](https://github.com/microsoft/vscode/issues/71888)
  - [vscode-fenced-code-block-grammar-injection-example](https://github.com/mjbvz/vscode-fenced-code-block-grammar-injection-example)
  - [vscode-comment-tagged-templates](https://github.com/mjbvz/vscode-comment-tagged-templates)