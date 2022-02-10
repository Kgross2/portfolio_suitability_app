# import required libraries



import questionary
import fire
from questionary.constants import Style, NO, YES, YES_OR_NO
import sqlalchemy
   
# Define the clients general information
custom_style=Style([
('answer', 'fg:#32cd32'),
('highlighted', 'fg:#32cd32 underline'),
('pointer', 'fg:#32cd32'),
('instruction', 'fg:#808080')
])

def survey_questions():
    full_name = (questionary.text(
        "What's your name?",
        validate=lambda text: True if len(text) > 0 else "Please enter a valid name",
        style=custom_style
        ).ask())
    
    phone_number = (questionary.text(
        "What's your phone number?",
        instruction = '(No dashes only numbers)',   
        validate=lambda text: True if len(text) == 10 else "Please enter a valid 10-digit phone number",
        style=custom_style  
        ).ask())
            # I'd like the message to only display after the user presses enter, not while they are repsonding.
    
    email_address = (questionary.text(
        "What's your email address?",
        validate=lambda text: True if len(text) > 0 else "Please enter a valid email address",
        style=custom_style
        ).ask())
    



    annual_income = (questionary.text(
        "What's your annual income?",
        validate=lambda text: True if int(text) > 0 else "Please enter a positive value",
        style=custom_style
        ).ask())
            # I want to require numeric values entered
        
    investing_experience = questionary.text(
        "How many years of investing experience do you have?",
        validate=lambda text: True if int(text) > 0 and int(text) < 100 else "Please enter a valid value",
        style=custom_style
        ).ask()
    
    investment_amount = (questionary.text(
        "What is the amount you wish to start investing?",
        validate=lambda text: True if int(text) > 0 else "Please enter a positive value",
        style=custom_style
        ).ask())
    
    annual_expenses = (questionary.text(
        "What are your annual expenses?",
        validate=lambda text: True if int(text) > 0 else "Please enter a positive value",
        style=custom_style
        ).ask())
    
    income_stability = questionary.text(
        f"Is your source of income stable?",
        instruction = '(YES or NO)',
        style=custom_style
        ).ask(YES_OR_NO)
    
    
    annual_income = float(annual_income)
    investing_experience = int(investing_experience)
    investment_amount = float(investment_amount)
    annual_expenses = float(annual_expenses)
    income_stability = str(income_stability)
    



    risk_level = questionary.select(
        "What is your level of risk?",
        choices=["Low", "Moderate", "High", "Speculative"],
        instruction = '(Use arrow keys)',
        use_indicator= True,
        style=custom_style
    ).ask()
    
    investment_strategy = questionary.select(
        "What do you want to do with this investment?",
        choices=["Income", "Growth", "Value", "Income/Growth", "Income/Value", "Growth/Value", "Income/Growth/Value"],
        instruction = '(Use arrow keys)',
        use_indicator= True,
        style=custom_style
    ).ask()
    
    investment_length = questionary.select(
        "How long do you plan to invest the money in years?",
        choices=["0-1", "2-4", "5-9", "10+"],
        instruction = '(Use arrow keys)',
        use_indicator= True,
        style=custom_style
    ).ask()
    
    insert_data = """
    INSERT INTO client (
        'full_name', 'phone_number', 'email_address', 'annual_income', 'investing_experience', 'investment_amount', 'annual_expenses', 'income_stability', 'risk_level', 
        'investment_strategy', 'investment_length')
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    
    engine.execute(insert_data, (full_name, phone_number, email_address, annual_income, investing_experience, investment_amount, annual_expenses, income_stability, risk_level, investment_strategy, investment_length))
    
    return insert_data
