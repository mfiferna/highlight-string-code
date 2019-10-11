import os
import json

ext_folder = '/Applications/Visual Studio Code.app/Contents/Resources/app/extensions'


def getBuiltinLanguageInfo():
    exts = os.listdir(ext_folder)
    with open('scopename.md', 'w') as out:
        out.write('# Language ScopeName\n\n|language|scopeName|\n|---|---|\n')
        for ext in exts:
            pkg_path = os.path.join(ext_folder, ext, 'package.json')
            if os.path.isfile(pkg_path):
                pkg = json.load(open(pkg_path, 'r'))
                try:
                    if 'contributes' in pkg and 'grammars' in pkg['contributes']:
                        for grammar in pkg['contributes']['grammars']:
                            if 'language' in grammar:
                                out.write(f"|{grammar['language']}|{grammar['scopeName']}|\n")
                            else:
                                out.write(f"|{ext}|{grammar['scopeName']}|\n")


                
                    # for language in pkg['contributes']['languages']:
                    #     # print(language)
                    #     pass
                    # for grammar in pkg['contributes']['grammars']:
                    #     # print(grammar['language'], grammar['scopeName'])
                    #     out.write(f"|{grammar['language']}|{grammar['scopeName']}|\n")
                except Exception as e:
                    # print(e)
                    print(ext, e)
                    pass


if __name__ == "__main__":
    getBuiltinLanguageInfo()