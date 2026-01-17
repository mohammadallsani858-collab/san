pip install requests

# ১. কুরআনের সূরা ও আয়াত পাওয়ার ফাংশন
def get_quran_verse(surah, ayah):
    url = f"https://api.alquran.cloud/v1/ayah/{surah}:{ayah}/bn.bengali"
    try:
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'OK':
            return data['data']['text']
        return "আয়াত পাওয়া যায়নি।"
    except:
        return "ইন্টারনেট কানেকশন নেই।"

# ২. মূল চ্যাটবট লুপ
print("--- সানি ভাইয়ের ৫৯ মিলিয়ন ভিউ হওয়া স্পেশাল AI ---")
print("আসসালামু আলাইকুম সানি ভাই! আমি আপনার ইসলামিক অ্যাসিস্ট্যান্ট।")

while True:
    print("\n১. কুরআনের আয়াত পড়ুন")
    print("২. বিদায় নিন")
    
    choice = input("আপনার পছন্দ (১/২): ")
    
    if choice == '1':
        s = input("সূরা নম্বর দিন: ")
        a = input("আয়াত নম্বর দিন: ")
        print("\nউত্তর: ", get_quran_verse(s, a))
    elif choice == '2':
        print("আল্লাহ হাফেজ সানি ভাই! আপনার ইউটিউব চ্যানেল যেন আরও বড় হয়।")
        break
