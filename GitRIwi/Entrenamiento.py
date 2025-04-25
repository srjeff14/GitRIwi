

Conti = input("¿Desea ingresar a la tienda? s/n\n")
productList = []
valueList = []
discountList = []
discountProduct = []
if (Conti == "s" or Conti == "S"):
    totalValue = 0
    while (Conti == "s" or Conti == "S"):
        conta = 0
        print("Bienvenido a la tienda\n ***Cacharros Riwi***\n")
        
        productValue = 0
        productName = input("Ingrese el nombre del producto:\n")
        def listOfproducts():
            productList.insert(conta, productName)
            return productList
        productList = listOfproducts()
        priceString = input("Ingrese el precio del producto:\n")
        price = float(priceString)
        while (price < 0):
            print("El precio no puede ser menor a 0, por favor ingrese el precio valido")
            priceString = input("Ingrese el precio del producto:\n")
            price = float(priceString)
        def quantifyFuntion ():
            QuantifyString = input("Ingrese la cantidad del producto\n")
            Quantify = float(QuantifyString)
            while (Quantify < 0):
                print("La cantidad no puede ser menor a 0, por favor ingrese la cantidad valida")
                QuantifyString = input("Ingrese la cantidad del producto:\n")
                Quantify = float(QuantifyString)
            return float(Quantify)
        Quantify = quantifyFuntion()
        productValue = price * Quantify
        productValueneto = productValue
        valueList.insert(conta,productValueneto)
        
        opcion = input("¿El producto tiene descuento? s/n\n")
        
        if (opcion == "s" or opcion == "S"):
            discountString = input("Digite el porcentaje:\n")
            discount = float(discountString)
            while (discount < -1):
                print("El descuento no puede ser menor a 0, por favor ingrese el descuento valido")
                discountString = input("Digite el porcentaje:\n")
                discount = float(discountString)
            if (discount > 0 and discount <= 100 ):
                    discount = discount/100
                    discount = productValue * discount
                    productValue = productValue - discount
                    discountList.insert(conta,productValue)
                    discountProduct.insert(conta,productName)   
        
        totalValue += productValue
        print (f"El precio total del producto {productName} es: {productValue}")
        Conti = input("¿Desea ingresar más productos? s/n\n")
    
    print(f"""Los productos fueron:\n {productList}\n
    Los precios sin descuento fueron:\n {valueList}\n
    Los productos con descuento fueron\n {discountProduct}\n
    Los precios con descuento fueron:\n {discountList}\n
    el total de la compra es de: {totalValue}""")
        
    
    
    
    
    
    
    