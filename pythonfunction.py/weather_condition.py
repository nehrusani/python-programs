def display_weather(season):
 if season.lower() == "autumm":
  print("Autumm: The leaves turn orange and the weather is cold and breezy ")
 elif season.lower() == "spring":
  print("Spring: Flowers bloom and the waher is warm and pleasent!")
 else:
  print("Invailed season pleas try again!")
season = input("enter spring or autummm : ") 
display_weather(season)