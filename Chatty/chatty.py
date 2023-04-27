### TLDR;

# Generate and add your API Key to the paramter in this script
# If you get errors saying you reached your limit you have to add a payment method
# Shit's super cheap...While developing this I sent quite a few request and it only cost a penny by the time this app was finished...Took a day to write
# Once you have your API key added you should be good to proceed like normal
# If you get missing module errors on the openai import or anything like that just pip install it


### Generating the Chat GPT API Key Instructions and using it for Chatty

# 1. Go to the ChatGPT website at https://www.chatgpt.com/api/.
# 2. Click on the "Get API Key" button located in the top right corner of the page.
# 3. Sign up for a ChatGPT account by providing your name, email address, and a password. If you already have an account, log in with your credentials.
# 4. Once you have signed up or logged in, you will be redirected to the API key generation page.
# 5. You will be prompted to choose a package for your API key. Select the package that best suits your needs and click on the "Subscribe" button.
# 6. Enter your payment information...It's super cheap trust me...One day of use while developing this tool only cost me a penny
# 7. After completing the payment process, you will be redirected to the API key generation page.
# 8. Your API key will be displayed on the page, along with instructions on how to use it.

# Note: Please keep your API key secure and do not share it with unauthorized personnel. To ensure that your data is protected, please follow the best practices for API key management.

##################################################################################################################################################################################

import openai
import argparse
import warnings
from colorama.colorama_bin import just_fix_windows_console, Fore, Back, Style


# Argument Variables
parser = argparse.ArgumentParser()
parser.add_argument('-q', '--query', help='Use -q to ask ChatGPT a question', dest='query')
args = parser.parse_args()


# Argument Mapping
varquery = args.query


# Banner with Color

def banner():
  varbanner = '''
   ___  _             _    _          
  / __\| |__    __ _ | |_ | |_  _   _ 
 / /   | '_ \  / _` || __|| __|| | | |
/ /___ | | | || (_| || |_ | |_ | |_| |
\____/ |_| |_| \__,_| \__| \__| \__, |
                                |___/ 
'''

  # Assign Help Menu to Variable and colorize banner output
  
  print(Fore.LIGHTYELLOW_EX + str(varbanner))
  #print(Style.NORMAL + str(parser.print_help()))
  

varhelpmenu = parser.print_help()


# API Key - See steps above to generate yours
API_KEY = 'ADD YOUR API KEY HERE'
openai.api_key = API_KEY


# Chat GPT API Call and Output 
def gpt_output():
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": str(varquery)}
          ]
      )
  message = response.choices[0]['message']
  print("{}: {}".format(message['role'], message['content']))

# No input handling
if varquery == None or varquery == '':
  banner() ; Fore.RESET + str(varhelpmenu)
else:
  # Print Chat GPT Output
  gpt_output()


#  ________________________
# < A1 CH1PS 1N Y0Ur 8r41N >
#  ------------------------
#    \      {
#     \  }   }   {
#       {   {  }  }
#        }   }{  {
#       {  }{  }  }
#      ( }{ }{  { )
#     .-{   }   }-.
#    ( ( } { } { } )
#    |`-.._____..-'|
#    |             ;--.
#    |   (__)     (__  \
#    |   (oo)      | )  )
#    |    \/       |/  /
#    |             /  /
#    |            (  /
#    \             y'
#     `-.._____..-'
