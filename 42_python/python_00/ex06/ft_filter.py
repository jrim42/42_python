def ft_filter(function, iterable):
    """
    Recode your own ft_filter, it should behave like the original built-in function
    (it should return the same thing as "print(filter.__doc__)"), you should use list comprehensions to recode your ft_filter.
    
    Of course using the original filter built-in is forbidden
    """
    return [item for item in iterable if function(item)]