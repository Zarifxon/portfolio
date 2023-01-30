# c="""Aviachiptalarga buyurtmalar haqida joriy ma'lumotlarni taqdim etuvchi dastur"""
# print(c,)
# manzil = input("Borish manzilini kiriting:\n>>>")
# reys = 298
# print(f"Borish manzili:{manzil}\nParvoz raqami:{reys}")
# ism_sharif= input("Ismi sharifingizni kiriting:\n>>>")
# print(f"Borish manzili:{manzil}\nParvoz raqami:{reys}\nIsmi sharifingiz:{ism_sharif}")
# sana = input("Parvoz qilish sanasini kiriting:\n>>>")
# print(f"Sizning biletingiz!!!\nBorish manzili:{manzil}\nParvoz raqami:{reys}\nIsmi sharifingiz:{ism_sharif}\nUchish sanasi:{sana}")
# result=input("Ma'lumotlar to'g'ri bo'lsa 'y'ni yoki 'n'ni bosing\n>>>")
# if (result=="y"):
#   print(f"Sizning biletingiz!!!\n Borish manzili:{manzil}\n Parvoz raqami:{reys}\n Ismi sharifingiz:{ism_sharif}\n Uchish sanasi:{sana}")
# else:
#   print("Dasturni qayta ishga tushiring!")


from binarytre import build
poyiz =[]
poyiz.append(input("Manzil: "))
poyiz.append((input("Parvoz raqami: ")))
poyiz.append(input("Yo'lovchi ismi sharfi': "))  
poyiz.append((input("Parvoz qilish sanasi: ")))
binar_daraxt = build(poyiz)
print("Ro'yxatdagi ikkilik daraxt :\n", binar_daraxt)
print("\nIkkilik daraxtdan ro'yxat :", binar_daraxt.values)