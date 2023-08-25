class dic_up:
    def dic_change(self):
        import json

        # Take user input for the dictionary string
        dict_str = input('Enter a dictionary string like {"Age":25} string must be in doble qute')

        try:
            # Convert the string to a dictionary
            dictionary = json.loads(dict_str)
            print("Converted Dictionary:", dictionary)
        except json.JSONDecodeError:
            print("Invalid dictionary string format.")

        for i,j in dictionary.items():
            dictionary[i].update({"perfection":"Eng"})

        print(dictionary)
          

        

    def prime(self):
          inp=int(input("enter value above 2 "))
          if inp>2:
               for i in range (3,inp):
                    if inp%i==0:
                         print("is no prime ")
                         break
               else:     
                    print("prime")
          else:
               print("not prime")



    def change_list_di(self):
        
            import json

            # Take user input for the list of dictionaries
            list_str = input("Enter a list, string value of list must be in duble qute  dictionaries must add at 4 index & change only (name) key")

            try:
            # Convert the input string to a list
                list_of_dicts = json.loads(list_str)
    
                # Ensure the converted data is a list
                if isinstance(list_of_dicts, list):
                    print("Input List of Dictionaries:", list_of_dicts)
                else:
                    print("Input is not a valid list of dictionaries.")
            except json.JSONDecodeError:
                print("Invalid JSON format.")

            list_of_dicts[4]["name"]="mom"

            print(list_of_dicts)
    


    def find_prime_in_range(self):
        x=int(input("Enter start point above 2"))
        y=int(input("Enter end point"))
              
        for i in range(x,y):
            for j in range (2,i):
               if i%j==0:
                    break
            else:
                print(i,end=" ")

    def pas_con(self):
    
        for i in range(1,10):
          if i==3:
               pass
          if i==5:
               continue
          if i==8:
               break
          
          print("Hellow",i)
    


    def split_val(self):
        va=input("enter string")
        for i in va:
            print(i)



    def coman_in_list(self):
        x=eval(input("Enter list"))
        y=eval(input("Enter list"))

        for i in range(len(x)):
            if x[i]==y[i]:
                print(x[i],end=",")


    
    def change_in_dic(self):
        x=eval(input("Enter dic"))

        for k,v in (x.items()):

            if x[k]==5:
                x[k]="change value" 
        print(x)
 



    def con_to_dic(self):
        dic={}
        a=eval(input("Enter list of same lenght"))
        b=eval(input("Enter list of same lenght"))
        for i in range(len(a)):
          dic[a[i]]=b[i]
        print(dic)

    def oder_list(self):

        li=eval(input("input list"))
        w=[]
        z=[]
        c=[]
        for i in li:
            if isinstance(i, int):
                w.append(i)
            elif isinstance(i, str):
                c.append(i)
            else:
                z.append(i)

        l=len(w)
        for i in range(0,l):
            
            for j in range(0,l-i-1):
                
                if w[j]>w[j+1]:
                    w[j],w[j+1]=w[j+1],w[j]
                

        l1=len(c)
        for i in range(0,l1):
            
            for j in range(0,l1-i-1):
                
                if c[j]>c[j+1]:
                    c[j],c[j+1]=c[j+1],c[j]
                
        l2=len(z)
        for i in range(0,l2):
            
            for j in range(0,l2-i-1):
                
                if z[j]>z[j+1]:
                    z[j],z[j+1]=z[j+1],z[j]
        

        listss=c+z+w
        print(listss)
    


    
    def cards_sort(self):

        li=eval(input("input list"))
        w=[]
        z=[]
        c=[]
        for i in li:
            if isinstance(i, int):
                w.append(i)
            elif isinstance(i, str):
                c.append(i)
            else:
                z.append(i)

        l=len(w)
        for i in range(0,l):
            
            for j in range(0,l-i-1):
                
                if w[j]<w[j+1]:
                    w[j],w[j+1]=w[j+1],w[j]
                

        q=['a','k','q','j']
        ln=[]


        for i in q:
            for j in c:
                if i==j[0]:
                    ln.append(j)
                else:
                    continue
        

        listss=ln+w
        print(listss)

