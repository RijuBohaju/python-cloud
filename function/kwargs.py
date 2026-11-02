#**kwargs allows you to pass multiple keyword arguments.
def user_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")
user_info(
    name="Williams",
    age=50,
    skill="Python"
)
