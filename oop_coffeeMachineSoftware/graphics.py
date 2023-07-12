from UI_interactions import *

company_logo = """
██████╗ ███████╗ █████╗ ███╗   ██╗      ██╗  ██╗ █████╗ ██╗   ██╗███████╗███╗   ██╗
██╔══██╗██╔════╝██╔══██╗████╗  ██║      ██║  ██║██╔══██╗██║   ██║██╔════╝████╗  ██║
██████╔╝█████╗  ███████║██╔██╗ ██║█████╗███████║███████║██║   ██║█████╗  ██╔██╗ ██║
██╔══██╗██╔══╝  ██╔══██║██║╚██╗██║╚════╝██╔══██║██╔══██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║
██████╔╝███████╗██║  ██║██║ ╚████║      ██║  ██║██║  ██║ ╚████╔╝ ███████╗██║ ╚████║
╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝      ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝
                                                                                   
"""

report= """
██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗       
██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╗    
██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   ╚═╝    
██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╗    
██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   ╚═╝    
╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝          
                                                         
"""

payment_section = """
██████╗  █████╗ ██╗   ██╗███╗   ███╗███████╗███╗   ██╗████████╗
██╔══██╗██╔══██╗╚██╗ ██╔╝████╗ ████║██╔════╝████╗  ██║╚══██╔══╝
██████╔╝███████║ ╚████╔╝ ██╔████╔██║█████╗  ██╔██╗ ██║   ██║   
██╔═══╝ ██╔══██║  ╚██╔╝  ██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   
██║     ██║  ██║   ██║   ██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   
╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   
███████╗███████╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗        
██╔════╝██╔════╝██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║        
███████╗█████╗  ██║        ██║   ██║██║   ██║██╔██╗ ██║        
╚════██║██╔══╝  ██║        ██║   ██║██║   ██║██║╚██╗██║        
███████║███████╗╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║        
╚══════╝╚══════╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝        
                                                               
"""

help_art = """
██╗  ██╗███████╗██╗     ██████╗ 
██║  ██║██╔════╝██║     ██╔══██╗
███████║█████╗  ██║     ██████╔╝
██╔══██║██╔══╝  ██║     ██╔═══╝ 
██║  ██║███████╗███████╗██║     
╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     
                                
"""

class SystemGraphics:
    def __init__(self, logo = company_logo, report = report, transaction = payment_section, help_ = help_art):
        self.logo = logo;
        self.report = report;
        self.transaction = transaction;
        self.help_ = help_;

    def display_welcome_screen(self):
        print(self.logo);
        general_pause('start');

    def display_help_section(self):
        printHelp(self.help_);
        general_pause("restart");
        loading_animation("restarting Coffee machine ", 1.5);

    def display_report(self, coffeeMakerObject):
        print(self.report);
        coffeeMakerObject.report();
        print();
        general_pause('continue');

    def display_shutdown(self):
        cts();
        loading_animation('shutting down ', 4)
        print(company_logo);
        loading_animation('',2);
        cts();
        #switching off the system.

    def display_payment_section(self):
        loading_animation('heading to payment section',1);
        general_pause('enter payment section');
        print(self.transaction);

    def display_initial_report(self, coffeeMakerObject):
        cts();
        print(self.report);
        loading_animation('generating initial report',1);
        coffeeMakerObject.report();
        print();
        general_pause('continue');
        #print company logo afterwards
    
    def display_static_logo(self):
        print(self.logo);
    

    def display_final_report(self, coffeeMakerObject):
        print()
        general_pause('generate final report')
        print(self.report);
        loading_animation('generating final report',1);
        coffeeMakerObject.report();
        print();
        general_pause('continue');
        #print company logo afterwards
    
    def restart_system(self):
        cts();
        general_pause('restart')
        loading_animation('restarting software', 3);




        
    