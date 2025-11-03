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


# ----------------------------------------module price------------------------------------------   
def price_ht(price_ttc: float, tva: float) -> float:
    return round(price_ttc / (1 + tva), 2)
    
def show_price(price: float, tva: float) -> str:
    print(f"Prix Hors Taxe : {price_ht(price, tva)}\nPrix Toute taxes {price_ttc(price, tva)}")
# ----------------------------------------module price------------------------------------------   
    

# --------------------------module stock------------------------------
def check_stock(stock: int , comand: int) -> bool:
    if (comand > stock):
        return False
    return True
# --------------------------module stock------------------------------
 
 
# ---------------------------module price-----------------------------
def price_ttc(price_ht: float, tva: float ) -> float:
    return round(price_ht * (1 + tva), 2)

def amount_price_ht(price:float, answer_user: int) -> float:
    return round(price*answer_user, 2)

def amount_price_ttc(price:float,tva: float, answer_user: int) -> float:
    return round(price_ttc(price,tva)*answer_user, 2)

def new_stock(stock: int, answer_user: int) -> int:
    return stock - answer_user

def new_compte_client(compte_client:int , price: int, answer_user: int) -> int:
    return compte_client - price*answer_user

def new_compte_shop(compte_boutique: int, price : int, answer_user: int) -> int:
    return compte_boutique + price*answer_user        
# ---------------------------module price---------------------------

def recapitulatif(answer_user: int, tva: float, stock: int, compte_client: float, price: float, compte_boutique:int) -> str:
    print(f'Le montant HT de l’achat : {amount_price_ht(price, answer_user)} €\nLe montant TTC de l’achat : {amount_price_ttc(price, tva, answer_user)} €\nLe stock restant après la vente : {new_stock(stock, answer_user)}\nCompte client : {new_compte_client(compte_client , price, answer_user)} €\nCompte de la boutique : {new_compte_shop(compte_boutique, price, answer_user)} €')
    
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


