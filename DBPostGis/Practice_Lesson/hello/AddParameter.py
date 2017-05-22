def make_api_call(foo, bar, baz):
    if baz in ('horse', 'pig', 'dog'):
        return baz(foo)
    else:
        return foo(baz)


# without breaking everyone's existing code.
# Easy...
def new_hotness():


    def make_api_call(foo, bar, baz, *args, **kwargs):


        # Now I can accept any type and number of arguments
        # without worrying about breaking existing code.
        baz_coefficient = kwargs['the_baz']
        # I can even forward my args to a different function without
        # knowing their contents!
        return baz_coefficient in new_function(args)
