

# ----------------------------------------module price------------------------------------------   
def price_ht(price_ttc: float, tva: float) -> float:
    """Return the ht price with ttc price and tva

    Args:
        price_ttc (float): Price ttc of product
        tva (float): tva in % 0=<tva=<1

    Returns:
        float: ttc price
    """
    return round(price_ttc / (1 + tva), 2)
    

def price_ttc(price_ht: float, tva: float ) -> float:
    """Return the ttc price with ht price and tva

    Args:
        price_ht (float): Price ht of product
        tva (float): tva in % 0=<tva=<1

    Returns:
        float: ttc price
    """
    return round(price_ht * (1 + tva), 2)

def amount_price_ht(price:float, answer_user: int) -> float:
    """Calculate the ht price whith the quantity enter by user

    Args:
        price (float): Price of product
        answer_user (int): Quantity enter by user

    Returns:
        float: the ht amount price 
    """
    return round(price*answer_user, 2)

def amount_price_ttc(price:float,tva: float, answer_user: int) -> float:
    """Calculate the ttc price whith the quantity enter by user

    Args:
        price (float): price of product
        tva (float): tva of product
        answer_user (int): Quantity enter by user

    Returns:
        float: the ttc amount price
    """
    return round(price_ttc(price,tva)*answer_user, 2)

def new_stock(stock: int, answer_user: int) -> int:
    """returns the total stock after a transaction

    Args:
        stock (int): total stock
        answer_user (int): Quantity enter by user

    Returns:
        int: total stock after a transaction
    """
    return stock - answer_user

def new_compte_client(compte_client:int , price: int, answer_user: int) -> int:
    """Calculates the customer's new balance

    Args:
        compte_client (int): customer account balance
        price (int): price of product
        answer_user (int): Quantity enter by user

    Returns:
        int: customer's new balance
    """
    return compte_client - price*answer_user

def new_compte_shop(compte_boutique: int, price : int, answer_user: int) -> int:
    """Calculate the shop new balance

    Args:
        compte_boutique (int): shop account balance
        price (int): price of product
        answer_user (int): Quantity enter by user

    Returns:
        int: The shop new balance
    """
    return compte_boutique + price*answer_user        
# ----------------------------------------module price------------------------------------------   
    

# --------------------------module stock------------------------------
def check_stock(stock: int , comand: int) -> bool:
    """Check if the customer  can command a product

    Args:
        stock (int): stock quantity
        comand (int): Quantity enter by user

    Returns:
        bool: return true if the custommer can command the product, false if the custommer can't
    """
    if (comand > stock):
        return False
    return True
# --------------------------module stock------------------------------
 
 

# --------------------------module display------------------------------
def show_message(
    nom_boutique: str,
    produit: str,
    prix_unitaire: float,
    quantite_stock: int ,
    tva: float ,
    compte_client: int ,
    compte_boutique: int
    ) -> str: 
    print(f"Le nom de la boutique est {nom_boutique} cette boutique vend des {produit} au prix de {prix_unitaire} €, attention il ne reste plus que {quantite_stock} exemplaires de chaussettes en stock.\nTVA du produit : {tva}\nNombre de compte client : {compte_client}\ncompte boutique : {compte_boutique}")



def recapitulatif(answer_user: int, tva: float, stock: int, compte_client: float, price: float, compte_boutique:int) -> str:
    print(f'Le montant HT de l’achat : {amount_price_ht(price, answer_user)} €\nLe montant TTC de l’achat : {amount_price_ttc(price, tva, answer_user)} €\nLe stock restant après la vente : {new_stock(stock, answer_user)}\nCompte client : {new_compte_client(compte_client , price, answer_user)} €\nCompte de la boutique : {new_compte_shop(compte_boutique, price, answer_user)} €')
    
def show_price(price: float, tva: float) -> str:
    """Return in string the price calculate with tva

    Args:
        price (float): price of product
        tva (float): TVA

    Returns:
        str: price calculate
    """
    print(f"Prix Hors Taxe : {price_ht(price, tva)}\nPrix Toute taxes {price_ttc(price, tva)}")
    
def show_invoice(name: str, product: str, quantity: int, price_ht: float, tva: float, price_ttc) -> str:
    print(f"{'':->100}\n")
    print(f"{name}\n")
    print(f"{'':->100}\n")
    print(f"{'Produit': <80}{'qté': >10}{'ht': >10}")
    print(f"{product:.<80}{quantity: >10}{price_ht:>10}\n")
    print(f"{'Total HT :': >90}{price_ht: >10}")
    print(f"{'TVA :':->90}{tva*100:> 10}")
    print(f"{'Total TTC :':->90}{price_ttc:> 10}")
    print(f"{'':->100}")

def show_type(
    nom_boutique: str,
    produit: str,
    prix_unitaire: float,
    quantite_stock: int ,
    tva: float ,
    compte_client: int ,
    compte_boutique: int
):
    print(f'Type de nom_boutique : {type(nom_boutique)}\n')
    print(f'Type de produit : {type(produit)}\n')
    print(f'Type de prix_unitaire : {type(prix_unitaire)}\n')
    print(f'Type de quantite_stock : {type(quantite_stock)}\n')
    print(f'Type de tva : {type(tva)}\n')
    print(f'Type de compte_client : {type(compte_client)}\n')
    print(f'Type de compte_boutique : {type(compte_boutique)}\n')

# --------------------------module display------------------------------
