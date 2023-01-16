import json
import os
import mercadopago

def lambda_handler(event, context):
    sdk = mercadopago.SDK(os.environ["ACCESS_TOKEN"])
    
    bodyGet=json.loads(event["body"])
    
    
    payment_data = {
            "transaction_amount": float(bodyGet["transaction_amount"]),
            "token": bodyGet["token"],
            "installments": int(bodyGet["installments"]),
            "payment_method_id": bodyGet["payment_method_id"],
            "payer": {
                "email": bodyGet["payer"]["email"],
                "identification": {
                    "type": bodyGet["payer"]["identification"]["type"],
                    "number": bodyGet["payer"]["identification"]["number"],
                },
            },
        }

    payment_response = sdk.payment().create(payment_data)
    payment = payment_response["response"]
    status = {"status":payment["status"], "status_detail":payment["status_detail"], "id":payment["id"]}

    return {
            "statusCode": 201,
            "body": json.dumps(status),
        
