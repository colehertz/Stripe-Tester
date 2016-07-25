# Stripe-Tester
This is a simple tool built in python that enables you to generate test tokens for your stripe account in order to create test charges. In addition, you can perform helpful stripe functions such as listing the last 10 charges. This program is meant to help you when you are using stripe's api for a project.



To get started, make sure to add your stripe key inside main.py



Commands:


list 10 most recent stripe charges 
``` python
ls charges
```


Generates a token using the default stripe test card to return a token
``` python
generate token
```


Perform a $1 test charge with a generated token 
``` python
test charge
```