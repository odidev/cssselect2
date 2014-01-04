if str is bytes:
    # sys.intern on 2.x only accepts byte strings.
    def intern_unicode(string):
        # TODO do something with weakrefs
        return string
else:  # Python 3
    from sys import intern as intern_unicode
