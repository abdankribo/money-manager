def balance(transactions):
    return sum((t['amount'] if t['type']=='income' else -t['amount']) for t in transactions)

def category_totals(transactions):
    out={}
    for t in transactions:
        if t['type']=='expense': out[t['category']]=out.get(t['category'],0)+t['amount']
    return out
