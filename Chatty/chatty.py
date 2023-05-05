# Twitter: Clutchisback1
# Blog: https://H4cklife.org


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
from colorama.colorama_bin import just_fix_windows_console, Fore
from time import sleep
from progress.spinner import MoonSpinner



# API Key - See steps above to generate yours
API_KEY = 'ENTER API KEY HERE'
openai.api_key = API_KEY


# Argument Variables
parser = argparse.ArgumentParser()
parser.add_argument('-q', '--query', help='Use -q to ask ChatGPT a question', dest='query')
parser.add_argument('-o', '--output', help='Use -f to output to a file', dest='outfile')
parser.add_argument('-s', '--session', help='Use -s to begin a chat session with ChatGpt', dest='session', action='store_true')
args = parser.parse_args()

# Argument Mapping
varquery = args.query
ouptut_file = args.outfile
convo = args.session
 



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


# Loading Bar
def loadingbar2():
  with MoonSpinner('Processing…') as bar:
    for i in range(100):
        sleep(0.07)
        bar.next()


# Chat GPT API Call and Output 
def gpt_output():
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": str(varquery)}
          ]
      )

  # Assigns Ouput to a Variable
  message = response.choices[0]['message']
  output = str(message['content'])
  
  # No input handling
  if varquery == None and convo == False:
    banner() ; str(parser.print_help())

  # Write output to file and print content
  elif bool(ouptut_file) == True:
    loadingbar2()
    with open(ouptut_file, 'w') as file:
      print(Fore.LIGHTBLUE_EX + '😈 Chatty: ' + output + ' 📢')
      file.write(output)
 

 # Session Logic
  elif convo == True:
    while convo == True:
      session_query = input('Ask ChatGPT a Question! ')

      # New ChatGPT Input Source
      response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
          {"role": "user", "content": str(session_query)}
            ]
          )
  # Assigns Ouput to a Variable
      message = response.choices[0]['message']
      session_output = str(message['content'])
      
      loadingbar2()
      # Feel free to customize your Prompt a bit!
      print(Fore.LIGHTBLUE_EX + '😈 Chatty: ' + session_output + ' 📢')
  else:
    loadingbar2()
    # Feel free to customize your Prompt a bit!
    print(Fore.LIGHTBLUE_EX + '😈 Chatty: ' + output + ' 📢')


# Execute!!!
gpt_output()



#  ________________________
# < A1 Ch1pZ 1n Y3r 8r41n >
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
#





# Special Thanks!

# Sweetroll - Podcast days and lifetime brother
# Poncho - My Diet Elon Musk and Death Metal recognition 
# Wraiith75 - For being the example of giving back during his OSCP journey 
# Hexcartel - Teaching me the way and for always presenting opportunities of a lifetime
# Radioboy - FISH, ssh -XD, Denhac and for demonstrating the meaning of being a hacker vs a security professional
# Ch33z_plz - For challenging me, hand holding me, and forcing me to learn! One of my greatest mentors!
# T0w3nTum - Where's Wald0??? days
# DrRayke & Kevin - Always pushing the envelope, training like goku and vegeta, and rediness to teach
# N00py - For allowing me to bring people together on his platform and supporting Coalcast
# Anans3 & Dzolali - For Being Dynamic! 
# Broan - For teaching me Certificate Attacks and getting me Domain Admin everytime I've reached out to him
# Disc0rdantMel0dy - For being supportive of me taking a dump on someones front lawn (figuratively of course 😑)
# Gh0st - For Alignment with key stakeholders and completing Q4 his objectives 🤣 - One of the smartest people I know!
# Oomami - For supporting me in all areas of life - "Nah Nah Nah...."!


