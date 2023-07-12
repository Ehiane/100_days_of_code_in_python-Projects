from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from graphics import SystemGraphics

#globals
ACTIVE = True;
DORMANT = False;
DRINKS = ["espresso","latte","cappuccino"];

Price = 0;



def generate_report(coffeeObject):
    if isinstance(coffeeObject, CoffeeMaker):
        coffeeObject.report();

def find_drinkObject(requested_drink, menu):
    """
    returns the object that matches the drink requested.
    """
    #find the drink that matches the drinkObj name
    return menu[requested_drink];

def run_software():
    
    #Object instantiation:
    coffee_handler = CoffeeMaker();
    finance_handler = MoneyMachine();
    system = SystemGraphics();

    coffee_resources = Menu();
    ## Explanation:
    # returns an obj of menuItem-> of type espresso, the construtor then deals with arranging the data by destructuring the MenuItem obj into its attributes;
    espresso = coffee_resources.find_drink('espresso'); 


    #same thing occures here but for latte.
    latte = coffee_resources.find_drink('latte');
    #same thing occures here but for cappuccino.
    cappuccino = coffee_resources.find_drink('cappuccino');

    the_menu = {
        'espresso': espresso,
        'latte': latte,
        'cappuccino': cappuccino,
    }



    machine_status = ACTIVE;

    #UI stuff
    system.display_welcome_screen();

    while(machine_status):
        system.display_static_logo();
        command = input("\ntype:\n'espresso'\n'latte'\n'cappuccino'\nto make your drink.\n************************\n************************\ntype 'help' for other commands. \n>> ").lower();
        if command == "help":
            
            #UI stuff
            system.display_help_section();

            run_software();
        
        elif command == "report":
           #UI stuff
           system.display_report(coffeeMakerObject=coffee_handler);

           generate_report(coffee_handler);
           pass;
        
        elif command == "off":  
            #UI stuff
            system.display_shutdown();
            machine_status = False; #switching off the system.
            break;
        elif command in DRINKS:
            system.display_initial_report(coffeeMakerObject= coffee_handler);
            
            #find the drink that matches the drinkObj name
            drink = find_drinkObject(command,the_menu)

            #checking if there are enough resources to make the drink.
            if coffee_handler.is_resource_sufficient(drink):
                #prompting user to insert coins
                system.display_payment_section();
                user_cost = finance_handler.process_coins(drink);
                transaction_status = finance_handler.make_payment(user_cost, drink);
                if transaction_status: 
                    #update report in money machine by updating the profit
                    # finance_handler.profit += user_cost; handled in make_payement
                    coffee_handler.make_coffee(drink);
                    system.display_final_report(coffeeMakerObject=coffee_handler);
                else:
                    print("payment was not accepted.");
            else:
                print(f"not enough resources to make {command}");
                system.restart_system();
            


            pass;



run_software();
