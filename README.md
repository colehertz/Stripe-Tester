# Stripe-Tester
This is a simple tool built in python that enables you to generate test tokens for your stripe account in order to create test charges. In addition, you can perform helpful stripe functions such as listing the last 10 charges. This program is meant to help you when you are using stripe's api for a project.


Commands:
''' python
ls charges
'''
1. ls charges - lists 10 most recent stripe charges 
2. generate token - uses the default stripe test card to return a token
3. test charge - performs a $1 test charge with a generated token 