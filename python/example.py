import whatrunswhere

def test_run():

    print "*" * 80
    print "WhatRunsWhere API client example"
    print "*" * 80
    print ""

    token = raw_input("Please enter your API token: ")
    client = whatrunswhere.WhatRunsWhere(token)
    client.set_filter("country", "United States")

    api_methods = [method for method in dir(client)
        if callable(getattr(client, method))
            and not method.startswith("set")
            and not method.startswith("_")]
    method_listing = dict([(index, method)
            for index, method in enumerate(api_methods, start=1)])

    print ""
    print "Please select a function to test: "

    for index, method in method_listing.items():
        print "- ({0}) {1}".format(index, method)

    print ""
    selection = int(raw_input("> "))
    print ""

    if method_listing.get(selection):
        selected_fn = method_listing.get(selection)
        fn = getattr(client, selected_fn)
    else:
        print "Invalid selection."
        return

    print ""
    print "Please enter a resource name (domain name):"
    print ""
    domain = raw_input("> ")
    print ""

    result = fn(domain)

    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(result)


if __name__ == "__main__":
    test_run()
