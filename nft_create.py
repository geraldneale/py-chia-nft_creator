import subprocess
import hashlib
import requests

fprint = "790396907"
wallet = 4
originals_path = "./files/originals/"
tmp_files__path = "./files/"
royalty_address = "txch150trmj9g08555k3qaptn0sl5dseq0recwmvgn73cdtch2dc3t0ksjuespy"
target_address = "txch150trmj9g08555k3qaptn0sl5dseq0recwmvgn73cdtch2dc3t0ksjuespy"
lower_limit, upper_limit = 50, 53
series_total = 726


def create_nft(num, nlink, mlink, wallet, nhash, mhash):
    
    try:
        result = subprocess.run(["chia", "wallet", "nft", "mint", 
        "-f", fprint,
        "-i", str(wallet),
        "-ra", royalty_address,
        "-ta", target_address,
        "-u", nlink,
        "-nh", nhash, 
        "-mu", mlink,
        "-mh", mhash,
        "-lu", "https://raw.githubusercontent.com/Chia-Network/chia-blockchain/main/LICENSE",
        "-lh", "30a358857da6b49f57cfe819c1ca43bfe007f528eb784df5da5cb64577e0ffc6", 
        "-sn", str(num), "-st", str(series_total), 
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
     filename = tmp_files__path + filename + "_local.tmp"
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
    for num in range(lower_limit, upper_limit):
        for ext in ["png","json"]:
            filename = "gneale-san_francisco{}.{}".format(num, ext)
            url = "https://mojopuzzler.org/nft/gnsf/gneale-san_francisco{}.{}".format(num, ext)
            online_hash = get_online_hash(num, url, filename)
            local_hash = get_local_hash(num, originals_path, filename)
            if online_hash != local_hash:
                print("{} file number {} hash does NOT successfully match.".format(ext,num))
            if ext == "png":
                nhash = online_hash
            else:
                mhash = online_hash        

        yn = yes_or_no("Would you like to make NFT # {}".format(num))
        if yn:
            nlink = "https://mojopuzzler.org/nft/gnsf/gneale-san_francisco{}.png".format(num)
            mlink = "https://mojopuzzler.org/nft/gnsf/gneale-san_francisco{}.json".format(num)
            create_nft(num, nlink, mlink, wallet, nhash, mhash)
        else:
            break    
