print("hello world")

try:
    #try to see whether this gives an exception
    import blah
except Exception:
    #if there is an exception throw this message
    print("this request module does not exist")
else:
    #if there is no exceptions then excute this code
     print(blah)

print("how are you Ade")