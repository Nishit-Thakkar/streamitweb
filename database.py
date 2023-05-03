from deta import Deta

DETA_KEY = "d0b59mwflze_AN5uVSELkcHXH5vSF1B7LXMpDnZuWBji"

deta = Deta(DETA_KEY)

db=deta.Base("Leukemia_Stage_Data")

def insert_result(docname,doc_contact,doc_quli,hospital_name,hospital_address,id,name,age,date,address,pat_contact,aadhar,remark,pred):
    db.put({
        "docname":docname,
        "doc_contact":doc_contact,
        "doc_quli":doc_quli,
        "hospital_name":hospital_name,
        "hospital_address":hospital_address,
        "id":id,
        "name":name,
        "age":age,
        "date":str(date),
        "address":address,
        "pat_contact":pat_contact,
        "aadhar":aadhar,
        "remark":remark,
        "pred":pred,
    })
