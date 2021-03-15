## extracting zip with password
import zipfile
from tqdm import tqdm

def main():
    file_name = r'D:\pswd_file.zip'
    zip_file = zipfile.ZipFile(file_name)
    wordlist = r"D:\data science\crackstation\wordlist.txt"
    pswd = 'datacamp'

    # count the number of words in this wordlist
    n_words = len(list(open(wordlist, "rb")))
    # print the total number of passwords
    print("Total passwords to test:", n_words)

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