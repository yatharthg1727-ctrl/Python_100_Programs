# Keyword Variable Arguments (**kwargs): Create a function that displays user profile details passed as arbitrary keyword pairs.

def profile(**kwargs):

    for key, value in kwargs.items():

        print(key, ":", value)

profile(name="Yatharth Jain", age = 19, post = "CEO")