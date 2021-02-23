# Solution by PauloBA

def evaporator(content, evap_per_day, threshold):
    use = content
    c = 0
    while use > content*threshold/100:
        use = use - (use * (evap_per_day/100))
        c = c + 1
    return c

print(evaporator(10, 10, 5))