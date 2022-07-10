import subprocess
import hashlib
import requests

wallet = 4
originals_path = "/home/gneale/Programming/nft0/files/originals/"

def create_nft(num, nlink, mlink, wallet):
    
    try:
        result = subprocess.run(["chia", "wallet", "nft", "mint", 
        "-f","790396907",
        "-i", str(wallet),
        "-ra", "txch150trmj9g08555k3qaptn0sl5dseq0recwmvgn73cdtch2dc3t0ksjuespy",
        "-ta", "txch150trmj9g08555k3qaptn0sl5dseq0recwmvgn73cdtch2dc3t0ksjuespy",
        "-u", nlink,
        "-nh", "cfb48193d9c8ab7c9585c9653430c95c5fc0d1d17aa4a45aad63548602eb47d7", 
        "-mu", mlink,
        "-mh", "f7fb3c5fd263a3b0845c0122555179f3ceb6a3091da48065df90aaea86531118",
        "-lu", "https://raw.githubusercontent.com/Chia-Network/chia-blockchain/main/LICENSE",
        "-lh", "30a358857da6b49f57cfe819c1ca43bfe007f528eb784df5da5cb64577e0ffc6", 
        "-sn", str(num), "-st", "726", 
        "-rp", str(num), "-m" "0.0001"
        ])
    finally:
        print("stdout:", result.stdout)
        print("stderr:", result.stderr)

def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+" (y/n): ")).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False
        else:
            return yes_or_no("Please re-enter")

def get_online_hash(image_number, url, filename):
     response = requests.get(url)
     filename = filename + "tmp"
     open(filename, "wb").write(response.content)
     with open(filename,"rb") as f:
          bytes = f.read()
          readable_hash = hashlib.sha256(bytes).hexdigest()
          print("{} hash: {}".format(filename, readable_hash))
          return readable_hash         

def get_local_hash(image_number, originals_path, filename):
     
     with open(originals_path + filename,"rb") as f:
          bytes = f.read()
          readable_hash = hashlib.sha256(bytes).hexdigest()
          print("{} hash: {}".format(filename, readable_hash))
          return readable_hash                        

if __name__=='__main__':
    for num in range(10,100):
        for ext in ["png","json"]:
            filename = "gneale-san_francisco{}.{}".format(num, ext)
            url = "https://mojopuzzler.org/nft/gnsf/gneale-san_francisco{}.{}".format(num, ext)
            if get_online_hash(num, url, filename) != get_local_hash(num, originals_path, filename):
                print("{} file number {} hash does NOT successfully match.".format(ext,num))

        yn = yes_or_no("Would you like to make NFT # {}".format(num))
        if yn:
            nlink = "https://mojopuzzler.org/nft/gnsf/gneale-san_francisco{}.png".format(num)
            mlink = "https://mojopuzzler.org/nft/gnsf/gneale-san_francisco{}.json".format(num)
            create_nft(num, nlink, mlink, wallet)
