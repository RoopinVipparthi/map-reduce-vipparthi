# Case 2 - Mapper using standard input and output
# Easy to test locally in the terminal

import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split("	")
  if (len(datalist) == 19) : 
    RowID,OrderID,OrderDate,ShipDate,ShipMode,CustomerID,CustomerName,SalesAgentID,CountryRegion,City,State,PostalCode,Region,ProductID,Category,SubCategory,ProductName,Sales,Quantity = datalist

    # print intermediate key-value pairs to standard output
    print(City,"\t",1)