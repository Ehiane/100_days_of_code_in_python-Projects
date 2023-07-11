#-----------------Coffeee Machine Software-------------------------#

##-----[Program Requirements]-------#
#1. print report
#2. check resources if they are sufficient.
#3. process coins.
#4. check transaction successful
#5. make coffee.

#globals
ACTIVE = True;
DORMANT = False;
DRINKS = ["espresso","latte","cappuccino"];
#Imports
from prog_functions import *
from art import *

def run_coffee_software():
    machine_status = ACTIVE;
    price = read_company_profit();

    #UI stuff
    print(company_logo);
    general_pause('start');

    while(machine_status):
        print(company_logo);
        command = input("\ntype:\n'espresso'\n'latte'\n'cappuccino'\nto make your drink.\n************************\n************************\ntype 'help' for other commands. \n>> ").lower();
        if command == "help":
            
            #UI stuff
            print(help_art);
            printHelp();
            general_pause("restart");
            loading_animation("restarting Coffee machine ", 1.5);
            
            run_coffee_software();
        
        elif command == "report":
            loading_animation('generating report', 1);
            generate_report(price);
            print()
            general_pause('continue');
        
        elif command == "off":
            
            #UI stuff
            cts();
            loading_animation('shutting down ', 4)
            print(company_logo);
            loading_animation('',2);
            cts();
            machine_status = False; #switching off the system.
            break;
        elif command in DRINKS:
            
            #UI stuff
            cts();
            loading_animation('generating initial report', 1);
            generate_report(price);
            general_pause('continue');
            print(company_logo);


            price = buy_drink(command); #if price == -1, smth went wrong
            if price >= 0:

                #UI stuff;
                loading_animation('heading to payment section', 1)
                general_pause('enter payment section');

                valid_payment = process_payment(price);
                if(valid_payment):
                    price = read_company_profit();
                    print(price)
                    print();

                    general_pause('generate final report')
                    loading_animation('generating final report', 1.5);
                    generate_report(price);
                    general_pause('continue ')
            else:
                print("smth went wrong with the payment.")
        else:
            print("command not recognized!");
            run_coffee_software();
    pass;


run_coffee_software();