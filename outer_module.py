from test_hello import sayhi

def outer_task():
    sayhi()
    print "woohooo"
    
outer_task()