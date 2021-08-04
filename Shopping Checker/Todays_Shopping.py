class Shop():
    def Calculate():
        SumProducts=int(input("Enter total products:"))
        dictionary={}
        temp=0
        for i in range(SumProducts):
            Name=input("Enter Product name:")
            dictionary[Name]=float(input("Enter price of the product: Rs."))
        print("Data is Stored!!!")
        req=input("#Enter Yes or No to view the dictionary:")
        if req=="Yes":
            print("The Dictionary of the products:",dictionary)
        else:
            print("No problem Sir/Madam")
        for value in dictionary.values():
            temp=temp+value
        print("Today's total shopping was for: Rs.",temp)
        req1=input("Enter Y or N to check product cost(Any product):")
        if req1=="Y":
            x=input("Enter product name:")
            if dictionary[x]==dictionary[x]:
                print("The",x,"is purchased for: Rs.",dictionary[x])
            else:
                print("Sorry!! Invalid Product name.Please enter product name stored only")
        else:
            print("No problem Sir/Madam")
        print("Thank you for using till the end!!!")

Shop.Calculate()
