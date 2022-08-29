import numpy as np
print('Hi I\'m your Heat transfer evaluator. I am going to help with your Rate of Heat Transfer calculations.\nKindly provide the following parameters. All parameters must be in standard units.')
print('\nFor standard forms of input, multiplication is denoted \"*\", exponents are denoted with \"**\". Eg. 5.6 x 10^-1 = 5.6 * 10**-1')
Type_heat_trans = input('Which Type of Heat transfer are we working on. \'1\' - Conduction, \'2\' - Convection, \'3\' - Radiation: ')

while not Type_heat_trans in ['1','2','3']:
    print("\nWrong input ")
    Type_heat_trans = input('\nWhich Type of Heat transfer are we working on. \'1\' - Conduction, \'2\' - Convection, \'3\' - Radiation: ')

if Type_heat_trans == '1':
    Type_conduction = input('\nChoose the type of conduction. \'1\' - Single layer, \'2\' - Conduction Series: or \'3\' - Conduction in cylindrical tube: ')
    while not Type_conduction in ['1','2','3']:
        print("\nWrong input ")
        Type_conduction = input('\nChoose the type of conduction. \'1\' - Single layer, \'2\' - Conduction Series: or \'3\' - Conduction in cylindrical tube: ')
    if Type_conduction == '1':
     par = input('\nWhat are we looking for. Input \'Q\' - Rate of heat transfer, \'A\' - Area, \'K\' - Thermal conductivity, \'dt\' - Temp diff or \'X\' - Thickness: ').capitalize()   
     while not par in ['Q','A','K','dt','X']:
         print('Wrong Input')
         par = input('\nWhat are we looking for. Input \'Q\' - Rate of heat transfer, \'A\' - Area, \'K\' - Thermal conductivity, \'dt\' - Temp diff or \'X\' - Thickness: ').capitalize()
     if par == 'A':
          a = float(input('Rate of heat Transfer(q): '))
          b = float(input('Thermal conductivity: '))
          c = float(input('Temp diff: '))
          d = float(input('Thickness: '))
          A =(a*d)/(b*c)
          print(str(A)+'m^2')
     elif par == 'K':
          a = float(input('Rate of heat Transfer(q): '))
          b = float(input('Area: '))
          c = float(input('Temp diff: '))
          d = float(input('Thickness: '))
          A =(a*d)/(b*c)
          print(str(A)+'J/ms0C')
     elif par == 'dt':
          a = float(input('Rate of heat Transfer(q): '))
          b = float(input('Thermal conductivity: '))
          c = float(input('Area: '))
          d = float(input('Thickness: '))
          A =(a*d)/(b*c)
          print(str(A)+'0C')
     elif par == 'X':
          a = float(input('Rate of heat Transfer(q): '))
          b = float(input('Thermal conductivity: '))
          c = float(input('Temp diff: '))
          d = float(input('Area: '))
          A =(b*d*c)/(a)
          print(str(A)+'m')
     elif par == 'Q':                    
      def single_layer_con(k,A,dt,x):
       qc = (k*A*dt)/x
       return str(qc)+'J/s'
      print(single_layer_con(float(input('\nThermal conductivity(W/m0C): ')),
      float(input('Area(m): ')),float(input("Temperature difference(0C):")),
      float(input('Thickness(m): '))))
    elif Type_conduction == '2': # For conduction Series
     
     def series(u,A,dt):
      qc = u*A*dt
      return str(qc)+'J/s'  
     
     no_of_layers = int(input('Number of layers: '))
     l = 0
     for i in range(1,no_of_layers+1):
      a = float(input('Thickness(X'+str(i)+'): '))
      b = float(input("Thermal conductivity(K"+str(i)+'): '))
      c = a/b
      l+=c
     Area = float(input('Area(m^2):'))
     temp = float(input("Temperature difference(0C): "))
     print(series(1/l,Area,temp))
    elif Type_conduction == '3':
          a = float(input('Length of pipe: '))
          b = float(input('Thermal conductivity: '))
          c = float(input('Temp diff: '))
          d = float(input('Radius 1: '))
          e = float(input('Radius 2: '))
          A =(2*3.142*a*b*c)/(np.log(e/d))
          print(str(A)+'J/s')
    "Convection"
elif Type_heat_trans == '2':
    par = input('\nWhat are we looking for. Input \'Q\' - Rate of heat transfer, \'dt\' - Temperature diff, \'A\' - Area or \'H\' - Coefficient of Convective HT: ').upper()   
    while not par in ['Q','dt','A','H']:
       print('\nWrong input')
       par = input('\nWhat are we looking for. Input \'Q\' - Rate of heat transfer, \'dt\' - Temperature diff, \'A\' - Area or \'H\' - Coefficient of Convective HT: ').upper() 
    if par == 'Q':
     def convection(h,A,dt): 
       q = h*A*dt
       return q
     a = float(input('Coefficient(h): '))
     b = float(input('Area(m^2): '))
     c = float(input('Temperature difference(dt): '))
     print(convection(a,b,c))
    elif par == 'A':
     a = float(input('Coefficient(h): '))
     b = float(input('Rate of heat transfer: '))
     c = float(input('Temperature difference(dt): '))
     A = b/(a*c)
     print(str(A)+'m^2')
    elif par == 'H':
     a = float(input('Area: '))
     b = float(input('Rate of heat transfer: '))
     c = float(input('Temperature difference(dt): '))
     A = b/(a*c)
     print(str(A)+'J/m^20C')
    elif par == 'dt':
     a = float(input('Coefficient(h): '))
     b = float(input('Rate of heat transfer: '))
     c = float(input('Area: '))
     A = b/(a*c)
     print(str(A)+'0C')

     "Radiation" 
elif Type_heat_trans == '3':
    par = input('\nWhat are we looking for. Input \'Q\' - Rate of heat transfer, \'A\' - Area, \'dt\' - Temperature diff or \'E\' - Emissivity: ').upper()   
    while not par in ['Q','A','dt','E']:
        print('\nWrong input')
        par = input('\nWhat are we looking for. Input \'Q\' - Rate of heat transfer, \'A\' - Area, \'dt\' - Temperature diff or \'E\' - Emissivity: ').upper()   
    if par == 'Q': 
     
     def radiation(A,e,z,dt):
        q = A*e*z*dt
        return str(round(q,2))+ 'J/s'
     a = float(input('Area(m^2): '))
     b = float(input('Emissivity: '))
     c = float(5.67 * 10**-8)
     d = float(input('T1(Absolute temp): '))
     e = float(input('T2(Absolute temp): '))
     f = (d**4) - (e**4)
     print(radiation(a,b,c,f))
    elif par == "A":
        a = float(input('Rate of Heat Transfer: '))
        b = float(input('Emissivity: '))
        c = float(5.67 * 10**-8)
        d = float(input('T1(Absolute temp): '))
        e = float(input('T2(Absolute temp): '))
        f = (d**4) - (e**4)
        A = a/(b*c*f)
        print(str(A)+'m^2')
    elif par == 'E':
        a = float(input('Rate of Heat Transfer: '))
        b = float(input('Area: '))
        c = float(5.67 * 10**-8)
        d = float(input('T1(Absolute temp): '))
        e = float(input('T2(Absolute temp): '))
        f = (d**4) - (e**4)
        A = a/(b*c*f)  
        print(str(A))  
    elif par == 'dt':
        a = float(input('Rate of Heat Transfer: '))
        b = float(input('Area: '))
        c = float(5.67 * 10**-8)
        d = float(input('Area: '))
        A = a/(b*c*d)  
        print(str(A)+'0C')    
     

#Conduction in parallel
# elif Type_conduction == '3':
#     def parallel(k,A,dt,x):
#       qc = ()
