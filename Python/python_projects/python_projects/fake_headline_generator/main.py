import random
subject=("Local goat","Angry Traffic Police","Suspicious momo vendor","Proud plus two topper","Drunk uncle","Anbitious chicken",
         "Village Chairman's nephew","Tiktok Influencers From pokhara","Retired cricket umpire","CHATGPT user from durlung")
actions=("declares himself prime minister of ward no 5","starts protest demanding free Wi-Fi in jungle",
         "discovers Wi-Fi signal at annapurna base camp","replaces street bulbs with fairy light",
         "refuses to stop dancing even after load-shedding ends","challenges rhino to debate about inflation",
         "accidently orders 1000 momos online","blames earthquake drill for real tremor",
         "tries to blame sky for rainfall","tries to recharge bus card with esewa")
place=("in kathmandu traffic jam","At pokhara lakeside","in front of singha durbar","at river","Alcohol","near dharahara top",
       "inside a sajha bus","at a random place","at the jungle")
while True:
    rand_no1= random.randint(0,8)
    rand_no2= random.randint(0,8)
    rand_no3= random.randint(0,8)

    str=subject[rand_no1]
    str=str+" "+actions[rand_no2]
    str=str+" "+place[rand_no3]
    print(str)

    user_request=input("Do You want to continue (Y/N) ").upper()

    if ( user_request=="N" or user_request=="NO"):
        break