def main():#working
    try:
       a= int(input("1.Kg,Pound(type 1)\n---------------\n2.Km,mile(type 2)\n---------------\n3.km/h,m/s(type 3)\n---------------\ntype 4 for more\n---------------\nInput:"))
       if a==1: 
        kgPound()
       if a==2:
        kmMile()
       if a==3:
        kmh_ms()
       if a==4:
        extras()
    except ValueError or a > 4:
        print("---------------\nValue is invalid\n---------------\n")
        restart()     
def kgPound():#working
    try:
     ch=int(input("\nKg to pound(Type 1)\n---------------\nPound to Kg(Type 2)\n---------------\nInput:"))
     if ch==1 :
        try:
          ip= float(input("Enter the value:")) 
          print("pounds")
          ip=ip*2.205
          print(str(ip)+" pounds")
        except ValueError:
            print("---------------\nValue is invalid\n---------------\n")
            pass
           
     if ch==2 :
       try: 
          ip= float(input("Enter the value:"))
          ip=ip/2.205
          print(str(ip)+" Kg")
       except ValueError:
            print("---------------\nValue is invalid\n---------------\n")
            pass
    except ValueError or ch > 2:
        print ("Invalid")
        pass    
    restart()        
def kmMile():#working
    try:
     ch=int(input("\nKm to Mile(Type 1)\n---------------\nMile to Km(Type 2)\n---------------\nInput:"))
     if ch==1:
        try:
           ip= float(input("Enter the value:"))
           ip=round(ip/1.609,3)
           print(str(ip)+" Miles")
        except ValueError:
            print("---------------\nValue is invalid\n---------------\n")
            pass           
     if ch==2 :
        try:
           ip= float(input("Enter the value:"))
           ip=round(ip*1.609, 3)
           print(str(ip)+" Km") 
        except ValueError:
            print("---------------\nValue is invalid\n---------------\n")
            pass
    except ValueError or ch > 2:
        print ("Invalid")
        pass       
    restart()    
def kmh_ms():#working
    try:
     ch=int(input("\nKm/h to M/s(Type 1)\n---------------\nM/s to Km/h(Type 2)\n---------------\nInput:"))
     if ch==1:
        try:
           ip= float(input("Enter the value:"))
           ip=round(ip/3.6,3)
           print(str(ip)+" M/s") 
        except ValueError:
           print("---------------\nValue is invalid\n---------------\n")
           pass      
     if ch==2 :
        try:
           ip= float(input("Enter the value:"))
           ip=round(ip*3.6,3)
           print(str(ip)+" Km/h")
        except ValueError:
            print("---------------\nValue is invalid\n---------------\n")
            pass 
    except ValueError or ch > 2:
        print ("Invalid")
        pass      
    restart() 
def extras():
    try:
      o=int(input("Which do you wanna choose:\n---------------\nFarenheit, celsius(type 1)\n---------------\nFoot to meters(type 2)\n---------------\n"))
      if o == 1:
        Frnh_cls()
      if o == 2 :
        Foot_meter()
    except ValueError or o > 2:
        print ("Invalid")
        pass    
      
def Frnh_cls():#working
    try:
      p=int(input("\nFarenheit to celsius(Type 1)\n---------------\nCelsiuis to farenheit(Type 2)\n---------------\nInput:"))
      if p==1:
        try:
           ip= int(input("Enter the value:"))
           ip=5*(ip-32)/9
           print(str(ip)+"*C") 
        except ValueError:
           print("---------------\nValue is invalid\n---------------\n")
           pass      
      if p==2 :
        try:
           ip= float(input("Enter the value:"))
           ip=((9*ip)/5)+32
           print(str(ip)+"*F")
        except ValueError:
            print("---------------\nValue is invalid\n---------------\n")
            pass
    except ValueError or p > 2:
        print ("Invalid")
        pass      
    restart()
def Foot_meter():#working
  try:
    p=int(input("\nFoot to meters(Type 1)\n---------------\nMeters to feet(Type 2)\n---------------\nInput:"))
    if p==1:
     try:
       ip= float(input("Enter the value:"))
       ip/=3.281
       print(str(ip)+" m") 
     except ValueError:
       print("---------------\nValue is invalid\n---------------\n")
       pass      
    if p==2 :
     try:
       ip= float(input("Enter the value:"))
       ip*=3.281
       print(str(ip)+" foot")
     except ValueError:
        print("---------------\nValue is invalid\n---------------\n")
        pass
  except ValueError or p > 2:
        print ("Invalid")
        passt
  restart()   
def restart():#working
    try:
        try:
          r=int(input("Try again? If yes, type 1\n--------------------------\n           If no, type 2\n"))
        except ValueError:
          print("---------------\nValue is invalid\n---------------\n")
          restart()   
        if r==1 :
          main()
        if r==2 :
           print("Terminating program.......\n****Program Succesfully Terminated****")
           quit()
    except ValueError or r > 2:
        print ("Invalid")
        restart()       
            
main()
