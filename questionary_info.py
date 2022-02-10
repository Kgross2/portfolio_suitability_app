# import required libraries



import questionary
import fire
from questionary.constants import NO, YES, YES_OR_NO
import sqlalchemy
   
# Define the clients general information

def survey_questions():
    # contact information
    full_name = questionary.text("What's your name?").ask()
    phone_number = questionary.text("What's your phone number?, no dashes only number").ask()
    email_address = questionary.text("What's your email address?").ask()
    #income questions
    annual_income = questionary.text("What's your annual income?").ask()
    investing_experience = questionary.text("How many years of investing experience do you have?").ask()
    investment_amount = questionary.text("What is the amount you wish to start investing?").ask()
    annual_expenses = questionary.text("What are your annual expenses?").ask()
    income_stability = questionary.text(f"Is your source of income stable, YES or NO").ask(YES_OR_NO)
    
    annual_income = float(annual_income)
    investing_experience = int(investing_experience)
    investment_amount = float(investment_amount)
    annual_expenses = float(annual_expenses)
    income_stability = str(income_stability)
    
    # Investing background

    risk_level = questionary.select(
        "What is your level of risk?",
        choices=["Low", "Moderate", "High", "Speculative"],
    ).ask()
    
    investment_strategy = questionary.select(
        "What do you want to do with this investment.",
        choices=["Income", "Growth", "Value", "Income/Growth", "Income/Value", "Growth/Value", "Income/Growth/Value"],
    ).ask()
    
    investment_length = questionary.select(
        "How long do you plan to invest the money",
        choices=["0-1", "2-4yrs", "5-9yrs", "10yrs+"],
    ).ask()

    risk_level = str(risk_level)
    investment_strategy = str(investment_strategy)
    investment_length = str(investment_length)
    

    insert_data = """
    INSERT INTO client (
        'full_name', 'phone_number', 'email_address', 'annual_income', 'investing_experience', 'investment_amount', 'annual_expenses', 'income_stability', 'risk_level', 
        'investment_strategy', 'investment_length')
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    
    engine.execute(insert_data, (full_name, phone_number, email_address, annual_income, investing_experience, investment_amount, annual_expenses, income_stability, risk_level, investment_strategy, investment_length))
    
    return insert_data









    







