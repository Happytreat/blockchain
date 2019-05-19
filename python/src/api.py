from time import time


def checkNotNull(params):
    """
    Check if arguments are non Null
    
    Arguments:
        params {array}
    """
    for value in params:
        if value == None:
            return False
    return True


def create_valid_transaction(sender="a", recipient="b", amount=1, timestamp=time()):
    transaction = {
        "sender": sender,
        "recipient": recipient,
        "amount": amount,
        "timestamp": timestamp,
    }
    return transaction


def create_transaction(transaction):
    print(transaction)
    # self.blockchain.new_transaction(
    #     sender=transaction["sender"],
    #     recipient=transaction["recipient"],
    #     amount=transaction["amount"],
    #     timestamp=transaction["timestamp"],
    # )


trans = create_valid_transaction()
create_transaction(trans["amount"])
