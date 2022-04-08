input_month, day = input("輸入月及日為:").split()
star = {"01": ("Capricorn", "Aquarius", 20),
                  "02": ("Aquarius", "Pisces", 18),
                  "03": ("Pisces", "Aries", 20),
                  "04": ("Aries", "Taurus", 20),
                  "05": ("Taurus", "Gemini", 21),
                  "06": ("Gemini", "Canser", 21),
                  "07": ("Canser", "Leo", 22),
                  "08": ("Leo", "Virgo", 23),
                  "09": ("Virgo", "Libra", 23),
                  "10": ("Libra", "Scorpio", 23),
                  "11": ("Scorpio", "Sagittarius", 22),
                  "12": ("Sagittarius", "Capricorn", 21),}
for month in star:
    if input_month == month:
        ans = star[month][0] if int(day) <= star[month][2] else star[month][1]
print("星座為:" + ans)