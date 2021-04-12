### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
# source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]
import os, tkinter, tkinter.filedialog, tkinter.messagebox

def source_from_csv():

    root = tkinter.Tk()
    root.withdraw()
    fTyp = [("","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    tkinter.messagebox.showinfo('csvファイル選択','csvファイルを選択してください')
    file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    if file[-3:] != 'csv':
        tkinter.messagebox.showinfo('Worning','csvファイルではありません')
        exit()
    else:
        return file

def yes_no_input():
    while True:
        choice = input("Please respond with 'yes' or 'no' [y/N]: ").lower()
        if choice in ['y', 'ye', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False

def source_select():
    if yes_no_input():
        path = source_from_csv()
        with open(path) as f:
            source = [s.strip() for s in f.readlines()]
    else:
        path = ""
        source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]
    return path, source

### 検索ツール
def search():
    print("csvからsourceを選択しますか？")
    path, source = source_select()
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    if word in source:
        print("{}が見つかりました".format(word))
    else:
        print("{}がいません".format(word))
        print("sourceに追加しますか？")
        if yes_no_input():
            source.append(word)
            print(source)
            if path != "":
                with open(path, mode='a') as f:
                    f.write('\n')
                    f.write(word)
        else:
            pass

if __name__ == "__main__":
    search()