from flask import Flask, render_template, request, jsonify, redirect, url_for, json, jsonify


app = Flask(__name__)

@app.route('/')
def intro():
    return render_template('intro.html')

@app.route('/show_availability', methods=['GET'])
def show_availability():
    #API Availability (Time Slots) V2 - Mock Response
    slots = [
        {
            "id": "12345",
            "from": "2023-08-21T14:00:00.000Z",
            "to": "2023-08-21T15:00:00.000Z",
            "store": {
                "id": "store_001",
                "name": "TongoMart - Magento"
            },
            "description": "Delivery Slot between 2PM to 3PM",
            "operational_model": "PICK_AND_DELIVERY",
            "expires_at": "2023-08-21T13:59:59.000Z"
        },
        {
            "id": "12346",
            "from": "2023-08-21T15:00:00.000Z",
            "to": "2023-08-21T16:00:00.000Z",
            "store": {
                "id": "store_001",
                "name": "TongoMart - Magento"
            },
            "description": "Delivery Slot between 3PM to 4PM",
            "operational_model": "PICK_AND_DELIVERY",
            "expires_at": "2023-08-21T14:59:59.000Z"
        },
         {
            "id": "12347",
            "from": "2023-08-21T16:00:00.000Z",
            "to": "2023-08-21T17:00:00.000Z",
            "store": {
                "id": "store_001",
                "name": "TongoMart - Magento"
            },
            "description": "Delivery Slot between 4PM to 5PM",
            "operational_model": "PICK_AND_DELIVERY",
            "expires_at": "2023-08-21T15:59:59.000Z"
        }
    ]
    
    return render_template('availability.html', slots=slots)

@app.route('/create_job', methods=['POST'])
def create_job(slot_id):
    # API Create a Job - Mock Response
    response = {
        "message": "Job created successfully!",
        "job_id": "mock_job_001" + slot_id
    }
    
    return jsonify(response)

@app.route('/get_job_by_id/<job_id>', methods=['GET'])
def get_job_by_id(job_id):
    # API Get job by id - Mock Response
    response = {
        "job_number": job_id,
         # ... (other informations)
        "origin": {
            "name": "TongoMart - Magento",
            "country": "Uganda",
             # ... (other informations)
        },
         # ... (other informations)
        "items": [{
            "id": "item001",
            "state": "new",
             # ... (other informations)
        }],
         # ... (other informations)
    }
    return jsonify(response)

@app.route('/create_order', methods=['POST'])
def create_order():
    selected_slot_id = request.form.get('slot_id')
    
    slot_details = get_slot_details(selected_slot_id) 

    response = create_job(selected_slot_id).get_json()

    if response.get("message") == "Job created successfully!":
        job_id = response.get("job_id")
        return render_template('order_details.html', 
                               job_id=job_id, 
                               slot_description=slot_details['description'],
                               store_name=slot_details['store']['name'])
    else:
        return redirect(url_for('show_availability', error="There was an error creating the job. Please try again."))

def get_slot_details(slot_id):
    if slot_id == '12345':
        return {
            "description": "Delivery Slot between 2PM to 3PM",
            "store": {
                "name": "TongoMart - Magento"
            }
        }
    elif slot_id == '12346':
        return {
            "description": "Delivery Slot between 3PM to 4PM",
            "store": {
                "name": "TongoMart - Magento"
            }
        }
    elif slot_id == '12347':
        return {
            "description": "Delivery Slot between 4PM to 5PM",
            "store": {
                "name": "TongoMart - Magento"
            }
        }
        
@app.route('/process_invoicing', methods=['POST'])
def process_invoicing():
    amount = request.json['amount']
    
    response = mock_payment_info(amount)
    
    #API Payment info - Mock Response
    response = {
        "currencyCode": "USD",
        "prices": {
            "subtotal": float(amount),
            "shippingFee": 0,
            "discounts": 0,
            "taxes": 0,
            "order_value": float(amount),
            "attributes": []
        },
        "payment": {
            "id": "sample_id",
            "payment_status": "SUCCESS",
            "method": "CASH",
            "reference": "sample_ref",
            "value": float(amount),
            "payment_status_details": "Payment processed",
            "method_details": "CASH",
            "blocking_policy": "UNBLOCKED",
            "metadata": {}
        },
        "invoice": {
            "reference": "sample_invoice_ref",
            "attachments": []
        }
    }

    return jsonify(response)

def mock_payment_info(amount):
    # API Payment info - Mock Response
    return {
        "currencyCode": "USD",
        "prices": {
            "subtotal": float(amount) - 10,  # fictitious values
            "shippingFee": 5,
            "discounts": 2,
            "taxes": 3,
            "order_value": float(amount),
            "attributes": []
        },
        "payment": {
            "id": "payment_12345",
            "payment_status": "SUCCESS",
            "method": "CASH",
            "reference": "ref_12345",
            "value": float(amount),
            "payment_status_details": "Payment successful",
            "method_details": "Cash on delivery",
            "blocking_policy": "CHECKOUT",
            "metadata": {}
        },
        "invoice": {
            "reference": "invoice_12345",
            "attachments": []
        }
    }

@app.route('/invoice_info')
def invoice_details():
    job_id = request.args.get('job_id') 
    details = request.args.get('details')  

    if details:
        details_dict = json.loads(details)
    else:
        details_dict = {}  

    return render_template('invoice_info.html', job_id=job_id, details=details_dict)


if __name__ == "__main__":
    app.run(debug=True)
