import urllib.request
import json

# ১. লাইব্রেরি ছাড়া কুরআন ডাটা আনার ফাংশন
def get_quran_verse(surah, ayah):
    url = f"https://api.alquran.cloud/v1/ayah/{surah}:{ayah}/bn.bengali"
    try:
        # requests এর বদলে urllib ব্যবহার
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            if data['status'] == 'OK':
                return data['data']['text']
            return "সানি ভাই, আয়াতটি পাওয়া যায়নি।"
    except Exception as e:
        return "ইন্টারনেট কানেকশন বা কোডে সমস্যা হয়েছে।"

# ২. চ্যাটবট শুরু
print("--- সানি ভাইয়ের লাইব্রেরি-ফ্রি ইসলামিক AI ---")
print("আসসালামু আলাইকুম সানি ভাই! ৩ বছরের তথ্য নিয়ে আমি তৈরি।")

while True:
    print("\n১. কুরআনের আয়াত দেখুন")
    print("২. বিদায় নিন")
    
    choice = input("আপনার চয়েস (১/২): ")
    
    if choice == '1':
        s = input("সূরা নম্বর দিন: ")
        a = input("আয়াত নম্বর দিন: ")
        print("\nফলাফল: ", get_quran_verse(s, a))
    elif choice == '2':
        print("আল্লাহ হাফেজ সানি ভাই! ডি মারিয়ার মতো চিল করুন।")
        break
