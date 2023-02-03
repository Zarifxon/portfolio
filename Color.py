import colorama
from colorama import Fore

name= input(Fore.GREEN+"Rang nomini kiriting:\n>>>")


#Red	#FF0000	rgb(255, 0, 0)
if(name=="red" or name=="FF0000"):
  print(Fore.RED + "Color: Red \nrgb(255, 0, 0) \ncode: FF0000 ")

#Black	#000000	rgb(0, 0, 0)
elif(name=="black" or name=="00000"):
  print(Fore.BLACK + "Color: Black \nrgb(0, 0, 0) \ncode: 00000 ")

# Green	#008000	rgb(0, 128, 0)
elif(name=="green" or name=="008000"):
  print(Fore.GREEN + "Color: Green \nrgb(0, 128, 0) \ncode: 008000 ")

# Yellow	#FFFF00	rgb(255, 255, 0)
elif(name=="yellow" or name=="FFFF00"):
  print(Fore.YELLOW + "Color: Yellow \nrgb(255, 255, 0) \ncode: FFFF00 ")

# Blue	#0000FF	rgb(0, 0, 255)
elif(name=="blue" or name=="0000FF"):
  print(Fore.BLUE+ "Color: Blue \nrgb(0, 0, 255) \ncode: 0000FF ")

#Magenta #FF00FF   rgb(255, 0, 255)
elif(name=="magenta" or name=="FF00FF"):
  print(Fore.MAGENTA+ "Color: MAGENTA \nrgb(255, 0, 255) \ncode: FF00FF")

#Cyan #00FFFF	rgb(0, 255, 255)
elif(name=="cyan" or name=="00FFFF"):
  print(Fore.CYAN+ "Color: CYAN \nrgb(0, 255, 255) \ncode: 00FFFF")

# white #FFFFFF rgb(255, 255, 255)
elif(name=="white" or name=="FFFFFF"):
  print(Fore.WHITE+ "Color: White \nrgb(255, 255, 255) \ncode: FFFFFF")

else:
  print("Kechirasiz bunaqa rang bizda yo'q")



