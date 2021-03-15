## extracting zip with password
import zipfile
from tqdm import tqdm
import os

def main():
    filepath = r"D:\git_repo\wpa2-wordlists\Wordlists"
    file_name = r'D:\pswd_file.zip'
    zip_file = zipfile.ZipFile(file_name)
    #wordlist = r"D:\data science\crackstation\wordlist.txt"
    #pswd = 'datacamp'

    for root, dir, filename in os.walk(filepath):
        for file in filename:
            if file.endswith('.txt'):
                wordlist = os.path.join(root, file)

                # count the number of words in this wordlist
                n_words = len(list(open(wordlist, "rb")))
                # print the total number of passwords
                print("Total passwords to test:", n_words, "in file: ", wordlist)

                with open(wordlist, "rb") as wordlist:
                    for word in tqdm(wordlist, total=n_words, unit="word"):
                        try:
                            zip_file.extractall(pwd=word.strip())
                        except:
                            continue
                        else:
                            print("[+] Password found:", word.decode().strip())
                            exit(0)
                print("[!] Password not found, try other wordlist.")

if __name__ == '__main__': main()