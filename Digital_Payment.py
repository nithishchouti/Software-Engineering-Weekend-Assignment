class PaymentSystem:
    def __init__(self):
        self.transactions = []
        
    def process_transaction(self, amount, payment_method, transaction_time):
        transaction = {"amount": amount, "payment_method": payment_method, "transaction_time": transaction_time}
        self.transactions.append(transaction)
        return "Transaction successful"
    
    def get_transactions(self):
        return self.transactions