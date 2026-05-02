from models import DatabaseManager ,ProductFactory ,Order ,Customer 

def run_pet_store_system ():

    db =DatabaseManager ()


    print ("\n--- Admin: Adding Products (Factory Pattern) ---")
    products_to_add =[
    ("pet","Persian Cat",150 ),
    ("pet","Parrot",800 ),
    ("food","Dog Food",25 ),
    ("accessory","Pet Collar",10 )
    ]

    for p_type ,name ,price in products_to_add :
        product =ProductFactory .create_product (p_type ,name ,price )
        db .add_product (product )


    print ("\n--- User: Viewing Products ---")
    all_items =db .get_all_products ()
    for index ,item in enumerate (all_items ,1 ):
        print (f"{index}. {item.get_info()}")


    print ("\n--- User: Placing Order & Tracking (Observer Pattern) ---")

    customer =Customer ("Ahmed Ali")


    order =Order (order_id =101 )


    order .attach (customer )


    print ("... Order is being processed ...")
    order .set_status ("Shipped")

    print ("... Order is on the way ...")
    order .set_status ("Delivered")

if __name__ =="__main__":
    print ("===============================================")
    print ("  Pet Store Management System - SWA Project    ")
    print ("===============================================")
    run_pet_store_system ()
    print ("\n===============================================")
