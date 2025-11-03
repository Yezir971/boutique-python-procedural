from app.utils import *
def main():
    nom_boutique: str = "ChossettZ"
    produit: str = "chaussettes"
    prix_unitaire: float = 5.99
    quantite_stock: int = 20
    tva: float = 0.20
    compte_client: int = 100
    compte_boutique: int = 0
    show_message(
    nom_boutique,
    produit,
    prix_unitaire,
    quantite_stock ,
    tva ,
    compte_client,
    compte_boutique)
    
    show_price(prix_unitaire, tva)
    print('Combien de paires de chaussettes voulez vous acheter ?')
    number = input()  
    answer_user = int(number)
    if type(answer_user) == int and answer_user >= 0 and check_stock(quantite_stock , answer_user) :
        recapitulatif(answer_user,tva,quantite_stock, compte_client, prix_unitaire, compte_boutique)
        quantite_stock = new_stock(quantite_stock, answer_user)
        price_unitaire_ht = amount_price_ht(prix_unitaire, answer_user)
        prix_unitaire_ttc = amount_price_ttc(prix_unitaire, tva, answer_user)
        new_price_ttc_to_string = str(prix_unitaire_ttc)
        if quantite_stock < 10 : 
            print('Stock bientôt épuisé !!')
        if quantite_stock < 15 and quantite_stock > 10 and prix_unitaire >5 :
            print('Attention produit presque en ruptures')
        print(f'Prix ttc : {new_price_ttc_to_string} €')
        show_invoice(nom_boutique, produit, answer_user,price_unitaire_ht ,tva, prix_unitaire_ttc )
        show_type(nom_boutique,produit,prix_unitaire,quantite_stock,tva,compte_client ,compte_boutique)

    
if __name__ == "__main__":
    main()