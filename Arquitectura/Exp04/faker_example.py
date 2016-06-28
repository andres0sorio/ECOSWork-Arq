from faker import Factory
 
#----------------------------------------------------------------------
def create_fake_stuff(fake):
    """"""
    stuff = ["email", "bs", "address",
             "city", "state",
             "paragraph"]
    for item in stuff:
        print "%s = %s" % (item, getattr(fake, item)())
 
if __name__ == "__main__":
    fake = Factory.create()
    create_fake_stuff(fake)
