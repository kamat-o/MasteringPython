#Fucntion
import time

def generateInvoiceNumber(InvoiceList):
    
    #multiliner code
    prefix = "Inv"
    year = time.strftime("%y")
    current_num = getLastInvoiceNumber(lst)
    return "{}-{}-{}".format(prefix, year, current_num)
    
    # One liner code
    # return "{}-{}-{}".format("Inv",time.strftime("%y"),getLastInvoiceNumber(lst))

def getLastInvoiceNumber(InvoiceList):
    
    invoice_id_list = []

    for i in InvoiceList:
        invoice_id_list.append(int(i.split("-")[2]))

    last_inv_id = max(invoice_id_list)

    return "{:02d}".format(last_inv_id+1)


#Driver Code

lst= ["Inv-19-02","Inv-19-01","Inv-19-10","Inv-19-05"]
print(generateInvoiceNumber(lst))


